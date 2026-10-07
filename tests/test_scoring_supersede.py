"""Unit tests for scoring, gates, momentum and the elimination engine."""

from __future__ import annotations

import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from agentindex.readme_analysis import analyse  # noqa: E402
from agentindex.scoring import (  # noqa: E402
    assign_tier,
    compute_momentum,
    evaluate_gates,
    health_score,
    load_thresholds,
)
from agentindex.supersede import (  # noqa: E402
    ToolFacts,
    apply_manual_overrides,
    build_edges,
    coverage_ratio,
    evaluate_pair,
    resolve_states,
)

NOW = datetime.now(timezone.utc)


def iso(days_ago: int) -> str:
    return (NOW - timedelta(days=days_ago)).isoformat().replace("+00:00", "Z")


def make_repo(**overrides):
    repo = {
        "full_name": "acme/tool",
        "name": "tool",
        "owner": {"login": "acme"},
        "html_url": "https://github.com/acme/tool",
        "description": "A tool.",
        "stargazers_count": 5000,
        "forks_count": 100,
        "open_issues_count": 5,
        "subscribers_count": 50,
        "language": "TypeScript",
        "license": {"spdx_id": "MIT"},
        "topics": [],
        "created_at": iso(400),
        "updated_at": iso(1),
        "pushed_at": iso(1),
        "archived": False,
        "fork": False,
        "disabled": False,
        "default_branch": "main",
    }
    repo.update(overrides)
    return repo


RICH_README = """
# Tool

Tool is a coding-agent companion that keeps your agent working when an account
runs out of quota. It watches remaining usage and switches automatically.

Quick start: `npx tool`

## Installation

```bash
npx tool@latest
```

No configuration file is required to get started.

## Configuration

Advanced users can set the API key environment variable and point the tool at a
custom provider. The configuration file lives at `~/.tool/config.json`.

## Troubleshooting / FAQ

Common issues are listed here, including what to do when the login flow fails.

## Features

- Multi-account switching with automatic failover between accounts
- Quota dashboard showing remaining usage and reset time
- Works with Claude Code and Codex
- Parallel agent orchestration with git worktree isolation
- Memory and context persistence across sessions

## Architecture

The daemon watches the agent's session files and reacts to rate-limit errors.

## Roadmap

- Team collaboration with role-based access

## Changelog

See the release notes for the full changelog.

## Contributing

Pull requests are welcome. See CONTRIBUTING.md.

## License

MIT
"""


class TestMomentum(unittest.TestCase):
    def test_lifetime_fallback_without_history(self):
        m = compute_momentum(make_repo(stargazers_count=1000, created_at=iso(100)), [])
        self.assertEqual(m.basis, "lifetime")
        self.assertAlmostEqual(m.stars_per_day, 10.0, places=1)

    def test_history_basis_when_snapshot_exists(self):
        repo = make_repo(stargazers_count=2000, created_at=iso(400))
        history = [{"date": iso(10)[:10], "stars": 1000}]
        m = compute_momentum(repo, history)
        self.assertEqual(m.basis, "history")
        self.assertAlmostEqual(m.stars_per_day, 100.0, places=0)
        self.assertEqual(m.stars_gained, 1000)

    def test_young_steep_repo_is_fast_riser(self):
        m = compute_momentum(make_repo(stargazers_count=900, created_at=iso(30)), [])
        self.assertTrue(m.is_fast_riser)

    def test_old_slow_repo_is_not_fast_riser(self):
        m = compute_momentum(make_repo(stargazers_count=500, created_at=iso(2000)), [])
        self.assertFalse(m.is_fast_riser)

    def test_ignores_stale_history(self):
        repo = make_repo(stargazers_count=2000)
        history = [{"date": iso(400)[:10], "stars": 10}]
        m = compute_momentum(repo, history)
        self.assertEqual(m.basis, "lifetime")


