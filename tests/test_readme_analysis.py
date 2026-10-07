"""Unit tests for the README analyser.

These are the tests that matter most: the analyser's output is what the README
claims about every tool, so a regression here silently misinforms readers.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from agentindex.readme_analysis import (  # noqa: E402
    analyse,
    assess_friction,
    detect_agents,
    detect_capabilities,
    extract_install_hint,
    score_docs,
    strip_markdown,
    summarise,
)

TURNKEY_README = """
# SuperSwitch

[![npm](https://img.shields.io/npm/v/superswitch)](https://npmjs.com/superswitch)

SuperSwitch keeps your coding agent running when one account runs out of quota.
It watches your remaining usage and automatically switches to the next account.

## Quick start

```bash
npx superswitch@latest
```

That is it — no configuration file is required. The desktop app walks you
through signing in. No coding required.

## Features

- Multi-account switching with automatic failover
- Quota dashboard showing remaining usage and reset time
- Works with Claude Code and Codex

## Troubleshooting

See the FAQ. Licensed MIT.
"""

HARD_README = """
# infra-gateway

A self-hosted gateway.

## Installation

```bash
git clone https://github.com/example/infra-gateway
cd infra-gateway
docker compose up -d
```

## Configuration

Create a `.env` file and set the following environment variables. You will need
an API key from each upstream provider. The service requires PostgreSQL and
Redis. Run the database migration before first start. Put nginx in front of it
and configure a reverse proxy with an SSL certificate.
"""


class TestStripMarkdown(unittest.TestCase):
    def test_removes_code_fences_and_links(self):
        text = strip_markdown("# Title\n\n```bash\nrm -rf /\n```\n\nSee [docs](http://x).")
        self.assertNotIn("rm -rf", text)
        self.assertIn("docs", text)
        self.assertNotIn("http://x", text)

    def test_keeps_prose(self):
        self.assertIn("hello world", strip_markdown("hello **world**"))


class TestCapabilities(unittest.TestCase):
    def test_detects_multi_account_and_failover(self):
        caps, evidence, _ = detect_capabilities(TURNKEY_README)
        self.assertIn("multi-account-switching", caps)
        self.assertIn("auto-failover", caps)
        self.assertIn("quota-management", caps)
        self.assertTrue(evidence["multi-account-switching"])

    def test_evidence_quotes_the_readme(self):
        _, evidence, _ = detect_capabilities(TURNKEY_README)
        self.assertIn("account", evidence["multi-account-switching"].lower())

    def test_chinese_patterns_detected(self):
        caps, _, _ = detect_capabilities("支持多账号切换，额度用完后自动切换。")
        self.assertIn("multi-account-switching", caps)
        self.assertIn("auto-failover", caps)

    def test_negated_capability_not_credited(self):
        # "does not support" must not grant the capability when it is the only mention.
        caps, _, _ = detect_capabilities("This tool does not support multi-account switching.")
        self.assertNotIn("multi-account-switching", caps)

    def test_negation_overridden_by_later_positive_mention(self):
        body = (
            "Earlier versions did not support multi-account switching. "
            "Version 2 adds multi-account switching with an account pool."
        )
        caps, _, _ = detect_capabilities(body)
        self.assertIn("multi-account-switching", caps)

    def test_no_capabilities_on_empty(self):
        caps, _, _ = detect_capabilities("")
        self.assertEqual(caps, [])


class TestFriction(unittest.TestCase):
    def test_turnkey_readme_is_low_friction(self):
        result = assess_friction(TURNKEY_README, strip_markdown(TURNKEY_README))
        self.assertIn(result.level, {"turnkey", "low"})
        self.assertTrue(result.out_of_the_box)
        self.assertTrue(result.non_programmer_friendly)

    def test_server_readme_is_high_friction(self):
        result = assess_friction(HARD_README, strip_markdown(HARD_README))
        self.assertIn(result.level, {"moderate", "high"})
        self.assertFalse(result.out_of_the_box)
        self.assertFalse(result.non_programmer_friendly)
        self.assertGreater(result.score, 50)

    def test_friction_ordering(self):
        easy = assess_friction(TURNKEY_README, strip_markdown(TURNKEY_README))
        hard = assess_friction(HARD_README, strip_markdown(HARD_README))
        self.assertLess(easy.score, hard.score)

    def test_notes_are_bilingual(self):
        result = assess_friction(TURNKEY_README, strip_markdown(TURNKEY_README))
        self.assertTrue(result.note_en)
        self.assertTrue(result.note_zh)
        # The Chinese note must actually be Chinese.
        self.assertTrue(any("\u4e00" <= ch <= "\u9fff" for ch in result.note_zh))

    def test_detects_platforms(self):
        result = assess_friction(
            "Available for macOS, Windows and Linux. Also an iOS app.",
            "Available for macOS, Windows and Linux. Also an iOS app.",
        )
        self.assertIn("macOS", result.platforms)
        self.assertIn("iOS", result.platforms)

    def test_score_bounded(self):
        for body in ("", "npx x", HARD_README, TURNKEY_README * 3):
            result = assess_friction(body, strip_markdown(body))
            self.assertGreaterEqual(result.score, 0)
            self.assertLessEqual(result.score, 100)


class TestDocScore(unittest.TestCase):
    def test_rich_readme_scores_higher(self):
        rich = score_docs(TURNKEY_README)[0]
        poor = score_docs("# x\n\nhi")[0]
        self.assertGreater(rich, poor)

    def test_score_bounded(self):
        self.assertLessEqual(score_docs(TURNKEY_README * 20)[0], 100)

    def test_signals_reported(self):
        _, signals = score_docs(TURNKEY_README)
        self.assertTrue(any("quick" in s.lower() for s in signals))


class TestAgents(unittest.TestCase):
    def test_detects_known_agents(self):
        agents = detect_agents("Works with Claude Code, Codex and Gemini CLI.")
        self.assertIn("Claude Code", agents)
        self.assertIn("Codex", agents)
        self.assertIn("Gemini CLI", agents)

    def test_empty_when_none(self):
        self.assertEqual(detect_agents("a tool for nothing in particular"), [])


class TestInstallHint(unittest.TestCase):
    def test_finds_npx(self):
        self.assertIn("npx", extract_install_hint(TURNKEY_README))

    def test_finds_docker(self):
        self.assertIn("docker", extract_install_hint(HARD_README))

    def test_empty_when_absent(self):
        self.assertEqual(extract_install_hint("# x\n\nno code here"), "")


class TestSummarise(unittest.TestCase):
    def test_prefers_readme_prose_over_description(self):
        summary, _ = summarise(TURNKEY_README, "github description")
        self.assertIn("SuperSwitch", summary)
        self.assertNotIn("github description", summary)

    def test_falls_back_to_description(self):
        summary, _ = summarise("# Title\n\n![badge](x)\n", "A neat tool.")
        self.assertIn("neat tool", summary)

    def test_skips_badges(self):
        body = "# T\n\n[![b](i)](u)\n\n![img](x)\n\nThe real summary lives here.\n"
        summary, _ = summarise(body, "")
        self.assertIn("real summary", summary)


class TestAnalyseEndToEnd(unittest.TestCase):
    def test_produces_complete_record(self):
        result = analyse("acme/tool", TURNKEY_README, "desc", "raw:HEAD/README.md")
        self.assertEqual(result.full_name, "acme/tool")
        self.assertGreater(result.readme_chars, 100)
        self.assertTrue(result.capabilities)
        self.assertGreater(result.doc_score, 0)
        self.assertTrue(result.install_hint)
        self.assertTrue(result.summary_en)
        self.assertIn("Claude Code", result.agents)

    def test_roundtrip_through_dict(self):
        from agentindex.readme_analysis import ReadmeAnalysis

        original = analyse("acme/tool", TURNKEY_README, "desc")
        restored = ReadmeAnalysis.from_dict(original.as_dict())
        self.assertEqual(restored.capabilities, original.capabilities)
        self.assertEqual(restored.friction.level, original.friction.level)
        self.assertEqual(restored.doc_score, original.doc_score)

    def test_handles_empty_readme(self):
        result = analyse("acme/empty", "", "")
        self.assertEqual(result.capabilities, [])
        self.assertEqual(result.readme_chars, 0)

    def test_handles_emoji_and_cjk_without_crashing(self):
        body = "# 工具 🚀\n\n支持多账号切换，额度用完自动切换账号。手机 App 远程控制。\n"
        result = analyse("acme/cjk", body, "")
        self.assertIn("multi-account-switching", result.capabilities)
        self.assertIn("mobile-access", result.capabilities)


if __name__ == "__main__":
    unittest.main()
