<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Methodology

This list is generated, not curated by hand. Understanding the rules is enough to predict exactly what will and will not appear.

## 1. Discovery

Every day the crawler runs the queries in [`config/categories.json`](../config/categories.json), plus a **rising pass** that asks GitHub for recently created repositories with traction. The rising pass is what lets a dark horse be discovered before it has more stars than the incumbents.

Hand-picked entries in [`config/seeds.json`](../config/seeds.json) are always evaluated. Seeding guarantees evaluation, not inclusion.

## 2. Quality gates

A candidate must clear every gate to be listed:

| Gate | Threshold |
| --- | --- |
| Stars | ≥ 120 — *or* a fast riser (≥ 60 stars projected per 14 days) |
| Recency | pushed within 180 days |
| Age | at least 14 days old |
| Documentation | doc score ≥ 22/100 |
| README | at least 900 characters |
| Archived | excluded |

## 3. README analysis

The GitHub `description` field is a tagline, so nothing here relies on it. The crawler downloads the README and derives:

- **Capabilities** — which of the catalogue's problems this tool addresses.
- **Setup difficulty** — matched install and configuration signals, scored 0 (turnkey) to 100 (heavy).
- **Out of the box** — installable without a source build or a server stack.
- **Non-programmer friendly** — a GUI or an explicit no-code path, and no server to run.
- **Documentation score** — structural signals (quick start, config docs, FAQ, screenshots, code blocks…).

Negation is handled: a capability mentioned only inside "not supported" or "planned" phrasing is not credited.

## 4. Health score

| Component | Weight | What it measures |
| --- | ---: | --- |
| `popularity` | 28% | log-scaled stars — other people already found the bugs |
| `momentum` | 24% | observed stars/day, saturated at the 99th percentile |
| `maintenance` | 20% | recency of the last push, with hard penalties for abandonment |
| `documentation` | 16% | README documentation score |
| `accessibility` | 12% | inverse of setup friction, bonused for turnkey and non-dev friendly |

Tiers:

| Tier | Minimum score |
| --- | ---: |
| 🏆 Flagship | 78 |
| ✅ Recommended | 62 |
| 🔹 Notable | 45 |
| 👀 Watchlist | 0 |

## 5. Momentum measurement

Momentum is measured from `data/history/<tool>.json`, a rolling star snapshot taken once per day. On the very first run there is no history, so the crawler falls back to lifetime stars/day — a good proxy for young repos and a conservative one for old repos. From the second run onward, growth is **observed**, not inferred.

## 6. Category discovery

Categories are **not declared anywhere**. Each run clusters the indexed tools by how prominently their READMEs document each capability, and the clusters become the sections. See [TAXONOMY.md](TAXONOMY.md) for the algorithm and why the obvious approaches fail on this data.

A tool may belong to several categories at once, because tools genuinely span problem areas. It is described in full only under its primary category.

## 7. Elimination

See [SUPERSEDE.md](SUPERSEDE.md) for the full rule set.

## Reproducing

```bash
python scripts/agentindex.py build     # crawl + render
python scripts/agentindex.py validate  # check data/index.json
python scripts/agentindex.py stats     # summarise
```

No third-party dependencies — the pipeline runs on a bare Python 3.11+ interpreter, which is also why the GitHub Actions workflow needs no install step.