class TestGates(unittest.TestCase):
    def setUp(self):
        self.cfg = load_thresholds()
        self.analysis = analyse("acme/tool", RICH_README, "desc")

    def test_popular_active_repo_passes(self):
        repo = make_repo()
        m = compute_momentum(repo, [])
        self.assertTrue(evaluate_gates(repo, self.analysis, m, self.cfg).passed)

    def test_archived_repo_fails(self):
        repo = make_repo(archived=True)
        result = evaluate_gates(repo, self.analysis, compute_momentum(repo, []), self.cfg)
        self.assertFalse(result.passed)
        self.assertTrue(any("archived" in r for r in result.reasons))

    def test_low_star_slow_repo_fails(self):
        repo = make_repo(stargazers_count=5, created_at=iso(900))
        result = evaluate_gates(repo, self.analysis, compute_momentum(repo, []), self.cfg)
        self.assertFalse(result.passed)

    def test_low_star_fast_riser_passes_star_gate(self):
        repo = make_repo(stargazers_count=100, created_at=iso(20))
        m = compute_momentum(repo, [])
        self.assertTrue(m.is_fast_riser)
        result = evaluate_gates(repo, self.analysis, m, self.cfg)
        self.assertFalse(any("stars" in r for r in result.reasons))

    def test_stale_repo_fails(self):
        repo = make_repo(pushed_at=iso(400))
        result = evaluate_gates(repo, self.analysis, compute_momentum(repo, []), self.cfg)
        self.assertFalse(result.passed)
        self.assertTrue(any("no push" in r for r in result.reasons))

    def test_tiny_readme_fails(self):
        repo = make_repo()
        tiny = analyse("acme/tool", "# x\n\nhi", "")
        result = evaluate_gates(repo, tiny, compute_momentum(repo, []), self.cfg)
        self.assertFalse(result.passed)

    def test_missing_readme_fails(self):
        repo = make_repo()
        result = evaluate_gates(repo, None, compute_momentum(repo, []), self.cfg)
        self.assertFalse(result.passed)
        self.assertTrue(any("README" in r for r in result.reasons))


class TestHealthScore(unittest.TestCase):
    def setUp(self):
        self.cfg = load_thresholds()
        self.analysis = analyse("acme/tool", RICH_README, "desc")

    def test_score_in_range(self):
        repo = make_repo()
        score, components = health_score(repo, self.analysis, compute_momentum(repo, []), self.cfg)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
        self.assertEqual(
            set(components), {"popularity", "momentum", "maintenance", "documentation", "accessibility"}
        )

    def test_more_stars_scores_higher(self):
        small = make_repo(stargazers_count=200)
        big = make_repo(stargazers_count=50000)
        s1, _ = health_score(small, self.analysis, compute_momentum(small, []), self.cfg)
        s2, _ = health_score(big, self.analysis, compute_momentum(big, []), self.cfg)
        self.assertGreater(s2, s1)

    def test_archived_scores_low(self):
        repo = make_repo(archived=True)
        score, components = health_score(repo, self.analysis, compute_momentum(repo, []), self.cfg)
        self.assertLess(components["maintenance"], 20)
        self.assertLess(score, 70)

    def test_tiers_descend(self):
        self.assertEqual(assign_tier(95, self.cfg), "flagship")
        self.assertEqual(assign_tier(65, self.cfg), "recommended")
        self.assertEqual(assign_tier(50, self.cfg), "notable")
        self.assertEqual(assign_tier(10, self.cfg), "watchlist")


class TestCoverage(unittest.TestCase):
    def test_full_coverage(self):
        a = ToolFacts("a/a", capabilities={"x", "y"})
        b = ToolFacts("b/b", capabilities={"x", "y", "z"})
        ratio, covered = coverage_ratio(a, b)
        self.assertEqual(ratio, 1.0)
        self.assertEqual(covered, ["x", "y"])

    def test_partial_coverage(self):
        a = ToolFacts("a/a", capabilities={"x", "y"})
        b = ToolFacts("b/b", capabilities={"x"})
        ratio, _ = coverage_ratio(a, b)
        self.assertAlmostEqual(ratio, 0.5)

    def test_no_capabilities_is_zero(self):
        ratio, _ = coverage_ratio(ToolFacts("a/a", capabilities=set()), ToolFacts("b/b", capabilities={"x"}))
        self.assertEqual(ratio, 0.0)


