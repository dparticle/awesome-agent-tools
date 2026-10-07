"""Render ``README.md`` and the ``docs/`` pages from ``data/index.json``.

Design rules that keep the generated output readable:

* The **main README is the deliverable**, not a dump. Each category gets a
  short "why this matters" paragraph, then a ranked table, then per-tool
  detail cards for the tools that earned them.
* **Every claim is traceable.** Setup difficulty, out-of-the-box status and
  capabilities all come from the analysed README, and the per-tool page shows
  the evidence sentence.
* **Bilingual.** Chinese and English readers get the same structure; the
  language toggle is a link, not a build flag.
"""

from __future__ import annotations

import re
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import quote

from .highlights import best_description, cjk_ratio, has_cjk, is_descriptive
from .readme_analysis import capability_label
from .scoring import TIER_ICON, TIER_LABEL, tier_rank
from .supersede import STATE_ICON, STATE_LABEL
from .util import (
    DATA_DIR,
    DOCS_DIR,
    REPO_ROOT,
    escape_table_cell,
    human_number,
    truncate,
    write_text,
)

GENERATED_BANNER = (
    "<!-- GENERATED FILE — do not edit by hand. "
    "Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->"
)

SETUP_ICON = {
    "turnkey": "🟢",
    "low": "🟢",
    "moderate": "🟡",
    "high": "🔴",
    "unknown": "⚪",
}

SETUP_LABEL = {
    "turnkey": {"en": "Turnkey", "zh": "开箱即用"},
    "low": {"en": "Easy", "zh": "较易"},
    "moderate": {"en": "Some setup", "zh": "需配置"},
    "high": {"en": "Involved", "zh": "较重"},
    "unknown": {"en": "Unknown", "zh": "未知"},
}

MAX_CATEGORY_ROWS = 30
MAX_DETAIL_CARDS = 5


def _now(index: dict[str, Any] | None = None) -> str:
    """Render timestamp, derived from the index — never from the wall clock.

    Rendering must be a pure function of ``data/index.json``. Stamping the
    current time made every render differ from the committed files, so CI's
    ``render --check`` failed on every run and each daily job produced a
    meaningless one-line diff.
    """
    stamp = (index or {}).get("generated_at")
    if stamp:
        parsed = None
        try:
            parsed = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
        except ValueError:
            parsed = None
        if parsed is not None:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return "unknown"


def _stars_cell(entry: dict[str, Any]) -> str:
    stars = entry.get("stars", 0)
    momentum = entry.get("momentum", {})
    per_day = float(momentum.get("stars_per_day") or 0)
    cell = f"{human_number(stars)}"
    if momentum.get("is_fast_riser"):
        cell += f" 🚀 +{per_day:.0f}/d"
    elif per_day >= 5:
        cell += f" (+{per_day:.0f}/d)"
    return cell


def _setup_cell(entry: dict[str, Any]) -> str:
    friction = (entry.get("analysis") or {}).get("friction") or {}
    level = friction.get("level", "unknown")
    icon = SETUP_ICON.get(level, "⚪")
    label = SETUP_LABEL.get(level, SETUP_LABEL["unknown"])["en"]
    if friction.get("out_of_the_box"):
        return f"{icon} {label} · OOTB"
    return f"{icon} {label}"


def _friendly_cell(entry: dict[str, Any]) -> str:
    friction = (entry.get("analysis") or {}).get("friction") or {}
    return "✅" if friction.get("non_programmer_friendly") else "—"


def _capability_summary(entry: dict[str, Any], limit: int = 4) -> str:
    caps = (entry.get("analysis") or {}).get("capabilities") or []
    labels = [capability_label(c) for c in caps[:limit]]
    extra = len(caps) - len(labels)
    text = ", ".join(labels)
    return f"{text} +{extra} more" if extra > 0 else text


#: Where a Chinese description came from. Rendered as a marker so a reader can
#: tell the author's own words from ours.
ZH_NATIVE = "native"  # the project's own Chinese README
ZH_CURATED = "curated"  # a maintainer-written note in config/overrides.json
ZH_DERIVED = "derived"  # our summary of capabilities we detected ourselves
ZH_ENGLISH = "english"  # kept in English rather than machine-translated

ZH_MARKER = {
    ZH_NATIVE: "",
    ZH_CURATED: "",
    ZH_DERIVED: " ‡",
    ZH_ENGLISH: " †",
}


def _zh_capability_summary(
    tool: dict[str, Any],
    entry: dict[str, Any],
    category_caps: set[str],
) -> str:
    """Compose a Chinese one-liner from capabilities we detected ourselves.

    This is **not** a translation of the project's English README — it is a
    summary built from this project's own bilingual capability taxonomy, which
    already carries Chinese labels for every capability. Two properties make it
    worth showing:

    * It is honest. Every clause traces to a pattern matched in the README and
      recorded as evidence, and the legend tells the reader the sentence is ours
      rather than the author's.
    * It is specific. Capabilities that merely *define the category* are
      filtered out, so the line describes what distinguishes this tool instead
      of restating the heading above it — the exact failure the first version of
      this list had.

    Returns an empty string when there is nothing distinctive to say, so the
    caller can fall back to the English text instead of padding the cell.
    """
    analysis = entry.get("analysis") or {}
    hits = analysis.get("capability_hits") or {}
    caps = tool.get("capabilities") or analysis.get("capabilities") or []
    agents = tool.get("agents") or analysis.get("agents") or []

    # Most-emphasised first: a capability the README documents repeatedly is
    # more central than one it mentions once.
    ranked = sorted(caps, key=lambda c: (-int(hits.get(c, 1)), c))
    distinctive = [c for c in ranked if c not in category_caps][:3]

    # The capability labels are already noun phrases ("跨 Agent 支持",
    # "自动故障转移"), so they are listed bare. Prefixing them with 支持 produced
    # "支持跨 Agent 支持".
    if not distinctive:
        # Nothing beyond what the heading already says. Better to show the
        # project's English than to pad the cell with a restatement.
        return ""

    clauses = ["、".join(capability_label(c, "zh") for c in distinctive)]
    if agents:
        clauses.append("兼容 " + "、".join(agents[:4]))
    return "；".join(clauses) + "。"


def _zh_description(
    tool: dict[str, Any],
    entry: dict[str, Any],
    analysis: dict[str, Any],
    highlights: list[str],
    category_caps: set[str] | None = None,
) -> tuple[str, str]:
    """Chinese description for a tool, plus which tier produced it.

    Four tiers, ordered by how much of the text is the project's own:

    1. ``native`` — the project's own Chinese README. The author's actual
       wording, and the best possible source.
    2. ``curated`` — a maintainer-written Chinese note in
       ``config/overrides.json``.
    3. ``derived`` — our own Chinese summary built from detected capabilities
       (see ``_zh_capability_summary``). Ours, not the author's, and marked.
    4. ``english`` — the English text, kept in English. Machine translating it
       would attribute claims to the project that it never made, and a Chinese
       reader is better served by an honest English sentence than by a fluent
       fabrication.

    Returns ``(text, tier)``.
    """
    # Tier 1: the author's own Chinese documentation.
    native_summary = (analysis.get("summary_zh_native") or "").strip()
    native_highlights = analysis.get("highlights_zh") or []
    # Thresholds are English-equivalent characters, so a complete Chinese
    # sentence is not mistaken for a fragment and padded with a bullet.
    text = best_description(native_summary, native_highlights, min_summary=45)
    if text:
        return truncate(text, 200), ZH_NATIVE

    # Tier 2: a maintainer-written Chinese note.
    curated = _curated_note(tool["full_name"], "zh")
    if curated:
        return truncate(curated, 200), ZH_CURATED

    # Tier 3: our own Chinese summary, derived from detected capabilities.
    derived = _zh_capability_summary(tool, entry, category_caps or set())
    if derived:
        return truncate(derived, 200), ZH_DERIVED

    # Tier 4: keep the English rather than invent a translation.
    summary = analysis.get("summary_en") or entry.get("description") or ""
    english = best_description(summary, highlights)
    if not english:
        english = (entry.get("description") or "").strip()

    # English that is clearly not prose — a stray HTML attribute, a CLI prompt
    # snippet — is worse than a plain statement of what we do know.
    if not english or not is_descriptive(english):
        fallback = _zh_minimal(tool, entry, category_caps or set())
        if fallback:
            return fallback, ZH_DERIVED
        if english:
            return truncate(english, 200), ZH_ENGLISH
        return (
            "、".join(capability_label(c, "zh") for c in (tool.get("capabilities") or [])[:3]),
            ZH_DERIVED,
        )
    # Some projects write Chinese in their main README without naming the file
    # README.zh-CN.md, so "summary_en" holds Chinese. Marking that with † would
    # tell the reader it is untranslated English when it is the author's own
    # words.
    if has_cjk(english) and cjk_ratio(english) >= 0.3:
        return truncate(english, 200), ZH_NATIVE
    return truncate(english, 200), ZH_ENGLISH


