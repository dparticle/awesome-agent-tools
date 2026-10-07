"""The elimination engine.

The premise: *there is always a dark horse.* When a newer tool covers every
capability of an incumbent, matches or beats its traction, and is no harder to
set up, the incumbent should stop being recommended — otherwise the index
slowly fills with tools nobody should install any more.

The canonical example is ``magpie`` over ``cc-switch``: same problem space
(multi-account / provider switching), but magpie also routes other models
through the agent, so it strictly covers the older tool's feature set.

This module is deliberately conservative. A wrong elimination silently hides a
good tool, which is worse than showing two overlapping tools. Every rule below
must hold before an edge is recorded, and every edge carries its evidence.

See ``docs/SUPERSEDE.md`` for the human-readable specification.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable

from .github import parse_iso
from .scoring import Momentum, load_thresholds
from .util import LOG

# --------------------------------------------------------------------------
# Lifecycle states
# --------------------------------------------------------------------------

STATE_ACTIVE = "active"
STATE_DORMANT = "dormant"
STATE_SUPERSEDED = "superseded"
STATE_DEPRECATED = "deprecated"
STATE_ARCHIVED = "archived"

STATE_LABEL = {
    STATE_ACTIVE: {"en": "Active", "zh": "活跃"},
    STATE_DORMANT: {"en": "Dormant", "zh": "停滞"},
    STATE_SUPERSEDED: {"en": "Superseded", "zh": "已被取代"},
    STATE_DEPRECATED: {"en": "Deprecated", "zh": "已废弃"},
    STATE_ARCHIVED: {"en": "Archived", "zh": "已归档"},
}

STATE_ICON = {
    STATE_ACTIVE: "🟢",
    STATE_DORMANT: "🟡",
    STATE_SUPERSEDED: "🔻",
    STATE_DEPRECATED: "⛔",
    STATE_ARCHIVED: "📦",
}

#: States whose tools are moved out of the live tables into the graveyard.
RETIRED_STATES = {STATE_SUPERSEDED, STATE_DEPRECATED, STATE_ARCHIVED}

#: Edge kinds.
EDGE_SUPERSEDE = "supersede"
#: A challenger covers an incumbent's ground and is rising, but has not yet
#: matched its traction. Recorded as a *watch* signal rather than a retirement:
#: claiming a two-week-old 5.6k-star project has replaced a 140k-star incumbent
#: would not survive this project's own stated rules.
EDGE_CHALLENGER = "challenger"


@dataclass
class SupersedeEdge:
    """A single "B replaces A" conclusion, with the evidence that produced it."""

    incumbent: str  # full_name being superseded
    challenger: str  # full_name doing the superseding
    #: What the edge *means*: EDGE_SUPERSEDE (retire the incumbent) or
    #: EDGE_CHALLENGER (report the pair, retire nothing).
    kind: str = EDGE_SUPERSEDE
    #: How it was decided: "auto" by the rules, or "curated" by a human.
    source: str = "auto"
    confidence: str = "medium"  # high | medium | low
    coverage: float = 0.0
    covered: list[str] = field(default_factory=list)
    star_ratio: float = 0.0
    momentum_ratio: float = 0.0
    setup_delta: int = 0
    dominance: float = 0.0
    reasons: list[str] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)

    @property
    def incumbent_name(self) -> str:
        """Display-case name, for rendering."""
        return self.incumbent

    @property
    def challenger_name(self) -> str:
        return self.challenger

    @property
    def key(self) -> str:
        """Lower-cased incumbent, matching the ``tools`` map key."""
        return (self.incumbent or "").lower()

    @property
    def challenger_key(self) -> str:
        return (self.challenger or "").lower()

    def as_dict(self) -> dict[str, Any]:
        return {
            # Lower-cased to match the ``tools`` map in ``data/index.json``,
            # which is keyed by ``full_name.lower()``. Storing display case here
            # made every consumer do its own case-insensitive lookup, and one
            # that forgot silently produced dangling references.
            "incumbent": self.key,
            "challenger": self.challenger_key,
            "incumbent_name": self.incumbent,
            "challenger_name": self.challenger,
            "kind": self.kind,
            "source": self.source,
            "confidence": self.confidence,
            "coverage": round(self.coverage, 3),
            "covered": self.covered,
            "star_ratio": round(self.star_ratio, 3),
            "momentum_ratio": round(self.momentum_ratio, 3),
            "setup_delta": self.setup_delta,
            "dominance": round(self.dominance, 3),
            "reasons": self.reasons,
            "evidence": self.evidence,
        }


@dataclass
class ToolFacts:
    """The minimum a supersede decision needs to know about one tool."""

    full_name: str
    capabilities: set[str] = field(default_factory=set)
    stars: int = 0
    stars_per_day: float = 0.0
    setup_score: int = 50  # friction: lower is easier
    out_of_the_box: bool = False
    non_programmer_friendly: bool = False
    health: int = 0
    doc_score: int = 0
    pushed_at: str | None = None
    archived: bool = False
    category: str = ""
    is_self_hosted: bool = False

    @classmethod
    def from_entry(cls, entry: dict[str, Any], category: str = "") -> "ToolFacts":
        analysis = entry.get("analysis") or {}
        friction = analysis.get("friction") or {}
        caps = set(analysis.get("capabilities") or [])
        return cls(
            full_name=entry["full_name"],
            capabilities=caps,
            stars=int(entry.get("stars") or 0),
            stars_per_day=float((entry.get("momentum") or {}).get("stars_per_day") or 0.0),
            setup_score=int(friction.get("score") or 50),
            out_of_the_box=bool(friction.get("out_of_the_box")),
            non_programmer_friendly=bool(friction.get("non_programmer_friendly")),
            health=int(entry.get("health_score") or 0),
            doc_score=int(analysis.get("doc_score") or 0),
            pushed_at=entry.get("pushed_at"),
            archived=bool(entry.get("archived")),
            category=category,
            is_self_hosted="self-hosted" in caps,
        )


# --------------------------------------------------------------------------
# Individual rules
# --------------------------------------------------------------------------


def coverage_ratio(incumbent: ToolFacts, challenger: ToolFacts) -> tuple[float, list[str]]:
    """Fraction of the incumbent's capabilities the challenger also has.

    A tool with no detected capabilities is treated as uncovered (ratio 0):
    we have no evidence it does anything, so it cannot be eliminated on
    functional grounds.
    """
    if not incumbent.capabilities:
        return 0.0, []
    covered = incumbent.capabilities & challenger.capabilities
    return len(covered) / len(incumbent.capabilities), sorted(covered)


def evaluate_pair(
    incumbent: ToolFacts,
    challenger: ToolFacts,
    cfg: dict[str, Any] | None = None,
) -> SupersedeEdge | None:
    """Decide whether ``challenger`` eliminates ``incumbent``.

    Returns ``None`` unless *every* rule passes. Ordering matters: cheap
    disqualifiers run first so the common case is fast.
    """
    cfg = cfg or load_thresholds()
    rules = cfg.get("supersede", {})

    # Rule 0 — a tool never supersedes itself, and a retired tool supersedes
    # nothing (otherwise dead tools keep killing live ones).
    if incumbent.full_name == challenger.full_name:
        return None
    if challenger.archived or incumbent.archived:
        return None
    if challenger.health <= 0:
        return None

    # Rule 0b — refuse to eliminate on the strength of a suspiciously broad
    # capability set. A tool credited with nearly every capability is almost
    # always a directory or an over-matching README, not a genuine superset.
    # This is a safety net for analyser regressions, not the primary defence.
    max_caps = int(rules.get("max_challenger_capabilities", 18))
    if len(challenger.capabilities) > max_caps or len(incumbent.capabilities) > max_caps:
        return None

    # Rule 0c — elimination is a *within-category* judgement.
    #
    # The requirement is "a tool that covers everything the tools in this
    # category do". Without this rule a large multi-purpose tool trivially
    # "covers" every narrow tool in every category (a 16-capability tool covers
    # a 2-capability one 100% of the time), which retired 73 of 191 tools in
    # testing. Comparing only same-category tools is both correct and what a
    # reader expects.
    if incumbent.category and challenger.category and incumbent.category != challenger.category:
        return None

    # Rule 0d — a tool with almost no detected capabilities is not a meaningful
    # incumbent. "Covers 100% of one capability" is not evidence of replacement.
    min_incumbent_caps = int(rules.get("min_incumbent_capabilities", 3))
    if len(incumbent.capabilities) < min_incumbent_caps:
        return None

    # Rule 0e — a strict superset is required, not merely a superset of a tiny
    # set. The challenger must be a genuinely broader tool.
    min_challenger_caps = int(rules.get("min_challenger_capabilities", 4))
    if len(challenger.capabilities) < min_challenger_caps:
        return None

    # Rule 1 — the challenger must be healthy enough to be a recommendation.
    min_dominance = float(rules.get("min_dominance_score", 0.55))
    if challenger.health < incumbent.health and challenger.stars < incumbent.stars:
        return None

    # Rule 2 — functional coverage.
    coverage, covered = coverage_ratio(incumbent, challenger)
    if coverage < float(rules.get("min_coverage_ratio", 1.0)):
        return None
    missing = incumbent.capabilities - challenger.capabilities
    if missing:
        return None

    # Rule 3 — traction. The challenger must be at least as popular.
    star_ratio = (challenger.stars / incumbent.stars) if incumbent.stars else float("inf")
    if star_ratio < float(rules.get("min_star_advantage", 1.15)):
        return None

    # Rule 4 — momentum. A stagnant challenger must not kill a rising tool.
    inc_mom = max(incumbent.stars_per_day, 0.05)
    momentum_ratio = challenger.stars_per_day / inc_mom
    if momentum_ratio < float(rules.get("min_momentum_advantage", 1.0)):
        return None

    # Rule 5 — adoption cost. A strictly better tool that is much harder to set
    # up does not actually replace the incumbent for most readers.
    setup_delta = challenger.setup_score - incumbent.setup_score
    if setup_delta > int(rules.get("max_setup_penalty", 12)):
        return None

    # Rule 6 — the challenger must not be documentation-poor.
    if challenger.doc_score + 10 < incumbent.doc_score:
        return None

    # Rule 7 — dominance margin, so marginal calls stay out of the graveyard.
    dominance = _dominance(incumbent, challenger, coverage, star_ratio, momentum_ratio, setup_delta)
    if dominance < min_dominance:
        return None

    reasons = [
        f"covers 100% of capabilities ({len(covered)}/{len(incumbent.capabilities)})",
        f"{star_ratio:.2f}x the stars ({challenger.stars:,} vs {incumbent.stars:,})",
        f"{momentum_ratio:.2f}x the star velocity "
        f"({challenger.stars_per_day:.1f}/day vs {incumbent.stars_per_day:.1f}/day)",
    ]
    if setup_delta <= 0:
        reasons.append(f"no harder to set up ({challenger.setup_score} vs {incumbent.setup_score} friction)")
    else:
        reasons.append(f"slightly heavier setup (+{setup_delta} friction, within tolerance)")

    confidence = "high" if (coverage >= 1.0 and star_ratio >= 1.5 and setup_delta <= 0) else "medium"

    return SupersedeEdge(
        incumbent=incumbent.full_name,
        challenger=challenger.full_name,
        kind=EDGE_SUPERSEDE,
        source="auto",
        confidence=confidence,
        coverage=coverage,
        covered=covered,
        star_ratio=star_ratio,
        momentum_ratio=momentum_ratio,
        setup_delta=setup_delta,
        dominance=dominance,
        reasons=reasons,
        evidence={
            "incumbent_capabilities": sorted(incumbent.capabilities),
            "challenger_capabilities": sorted(challenger.capabilities),
            "incumbent_health": incumbent.health,
            "challenger_health": challenger.health,
            "incumbent_setup_score": incumbent.setup_score,
            "challenger_setup_score": challenger.setup_score,
        },
    )


def _dominance(
    incumbent: ToolFacts,
    challenger: ToolFacts,
    coverage: float,
    star_ratio: float,
    momentum_ratio: float,
    setup_delta: int,
) -> float:
    """Blend the margins into one 0-1 confidence value."""
    import math

    star_term = min(1.0, math.log10(max(star_ratio, 1.0)) / math.log10(3.0)) if star_ratio > 1 else 0.0
    mom_term = min(1.0, math.log10(max(momentum_ratio, 1.0)) / math.log10(5.0)) if momentum_ratio > 1 else 0.0
    setup_term = 1.0 if setup_delta <= 0 else max(0.0, 1.0 - setup_delta / 20.0)
    health_term = 1.0 if challenger.health >= incumbent.health else 0.4
    return (
        coverage * 0.40 + star_term * 0.25 + mom_term * 0.20 + setup_term * 0.10 + health_term * 0.05
    )


# --------------------------------------------------------------------------
# Graph-level resolution
# --------------------------------------------------------------------------


def build_edges(
    facts: Iterable[ToolFacts],
    cfg: dict[str, Any] | None = None,
) -> list[SupersedeEdge]:
    """Evaluate every pair, then keep only the *nearest* superseder per tool.

    Without this reduction a long chain (C > B > A) would mark A as superseded
    by both B and C, which reads as noise. We keep the strongest direct edge.
    """
    items = [f for f in facts if f.capabilities]
    edges: list[SupersedeEdge] = []
    for incumbent in items:
        for challenger in items:
            if incumbent.full_name == challenger.full_name:
                continue
            edge = evaluate_pair(incumbent, challenger, cfg)
            if edge:
                edges.append(edge)

    best: dict[str, SupersedeEdge] = {}
    for edge in edges:
        current = best.get(edge.incumbent)
        if current is None or edge.dominance > current.dominance:
            best[edge.incumbent] = edge

    return sorted(best.values(), key=lambda e: (-e.dominance, e.incumbent))


def apply_manual_overrides(
    edges: list[SupersedeEdge],
    overrides: dict[str, Any],
    facts: dict[str, ToolFacts] | None = None,
) -> list[SupersedeEdge]:
    """Fold hand-curated verdicts into the automatic graph.

    ``overrides.supersede`` entries look like::

        {"incumbent": "owner/old", "challenger": "owner/new", "note": "..."}

    A curated entry is a **nomination, not a verdict**. When ``facts`` is
    supplied the claim is checked against the same coverage rule the automatic
    engine uses, and the edge is recorded as one of two kinds:

    * ``supersede`` — the challenger genuinely covers the incumbent's
      capabilities. The incumbent is retired.
    * ``challenger`` — it does not (yet). The pair is still reported, because it
      is the interesting kind of finding, but nothing is retired.

    This distinction exists because the project's own rules refused the
    magpie/cc-switch pair: magpie covers only part of cc-switch's capability set
    and has ~4% of its stars. Recording that as a retirement would have meant the
    list asserting something its own methodology contradicts.
    """
    curated: list[SupersedeEdge] = []
    for item in overrides.get("supersede", []) or []:
        incumbent_key = (item.get("incumbent") or "").lower()
        challenger_key = (item.get("challenger") or "").lower()
        if not incumbent_key or not challenger_key:
            continue

        note = item.get("note") or "curated relationship"
        coverage = 1.0
        covered: list[str] = []
        missing: list[str] = []
        kind = EDGE_SUPERSEDE
        confidence = "high"
        reasons = [note]

        inc = (facts or {}).get(incumbent_key)
        cha = (facts or {}).get(challenger_key)
        if inc is not None and cha is not None:
            coverage, covered = coverage_ratio(inc, cha)
            missing = sorted(inc.capabilities - cha.capabilities)
            if missing or coverage < 1.0:
                kind = EDGE_CHALLENGER
                confidence = "medium"
                reasons = [
                    note,
                    f"covers {coverage:.0%} of {inc.full_name}'s capabilities "
                    f"({len(covered)}/{len(inc.capabilities)})",
                    "not covered: " + ", ".join(missing) if missing else "partial overlap",
                ]
            if inc.stars and cha.stars:
                ratio = cha.stars / inc.stars
                reasons.append(f"{ratio:.2f}x the stars ({cha.stars:,} vs {inc.stars:,})")

        curated.append(
            SupersedeEdge(
                incumbent=incumbent_key,
                challenger=challenger_key,
                kind=kind,
                source="curated",
                confidence=confidence,
                coverage=coverage,
                covered=covered,
                reasons=reasons,
                evidence={
                    "curated": True,
                    "note": item.get("note", ""),
                    "missing_capabilities": missing,
                },
            )
        )

    by_incumbent = {e.incumbent: e for e in edges}
    for edge in curated:
        # A challenger edge must not displace a genuine automatic supersede.
        existing = by_incumbent.get(edge.incumbent)
        if existing is not None and existing.source == "auto" and edge.kind == EDGE_CHALLENGER:
            continue
        by_incumbent[edge.incumbent] = edge
    return sorted(by_incumbent.values(), key=lambda e: (-e.dominance, e.incumbent))


def resolve_states(
    entries: dict[str, dict[str, Any]],
    edges: list[SupersedeEdge],
    overrides: dict[str, Any],
    cfg: dict[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    """Assign a lifecycle state to every tool.

    Precedence: explicit override > archived > manual deprecation > superseded
    > dormant > active.
    """
    cfg = cfg or load_thresholds()
    rules = cfg.get("supersede", {})
    dormant_days = int(rules.get("dormant_days", 240))

    # Keys are lower-cased on both sides. ``entries`` is keyed by
    # ``full_name.lower()`` while ``SupersedeEdge`` stores the display-case
    # name, so comparing them directly silently dropped every edge whose repo
    # name contained an uppercase letter.
    superseded_by = {(e.incumbent or "").lower(): e for e in edges}
    manual_states = {
        (k or "").lower(): v for k, v in (overrides.get("states", {}) or {}).items()
    }
    notes = {(k or "").lower(): v for k, v in (overrides.get("notes", {}) or {}).items()}

    now = datetime.now(timezone.utc)
    out: dict[str, dict[str, Any]] = {}

    for full_name, entry in entries.items():
        key = full_name.lower()
        state = STATE_ACTIVE
        note_en = ""
        note_zh = ""
        edge: SupersedeEdge | None = None
        challenger_edge: SupersedeEdge | None = None

        if entry.get("archived"):
            state = STATE_ARCHIVED
            note_en = "The repository is archived by its owner."
            note_zh = "仓库已被作者归档。"
        elif key in manual_states:
            spec = manual_states[key] or {}
            state = spec.get("state", STATE_DEPRECATED)
            note_en = spec.get("note_en", "")
            note_zh = spec.get("note_zh", "")
        elif key in superseded_by:
            candidate = superseded_by[key]
            if candidate.kind == EDGE_CHALLENGER:
                # A challenger has not met the bar for retirement. Surface it as
                # a signal on a live entry instead of moving the tool out.
                challenger_edge = candidate
            else:
                edge = candidate
                state = STATE_SUPERSEDED
                note_en = f"Superseded by {edge.challenger}: {edge.reasons[0]}."
                note_zh = f"已被 {edge.challenger} 取代：{edge.reasons[0]}。"

        if state == STATE_ACTIVE:
            pushed = parse_iso(entry.get("pushed_at"))
            if pushed and (now - pushed).days > dormant_days:
                state = STATE_DORMANT
                days = (now - pushed).days
                note_en = f"No commits in {days} days."
                note_zh = f"已有 {days} 天没有提交。"

        # A curated note replaces the generated prose for this tool, because a
        # human explanation is always better than a templated one. It never
        # overrides the *state* — that stays governed by the rules above unless
        # an explicit ``states`` entry says otherwise.
        curated = notes.get(key) or {}
        if curated:
            if curated.get("note_en"):
                note_en = curated["note_en"]
            if curated.get("note_zh"):
                note_zh = curated["note_zh"]

        out[full_name] = {
            "state": state,
            "note_en": note_en,
            "note_zh": note_zh,
            "superseded_by": edge.challenger if edge else "",
            "supersede_edge": edge.as_dict() if edge else None,
            "challenger": challenger_edge.challenger if challenger_edge else "",
            "challenger_edge": challenger_edge.as_dict() if challenger_edge else None,
        }
    return out


def describe_elimination(
    edges: list[SupersedeEdge],
    entries: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Shape edges for the rendered report."""
    rows: list[dict[str, Any]] = []
    for edge in edges:
        incumbent = entries.get(edge.incumbent) or entries.get(edge.incumbent.lower()) or {}
        challenger = entries.get(edge.challenger) or entries.get(edge.challenger.lower()) or {}
        rows.append(
            {
                **edge.as_dict(),
                "incumbent_name": incumbent.get("name", edge.incumbent),
                "challenger_name": challenger.get("name", edge.challenger),
                "incumbent_stars": incumbent.get("stars", 0),
                "challenger_stars": challenger.get("stars", 0),
            }
        )
    return rows