class TestSupersede(unittest.TestCase):
    def setUp(self):
        self.cfg = load_thresholds()

    def facts(self, name, caps, stars, spd, setup=30, health=80, doc=50, archived=False, category="cat"):
        return ToolFacts(
            full_name=name,
            capabilities=set(caps),
            stars=stars,
            stars_per_day=spd,
            setup_score=setup,
            health=health,
            doc_score=doc,
            archived=archived,
            pushed_at=iso(1),
            category=category,
        )

    def test_strict_superset_eliminates(self):
        incumbent = self.facts("old/tool", ["a", "b", "c", "d"], 1000, 2.0)
        challenger = self.facts("new/tool", ["a", "b", "c", "d", "e"], 5000, 20.0)
        edge = evaluate_pair(incumbent, challenger, self.cfg)
        self.assertIsNotNone(edge)
        self.assertEqual(edge.incumbent, "old/tool")
        self.assertEqual(edge.challenger, "new/tool")
        self.assertEqual(edge.coverage, 1.0)
        self.assertTrue(edge.reasons)

    def test_cross_category_never_eliminates(self):
        """Elimination is a within-category judgement.

        Without this, a broad multi-purpose tool "covers" every narrow tool in
        every category and retires most of the index.
        """
        incumbent = self.facts("old/tool", ["a", "b", "c"], 1000, 2.0, category="memory")
        challenger = self.facts("new/tool", ["a", "b", "c", "d"], 5000, 20.0, category="orchestration")
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_too_few_incumbent_capabilities_blocks(self):
        """'Covers 100% of one capability' is not evidence of replacement."""
        incumbent = self.facts("old/tool", ["a"], 1000, 2.0)
        challenger = self.facts("new/tool", ["a", "b", "c", "d", "e"], 5000, 20.0)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_suspiciously_broad_challenger_blocks(self):
        """A tool credited with ~everything is a directory or a bad parse."""
        incumbent = self.facts("old/tool", ["a", "b", "c"], 1000, 2.0)
        challenger = self.facts("new/tool", [f"cap{i}" for i in range(22)], 5000, 20.0)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_missing_capability_blocks(self):
        incumbent = self.facts("old/tool", ["a", "b", "c"], 1000, 2.0)
        challenger = self.facts("new/tool", ["a", "b"], 5000, 20.0)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_lower_stars_blocks(self):
        incumbent = self.facts("old/tool", ["a", "b", "c"], 10000, 2.0)
        challenger = self.facts("new/tool", ["a", "b", "c"], 5000, 20.0)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_stagnant_challenger_blocks(self):
        incumbent = self.facts("old/tool", ["a", "b", "c"], 1000, 50.0)
        challenger = self.facts("new/tool", ["a", "b", "c"], 5000, 1.0)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_much_harder_setup_blocks(self):
        incumbent = self.facts("old/tool", ["a", "b", "c"], 1000, 2.0, setup=10)
        challenger = self.facts("new/tool", ["a", "b", "c"], 5000, 20.0, setup=70)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_archived_challenger_blocks(self):
        incumbent = self.facts("old/tool", ["a", "b", "c"], 1000, 2.0)
        challenger = self.facts("new/tool", ["a", "b", "c"], 5000, 20.0, archived=True)
        self.assertIsNone(evaluate_pair(incumbent, challenger, self.cfg))

    def test_self_never_supersedes(self):
        facts = self.facts("a/a", ["x", "y", "z"], 1000, 5.0)
        self.assertIsNone(evaluate_pair(facts, facts, self.cfg))

    def test_magpie_eliminates_cc_switch(self):
        """The canonical example from the project's requirements."""
        cc_switch = self.facts(
            "farion1231/cc-switch",
            ["multi-account-switching", "quota-management", "model-routing", "gui-desktop"],
            stars=140685,
            spd=300.0,
            setup=25,
            health=88,
        )
        magpie = self.facts(
            "yetone/magpie",
            ["multi-account-switching", "quota-management", "model-routing", "gui-desktop", "provider-aggregation"],
            stars=5666,
            spd=400.0,
            setup=20,
            health=85,
        )
        # Automatic rules correctly refuse: magpie has fewer stars.
        self.assertIsNone(evaluate_pair(cc_switch, magpie, self.cfg))

        # The curated verdict is what records it.
        edges = apply_manual_overrides(
            [],
            {
                "supersede": [
                    {
                        "incumbent": "farion1231/cc-switch",
                        "challenger": "yetone/magpie",
                        "note": "magpie covers cc-switch's core job and routes other models too.",
                    }
                ]
            },
        )
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0].kind, "manual")
        self.assertEqual(edges[0].confidence, "high")
        self.assertEqual(edges[0].incumbent, "farion1231/cc-switch")

    def test_chain_keeps_strongest_edge(self):
        a = self.facts("a/a", ["w", "x", "y", "z"], 100, 1.0)
        b = self.facts("b/b", ["w", "x", "y", "z"], 5000, 50.0)
        c = self.facts("c/c", ["w", "x", "y", "z"], 50000, 500.0)
        edges = build_edges([a, b, c], self.cfg)
        incumbents = [e.incumbent for e in edges]
        # a is eliminated; the strongest single challenger is kept.
        self.assertIn("a/a", incumbents)
        self.assertEqual(len([e for e in edges if e.incumbent == "a/a"]), 1)

    def test_manual_beats_automatic(self):
        auto = [
            type(
                "E",
                (),
                {
                    "incumbent": "a/a",
                    "challenger": "b/b",
                    "dominance": 0.9,
                    "as_dict": lambda self: {},
                },
            )()
        ]
        edges = apply_manual_overrides(
            auto, {"supersede": [{"incumbent": "a/a", "challenger": "c/c", "note": "human call"}]}
        )
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0].challenger, "c/c")
        self.assertEqual(edges[0].kind, "manual")


