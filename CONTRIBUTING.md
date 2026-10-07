# Contributing

Thanks for helping. This repository is **generated**, so the most useful
contributions change the *inputs* — the config and the code — rather than the
output files.

> ⚠️ **Never hand-edit `README.md`, `README.zh-CN.md` or `docs/`.** They are
> rebuilt from `data/index.json` on every run and your edit will be
> overwritten. CI fails if generated files are out of sync.

---

## The three ways to contribute

### 1. Nominate a tool

Add an entry to [`config/seeds.json`](config/seeds.json):

```json
{
  "repo": "owner/repo",
  "category": "quota-account-ops",
  "why": "One sentence on the core problem it solves."
}
```

Then run the pipeline locally so the tool gets analysed:

```bash
python scripts/agentindex.py crawl --limit 40
python scripts/agentindex.py render
```

Seeding guarantees **evaluation**, not inclusion. Your nominee still has to
clear the same quality gates as everything else (see
[docs/METHODOLOGY.md](docs/METHODOLOGY.md)). If it fails a gate, the reason is
recorded in `data/index.json` under `rejected` — that is the best place to look
if you are wondering why a tool did not show up.

**Before nominating, check it passes the gates:**

| Gate | Threshold |
| --- | --- |
| Stars | ≥ 120, **or** a fast riser (≥ 60 stars projected per 14 days) |
| Recency | pushed within 180 days |
| Age | at least 14 days old |
| Documentation | doc score ≥ 22/100 |
| README | at least 900 characters |
| Archived | must not be archived |

A tool that fails the star gate but is genuinely rising is still welcome — the
rising pass in [`config/discovery.json`](config/discovery.json) exists exactly
to catch those before they are popular.

### 2. Challenge a verdict

Two kinds of verdict can be wrong, and both are fixed in
[`config/overrides.json`](config/overrides.json):

**A tool was retired unfairly.** Add a `states` entry to force a lifecycle
state, or remove/correct the `supersede` edge:

```json
{
  "states": {
    "owner/repo": {
      "state": "active",
      "note_en": "Not actually superseded: the newer tool cannot do X.",
      "note_zh": "并未真正被取代：新工具做不到 X。"
    }
  }
}
```

> **A curated `supersede` entry is a nomination, not a verdict.** The pair is
> re-checked against the same capability-coverage rule the automatic engine
> uses. If the challenger genuinely covers the incumbent it is recorded as a
> supersede and the incumbent retires; if it does not, the pair is reported as a
> **challenger** — visible in the README under "Challengers", but nothing is
> retired. That is why `magpie`/`cc-switch` is a challenger rather than an
> elimination: magpie covers ~62% of cc-switch's capabilities and has ~4% of its
> stars, so declaring the older tool replaced would contradict this project's
> own methodology.

**A capability was misdetected.** The analyser matches patterns from
[`config/capabilities.json`](config/capabilities.json) against the README body.
If a tool is credited with something it does not do (or misses something it
does), the fix is usually to tighten a pattern — add a negative context, or
require a more specific phrase. Patterns are regexes, matched
case-insensitively against the plain-text README.

### 3. Improve a Chinese description

The Chinese README describes each tool using, in priority order:

1. **The project's own Chinese README**, if it ships one — fetched from
   `README.zh-CN.md`, `README_CN.md` and similar filenames. The author's own
   words, and the best source.
2. **A `summary_zh` note in [`config/overrides.json`](config/overrides.json)** —
   add one for any tool you can describe accurately:

   ```json
   {
     "notes": {
       "owner/repo": {
         "summary_zh": "一句话说明这个工具解决什么问题。"
       }
     }
   }
   ```

3. **A summary generated from detected capabilities**, marked `‡`.
4. **The English text, kept in English**, marked `†`.

Adding a `summary_zh` is the single most useful contribution to the Chinese
index: it takes a row from tier 3 or 4 to tier 2, and it is the only tier that
adds knowledge the analyser does not already have.

The English text is **never machine-translated**. A translation would put claims
in a project's mouth that it never made, and the whole value of this list is
that its conclusions can be checked. An honest English sentence marked `†` is
more useful to a Chinese reader than a fluent fabrication.

To see what the analyser currently believes and why:

```bash
python scripts/agentindex.py stats
python - <<'PY'
import json, pathlib
entry = json.loads(pathlib.Path("data/entries/owner__repo.json").read_text(encoding="utf-8"))
print(json.dumps(entry["analysis"], indent=2, ensure_ascii=False))
PY
```

Every detected capability carries an `evidence` string — the sentence from the
README that triggered it. Quote that in your issue or PR; it makes review fast.

### 3. Improve the engine

The pipeline is standard-library Python 3.11+ with no dependencies. That is a
deliberate constraint: it keeps the daily job fast and means contributors can
run it without setting up an environment.

