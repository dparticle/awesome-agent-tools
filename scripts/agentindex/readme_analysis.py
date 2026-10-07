"""Turn a README into structured, comparable facts.

This module exists because a GitHub ``description`` field is a marketing
sentence, not an answer to "what does this actually solve, and can I run it?".
Everything here is derived from the README **body**, with the sentence that
triggered each conclusion kept as evidence so a reviewer can audit it.

Four questions are answered per tool:

1. **What capabilities does it have?**      -> :func:`detect_capabilities`
2. **How much setup does it need?**         -> :func:`assess_friction`
3. **Is it usable without being a dev?**    -> ``non_programmer_friendly``
4. **How good is the documentation?**       -> :func:`score_docs`
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .util import (
    CONFIG_DIR,
    first_sentence,
    normalise,
    read_json,
    strip_markdown,
    truncate,
)

# --------------------------------------------------------------------------
# Signals
# --------------------------------------------------------------------------

#: Ways a README tells you "this is one command and you are done".
EASY_INSTALL_PATTERNS: list[tuple[str, str]] = [
    (r"\bnpx\s+[@\w]", "npx one-liner"),
    (r"\bbunx\s+[@\w]", "bunx one-liner"),
    (r"\buvx\s+[@\w]", "uvx one-liner"),
    (r"\bpipx?\s+install\s+[\w\-]+", "pip install"),
    (r"\bbrew\s+install\s+[\w\-/]+", "Homebrew install"),
    (r"\bwinget\s+install\b", "winget install"),
    (r"\bscoop\s+install\b", "scoop install"),
    (r"\bcargo\s+install\s+[\w\-]+", "cargo install"),
    (r"\bgo\s+install\s+[\w\-./]+", "go install"),
    (r"\bcurl\s+-[a-z]*f?[a-z]*s?[a-z]*L?\s+https?://\S+\s*\|\s*(ba)?sh", "curl | sh installer"),
    (r"\birm\s+https?://\S+\s*\|\s*iex", "PowerShell irm | iex installer"),
    (r"npm\s+install\s+-g\s+[@\w\-/]+", "global npm install"),
    (r"download (the )?(latest )?(release|installer|binary)", "download a release binary"),
    (r"\b(installer|\.dmg|\.exe|\.msi|appimage|\.deb|\.apk)\b", "native installer / package"),
]

#: Ways a README tells you "you will be here for a while".
HARD_SETUP_PATTERNS: list[tuple[str, str]] = [
    (r"docker[\s-]?compose\s+up", "docker compose up"),
    (r"\bdocker\s+run\b", "docker run"),
    (r"\bkubectl\s+(apply|create)\b", "kubectl apply"),
    (r"\bhelm\s+install\b", "helm install"),
    (r"git\s+clone\s+\S+", "git clone (build from source)"),
    (r"\bpnpm\s+(install|build|dev)\b", "pnpm install/build"),
    (r"\bnpm\s+(install|run\s+build)\b", "npm install/build"),
    (r"\byarn\s+(install|build)\b", "yarn install/build"),
    (r"\bmake\s+(install|build)\b", "make build"),
    (r"\bcmake\b", "cmake build"),
    (r"\bcargo\s+build\b", "cargo build"),
    (r"\bgo\s+build\b", "go build"),
    (r"\bpip\s+install\s+-r\s+requirements", "pip install -r requirements"),
    (r"\bpython\s+-m\s+venv\b", "create a Python venv"),
]

#: Evidence that the tool needs accounts, keys, servers or config files.
CONFIG_BURDEN_PATTERNS: list[tuple[str, str]] = [
    (r"\benv(ironment)?\s+variable", "environment variables"),
    (r"\bAPI[_ ]?KEY\b", "API key configuration"),
    (r"\b\.env\b", ".env file"),
    (r"\bconfig(uration)?\s+file\b", "config file"),
    (r"\bconfig\.(json|ya?ml|toml)\b", "config.json/yaml/toml"),
    (r"\b(yaml|yml|toml|json)\s+config", "config file"),
    (r"\boauth\b", "OAuth login flow"),
    (r"\bsign\s+in\b|\blog\s+in\b|\blogin\b", "sign-in required"),
    (r"\bapi\s+(token|secret|credential)", "API token/secret"),
    (r"\bdatabase\b|\bpostgres\b|\bmysql\b|\bredis\b|\bsqlite\b", "database dependency"),
    (r"\bmigrat(e|ion)\b", "database migration"),
    (r"\bnginx\b|\breverse\s+proxy\b|\bdomain\b|\bSSL\s+certificate\b", "server/reverse-proxy setup"),
    (r"\bpm2\b|\bsystemd\b|\bsupervisor\b", "process manager"),
]

#: Signals that a non-programmer is welcome.
NON_PROGRAMMER_PATTERNS: list[tuple[str, str]] = [
    (r"no\s+(coding|code|programming)\s+(required|needed|knowledge)", "explicitly no coding required"),
    (r"without\s+(writing\s+)?(any\s+)?code", "no code needed"),
    (r"\bno[- ]code\b", "no-code positioning"),
    (r"one[- ]click\b|single[- ]click\b", "one-click setup"),
    (r"beginner[- ]friendly|for\s+beginners|non[- ]?(technical|programmer|developer)", "beginner-friendly"),
    (r"\bdesktop\s+(app|application)\b|\bGUI\b|\bgraphical\b|\bTauri\b|\bElectron\b", "GUI application"),
    (r"无需(编程|代码|命令行|技术)", "Chinese: no coding needed"),
    (r"小白|零基础|开箱即用|一键(安装|部署|启动)", "Chinese: beginner/one-click framing"),
    (r"保姆级|手把手|图文教程|step[- ]by[- ]step\s+(guide|tutorial)", "tutorial-style docs"),
]

#: Doc-quality signals, each worth points.
DOC_QUALITY_SIGNALS: list[tuple[str, int, str]] = [
    (r"```", 10, "contains code blocks"),
    (r"!\[[^\]]*\]\(", 8, "contains screenshots/diagrams"),
    (r"^\s*[-*]\s+\[[ xX]\]", 6, "has a task checklist"),
    (r"(?m)^#{1,3}\s", 6, "has section headings"),
    (r"quick\s?start|getting\s+started|快速开始|快速上手", 8, "has a quick-start section"),
    (r"installation|install\b|安装", 6, "documents installation"),
    (r"configuration|config\b|配置", 5, "documents configuration"),
    (r"troubleshoot|FAQ|常见问题|疑难", 5, "has troubleshooting/FAQ"),
    (r"contribut|贡献", 3, "has contribution guidance"),
    (r"license|许可", 3, "mentions licensing"),
    (r"table of contents|目录", 3, "has a table of contents"),
    (r"https?://\S*(docs?|documentation)\.", 5, "links to dedicated docs"),
    (r"简体中文|繁體中文|中文文档", 5, "has a Chinese translation"),
    (r"changelog|release notes|更新日志", 4, "documents changes"),
    (r"roadmap|路线图", 3, "publishes a roadmap"),
    (r"benchmark|bench", 3, "reports benchmarks"),
    (r"architecture|架构", 3, "explains architecture"),
]

#: Platform claims worth surfacing, since "works on my OS" is a real blocker.
PLATFORM_PATTERNS: list[tuple[str, str]] = [
    (r"\bmacOS\b|\bmac\b|MacBook", "macOS"),
    (r"\bWindows\b|\bWin32\b|\bWSL\b", "Windows"),
    (r"\bLinux\b|Ubuntu|Debian|Arch\b", "Linux"),
    (r"\biOS\b|iPhone|iPad", "iOS"),
    (r"\bAndroid\b|Google Play", "Android"),
    (r"\bweb\b|browser|self-hosted web", "Web"),
]

#: Which agent(s) a tool plugs into — the single most useful filter for readers.
#: Also used to count *distinct* agents for capabilities that need it.
AGENT_PATTERNS: list[tuple[str, str]] = [
    (r"\bClaude Code\b|claude[- ]code", "Claude Code"),
    (r"\bCodex\b|codex[- ]cli|OpenAI Codex", "Codex"),
    (r"\bGemini CLI\b|gemini[- ]cli", "Gemini CLI"),
    (r"\bOpenCode\b|opencode", "OpenCode"),
    (r"\bCursor\b", "Cursor"),
    (r"\bGitHub Copilot\b|\bCopilot\b", "Copilot"),
    (r"\bAider\b", "Aider"),
    (r"\bCline\b|\bRoo Code\b", "Cline / Roo"),
    (r"\bQwen Code\b", "Qwen Code"),
    (r"\bGoose\b", "Goose"),
    (r"\bCrush\b", "Crush"),
    (r"\bDroid\b|Factory", "Droid"),
]

#: ``(canonical name, pattern)`` used to count distinct agents. Kept separate
#: from :data:`AGENT_PATTERNS` because some groups collapse two products into
#: one entry ("Cline / Roo") and would otherwise double-count.
AGENT_GROUP_PATTERNS: list[tuple[str, str]] = [
    ("Claude Code", r"\bclaude code\b|claude[- ]code"),
    ("Codex", r"\bcodex\b|codex[- ]cli"),
    ("Gemini CLI", r"\bgemini (cli|code)\b|gemini[- ]cli"),
    ("OpenCode", r"\bopencode\b"),
    ("Cursor", r"\bcursor\b"),
    ("Copilot", r"\bgithub copilot\b|\bcopilot\b"),
    ("Aider", r"\baider\b"),
    ("Cline", r"\bcline\b"),
    ("Roo Code", r"\broo code\b"),
    ("Qwen Code", r"\bqwen code\b"),
    ("Goose", r"\bgoose\b"),
    ("Crush", r"\bcrush\b"),
    ("Amp", r"\bamp\b"),
    ("Droid", r"\bdroid\b"),
    ("Kilo Code", r"\bkilo code\b"),
    ("Continue", r"continue\.dev"),
]

FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)

# --------------------------------------------------------------------------
# Curated-list detection
# --------------------------------------------------------------------------

#: A curated list is not a tool. These repos match every capability keyword
#: because they *describe* hundreds of tools, so without this filter they
#: dominate the index and "supersede" everything else.
LIST_NAME_RE = re.compile(
    r"^(awesome|best[- ]of|top[- ]\d+|list[- ]of|collection[- ]of|"
    r"resources?|curated|handbook|guide|tutorial|roadmap|cheat[- ]?sheet|"
    r"interview|papers|books|courses)",
    re.IGNORECASE,
)

LIST_SIGNAL_PATTERNS: list[tuple[str, str]] = [
    (r"^\s*[-*]\s*\[[^\]]+\]\(https?://[^)]+\)\s*[-–—:]\s*\S", "bullet list of external links"),
    (r"a curated list of", "self-describes as a curated list"),
    (r"awesome list", "self-describes as an awesome list"),
    (r"contributions? welcome.{0,80}(add|submit).{0,40}link", "accepts link submissions"),
    (r"pull requests? (to add|adding|for adding).{0,40}(link|project|tool)", "accepts link PRs"),
    (r"(table of contents|contents)\s*\n(.{0,200}\n){1,3}\s*[-*]\s*\[", "link-directory table of contents"),
    (r"精选|收录|汇总|清单|大全|合集|导航", "Chinese: directory framing"),
    # Directory framing that does not use the word "awesome". These catch the
    # big non-"awesome" lists (public-apis, free-for-dev, open-source-ios-apps).
    (r"(a |the )?(collective|curated|community[- ]maintained) list", "self-describes as a maintained list"),
    (r"list of (free|open[- ]source|public|useful|available|popular) \w+", "self-describes as a list of things"),
    (r"^#{1,3}\s*(index|catalog(ue)?|directory)\b", "has an index/catalogue section"),
    (r"(add|submit) (your|a) (project|tool|api|entry|link)", "invites project submissions"),
    (r"no longer (maintained|accepting)|this list is", "list-maintenance framing"),
]

#: A repo needs several independent list signals, not one, to be excluded —
#: plenty of real tools have a "Table of contents".
MIN_LIST_SIGNALS = 3


@dataclass
class ListAssessment:
    """Whether this repository is a directory rather than a usable tool."""

    is_list: bool = False
    score: int = 0
    signals: list[str] = field(default_factory=list)
    external_link_ratio: float = 0.0

    def as_dict(self) -> dict[str, Any]:
        return {
            "is_list": self.is_list,
            "score": self.score,
            "signals": self.signals,
            "external_link_ratio": round(self.external_link_ratio, 3),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ListAssessment":
        obj = cls()
        for key, value in (data or {}).items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj


def assess_list(repo_name: str, body: str) -> ListAssessment:
    """Decide whether a README is a curated directory instead of a tool.

    Two independent kinds of evidence are combined: the repository *name*
    (``awesome-*``, ``*-list``) and the README *shape* — a very high ratio of
    external links relative to prose, plus directory-style framing.
    """
    result = ListAssessment()
    if not body:
        return result

    if LIST_NAME_RE.match(repo_name or ""):
        result.signals.append(f"name starts with a list-style word ({repo_name})")
        result.score += 2

    for pattern, label in LIST_SIGNAL_PATTERNS:
        if re.search(pattern, body, re.IGNORECASE | re.MULTILINE):
            result.signals.append(label)
            result.score += 1

    # Link density: a directory is mostly links. Count Markdown links that
    # point at other repositories/sites, relative to the README's length.
    external = re.findall(r"\[[^\]]+\]\(https?://(?!github\.com/[\w.-]+/[\w.-]+/(blob|tree))[^)]+\)", body)
    per_kchar = len(external) / max(len(body) / 1000.0, 1.0)
    result.external_link_ratio = per_kchar
    if per_kchar >= 8.0:
        result.signals.append(f"{per_kchar:.1f} external links per 1000 chars")
        result.score += 2
    elif per_kchar >= 4.0:
        result.score += 1

    # Many bullet points whose entire content is a link to elsewhere.
    link_bullets = len(
        re.findall(r"(?m)^\s*[-*]\s*\[[^\]]+\]\(https?://[^)]+\)\s*(?:[-–—:]|\s*$)", body)
    )
    if link_bullets >= 25:
        result.signals.append(f"{link_bullets} bare link bullets")
        result.score += 2
    elif link_bullets >= 10:
        result.score += 1

    result.is_list = result.score >= MIN_LIST_SIGNALS
    return result


# --------------------------------------------------------------------------
# Result types
# --------------------------------------------------------------------------


@dataclass
class FrictionAssessment:
    """How much work stands between `git clone` and a useful session."""

    level: str = "moderate"  # turnkey | low | moderate | high | unknown
    score: int = 0  # 0 (frictionless) .. 100 (heavy)
    out_of_the_box: bool = False
    non_programmer_friendly: bool = False
    easy_signals: list[str] = field(default_factory=list)
    hard_signals: list[str] = field(default_factory=list)
    config_signals: list[str] = field(default_factory=list)
    friendliness_signals: list[str] = field(default_factory=list)
    platforms: list[str] = field(default_factory=list)
    note_en: str = ""
    note_zh: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "level": self.level,
            "score": self.score,
            "out_of_the_box": self.out_of_the_box,
            "non_programmer_friendly": self.non_programmer_friendly,
            "easy_signals": self.easy_signals,
            "hard_signals": self.hard_signals,
            "config_signals": self.config_signals,
            "friendliness_signals": self.friendliness_signals,
            "platforms": self.platforms,
            "note_en": self.note_en,
            "note_zh": self.note_zh,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "FrictionAssessment":
        obj = cls()
        for key, value in (data or {}).items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj


@dataclass
class ReadmeAnalysis:
    full_name: str
    readme_chars: int = 0
    capabilities: list[str] = field(default_factory=list)
    capability_evidence: dict[str, str] = field(default_factory=dict)
    #: How many times each capability's pattern matched. A count of 1 usually
    #: means an incidental mention rather than a documented feature.
    capability_hits: dict[str, int] = field(default_factory=dict)
    friction: FrictionAssessment = field(default_factory=FrictionAssessment)
    doc_score: int = 0
    doc_signals: list[str] = field(default_factory=list)
    agents: list[str] = field(default_factory=list)
    summary_en: str = ""
    summary_zh: str = ""
    install_hint: str = ""
    source: str = "missing"
    list_assessment: ListAssessment = field(default_factory=ListAssessment)

    def as_dict(self) -> dict[str, Any]:
        return {
            "full_name": self.full_name,
            "readme_chars": self.readme_chars,
            "capabilities": self.capabilities,
            "capability_evidence": self.capability_evidence,
            "capability_hits": self.capability_hits,
            "friction": self.friction.as_dict(),
            "doc_score": self.doc_score,
            "doc_signals": self.doc_signals,
            "agents": self.agents,
            "summary_en": self.summary_en,
            "summary_zh": self.summary_zh,
            "install_hint": self.install_hint,
            "source": self.source,
            "list_assessment": self.list_assessment.as_dict(),
        }

    @property
    def is_curated_list(self) -> bool:
        return self.list_assessment.is_list

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ReadmeAnalysis":
        return cls(
            full_name=data.get("full_name", ""),
            readme_chars=data.get("readme_chars", 0),
            capabilities=data.get("capabilities", []),
            capability_evidence=data.get("capability_evidence", {}),
            capability_hits=data.get("capability_hits", {}),
            friction=FrictionAssessment.from_dict(data.get("friction", {})),
            doc_score=data.get("doc_score", 0),
            doc_signals=data.get("doc_signals", []),
            agents=data.get("agents", []),
            summary_en=data.get("summary_en", ""),
            summary_zh=data.get("summary_zh", ""),
            install_hint=data.get("install_hint", ""),
            source=data.get("source", "missing"),
            list_assessment=ListAssessment.from_dict(data.get("list_assessment", {})),
        )


# --------------------------------------------------------------------------
# Capability catalogue
# --------------------------------------------------------------------------


def load_capabilities() -> list[dict[str, Any]]:
    data = read_json(CONFIG_DIR / "capabilities.json", default={}) or {}
    return data.get("capabilities", [])


_CAPABILITY_CACHE: list[dict[str, Any]] | None = None


def capabilities() -> list[dict[str, Any]]:
    global _CAPABILITY_CACHE
    if _CAPABILITY_CACHE is None:
        _CAPABILITY_CACHE = load_capabilities()
    return _CAPABILITY_CACHE


def capability_label(cap_id: str, lang: str = "en") -> str:
    for cap in capabilities():
        if cap["id"] == cap_id:
            return cap.get("label", {}).get(lang) or cap_id
    return cap_id


# --------------------------------------------------------------------------
# Matching helpers
# --------------------------------------------------------------------------


def _find_signals(text: str, patterns: list[tuple[str, str]]) -> list[str]:
    found: list[str] = []
    for pattern, label in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            found.append(label)
    return found


def _find_signals_unnegated(text: str, patterns: list[tuple[str, str]]) -> list[str]:
    """Like :func:`_find_signals`, but ignores negated mentions.

    Without this, "no configuration file is required" and "no API key needed"
    register as configuration *burden* — the exact opposite of what the README
    says, and it would sink a genuinely turnkey tool's accessibility score.
    """
    found: list[str] = []
    for pattern, label in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            if not _is_negated(text, match.start()):
                found.append(label)
                break
    return found


def _prose_only(plain: str) -> str:
    """Blank out Markdown table rows, keeping character offsets stable.

    Table-heavy READMEs (agent-role catalogues, feature matrices) otherwise
    match almost every capability pattern somewhere in a cell, and the quoted
    evidence comes out as an unreadable mid-row fragment. Replacing table lines
    with spaces preserves indices so evidence offsets stay valid.
    """
    out = []
    for line in plain.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("|") or re.match(r"^[-:| ]{6,}$", stripped):
            out.append(" " * len(line))
        else:
            out.append(line)
    return "\n".join(out)


def _is_readable_quote(text: str) -> bool:
    """Reject 'evidence' that explains nothing to a reader.

    Filters out horizontal rules, table separators, bare URLs, badge lines and
    fragments with almost no words.
    """
    if len(text) < 25:
        return False
    # Separator / rule noise: mostly punctuation.
    letters = sum(1 for ch in text if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")
    if letters < len(text) * 0.5:
        return False
    # A URL or image reference.
    if re.search(r"https?://\S+", text) and letters < 40:
        return False
    # Badge / shield markup.
    if "shields.io" in text or "badge" in text.lower()[:20]:
        return False
    # Too few real words.
    if len(re.findall(r"[A-Za-z\u4e00-\u9fff]{2,}", text)) < 4:
        return False
    return True


def _first_match_sentence(body: str, pattern: str) -> str:
    """Return readable prose around the first match — the audit trail.

    Prefers a match in ordinary prose; falls back to any match. Table rows and
    separator lines are skipped when possible because a fragment of a feature
    matrix explains nothing to a reader.
    """
    prose = _prose_only(body)
    for haystack in (prose, body):
        for match in re.finditer(pattern, haystack, re.IGNORECASE):
            start = max(0, match.start() - 200)
            end = min(len(haystack), match.end() + 200)
            window = haystack[start:end]
            # Trim to the nearest sentence-ish boundary.
            left = max(window.rfind(". "), window.rfind("。"), window.rfind("\n"))
            if 0 <= left < (match.start() - start):
                window = window[left + 1 :]
            right_candidates = [
                idx for idx in (window.find(". "), window.find("。"), window.find("\n")) if idx > 0
            ]
            if right_candidates:
                window = window[: min(right_candidates) + 1]
            text = re.sub(r"\s+", " ", window.replace("|", " ")).strip()
            if _is_readable_quote(text):
                return truncate(text, 220)
    return ""


#: Negation markers, English and Chinese.
_NEGATION_RE = re.compile(
    r"\b(?:not|no|never|isn't|aren't|doesn't|don't|didn't|won't|without|"
    r"lacks?|lacking|missing|unsupported|planned|todo|coming soon)\b"
    r"|(?:暂不|暂未|不支持|尚未|即将|计划中|无法|不能)",
    re.IGNORECASE,
)

#: Sentence terminators used to scope negation to its own clause.
_CLAUSE_SPLIT_RE = re.compile(r"[.!?;。！？；\n]+")


def _is_negated(plain: str, match_start: int) -> bool:
    """Is the match negated *in its own clause*?

    Scoping matters. A naive fixed-width window produces false negatives like
    "no coding required. ... - multi-account switching": the unrelated "no"
    would cancel a genuine capability. We therefore only look at the text
    between the previous sentence terminator and the match itself.
    """
    prefix = plain[max(0, match_start - 120) : match_start]
    clauses = [c for c in _CLAUSE_SPLIT_RE.split(prefix) if c.strip()]
    if not clauses:
        return False
    return bool(_NEGATION_RE.search(clauses[-1]))


def extract_install_hint(body: str) -> str:
    """Pull the first plausible install command out of the README."""
    for fence in FENCE_RE.findall(body):
        for line in fence.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if re.match(
                r"^(npx|bunx|uvx|pip3?\s+install|pipx|brew|winget|scoop|cargo\s+install|"
                r"go\s+install|npm\s+(i|install)|pnpm\s+add|yarn\s+add|"
                r"docker(\s+compose)?\s+(run|up)|curl\s)",
                line,
                re.IGNORECASE,
            ):
                return truncate(line, 110)
    return ""


# --------------------------------------------------------------------------
# Main entry points
# --------------------------------------------------------------------------


def detect_capabilities(body: str) -> tuple[list[str], dict[str, str], dict[str, int]]:
    """Match the capability catalogue against the README body.

    Returns ``(capabilities, evidence, hit_counts)``.

    Negation is handled per clause: a keyword appearing only inside a
    "not supported" / "planned" statement does not grant the capability. If the
    same pattern also appears later in a non-negated clause, the capability is
    credited (a roadmap item that shipped, or a comparison against a rival).

    A capability may declare ``requires_distinct_agents``: it is then granted
    only when the README mentions that many *different* agents. This stops
    "cross-agent support" from being credited to every repo that name-drops
    Claude Code once.

    The hit count matters downstream: one incidental mention ("browser
    sessions", "Coding agents (Claude Code, Copilot)" in an install table) is
    not a feature claim, and relevance gating uses the count to tell them apart.
    """
    plain = strip_markdown(body)
    plain_norm = normalise(plain)
    # Capability *counting* ignores table cells: a feature matrix in a README
    # matches dozens of patterns in adjacent cells without the project actually
    # claiming those features. Detection still falls back to the full text so a
    # capability documented only in a table is not lost.
    prose_norm = normalise(_prose_only(plain))
    found: list[str] = []
    evidence: dict[str, str] = {}
    hits: dict[str, int] = {}

    for cap in capabilities():
        required_distinct = int(cap.get("requires_distinct_agents", 0) or 0)
        if required_distinct:
            distinct = {
                group
                for group, pattern in AGENT_GROUP_PATTERNS
                if re.search(pattern, plain_norm, re.IGNORECASE)
            }
            if len(distinct) < required_distinct:
                continue
            found.append(cap["id"])
            evidence[cap["id"]] = "Mentions " + ", ".join(sorted(distinct)[:4])
            hits[cap["id"]] = len(distinct)
            continue

        best_count = 0
        best_pattern = ""
        for pattern in cap.get("patterns", []):
            count = sum(
                1
                for match in re.finditer(pattern, prose_norm, re.IGNORECASE)
                if not _is_negated(prose_norm, match.start())
            )
            if count > best_count:
                best_count, best_pattern = count, pattern

        if not best_pattern:
            # Not corroborated in prose. A capability documented only inside a
            # table is still real, so accept a single non-negated mention from
            # the full text — but score it as weak evidence (one hit), which
            # keeps it out of relevance and category decisions.
            for pattern in cap.get("patterns", []):
                for match in re.finditer(pattern, plain_norm, re.IGNORECASE):
                    if not _is_negated(plain_norm, match.start()):
                        best_pattern, best_count = pattern, 1
                        break
                if best_pattern:
                    break

        if not best_pattern:
            continue
        found.append(cap["id"])
        evidence[cap["id"]] = _first_match_sentence(plain, best_pattern)
        hits[cap["id"]] = best_count

    return found, evidence, hits


def assess_friction(body: str, plain: str) -> FrictionAssessment:
    """Score setup effort from 0 (turnkey) to 100 (heavy).

    Install commands live inside fenced code blocks, which ``strip_markdown``
    removes. The easy/hard install signals are therefore matched against the
    **raw body**, while prose-only signals (friendliness, config burden) use the
    stripped text where a stray code sample would be noise.
    """
    result = FrictionAssessment()
    raw = normalise(body)
    low = normalise(plain)

    result.easy_signals = _find_signals(raw, EASY_INSTALL_PATTERNS)
    result.hard_signals = _find_signals(raw, HARD_SETUP_PATTERNS)
    # Config burden must respect negation: "no API key required" is the opposite
    # of a configuration burden.
    result.config_signals = _find_signals_unnegated(low, CONFIG_BURDEN_PATTERNS)
    result.friendliness_signals = _find_signals(low, NON_PROGRAMMER_PATTERNS)
    result.platforms = _find_signals(plain, PLATFORM_PATTERNS)

    score = 30  # neutral prior: most agent tooling needs *some* setup
    score += min(len(result.hard_signals), 4) * 9
    score += min(len(result.config_signals), 5) * 6
    score -= min(len(result.easy_signals), 3) * 9
    score -= min(len(result.friendliness_signals), 3) * 7

    # A published installer/binary is the single strongest turnkey signal.
    if any("installer" in s or "one-liner" in s or "install" in s for s in result.easy_signals):
        score -= 5

    # A README that only says "clone and build" is the single strongest negative.
    if "git clone (build from source)" in result.hard_signals and not result.easy_signals:
        score += 12

    result.score = int(max(0, min(100, score)))

    if result.score <= 18:
        result.level = "turnkey"
    elif result.score <= 36:
        result.level = "low"
    elif result.score <= 58:
        result.level = "moderate"
    else:
        result.level = "high"

    # Out-of-the-box: no source build, no server stack, at most light config.
    has_easy = bool(result.easy_signals)
    heavy_hard = [s for s in result.hard_signals if s not in {"npm install/build", "pnpm install/build"}]
    result.out_of_the_box = bool(has_easy and not heavy_hard and len(result.config_signals) <= 1)

    # Non-programmer friendly: GUI or explicit no-code framing, and not a
    # self-hosted server stack.
    gui_like = any(
        s in result.friendliness_signals
        for s in ("GUI application", "one-click setup", "explicitly no coding required", "no code needed", "no-code positioning")
    )
    server_like = any(
        s in result.config_signals for s in ("database dependency", "server/reverse-proxy setup", "process manager")
    )
    result.non_programmer_friendly = bool(gui_like and not server_like and result.score <= 45)

    result.note_en, result.note_zh = _friction_note(result)
    return result


def _friction_note(f: FrictionAssessment) -> tuple[str, str]:
    level_en = {
        "turnkey": "Turnkey",
        "low": "Easy",
        "moderate": "Some setup",
        "high": "Involved setup",
    }.get(f.level, "Unknown")
    level_zh = {
        "turnkey": "开箱即用",
        "low": "较易上手",
        "moderate": "需要一些配置",
        "high": "配置较重",
    }.get(f.level, "未知")

    bits_en: list[str] = []
    bits_zh: list[str] = []
    if f.easy_signals:
        bits_en.append("install via " + ", ".join(f.easy_signals[:2]))
        bits_zh.append("可通过 " + "、".join(f.easy_signals[:2]) + " 安装")
    if f.hard_signals:
        bits_en.append("needs " + ", ".join(f.hard_signals[:2]))
        bits_zh.append("需要 " + "、".join(f.hard_signals[:2]))
    if f.config_signals:
        bits_en.append("configure " + ", ".join(f.config_signals[:2]))
        bits_zh.append("需配置 " + "、".join(f.config_signals[:2]))
    if f.friendliness_signals:
        bits_en.append(f.friendliness_signals[0])
        bits_zh.append(f.friendliness_signals[0])

    note_en = f"{level_en}. " + ("; ".join(bits_en) if bits_en else "No setup signals found in the README.")
    note_zh = f"{level_zh}。" + ("；".join(bits_zh) if bits_zh else "README 中没有找到安装/配置说明。")
    return truncate(note_en, 240), truncate(note_zh, 240)


def score_docs(body: str) -> tuple[int, list[str]]:
    """Score documentation quality 0-100 from structural signals."""
    signals: list[str] = []
    points = 0
    for pattern, weight, label in DOC_QUALITY_SIGNALS:
        if re.search(pattern, body, re.IGNORECASE | re.MULTILINE):
            points += weight
            signals.append(label)
    length_bonus = min(len(body) // 2500, 12)
    points += length_bonus
    if length_bonus >= 8:
        signals.append("long, detailed README")
    return int(min(100, points)), signals


def detect_agents(body: str) -> list[str]:
    return _find_signals(body, AGENT_PATTERNS)


def summarise(body: str, description: str) -> tuple[str, str]:
    """Build a one-line summary.

    Prefers the README's own opening prose — its first real paragraph after
    badges and titles — because that is where projects state their purpose.
    Falls back to the GitHub description.
    """
    lines = body.splitlines()
    paragraph: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if paragraph:
                break
            continue
        # Skip headings, badges, images, HTML, tables, fences, TOC links.
        if stripped.startswith(("#", "!", "[![", "<", "|", "```", ">", "---", "===")):
            continue
        if re.match(r"^\[!\[", stripped) or re.match(r"^\[.*\]\(#", stripped):
            continue
        if re.match(r"^\s*[-*]\s*$", stripped):
            continue
        # A bare URL or image reference is not prose. READMEs very often open
        # with a screenshot or a demo-video link, which produced summaries like
        # "https://github.com/user-attachments/assets/...".
        if re.fullmatch(r"https?://\S+", stripped):
            continue
        if re.match(r"^\[?https?://\S+\]?(\([^)]*\))?$", stripped):
            continue
        # A lone list marker, ordered-list number, or one-word fragment.
        # ``strip_markdown`` strips emphasis first, so "1. **Multi-provider...**"
        # must be judged on the text after the marker, not rejected outright.
        marker = re.match(r"^(?:[-*+]|\[[ xX]\]|\d+[.)])\s+(.*)$", stripped)
        if marker:
            remainder = strip_markdown(marker.group(1)).strip()
            if len(remainder) < 15:
                continue
            stripped = remainder
        elif re.fullmatch(r"[-*+>]|\[[ xX]\]|\d+[.)]", stripped):
            continue
        if len(strip_markdown(stripped)) < 15:
            continue
        paragraph.append(stripped)
        if len(" ".join(paragraph)) > 400:
            break

    text = strip_markdown(" ".join(paragraph))
    # A summary that is still just a URL (or a lone markdown image alt) tells the
    # reader nothing, so fall back to the GitHub description.
    if _is_useless_summary(text):
        text = strip_markdown(description or "")
    return first_sentence(text, 240), ""


def _is_useless_summary(text: str) -> bool:
    text = (text or "").strip()
    if len(text) < 20:
        return True
    # Mostly a URL.
    if re.fullmatch(r"[\s\w:/.\-?#\[\]()]*https?://\S*[\s\w:/.\-?#\[\]()]*", text):
        return True
    # No letters at all (e.g. only punctuation/emoji).
    if not re.search(r"[A-Za-z\u4e00-\u9fff]", text):
        return True
    return False


def analyse(
    full_name: str,
    body: str,
    description: str = "",
    source: str = "raw",
) -> ReadmeAnalysis:
    """Analyse one README into a :class:`ReadmeAnalysis`."""
    plain = strip_markdown(body)
    repo_name = full_name.partition("/")[2] or full_name
    list_assessment = assess_list(repo_name, body)

    # A curated directory matches every capability keyword because it describes
    # hundreds of tools. Crediting it would let it "supersede" real tools, so we
    # refuse to derive capabilities from it at all.
    if list_assessment.is_list:
        caps, evidence, hits = [], {}, {}
    else:
        caps, evidence, hits = detect_capabilities(body)

    friction = assess_friction(body, plain)
    doc_score, doc_signals = score_docs(body)
    summary_en, _ = summarise(body, description)

    return ReadmeAnalysis(
        full_name=full_name,
        readme_chars=len(body),
        capabilities=caps,
        capability_evidence=evidence,
        capability_hits=hits,
        friction=friction,
        doc_score=doc_score,
        doc_signals=doc_signals,
        agents=detect_agents(plain),
        summary_en=summary_en,
        summary_zh="",
        install_hint=extract_install_hint(body),
        source=source,
        list_assessment=list_assessment,
    )
