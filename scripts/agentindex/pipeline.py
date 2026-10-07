"""The daily pipeline: discover -> fetch -> analyse -> score -> eliminate -> persist.

State lives in ``data/``:

* ``data/entries/<owner>__<repo>.json`` — one file per tool, the full record.
  Per-tool files keep git diffs readable: a daily run touches only the tools
  whose numbers actually moved.
* ``data/history/<owner>__<repo>.json`` — a rolling star snapshot series, which
  is what makes real momentum measurable instead of guessed. The first run has
  no history and falls back to lifetime velocity; from the second run onward
  growth is measured rather than inferred.
* ``data/index.json`` — the aggregate the renderer and any downstream tool reads.
* ``data/graveyard.json`` — retired tools and the edges that retired them.

API budget
----------
GitHub's search endpoint returns *complete repository objects*, so a search
result is used directly as metadata and the expensive
``/repos/{owner}/{repo}`` call is reserved for seeds (which have no search
payload) and for runs that explicitly ask for verified numbers. This is what
lets the unauthenticated 60-calls/hour budget hydrate several hundred repos.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from . import SCHEMA_VERSION
from .discover import (
    EXCLUDED_REPOS,
    IDENTITY_PROSE_CHARS,
    Candidate,
    assign_category,
    discover,
    is_on_topic,
    load_categories,
    load_discovery_config,
)
from .github import GitHubClient, RateLimitExhausted, now_iso, parse_iso
from .readme_analysis import ReadmeAnalysis, analyse
from .scoring import (
    assign_tier,
    compute_momentum,
    evaluate_gates,
    health_score,
    load_thresholds,
)
from .supersede import (
    STATE_ACTIVE,
    ToolFacts,
    apply_manual_overrides,
    build_edges,
    resolve_states,
)
from .util import (
    CONFIG_DIR,
    DATA_DIR,
    LOG,
    read_json,
    slugify,
    write_json,
)

ENTRIES_DIR = DATA_DIR / "entries"
HISTORY_DIR = DATA_DIR / "history"
INDEX_PATH = DATA_DIR / "index.json"
GRAVEYARD_PATH = DATA_DIR / "graveyard.json"

#: Fields we require from a metadata payload before trusting it.
REQUIRED_META_FIELDS = ("full_name", "stargazers_count", "pushed_at", "created_at")


def entry_path(full_name: str):
    owner, _, repo = full_name.partition("/")
    return ENTRIES_DIR / f"{slugify(owner)}__{slugify(repo)}.json"


def history_path(full_name: str):
    owner, _, repo = full_name.partition("/")
    return HISTORY_DIR / f"{slugify(owner)}__{slugify(repo)}.json"


# --------------------------------------------------------------------------
# History
# --------------------------------------------------------------------------


def load_history(full_name: str) -> list[dict[str, Any]]:
    data = read_json(history_path(full_name), default=[]) or []
    return data if isinstance(data, list) else []


def append_history(
    full_name: str, stars: int, extras: dict[str, Any] | None = None
) -> list[dict[str, Any]]:
    """Append today's snapshot, keeping at most one point per day."""
    today = datetime.now(timezone.utc).date().isoformat()
    series = [p for p in load_history(full_name) if p.get("date") != today]
    point: dict[str, Any] = {"date": today, "stars": int(stars)}
    if extras:
        point.update(extras)
    series.append(point)
    series.sort(key=lambda p: p.get("date", ""))
    series = series[-400:]
    write_json(history_path(full_name), series)
    return series


# --------------------------------------------------------------------------
# Stats
# --------------------------------------------------------------------------


