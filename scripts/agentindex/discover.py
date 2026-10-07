"""Candidate discovery.

Three sources feed the pipeline:

1. **Seeds** (``config/seeds.json``) — hand-picked repos, always evaluated.
2. **Category queries** (``config/categories.json``) — the daily crawl, sorted
   by stars.
3. **Rising queries** (``config/discovery.json``) — recently created repos with
   traction. Without this pass the star-sorted crawl would never surface a
   dark horse, and the elimination engine would have nothing to promote.

A repo may match several categories; we record every match and let the
category with the strongest capability overlap own it, so a tool never appears
twice in the rendered index.

Efficiency note: GitHub's search endpoint returns *complete repository
objects*. We keep that payload on the candidate and use it as provisional
metadata, so the expensive ``/repos/{owner}/{repo}`` call is only spent on
repos that already look worth keeping.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

from .github import GitHubClient, RateLimitExhausted
from .readme_analysis import ReadmeAnalysis
from .util import CONFIG_DIR, LOG, read_json


@dataclass
class Candidate:
    full_name: str
    categories: list[str] = field(default_factory=list)
    source: str = "search"  # seed | search | rising
    seed_reason: str = ""
    #: Full repo object as returned by the search API, usable as metadata.
    metadata: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "full_name": self.full_name,
            "categories": self.categories,
            "source": self.source,
            "seed_reason": self.seed_reason,
        }


def load_categories() -> list[dict[str, Any]]:
    data = read_json(CONFIG_DIR / "categories.json", default={}) or {}
    return sorted(data.get("categories", []), key=lambda c: c.get("order", 999))


def load_seeds() -> list[dict[str, Any]]:
    data = read_json(CONFIG_DIR / "seeds.json", default={}) or {}
    return data.get("seeds", [])


def load_discovery_config() -> dict[str, Any]:
    return read_json(CONFIG_DIR / "discovery.json", default={}) or {}


def normalise_search_item(item: dict[str, Any]) -> dict[str, Any]:
    """Fill in the fields the search payload omits, so downstream code is uniform."""
    item = dict(item)
    item.setdefault("owner", {})
    if isinstance(item["owner"], str):
        item["owner"] = {"login": item["owner"]}
    item.setdefault("subscribers_count", item.get("watchers_count", 0))
    item.setdefault("open_issues_count", item.get("open_issues", 0))
    item.setdefault("license", None)
    item.setdefault("topics", [])
    item.setdefault("fork", False)
    item.setdefault("archived", False)
    item.setdefault("disabled", False)
    return item


def _merge(
    candidates: dict[str, Candidate],
    item: dict[str, Any],
    category: str,
    source: str,
    why: str = "",
) -> None:
    full_name = item.get("full_name") or ""
    if not full_name:
        return
    key = full_name.lower()
    existing = candidates.get(key)
    if existing is None:
        candidates[key] = Candidate(
            full_name=full_name,
            categories=[category],
            source=source,
            seed_reason=why,
            metadata=item,
        )
        return
    if category not in existing.categories:
        existing.categories.append(category)
    if not existing.metadata and item:
        existing.metadata = item
    # A seed always outranks a search hit for provenance purposes.
    if source == "seed" and existing.source != "seed":
        existing.source = "seed"
        existing.seed_reason = why


def discover(client: GitHubClient, *, per_query: int | None = None) -> list[Candidate]:
    """Collect candidates from seeds, category queries and rising queries."""
    cfg = load_discovery_config()
    per_query = per_query or int(cfg.get("per_query", 30))
    candidates: dict[str, Candidate] = {}

    # -- seeds (no search cost) -------------------------------------------
    for seed in load_seeds():
        repo = (seed.get("repo") or "").strip()
        if not repo:
            continue
        _merge(
            candidates,
            {"full_name": repo},
            seed.get("category", "agent-runtimes"),
            "seed",
            seed.get("why", ""),
        )
    LOG.info("seeded %d candidates", len(candidates))

    # -- category crawl ----------------------------------------------------
    for category in load_categories():
        cat_id = category["id"]
        for query in category.get("queries", []):
            try:
                items = client.search_repositories(query, per_page=per_query)
            except RateLimitExhausted:
                LOG.warning("search budget exhausted while crawling %s", cat_id)
                return list(candidates.values())
            except RuntimeError as exc:
                LOG.warning("search %r failed: %s", query, exc)
                continue
            for item in items:
                _merge(candidates, normalise_search_item(item), cat_id, "search")
            LOG.info("  %-20s %-50s -> %2d hits", cat_id, query[:50], len(items))

    # -- rising / dark-horse pass -----------------------------------------
    rising = cfg.get("rising", {})
    if rising.get("enabled", True):
        since = (
            datetime.now(timezone.utc) - timedelta(days=int(rising.get("recent_days", 150)))
        ).date().isoformat()
        min_stars = int(rising.get("min_stars", 40))
        for template in rising.get("queries", []):
            query = template.format(since=since, min_stars=min_stars)
            try:
                items = client.search_repositories(query, per_page=per_query)
            except RateLimitExhausted:
                LOG.warning("search budget exhausted during rising pass")
                break
            except RuntimeError as exc:
                LOG.warning("rising query %r failed: %s", query, exc)
                continue
            for item in items:
                _merge(candidates, normalise_search_item(item), "", "rising")
            LOG.info("  %-20s %-50s -> %2d hits", "rising", query[:50], len(items))

    LOG.info("discovered %d unique candidates", len(candidates))
    return list(candidates.values())


# --------------------------------------------------------------------------
# Category assignment
# --------------------------------------------------------------------------


def score_category(
    category: dict[str, Any],
    analysis: ReadmeAnalysis,
    *,
    min_hits: int = 1,
) -> tuple[float, list[str]]:
    """Score how well a README's capabilities fit a category.

    ``min_hits`` requires a capability to be mentioned more than once before it
    counts towards membership. A single incidental mention ("...as a tool for AI
    agents", "browser sessions") should not place a general-purpose project in a
    category about agent operations.
    """
    caps = set(analysis.capabilities)
    hits = analysis.capability_hits or {}
    required_any = set(category.get("required_any", []))
    boost = set(category.get("boost_capabilities", []))
    any_caps = set(category.get("any_capabilities", []))

    def corroborated(cap: str) -> bool:
        return hits.get(cap, 1) >= min_hits

    required_hit = {c for c in caps & required_any if corroborated(c)}
    if required_any and not required_hit:
        return 0.0, []

    hit_boost = {c for c in caps & boost if corroborated(c)}
    hit_any = {c for c in caps & any_caps if corroborated(c)}

    score = 0.0
    score += 10.0 * len(required_hit)
    score += 3.0 * len(hit_boost)
    score += 1.0 * len(hit_any - required_any - boost)

    # Accessibility nudges: an easier tool is a better fit for a practical list.
    if analysis.friction.out_of_the_box:
        score += 1.5
    if analysis.friction.non_programmer_friendly:
        score += 1.0
    if analysis.doc_score >= 60:
        score += 1.0

    return score, sorted(required_hit) or sorted(hit_any)


#: Capabilities that only make sense in an agent context. Deliberately excludes
#: ``cross-agent-support`` (granted to anything naming two agents, which a
#: general-purpose tool can do in a comparison table) and ``api-gateway`` /
#: ``billing-metering`` / ``gui-desktop`` / ``notifications`` /
#: ``security-isolation`` / ``team-collaboration`` / ``self-hosted``, all of
#: which ordinary software also legitimately claims.
AGENT_DOMAIN_CAPABILITIES = {
    "agent-runtime",
    "multi-agent-orchestration",
    "parallel-execution",
    "worktree-isolation",
    "multi-account-switching",
    "quota-management",
    "auto-failover",
    "remote-control",
    "mobile-access",
    "model-routing",
    "provider-aggregation",
    "quota-distribution",
    "session-persistence",
    "memory-context",
    "skills-plugins",
    "mcp-support",
    "voice-input",
}

#: Capabilities strong enough that a single match proves the repo is about
#: coding agents rather than merely adjacent to them. These are narrow enough
#: that ordinary software does not trip them by accident.
STRONG_AGENT_CAPABILITIES = {
    "multi-account-switching",
    "quota-management",
    "auto-failover",
    "model-routing",
    "provider-aggregation",
    "quota-distribution",
    "multi-agent-orchestration",
    "worktree-isolation",
    "agent-runtime",
}

#: Weaker signals. Two or more together also establish relevance.
WEAK_AGENT_CAPABILITIES = AGENT_DOMAIN_CAPABILITIES - STRONG_AGENT_CAPABILITIES

#: A match is only credible when it recurs. A single incidental mention —
#: Playwright's README saying "browser sessions" or "Coding agents (Claude
#: Code, Copilot)" in an install table — is not a feature claim.
MIN_PATTERN_HITS = 2


#: Language that identifies a project as being *about* AI coding agents. Matched
#: against the repo's identity text (name + GitHub description + opening README
#: prose) rather than the whole README, because that is where a project states
#: what it is. A tool that merely *mentions* agents somewhere in 60 KB of docs
#: does not become an agent tool.
AGENT_IDENTITY_RE = re.compile(
    r"coding agent|code agent|ai agent|agentic|agent (manager|orchestrat|harness|runtime|fleet|swarm|team)|"
    r"claude code|codex|gemini cli|opencode|cursor|copilot|aider|cline|roo code|qwen code|"
    r"mcp server|model context protocol|subagent|sub-agent|"
    r"agent (skill|plugin|session|memory|workflow|personality)|"
    r"llm (gateway|router|proxy)|api (gateway|relay) for (llm|ai)|"
    r"ai (subscription|quota|account)|coding (assistant|agent)|"
    r"智能体|编码 ?agent|编程助手|ai ?代理|大模型(网关|中转|路由)",
    re.IGNORECASE,
)

#: How much of the README's opening counts as "identity" prose.
IDENTITY_PROSE_CHARS = 1200

#: Repos that keyword search keeps surfacing and that are genuinely useful but
#: are not agent tools. Playwright, for instance, says it is "a tool for AI
#: agents" while being a browser-automation framework. Excluding them by name is
#: honest: it is a curation decision, and it is visible in config rather than
#: hidden inside a scoring heuristic.
EXCLUDED_REPOS = {
    "microsoft/playwright",
    "microsoft/playwright-mcp",
    "asgeirtj/system_prompts_leaks",
    "jamiepine/voicebox",
    "ruvnet/ruview",
    "public-apis/public-apis",
    "ripienaar/free-for-dev",
    "sindresorhus/awesome",
    "avelino/awesome-go",
}


def is_on_topic(analysis: ReadmeAnalysis, identity_text: str = "") -> bool:
    """Does this project present itself as being about AI coding agents?

    Keyword search surfaces plenty of adjacent-but-irrelevant repos — a web
    testing framework, a WiFi sensing project, a voice-cloning studio — that
    match capability patterns incidentally deep inside their documentation.

    The discriminator that actually works is the project's *identity*: its name,
    its GitHub description, and the opening of its README. Playwright calls
    itself "a framework for Web Testing and Automation" and never claims to be
    an agent tool, even though its docs mention coding agents in an install
    table. Happy calls itself "the open-source desktop app for Claude Code,
    Codex, and Grok ... to control your coding agents".
    """
    if not analysis.capabilities:
        return False

    identity = identity_text or (analysis.summary_en or "")
    if AGENT_IDENTITY_RE.search(identity):
        return True

    # Fall back to capability breadth for tools whose identity text is sparse
    # (some READMEs open with a screenshot and a one-word tagline).
    hits = analysis.capability_hits or {}
    strong = {c for c in set(analysis.capabilities) & STRONG_AGENT_CAPABILITIES if hits.get(c, 1) >= 2}
    if len(strong) >= 2:
        return True
    return bool(strong) and bool(analysis.agents)


def assign_category(
    candidate_categories: Iterable[str],
    analysis: ReadmeAnalysis,
    categories_by_id: dict[str, dict[str, Any]],
    *,
    min_hits: int = 2,
) -> tuple[str, list[str], float]:
    """Pick the single owning category for a tool.

    Returns ``(category_id, matched_capabilities, score)``. An empty
    ``category_id`` means the README showed no corroborated matching capability
    and the caller should drop the candidate.
    """
    best_id = ""
    best_score = 0.0
    best_matched: list[str] = []

    for cat_id in candidate_categories:
        category = categories_by_id.get(cat_id)
        if not category:
            continue
        score, matched = score_category(category, analysis, min_hits=min_hits)
        if score > best_score:
            best_id, best_score, best_matched = cat_id, score, matched

    return best_id, best_matched, best_score
