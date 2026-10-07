#!/usr/bin/env python3
"""agentindex CLI — the single entry point for the daily job and local runs.

Usage
-----
    python scripts/agentindex.py crawl            # discover, analyse, score, persist
    python scripts/agentindex.py crawl --limit 40 # bounded run (small API budget)
    python scripts/agentindex.py render           # regenerate README.md + docs/
    python scripts/agentindex.py build            # crawl + render (what CI runs)
    python scripts/agentindex.py validate         # schema + integrity checks
    python scripts/agentindex.py stats            # print a summary of data/
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from agentindex import __version__  # noqa: E402
from agentindex.github import Budget, GitHubClient  # noqa: E402
from agentindex.pipeline import INDEX_PATH, run_pipeline  # noqa: E402
from agentindex.util import DATA_DIR, LOG, read_json, setup_console, write_json  # noqa: E402


def cmd_crawl(args: argparse.Namespace) -> int:
    client = GitHubClient(
        budget=Budget(core=args.core_budget, search=args.search_budget),
        offline=args.offline,
    )
    LOG.info(
        "crawl starting (authenticated=%s, core_budget=%d, search_budget=%d)",
        client.authenticated,
        client.budget.core,
        client.budget.search,
    )
    index, stats = run_pipeline(
        client,
        limit=args.limit,
        refresh=args.refresh,
        dry_run=args.dry_run,
        allow_shrink=args.allow_shrink,
    )
    LOG.info("stats: %s", json.dumps(stats.as_dict(), ensure_ascii=False))
    if args.dry_run:
        LOG.info("dry run: nothing written")
    if any(str(e).startswith("write refused") for e in stats.errors):
        LOG.error("the index was NOT updated — see the refusal above")
        return 1
    return 0


def cmd_render(args: argparse.Namespace) -> int:
    from agentindex.render import render_all

    index = read_json(INDEX_PATH)
    if not index:
        LOG.error("no %s — run `crawl` first", INDEX_PATH)
        return 1
    written = render_all(index, check=args.check)
    for path in written:
        LOG.info("wrote %s", path.relative_to(DATA_DIR.parent))
    if args.check:
        LOG.info("check mode: no files modified")
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    rc = cmd_crawl(args)
    if rc != 0:
        return rc
    return cmd_render(args)


def cmd_validate(args: argparse.Namespace) -> int:
    from agentindex.render import validate_index

    index = read_json(INDEX_PATH)
    if not index:
        LOG.error("no index at %s", INDEX_PATH)
        return 1
    problems = validate_index(index)
    if problems:
        for problem in problems:
            LOG.error("INVALID: %s", problem)
        return 1
    LOG.info(
        "index OK: %d tools across %d categories",
        index["counts"]["tools"],
        index["counts"]["categories"],
    )
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    index = read_json(INDEX_PATH)
    if not index:
        LOG.error("no index at %s — run `crawl` first", INDEX_PATH)
        return 1

    print(f"generated_at : {index.get('generated_at')}")
    print(f"tools        : {index['counts']['tools']}")
    print(f"categories   : {index['counts']['categories']}")
    print(f"edges        : {index['counts']['supersede_edges']}")
    print(f"rejected     : {index['counts']['rejected']}")
    print()
    print(f"{'category':<24} {'tools':>5}  {'top tool':<34} {'stars':>8}")
    print("-" * 76)
    for category in index.get("categories", []):
        tools = category.get("tools", [])
        if not tools:
            continue
        top = tools[0]
        entry = index["tools"].get(top, {})
        print(
            f"{category['id']:<24} {len(tools):>5}  {top:<34} {entry.get('stars', 0):>8,}"
        )
    print()
    states: dict[str, int] = {}
    for tool in index.get("tools", {}).values():
        states[tool["state"]] = states.get(tool["state"], 0) + 1
    print("lifecycle states:", ", ".join(f"{k}={v}" for k, v in sorted(states.items())))
    return 0


def main(argv: list[str] | None = None) -> int:
    setup_console()
    parser = argparse.ArgumentParser(prog="agentindex", description=__doc__.split("\n")[0])
    parser.add_argument("--version", action="version", version=f"agentindex {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--limit", type=int, default=None, help="max candidates to process")
        p.add_argument("--refresh", action="store_true", help="ignore the on-disk cache")
        p.add_argument("--dry-run", action="store_true", help="analyse without writing data/")
        p.add_argument("--check", action="store_true", help="render without writing files")
        p.add_argument("--offline", action="store_true", help="use only cached API responses")
        p.add_argument("--core-budget", type=int, default=45, help="max core API calls")
        p.add_argument("--search-budget", type=int, default=25, help="max search API calls")
        p.add_argument(
            "--allow-shrink",
            action="store_true",
            help="write the index even if this run found far fewer tools than before",
        )

    for name, help_text, fn in (
        ("crawl", "discover, analyse and persist", cmd_crawl),
        ("render", "regenerate README.md and docs/", cmd_render),
        ("build", "crawl then render", cmd_build),
        ("validate", "check data/index.json integrity", cmd_validate),
        ("stats", "summarise data/index.json", cmd_stats),
    ):
        p = sub.add_parser(name, help=help_text)
        add_common(p)
        p.set_defaults(func=fn)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        LOG.warning("interrupted")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
