"""Health scoring, quality gates, tiers and momentum.

The score answers one question: *if a reader installs this today, how likely
are they to still be using it in six months?* It blends popularity (a proxy for
"other people already found the bugs"), momentum (is it still winning?),
maintenance recency, documentation quality and setup accessibility.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .github import parse_iso
from .readme_analysis import ReadmeAnalysis
from .util import CONFIG_DIR, clamp, read_json

TIER_ORDER = ["flagship", "recommended", "notable", "watchlist"]

TIER_LABEL = {
    "flagship": {"en": "Flagship", "zh": "旗舰"},
    "recommended": {"en": "Recommended", "zh": "推荐"},
    "notable": {"en": "Notable", "zh": "值得关注"},
    "watchlist": {"en": "Watchlist", "zh": "观察名单"},
}

TIER_ICON = {
    "flagship": "🏆",
    "recommended": "✅",
    "notable": "🔹",
    "watchlist": "👀",
}


def load_thresholds() -> dict[str, Any]:
    return read_json(CONFIG_DIR / "thresholds.json", default={}) or {}


# --------------------------------------------------------------------------
# Momentum
# --------------------------------------------------------------------------


@dataclass
class Momentum:
    stars_gained: int = 0
    days_span: int = 0
    stars_per_day: float = 0.0
    lifetime_stars_per_day: float = 0.0
    basis: str = "unknown"  # history | lifetime | none
    is_fast_riser: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "stars_gained": self.stars_gained,
            "days_span": self.days_span,
            "stars_per_day": round(self.stars_per_day, 2),
            "lifetime_stars_per_day": round(self.lifetime_stars_per_day, 2),
            "basis": self.basis,
            "is_fast_riser": self.is_fast_riser,
        }


def compute_momentum(
    repo: dict[str, Any],
    history: list[dict[str, Any]] | None,
    cfg: dict[str, Any] | None = None,
) -> Momentum:
    """Estimate star velocity.

    Preferred basis is a stored snapshot from ``history`` (real observed
    growth). On a cold start — or for a repo we just discovered — we fall back
    to lifetime stars/day, which is a good proxy for young repos and a
    conservative one for old ones.
    """
    cfg = cfg or load_thresholds()
    mcfg = cfg.get("momentum", {})
    history_days = int(mcfg.get("history_days", 21))
    min_history_days = int(mcfg.get("min_history_days", 5))
    young_days = int(mcfg.get("young_repo_days", 120))
    fast_riser = int(cfg.get("gates", {}).get("fast_riser_stars_14d", 60))

    stars = int(repo.get("stargazers_count") or 0)
    created = parse_iso(repo.get("created_at"))
    now = datetime.now(timezone.utc)
    age_days = max(1, (now - created).days) if created else 1

    result = Momentum()
    result.lifetime_stars_per_day = stars / age_days if age_days else float(stars)

    best: tuple[int, int] | None = None
    for snapshot in history or []:
        snap_date = parse_iso(snapshot.get("date"))
        snap_stars = int(snapshot.get("stars") or 0)
        if not snap_date or snap_stars <= 0:
            continue
        span = (now - snap_date).days
        if span < min_history_days or span > history_days * 3:
            continue
        gain = stars - snap_stars
        if gain < 0:
            continue
        if best is None or span < best[1]:
            best = (gain, span)

    if best is not None:
        gain, span = best
        result.stars_gained = gain
        result.days_span = span
        result.stars_per_day = gain / span
        result.basis = "history"
    else:
        result.basis = "lifetime"
        result.stars_per_day = result.lifetime_stars_per_day
        result.days_span = age_days
        result.stars_gained = stars

    # Fast riser: either an observed surge, or a young repo with a steep
    # lifetime slope. Both are expressed against the same configured threshold
    # (stars gained per 14 days) so the two bases stay comparable.
    threshold_per_day = fast_riser / 14.0
    if result.basis == "history":
        result.is_fast_riser = result.stars_per_day >= threshold_per_day
    else:
        result.is_fast_riser = age_days <= young_days and result.stars_per_day >= threshold_per_day

    return result


# --------------------------------------------------------------------------
# Health score
# --------------------------------------------------------------------------


def _popularity_score(stars: int) -> float:
    """Log-scaled: 100 stars -> ~40, 1k -> ~66, 10k -> ~88, 100k -> ~100."""
    if stars <= 0:
        return 0.0
    return clamp((math.log10(stars) / 5.0) * 100.0, 0.0, 100.0)


def _momentum_score(momentum: Momentum, cfg: dict[str, Any]) -> float:
    saturate = float(cfg.get("momentum", {}).get("saturate_gain_per_day", 120))
    return clamp((momentum.stars_per_day / saturate) * 100.0, 0.0, 100.0)


def _maintenance_score(repo: dict[str, Any], cfg: dict[str, Any]) -> float:
    """Freshness of the last push, with hard penalties for abandonment."""
    if repo.get("archived"):
        return 5.0
    pushed = parse_iso(repo.get("pushed_at"))
    if not pushed:
        return 20.0
    days = (datetime.now(timezone.utc) - pushed).days
    max_days = float(cfg.get("gates", {}).get("max_days_since_push", 180))
    if days <= 7:
        return 100.0
    if days <= 30:
        return 92.0
    if days <= 90:
        return 78.0
    if days <= max_days:
        return 55.0
    if days <= max_days * 2:
        return 25.0
    return 8.0


def _documentation_score(analysis: ReadmeAnalysis | None) -> float:
    if not analysis:
        return 0.0
    return float(analysis.doc_score)


def _accessibility_score(analysis: ReadmeAnalysis | None) -> float:
    """Reward tools a newcomer can actually adopt.

    This is deliberately *not* "fewer features is better": a turnkey tool and a
    powerful-but-GUI tool both score well; only heavy server/credential setup
    is penalised.
    """
    if not analysis:
        return 40.0
    friction = analysis.friction
    score = 100.0 - friction.score
    if friction.out_of_the_box:
        score += 12.0
    if friction.non_programmer_friendly:
        score += 8.0
    return clamp(score, 0.0, 100.0)


def health_score(
    repo: dict[str, Any],
    analysis: ReadmeAnalysis | None,
    momentum: Momentum,
    cfg: dict[str, Any] | None = None,
) -> tuple[int, dict[str, float]]:
    """Return ``(score, component_breakdown)``."""
    cfg = cfg or load_thresholds()
    weights = cfg.get("weights", {})
    components = {
        "popularity": _popularity_score(int(repo.get("stargazers_count") or 0)),
        "momentum": _momentum_score(momentum, cfg),
        "maintenance": _maintenance_score(repo, cfg),
        "documentation": _documentation_score(analysis),
        "accessibility": _accessibility_score(analysis),
    }
    total = sum(components[key] * float(weights.get(key, 0.0)) for key in components)
    weight_sum = sum(float(weights.get(key, 0.0)) for key in components) or 1.0
    return int(round(clamp(total / weight_sum, 0.0, 100.0))), {
        k: round(v, 1) for k, v in components.items()
    }


# --------------------------------------------------------------------------
# Gates & tiers
# --------------------------------------------------------------------------


@dataclass
class GateResult:
    passed: bool = True
    reasons: list[str] = field(default_factory=list)

    def fail(self, reason: str) -> None:
        self.passed = False
        self.reasons.append(reason)


def evaluate_gates(
    repo: dict[str, Any],
    analysis: ReadmeAnalysis | None,
    momentum: Momentum,
    cfg: dict[str, Any] | None = None,
) -> GateResult:
    """Decide whether a repo deserves a place in the index."""
    cfg = cfg or load_thresholds()
    gates = cfg.get("gates", {})
    result = GateResult()

    stars = int(repo.get("stargazers_count") or 0)
    min_stars = int(gates.get("min_stars", 120))
    if stars < min_stars and not momentum.is_fast_riser:
        result.fail(
            f"only {stars} stars (< {min_stars}) and not a fast riser "
            f"({momentum.stars_per_day:.1f} stars/day)"
        )

    if repo.get("archived") and not gates.get("allow_archived", False):
        result.fail("repository is archived")

    if repo.get("disabled"):
        result.fail("repository is disabled")

    created = parse_iso(repo.get("created_at"))
    if created:
        age = (datetime.now(timezone.utc) - created).days
        min_age = int(gates.get("min_age_days", 14))
        # A young repo that is already rising fast is exactly the "dark horse"
        # this project exists to surface, so the age gate must not exclude it.
        # magpie was rejected as "too new" while already at 5.6k stars.
        if age < min_age and not momentum.is_fast_riser:
            result.fail(f"only {age} days old (< {min_age}) and not yet a fast riser")

    pushed = parse_iso(repo.get("pushed_at"))
    max_days = int(gates.get("max_days_since_push", 180))
    if pushed:
        days = (datetime.now(timezone.utc) - pushed).days
        if days > max_days:
            result.fail(f"no push in {days} days (> {max_days})")

    if analysis is None or not analysis.readme_chars:
        result.fail("no README could be retrieved")
        return result

    # A curated directory is a reading list, not a tool you can install.
    if gates.get("exclude_curated_lists", True) and analysis.is_curated_list:
        signals = ", ".join(analysis.list_assessment.signals[:3])
        result.fail(f"looks like a curated list rather than a tool ({signals})")
        return result

    if analysis.readme_chars < int(gates.get("min_readme_chars", 900)):
        result.fail(f"README is only {analysis.readme_chars} chars")

    min_doc = int(gates.get("min_doc_score", 22))
    if analysis.doc_score < min_doc:
        result.fail(f"documentation score {analysis.doc_score} < {min_doc}")

    return result


def assign_tier(score: int, cfg: dict[str, Any] | None = None) -> str:
    cfg = cfg or load_thresholds()
    tiers = cfg.get("tiers", {})
    for tier in TIER_ORDER:
        if score >= int(tiers.get(tier, {}).get("min_score", 0)):
            return tier
    return "watchlist"


def tier_rank(tier: str) -> int:
    try:
        return TIER_ORDER.index(tier)
    except ValueError:
        return len(TIER_ORDER)
