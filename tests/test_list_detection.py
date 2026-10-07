"""Tests for curated-list detection and the supersede safety rules.

These guard the two regressions that produced a badly wrong index during
development: awesome-lists being treated as tools, and over-broad capability
patterns marking almost every tool as superseded.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from agentindex.readme_analysis import (  # noqa: E402
    MIN_LIST_SIGNALS,
    analyse,
    assess_list,
    detect_capabilities,
)

AWESOME_LIST_README = """
# Awesome Widgets

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome widgets, tools and resources.

## Contents

- [Editors](#editors)
- [Libraries](#libraries)
- [Resources](#resources)

## Editors

- [Widget One](https://github.com/a/one) - A widget editor for macOS
- [Widget Two](https://github.com/b/two) - Cross-platform widget editor
- [Widget Three](https://github.com/c/three) - Browser-based widget editor
- [Widget Four](https://github.com/d/four) - Terminal widget editor
- [Widget Five](https://github.com/e/five) - Vim widget plugin
- [Widget Six](https://github.com/f/six) - Emacs widget mode
- [Widget Seven](https://github.com/g/seven) - VS Code widget extension
- [Widget Eight](https://github.com/h/eight) - Sublime widget package
- [Widget Nine](https://github.com/i/nine) - JetBrains widget plugin
- [Widget Ten](https://github.com/j/ten) - Atom widget package
- [Widget Eleven](https://github.com/k/eleven) - Widget CLI
- [Widget Twelve](https://github.com/l/twelve) - Widget GUI
- [Widget Thirteen](https://github.com/m/thirteen) - Widget library
- [Widget Fourteen](https://github.com/n/fourteen) - Widget framework
- [Widget Fifteen](https://github.com/o/fifteen) - Widget toolkit
- [Widget Sixteen](https://github.com/p/sixteen) - Widget SDK
- [Widget Seventeen](https://github.com/q/seventeen) - Widget IDE
- [Widget Eighteen](https://github.com/r/eighteen) - Widget server
- [Widget Nineteen](https://github.com/s/nineteen) - Widget client
- [Widget Twenty](https://github.com/t/twenty) - Widget proxy
- [Widget Twentyone](https://github.com/u/twentyone) - Widget gateway
- [Widget Twentytwo](https://github.com/v/twentytwo) - Widget memory
- [Widget Twentythree](https://github.com/w/twentythree) - Widget skills
- [Widget Twentyfour](https://github.com/x/twentyfour) - Widget plugins
- [Widget Twentyfive](https://github.com/y/twentyfive) - Widget orchestration
- [Widget Twentysix](https://github.com/z/twentysix) - Widget mobile app

## Contributing

Contributions welcome! Please add a link via pull request.
"""

REAL_TOOL_README = """
# WidgetRunner

WidgetRunner is a desktop app that keeps your coding agent working when an
account runs out of quota. It watches remaining usage and switches automatically.

## Installation

Download the installer for macOS or Windows, or run:

```bash
npx widgetrunner@latest
```

## Contents

- Features
- Configuration

## Features

- Multi-account switching with automatic failover between accounts
- Quota dashboard showing remaining usage and reset time

## Contributing

See CONTRIBUTING.md.
"""


class TestListDetection(unittest.TestCase):
    def test_awesome_list_detected(self):
        result = assess_list("awesome-widgets", AWESOME_LIST_README)
        self.assertTrue(result.is_list)
        self.assertGreaterEqual(result.score, MIN_LIST_SIGNALS)
        self.assertTrue(result.signals)

    def test_real_tool_not_detected_as_list(self):
        result = assess_list("widgetrunner", REAL_TOOL_README)
        self.assertFalse(result.is_list, f"false positive: {result.signals}")

    def test_list_name_alone_is_not_enough(self):
        # A repo called "awesome-thing" that is actually a tool must survive.
        body = "# awesome-thing\n\nA CLI that switches accounts.\n\n```bash\nnpx awesome-thing\n```\n"
        result = assess_list("awesome-thing", body)
        self.assertFalse(result.is_list, f"name alone should not exclude: {result.signals}")

    def test_awesome_list_gets_no_capabilities(self):
        analysis = analyse("acme/awesome-widgets", AWESOME_LIST_README, "")
        self.assertTrue(analysis.is_curated_list)
        self.assertEqual(
            analysis.capabilities,
            [],
            "a directory must not be credited with capabilities it merely describes",
        )

    def test_real_tool_keeps_capabilities(self):
        analysis = analyse("acme/widgetrunner", REAL_TOOL_README, "")
        self.assertFalse(analysis.is_curated_list)
        self.assertIn("multi-account-switching", analysis.capabilities)

    def test_roundtrip_preserves_list_flag(self):
        from agentindex.readme_analysis import ReadmeAnalysis

        analysis = analyse("acme/awesome-widgets", AWESOME_LIST_README, "")
        restored = ReadmeAnalysis.from_dict(analysis.as_dict())
        self.assertTrue(restored.is_curated_list)

    def test_empty_readme_is_not_a_list(self):
        self.assertFalse(assess_list("x", "").is_list)


class TestCapabilitySpecificity(unittest.TestCase):
    """Guards against the over-detection regression.

    Generic prose must not credit capabilities. During development a README
    containing the words 'provider', 'memory' and 'proxy' in passing scored
    20+/25 capabilities, which made the elimination engine retire 147 of 255
    tools.
    """

    def test_generic_prose_credits_little(self):
        body = (
            "# Tool\n\n"
            "This project is a provider of solutions. It has a memory of past "
            "releases. It uses a proxy for downloads. It supports plugins. "
            "It is a gateway to productivity. It manages quota for your team.\n"
        )
        caps, _, _ = detect_capabilities(body)
        self.assertLess(
            len(caps), 8, f"generic prose should not credit many capabilities, got {caps}"
        )

    def test_specific_phrasing_credits_capability(self):
        body = "This tool lets you switch between accounts automatically when quota runs out."
        caps, _, _ = detect_capabilities(body)
        self.assertIn("multi-account-switching", caps)
        self.assertIn("quota-management", caps)

    def test_cross_agent_needs_two_distinct_agents(self):
        one, _, _ = detect_capabilities("Works with Claude Code.")
        self.assertNotIn("cross-agent-support", one)

        two, _, _ = detect_capabilities("Works with Claude Code and Codex.")
        self.assertIn("cross-agent-support", two)

    def test_cross_agent_evidence_lists_agents(self):
        _, evidence, _ = detect_capabilities("Supports Claude Code, Codex and Gemini CLI.")
        self.assertIn("Claude Code", evidence["cross-agent-support"])

    def test_chinese_specific_phrasing(self):
        caps, _, _ = detect_capabilities("支持多账号切换，额度用完后自动切换到下一个账号。")
        self.assertIn("multi-account-switching", caps)
        self.assertIn("auto-failover", caps)

    def test_mcp_still_detected(self):
        caps, _, _ = detect_capabilities("Add MCP servers to your agent.")
        self.assertIn("mcp-support", caps)


if __name__ == "__main__":
    unittest.main()
