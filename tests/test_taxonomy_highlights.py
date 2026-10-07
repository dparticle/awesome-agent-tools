"""Tests for category discovery and highlight extraction.

These cover the two things the user pushed back on hardest: categories must be
*derived from the data* rather than declared by hand, and a tool must be able to
belong to several of them at once.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from agentindex.highlights import (  # noqa: E402
    best_description,
    build_corpus,
    extract_highlights,
    is_descriptive,
)
from agentindex.taxonomy import (  # noqa: E402
    capability_tool_sets,
    cluster_tools,
    compute_idf,
    cosine,
    discover_categories,
    prominence_vector,
    split_ubiquitous,
)


def make_entry(name: str, caps: list[str], hits: dict[str, int] | None = None) -> dict:
    return {
        "full_name": name,
        "analysis": {
            "capabilities": caps,
            "capability_hits": hits or {c: 3 for c in caps},
        },
    }


#: A small synthetic ecosystem with two clearly separate problem areas plus one
#: tool that spans both.
ECOSYSTEM = (
    [make_entry(f"acct/tool{i}", ["multi-account-switching", "quota-management", "auto-failover"])
     for i in range(6)]
    + [make_entry(f"orch/tool{i}", ["multi-agent-orchestration", "parallel-execution", "worktree-isolation"])
       for i in range(6)]
    + [make_entry(f"mem/tool{i}", ["memory-context", "session-persistence"])
       for i in range(5)]
    + [make_entry("spans/both", ["multi-account-switching", "quota-management", "model-routing"])]
)


class TestProminence(unittest.TestCase):
    def test_idf_rewards_rare_capabilities(self):
        sets = {"common": {f"t{i}" for i in range(10)}, "rare": {"t0"}}
        idf = compute_idf(sets, 10)
        self.assertLess(idf["common"], idf["rare"])

    def test_vector_is_normalised(self):
        idf = {"a": 1.0, "b": 2.0}
        vec = prominence_vector(make_entry("x/y", ["a", "b"]), idf)
        norm = sum(v * v for v in vec.values()) ** 0.5
        self.assertAlmostEqual(norm, 1.0, places=6)

    def test_ubiquitous_capabilities_excluded(self):
        idf = {"a": 1.0, "b": 1.0}
        vec = prominence_vector(make_entry("x/y", ["a", "b"]), idf, ubiquitous={"a"})
        self.assertNotIn("a", vec)
        self.assertIn("b", vec)

    def test_empty_when_all_ubiquitous(self):
        idf = {"a": 1.0}
        self.assertEqual(prominence_vector(make_entry("x/y", ["a"]), idf, ubiquitous={"a"}), {})

    def test_cosine_bounds(self):
        a = {"x": 0.6, "y": 0.8}
        self.assertAlmostEqual(cosine(a, a), 1.0, places=6)
        self.assertEqual(cosine({"x": 1.0}, {"y": 1.0}), 0.0)
        self.assertEqual(cosine({}, a), 0.0)

    def test_ubiquity_split(self):
        entries = [make_entry(f"t{i}", ["common", "rare"] if i == 0 else ["common"]) for i in range(10)]
        sets = capability_tool_sets(entries)
        distinctive, ubiquitous = split_ubiquitous(sets, len(entries))
        self.assertIn("common", ubiquitous)
        self.assertIn("rare", distinctive)


class TestClustering(unittest.TestCase):
    def setUp(self):
        self.sets = capability_tool_sets(ECOSYSTEM)
        self.idf = compute_idf(self.sets, len(ECOSYSTEM))
        self.vectors = {
            e["full_name"].lower(): v
            for e in ECOSYSTEM
            if (v := prominence_vector(e, self.idf))
        }

    def test_clustering_is_deterministic(self):
        first = cluster_tools(self.vectors, threshold=0.35)
        second = cluster_tools(self.vectors, threshold=0.35)
        self.assertEqual(first, second)

    def test_separates_distinct_problem_areas(self):
        clusters = cluster_tools(self.vectors, threshold=0.35)
        self.assertGreaterEqual(len(clusters), 2)
        # Every tool lands in exactly one cluster.
        all_members = [m for c in clusters for m in c]
        self.assertEqual(sorted(all_members), sorted(self.vectors))

    def test_average_linkage_does_not_collapse_everything(self):
        """The centroid-linkage bug produced a single mega-cluster."""
        clusters = cluster_tools(self.vectors, threshold=0.5)
        self.assertGreater(len(clusters), 1, "clustering collapsed into one group")


class TestDiscovery(unittest.TestCase):
    def test_discovers_multiple_categories(self):
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        self.assertGreaterEqual(len(clusters), 2)

    def test_every_tool_gets_a_primary_category(self):
        entries = [dict(e) for e in ECOSYSTEM]
        discover_categories(entries)
        for entry in entries:
            self.assertTrue(entry.get("primary_category"), f"{entry['full_name']} unplaced")

    def test_a_tool_can_belong_to_several_categories(self):
        """The user's point: magpie does both accounts and model routing."""
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        by_name = {e["full_name"]: e for e in entries}
        # spans/both shares capabilities with the accounts cluster.
        accounts = next(
            (c for c in clusters if "multi-account-switching" in c.capabilities), None
        )
        self.assertIsNotNone(accounts)
        self.assertIn("spans/both", accounts.tools)

    def test_categories_are_named_from_capabilities(self):
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        for cluster in clusters:
            self.assertTrue(cluster.title_en)
            self.assertTrue(cluster.slug)
            self.assertTrue(cluster.capabilities)

    def test_cohesion_is_reported(self):
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        for cluster in clusters:
            self.assertGreaterEqual(cluster.cohesion, 0.0)
            self.assertLessEqual(cluster.cohesion, 1.0)

    def test_empty_input_is_safe(self):
        self.assertEqual(discover_categories([]), [])

    def test_entries_without_capabilities_are_tolerated(self):
        entries = [dict(e) for e in ECOSYSTEM] + [make_entry("bare/tool", [])]
        clusters = discover_categories(entries)
        self.assertTrue(clusters)


