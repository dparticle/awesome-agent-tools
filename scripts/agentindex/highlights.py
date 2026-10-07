"""Extract per-tool highlights from a README.

The first version of the index described each tool with a single line that
usually restated its category ("Multi-account switching — ..."), which tells a
reader nothing they could not infer from the section heading. Good awesome lists
do better: their entries name a concrete mechanism, a proper noun, a number, or
an honest limitation.

This module mines the README for those specifics. It reads bullet lists (where
projects actually enumerate features), scores each candidate on how informative
it is, and keeps the best few. Scoring rewards:

* concrete nouns, versions, numbers, file formats, protocol names
* a length that fits one line
* **distinctiveness** — a bullet whose wording is common across the corpus
  ("Open source", "Easy to use") is worth nothing, while one that is rare
  across the corpus is likely specific to this tool

The last point is what ``data/corpus.json`` provides: document frequencies over
every analysed README, so "works with Claude Code, Codex and Gemini CLI" can be
recognised as boilerplate while "pools five ChatGPT accounts and rotates on
429" stands out.
"""

from __future__ import annotations

import math
import re
from typing import Any, Iterable

from .util import DATA_DIR, read_json, strip_markdown, truncate, write_json

CORPUS_PATH = DATA_DIR / "corpus.json"

#: Bullets shorter than this are labels, not explanations.
MIN_LENGTH = 24
#: Longer than this and it will not fit a table cell.
MAX_LENGTH = 190

#: Minimum score for a bullet to be worth showing. Showing two real features
#: beats padding the list with install steps, so a README that has nothing
#: concrete simply gets no highlights and the renderer falls back to its
#: summary.
MIN_SCORE = 7.0

#: Openers that signal marketing filler rather than a concrete capability.
FILLER_RE = re.compile(
    r"^(open[- ]?source|free|easy|simple|fast|lightweight|powerful|modern|"
    r"flexible|beautiful|blazing|the best|a (?:fast|simple|modern|powerful)|"
    r"fully|highly|very|just|simply|no more|say goodbye|introducing|"
    r"welcome to|get started|why |what |features?$|note[:s]?|"
    r"开源|免费|简单|强大|优雅|快速|轻量|欢迎|介绍)\b",
    re.IGNORECASE,
)

#: Words that make a bullet concrete: mechanisms, formats, protocols, numbers.
CONCRETE_RE = re.compile(
    r"\b(?:\d+|one[- ]click|single[- ]click|"
    r"api|cli|gui|sdk|json|ya?ml|toml|sqlite|postgres|redis|docker|kubernetes|"
    r"oauth|jwt|sso|mcp|http|https|grpc|websocket|ssh|tls|e2ee|"
    r"macos|windows|linux|ios|android|wsl|termux|"
    r"claude code|codex|gemini|opencode|cursor|copilot|aider|cline|"
    r"deepseek|kimi|qwen|glm|ollama|openrouter|bedrock|vertex|"
    r"worktree|subagent|webhook|statusline|tui|daemon|proxy|gateway|"
    r"quota|token|rate[- ]limit|failover|encrypt\w*|"
    r"支持|自动|无需|一键|加密|隔离|并发|兼容)",
    re.IGNORECASE,
)

#: A bullet that is really a link dump or a badge row.
LINKY_RE = re.compile(r"^\s*[\[!]|https?://\S+\s*$")

#: Markdown heading text we never want as a highlight.
HEADING_RE = re.compile(r"^#{1,6}\s")

#: Installation, download and packaging bullets. Useful in a README, useless as
#: a description of what the tool does.
INSTALL_RE = re.compile(
    r"\b(?:download|install(?:er|ation)?|unzip|\.dmg|\.exe|\.apk|\.deb|appimage|"
    r"brew install|npm i |npx |pip install|cargo install|docker pull|"
    r"system requirements|glibc|arm64|x86_64|see the .{0,25}guide|"
    r"grab a build|all builds|release page|getting started|"
    r"下载|安装|解压|构建)\b",
    re.IGNORECASE,
)

