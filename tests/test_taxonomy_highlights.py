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
    cjk_ratio,
    effective_length,
    extract_highlights,
    first_sentence,
    has_cjk,
    is_descriptive,
)
from agentindex.readme_analysis import analyse  # noqa: E402
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

    def test_slugs_are_unique(self):
        """Regression: two clusters could inherit the same previous slug.

        When the taxonomy shifts, two different clusters can both match the same
        previous category. The uniqueness check used to run only on freshly
        generated slugs, so both inherited "billing" — producing a duplicate
        section, one of them empty.
        """
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        slugs = [c.slug for c in clusters]
        self.assertEqual(len(slugs), len(set(slugs)), f"duplicate slugs: {slugs}")

    def test_no_empty_categories(self):
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        for cluster in clusters:
            self.assertTrue(
                cluster.primary_tools, f"{cluster.slug} has no primary tools"
            )

    def test_tools_are_not_lost_across_categories(self):
        entries = [dict(e) for e in ECOSYSTEM]
        clusters = discover_categories(entries)
        primaries = [t for c in clusters for t in c.primary_tools]
        self.assertEqual(len(primaries), len(set(primaries)), "a tool has two primaries")
        self.assertEqual(set(primaries), {e["full_name"].lower() for e in entries})


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


class TestChineseHandling(unittest.TestCase):
    """The Chinese index must quote real Chinese text, never a translation."""

    ZH_README = """
# 工具

一个可以在多个账号之间自动切换的命令行工具，额度用完之前会提前提醒你。

## 功能特性

- 支持同时管理多个 Claude Code 账号，额度用完自动切换到下一个
- 实时监控 5 小时和 7 天的额度窗口，快用完时提前预警
- 所有凭据加密保存在本地，不会上传到任何服务器

## 安装

```bash
npm install -g tool
```

- 下载 macOS 的 .dmg 安装包或 Windows 的 .exe
"""

    def test_extracts_chinese_highlights(self):
        found = extract_highlights(self.ZH_README)
        self.assertTrue(found, "expected Chinese bullets to be extracted")
        joined = "".join(found)
        self.assertIn("账号", joined)

    def test_chinese_install_bullets_excluded(self):
        found = "".join(extract_highlights(self.ZH_README))
        self.assertNotIn(".dmg", found)
        self.assertNotIn("npm install", found)

    def test_has_cjk_detection(self):
        self.assertTrue(has_cjk("自动切换账号"))
        self.assertFalse(has_cjk("switch accounts"))

    def test_cjk_ratio(self):
        self.assertGreater(cjk_ratio("自动切换账号"), 0.9)
        self.assertEqual(cjk_ratio("switch accounts"), 0.0)

    def test_chinese_enumeration_rejected(self):
        body = "## 功能\n\n- 支持模型：gpt-4o、gpt-4o-mini、o1、o3、o4-mini、gpt-5、gpt-5-mini、gpt-5-nano\n"
        self.assertEqual(extract_highlights(body), [])

    def test_chinese_short_bullet_rejected(self):
        """Chinese has no spaces, so a word-count test would wrongly accept this."""
        body = "## 功能\n\n- 支持多账号\n- 支持切换\n- 支持监控\n"
        self.assertEqual(extract_highlights(body), [])

    def test_analyse_prefers_native_chinese(self):
        analysis = analyse("a/b", "English README about switching accounts", chinese_body=self.ZH_README)
        self.assertTrue(analysis.summary_zh_native or analysis.highlights_zh)
        self.assertTrue(analysis.highlights_zh)

    def test_analyse_without_chinese_is_empty_not_translated(self):
        analysis = analyse("a/b", "English README about switching accounts")
        self.assertEqual(analysis.summary_zh_native, "")
        self.assertEqual(analysis.highlights_zh, [])
        self.assertEqual(analysis.chinese_readme, "")


class TestChineseRatioGate(unittest.TestCase):
    """A README.zh-CN.md that is actually English must not be treated as Chinese."""

    def test_english_file_is_rejected(self):
        from agentindex.github import _chinese_ratio

        self.assertLess(_chinese_ratio("This is an English README. " * 50), 0.15)

    def test_short_stub_is_rejected(self):
        from agentindex.github import _chinese_ratio

        self.assertEqual(_chinese_ratio("中文"), 0.0)

    def test_real_chinese_passes(self):
        from agentindex.github import _chinese_ratio

        body = "这是一个中文说明文档，用来介绍工具的功能和使用方法。" * 20
        self.assertGreaterEqual(_chinese_ratio(body), 0.15)


class TestLanguageAwareLength(unittest.TestCase):
    """Chinese text must not be measured with Latin character thresholds."""

    def test_effective_length_counts_cjk_double(self):
        self.assertEqual(effective_length("abcd"), 4)
        self.assertEqual(effective_length("中文"), 4)

    def test_complete_chinese_sentence_is_not_padded(self):
        """A full Chinese sentence must not be treated as a short tagline.

        Raw character count made "…用你的 ChatGPT 订阅。" (44 chars) look shorter
        than the 80-char tagline threshold, so an unrelated feature bullet was
        appended to it.
        """
        summary = "Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。"
        result = best_description(summary, ["局域网共享：打开「在局域网共享」，为每个客户端创建网关 key"])
        self.assertEqual(result, summary)

    def test_chinese_sentence_split_without_space(self):
        """CJK sentences end with 。 and have no following space."""
        text = "这是一个完整的句子，用来描述工具的核心功能。这是第二句话，也应该被保留。"
        self.assertEqual(first_sentence(text), "这是一个完整的句子，用来描述工具的核心功能。")

    def test_latin_sentence_split_still_works(self):
        self.assertEqual(
            first_sentence("This is the first sentence of the description. And more."),
            "This is the first sentence of the description.",
        )

    def test_short_lead_is_not_used_alone(self):
        """"Never stop coding." is too short to stand as the whole description."""
        text = "Never stop coding. Routes every request through a local gateway."
        self.assertEqual(first_sentence(text), text)


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