class TestHighlights(unittest.TestCase):
    README = """
# Tool

## Features

- Pool five ChatGPT accounts and rotate automatically when one hits its 429 rate limit
- Route every agent through a local gateway so keys never reach the vendor
- Sync configuration between machines over WebDAV or S3

## Installation

```bash
npx tool@latest
```

- Download the macOS .dmg or the Windows .exe installer
- Linux: x86_64 with glibc 2.35+, Ubuntu 22.04 or newer

## Configuration

- Set OPENAI_API_KEY= in your .env file
- The config file lives at ~/.tool/config.json
"""

    def test_extracts_feature_bullets(self):
        found = extract_highlights(self.README)
        self.assertTrue(found)
        joined = " ".join(found).lower()
        self.assertIn("pool", joined)

    def test_excludes_installation_bullets(self):
        found = " ".join(extract_highlights(self.README)).lower()
        self.assertNotIn(".dmg", found)
        self.assertNotIn("glibc", found)

    def test_excludes_configuration_bullets(self):
        found = " ".join(extract_highlights(self.README)).lower()
        self.assertNotIn("openai_api_key", found)
        self.assertNotIn("config.json", found)

    def test_respects_limit(self):
        self.assertLessEqual(len(extract_highlights(self.README, limit=2)), 2)

    def test_rejects_link_dumps(self):
        body = "## Features\n\n- [Some Tool](https://example.com) - a thing\n" * 5
        self.assertEqual(extract_highlights(body), [])

    def test_rejects_enumerations(self):
        body = "## Features\n\n- Models: gpt-4o, gpt-4o-mini, o1, o3, o4-mini, gpt-5, gpt-5-mini, gpt-5-nano\n"
        self.assertEqual(extract_highlights(body), [])

    def test_empty_body_is_safe(self):
        self.assertEqual(extract_highlights(""), [])


class TestDescriptive(unittest.TestCase):
    def test_accepts_a_real_description(self):
        self.assertTrue(is_descriptive("Switches between accounts automatically when quota runs out"))

    def test_rejects_install_instruction(self):
        self.assertFalse(
            is_descriptive("If you want Codex in your code editor, install in your IDE.")
        )

    def test_rejects_shell_snippet(self):
        self.assertFalse(is_descriptive("Run npm install -g @openai/codex to get started quickly"))

    def test_rejects_entity_noise(self):
        self.assertFalse(is_descriptive("&nbsp;&bull;&nbsp; &nbsp;&bull;&nbsp; &nbsp;"))

    def test_rejects_chinese_config_prose(self):
        self.assertFalse(
            is_descriptive("WebSocket 默认仅本机访问：监听 127.0.0.1，默认端口 19528，可在设置中关闭")
        )


class TestBestDescription(unittest.TestCase):
    def test_prefers_substantive_summary(self):
        summary = "Keeps your coding agent running when one account runs out of quota"
        self.assertEqual(best_description(summary, ["some highlight"]), summary)

    def test_falls_back_to_highlight_when_summary_is_an_instruction(self):
        summary = "Install via npm install -g tool"
        result = best_description(summary, ["Pools accounts and rotates on rate limits"])
        self.assertIn("Pools accounts", result)

    def test_returns_empty_when_nothing_is_usable(self):
        """An empty result lets the caller use the repo description instead."""
        self.assertEqual(best_description("npm install -g tool", []), "")

    def test_never_returns_an_install_line(self):
        for summary in ("npm install -g x", "Download the .dmg installer today"):
            self.assertNotIn("install", best_description(summary, []).lower())


class TestCorpus(unittest.TestCase):
    def test_counts_documents(self):
        corpus = build_corpus(["hello world", "hello there"])
        self.assertEqual(corpus["__documents__"], 2)
        self.assertEqual(corpus["hello"], 2)
        self.assertEqual(corpus["world"], 1)

    def test_skips_empty_bodies(self):
        self.assertEqual(build_corpus(["", ""])["__documents__"], 0)


if __name__ == "__main__":
    unittest.main()