@dataclass
class PipelineStats:
    discovered: int = 0
    considered: int = 0
    prefetched: int = 0
    accepted: int = 0
    rejected: int = 0
    readme_ok: int = 0
    readme_missing: int = 0
    api_metadata_calls: int = 0
    supersede_edges: int = 0
    budget: dict[str, int] = field(default_factory=dict)
    duration_s: float = 0.0
    errors: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "discovered": self.discovered,
            "considered": self.considered,
            "prefiltered_out": self.prefetched,
            "accepted": self.accepted,
            "rejected": self.rejected,
            "readme_ok": self.readme_ok,
            "readme_missing": self.readme_missing,
            "api_metadata_calls": self.api_metadata_calls,
            "supersede_edges": self.supersede_edges,
            "budget": self.budget,
            "duration_s": round(self.duration_s, 1),
            "errors": self.errors[:40],
        }


# --------------------------------------------------------------------------
# Pipeline
# --------------------------------------------------------------------------


def run_pipeline(
    client: GitHubClient,
    *,
    limit: int | None = None,
    refresh: bool = False,
    dry_run: bool = False,
    verify_metadata: bool = False,
    allow_shrink: bool = False,
) -> tuple[dict[str, Any], PipelineStats]:
    started = time.time()
    stats = PipelineStats()
    thresholds = load_thresholds()
    discovery_cfg = load_discovery_config()
    categories = load_categories()
    categories_by_id = {c["id"]: c for c in categories}
    all_category_ids = list(categories_by_id)
    overrides = read_json(CONFIG_DIR / "overrides.json", default={}) or {}

    # -- 1. discover ------------------------------------------------------
    candidates = discover(client)
    stats.discovered = len(candidates)

    # Priority: seeds first (readers ask about these by name), then traction,
    # with rising-pass discoveries boosted so a dark horse is never crowded
    # out by the long tail of a star-sorted query.
    def priority(c: Candidate) -> tuple[int, float]:
        meta = c.metadata or {}
        stars = float(meta.get("stargazers_count") or 0)
        if c.source == "seed":
            return (0, -stars)
        if c.source == "rising":
            return (1, -stars)
        return (2, -stars)

    candidates.sort(key=priority)

    max_candidates = int(discovery_cfg.get("max_candidates", 400))
    if limit:
        candidates = candidates[:limit]
    elif len(candidates) > max_candidates:
        LOG.info("capping %d candidates at max_candidates=%d", len(candidates), max_candidates)
        candidates = candidates[:max_candidates]
    stats.considered = len(candidates)
    LOG.info("pipeline: %d candidates to consider", len(candidates))

    # -- 2. metadata + README --------------------------------------------
    entries: dict[str, dict[str, Any]] = {}
    rejected: list[dict[str, Any]] = []
    prefilter = discovery_cfg.get("prefilter", {})

    for i, candidate in enumerate(candidates, 1):
        provisional = candidate.metadata or {}

        # Cheap rejection from the search payload, before any further work.
        if provisional and candidate.source != "seed":
            reason = _prefilter_reason(provisional, prefilter)
            if reason:
                rejected.append(
                    {
                        "full_name": candidate.full_name,
                        "reasons": [reason],
                        "stars": provisional.get("stargazers_count", 0),
                    }
                )
                stats.rejected += 1
                stats.prefetched += 1
                continue

        repo, meta_source = _resolve_metadata(
            client, candidate, refresh=refresh, verify=verify_metadata, stats=stats
        )
        if not repo:
            stats.errors.append(f"{candidate.full_name}: metadata unavailable")
            continue

        full_name = repo["full_name"]

        if repo.get("archived") or repo.get("disabled"):
            rejected.append(
                {
                    "full_name": full_name,
                    "reasons": [
                        "repository is archived" if repo.get("archived") else "repository is disabled"
                    ],
                    "stars": repo.get("stargazers_count", 0),
                }
            )
            stats.rejected += 1
            continue

        try:
            body, source = client.get_readme(full_name, refresh=refresh)
        except Exception as exc:  # noqa: BLE001 - never let one README kill the run
            body, source = "", f"error:{type(exc).__name__}"

        analysis = analyse(full_name, body, repo.get("description") or "", source) if body else None
        if analysis and analysis.readme_chars:
            stats.readme_ok += 1
        else:
            stats.readme_missing += 1

        momentum = compute_momentum(repo, load_history(full_name), thresholds)

        gate = evaluate_gates(repo, analysis, momentum, thresholds)
        if not gate.passed:
            rejected.append(
                {
                    "full_name": full_name,
                    "reasons": gate.reasons,
                    "stars": repo.get("stargazers_count", 0),
                    "stars_per_day": round(momentum.stars_per_day, 2),
                }
            )
            stats.rejected += 1
            continue

        assert analysis is not None

        # Relevance: keyword search pulls in adjacent-but-unrelated repos that
        # match a capability pattern incidentally. Judge them on their identity
        # (name, description, opening prose), not on stray doc mentions.
        identity = " ".join(
            [
                repo.get("name") or "",
                repo.get("description") or "",
                analysis.summary_en or "",
                body[:IDENTITY_PROSE_CHARS],
            ]
        )
        # A seed is a human-curated nomination, so it bypasses the automated
        # relevance judgement — a maintainer has already asserted it belongs.
        # It still has to clear every quality gate.
        excluded = full_name.lower() in EXCLUDED_REPOS
        if excluded:
            rejected.append(
                {
                    "full_name": full_name,
                    "reasons": ["explicitly excluded in config (not an agent tool)"],
                    "stars": repo.get("stargazers_count", 0),
                }
            )
            stats.rejected += 1
            continue

        if candidate.source != "seed" and not is_on_topic(analysis, identity):
            rejected.append(
                {
                    "full_name": full_name,
                    "reasons": [
                        "not about AI agents "
                        f"(capabilities: {', '.join(analysis.capabilities[:6]) or 'none'})"
                    ],
                    "stars": repo.get("stargazers_count", 0),
                }
            )
            stats.rejected += 1
            continue

        # A rising-pass candidate has no category yet: let every category
        # compete for it on the strength of its README. Seeds are trusted, so
        # they only need a single mention.
        candidate_categories = candidate.categories or all_category_ids
        cat_id, matched, cat_score = assign_category(
            candidate_categories,
            analysis,
            categories_by_id,
            min_hits=1 if candidate.source == "seed" else 2,
        )
        if not cat_id:
            rejected.append(
                {
                    "full_name": full_name,
                    "reasons": [
                        "no category matched the README's capabilities "
                        f"(detected: {', '.join(analysis.capabilities[:6]) or 'none'})"
                    ],
                    "stars": repo.get("stargazers_count", 0),
                }
            )
            stats.rejected += 1
            continue

        score, components = health_score(repo, analysis, momentum, thresholds)
        tier = assign_tier(score, thresholds)

        if not dry_run:
            append_history(full_name, repo.get("stargazers_count", 0))

        entries[full_name.lower()] = _build_entry(
            repo=repo,
            analysis=analysis,
            momentum=momentum,
            score=score,
            components=components,
            tier=tier,
            category=cat_id,
            matched_capabilities=matched,
            category_score=cat_score,
            source=candidate.source,
            seed_reason=candidate.seed_reason,
            also_in=[c for c in candidate.categories if c != cat_id],
            metadata_source=meta_source,
        )
        stats.accepted += 1

        if i % 25 == 0:
            LOG.info(
                "  %d/%d processed (accepted=%d rejected=%d, core_used=%d)",
                i,
                len(candidates),
                stats.accepted,
                stats.rejected,
                client.budget.used_core,
            )

    # -- 3. elimination ---------------------------------------------------
    facts = [ToolFacts.from_entry(e, e.get("category", "")) for e in entries.values()]
    edges = apply_manual_overrides(build_edges(facts, thresholds), overrides)
    stats.supersede_edges = len(edges)
    states = resolve_states(entries, edges, overrides, thresholds)

    for full_name, entry in entries.items():
        info = states.get(full_name, {})
        entry["lifecycle"] = {
            "state": info.get("state", STATE_ACTIVE),
            "note_en": info.get("note_en", ""),
            "note_zh": info.get("note_zh", ""),
            "superseded_by": info.get("superseded_by", ""),
        }
        if info.get("supersede_edge"):
            entry["lifecycle"]["supersede"] = info["supersede_edge"]

    # -- 4. persist -------------------------------------------------------
    stats.duration_s = time.time() - started
    stats.budget = client.budget.as_dict()

    # Safety valve. If the network is down, a rate limit hit, or GitHub changes
    # shape, the run finds nothing and would happily overwrite a good index with
    # an empty one — and the daily workflow would commit that. Refuse instead.
    previous = read_json(INDEX_PATH, default={}) or {}
    previous_count = int((previous.get("counts") or {}).get("tools") or 0)
    if not allow_shrink and not dry_run:
        refusal = _check_shrink_safety(stats.accepted, previous_count, stats)
        if refusal:
            LOG.error("REFUSING TO WRITE: %s", refusal)
            LOG.error("the existing index (%d tools) was left untouched", previous_count)
            stats.errors.append(f"write refused: {refusal}")
            return previous or _build_index(entries, edges, rejected, stats, categories), stats

    if not dry_run:
        _prune_stale_entries(entries)
        for entry in entries.values():
            write_json(entry_path(entry["full_name"]), entry)

    index = _build_index(entries, edges, rejected, stats, categories)
    if not dry_run:
        write_json(INDEX_PATH, index)
        write_json(GRAVEYARD_PATH, _build_graveyard(entries, edges))

    LOG.info(
        "pipeline done: accepted=%d rejected=%d edges=%d core_calls=%d in %.1fs",
        stats.accepted,
        stats.rejected,
        stats.supersede_edges,
        stats.api_metadata_calls,
        stats.duration_s,
    )
    return index, stats