def _zh_minimal(
    tool: dict[str, Any],
    entry: dict[str, Any],
    category_caps: set[str],
) -> str:
    """A last-resort Chinese line when the tool has nothing distinctive.

    Says what the tool is *for* — its category's purpose — plus the interfaces
    it offers. Deliberately modest: it is better to state the obvious in Chinese
    than to show a reader a broken HTML fragment because the README had no
    usable prose.
    """
    analysis = entry.get("analysis") or {}
    caps = set(tool.get("capabilities") or analysis.get("capabilities") or [])
    agents = tool.get("agents") or analysis.get("agents") or []
    if not caps:
        return ""

    clauses: list[str] = []
    # Capabilities this tool has that its category is not already about.
    extra = sorted(caps - category_caps)
    if extra:
        clauses.append("、".join(capability_label(c, "zh") for c in extra[:3]))
    if agents:
        clauses.append("兼容 " + "、".join(agents[:4]))
    if not clauses:
        return ""
    return "；".join(clauses) + "。"


def _reason(edge: dict[str, Any], lang: str = "en", keyword: str = "") -> str:
    """Pick an edge's explanation in the requested language.

    Chinese reasons are positionally aligned with the English ones; a missing
    Chinese entry falls back to the English string rather than being machine
    translated, matching how tool descriptions are handled.
    """
    en = edge.get("reasons") or []
    if lang == "zh":
        zh = edge.get("reasons_zh") or []
        pairs = list(zip(en, zh + [""] * max(0, len(en) - len(zh))))
        if keyword:
            for english, chinese in pairs:
                if keyword in english:
                    return chinese or english
            return ""
        if pairs:
            english, chinese = pairs[0]
            return chinese or english
        return ""
    if keyword:
        return next((r for r in en if keyword in r), "")
    return en[0] if en else ""


def _curated_note(full_name: str, lang: str) -> str:
    """A human-written description from ``config/overrides.json``, if present."""
    overrides = _overrides()
    notes = overrides.get("notes") or {}
    spec = notes.get(full_name) or notes.get(full_name.lower()) or {}
    return (spec.get(f"summary_{lang}") or "").strip()


@lru_cache(maxsize=1)
def _overrides() -> dict[str, Any]:
    from .util import CONFIG_DIR, read_json

    return read_json(CONFIG_DIR / "overrides.json", default={}) or {}


def _anchor(title: str) -> str:
    """GitHub's heading anchor for a category title."""
    text = title.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # drop &, punctuation
    text = re.sub(r"\s+", "-", text.strip())
    return text


def _tool_anchor(full_name: str) -> str:
    return full_name.replace("/", "").replace(".", "").lower()


def _project() -> dict[str, Any]:
    from .util import CONFIG_DIR, read_json

    data = read_json(CONFIG_DIR / "project.json", default={}) or {}
    return {
        "repo": data.get("repo") or "dparticle/awesome-agent-tools",
        "default_branch": data.get("default_branch") or "main",
        "name": data.get("name") or "Awesome Agent Tools",
    }