#: Repository-layout bullets ("happy-cli: the original CLI", "packages/server: …").
LAYOUT_RE = re.compile(
    r"^(?:packages?|src|apps?|lib|crates|cmd|internal|docs?)/[\w./-]*\s*[:—-]"
    r"|^[\w.-]*(?:-cli|-server|-app|-core|-sdk|\.dev)\s*[:—-]\s",
    re.IGNORECASE,
)

#: Configuration / credential file paths — implementation detail, not a feature.
CONFIG_PATH_RE = re.compile(r"[\w.-]+\.(?:json|toml|ya?ml|ini|env)\b", re.IGNORECASE)

#: Environment-variable knobs, also implementation detail.
ENVVAR_RE = re.compile(r"\b[A-Z][A-Z0-9_]{4,}\s*=")

#: Section headings whose bullets are the most likely to be real capabilities.
FEATURE_SECTION_RE = re.compile(
    r"feature|what (?:you get|it does|it solves|'s new)|highlight|capabilit|"
    r"why (?:use|choose|magpie|switch)|key (?:feature|benefit)|benefits|"
    r"功能|特性|亮点|能做什么|核心|优势",
    re.IGNORECASE,
)

#: Section headings whose bullets are *never* capabilities. Skipping these
#: outright is more predictable than scoring them down: a "System Requirements"
#: bullet is dense with concrete tokens (versions, architectures) and outscored
#: real features under a purely lexical score.
NON_FEATURE_SECTION_RE = re.compile(
    r"install|download|requirement|system requirement|prerequisit|setup|"
    r"getting started|quick ?start|usage|how to (?:run|use|install)|"
    r"configuration|config\b|environment|cli (?:reference|command)|"
    r"command(?:s)?\b|api reference|reference|options?\b|"
    r"troubleshoot|faq|known issue|limitation|note|changelog|release|"
    r"roadmap|todo|contribut|licen[cs]e|sponsor|acknowledg|credit|"
    r"star history|community|screenshot|demo|benchmark|architecture|"
    r"project structure|repository|layout|directory|"
    r"安装|下载|配置|使用|快速开始|常见问题|更新|许可|贡献|架构|目录",
    re.IGNORECASE,
)

#: Verbs that describe what a tool *does* to a problem.
ACTION_RE = re.compile(
    r"\b(?:switch(?:es|ing)?|route[sd]?|rotat\w+|pool\w*|sync\w*|encrypt\w*|"
    r"isolat\w+|resum\w+|delegat\w+|orchestrat\w+|track\w*|meter\w*|shar\w+|"
    r"inject\w*|expos\w+|convert\w*|aggregat\w+|failover|fail(?:s|ing)? over|"
    r"detect\w*|monitor\w*|manag\w+|generat\w+|run[s]? |keep[s]? |let[s]? you|"
    r"allows? you|支持|自动|无需|可以)",
    re.IGNORECASE,
)

#: A comma-heavy bullet is usually an enumeration (a model list, a platform
#: list), not a description.
_ENUM_SPLIT_RE = re.compile(r",|、")

_BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.*)$")
_HEADING_LINE_RE = re.compile(r"^\s*#{1,6}\s+(.*)$")