def _resolve_metadata(
    client: GitHubClient,
    candidate: Candidate,
    *,
    refresh: bool,
    verify: bool,
    stats: PipelineStats,
) -> tuple[dict[str, Any], str]:
    """Return ``(repo, source)`` for a candidate.

    Prefers the search payload, which is complete enough for every downstream
    calculation, and only pays for an API call when the payload is missing
    fields or verification was requested.
    """
    provisional = candidate.metadata or {}
    complete = all(provisional.get(f) is not None for f in REQUIRED_META_FIELDS)

    if complete and not verify and candidate.source != "seed":
        return provisional, "search"

    try:
        repo = client.get_repo(candidate.full_name, refresh=refresh)
        stats.api_metadata_calls += 1
    except RateLimitExhausted:
        stats.errors.append("core rate budget exhausted during metadata fetch")
        if complete:
            LOG.warning("core budget exhausted; falling back to search metadata")
            return provisional, "search"
        return {}, ""
    except RuntimeError as exc:
        stats.errors.append(f"{candidate.full_name}: {exc}")
        if complete:
            return provisional, "search"
        return {}, ""

    if not repo:
        # A 404 is not fatal if the search payload is usable (rare rename).
        if complete:
            return provisional, "search"
        return {}, ""
    return repo, "api"