```
scripts/
  agentindex.py            CLI entry point
  agentindex/
    util.py                IO, text normalisation, table escaping
    github.py              cached, budget-aware GitHub REST client
    discover.py            candidate discovery + relevance judgement
    readme_analysis.py     README -> capabilities, setup friction, doc score
    highlights.py          README -> concrete feature bullets
    taxonomy.py            category DISCOVERY by clustering capabilities
    scoring.py             health score, quality gates, tiers, momentum
    supersede.py           the elimination engine and lifecycle states
    pipeline.py            orchestration and persistence
    render.py              README / docs generation
config/                    all tunable behaviour (no logic lives here)
data/                      generated state, committed on purpose
tests/                     unit tests over the analyser, taxonomy and rules
```

**Run the tests before opening a PR:**

```bash
python -m unittest discover -s tests -v
python scripts/agentindex.py validate
python scripts/agentindex.py render --check
```

---

## Categories are discovered, not declared

**There is no list of categories to edit.** No file enumerates them, and adding
one by hand is not possible — deliberately.

Each run clusters the indexed tools by how prominently their READMEs document
each capability, and the resulting groups become the sections you see. A tool
that spans several problem areas appears under each of them. See
[docs/TAXONOMY.md](docs/TAXONOMY.md) for the algorithm.

What this means for contributions:

- **To add a category, add tools that share a problem.** If several tools
  genuinely do something no current section covers, a section will appear for
  it on the next run. That is the only mechanism, and it keeps the taxonomy
  honest about what the ecosystem actually looks like.
- **To influence naming**, edit `label` / `short` / `problem` on the relevant
  capability in [`config/capabilities.json`](config/capabilities.json). Category
  titles are composed from those strings, so renaming a capability renames any
  category built on it.
- **To widen discovery**, add queries to
  [`config/queries.json`](config/queries.json). These are deliberately decoupled
  from categories: they only decide what gets *looked at*, never how it is
  grouped.
- **A category that stops being distinct disappears on its own**, and its tools
  move to whichever section now fits them best.

Tuning knobs live at the top of `scripts/agentindex/taxonomy.py`:
`DEFAULT_MERGE_THRESHOLD` (how similar two groups must be to merge),
`MIN_CLUSTER_TOOLS` (how large a section must be to exist) and
`UBIQUITY_CEILING` (how common a capability must be before it is treated as
describing the whole field rather than any category).

If you change the threshold, re-run the pipeline and **read the resulting
sections** — the values in the file were chosen by sweeping and inspecting, and
the comments record what the neighbours produce.

---

## Adding a capability

A capability is a *problem a tool solves*, not a feature name. Good:

```json
{
  "id": "auto-failover",
  "label": { "en": "Automatic failover", "zh": "自动故障转移" },
  "short": { "en": "Failover", "zh": "故障转移" },
  "problem": {
    "en": "When one account or provider dies, work should continue on the next one instead of stopping.",
    "zh": "某个账号或供应商不可用时，任务应自动切到下一个而不是中断。"
  },
  "patterns": ["auto[- ]?switch", "failover", "自动切换", "故障转移"]
}
```

Write `patterns` for both English and Chinese — many tools in this space
document only in Chinese. Include negative-context handling where it matters:
the analyser already skips a match that appears only inside "not supported" or
"planned" phrasing, but a more specific pattern is always better than relying
on that.

---

## Local development notes

**API budget.** Without a token, GitHub allows 60 core requests and 10 searches
per hour. The client caches every response in `data/cache/` (gitignored) and
enforces its own ceiling. For a comfortable local run:

```bash
export GITHUB_TOKEN=ghp_...        # PowerShell: $env:GITHUB_TOKEN="ghp_..."
python scripts/agentindex.py crawl --limit 100
```

**Useful flags:**

| Flag | Effect |
| --- | --- |
| `--limit N` | Process at most N candidates (seeds are prioritised) |
| `--dry-run` | Analyse and score without writing `data/` |
| `--offline` | Use only cached API responses — great for iterating on rendering |
| `--refresh` | Ignore the cache and re-fetch |
| `--check` | With `render`: report drift without writing |

**Iterating on rendering is free:**

```bash
python scripts/agentindex.py render --check   # what would change?
python scripts/agentindex.py render           # write it
```

No network calls, no API budget.

---

## Pull request checklist

- [ ] `python -m unittest discover -s tests -v` passes
- [ ] `python scripts/agentindex.py validate` passes
- [ ] Generated files are committed if the data changed (`render`, not hand-edits)
- [ ] Config changes are valid JSON
- [ ] New capabilities or categories include both English and Chinese text
- [ ] The PR explains **why**, with the README evidence sentence where relevant

## Code of conduct

Be decent. Disagreements about whether a tool is good are welcome and should be
argued with evidence — stars, commit recency, capability coverage, an actual
try. Personal attacks on maintainers of listed tools are not acceptable, and
issues that are really about a tool's politics rather than its engineering will
be closed.