def extract_highlights(
    body: str,
    *,
    corpus: dict[str, int] | None = None,
    limit: int = 4,
) -> list[str]:
    """Return up to ``limit`` concrete, distinctive feature bullets.

    Bullets are tracked with the heading they appear under. Only bullets inside
    a feature-like section are considered, and bullets inside a known
    non-feature section (installation, configuration, FAQ, licence, credits) are
    skipped outright. Section context is by far the strongest signal available:
    the same sentence is a capability under "Features" and an instruction under
    "Installation".
    """
    corpus = corpus or {}
    total_docs = int(corpus.get("__documents__", 0)) or 0

    candidates: list[tuple[float, str]] = []
    seen: set[str] = set()
    # None = before any heading; True/False = inside a feature / non-feature one.
    in_features: bool | None = None

    for raw in body.split("\n"):
        heading = _HEADING_LINE_RE.match(raw)
        if heading:
            title = heading.group(1)
            if NON_FEATURE_SECTION_RE.search(title):
                in_features = False
            elif FEATURE_SECTION_RE.search(title):
                in_features = True
            else:
                in_features = None
            continue

        if in_features is False:
            continue

        match = _BULLET_RE.match(raw)
        if not match:
            continue
        text = strip_markdown(match.group(1)).strip()
        text = re.sub(r"\s+", " ", text)
        if not _is_candidate(text):
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        candidates.append((_score(text, corpus, total_docs, in_features is True), text))

    candidates.sort(key=lambda pair: (-pair[0], pair[1]))
    return [
        truncate(text, MAX_LENGTH)
        for score, text in candidates[:limit]
        if score >= MIN_SCORE
    ]


def _is_candidate(text: str) -> bool:
    """Reject anything that cannot be a description of a capability.

    Install steps, download links and repository-layout lines are rejected
    outright rather than scored down. They are dense with concrete tokens
    (versions, architectures, file paths) and reliably outscored real features
    under a purely lexical score, so a penalty was not enough.
    """
    if len(text) < MIN_LENGTH or len(text) > 400:
        return False
    if LINKY_RE.match(text) or HEADING_RE.match(text):
        return False
    # Needs some real words, not just punctuation or emoji.
    if len(re.findall(r"[A-Za-z\u4e00-\u9fff]{2,}", text)) < 4:
        return False
    # A markdown table row or a stray separator.
    if text.count("|") >= 2:
        return False
    # Installation / packaging / repo layout / config plumbing.
    if INSTALL_RE.search(text) or LAYOUT_RE.match(text):
        return False
    if CONFIG_PATH_RE.search(text) or ENVVAR_RE.search(text):
        return False
    # A bare enumeration of names.
    if _enumeration_penalty(text) > 0:
        return False
    return True


def _enumeration_penalty(text: str) -> float:
    """Detect bullets that are really a list of names rather than a claim."""
    parts = [p.strip() for p in _ENUM_SPLIT_RE.split(text) if p.strip()]
    if len(parts) < 4:
        return 0.0
    short = sum(1 for p in parts if len(p.split()) <= 2)
    if short / len(parts) >= 0.6:
        return 4.0 + min(len(parts), 12) * 0.25
    return 0.0


def _score(
    text: str,
    corpus: dict[str, int],
    total_docs: int,
    in_feature_section: bool,
) -> float:
    """How informative is this bullet as a one-line description?"""
    score = 0.0

    # Bullets from a Features-style section are far more likely to be real
    # capabilities rather than install steps or credits.
    if in_feature_section:
        score += 6.0

    # Concrete vocabulary.
    score += 2.0 * len(CONCRETE_RE.findall(text))

    # Numbers are almost always specific and checkable.
    score += 1.5 * len(re.findall(r"\b\d+\b", text))

    # Marketing filler is penalised, and a bullet that *starts* with it is
    # usually a tagline rather than a capability.
    if FILLER_RE.match(text):
        score -= 4.0

    # Install instructions, download links and repo layout are not features.
    if INSTALL_RE.search(text):
        score -= 5.0
    if LAYOUT_RE.match(text):
        score -= 6.0
    # A bullet naming config files or env vars is implementation detail.
    if CONFIG_PATH_RE.search(text) or ENVVAR_RE.search(text):
        score -= 3.0
    score -= _enumeration_penalty(text)

    # Length: one comfortable line is ideal.
    length = len(text)
    if 45 <= length <= 150:
        score += 2.0
    elif length < 35:
        score -= 1.0

    # Distinctiveness against the corpus. A bullet made of words that appear in
    # most READMEs says nothing about this tool.
    if total_docs:
        words = [w for w in re.findall(r"[a-z][a-z0-9+.#-]{2,}", text.lower())]
        if words:
            idf = [math.log(total_docs / max(corpus.get(w, 0), 1)) for w in set(words)]
            score += 1.2 * (sum(idf) / len(idf))

    # A bullet describing an action the tool performs beats a noun phrase.
    if ACTION_RE.search(text):
        score += 2.0

    return score