def _prefilter_reason(repo: dict[str, Any], prefilter: dict[str, Any]) -> str:
    """Cheap rejection using only the search payload.

    This exists to protect the API budget: a keyword query returns plenty of
    abandoned and trivial repos, and there is no reason to fetch a README for
    them. It is intentionally looser than :func:`evaluate_gates` — anything
    borderline is passed through so the real gates can judge it with the
    README in hand.
    """
    if not prefilter:
        return ""
    if repo.get("archived") and not prefilter.get("allow_archived", False):
        return "repository is archived"
    if repo.get("disabled"):
        return "repository is disabled"
    if repo.get("fork"):
        return "is a fork"

    stars = int(repo.get("stargazers_count") or 0)
    min_stars = int(prefilter.get("min_stars", 0))
    if min_stars and stars < min_stars:
        return f"only {stars} stars (< pre-filter {min_stars})"

    pushed = parse_iso(repo.get("pushed_at"))
    max_days = int(prefilter.get("max_days_since_push", 0))
    if pushed and max_days:
        days = (datetime.now(timezone.utc) - pushed).days
        if days > max_days:
            return f"no push in {days} days (> pre-filter {max_days})"
    return ""


def _check_shrink_safety(accepted: int, previous_count: int, stats: PipelineStats) -> str:
    """Decide whether writing this run would destroy a good index.

    Returns a refusal reason, or ``""`` to allow the write.

    The scenario this exists for is mundane: GitHub is unreachable, every
    metadata fetch fails, and the run produces zero tools. Without this check
    the daily workflow would commit an empty index and the project would look
    abandoned until someone noticed.
    """
    if previous_count <= 0:
        return ""  # first run — nothing to protect
    if accepted == 0:
        return "this run produced 0 tools (network or API failure?)"
    # A real crawl can legitimately lose tools, but not most of them at once.
    floor = int(previous_count * 0.5)
    if accepted < floor:
        return (
            f"this run produced {accepted} tools, less than half of the "
            f"{previous_count} already indexed"
        )
    # A run that failed on most candidates is untrustworthy even if some passed.
    attempted = stats.considered or 0
    if attempted and len(stats.errors) >= max(5, attempted // 4):
        return f"{len(stats.errors)} of {attempted} candidates errored"
    return ""


def _prune_stale_entries(entries: dict[str, dict[str, Any]]) -> None:
    """Delete per-tool files for tools that are no longer in the index.

    Without this, a tool that gets renamed or dropped leaves an orphan file
    that a later ``git status`` reports as an unexplained deletion.
    """
    keep = {slugify(e["full_name"].partition("/")[0]) + "__" + slugify(e["full_name"].partition("/")[2]) for e in entries.values()}
    if not ENTRIES_DIR.exists():
        return
    for path in ENTRIES_DIR.glob("*.json"):
        if path.stem not in keep:
            LOG.info("pruning stale entry %s", path.name)
            path.unlink(missing_ok=True)


def _build_entry(
    *,
    repo: dict[str, Any],
    analysis: ReadmeAnalysis,
    momentum: Any,
    score: int,
    components: dict[str, float],
    tier: str,
    category: str,
    matched_capabilities: list[str],
    category_score: float,
    source: str,
    seed_reason: str,
    also_in: list[str],
    metadata_source: str = "api",
) -> dict[str, Any]:
    license_info = repo.get("license") or {}
    if isinstance(license_info, str):
        license_info = {"spdx_id": license_info}
    owner = repo.get("owner") or {}
    if isinstance(owner, str):
        owner = {"login": owner}

    return {
        "schema": SCHEMA_VERSION,
        "full_name": repo["full_name"],
        "name": repo.get("name") or repo["full_name"].partition("/")[2],
        "owner": owner.get("login", ""),
        "url": repo.get("html_url") or f"https://github.com/{repo['full_name']}",
        "description": repo.get("description") or "",
        "homepage": repo.get("homepage") or "",
        "category": category,
        "also_in": also_in,
        "matched_capabilities": matched_capabilities,
        "category_score": round(category_score, 2),
        "stars": int(repo.get("stargazers_count") or 0),
        "forks": int(repo.get("forks_count") or 0),
        "open_issues": int(repo.get("open_issues_count") or 0),
        "language": repo.get("language") or "",
        "license": license_info.get("spdx_id") or "",
        "topics": repo.get("topics") or [],
        "created_at": repo.get("created_at"),
        "updated_at": repo.get("updated_at"),
        "pushed_at": repo.get("pushed_at"),
        "archived": bool(repo.get("archived")),
        "is_fork": bool(repo.get("fork")),
        "default_branch": repo.get("default_branch") or "main",
        "age_days": _days_since(repo.get("created_at")),
        "days_since_push": _days_since(repo.get("pushed_at")),
        "health_score": score,
        "health_components": components,
        "tier": tier,
        "momentum": momentum.as_dict(),
        "analysis": analysis.as_dict(),
        "discovery": {
            "source": source,
            "seed_reason": seed_reason,
            "metadata_source": metadata_source,
        },
        "fetched_at": now_iso(),
    }


def _build_index(
    entries: dict[str, dict[str, Any]],
    edges: list[Any],
    rejected: list[dict[str, Any]],
    stats: PipelineStats,
    categories: list[dict[str, Any]],
) -> dict[str, Any]:
    # Everything in the index is keyed by the lower-cased full name so that
    # ``categories[].tools``, ``supersede[]`` and ``tools{}`` all agree and no
    # consumer has to remember which casing it is holding. Display case lives in
    # ``tools[key].full_name`` (and ``*_name`` on supersede edges).
    by_category: dict[str, list[str]] = {c["id"]: [] for c in categories}
    for key, entry in entries.items():
        by_category.setdefault(entry["category"], []).append(key)

    # Retired tools stay in the data but are excluded from the live tables.
    live = {
        name: e
        for name, e in entries.items()
        if e.get("lifecycle", {}).get("state") == STATE_ACTIVE
    }

    return {
        "schema": SCHEMA_VERSION,
        "generated_at": now_iso(),
        "generator": "agentindex",
        "counts": {
            "tools": len(live),
            "retired": len(entries) - len(live),
            "categories": len([c for c in categories if by_category.get(c["id"])]),
            "supersede_edges": len(edges),
            "rejected": len(rejected),
        },
        "stats": stats.as_dict(),
        "categories": [
            {
                "id": c["id"],
                "order": c.get("order", 999),
                "title": c.get("title", {}),
                "tagline": c.get("tagline", {}),
                "problem": c.get("problem", {}),
                "tools": sorted(
                    by_category.get(c["id"], []),
                    key=lambda n: (
                        -int(entries.get(n, {}).get("health_score", 0)),
                        -int(entries.get(n, {}).get("stars", 0)),
                    ),
                ),
            }
            for c in categories
        ],
        "tools": {
            name: {
                "full_name": e["full_name"],
                "category": e["category"],
                "stars": e["stars"],
                "stars_per_day": e["momentum"]["stars_per_day"],
                "health_score": e["health_score"],
                "tier": e["tier"],
                "state": e["lifecycle"]["state"],
                "out_of_the_box": e["analysis"]["friction"]["out_of_the_box"],
                "non_programmer_friendly": e["analysis"]["friction"]["non_programmer_friendly"],
                "setup_level": e["analysis"]["friction"]["level"],
                "capabilities": e["analysis"]["capabilities"],
                "agents": e["analysis"]["agents"],
            }
            for name, e in entries.items()
        },
        "supersede": [e.as_dict() for e in edges],
        "rejected": rejected,
    }


def _build_graveyard(entries: dict[str, dict[str, Any]], edges: list[Any]) -> dict[str, Any]:
    retired = {
        name: e
        for name, e in entries.items()
        if e["lifecycle"]["state"] in {"superseded", "deprecated", "archived"}
    }
    return {
        "schema": SCHEMA_VERSION,
        "generated_at": now_iso(),
        "count": len(retired),
        "tools": {
            name: {
                "full_name": e["full_name"],
                "category": e["category"],
                "stars": e["stars"],
                "state": e["lifecycle"]["state"],
                "superseded_by": e["lifecycle"].get("superseded_by", ""),
                "note_en": e["lifecycle"].get("note_en", ""),
                "note_zh": e["lifecycle"].get("note_zh", ""),
                "last_push": e["pushed_at"],
            }
            for name, e in retired.items()
        },
        "edges": [e.as_dict() for e in edges],
    }


def _days_since(value: str | None) -> int:
    parsed = parse_iso(value)
    if not parsed:
        return 0
    return (datetime.now(timezone.utc) - parsed).days
