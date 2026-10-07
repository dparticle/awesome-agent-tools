# Architecture

A map of how a repository on GitHub becomes a row in the README, and why the
pipeline is shaped the way it is.

```
                      config/                     data/                 rendered
                 ┌──────────────┐          ┌──────────────────┐    ┌──────────────┐
                 │ categories   │          │ cache/ (ignored) │    │ README.md    │
   GitHub API ──▶│ capabilities │──┐       │ entries/*.json   │───▶│ README.zh-CN │
                 │ thresholds   │  │       │ history/*.json   │    │ docs/*.md    │
                 │ discovery    │  │       │ index.json       │    │ docs/tools/* │
                 │ seeds        │  │       │ graveyard.json   │    └──────────────┘
                 │ overrides    │  │       └──────────────────┘
                 └──────────────┘  │                 ▲
                                   ▼                 │
        discover ─▶ analyse ─▶ score ─▶ eliminate ─▶ persist ─▶ render
```

## Modules

| Module | Responsibility |
| --- | --- |
| `util.py` | UTF-8 IO, Markdown stripping, table escaping, logging |
| `github.py` | Cached, budget-aware GitHub REST client |
| `discover.py` | Candidate discovery, relevance judgement, category assignment |
| `readme_analysis.py` | README → capabilities, setup friction, doc score, list detection |
| `scoring.py` | Momentum, health score, quality gates, tiers |
| `supersede.py` | The elimination engine and lifecycle states |
| `pipeline.py` | Orchestration, persistence, index assembly |
| `render.py` | README / docs generation and validation |

## Why the pipeline is shaped this way

### The API budget drives the design

An unauthenticated GitHub token allows **60 core requests and 10 searches per
hour**. That is not enough to fetch metadata for a few hundred repos, so the
pipeline exploits a property of the search endpoint: **search results are
complete repository objects**.

Consequence: a search result is used directly as metadata, and the expensive
`/repos/{owner}/{repo}` call is reserved for seeds (which have no search
payload) and for explicit `--verify-metadata` runs. A full crawl of 400
candidates typically spends **one** core request.

READMEs are fetched from `raw.githubusercontent.com`, which is not part of the
REST rate limit at all. Everything is cached in `data/cache/` with a TTL, so a
re-run is nearly free and `--offline` works for iterating on rendering.

### Discovery must be able to find a dark horse

Sorting every query by total stars means a brand-new project can never surface —
it will always be outranked by incumbents. That would make the elimination
engine useless, because it would have nothing to promote.

`config/discovery.json` therefore defines a **rising pass**: additional queries
for recently created repos with meaningful traction
(`agent created:>2026-05-10 stars:>40`). Rising candidates carry no category and
compete for one on the strength of their README.

### The README is the source of truth

A GitHub `description` is a marketing sentence. Everything the index claims —
what a tool solves, how hard it is to run, whether a non-programmer can use it —
is derived from the README body, and each conclusion keeps the sentence that
triggered it as evidence.

Two failure modes had to be handled explicitly:

1. **Curated lists.** An `awesome-*` repo matches every capability keyword
   because it *describes* hundreds of tools. Left unchecked, these dominated
   the index and "superseded" real tools. `assess_list` combines name patterns,
   directory framing, and link density to exclude them.
2. **Over-broad patterns.** Early capability patterns matched bare words
   (`provider`, `memory`, `proxy`), which credited tools with 20+ of 25
   capabilities and made the elimination engine retire 147 of 255 tools. The
   patterns are now phrase-level, negation-aware, and scored per clause.

### Elimination is a within-category judgement

The requirement is "a tool that covers everything the tools *in this category*
do". Comparing across categories looks reasonable and is catastrophically
wrong: a 16-capability tool covers a 2-capability tool 100% of the time, in
every category. `evaluate_pair` therefore refuses cross-category edges, plus
guards for suspiciously broad capability sets, too-small incumbents, and
documentation regressions.

See [SUPERSEDE.md](SUPERSEDE.md) for the full rule set.

### Generated output is never hand-edited

`data/index.json` is the single source for every rendered file. CI runs
`render --check` and fails if the committed output drifts, so the README cannot
silently diverge from the data.

Per-tool entry files exist so that a daily run touches only the tools whose
numbers actually moved, which keeps `git log` readable. Orphaned entry files and
tool pages are pruned automatically, so a rename does not leave a stale page
that still looks authoritative.

## Data model

```
data/entries/<owner>__<repo>.json     one tool, full record (the source of truth)
data/history/<owner>__<repo>.json     daily star snapshots -> real momentum
data/index.json                       aggregate: categories, tools, edges, rejects
data/graveyard.json                   retired tools + the edges that retired them
```

`data/index.json` is keyed by **lower-cased** full name throughout — `tools{}`,
`categories[].tools[]` and `supersede[].incumbent` all agree. Display case lives
in `tools[key].full_name` and `supersede[].*_name`. This was a real bug source:
mixed casing silently dropped supersede edges and produced dangling references.

## Running it

```bash
python scripts/agentindex.py crawl          # discover, analyse, score, persist
python scripts/agentindex.py render         # regenerate README + docs
python scripts/agentindex.py build          # both (what CI runs)
python scripts/agentindex.py validate       # integrity checks
python scripts/agentindex.py stats          # summary table
python -m unittest discover -s tests -v     # 79 unit tests
```

No third-party dependencies — standard library only, Python 3.11+.
