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

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

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
        anchor = f"#-{title.lower().replace(' ', '-').replace('&', '').replace('--', '-')}"
        add(f"- [{title}](#{anchor.replace('#-', '').strip('-')}) — {len(names)} tools")
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

        add("| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |")
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
            kind = "👤 curated" if edge.get("kind") == "manual" else f"🤖 auto ({edge.get('confidence', '')})"
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
                if edge.get("kind") == "manual":
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
    if edge.get("kind") == "manual":
        return reasons[0] if reasons else "curated supersede decision"
    return reasons[0] if reasons else ""


def _solves_line(entry: dict[str, Any], tool: dict[str, Any]) -> str:
    """One line answering 'what core problem does this solve?'

    The README's own opening sentence is the most informative thing available,
    so it leads. The tool's strongest capability is appended only when the
    summary is too short to stand alone, and never when the summary already
    contains that wording — otherwise every row reads
    "… — Remote control" regardless of what the tool does.
    """
    analysis = entry.get("analysis") or {}
    summary = (analysis.get("summary_en") or entry.get("description") or "").strip()
    summary = truncate(summary, 150)

    caps = tool.get("capabilities") or analysis.get("capabilities") or []
    if not caps:
        return summary

    label = capability_label(caps[0])
    # A 50-character summary already answers the question; appending a
    # capability label to it just adds noise.
    if len(summary) >= 40:
        return summary
    if summary and label.lower() in summary.lower():
        return summary
    if summary:
        return truncate(f"{summary} — {label}", 150)
    return label


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
            caps = tool.get("capabilities", [])
            solves = "、".join(capability_label(c, "zh") for c in caps[:3]) or truncate(
                entry.get("description", ""), 80
            )
            friction = (entry.get("analysis") or {}).get("friction") or {}
            level = friction.get("level", "unknown")
            setup = f"{SETUP_ICON.get(level, '⚪')} {SETUP_LABEL.get(level, SETUP_LABEL['unknown'])['zh']}"
            add(
                f"| {icon} **[{tool['full_name']}]({entry.get('url', '#')})** "
                f"| {escape_table_cell(solves)} "
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
            kind = "👤 人工" if edge.get("kind") == "manual" else f"🤖 自动（{edge.get('confidence', '')}）"
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

    out: list[str] = [GENERATED_BANNER, "", "# Capability taxonomy", ""]
    out.append(
        "Categories group tools by **the problem they solve**. Capabilities are the finer "
        "grained, machine-detected features used for scoring and for the elimination engine. "
        "Both are matched against the README body, with the triggering sentence kept as evidence."
    )
    out.append("")
    out.append("## Categories")
    out.append("")
    for category in index.get("categories", []):
        count = sum(1 for t in tools.values() if t.get("category") == category["id"])
        title = category.get("title", {}).get("en", category["id"])
        zh = category.get("title", {}).get("zh", "")
        out.append(f"### `{category['id']}` — {title} / {zh}")
        out.append("")
        problem = category.get("problem", {}).get("en", "")
        if problem:
            out.append(problem)
            out.append("")
        out.append(f"- Required capabilities: `{', '.join(category.get('required_any', [])) or 'any'}`")
        out.append(f"- Tools currently listed: **{count}**")
        out.append("")
        out.append("Discovery queries:")
        out.append("")
        for query in category.get("queries", []):
            out.append(f"- `{query}`")
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

    out.append("## 6. Elimination")
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

    out.append("## Recorded eliminations")
    out.append("")
    if edges:
        for edge in edges:
            out.append(
                f"### {edge.get('incumbent_name') or edge['incumbent']} "
                f"→ {edge.get('challenger_name') or edge['challenger']}"
            )
            out.append("")
            if edge.get("kind") == "manual":
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
        "**`magpie` retires `cc-switch`.** Both manage multiple accounts and providers for "
        "Claude Code and Codex. `cc-switch` is enormously popular and still actively "
        "maintained — but `magpie` covers the same ground *and* routes other models through "
        "the same agent loop, so it strictly covers the older tool's feature set. The "
        "elimination is recorded as **manual**, because a human read both READMEs and made "
        "the call; the automatic rules then keep it consistent on later runs."
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
            problems.append(f"{name}: unknown category {tool.get('category')!r}")
        seen_categories.add(tool.get("category"))
        if not isinstance(tool.get("health_score"), int):
            problems.append(f"{name}: health_score is not an int")
        if tool.get("health_score", 0) < 0 or tool.get("health_score", 0) > 100:
            problems.append(f"{name}: health_score out of range")
        if not tool.get("capabilities"):
            problems.append(f"{name}: no capabilities detected")

    # Every tool must appear in exactly one category listing.
    listed: dict[str, int] = {}
    for category in index.get("categories", []):
        for name in category.get("tools", []):
            listed[name] = listed.get(name, 0) + 1
    for name, count in listed.items():
        if count > 1:
            problems.append(f"{name}: listed in {count} categories")
        if name not in tools:
            problems.append(f"{name}: listed in a category but missing from tools")

    for edge in index.get("supersede", []):
        if edge.get("incumbent") not in tools:
            problems.append(f"supersede edge references unknown incumbent {edge.get('incumbent')}")
        if edge.get("challenger") not in tools:
            problems.append(f"supersede edge references unknown challenger {edge.get('challenger')}")

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