def _badges() -> str:
    """Shields.io badges driven by the published index.

    The repository slug comes from ``config/project.json`` rather than from the
    git remote: rendering must depend only on version-controlled inputs, or a
    fork and CI would produce different output from the same data.
    """
    project = _project()
    index_url = (
        f"https://raw.githubusercontent.com/{project['repo']}"
        f"/{project['default_branch']}/data/index.json"
    )
    encoded = quote(index_url, safe="")
    return "\n".join(
        [
            f"[![Tools](https://img.shields.io/badge/dynamic/json?url={encoded}&query=%24.counts.tools&label=tools&color=blue)](data/index.json)",
            f"[![Categories](https://img.shields.io/badge/dynamic/json?url={encoded}&query=%24.counts.categories&label=categories&color=informational)](data/index.json)",
            f"[![Retired](https://img.shields.io/badge/dynamic/json?url={encoded}&query=%24.counts.retired&label=retired&color=critical)](data/graveyard.json)",
            "[![Daily crawl](https://img.shields.io/badge/crawl-daily%20via%20GitHub%20Actions-2ea44f?logo=githubactions&logoColor=white)](.github/workflows/daily.yml)",
            "[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)",
            "[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        ]
    )


# --------------------------------------------------------------------------
# README
# --------------------------------------------------------------------------


def render_readme(index: dict[str, Any]) -> str:
    tools = index.get("tools", {})
    categories = index.get("categories", [])
    counts = index.get("counts", {})
    edges = index.get("supersede", [])

    live_by_category: dict[str, list[str]] = {}
    for name, tool in tools.items():
        if tool.get("state") == "active":
            live_by_category.setdefault(tool["category"], []).append(name)

    total_live = sum(len(v) for v in live_by_category.values())

    out: list[str] = []
    add = out.append

    add(GENERATED_BANNER)
    add("")
    add("# Awesome Agent Tools")
    add("")
    add(
        "> **Building an \"AGI\" out of the tools we already have.** No single agent is "
        "enough — one hits its quota, one cannot be reached from your phone, one forgets "
        "your project. This is the curated, continuously-verified map of the tools that "
        "patch those gaps, and of which ones have been overtaken."
    )
    add("")
    add(
        "**[中文说明](README.zh-CN.md)** · "
        "[Methodology](docs/METHODOLOGY.md) · "
        "[Elimination rules](docs/SUPERSEDE.md) · "
        "[Capability taxonomy](docs/TAXONOMY.md) · "
        "[Machine-readable index](data/index.json)"
    )
    add("")
    add(_badges())
    add("")
    add(
        f"**{total_live} tools** across **{counts.get('categories', 0)} categories** · "
        f"**{counts.get('retired', 0)} retired** into the [graveyard](#-the-graveyard) · "
        f"last rebuilt **{_now(index)}**"
    )
    add("")
    add("---")
    add("")

    # -- How to read this list -------------------------------------------
    add("## How to read this list")
    add("")
    add(
        "Every entry was scored from its **README**, not its tagline. The columns mean "
        "something specific:"
    )
    add("")
    add("| Column | Meaning |")
    add("| --- | --- |")
    add(
        "| **Setup** | 🟢 turnkey (installer or one-liner) · 🟡 needs config or a "
        "dependency · 🔴 expects you to build/self-host a stack |"
    )
    add(
        "| **OOTB** | Works after install with no source build, no server and at most "
        "trivial configuration. |"
    )
    add(
        "| **Non-dev** | A GUI or an explicit no-code story, and no server stack to run. "
        "✅ means a non-programmer has a realistic path in. |"
    )
    add(
        "| **Stars** | Total stars, with observed stars/day where we have history. 🚀 marks "
        "a fast riser. |"
    )
    add(
        "| **Score** | 0-100 health score: popularity, momentum, maintenance, docs and "
        "accessibility. See [METHODOLOGY](docs/METHODOLOGY.md). |"
    )
    add("")
    add(
        "**Tiers:** "
        + " · ".join(
            f"{TIER_ICON[t]} {TIER_LABEL[t]['en']}" for t in ("flagship", "recommended", "notable", "watchlist")
        )
    )
    add("")
    add("---")
    add("")

    # -- Table of contents ------------------------------------------------
    add("## Contents")
    add("")
    for category in categories:
        cat_id = category["id"]
        names = live_by_category.get(cat_id, [])
        if not names:
            continue
        title = category.get("title", {}).get("en", cat_id)
        add(f"- [{title}](#{_anchor(title)}) — {len(names)} tools")
    add("- [Cross-listed tools](#cross-listed-tools) — tools that span several categories")
    add("- [Challengers](#-challengers) — newer tools that may overtake an incumbent")
    add("- [The Graveyard](#-the-graveyard) — retired tools and why")
    add("- [Contributing](#contributing)")
    add("")
    add("---")
    add("")

    # -- Categories -------------------------------------------------------
    for category in categories:
        cat_id = category["id"]
        names = live_by_category.get(cat_id, [])
        if not names:
            continue

        title = category.get("title", {}).get("en", cat_id)
        tagline = category.get("tagline", {}).get("en", "")
        problem = category.get("problem", {}).get("en", "")

        add(f"## {title}")
        add("")
        if tagline:
            add(f"*{tagline}*")
            add("")
        if problem:
            add(problem)
            add("")

        ranked = sorted(
            names,
            key=lambda n: (
                tier_rank(tools[n].get("tier", "watchlist")),
                -int(tools[n].get("health_score", 0)),
            ),
        )
        shown = ranked[:MAX_CATEGORY_ROWS]

        add("| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |")
        add("| --- | --- | --- | --- | :---: | --- | :---: |")
        for name in shown:
            tool = tools[name]
            entry = _load_entry(tool["full_name"])
            tier = tool.get("tier", "watchlist")
            icon = TIER_ICON.get(tier, "")
            solves = _solves_line(entry, tool)
            add(
                f"| {icon} **[{tool['full_name']}]({entry.get('url', '#')})** "
                f"| {escape_table_cell(solves)} "
                f"| {_setup_cell(entry)} "
                f"| {'✅' if tool.get('out_of_the_box') else '—'} "
                f"| {_friendly_cell(entry)} "
                f"| {_stars_cell(entry)} "
                f"| **{tool.get('health_score', 0)}** |"
            )
        add("")

        # Tools whose primary home is elsewhere but which genuinely do this job.
        also_in = [
            n for n in category.get("also_in", []) if tools.get(n, {}).get("state") == "active"
        ]
        if also_in:
            links = ", ".join(
                f"[{tools[n]['full_name']}]({_load_entry(tools[n]['full_name']).get('url', '#')})"
                for n in also_in[:12]
            )
            extra = f" *(+{len(also_in) - 12} more)*" if len(also_in) > 12 else ""
            add(f"**Also does this:** {links}{extra}")
            add("")

        if len(ranked) > len(shown):
            add(f"*…and {len(ranked) - len(shown)} more in [the full index](data/index.json).*")
            add("")

        # Detail cards for the strongest tools in this category.
        detail = shown[:MAX_DETAIL_CARDS]
        if detail:
            add("<details>")
            add(f"<summary><b>Why these tools — {len(detail)} detailed breakdowns</b></summary>")
            add("")
            for name in detail:
                tool = tools[name]
                entry = _load_entry(tool["full_name"])
                add(_detail_card(entry, tool))
            add("</details>")
            add("")

    # -- Cross-listed tools -----------------------------------------------
    # A tool can genuinely belong to several problem areas — magpie does both
    # account management and model routing — so membership is a set rather than
    # a choice. This section makes that visible instead of hiding it.
    cross_listed = {
        name: tool
        for name, tool in tools.items()
        if tool.get("state") == "active" and len(tool.get("categories") or []) > 1
    }
    if cross_listed:
        titles = {c["id"]: c.get("title", {}).get("en", c["id"]) for c in categories}
        add("---")
        add("")
        add("## Cross-listed tools")
        add("")
        add(
            "These tools solve problems in more than one area, so they appear under "
            "several headings. Each is described in full only under its primary category."
        )
        add("")
        add("| Tool | Primary | Also listed under |")
        add("| --- | --- | --- |")
        for name, tool in sorted(
            cross_listed.items(), key=lambda kv: -int(kv[1].get("health_score", 0))
        ):
            entry = _load_entry(tool["full_name"])
            primary = titles.get(tool.get("category", ""), tool.get("category", ""))
            others = [
                titles.get(c, c)
                for c in tool.get("categories", [])
                if c != tool.get("category")
            ]
            add(
                f"| **[{tool['full_name']}]({entry.get('url', '#')})** "
                f"| {primary} | {', '.join(others)} |"
            )
        add("")

    # -- Challengers ------------------------------------------------------
    challengers = index.get("challengers", [])
    add("---")
    add("")
    add("## ⚔️ Challengers")
    add("")
    add(
        "A challenger covers an incumbent's ground and is rising, but has **not** yet met "
        "the bar for retirement — either it misses some of the incumbent's capabilities, or "
        "its traction is still far behind. These are the pairs to watch: they are where the "
        "next elimination is most likely to come from."
    )
    add("")
    if challengers:
        add("| Incumbent | Challenger | Coverage | Traction gap |")
        add("| --- | --- | ---: | --- |")
        for edge in challengers:
            inc = edge.get("incumbent_name") or edge["incumbent"]
            cha = edge.get("challenger_name") or edge["challenger"]
            coverage = f"{edge.get('coverage', 0):.0%}"
            gap = next(
                (r for r in edge.get("reasons", []) if "stars" in r),
                "not yet measured",
            )
            add(
                f"| **[{inc}](https://github.com/{edge['incumbent']})** "
                f"| **[{cha}](https://github.com/{edge['challenger']})** "
                f"| {coverage} | {escape_table_cell(gap)} |"
            )
        add("")
        for edge in challengers:
            inc = edge.get("incumbent_name") or edge["incumbent"]
            cha = edge.get("challenger_name") or edge["challenger"]
            note = (edge.get("reasons") or [""])[0]
            missing = (edge.get("evidence") or {}).get("missing_capabilities") or []
            add(f"<details><summary><b>{cha} vs {inc}</b></summary>")
            add("")
            if note:
                add(note)
                add("")
            if missing:
                labels = ", ".join(capability_label(c) for c in missing)
                add(f"**Not covered:** {labels}")
                add("")
            add("</details>")
            add("")
    else:
        add("*No challengers recorded yet.*")
        add("")

    # -- Graveyard --------------------------------------------------------
    add("---")
    add("")
    add("## 🪦 The Graveyard")
    add("")
    add(
        "There is always a dark horse. When a newer tool covers **every** capability of an "
        "incumbent, matches its traction and is no harder to set up, the incumbent is "
        "retired here rather than quietly left in the list. "
        "Full rules: [docs/SUPERSEDE.md](docs/SUPERSEDE.md)."
    )
    add("")

    if edges:
        add("### Recorded eliminations")
        add("")
        add("| Retired | Replaced by | Why it lost | Source |")
        add("| --- | --- | --- | --- |")
        for edge in edges:
            incumbent_name = edge.get("incumbent_name") or edge["incumbent"]
            challenger_name = edge.get("challenger_name") or edge["challenger"]
            reason = _elimination_reason(edge)
            kind = "👤 curated" if edge.get("source") == "curated" else f"🤖 auto ({edge.get('confidence', '')})"
            add(
                f"| **[{incumbent_name}](https://github.com/{edge['incumbent']})** "
                f"| **[{challenger_name}](https://github.com/{edge['challenger']})** "
                f"| {escape_table_cell(reason)} | {kind} |"
            )
        add("")

    retired_tools = {
        name: tool for name, tool in tools.items() if tool.get("state") in {"superseded", "deprecated", "archived"}
    }
    if retired_tools:
        add("### Retired tools")
        add("")
        add("| Tool | Category | Stars | Status | Note |")
        add("| --- | --- | --- | --- | --- |")
        for name, tool in sorted(retired_tools.items(), key=lambda kv: -kv[1].get("stars", 0)):
            entry = _load_entry(tool["full_name"])
            state = tool.get("state", "deprecated")
            lifecycle = entry.get("lifecycle") or {}
            note = lifecycle.get("note_en", "")
            # The generated note repeats "Superseded by X: covers 100%…" for
            # every auto edge, which is already in the table above. Prefer the
            # curated note; otherwise state the distinguishing fact.
            edge = lifecycle.get("supersede") or {}
            if not note or note.startswith("Superseded by"):
                if edge.get("source") == "curated":
                    note = edge.get("reasons", [""])[0]
                else:
                    note = _elimination_reason(edge) or note
            add(
                f"| **[{tool['full_name']}]({entry.get('url', '#')})** "
                f"| {tool.get('category', '')} "
                f"| {human_number(tool.get('stars', 0))} "
                f"| {STATE_ICON.get(state, '')} {STATE_LABEL.get(state, {}).get('en', state)} "
                f"| {escape_table_cell(truncate(note, 120))} |"
            )
        add("")
    else:
        add("*No tools have been retired yet. The engine is watching.*")
        add("")

    # -- Contributing -----------------------------------------------------
    add("---")
    add("")
    add("## Contributing")
    add("")
    add(
        "Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):"
    )
    add("")
    add(
        "1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the "
        "category you think it belongs to. The next crawl evaluates it against the same "
        "gates as everything else."
    )
    add(
        "2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was "
        "misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue "
        "quoting the evidence line from the tool's page."
    )
    add("")
    add(
        "The pipeline runs daily at 04:17 UTC "
        "([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, "
        "never hand-edited."
    )
    add("")
    add("---")
    add("")
    add(
        f"<sub>Generated by `agentindex` v1.0.0 on {_now(index)}. "
        f"{total_live} live tools · {counts.get('rejected', 0)} candidates rejected by the quality gates.</sub>"
    )
    add("")

    return "\n".join(out)


def _elimination_reason(edge: dict[str, Any]) -> str:
    """Summarise *why* the incumbent lost, in the reader's terms.

    "covers 100% of capabilities" is true of every edge by construction, so it
    carries no information in a table. The discriminating facts are traction
    (stars and velocity) and adoption cost, which is what a reader deciding
    whether to migrate actually cares about.
    """
    reasons = edge.get("reasons") or []
    # Prefer the stars line, then velocity, then setup, then anything else.
    for keyword in ("stars", "velocity", "set up", "setup"):
        for reason in reasons:
            if keyword in reason:
                return reason
    if edge.get("source") == "curated":
        return reasons[0] if reasons else "curated supersede decision"
    return reasons[0] if reasons else ""


def _solves_line(entry: dict[str, Any], tool: dict[str, Any]) -> str:
    """One line answering 'what does this tool actually do?'

    Built from the tool's own README: its opening sentence when that is
    substantive, otherwise its most concrete feature bullet. This deliberately
    avoids restating the category name — a reader already knows which section
    they are in, so an entry reading "multi-account switching" under a heading
    called Accounts is noise.

    The shape follows the conventions high-quality awesome lists converge on:
    lead with what it is, then name the distinguishing mechanism.
    """
    analysis = entry.get("analysis") or {}
    summary = analysis.get("summary_en") or entry.get("description") or ""
    highlights = analysis.get("highlights") or []
    text = best_description(summary, highlights)
    if not text:
        text = (entry.get("description") or "").strip()
    return truncate(text, 220)


def _detail_card(entry: dict[str, Any], tool: dict[str, Any]) -> str:
    analysis = entry.get("analysis") or {}
    friction = analysis.get("friction") or {}
    lines: list[str] = []

    lines.append(f"#### [{entry.get('full_name')}]({entry.get('url', '#')})")
    lines.append("")
    summary = analysis.get("summary_en") or entry.get("description") or ""
    if summary:
        lines.append(f"> {summary}")
        lines.append("")

    # Capabilities as "what it solves".
    caps = analysis.get("capabilities") or []
    if caps:
        lines.append("**Core problems it solves**")
        lines.append("")
        for cap in caps[:8]:
            label = capability_label(cap)
            evidence = (analysis.get("capability_evidence") or {}).get(cap, "")
            if evidence:
                lines.append(f"- **{label}** — *{truncate(evidence, 150)}*")
            else:
                lines.append(f"- **{label}**")
        lines.append("")

    # Setup reality.
    lines.append("**Getting it running**")
    lines.append("")
    level = friction.get("level", "unknown")
    lines.append(
        f"- Setup: {SETUP_ICON.get(level, '⚪')} **{SETUP_LABEL.get(level, SETUP_LABEL['unknown'])['en']}** "
        f"(friction {friction.get('score', '?')}/100)"
    )
    lines.append(f"- Out of the box: {'**yes**' if friction.get('out_of_the_box') else 'no'}")
    lines.append(
        f"- Non-programmer friendly: {'**yes**' if friction.get('non_programmer_friendly') else 'no'}"
    )
    if analysis.get("install_hint"):
        lines.append(f"- Quickest install: `{analysis['install_hint']}`")
    if friction.get("platforms"):
        lines.append(f"- Platforms mentioned: {', '.join(friction['platforms'])}")
    if friction.get("note_en"):
        lines.append(f"- {friction['note_en']}")
    lines.append("")

    # Facts.
    lines.append("**Facts**")
    lines.append("")
    momentum = entry.get("momentum") or {}
    lines.append(
        f"- Stars: **{entry.get('stars', 0):,}**"
        + (
            f" (+{momentum.get('stars_per_day', 0):.1f}/day over {momentum.get('days_span', 0)}d)"
            if momentum.get("basis") == "history"
            else f" (~{momentum.get('lifetime_stars_per_day', 0):.1f}/day lifetime average)"
        )
    )
    lines.append(f"- Health score: **{entry.get('health_score', 0)}/100**")
    lines.append(f"- Documentation score: **{analysis.get('doc_score', 0)}/100**")
    if entry.get("license"):
        lines.append(f"- License: {entry['license']}")
    if entry.get("language"):
        lines.append(f"- Language: {entry['language']}")
    lines.append(f"- Last push: {str(entry.get('pushed_at', ''))[:10]}")
    if analysis.get("agents"):
        lines.append(f"- Works with: {', '.join(analysis['agents'][:6])}")
    if entry.get("discovery", {}).get("seed_reason"):
        lines.append(f"- *Why it is seeded: {entry['discovery']['seed_reason']}*")
    lines.append("")

    # Supersede note.
    lifecycle = entry.get("lifecycle") or {}
    if lifecycle.get("superseded_by"):
        lines.append(
            f"> ⚠️ **Superseded by [{lifecycle['superseded_by']}]"
            f"(https://github.com/{lifecycle['superseded_by']})** — {lifecycle.get('note_en', '')}"
        )
        lines.append("")

    return "\n".join(lines)


# --------------------------------------------------------------------------
# Chinese README
# --------------------------------------------------------------------------


def render_readme_zh(index: dict[str, Any]) -> str:
    tools = index.get("tools", {})
    categories = index.get("categories", [])
    counts = index.get("counts", {})
    edges = index.get("supersede", [])

    live_by_category: dict[str, list[str]] = {}
    for name, tool in tools.items():
        if tool.get("state") == "active":
            live_by_category.setdefault(tool["category"], []).append(name)
    total_live = sum(len(v) for v in live_by_category.values())

    # Compute every Chinese description up front. The legend states how many
    # entries are quoted in Chinese versus left in English, so the counts have
    # to come from the same function that renders the rows — deriving them
    # separately produced a legend claiming 25 while 185 rows carried the
    # marker.
    descriptions: dict[str, tuple[str, str]] = {}
    # Only the top capabilities define a category; filtering the whole signature
    # would leave too little for a useful derived summary.
    category_caps_by_id = {
        c["id"]: set((c.get("capabilities") or [])[:3]) for c in categories
    }

    # Work out which rows will actually be rendered before writing the legend.
    # Categories are capped at MAX_CATEGORY_ROWS, so counting every live tool
    # made the legend claim one more Chinese entry than the reader could find.
    displayed: list[str] = []
    for category in categories:
        names = live_by_category.get(category["id"], [])
        if not names:
            continue
        ranked = sorted(
            names,
            key=lambda n: (
                tier_rank(tools[n].get("tier", "watchlist")),
                -int(tools[n].get("health_score", 0)),
            ),
        )
        displayed.extend(ranked[:MAX_CATEGORY_ROWS])

    for name in displayed:
        tool = tools[name]
        entry = _load_entry(tool["full_name"])
        analysis = entry.get("analysis") or {}
        descriptions[name] = _zh_description(
            tool,
            entry,
            analysis,
            analysis.get("highlights") or [],
            category_caps_by_id.get(tool.get("category", ""), set()),
        )
    tiers = Counter(tier for _text, tier in descriptions.values())
    native_zh_count = tiers[ZH_NATIVE] + tiers[ZH_CURATED]

    out: list[str] = []
    add = out.append

    add(GENERATED_BANNER)
    add("")
    add("# Awesome Agent Tools 中文版")
    add("")
    add(
        "> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、"
        "新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。"
    )
    add("")
    add(
        "**[English](README.md)** · "
        "[方法论](docs/METHODOLOGY.md) · "
        "[淘汰规则](docs/SUPERSEDE.md) · "
        "[能力分类法](docs/TAXONOMY.md) · "
        "[机器可读索引](data/index.json)"
    )
    add("")
    add(
        f"**{total_live} 个工具**，分 **{counts.get('categories', 0)} 个分类** · "
        f"**{counts.get('retired', 0)} 个已淘汰**（见[淘汰区](#-淘汰区)） · "
        f"最近更新 **{_now(index)}**"
    )
    add("")
    add("---")
    add("")

    add("## 怎么读这份清单")
    add("")
    add("所有结论都来自对 **README 正文的分析**，而不是仓库简介。各列含义：")
    add("")
    add("| 列 | 含义 |")
    add("| --- | --- |")
    add("| **上手难度** | 🟢 开箱即用（有安装包或一行命令）· 🟡 需要配置或依赖 · 🔴 需要自行构建/自建服务 |")
    add("| **开箱即用** | 装完就能用：不需要从源码构建、不需要起服务、最多改一点配置 |")
    add("| **非程序员友好** | 有图形界面或明确的无代码方案，且不需要自己运维服务。✅ 表示非程序员有现实可行路径 |")
    add("| **Star** | 总 star 数，括号内是观测到的日均增长。🚀 表示近期涨得很快 |")
    add("| **评分** | 0-100 健康分：流行度、增长势头、维护活跃度、文档质量、上手难度。详见[方法论](docs/METHODOLOGY.md) |")
    add("")
    add(
        f"**关于「解决什么问题」这一列：** 尽量用中文说明。来源分三档，"
        f"标记不同，可信度也不同："
    )
    add("")
    add("| 标记 | 来源 | 数量 |")
    add("| --- | --- | ---: |")
    add(
        f"| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | {native_zh_count} |"
    )
    add(
        f"| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | {tiers[ZH_DERIVED]} |"
    )
    add(
        f"| † | 项目只写了英文，**保留英文原文，不做机器翻译** | {tiers[ZH_ENGLISH]} |"
    )
    add("")
    add(
        "带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，"
        "而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。"
        "带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。"
    )
    add("")
    add(
        "如果你想补齐某个工具的中文说明，欢迎在 "
        "[`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，"
        "它会以最高优先级显示。"
    )
    add("")
    add("---")
    add("")

    for category in categories:
        cat_id = category["id"]
        names = live_by_category.get(cat_id, [])
        if not names:
            continue

        title = category.get("title", {}).get("zh") or category.get("title", {}).get("en", cat_id)
        tagline = category.get("tagline", {}).get("zh", "")
        problem = category.get("problem", {}).get("zh", "")

        add(f"## {title}")
        add("")
        if tagline:
            add(f"*{tagline}*")
            add("")
        if problem:
            add(problem)
            add("")

        ranked = sorted(
            names,
            key=lambda n: (
                tier_rank(tools[n].get("tier", "watchlist")),
                -int(tools[n].get("health_score", 0)),
            ),
        )
        shown = ranked[:MAX_CATEGORY_ROWS]

        add("| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |")
        add("| --- | --- | --- | :---: | :---: | --- | :---: |")
        for name in shown:
            tool = tools[name]
            entry = _load_entry(tool["full_name"])
            tier = tool.get("tier", "watchlist")
            icon = TIER_ICON.get(tier, "")
            analysis = entry.get("analysis") or {}
            highlights = analysis.get("highlights") or []
            solves, tier = descriptions.get(
                name, _zh_description(tool, entry, analysis, highlights)
            )
            # A marker tells the reader where the sentence came from: ours, or
            # the project's English kept untranslated.
            marker = ZH_MARKER.get(tier, "")
            friction = analysis.get("friction") or {}
            level = friction.get("level", "unknown")
            setup = f"{SETUP_ICON.get(level, '⚪')} {SETUP_LABEL.get(level, SETUP_LABEL['unknown'])['zh']}"
            add(
                f"| {icon} **[{tool['full_name']}]({entry.get('url', '#')})** "
                f"| {escape_table_cell(solves)}{marker} "
                f"| {setup} "
                f"| {'✅' if tool.get('out_of_the_box') else '—'} "
                f"| {_friendly_cell(entry)} "
                f"| {_stars_cell(entry)} "
                f"| **{tool.get('health_score', 0)}** |"
            )
        add("")
        if len(ranked) > len(shown):
            add(f"*还有 {len(ranked) - len(shown)} 个工具见[完整索引](data/index.json)。*")
            add("")

        also_in = [
            n for n in category.get("also_in", []) if tools.get(n, {}).get("state") == "active"
        ]
        if also_in:
            links = "、".join(
                f"[{tools[n]['full_name']}]({_load_entry(tools[n]['full_name']).get('url', '#')})"
                for n in also_in[:10]
            )
            add(f"**也能做这件事：** {links}")
            add("")

    # -- 挑战者 -----------------------------------------------------------
    challengers = index.get("challengers", [])
    add("---")
    add("")
    add("## ⚔️ 挑战者")
    add("")
    add(
        "挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——"
        "要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，"
        "下一次真正的淘汰最可能从它们之中产生。"
    )
    add("")
    if challengers:
        add("| 在位者 | 挑战者 | 覆盖度 | 热度差距 |")
        add("| --- | --- | ---: | --- |")
        for edge in challengers:
            inc = edge.get("incumbent_name") or edge["incumbent"]
            cha = edge.get("challenger_name") or edge["challenger"]
            gap = _reason(edge, "zh", "stars") or "尚未测算"
            add(
                f"| **[{inc}](https://github.com/{edge['incumbent']})** "
                f"| **[{cha}](https://github.com/{edge['challenger']})** "
                f"| {edge.get('coverage', 0):.0%} | {escape_table_cell(gap)} |"
            )
        add("")
        for edge in challengers:
            inc = edge.get("incumbent_name") or edge["incumbent"]
            cha = edge.get("challenger_name") or edge["challenger"]
            missing = (edge.get("evidence") or {}).get("missing_capabilities") or []
            add(f"<details><summary><b>{cha} 对比 {inc}</b></summary>")
            add("")
            note = _reason(edge, "zh")
            if note:
                add(note)
                add("")
            if missing:
                add(f"**未覆盖：** {'、'.join(capability_label(c, 'zh') for c in missing)}")
                add("")
            add("</details>")
            add("")
    else:
        add("*目前还没有记录挑战者。*")
        add("")

    add("---")
    add("")
    add("## 🪦 淘汰区")
    add("")
    add(
        "永远会有黑马出现。当新工具**完整覆盖**了旧工具的所有能力、热度不输、上手难度也不更高时，"
        "旧工具就会被移到这里，而不是悄悄留在推荐列表里。完整规则见 [docs/SUPERSEDE.md](docs/SUPERSEDE.md)。"
    )
    add("")

    if edges:
        add("### 已记录的取代关系")
        add("")
        add("| 被淘汰 | 取代者 | 落败原因 | 来源 |")
        add("| --- | --- | --- | --- |")
        for edge in edges:
            incumbent_name = edge.get("incumbent_name") or edge["incumbent"]
            challenger_name = edge.get("challenger_name") or edge["challenger"]
            reason = _elimination_reason(edge)
            kind = "👤 人工" if edge.get("source") == "curated" else f"🤖 自动（{edge.get('confidence', '')}）"
            add(
                f"| **[{incumbent_name}](https://github.com/{edge['incumbent']})** "
                f"| **[{challenger_name}](https://github.com/{edge['challenger']})** "
                f"| {escape_table_cell(reason)} | {kind} |"
            )
        add("")

    retired_tools = {
        name: tool for name, tool in tools.items() if tool.get("state") in {"superseded", "deprecated", "archived"}
    }
    if retired_tools:
        add("### 已淘汰工具")
        add("")
        add("| 工具 | 分类 | Star | 状态 | 说明 |")
        add("| --- | --- | --- | --- | --- |")
        for name, tool in sorted(retired_tools.items(), key=lambda kv: -kv[1].get("stars", 0)):
            entry = _load_entry(tool["full_name"])
            state = tool.get("state", "deprecated")
            note = (entry.get("lifecycle") or {}).get("note_zh") or (entry.get("lifecycle") or {}).get("note_en", "")
            add(
                f"| **[{tool['full_name']}]({entry.get('url', '#')})** "
                f"| {tool.get('category', '')} "
                f"| {human_number(tool.get('stars', 0))} "
                f"| {STATE_ICON.get(state, '')} {STATE_LABEL.get(state, {}).get('zh', state)} "
                f"| {escape_table_cell(truncate(note, 120))} |"
            )
        add("")
    else:
        add("*目前还没有工具被淘汰。引擎在持续观察。*")
        add("")

    add("---")
    add("")
    add("## 参与贡献")
    add("")
    add("详见 [CONTRIBUTING.md](CONTRIBUTING.md)：")
    add("")
    add("1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。")
    add("2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，"
        "或开 issue 并引用该工具页面上的证据句。")
    add("")
    add(f"<sub>由 `agentindex` 于 {_now(index)} 生成，所有数字均为自动重建，不手工编辑。</sub>")
    add("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Per-tool pages
# --------------------------------------------------------------------------


def render_tool_page(entry: dict[str, Any]) -> str:
    analysis = entry.get("analysis") or {}
    friction = analysis.get("friction") or {}
    momentum = entry.get("momentum") or {}
    lifecycle = entry.get("lifecycle") or {}

    out: list[str] = []
    add = out.append

    add(GENERATED_BANNER)
    add("")
    add(f"# {entry['full_name']}")
    add("")
    summary = analysis.get("summary_en") or entry.get("description") or ""
    if summary:
        add(f"> {summary}")
        add("")
    add(
        f"[Repository]({entry.get('url')}) · "
        f"[Back to index](../../README.md) · "
        f"Category: **{entry.get('category')}**"
    )
    add("")
    add("---")
    add("")

    add("## Snapshot")
    add("")
    add("| Metric | Value |")
    add("| --- | --- |")
    add(f"| Stars | {entry.get('stars', 0):,} |")
    add(
        f"| Star velocity | {momentum.get('stars_per_day', 0):.1f}/day "
        f"({momentum.get('basis', 'unknown')} basis, {momentum.get('days_span', 0)}d span) |"
    )
    add(f"| Health score | {entry.get('health_score', 0)}/100 |")
    add(f"| Documentation | {analysis.get('doc_score', 0)}/100 |")
    add(f"| Tier | {TIER_ICON.get(entry.get('tier', ''), '')} {TIER_LABEL.get(entry.get('tier', ''), {}).get('en', '')} |")
    add(f"| Lifecycle | {STATE_ICON.get(lifecycle.get('state', ''), '')} {STATE_LABEL.get(lifecycle.get('state', ''), {}).get('en', '')} |")
    add(f"| License | {entry.get('license') or 'not declared'} |")
    add(f"| Language | {entry.get('language') or 'n/a'} |")
    add(f"| Created | {str(entry.get('created_at', ''))[:10]} |")
    add(f"| Last push | {str(entry.get('pushed_at', ''))[:10]} ({entry.get('days_since_push', 0)} days ago) |")
    add(f"| Analyzed README | {analysis.get('readme_chars', 0):,} chars from `{analysis.get('source', '?')}` |")
    add("")

    if lifecycle.get("superseded_by"):
        add(
            f"> ⚠️ **Superseded by [{lifecycle['superseded_by']}]"
            f"(https://github.com/{lifecycle['superseded_by']})** — {lifecycle.get('note_en', '')}"
        )
        add("")

    add("## What it solves")
    add("")
    caps = analysis.get("capabilities") or []
    if caps:
        for cap in caps:
            label = capability_label(cap)
            evidence = (analysis.get("capability_evidence") or {}).get(cap, "")
            add(f"### {label}")
            add("")
            if evidence:
                add(f"> {evidence}")
                add("")
    else:
        add("*No capabilities could be detected from the README.*")
        add("")

    add("## Setup reality check")
    add("")
    add(f"- **Difficulty:** {SETUP_ICON.get(friction.get('level', ''), '⚪')} "
        f"{SETUP_LABEL.get(friction.get('level', ''), SETUP_LABEL['unknown'])['en']} "
        f"(friction score {friction.get('score', '?')}/100)")
    add(f"- **Out of the box:** {'yes' if friction.get('out_of_the_box') else 'no'}")
    add(f"- **Non-programmer friendly:** {'yes' if friction.get('non_programmer_friendly') else 'no'}")
    if analysis.get("install_hint"):
        add(f"- **Quickest install:** `{analysis['install_hint']}`")
    add("")
    if friction.get("easy_signals"):
        add(f"**Signals that make it easy:** {', '.join(friction['easy_signals'])}")
        add("")
    if friction.get("hard_signals"):
        add(f"**Signals that add work:** {', '.join(friction['hard_signals'])}")
        add("")
    if friction.get("config_signals"):
        add(f"**Configuration required:** {', '.join(friction['config_signals'])}")
        add("")
    if friction.get("note_en"):
        add(f"*{friction['note_en']}*")
        add("")

    add("## Documentation quality")
    add("")
    add(f"Score **{analysis.get('doc_score', 0)}/100**, based on these detected signals:")
    add("")
    for signal in analysis.get("doc_signals", []):
        add(f"- {signal}")
    add("")

    add("## Score breakdown")
    add("")
    add("| Component | Score |")
    add("| --- | ---: |")
    for key, value in (entry.get("health_components") or {}).items():
        add(f"| {key} | {value} |")
    add("")

    add("---")
    add("")
    add(
        "<sub>Generated by `agentindex`. Every field is derived from the repository's own "
        "README and GitHub metadata; nothing here is hand-written.</sub>"
    )
    add("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Docs
# --------------------------------------------------------------------------


def render_taxonomy(index: dict[str, Any]) -> str:
    tools = index.get("tools", {})
    from .readme_analysis import capabilities as all_caps

    out: list[str] = [GENERATED_BANNER, "", "# Category taxonomy", ""]
    out.append(
        "**Categories in this list are discovered, not declared.** No file lists them. "
        "Every run clusters the indexed tools by how prominently their READMEs document "
        "each capability, and the resulting groups become the sections you see. Adding a "
        "tool can therefore change the taxonomy, and a section that stops being distinct "
        "disappears on its own."
    )
    out.append("")
    out.append("## How a category is derived")
    out.append("")
    out.append(
        "1. Each capability is weighted by **inverse document frequency**, so a capability "
        "that nearly every tool claims contributes almost nothing."
    )
    out.append(
        "2. Each tool becomes a normalised vector of `idf × log(1 + mentions)` — what it "
        "*emphasises*, not merely what it mentions."
    )
    out.append(
        "3. Tools are clustered by cosine similarity using agglomerative average linkage, "
        "stopping at a similarity threshold."
    )
    out.append(
        "4. A cluster is named from the capabilities where it has the highest **lift** "
        "against the corpus, so the title reflects what makes the group distinct."
    )
    out.append("")
    out.append(
        "Capabilities claimed by more than 60% of tools are excluded from clustering: they "
        "describe the whole ecosystem, and including them collapsed every tool into a "
        "single section during development."
    )
    out.append("")
    out.append("## Categories")
    out.append("")
    out.append("| Category | Tools | Also in | Cohesion | Defining capabilities |")
    out.append("| --- | ---: | ---: | ---: | --- |")
    for category in index.get("categories", []):
        title = category.get("title", {}).get("en", category["id"])
        caps = ", ".join(capability_label(c) for c in (category.get("capabilities") or [])[:4])
        out.append(
            f"| **{title}** | {len(category.get('tools', []))} "
            f"| {len(category.get('also_in', []))} "
            f"| {category.get('cohesion', 0):.2f} "
            f"| {escape_table_cell(caps)} |"
        )
    out.append("")
    out.append(
        "*Cohesion* is the mean cosine similarity of a category's members to its centroid: "
        "higher means a tighter, more coherent group."
    )
    out.append("")
    out.append("## Multi-category membership")
    out.append("")
    cross = sum(1 for t in tools.values() if len(t.get("categories") or []) > 1)
    out.append(
        f"{cross} of {len(tools)} tools belong to more than one category. A tool is "
        "cross-listed when it shares at least two of another category's defining "
        "capabilities, capped at three categories so the signal stays meaningful. It is "
        "described in full only under its primary category — the one whose centroid it is "
        "closest to."
    )
    out.append("")
    out.append("## Capabilities")
    out.append("")
    out.append("| Capability | Problem it addresses | Patterns | Tools |")
    out.append("| --- | --- | ---: | ---: |")
    for cap in all_caps():
        cap_id = cap["id"]
        count = sum(1 for t in tools.values() if cap_id in (t.get("capabilities") or []))
        out.append(
            f"| **{cap['label']['en']}** / {cap['label']['zh']} "
            f"| {escape_table_cell(cap.get('problem', {}).get('en', ''))} "
            f"| {len(cap.get('patterns', []))} "
            f"| {count} |"
        )
    out.append("")
    return "\n".join(out)


def render_methodology(index: dict[str, Any]) -> str:
    from .scoring import load_thresholds

    cfg = load_thresholds()
    gates = cfg.get("gates", {})
    weights = cfg.get("weights", {})
    tiers = cfg.get("tiers", {})

    out: list[str] = [GENERATED_BANNER, "", "# Methodology", ""]
    out.append(
        "This list is generated, not curated by hand. Understanding the rules is enough to "
        "predict exactly what will and will not appear."
    )
    out.append("")

    out.append("## 1. Discovery")
    out.append("")
    out.append(
        "Every day the crawler runs the queries in "
        "[`config/categories.json`](../config/categories.json), plus a **rising pass** that "
        "asks GitHub for recently created repositories with traction. The rising pass is what "
        "lets a dark horse be discovered before it has more stars than the incumbents."
    )
    out.append("")
    out.append(
        "Hand-picked entries in [`config/seeds.json`](../config/seeds.json) are always "
        "evaluated. Seeding guarantees evaluation, not inclusion."
    )
    out.append("")

    out.append("## 2. Quality gates")
    out.append("")
    out.append("A candidate must clear every gate to be listed:")
    out.append("")
    out.append("| Gate | Threshold |")
    out.append("| --- | --- |")
    out.append(f"| Stars | ≥ {gates.get('min_stars')} — *or* a fast riser (≥ {gates.get('fast_riser_stars_14d')} stars projected per 14 days) |")
    out.append(f"| Recency | pushed within {gates.get('max_days_since_push')} days |")
    out.append(f"| Age | at least {gates.get('min_age_days')} days old |")
    out.append(f"| Documentation | doc score ≥ {gates.get('min_doc_score')}/100 |")
    out.append(f"| README | at least {gates.get('min_readme_chars')} characters |")
    out.append("| Archived | excluded |")
    out.append("")

    out.append("## 3. README analysis")
    out.append("")
    out.append(
        "The GitHub `description` field is a tagline, so nothing here relies on it. The "
        "crawler downloads the README and derives:"
    )
    out.append("")
    out.append("- **Capabilities** — which of the catalogue's problems this tool addresses.")
    out.append("- **Setup difficulty** — matched install and configuration signals, scored 0 (turnkey) to 100 (heavy).")
    out.append("- **Out of the box** — installable without a source build or a server stack.")
    out.append("- **Non-programmer friendly** — a GUI or an explicit no-code path, and no server to run.")
    out.append("- **Documentation score** — structural signals (quick start, config docs, FAQ, screenshots, code blocks…).")
    out.append("")
    out.append(
        "Negation is handled: a capability mentioned only inside \"not supported\" or "
        "\"planned\" phrasing is not credited."
    )
    out.append("")

    out.append("## 4. Health score")
    out.append("")
    out.append("| Component | Weight | What it measures |")
    out.append("| --- | ---: | --- |")
    labels = {
        "popularity": "log-scaled stars — other people already found the bugs",
        "momentum": "observed stars/day, saturated at the 99th percentile",
        "maintenance": "recency of the last push, with hard penalties for abandonment",
        "documentation": "README documentation score",
        "accessibility": "inverse of setup friction, bonused for turnkey and non-dev friendly",
    }
    for key, value in weights.items():
        if key.startswith("$"):
            continue
        out.append(f"| `{key}` | {value:.0%} | {labels.get(key, '')} |")
    out.append("")
    out.append("Tiers:")
    out.append("")
    out.append("| Tier | Minimum score |")
    out.append("| --- | ---: |")
    for tier in ("flagship", "recommended", "notable", "watchlist"):
        out.append(f"| {TIER_ICON[tier]} {TIER_LABEL[tier]['en']} | {tiers.get(tier, {}).get('min_score', 0)} |")
    out.append("")

    out.append("## 5. Momentum measurement")
    out.append("")
    out.append(
        "Momentum is measured from `data/history/<tool>.json`, a rolling star snapshot taken "
        "once per day. On the very first run there is no history, so the crawler falls back "
        "to lifetime stars/day — a good proxy for young repos and a conservative one for old "
        "repos. From the second run onward, growth is **observed**, not inferred."
    )
    out.append("")

    out.append("## 6. Category discovery")
    out.append("")
    out.append(
        "Categories are **not declared anywhere**. Each run clusters the indexed tools by "
        "how prominently their READMEs document each capability, and the clusters become "
        "the sections. See [TAXONOMY.md](TAXONOMY.md) for the algorithm and why the obvious "
        "approaches fail on this data."
    )
    out.append("")
    out.append(
        "A tool may belong to several categories at once, because tools genuinely span "
        "problem areas. It is described in full only under its primary category."
    )
    out.append("")

    out.append("## 7. Elimination")
    out.append("")
    out.append("See [SUPERSEDE.md](SUPERSEDE.md) for the full rule set.")
    out.append("")

    out.append("## Reproducing")
    out.append("")
    out.append("```bash")
    out.append("python scripts/agentindex.py build     # crawl + render")
    out.append("python scripts/agentindex.py validate  # check data/index.json")
    out.append("python scripts/agentindex.py stats     # summarise")
    out.append("```")
    out.append("")
    out.append(
        "No third-party dependencies — the pipeline runs on a bare Python 3.11+ "
        "interpreter, which is also why the GitHub Actions workflow needs no install step."
    )
    out.append("")
    return "\n".join(out)


def render_supersede_doc(index: dict[str, Any]) -> str:
    from .scoring import load_thresholds

    cfg = load_thresholds().get("supersede", {})
    edges = index.get("supersede", [])

    out: list[str] = [GENERATED_BANNER, "", "# The elimination engine", ""]
    out.append(
        "> There is always a dark horse. A curated list that only ever grows becomes a "
        "museum — eventually it recommends tools nobody should install."
    )
    out.append("")
    out.append(
        "When a newer tool **strictly covers** an incumbent, the incumbent is retired into "
        "the [graveyard](../README.md#-the-graveyard) with the evidence that retired it."
    )
    out.append("")

    out.append("## The rules")
    out.append("")
    out.append(
        "An edge `challenger → incumbent` is recorded only when **all** of the following hold. "
        "Each rule exists because dropping it produced a false elimination in testing."
    )
    out.append("")
    out.append("| # | Rule | Threshold | Why |")
    out.append("| ---: | --- | --- | --- |")
    out.append(
        f"| 1 | Capability coverage | ≥ {cfg.get('min_coverage_ratio', 1.0):.0%} "
        "| The challenger must do everything the incumbent does. 100% means *everything*. |"
    )
    out.append(
        f"| 2 | Popularity | ≥ {cfg.get('min_star_advantage', 1.15):.2f}× the stars "
        "| A strictly better tool nobody uses is not yet a replacement. |"
    )
    out.append(
        f"| 3 | Momentum | ≥ {cfg.get('min_momentum_advantage', 1.0):.2f}× the star velocity "
        "| Stops a stagnant tool from killing a rising one. |"
    )
    out.append(
        f"| 4 | Setup cost | no more than +{cfg.get('max_setup_penalty', 12)} friction "
        "| A better tool that is much harder to install does not actually replace the old one. |"
    )
    out.append(
        "| 5 | Documentation | challenger within 10 doc points "
        "| Prevents replacing a well-documented tool with an undocumented one. |"
    )
    out.append(
        f"| 6 | Dominance margin | ≥ {cfg.get('min_dominance_score', 0.55)} "
        "| Blends the margins so marginal calls stay out of the graveyard. |"
    )
    out.append("")
    out.append(
        "A tool is never eliminated by a tool that is itself retired, and a chain "
        "(C ⊃ B ⊃ A) keeps only the **strongest direct edge** per incumbent, so the report "
        "reads as a decision rather than a transitive closure."
    )
    out.append("")

    out.append("## Lifecycle states")
    out.append("")
    out.append("| State | Meaning |")
    out.append("| --- | --- |")
    out.append("| 🟢 Active | Listed normally. |")
    out.append("| 🟡 Dormant | No commits for a long time, but not formally replaced. |")
    out.append("| 🔻 Superseded | Strictly covered by a healthier tool; moved to the graveyard. |")
    out.append("| ⛔ Deprecated | Marked so by a human in `config/overrides.json`. |")
    out.append("| 📦 Archived | The owner archived the repository. |")
    out.append("")

    out.append("## Supersede vs. challenger")
    out.append("")
    out.append(
        "A pair can be reported without anything being retired. That distinction matters, "
        "because the obvious headline example in this space does not actually qualify:"
    )
    out.append("")
    out.append(
        "**`magpie` is a challenger to `cc-switch`, not its replacement.** They compete for "
        "the same job, and magpie additionally routes other models through the same agent "
        "loop. But magpie covers roughly 62% of cc-switch's capability set, and at the time "
        "of writing has about 4% of its stars. Recording that as a retirement would mean "
        "this list asserting something its own methodology contradicts — so the pair appears "
        "under **Challengers**, cc-switch stays listed, and the engine keeps watching. If "
        "magpie closes the capability gap and the traction gap, the automatic rules will "
        "retire cc-switch on their own."
    )
    out.append("")
    out.append(
        "A curated entry in `config/overrides.json` is therefore a **nomination, not a "
        "verdict**: the claim is re-checked against the same coverage rule the automatic "
        "engine uses, and recorded as a `supersede` (retire) or a `challenger` (watch) "
        "accordingly."
    )
    out.append("")

    out.append("## Recorded eliminations")
    out.append("")
    if edges:
        for edge in edges:
            out.append(
                f"### {edge.get('incumbent_name') or edge['incumbent']} "
                f"→ {edge.get('challenger_name') or edge['challenger']}"
            )
            out.append("")
            if edge.get("source") == "curated":
                source = "human curation"
            else:
                source = f"automatic ({edge.get('confidence', '')} confidence)"
            out.append(f"- **Source:** {source}")
            out.append(f"- **Dominance:** {edge.get('dominance', 0):.3f}")
            out.append("")
            out.append("Reasons:")
            out.append("")
            for reason in edge.get("reasons", []):
                out.append(f"- {reason}")
            out.append("")
            evidence = edge.get("evidence") or {}
            if evidence:
                out.append("Evidence:")
                out.append("")
                out.append("```json")
                import json

                out.append(json.dumps(evidence, indent=2, ensure_ascii=False))
                out.append("```")
                out.append("")
    else:
        out.append(
            "*No eliminations recorded yet. The engine evaluates every pair on every run.*"
        )
        out.append("")

    out.append("## The canonical example")
    out.append("")
    out.append(
        "**`magpie` vs `cc-switch` — reported as a challenger, not an elimination.** They "
        "solve the same problem, and magpie goes further by routing other models through the "
        "same agent loop. It is tempting to declare the older tool replaced. The rules "
        "refuse: magpie covers ~62% of cc-switch's capabilities and has ~4% of its stars. "
        "The pair is therefore surfaced under **Challengers**, which is where a reader "
        "deciding what to install actually benefits from seeing it — and nothing is retired "
        "on the strength of a claim the data does not support."
    )
    out.append("")
    out.append("## Challenging a verdict")
    out.append("")
    out.append(
        "Add or edit an entry in [`config/overrides.json`](../config/overrides.json):"
    )
    out.append("")
    out.append("```json")
    out.append("{")
    out.append('  "supersede": [')
    out.append("    {")
    out.append('      "incumbent": "owner/old",')
    out.append('      "challenger": "owner/new",')
    out.append('      "note": "why the new tool strictly covers the old one"')
    out.append("    }")
    out.append("  ]")
    out.append("}")
    out.append("```")
    out.append("")
    out.append(
        "A manual edge always wins over an automatic one for the same incumbent, because a "
        "human has read both READMEs."
    )
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Entry loading & validation
# --------------------------------------------------------------------------

_ENTRY_CACHE: dict[str, dict[str, Any]] = {}


def _load_entry(full_name: str) -> dict[str, Any]:
    """Load the per-tool entry file, cached for the process lifetime."""
    if full_name in _ENTRY_CACHE:
        return _ENTRY_CACHE[full_name]
    from .pipeline import entry_path
    from .util import read_json

    entry = read_json(entry_path(full_name), default={}) or {}
    if not entry:
        entry = {"full_name": full_name, "url": f"https://github.com/{full_name}"}
    _ENTRY_CACHE[full_name] = entry
    return entry


def validate_index(index: dict[str, Any]) -> list[str]:
    """Check the generated index for structural problems. Returns problems."""
    problems: list[str] = []
    tools = index.get("tools")
    if not isinstance(tools, dict):
        return ["`tools` is missing or not an object"]

    if not tools:
        problems.append("no tools in the index")

    seen_categories: set[str] = set()
    category_ids = {c["id"] for c in index.get("categories", [])}

    for name, tool in tools.items():
        if name != tool.get("full_name", "").lower():
            problems.append(f"{name}: key does not match full_name {tool.get('full_name')}")
        if tool.get("category") not in category_ids:
            problems.append(f"{name}: unknown primary category {tool.get('category')!r}")
        seen_categories.add(tool.get("category"))
        for cat in tool.get("categories") or []:
            if cat not in category_ids:
                problems.append(f"{name}: unknown category {cat!r}")
        if tool.get("category") and tool["category"] not in (tool.get("categories") or []):
            problems.append(f"{name}: primary category is not in its own category list")
        if not isinstance(tool.get("health_score"), int):
            problems.append(f"{name}: health_score is not an int")
        if tool.get("health_score", 0) < 0 or tool.get("health_score", 0) > 100:
            problems.append(f"{name}: health_score out of range")
        if not tool.get("capabilities"):
            problems.append(f"{name}: no capabilities detected")

    # Every tool must be listed in full exactly once, and cross-listed only in
    # the categories it actually claims.
    primary_counts: dict[str, int] = {}
    for category in index.get("categories", []):
        for name in category.get("tools", []):
            primary_counts[name] = primary_counts.get(name, 0) + 1
            if name not in tools:
                problems.append(f"{name}: listed in a category but missing from tools")
            elif tools[name].get("category") != category["id"]:
                problems.append(
                    f"{name}: listed as a primary member of {category['id']} "
                    f"but its primary category is {tools[name].get('category')}"
                )
    for name, count in primary_counts.items():
        if count > 1:
            problems.append(f"{name}: listed as primary in {count} categories")
    for name, tool in tools.items():
        if tool.get("state") == "active" and primary_counts.get(name, 0) == 0:
            problems.append(f"{name}: active tool is not listed in any category")

    for edge in index.get("supersede", []) + index.get("challengers", []):
        if edge.get("incumbent") not in tools:
            problems.append(f"edge references unknown incumbent {edge.get('incumbent')}")
        if edge.get("challenger") not in tools:
            problems.append(f"edge references unknown challenger {edge.get('challenger')}")

    return problems


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------


def render_all(index: dict[str, Any], *, check: bool = False) -> list[Path]:
    """Render every generated file. Returns the paths written."""
    written: list[Path] = []
    tools = index.get("tools", {})

    pages: list[tuple[Path, str]] = [
        (REPO_ROOT / "README.md", render_readme(index)),
        (REPO_ROOT / "README.zh-CN.md", render_readme_zh(index)),
        (DOCS_DIR / "TAXONOMY.md", render_taxonomy(index)),
        (DOCS_DIR / "METHODOLOGY.md", render_methodology(index)),
        (DOCS_DIR / "SUPERSEDE.md", render_supersede_doc(index)),
    ]

    # Per-tool pages for everything currently listed.
    keep: set[str] = set()
    for name in sorted(tools):
        entry = _load_entry(tools[name]["full_name"])
        if not entry.get("full_name"):
            continue
        owner, _, repo = entry["full_name"].partition("/")
        filename = f"{owner}__{repo}.md"
        keep.add(filename)
        pages.append((DOCS_DIR / "tools" / filename, render_tool_page(entry)))

    if not check:
        _prune_orphan_tool_pages(keep)

    for path, content in pages:
        if check:
            existing = path.read_text(encoding="utf-8") if path.exists() else ""
            if existing != content.rstrip("\n") + "\n":
                written.append(path)
            continue
        write_text(path, content)
        written.append(path)

    return written


def _prune_orphan_tool_pages(keep: set[str]) -> None:
    """Delete tool pages for tools no longer in the index.

    Without this, a tool that is renamed or drops out leaves a stale page that
    still renders confidently and is still linked from any external bookmark —
    worse than a 404, because it looks authoritative.
    """
    tools_dir = DOCS_DIR / "tools"
    if not tools_dir.exists():
        return
    for path in tools_dir.glob("*.md"):
        if path.name not in keep:
            path.unlink(missing_ok=True)
