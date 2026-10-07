"""Shared helpers: UTF-8 safe IO, logging, text normalisation.

Standard library only — the pipeline must run on a bare GitHub Actions runner
and on a fresh clone with no `pip install` step.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Iterable

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "config"
DATA_DIR = REPO_ROOT / "data"
CACHE_DIR = DATA_DIR / "cache"
DOCS_DIR = REPO_ROOT / "docs"


# --------------------------------------------------------------------------
# Logging / console
# --------------------------------------------------------------------------


def setup_console() -> None:
    """Force UTF-8 on stdout/stderr.

    Windows defaults to a legacy code page (GBK on zh-CN) which raises
    UnicodeEncodeError the moment a README contains an emoji. GitHub Actions
    is UTF-8 already, but the pipeline is also meant to run locally.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
        except (AttributeError, ValueError):  # pragma: no cover - exotic streams
            pass


def get_logger(name: str = "agentindex", level: int | None = None) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S")
        )
        logger.addHandler(handler)
        logger.propagate = False
    env_level = os.environ.get("AGENTINDEX_LOG", "").upper()
    logger.setLevel(level or getattr(logging, env_level, logging.INFO))
    return logger


LOG = get_logger()


# --------------------------------------------------------------------------
# JSON IO
# --------------------------------------------------------------------------


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        LOG.warning("could not read %s: %s", path, exc)
        return default


def write_json(path: Path, payload: Any, *, sort_keys: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=sort_keys)
    path.write_text(text + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


# --------------------------------------------------------------------------
# Text helpers
# --------------------------------------------------------------------------

_WS_RE = re.compile(r"[ \t\u00a0]+")
_MULTI_NL_RE = re.compile(r"\n{3,}")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
_MD_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_MD_INLINE_CODE_RE = re.compile(r"`([^`]*)`")
_MD_EMPHASIS_RE = re.compile(r"(\*{1,3}|_{1,3})(?=\S)(.+?)(?<=\S)\1", re.DOTALL)
_HTML_TAG_RE = re.compile(r"<[^>]+>")


def strip_markdown(text: str) -> str:
    """Reduce Markdown to readable plain text for keyword matching."""
    text = _MD_CODE_FENCE_RE.sub(" ", text)
    text = _MD_IMAGE_RE.sub(r"\1", text)
    text = _MD_LINK_RE.sub(r"\1", text)
    text = _MD_INLINE_CODE_RE.sub(r"\1", text)
    text = _MD_EMPHASIS_RE.sub(r"\2", text)
    text = _HTML_TAG_RE.sub(" ", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = _WS_RE.sub(" ", text)
    return _MULTI_NL_RE.sub("\n\n", text).strip()


def normalise(text: str) -> str:
    """Lowercase + NFKC so full-width and accented forms match ASCII keywords."""
    return unicodedata.normalize("NFKC", text or "").lower()


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def truncate(text: str, limit: int, suffix: str = "…") -> str:
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    return text[: max(0, limit - len(suffix))].rstrip() + suffix


def slugify(text: str) -> str:
    text = normalise(text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "item"


def first_sentence(text: str, limit: int = 200) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    match = re.search(r"(?<=[.!?。！？])\s+", text)
    if match:
        text = text[: match.start()]
    return truncate(text, limit)


def dedupe_preserve_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        key = item.lower()
        if key not in seen:
            seen.add(key)
            out.append(item)
    return out


def escape_table_cell(text: str) -> str:
    """Make a string safe inside a Markdown table cell."""
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def human_number(value: int | float) -> str:
    value = float(value or 0)
    for threshold, suffix in ((1_000_000, "M"), (1_000, "k")):
        if value >= threshold:
            rendered = value / threshold
            return f"{rendered:.1f}{suffix}".replace(".0" + suffix, suffix)
    return str(int(value))
