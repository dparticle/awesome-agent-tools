"""GitHub REST client.

Design constraints that shaped this module:

* **Unauthenticated budget is small** — 60 core requests/hour and 10 searches
  per minute. The daily job therefore caches every response on disk and
  budgets its calls explicitly instead of discovering the limit by hitting 403.
* **Authentication is optional** — ``GITHUB_TOKEN`` raises the limits to
  5000/hour and 30 searches/minute. The workflow supplies it; local runs and
  forks still work without one.
* **Every call must be resumable** — a job killed mid-run must not lose the
  metadata it already paid for, so cache writes happen immediately.
"""

from __future__ import annotations

import base64
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .util import CACHE_DIR, LOG, read_json, write_json

API_ROOT = "https://api.github.com"
RAW_ROOT = "https://raw.githubusercontent.com"

# README names we try, in order of preference.
README_CANDIDATES = (
    "README.md",
    "README.MD",
    "readme.md",
    "Readme.md",
    "README.rst",
    "README.markdown",
    "README.txt",
    "README",
    "README_EN.md",
    "README.en.md",
    "docs/README.md",
    ".github/README.md",
)

#: Chinese README filenames, most common first. Measured against the indexed
#: corpus, these three cover nearly every project that ships one; the rest of
#: the list is kept for reference but not probed, because each miss is a wasted
#: round trip and the probe runs for every candidate on every crawl.
CHINESE_README_CANDIDATES = (
    "README.zh-CN.md",
    "README_CN.md",
    "README.zh.md",
    "README-CN.md",
    "README.zh_CN.md",
    "docs/README.zh-CN.md",
    "README_CH.md",
    "README.chs.md",
    "README.zh-Hans.md",
)

#: Probed filenames, in order. Deliberately short.
CHINESE_PROBE_CANDIDATES = CHINESE_README_CANDIDATES[:3]

#: Branches tried when probing. ``HEAD`` resolves to the default branch on
#: raw.githubusercontent.com, so trying ``main``/``master`` as well tripled the
#: request count for no benefit — the first full crawl spent 29 minutes almost
#: entirely on 404s.
CHINESE_PROBE_BRANCHES = ("HEAD",)


class RateLimitExhausted(RuntimeError):
    """Raised when a budget would be exceeded before making the call."""


@dataclass
class Budget:
    """A self-imposed ceiling, always stricter than GitHub's own."""

    core: int = 45
    search: int = 25
    used_core: int = 0
    used_search: int = 0

    def spend_core(self, n: int = 1) -> None:
        if self.used_core + n > self.core:
            raise RateLimitExhausted(f"core budget spent ({self.used_core}/{self.core})")
        self.used_core += n

    def spend_search(self, n: int = 1) -> None:
        if self.used_search + n > self.search:
            raise RateLimitExhausted(f"search budget spent ({self.used_search}/{self.search})")
        self.used_search += n

    @property
    def remaining_core(self) -> int:
        return max(0, self.core - self.used_core)

    @property
    def remaining_search(self) -> int:
        return max(0, self.search - self.used_search)

    def as_dict(self) -> dict[str, int]:
        return {
            "core": self.core,
            "core_used": self.used_core,
            "search": self.search,
            "search_used": self.used_search,
        }