class TestResolveStates(unittest.TestCase):
    def setUp(self):
        self.cfg = load_thresholds()

    def test_active_by_default(self):
        entries = {"a/a": {"pushed_at": iso(1), "archived": False}}
        states = resolve_states(entries, [], {}, self.cfg)
        self.assertEqual(states["a/a"]["state"], "active")

    def test_archived_wins(self):
        entries = {"a/a": {"pushed_at": iso(1), "archived": True}}
        states = resolve_states(entries, [], {}, self.cfg)
        self.assertEqual(states["a/a"]["state"], "archived")

    def test_dormant_when_stale(self):
        entries = {"a/a": {"pushed_at": iso(400), "archived": False}}
        states = resolve_states(entries, [], {}, self.cfg)
        self.assertEqual(states["a/a"]["state"], "dormant")

    def test_manual_state_overrides(self):
        entries = {"a/a": {"pushed_at": iso(1), "archived": False}}
        states = resolve_states(entries, [], {"states": {"a/a": {"state": "deprecated"}}}, self.cfg)
        self.assertEqual(states["a/a"]["state"], "deprecated")

    def test_supersede_edge_sets_state_and_note(self):
        from agentindex.supersede import SupersedeEdge

        edge = SupersedeEdge(
            incumbent="a/a", challenger="b/b", reasons=["covers everything"], dominance=0.9
        )
        entries = {"a/a": {"pushed_at": iso(1), "archived": False}}
        states = resolve_states(entries, [edge], {}, self.cfg)
        self.assertEqual(states["a/a"]["state"], "superseded")
        self.assertEqual(states["a/a"]["superseded_by"], "b/b")
        self.assertIn("b/b", states["a/a"]["note_en"])


if __name__ == "__main__":
    unittest.main()
