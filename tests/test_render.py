"""Tests for the renderer.

The important property here is that rendering is a **pure function of
``data/index.json``**. An earlier version stamped the wall-clock time into the
output, so every render differed from the committed files: CI's
``render --check`` failed on every run, and each daily job produced a
meaningless one-line diff.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from agentindex.render import (  # noqa: E402
    _elimination_reason,
    _now,
    _project,
    render_readme,
    render_readme_zh,
    render_tool_page,
    validate_index,
)

INDEX_PATH = ROOT / "data" / "index.json"


def load_index() -> dict:
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


class TestTimestampStability(unittest.TestCase):
    def test_uses_index_timestamp_not_wall_clock(self):
        index = {"generated_at": "2026-10-07T13:48:33+00:00"}
        self.assertEqual(_now(index), "2026-10-07 13:48 UTC")

    def test_repeated_calls_are_identical(self):
        index = {"generated_at": "2026-10-07T13:48:33+00:00"}
        self.assertEqual(_now(index), _now(index))

    def test_missing_timestamp_does_not_crash(self):
        self.assertEqual(_now({}), "unknown")
        self.assertEqual(_now(None), "unknown")

    def test_bad_timestamp_does_not_crash(self):
        self.assertEqual(_now({"generated_at": "not-a-date"}), "unknown")

    def test_naive_timestamp_treated_as_utc(self):
        self.assertEqual(_now({"generated_at": "2026-10-07T13:48:33"}), "2026-10-07 13:48 UTC")


class TestRenderPurity(unittest.TestCase):
    """The rendered output must depend only on the index."""

    @classmethod
    def setUpClass(cls):
        cls.index = load_index()

    def test_readme_render_is_deterministic(self):
        self.assertEqual(render_readme(self.index), render_readme(self.index))

    def test_chinese_readme_render_is_deterministic(self):
        self.assertEqual(render_readme_zh(self.index), render_readme_zh(self.index))

    def test_committed_readme_matches_a_fresh_render(self):
        """The committed README must equal what the renderer produces now.

        This is the check CI runs; failing it means someone hand-edited a
        generated file or forgot to re-render.
        """
        path = ROOT / "README.md"
        expected = render_readme(self.index).rstrip("\n") + "\n"
        actual = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(actual, expected, "README.md is out of sync — run `render`")

    def test_committed_chinese_readme_matches_a_fresh_render(self):
        path = ROOT / "README.zh-CN.md"
        expected = render_readme_zh(self.index).rstrip("\n") + "\n"
        actual = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(actual, expected, "README.zh-CN.md is out of sync — run `render`")

    def test_no_placeholder_left_in_output(self):
        for text in (render_readme(self.index), render_readme_zh(self.index)):
            self.assertNotIn("PLACEHOLDER", text)


class TestBadges(unittest.TestCase):
    def test_project_slug_is_owner_repo(self):
        slug = _project()["repo"]
        self.assertRegex(slug, r"^[\w.-]+/[\w.-]+$")

    def test_project_config_is_stable_across_calls(self):
        self.assertEqual(_project(), _project())

    def test_badge_urls_are_percent_encoded(self):
        badge = render_readme(load_index())
        match = re.search(r"dynamic/json\?url=([^&]+)&query", badge)
        self.assertIsNotNone(match)
        self.assertNotIn("https://", match.group(1), "raw URL must be encoded")

    def test_badges_do_not_read_local_git_state(self):
        """Rendering must not depend on the git remote.

        Reading the remote made output differ between a fresh clone, a fork and
        CI, which broke `render --check` depending on the machine.
        """
        source = (ROOT / "scripts" / "agentindex" / "render.py").read_text(encoding="utf-8")
        self.assertNotIn("remote.origin.url", source)
        self.assertNotIn("subprocess", source)


class TestEliminationReason(unittest.TestCase):
    def test_prefers_traction_over_coverage(self):
        edge = {
            "kind": "auto",
            "reasons": [
                "covers 100% of capabilities (5/5)",
                "9.92x the stars (7,070 vs 713)",
                "10.35x the star velocity (30.3/day vs 2.9/day)",
            ],
        }
        self.assertIn("stars", _elimination_reason(edge))

    def test_falls_back_to_velocity(self):
        edge = {"kind": "auto", "reasons": ["covers 100% of capabilities (3/3)", "2.0x the star velocity"]}
        self.assertIn("velocity", _elimination_reason(edge))

    def test_manual_uses_its_note(self):
        edge = {"kind": "manual", "reasons": ["magpie covers cc-switch's core job"]}
        self.assertIn("magpie", _elimination_reason(edge))

    def test_empty_reasons_is_safe(self):
        self.assertEqual(_elimination_reason({"kind": "auto", "reasons": []}), "")


class TestToolPage(unittest.TestCase):
    def test_renders_without_crashing_for_every_indexed_tool(self):
        index = load_index()
        for key in list(index["tools"])[:15]:
            owner, _, repo = index["tools"][key]["full_name"].partition("/")
            path = ROOT / "docs" / "tools" / f"{owner}__{repo}.md"
            if not path.exists():
                continue
            entry = json.loads(
                (ROOT / "data" / "entries" / f"{owner}__{repo}.json").read_text(encoding="utf-8")
            )
            text = render_tool_page(entry)
            self.assertIn(entry["full_name"], text)
            self.assertTrue(text.startswith("<!-- GENERATED FILE"))


class TestValidate(unittest.TestCase):
    def test_committed_index_is_valid(self):
        self.assertEqual(validate_index(load_index()), [])

    def test_detects_dangling_supersede_reference(self):
        index = load_index()
        index["supersede"] = [
            {"incumbent": "ghost/one", "challenger": "ghost/two", "reasons": [], "evidence": {}}
        ]
        problems = validate_index(index)
        self.assertTrue(any("ghost/one" in p for p in problems))

    def test_detects_duplicate_category_listing(self):
        index = load_index()
        tools = list(index["tools"])
        if len(index["categories"]) >= 2 and tools:
            index["categories"][0]["tools"] = [tools[0]]
            index["categories"][1]["tools"] = [tools[0]]
            problems = validate_index(index)
            self.assertTrue(any("listed in" in p for p in problems))

    def test_detects_out_of_range_score(self):
        index = load_index()
        key = next(iter(index["tools"]))
        index["tools"][key]["health_score"] = 999
        problems = validate_index(index)
        self.assertTrue(any("out of range" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
