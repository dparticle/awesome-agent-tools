"""Tests for the write-safety valve.

The scenario: GitHub is unreachable, every metadata fetch fails, and the crawl
finds zero tools. Without a guard the daily workflow would commit an empty
index and the project would look abandoned until somebody noticed.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from agentindex.pipeline import PipelineStats, _check_shrink_safety  # noqa: E402


class TestShrinkSafety(unittest.TestCase):
    def test_first_run_is_allowed(self):
        stats = PipelineStats(accepted=0)
        self.assertEqual(_check_shrink_safety(0, 0, stats), "")

    def test_zero_tools_over_existing_index_is_refused(self):
        stats = PipelineStats(accepted=0)
        reason = _check_shrink_safety(0, 108, stats)
        self.assertTrue(reason)
        self.assertIn("0 tools", reason)

    def test_massive_shrink_is_refused(self):
        stats = PipelineStats(accepted=20)
        reason = _check_shrink_safety(20, 108, stats)
        self.assertTrue(reason)
        self.assertIn("less than half", reason)

    def test_modest_shrink_is_allowed(self):
        stats = PipelineStats(accepted=90)
        self.assertEqual(_check_shrink_safety(90, 108, stats), "")

    def test_growth_is_allowed(self):
        stats = PipelineStats(accepted=200)
        self.assertEqual(_check_shrink_safety(200, 108, stats), "")

    def test_half_exactly_is_allowed(self):
        stats = PipelineStats(accepted=54)
        self.assertEqual(_check_shrink_safety(54, 108, stats), "")

    def test_mostly_errored_run_is_refused(self):
        stats = PipelineStats(accepted=100, considered=200)
        stats.errors = [f"repo {i}: failed" for i in range(60)]
        reason = _check_shrink_safety(100, 108, stats)
        self.assertTrue(reason)
        self.assertIn("errored", reason)

    def test_few_errors_are_tolerated(self):
        stats = PipelineStats(accepted=100, considered=200)
        stats.errors = ["one repo failed"]
        self.assertEqual(_check_shrink_safety(100, 108, stats), "")

    def test_error_check_ignores_unknown_considered(self):
        stats = PipelineStats(accepted=100, considered=0)
        stats.errors = [f"e{i}" for i in range(50)]
        # Without a denominator we cannot judge the error rate, so allow.
        self.assertEqual(_check_shrink_safety(100, 108, stats), "")


if __name__ == "__main__":
    unittest.main()