def is_descriptive(text: str) -> bool:
    """Is this text a description of what a tool does, rather than an instruction?

    Used by the renderer too, because a README's *opening* line is often an
    install command ("If you want Codex in your code editor, install in your
    IDE") or a shell snippet, and quoting that as the summary is worse than
    saying nothing.
    """
    text = (text or "").strip()
    if len(text) < 20:
        return False
    # HTML entities and separator bullets only. READMEs that open with a
    # centred badge strip produce "&nbsp;&bull;&nbsp; &nbsp;&bull;&nbsp;".
    if text.count("&nbsp;") >= 2 or text.count("•") >= 2:
        return False
    if not re.search(r"[A-Za-z\u4e00-\u9fff]{3,}", text):
        return False
    if INSTALL_RE.search(text) or LAYOUT_RE.match(text):
        return False
    if CONFIG_PATH_RE.search(text) or ENVVAR_RE.search(text):
        return False
    # Shell/prompt snippets.
    if re.search(r"(?:^|\s)(?:curl|wget|git clone|npm|npx|pnpm|yarn|pip|uv|brew|docker)\s", text):
        return False
    if text.count("$ ") or text.count("&&") >= 1:
        return False
    # Configuration prose in Chinese ("默认端口 19528，可在设置中关闭"): a
    # description should say what the tool does, not how to configure it.
    if re.search(r"(?:默认|端口|监听|设置中|可通过|参数|环境变量|配置文件|启动|运行命令)", text):
        return False
    return True


def best_description(
    summary: str,
    highlights: list[str],
    *,
    min_summary: int = 55,
) -> str:
    """Choose the most informative single description for a tool.

    Prefers the README's own opening sentence when it is substantive and
    descriptive, otherwise the strongest highlight. This is the logic that keeps
    entries from restating their category name.
    """
    summary = (summary or "").strip()
    usable = [h for h in (highlights or []) if is_descriptive(h)]

    if is_descriptive(summary) and len(summary) >= min_summary:
        lead, rest = summary, usable[:1]
    elif usable:
        lead, rest = usable[0], usable[1:2]
    elif is_descriptive(summary):
        lead, rest = summary, []
    else:
        # Nothing usable. Returning the raw summary here would put an install
        # command in the table, so return nothing and let the caller fall back
        # to the repository's own description.
        return ""

    parts = [p for p in [lead] + rest if p]
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


# --------------------------------------------------------------------------
# Corpus statistics
# --------------------------------------------------------------------------


def build_corpus(bodies: Iterable[str]) -> dict[str, Any]:
    """Document frequencies over every analysed README.

    Stored so that ``extract_highlights`` can tell boilerplate from specifics
    without re-reading every README.
    """
    df: dict[str, int] = {}
    documents = 0
    for body in bodies:
        if not body:
            continue
        documents += 1
        for word in set(re.findall(r"[a-z][a-z0-9+.#-]{2,}", strip_markdown(body).lower())):
            df[word] = df.get(word, 0) + 1
    df["__documents__"] = documents
    return df


def save_corpus(corpus: dict[str, Any]) -> None:
    write_json(CORPUS_PATH, corpus)


def load_corpus() -> dict[str, int]:
    data = read_json(CORPUS_PATH, default={}) or {}
    return data if isinstance(data, dict) else {}