@dataclass
class GitHubClient:
    """Small, cache-first GitHub REST wrapper."""

    token: str | None = None
    budget: Budget = field(default_factory=Budget)
    cache_dir: Any = CACHE_DIR
    cache_ttl_seconds: int = 60 * 60 * 6
    offline: bool = False
    _search_window: list[float] = field(default_factory=list, repr=False)

    def __post_init__(self) -> None:
        if self.token is None:
            self.token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or None
        if self.token:
            # Authenticated: GitHub allows 5000 core/h and 30 search/min.
            self.budget.core = max(self.budget.core, 400)
            self.budget.search = max(self.budget.search, 60)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    # -- internals ---------------------------------------------------------

    @property
    def authenticated(self) -> bool:
        return bool(self.token)

    def _headers(self) -> dict[str, str]:
        headers = {
            "User-Agent": "awesome-agent-tools/1.0 (+https://github.com/)",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _cache_path(self, key: str):
        safe = urllib.parse.quote(key, safe="")
        return self.cache_dir / f"{safe[:180]}.json"

    def _cache_get(self, key: str) -> Any | None:
        payload = read_json(self._cache_path(key))
        if not isinstance(payload, dict):
            return None
        age = time.time() - float(payload.get("_cached_at", 0))
        if age > self.cache_ttl_seconds:
            return None
        return payload.get("data")

    def _cache_put(self, key: str, data: Any) -> None:
        write_json(self._cache_path(key), {"_cached_at": time.time(), "data": data})

    def _throttle_search(self) -> None:
        """Keep at most ``search_per_minute`` searches inside a rolling minute."""
        per_minute = 28 if self.authenticated else 9
        now = time.time()
        self._search_window = [t for t in self._search_window if now - t < 60]
        if len(self._search_window) >= per_minute:
            sleep_for = 61 - (now - self._search_window[0])
            if sleep_for > 0:
                LOG.info("search throttle: sleeping %.1fs", sleep_for)
                time.sleep(sleep_for)
            now = time.time()
            self._search_window = [t for t in self._search_window if now - t < 60]
        self._search_window.append(now)

    def _request(self, url: str, *, retries: int = 3) -> Any:
        last_error: Exception | None = None
        for attempt in range(retries):
            try:
                req = urllib.request.Request(url, headers=self._headers())
                with urllib.request.urlopen(req, timeout=45) as response:
                    return json.loads(response.read())
            except urllib.error.HTTPError as exc:
                body = exc.read()[:400].decode("utf-8", "replace")
                # 403/429 are usually secondary rate limits — back off and retry.
                if exc.code in (403, 429) and attempt < retries - 1:
                    wait = 15 * (attempt + 1)
                    LOG.warning("HTTP %s on %s — backing off %ss", exc.code, url, wait)
                    time.sleep(wait)
                    last_error = RuntimeError(f"HTTP {exc.code}: {body}")
                    continue
                if exc.code == 404:
                    return None
                raise RuntimeError(f"HTTP {exc.code} for {url}: {body}") from exc
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last_error = exc
                if attempt < retries - 1:
                    time.sleep(3 * (attempt + 1))
                    continue
        raise RuntimeError(f"request failed for {url}: {last_error}")

    # -- public API --------------------------------------------------------

    def get_repo(self, full_name: str, *, refresh: bool = False) -> dict[str, Any] | None:
        """Fetch repository metadata, with redirect handling.

        ``sst/opencode`` was renamed to ``anomalyco/opencode``; the API answers
        301 and urllib follows it, so the returned payload carries the *new*
        ``full_name``. Callers must trust the payload over their input.
        """
        cache_key = f"repo::{full_name.lower()}"
        if not refresh:
            cached = self._cache_get(cache_key)
            if cached is not None:
                return cached or None
        if self.offline:
            return None
        self.budget.spend_core()
        data = self._request(f"{API_ROOT}/repos/{full_name}")
        if isinstance(data, dict) and data.get("full_name"):
            # Cache under both the requested and the canonical name.
            self._cache_put(cache_key, data)
            canonical = data["full_name"].lower()
            if canonical != full_name.lower():
                self._cache_put(f"repo::{canonical}", data)
        return data if isinstance(data, dict) else None

    def get_repos(self, full_names: list[str], *, refresh: bool = False) -> dict[str, dict]:
        """Fetch many repos, skipping ones already cached."""
        out: dict[str, dict] = {}
        for name in full_names:
            try:
                repo = self.get_repo(name, refresh=refresh)
            except RateLimitExhausted:
                LOG.warning("core budget exhausted; %d repos left unfetched", len(full_names))
                break
            except RuntimeError as exc:
                LOG.warning("repo %s failed: %s", name, exc)
                continue
            if repo:
                out[repo["full_name"].lower()] = repo
        return out

    def search_repositories(
        self,
        query: str,
        *,
        per_page: int = 30,
        sort: str = "stars",
        order: str = "desc",
        page: int = 1,
    ) -> list[dict[str, Any]]:
        cache_key = f"search::{query}::{sort}::{order}::{per_page}::{page}"
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cached
        if self.offline:
            return []
        self._throttle_search()
        self.budget.spend_search()
        params = {"q": query, "per_page": per_page, "sort": sort, "order": order, "page": page}
        url = f"{API_ROOT}/search/repositories?" + urllib.parse.urlencode(params)
        data = self._request(url)
        items = (data or {}).get("items", []) if isinstance(data, dict) else []
        self._cache_put(cache_key, items)
        return items

    def get_readme(self, full_name: str, *, refresh: bool = False) -> tuple[str, str]:
        """Return ``(text, source)`` for a repo's README.

        Tries ``raw.githubusercontent.com`` first: it is not part of the REST
        rate limit, so a 60-request budget can still hydrate hundreds of
        READMEs. Falls back to the contents API when raw 404s (non-default
        branch layouts, unusual filenames).
        """
        cache_key = f"readme::{full_name.lower()}"
        if not refresh:
            cached = self._cache_get(cache_key)
            if isinstance(cached, dict) and cached.get("text"):
                return cached["text"], cached.get("source", "cache")
        if self.offline:
            return "", "offline"

        for branch in ("HEAD", "main", "master"):
            for name in README_CANDIDATES:
                url = f"{RAW_ROOT}/{full_name}/{branch}/{name}"
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": self._headers()["User-Agent"]})
                    with urllib.request.urlopen(req, timeout=30) as response:
                        raw = response.read()
                except urllib.error.HTTPError:
                    continue
                except Exception:  # noqa: BLE001 - network flake, try next candidate
                    continue
                text = raw.decode("utf-8", "replace")
                if text.strip():
                    self._cache_put(cache_key, {"text": text, "source": f"raw:{branch}/{name}"})
                    return text, f"raw:{branch}/{name}"

        # Fallback: contents API (costs one core request).
        try:
            self.budget.spend_core()
        except RateLimitExhausted:
            return "", "budget-exhausted"
        try:
            data = self._request(f"{API_ROOT}/repos/{full_name}/readme")
        except RuntimeError:
            data = None
        if isinstance(data, dict) and data.get("content"):
            try:
                text = base64.b64decode(data["content"]).decode("utf-8", "replace")
            except (ValueError, TypeError):
                return "", "decode-failed"
            self._cache_put(cache_key, {"text": text, "source": "contents-api"})
            return text, "contents-api"
        return "", "missing"

    def get_chinese_readme(self, full_name: str, *, refresh: bool = False) -> tuple[str, str]:
        """Return ``(text, source)`` for a repo's Chinese README, if it has one.

        Used so the Chinese index quotes the project's *own* Chinese wording.
        Machine-translating the English README would put claims in the project's
        mouth that it never made, which is exactly the failure this list exists
        to avoid.

        Costs one request per candidate filename on a miss, so the probe list is
        deliberately short and the result — including "no Chinese README" — is
        cached.
        """
        cache_key = f"readme-zh::{full_name.lower()}"
        if not refresh:
            cached = self._cache_get(cache_key)
            if isinstance(cached, dict):
                return cached.get("text", ""), cached.get("source", "cache")
        if self.offline:
            return "", "offline"

        # Probed concurrently: three sequential round trips per repo, for every
        # repo, dominated the crawl's wall time. The requests are independent
        # and the result is cached either way, so there is no reason to
        # serialise them.
        def fetch(name: str) -> tuple[str, str]:
            url = f"{RAW_ROOT}/{full_name}/HEAD/{name}"
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": self._headers()["User-Agent"]}
                )
                with urllib.request.urlopen(req, timeout=15) as response:
                    return response.read().decode("utf-8", "replace"), f"raw:HEAD/{name}"
            except Exception:  # noqa: BLE001 - a miss is the common case
                return "", ""

        with ThreadPoolExecutor(max_workers=len(CHINESE_PROBE_CANDIDATES)) as pool:
            results = list(pool.map(fetch, CHINESE_PROBE_CANDIDATES))

        # Prefer the earliest candidate in preference order, not the fastest.
        for text, source in results:
            if text and _chinese_ratio(text) >= 0.15:
                self._cache_put(cache_key, {"text": text, "source": source})
                return text, source

        self._cache_put(cache_key, {"text": "", "source": "missing"})
        return "", "missing"

    def prefetch_chinese_readmes(self, full_names: list[str], *, workers: int = 16) -> int:
        """Warm the Chinese-README cache for many repos concurrently.

        The main crawl loop is serial, so probing three filenames per repo inside
        it added a per-repo round trip to every candidate and stretched a run
        from ~35s to ~29min. Probing up front, concurrently, and letting the
        loop read the cache removes that cost from the critical path.

        Returns the number of repos that turned out to have Chinese docs.
        """
        if self.offline or not full_names:
            return 0
        found = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for text, _source in pool.map(self.get_chinese_readme, full_names):
                if text:
                    found += 1
        return found

    def rate_limit(self) -> dict[str, Any]:
        if self.offline:
            return {}
        try:
            return self._request(f"{API_ROOT}/rate_limit") or {}
        except RuntimeError as exc:
            LOG.warning("rate_limit probe failed: %s", exc)
            return {}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _chinese_ratio(text: str) -> float:
    """Share of characters that are CJK, ignoring markup and code.

    Used to tell a genuine Chinese README from an English file with a
    ``README.zh-CN.md`` name, or a stub that only links to the English version.
    """
    stripped = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    stripped = re.sub(r"<[^>]+>", " ", stripped)
    stripped = re.sub(r"https?://\S+", " ", stripped)
    letters = [ch for ch in stripped if not ch.isspace()]
    if len(letters) < 200:
        return 0.0
    cjk = sum(1 for ch in letters if "\u4e00" <= ch <= "\u9fff")
    return cjk / len(letters)


def parse_iso(value: str | None) -> datetime | None:
    """Parse an ISO-8601 timestamp or a bare date into an **aware** datetime.

    GitHub returns ``2026-10-07T13:15:32Z`` for timestamps, but our own history
    files store bare dates (``2026-10-07``). A bare date parses to a *naive*
    datetime, and subtracting that from ``datetime.now(timezone.utc)`` raises
    ``TypeError`` — so everything is normalised to UTC here.
    """
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed
