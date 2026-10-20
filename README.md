<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools

> **Building an "AGI" out of the tools we already have.** No single agent is enough — one hits its quota, one cannot be reached from your phone, one forgets your project. This is the curated, continuously-verified map of the tools that patch those gaps, and of which ones have been overtaken.

**[中文说明](README.zh-CN.md)** · [Methodology](docs/METHODOLOGY.md) · [Elimination rules](docs/SUPERSEDE.md) · [Capability taxonomy](docs/TAXONOMY.md) · [Machine-readable index](data/index.json)

[![Tools](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdparticle%2Fawesome-agent-tools%2Fmain%2Fdata%2Findex.json&query=%24.counts.tools&label=tools&color=blue)](data/index.json)
[![Categories](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdparticle%2Fawesome-agent-tools%2Fmain%2Fdata%2Findex.json&query=%24.counts.categories&label=categories&color=informational)](data/index.json)
[![Retired](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdparticle%2Fawesome-agent-tools%2Fmain%2Fdata%2Findex.json&query=%24.counts.retired&label=retired&color=critical)](data/graveyard.json)
[![Daily crawl](https://img.shields.io/badge/crawl-daily%20via%20GitHub%20Actions-2ea44f?logo=githubactions&logoColor=white)](.github/workflows/daily.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**218 tools** across **16 categories** · **55 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-20 09:29 UTC**

---

## How to read this list

Every entry was scored from its **README**, not its tagline. The columns mean something specific:

| Column | Meaning |
| --- | --- |
| **Setup** | 🟢 turnkey (installer or one-liner) · 🟡 needs config or a dependency · 🔴 expects you to build/self-host a stack |
| **OOTB** | Works after install with no source build, no server and at most trivial configuration. |
| **Non-dev** | A GUI or an explicit no-code story, and no server stack to run. ✅ means a non-programmer has a realistic path in. |
| **Stars** | Total stars, with observed stars/day where we have history. 🚀 marks a fast riser. |
| **Score** | 0-100 health score: popularity, momentum, maintenance, docs and accessibility. See [METHODOLOGY](docs/METHODOLOGY.md). |

**Tiers:** 🏆 Flagship · ✅ Recommended · 🔹 Notable · 👀 Watchlist

---

## Contents

- [Parallelism & Isolation](#parallelism-isolation) — 32 tools
- [Self-hosting & Security](#self-hosting-security) — 27 tools
- [Desktop UI](#desktop-ui) — 36 tools
- [Sharing](#sharing) — 15 tools
- [Security](#security) — 13 tools
- [Mobile & Remote Control](#mobile-remote-control) — 11 tools
- [Providers](#providers) — 13 tools
- [Desktop UI](#desktop-ui) — 12 tools
- [Model Routing](#model-routing) — 12 tools
- [Billing](#billing) — 11 tools
- [Mobile](#mobile) — 8 tools
- [Providers](#providers) — 8 tools
- [Voice & Remote Control](#voice-remote-control) — 6 tools
- [Sessions](#sessions) — 6 tools
- [Analytics](#analytics) — 5 tools
- [Sharing](#sharing) — 3 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Parallelism & Isolation

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. | 🟡 Some setup | — | — | 137k 🚀 +110/d | **88** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 10.4k 🚀 +190/d | **87** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Website: aimemory.sh | 🟡 Some setup | — | — | 11.7k 🚀 +469/d | **84** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 12.6k 🚀 +120/d | **83** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 84.2k 🚀 +59/d | **77** |
| ✅ **[edenfunf/reelmimic](https://github.com/edenfunf/reelmimic)** | It takes a while. A 30–60 second video usually takes 1–3.5 hours after you approve the plan, depending on the Three languages. 繁體中文, English and 简体中文, switch in the top right. | 🟡 Some setup | — | ✅ | 3.7k 🚀 +73/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.7k 🚀 +22/d | **72** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.5k 🚀 +16/d | **69** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.3k 🚀 +32/d | **66** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.3k 🚀 +17/d | **66** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 8.1k 🚀 +31/d | **65** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. | 🟢 Turnkey · OOTB | ✅ | — | 3.4k 🚀 +13/d | **65** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.6k 🚀 +9/d | **62** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 3.8k 🚀 +39/d | **61** |
| 🔹 **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. | 🟢 Turnkey | — | ✅ | 2.1k | **61** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k (+20/d) | **58** |
| 🔹 **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 한국어 \| 中文 \| Português \| 日本語 \| Français \| Español \| Nederlands \| Polski \| Русский \| Deutsch \| Tiếng Việt \| ภาษาไทย | 🟢 Easy | — | — | 1.3k | **57** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. | 🟡 Some setup | — | — | 1.1k 🚀 +8/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 563 🚀 +4/d | **57** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.5k 🚀 +7/d | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 577 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 312 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 417 | **54** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | The structured skill framework for Claude Code: 131 professional skills for deployment, security, databases, content, marketing, and more. | 🟢 Easy | — | — | 425 | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 789 | **52** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **51** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟡 Some setup | — | — | 434 | **49** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [stablyai/orca](https://github.com/stablyai/orca), [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design), [felinics/Memoh](https://github.com/felinics/Memoh), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j), [crshdn/mission-control](https://github.com/crshdn/mission-control), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

*…and 2 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> When I heard Karpathy say this, I wanted to find out how.

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *use and re-verify before committing.*
- **Parallel execution** — *t patterns depending on whether it's a landing page, dashboard, form, or card layout.*
- **Workspace isolation** — *hand, and gstack-uninstall*
- **Model / provider routing** — *deterministic aside repl scripts.*
- **Session persistence** — *Browse my kid's school parent portal and add all the other parents' names, phone numbers, and photos to my Google Contacts." Two ways to get authenti…*
- **Memory & context** — *Come work at YC — ycombinator.com/software*
- **Skills & plugins** — *single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup** then add a "gstack"…*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Some setup. install via native installer / package; needs git clone (build from source), go build; configure config file, config.json/yaml/toml; one-click setup

**Facts**

- Stars: **137,014** (+110.4/day over 5d)
- Health score: **88/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [TencentCloud/Octop](https://github.com/TencentCloud/Octop)

> Octop is an open-source, self-hosted AI assistant.

**Core problems it solves**

- **Mobile access** — *Linux alongside the web dashboard and IM channels.*
- **Multi-agent orchestration** — *A smarter, self-hosted AI assistant — multi-user, multi-agent.*
- **Parallel execution**
- **Workspace isolation** — *PyPI Any pip install octop (optional extras such as local-embedding)*
- **Model / provider routing** — *ild / quality** hatchling · ruff · mypy · pytest*
- **API gateway / proxy** — *ays back up first (octop backup) before a cross-version upgrade.*
- **Billing & metering** — *hina mirror: docker/docker-compose.cn.yml*
- **Memory & context** — *e notes, and manage your schedule; memory persists with the workspace.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs docker run, make build; configure config.json/yaml/toml, OAuth login flow; one-click setup

**Facts**

- Stars: **10,388** (+189.6/day over 5d)
- Health score: **87/100**
- Documentation score: **78/100**
- License: MIT
- Language: Python
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode

#### [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

> Website: aimemory.sh

**Core problems it solves**

- **Workspace isolation** — *box/queue plus the on-start "you have mail" notice.*
- **Model / provider routing** — *s session summaries and enables semantic search.*
- **API gateway / proxy** — *s session summaries and enables semantic search.*
- **Memory & context** — *> Long-term memory for AI coding agents.*
- **Skills & plugins**
- **Agent runtime** — *> Long-term memory for AI coding agents.*
- **MCP support** — *--features management-ui and start serve --transport http*
- **Security & isolation**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 46/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://github.com/akitaonrails/ai-memory/releases/latest/download/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via curl | sh installer, PowerShell irm | iex installer; needs docker run, git clone (build from source); configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **11,667** (+469.2/day over 5d)
- Health score: **84/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)

> English | 中文 | 日本語 | Русский

**Core problems it solves**

- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add Vincentwei1021/video-shotcraft`
- Platforms mentioned: macOS, Linux, Web
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **12,594** (+119.6/day over 5d)
- Health score: **83/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-17
- Works with: Claude Code, Codex

#### [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

> English | 中文 | 日本語 | Français | Русский | Português | 한국어

**Core problems it solves**

- **Automatic failover** — *d X-Forwarded-Proto: https) or localhost HTTP.*
- **Multi-agent orchestration** — *llion to our incredible community — you made this happen! 💪🔥*
- **Parallel execution** — *x plus Docker is the recommended deployment target for a persistent server.*
- **Workspace isolation** — *ame matches the payload's type field.*
- **Model / provider routing** — *urn a format error instead of exposing the raw provider payload.*
- **API gateway / proxy** — *es pass through request admission again.*
- **Usage analytics** — *and cloud-metadata hostname detection is case-insensitive.*
- **Session persistence** — *, and publish a new app version.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @minimax-ai/code`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **84,186** (+59.2/day over 5d)
- Health score: **77/100**
- Documentation score: **80/100**
- License: MIT
- Language: Python
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Cursor, Droid

</details>

## Self-hosting & Security

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 284.4k 🚀 +922/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 19.8k 🚀 +247/d | **88** |
| 🏆 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.5k 🚀 +162/d | **82** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Local-first search engine and MCP server for AI agents. XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 10.8k 🚀 +96/d | **81** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 10.1k 🚀 +76/d | **76** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 14.6k 🚀 +71/d | **74** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 32.6k 🚀 +49/d | **73** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 29.7k 🚀 +44/d | **73** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 8.2k 🚀 +62/d | **68** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.7k 🚀 +9/d | **67** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.3k | **61** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **61** |
| 🔹 **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | ╔═════════════════════════════════════════════════════════════════════════════╗ ║ MARKETING NOTES FOR IMAGE ASSETS ║ ║ All images below live under .github/assets/. | 🟡 Some setup | — | — | 2.2k 🚀 +6/d | **60** |
| 🔹 **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。 | 🟡 Some setup | — | — | 12.7k 🚀 +24/d | **58** |
| 🔹 **[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)** | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. | 🟢 Turnkey · OOTB | ✅ | — | 2.6k 🚀 +13/d | **58** |
| 🔹 **[graygnatconsole/mcp-audit-tool](https://github.com/graygnatconsole/mcp-audit-tool)** | Scan your AI agent configs for tool poisoning, rug pulls, hardcoded secrets, command injection, and supply-chain risks — before the model runs something you regret. | 🟢 Easy | — | — | 493 🚀 +21/d | **57** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.1k 🚀 +6/d | **56** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.7k | **56** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 416 | **54** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 490 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 677 | **50** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 414 | **45** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 247 | **45** |
| 👀 **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | An MCP server that lets your coding agent build and query a graph of concepts, architecture, and decisions — so it remembers across sessions. | 🟢 Easy | — | — | 727 | **43** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 545 | **40** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [superdesigndev/treg](https://github.com/superdesigndev/treg), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent) *(+13 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [affaan-m/ECC](https://github.com/affaan-m/ECC)

> Use the guided setup or native plugin commands.

**Core problems it solves**

- **Automatic failover**
- **Multi-agent orchestration** — *s and evidence live under docs/releases/.*
- **Parallel execution**
- **Workspace isolation**
- **Model / provider routing** — *shims such as /tdd and /eval live in legacy-command-shims/ for explicit opt-in only.*
- **API gateway / proxy** — *eway remaps model names, configure that in Claude Code rather than in ECC.*
- **Session persistence**
- **Memory & context** — *r debugging, before continuing feature work*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx ecc-universal@2.2.3 setup`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, bunx one-liner; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **284,378** (+922.4/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [lexmount/moli](https://github.com/lexmount/moli)

> media="(prefers-color-scheme: dark)" srcset="assets/moli-browser-banner-dark.jpg" media="(prefers-color-scheme: light)" srcset="assets/moli-browser-banner.jpg" src="assets/moli-browser-banner.jpg" alt="Moli Browser — Structure first.

**Core problems it solves**

- **MCP support** — *dpoint serves all three protocols: CDP, WebDriver Classic, and*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 6/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `curl --proto '=https' --tlsv1.2 -fsSL \`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via PowerShell irm | iex installer, native installer / package; configure sign-in required; GUI application

**Facts**

- Stars: **19,779** (+247.2/day over 5d)
- Health score: **88/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-20

#### [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)

> An agent that closes its session forgets everything it learned in it.

**Core problems it solves**

- **Workspace isolation**
- **Model / provider routing** — *etup and mem doctor report configuration and live-preflight results separately as Write*
- **API gateway / proxy** — *etup and mem doctor report configuration and live-preflight results separately as Write*
- **Memory & context** — *### agent-memory: the long-term memory runtime for AI agents*
- **MCP support** — *Existing files with status load without a reset.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 43/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via native installer / package; needs git clone (build from source); configure API key configuration, database dependency

**Facts**

- Stars: **4,516** (+161.6/day over 5d)
- Health score: **82/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-20
- Works with: Claude Code, Codex

#### [xerj-org/xerj](https://github.com/xerj-org/xerj)

> Local-first search engine and MCP server for AI agents.

**Core problems it solves**

- **Memory & context** — *f the same primitive: xerj autoindex makes an agent*
- **Agent runtime** — *rity audit of WordPress core,*
- **MCP support** — *. XERJ answers under its own name, xerj-history-vote-1;*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://xerj.org/get | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source), cargo build; configure API key configuration, config file

**Facts**

- Stars: **10,803** (~96.5/day lifetime average)
- Health score: **81/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-20
- Works with: Claude Code, Cursor

#### [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)

> Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats.

**Core problems it solves**

- **Parallel execution**
- **Model / provider routing** — *spark and skip keys, or bring your own*
- **API gateway / proxy** — *spark and skip keys, or bring your own*
- **Billing & metering** — *export as PDF or a native editable Word document.*
- **Usage analytics** — *ub Copilot, OpenCode and Windsurf*
- **Memory & context** — *he top hits leave the device; the index itself never does.*
- **Skills & plugins** — *l, OpenRouter, Requesty, Opper, Cheaper Inference, Atlas Cloud, or any OpenAI-compatible endpoint, local*
- **Agent runtime** — *etails and requirements in Download.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 20/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -T report.docx -H "Authorization: Bearer $GENOFFICE_MCP_TOKEN" http://server:3093/files/`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **10,098** (+75.8/day over 5d)
- Health score: **76/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 152.8k 🚀 +379/d | **90** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | ✅ | 168.5k 🚀 +919/d | **88** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Taste Skill is an Agent Skill that makes coding agents design websites and app screens instead of assembling the average landing page. | 🟢 Easy | — | — | 99.6k 🚀 +554/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 17.2k 🚀 +1114/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 32.9k 🚀 +645/d | **81** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 4.3k 🚀 +114/d | **74** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 27.2k 🚀 +34/d | **70** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.9k 🚀 +18/d | **68** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 4.9k 🚀 +55/d | **67** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 3.7k 🚀 +52/d | **65** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.7k | **59** |
| 🔹 **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 11.1k 🚀 +4/d | **58** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 870 | **58** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.1k 🚀 +14/d | **57** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.7k | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 539 | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 504 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 342 | **53** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | An open skill for agent-to-agent contracts. | 🟢 Easy | — | — | 6.8k | **52** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **52** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CR… | 🟡 Some setup | — | — | 373 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.4k 🚀 +8/d | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 Easy | — | — | 1.1k | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 901 | **51** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 303 | **51** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [garrytan/gstack](https://github.com/garrytan/gstack), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design), [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd), [maxritter/pilot-shell](https://github.com/maxritter/pilot-shell) *(+18 more)*

*…and 6 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [anthropics/claude-code](https://github.com/anthropics/claude-code)

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Core problems it solves**

- **Skills & plugins**
- **Agent runtime** — *Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, e…*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://claude.ai/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via Homebrew install, winget install; needs npm install/build

**Facts**

- Stars: **152,849** (+379.0/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-19
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

#### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

> You know him.

**Core problems it solves**

- **Skills & plugins** — *, a parser, money or security leaves one small test behind.*
- **GUI / desktop app** — *-audit, copy the task as Markdown, and fold the band into one line.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Easy** (friction 35/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: Web
- Easy. configure config file, config.json/yaml/toml; GUI application

**Facts**

- Stars: **168,506** (+919.4/day over 5d)
- Health score: **88/100**
- Documentation score: **48/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-18
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

> Taste Skill is an Agent Skill that makes coding agents design websites and app screens instead of assembling the average landing page.

**Core problems it solves**

- **Skills & plugins**
- **Agent runtime** — *t components for creative interfaces*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"`
- Platforms mentioned: Web
- Easy. install via npx one-liner; configure API key configuration, server/reverse-proxy setup

**Facts**

- Stars: **99,588** (+553.6/day over 5d)
- Health score: **86/100**
- Documentation score: **33/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-19
- Works with: Claude Code, Codex

#### [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)

> Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept.

**Core problems it solves**

- **Skills & plugins** — *ill folders, so that SKILL.md ends up at /anatomy/SKILL.md.*
- **Cross-agent support** — *Mentions Claude Code, Codex, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add wheresryan22/anatomy -g`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner; needs git clone (build from source), npm install/build; configure config.json/yaml/toml

**Facts**

- Stars: **17,186** (+1114.0/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-18
- Works with: Claude Code, Codex, OpenCode

#### [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

> A coding-agent skill that turns your agent into a security auditor.

**Core problems it solves**

- **Multi-agent orchestration** — *d Setup, core principles, platform terminology, workflow overview, and audit anti-patterns*
- **Skills & plugins**
- **Agent runtime** — *directory defaults to ~/security-audit-skill/ /run- .*
- **GUI / desktop app** — *tor-spend hunting classes*
- **Notifications** — *LOUD-AND-DEPLOYMENT.md IAM, infrastructure-as-code, container, serverless, ingress, and runtime-configuration hunting classes*

**Getting it running**

- Setup: 🟢 **Easy** (friction 22/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add https://github.com/cloudflare/security-audit-skill \`
- Platforms mentioned: Linux, Web
- Easy. install via npx one-liner; configure database migration

**Facts**

- Stars: **32,925** (+644.8/day over 5d)
- Health score: **81/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

</details>

## Sharing

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 130k 🚀 +143/d | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 17.6k 🚀 +887/d | **88** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 31.1k 🚀 +57/d | **71** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 31 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 17.7k 🚀 +46/d | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… Grok CLI 凭据不加密：access token/… | 🟢 Easy | — | — | 19.1k 🚀 +27/d | **67** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 9.7k 🚀 +35/d | **66** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.5k 🚀 +16/d | **56** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 554 | **54** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 470 🚀 +12/d | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 250 | **52** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 900 | **51** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.7k 🚀 +9/d | **50** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 297 | **50** |
| 👀 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | Built with C++ / Win32 / WebView2 for stability and speed. Quota dashboard, auto-refresh (5H / 7D), low-quota alerts and switch prompts | 🟡 Some setup | — | — | 250 | **41** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [cita-777/metapi](https://github.com/cita-777/metapi), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [openai/codex](https://github.com/openai/codex)

> If you want Codex in your code editor (VS Code, Cursor, Windsurf), install in your IDE.

**Core problems it solves**

- **Multi-account switching** — *inux-musl), so you likely want to rename it to codex after extracting it.*
- **Automatic failover** — *the following on Mac or Linux to install Codex CLI:*
- **Agent runtime** — *Codex CLI is a coding agent from OpenAI that runs locally on your computer.*
- **GUI / desktop app** — *Codex CLI is a coding agent from OpenAI that runs locally on your computer.*
- **Cross-agent support** — *Mentions Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 12/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via Homebrew install, curl | sh installer; needs npm install/build; configure API key configuration, sign-in required; GUI application

**Facts**

- Stars: **130,027** (+142.6/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-20
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *one key that matters in the agent's own config.*
- **Multi-agent orchestration** — ***Sync** Back up to a file, or sync machines over WebDAV (Nutstore, Nextcloud…), S3, or an encrypted GitHub repository backup*
- **Model / provider routing** — *&nbsp;·&nbsp; Plugins &nbsp;·&nbsp; Discord &nbsp;·&nbsp; English · 简体中文*
- **API gateway / proxy** — *t Cloud · Huawei Cloud MaaS · Volcengine Ark · Mistral · Groq · Nous Portal · xAI · OpenRouter · Together · Fireworks · SiliconFlow · NVIDIA NIM · Mo…*
- **MCP support** — *ers it as a provider to every other agent.*
- **GUI / desktop app** — *f you use more than one agent, more than one provider, or more than one account.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://usemagpie.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via go install, curl | sh installer; configure API key configuration, config file; one-click setup

**Facts**

- Stars: **17,595** (+886.8/day over 5d)
- Health score: **88/100**
- Documentation score: **61/100**
- License: MIT
- Language: Go
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

#### [decolua/9router](https://github.com/decolua/9router)

> Never stop coding.

**Core problems it solves**

- **Multi-account switching** — *uto-compress toolresult content, save 20-40% tokens per request*
- **Quota & usage management** — *Enable in Dashboard → Endpoint → Ponytail.*
- **Remote control**
- **Model / provider routing** — *> Mind the /v1 on embeddings.*
- **API gateway / proxy** — *repository package is private (9router-app), so source/Docker execution is the expected local development path.*
- **Billing & metering** — *tiers were discontinued in 2026*
- **Usage analytics** — *for compatibility/UI, but server runtime now prioritizes BASEURL/CLOUDURL.*
- **Self-hostable** — *openedai-speech, llama.cpp/llama-server,*

**Getting it running**

- Setup: 🔴 **Involved** (friction 73/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g 9router`
- Platforms mentioned: Windows, Linux, Web
- Involved setup. install via global npm install; needs docker run, git clone (build from source); configure environment variables, API key configuration

**Facts**

- Stars: **31,114** (+56.8/day over 5d)
- Health score: **71/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)

> Two commands, and every one of them runs any LLM you point it at.

**Core problems it solves**

- **Multi-account switching** — *tokens, images, in both directions.*
- **Automatic failover**
- **Multi-agent orchestration** — *### Claude Desktop, running any model Opus answers, then hands the task to a GPT-5.6 Sol subagent. ### Grok Build, running any model Sol drives the s…*
- **Model / provider routing** — *vision sidecars** — non-OpenAI models get real web search and image understanding*
- **API gateway / proxy** — *ystem One-compatible server.*
- **Self-hostable** — *e first currently eligible target; caller*
- **GUI / desktop app** — *t:10100 and configure everything in the web dashboard — add providers*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 42/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g @bitkyc08/opencodex`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via global npm install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow; GUI application

**Facts**

- Stars: **17,658** (+45.6/day over 5d)
- Health score: **69/100**
- Documentation score: **54/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

> English · Portuguese (BR) · 简体中文

**Core problems it solves**

- **Multi-account switching** — *surf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Quota & usage management** — *目前支持 Antigravity IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，…*
- **Automatic failover** — *aude CLI 与 Claude Desktop Gateway 第三方供应商预设、模型映射，以及从会话 JSONL 汇总真实用量的方向参考：CC Switch*
- **Multi-agent orchestration**
- **Parallel execution** — *ty IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Model / provider routing** — *emini、Ollama 兼容接口，两引擎共用账号池、代理和配置。*
- **Multi-provider aggregation** — *어 · 🇧🇷 Português · 🇷🇺 Русский · 🇹🇷 Türkçe · 🇵🇱 Polski · 🇨🇿 Čeština · 🇸🇦 العربية · 🇻🇳 Tiếng Việt · 🇮🇩 Bahasa Indonesia*
- **API gateway / proxy** — *权绑定状态；有效绑定始终高亮，不受是否加入 API 服务影响，服务成员状态单独显示。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **19,136** (+26.8/day over 5d)
- Health score: **67/100**
- Documentation score: **60/100**
- Language: Rust
- Last push: 2026-10-19
- Works with: Codex, OpenCode, Cursor, Copilot

</details>

## Security

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 5.9k 🚀 +111/d | **84** |
| 🏆 **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟡 Some setup | — | — | 5.3k 🚀 +85/d | **78** |
| ✅ **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k 🚀 +85/d | **74** |
| ✅ **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. Routines: ask a Bot to do something on a schedule and it does, running as y… | 🟡 Some setup | — | — | 6.7k 🚀 +39/d | **67** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 15.1k 🚀 +12/d | **64** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 782 | **55** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 308 | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 339 | **52** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 10-13 「本机/内网放行」支持通配符：192.168.1.: 放一整个网段，*.local:8080 放一类主机名 10-12 本机 Codex / Claude Code 读得到随消息传的文件了：粘贴的文字、图和文档都附上完整路径，不再只收到文件名 | 🟡 Some setup | — | ✅ | 336 | **52** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 542 | **50** |
| 🔹 **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | An advanced Distributed Automation Platform for high-concurrency account registration and full-lifecycle inventory management. | 🟡 Some setup | — | — | 1.4k | **49** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew brings task execution, human approvals, persistent memory, and scheduled work into one desktop application. | 🟡 Some setup | — | ✅ | 252 | **47** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [slopus/happy](https://github.com/slopus/happy), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [automazeio/ccpm](https://github.com/automazeio/ccpm), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [yc-software/qm](https://github.com/yc-software/qm), [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [cordum-io/cordum](https://github.com/cordum-io/cordum), [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) *(+3 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [superdesigndev/treg](https://github.com/superdesigndev/treg)

> OpenRouter, but for agent tools instead of models.

**Core problems it solves**

- **Automatic failover** — *secrets won't survive a restart)*
- **Model / provider routing** — *# Treg (OpenRouter for Tools)*
- **Billing & metering** — *e code to third parties as a competing hosted/managed registry service without written*
- **Skills & plugins** — *agent through the rest — the CLI, sign-in, then treg mcp install — so you end up with*
- **MCP support** — *install it as a Claude Code plugin*
- **Security & isolation** — *resolves the tool by host, injects the credential, and relays everything else faithfully*
- **Self-hostable** — *need to know which vendor sells backlink data, or to*
- **Notifications** — *lace a secret into a header/query*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://treg.to/install.sh | sh`
- Platforms mentioned: Linux, Web
- Easy. install via npx one-liner, pip install; configure environment variables, API key configuration; one-click setup

**Facts**

- Stars: **5,862** (+110.6/day over 5d)
- Health score: **84/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-20
- Works with: Claude Code

#### [aipoch/open-science](https://github.com/aipoch/open-science)

> AI research workbench for reproducible science — open-source, local-first, and model-agnostic.

**Core problems it solves**

- **Remote control** — *e host to stay on and online, with AIPOCH Open-Science and the Remote.It agent running, and the host added to a signed-in Remote.It account.*
- **Model / provider routing** — *overview - Node.js quick start and package entry point*
- **Billing & metering** — *### Why does the model connection test fail? A: Check the API Key for missing characters or spaces, verify the Base URL and region, use the provider'…*
- **Skills & plugins** — *s to the skill, not to the availability of every registered host.*
- **MCP support** — *Marketplace contributions are published after review; local imports do not publish skills.*
- **Security & isolation** — *untime owns each data directory.*
- **GUI / desktop app** — *ith a screening model configured, smart collections evaluate references against your inclusion/exclusion criteria; AI decisions remain separate from…*
- **Cross-agent support** — *Mentions Claude Code, Codex, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 41/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install --cask open-science`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow; one-click setup

**Facts**

- Stars: **5,303** (+85.2/day over 5d)
- Health score: **78/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode

#### [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)

> AOS gives AI agents a shared local environment for tools, permissions and services.

**Core problems it solves**

- **MCP support** — *les with explicit permissions and an audit trail.*
- **Security & isolation** — *e the access it needs, and give it capabilities you can*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 22/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl --proto '=https' --tlsv1.2 -fsSL https://aos.unicity.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via native installer / package; configure database migration

**Facts**

- Stars: **8,460** (~85.5/day lifetime average)
- Health score: **74/100**
- Documentation score: **28/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-20
- Works with: Claude Code, Codex

#### [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)

> The AI assistant your company can actually own.

**Core problems it solves**

- **Automatic failover** — *somewhere else: a gateway, a proxy.*
- **Model / provider routing** — *verything is on 3001 here, the app included, rather than the 3010 the clone uses.*
- **Session persistence**
- **MCP support** — *ack into themes it can cite.*
- **Security & isolation** — *who gets in**: /admin/people lists everybody who has signed in, promotes and demotes them, and removes access, which ends the session they are using…*
- **Self-hostable** — *Defaults to ../examples/fintech.*
- **Notifications**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx --yes copilotkit@latest login`
- Platforms mentioned: macOS, Linux, Web
- Some setup. install via npx one-liner; needs docker run; configure sign-in required, database dependency

**Facts**

- Stars: **6,696** (+39.2/day over 5d)
- Health score: **67/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19

#### [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)

> cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动态 Workflow 编排、模型请求追踪、Computer Use、技能市场、多主题、桌面宠物、H5 远程访问、IM 接入和定时任务，集中在一…

**Core problems it solves**

- **Automatic failover** — *图片生成：聊天中直接生成和编辑图片——ChatGPT / Grok 授权登录即可使用，也支持接入任意 OpenAI 兼容的 Images API。*
- **Remote control** — *de Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动…*
- **Multi-agent orchestration** — *GitHub Pull Requests License 中文 English Docs 简体中文 · English cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Cla…*
- **Workspace isolation** — *cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、…*
- **Billing & metering** — *GPT、Claude、Gemini、Grok 等主流模型和常用兼容协议，还支持 40 多种图片和视频模型。*
- **Usage analytics** — *：满血稳定不掺水，低成本享受全球 SOTA 模型。*
- **Session persistence** — */ Agent 定制需求，请联系作者 NanmiCoder。*
- **Memory & context** — *端功能 功能总览 · Computer Use · 桌面宠物 · 手机 H5 与 IM 接力*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Easy. configure API key configuration; GUI application

**Facts**

- Stars: **15,081** (+12.2/day over 5d)
- Health score: **64/100**
- Documentation score: **57/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code

</details>

## Mobile & Remote Control

*Remote control*

Your agent runs on a desktop, but you want to drive it from somewhere else.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 98.9k 🚀 +1196/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 105k 🚀 +521/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 21.5k 🚀 +111/d | **85** |
| 🏆 **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | Local & private. The proxy binds to 127.0.0.1 and sends no telemetry. Authorization, API keys, cookies, and secret-looking body fields are redacted before anything hits disk. Everything sta… Capture. Claude Code uses re… | 🟢 Turnkey | — | — | 6k 🚀 +199/d | **83** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8k 🚀 +36/d | **68** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 10.9k 🚀 +19/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.2k 🚀 +16/d | **64** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 2.8k 🚀 +9/d | **60** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **51** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 320 | **47** |

**Also does this:** [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design), [spinabot/brigade](https://github.com/spinabot/brigade), [Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent), [yetone/cumora](https://github.com/yetone/cumora), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [stablyai/orca](https://github.com/stablyai/orca)

> Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place.

**Core problems it solves**

- **Multi-account switching** — *ree create, snapshot, click, and fill.*
- **Quota & usage management**
- **Remote control** — *Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place.*
- **Mobile access** — *The AI Orchestrator for 100x builders.*
- **Multi-agent orchestration**
- **Parallel execution** — *### Mobile Companion Monitor and steer your agents from your phone — get notified when an agent finishes and send follow-ups from anywhere. iOS App S…*
- **Workspace isolation** — *when an agent finishes and send follow-ups from anywhere.*
- **Usage analytics**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `brew install --cask stablyai/orca/orca`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via Homebrew install, native installer / package; GUI application

**Facts**

- Stars: **98,851** (+1196.2/day over 5d)
- Health score: **92/100**
- Documentation score: **51/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

#### [paperclipai/paperclip](https://github.com/paperclipai/paperclip)

> Open-source orchestration for teams of AI agents.

**Core problems it solves**

- **Remote control**
- **Mobile access**
- **Multi-agent orchestration** — *people use to manage AI agents for work.*
- **Workspace isolation** — *ounded recovery handles supported failures and surfaces cases that need human action.*
- **Model / provider routing**
- **Usage analytics** — *hard-stops, and agent pause/resume/terminate.*
- **Session persistence**
- **Memory & context**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 45/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx paperclipai@latest onboard --yes`
- Platforms mentioned: Linux, Web
- Some setup. install via npx one-liner; needs git clone (build from source), pnpm install/build; configure environment variables, config file; GUI application

**Facts**

- Stars: **104,956** (+520.8/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [getpaseo/paseo](https://github.com/getpaseo/paseo)

> Paseo is an open source agentic development environment for desktop, mobile, web, and CLI.

**Core problems it solves**

- **Remote control**
- **Mobile access** — *emon machine and inside connected clients; install only code you trust.*
- **Multi-agent orchestration** — *once, each in its own worktree, on one machine or several.*
- **Parallel execution** — *Paseo is an open source agentic development environment for desktop, mobile, web, and CLI.*
- **Workspace isolation** — *nt environment for desktop, mobile, web, and CLI.*
- **Agent runtime** — *, composer pills, attachment sources, timeline items, themes.*
- **MCP support** — *: screens, sidebar items, workspace panels, Command Center items, slash commands, composer pills, attachment sources, timeline items, themes.*
- **Security & isolation** — *en Settings → your host → Pair Device.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npm install -g @getpaseo/cli`
- Platforms mentioned: iOS, Android, Web
- Easy. install via npx one-liner, global npm install; needs docker run, npm install/build; configure environment variables; GUI application

**Facts**

- Stars: **21,495** (+111.2/day over 5d)
- Health score: **85/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

#### [tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)

> Most usage tools read local logs.

**Core problems it solves**

- **Remote control** — *l and run claude / codex exactly as before — capture is automatic, no flags and no base-URL change.*
- **Agent runtime** — *ent · project · session, with token and dollar totals*
- **MCP support** — *but why it cost that much.*
- **GUI / desktop app** — *ound service (auto-start on boot, self-healing, port-adaptive) and doesn't change what your agent does, its results, or its cost — pause anytime with…*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 12/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/tigerless-labs/cost-xray/master/install.sh | bash`
- Platforms mentioned: macOS, Linux
- Turnkey. install via curl | sh installer, native installer / package; configure server/reverse-proxy setup, process manager; GUI application

**Facts**

- Stars: **6,041** (+199.0/day over 5d)
- Health score: **83/100**
- Documentation score: **48/100**
- License: MIT
- Language: Python
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Cursor

#### [zai-org/ZCode](https://github.com/zai-org/ZCode)

> ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。

**Core problems it solves**

- **Remote control**
- **Model / provider routing**
- **Session persistence**
- **Agent runtime**
- **Self-hostable**
- **GUI / desktop app** — *pnpm --filter @zcode/cli...*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via native installer / package; needs pnpm install/build; configure OAuth login flow; GUI application

**Facts**

- Stars: **8,023** (+36.4/day over 5d)
- Health score: **68/100**
- Documentation score: **44/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-20

</details>

## Providers

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 146.6k 🚀 +416/d | **93** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.5k 🚀 +16/d | **67** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 5.1k 🚀 +57/d | **66** |
| ✅ **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.4k 🚀 +13/d | **62** |
| 🔹 **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi is a fast, self-contained terminal AI coding agent. | 🟢 Easy | — | — | 3.3k | **56** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.8k | **54** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 446 | **53** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 285 | **53** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.7k 🚀 +16/d | **51** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 432 | **51** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 Easy | — | — | 368 | **47** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 315 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 520 | **43** |

**Also does this:** [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [cita-777/metapi](https://github.com/cita-777/metapi), [schmitech/orbit](https://github.com/schmitech/orbit), [isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [farion1231/cc-switch](https://github.com/farion1231/cc-switch)

> Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files.

**Core problems it solves**

- **Multi-account switching** — *For Codex, you can also sign in to multiple ChatGPT accounts inside CC Switch via "Sign in with ChatGPT" and choose an "Account to use" for each Open…*
- **Automatic failover** — *ools and Claude Desktop, so nothing you had configured is lost.*
- **Parallel execution**
- **Model / provider routing** — *- **Third-party providers for Claude Desktop** — Connect directly to Anthropic-compatible endpoints; for non-Claude models, choose "Model Mapping" to…*
- **Multi-provider aggregation**
- **API gateway / proxy** — *config file is written back to this direct provider's configuration.*
- **Billing & metering** — *ch turn did, which files changed, and which step failed, all at a glance*
- **Usage analytics** — *can also be enabled or disabled all at once per tool; providers, MCP servers, and prompts are edited full-page in the content area, and you're warned…*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install --cask cc-switch`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; configure environment variables, config file; one-click setup

**Facts**

- Stars: **146,625** (+415.6/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

#### [xai-org/grok-build](https://github.com/xai-org/grok-build)

> SpaceXAI's coding agent harness and TUI.

**Core problems it solves**

- **Automatic failover**
- **Agent runtime**
- **MCP support** — *ementations (terminal, file edit, search, ...)*
- **Cross-agent support** — *Mentions Codex, OpenCode*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://x.ai/cli/install.sh | bash   # macOS / Linux / Git Bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via cargo install, curl | sh installer; needs cargo build

**Facts**

- Stars: **27,462** (+15.8/day over 5d)
- Health score: **67/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

#### [totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)

> Work on the real project.

**Core problems it solves**

- **Automatic failover** — *r, chats and the browser connection wait, and the app says so.*
- **MCP support** — *tion that the provider blocked for safety.*
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via native installer / package; configure API key configuration, sign-in required

**Facts**

- Stars: **5,052** (+56.8/day over 5d)
- Health score: **66/100**
- Documentation score: **33/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Codex

#### [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)

> 🌐 English | 日本語 | 中文 | 한국어

**Core problems it solves**

- **Automatic failover** — *r goals (the ShardMind wizard does this for you).*
- **Multi-agent orchestration** — */scripts/ and the commands in .claude/commands/ are agent-agnostic — pure Markdown, TypeScript, and shell with no SDK dependencies.*
- **Memory & context**
- **Skills & plugins** — *A custom skill in .claude/skills/qmd/ that teaches the agent to use QMD semantic search proactively — before reading files, before creating notes (to…*
- **Agent runtime** — *erything still works — the agent falls back to grep and the Obsidian CLI, and the MCP server entry is skipped with a harmless warning.*
- **MCP support** — *en the conversation touches a listed topic.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 58/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g shardmind`
- Platforms mentioned: Windows, Linux, iOS, Web
- Some setup. install via global npm install; needs git clone (build from source), npm install/build; configure config.json/yaml/toml, database dependency

**Facts**

- Stars: **5,392** (+13.2/day over 5d)
- Health score: **62/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-17
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Copilot

#### [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)

> FuXi is a fast, self-contained terminal AI coding agent.

**Core problems it solves**

- **Automatic failover**
- **Model / provider routing** — *ad, set an API key via environment variable or*
- **Agent runtime**
- **MCP support** — *Full details: Privacy Policy · Security Whitepaper · Terms of Service. ## Documentation Guide What it covers --- --- Usage guide First session, permi…*
- **Security & isolation** — *ands: /model switch models · /help browse all commands ·*

**Getting it running**

- Setup: 🟢 **Easy** (friction 31/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://downloads.fuxicode.com/bootstrap.sh | bash`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; configure environment variables, API key configuration

**Facts**

- Stars: **3,342** (+0.0/day over 5d)
- Health score: **56/100**
- Documentation score: **63/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-09-29

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 218.3k 🚀 +921/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 7.7k 🚀 +644/d | **87** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 9.3k 🚀 +63/d | **72** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.1k 🚀 +14/d | **64** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.7k 🚀 +13/d | **62** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 468 | **56** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). orcarouter: OpenAI-compatible model gateway with namespaced model IDs. | 🔴 Involved | — | — | 1.8k 🚀 +5/d | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 755 | **54** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | Scope Recall v3 is a bounded local memory core with SQLite as the authority and rebuildable vector companions. | 🟢 Easy | — | — | 424 🚀 +17/d | **54** |
| 🔹 **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | Bring your AI conversations, project files, terminals, and live previews together. | 🟢 Easy | — | ✅ | 275 | **54** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. The domain model is Genesys-lineage. | 🟡 Some setup | — | — | 318 🚀 +5/d | **49** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [nexu-io/open-design](https://github.com/nexu-io/open-design), [openai/codex](https://github.com/openai/codex), [yetone/magpie](https://github.com/yetone/magpie), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [getpaseo/paseo](https://github.com/getpaseo/paseo), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [xerj-org/xerj](https://github.com/xerj-org/xerj), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [aipoch/open-science](https://github.com/aipoch/open-science) *(+47 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [anomalyco/opencode](https://github.com/anomalyco/opencode)

> curl -fsSL https://opencode.ai/v2/install | bash

**Core problems it solves**

- **Multi-agent orchestration** — *alysis and code exploration*
- **Agent runtime** — *The open source AI coding agent.*
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://opencode.ai/v2/install | bash`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via Homebrew install, curl | sh installer; GUI application

**Facts**

- Stars: **218,257** (+920.8/day over 5d)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

#### [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)

> Sketch, constrain, and build solids with a parametric feature timeline.

**Core problems it solves**

- **MCP support** — *constrain, and build solids with a parametric feature timeline.*
- **GUI / desktop app** — *rded with the demo script.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via winget install, native installer / package; GUI application

**Facts**

- Stars: **7,734** (~644.5/day lifetime average)
- Health score: **87/100**
- Documentation score: **55/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-20
- Works with: Claude Code

#### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

> BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into.

**Core problems it solves**

- **Skills & plugins**
- **GUI / desktop app** — *the last update attempt; update-state.json in the bsk home keeps its stage, result and error.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs pnpm install/build, cargo build; configure sign-in required, database migration

**Facts**

- Stars: **9,251** (+63.4/day over 5d)
- Health score: **72/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Cursor

#### [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)

> One image, one mood.

**Core problems it solves**

- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 2/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Web
- Turnkey. install via native installer / package; one-click setup

**Facts**

- Stars: **15,088** (+14.0/day over 5d)
- Health score: **64/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

#### [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)

> English · 简体中文 · 日本語

**Core problems it solves**

- **Agent runtime** — *tallation, configuration, reference material, guides, and the security model.*
- **GUI / desktop app** — *ks secret access to SSH keys, .env files, ~/.aws, and coding-CLI credentials, from the shell and from the agent's file tools.*
- **Cross-agent support** — *Mentions Amp, Claude Code, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `npx -y cc-safety-net@latest install`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via npx one-liner; configure config file; GUI application

**Facts**

- Stars: **1,697** (+12.8/day over 5d)
- Health score: **62/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | — | 75.7k 🚀 +196/d | **89** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 51 film styles, each with a short film made entirely in code. Default output 1920×1080, 24 fps; other sizes on request. | 🟡 Some setup | — | ✅ | 4.1k 🚀 +178/d | **80** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 10.5k 🚀 +86/d | **75** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 10.4k 🚀 +57/d | **69** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.3k 🚀 +23/d | **64** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.1k 🚀 +7/d | **58** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.6k 🚀 +5/d | **56** |
| 🔹 **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | DeepSeek Harness, OpenClaw, Hermes, Claude Code, Codex, Cursor, WorkBuddy, OpenCode, Pi...they all work! | 🟡 Some setup | — | — | 2.1k | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 342 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 712 | **50** |
| 🔹 **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | A multi-provider gateway for Claude Code and other coding agents. Claude tier routing: Fable / Opus / Sonnet / Haiku | 🟢 Easy | — | — | 624 | **49** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 466 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch), [zai-org/ZCode](https://github.com/zai-org/ZCode), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes), [future-agi/future-agi](https://github.com/future-agi/future-agi), [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) *(+2 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)

> So I built the filter I&nbsp;needed.

**Core problems it solves**

- **Model / provider routing** — *s the same in longer words.*
- **API gateway / proxy** — *s the same in longer words.*
- **Skills & plugins** — *does not duplicate the full project instructions when it reads both AGENTS.md and GEMINI.md.*
- **GUI / desktop app** — *n terminal dashboard lets you browse your pipeline visually:*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx @santifer/career-ops init`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, config file

**Facts**

- Stars: **75,734** (+195.8/day over 5d)
- Health score: **89/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

> 51 film styles, each with a short film made entirely in code.

**Core problems it solves**

- **Model / provider routing**
- **Agent runtime**
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 44/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows
- Some setup. needs git clone (build from source); GUI application

**Facts**

- Stars: **4,085** (~177.6/day lifetime average)
- Health score: **80/100**
- Documentation score: **53/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-19
- Works with: Claude Code, Cursor

#### [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)

> Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it.

**Core problems it solves**

- **Workspace isolation**
- **Model / provider routing** — *compatible endpoint, anthropic for the native API, or litellm / orcarouter for a gateway that speaks the OpenAI-compatible format), your GRAFTAPIKEY,…*
- **API gateway / proxy** — *The graft map is vendor-neutral: set GRAFTPROVIDER (openai for any OpenAI-compatible endpoint, anthropic for the native API, or litellm / orcarouter…*
- **Billing & metering**
- **Skills & plugins** — *a marker-fenced Trail-code section in their shared instruction file (AGENTS.md for Codex, OpenCode and other CLIs that read it, GEMINI.md, .github/co…*
- **Agent runtime** — *### The self-learning context layer for coding agents.*
- **MCP support** — *ooks add the matching files and functions to each prompt, and show what depends on a file right after your agent edits it (the "blast radius").*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 58/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g @trailhq/trail-code && trail init`
- Platforms mentioned: Linux
- Some setup. install via global npm install; needs git clone (build from source), npm install/build; configure API key configuration, config.json/yaml/toml

**Facts**

- Stars: **10,472** (+85.8/day over 5d)
- Health score: **75/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)

> gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。

**Core problems it solves**

- **Model / provider routing** — *pt-6.1-sol-v1-rc2；被替换的 Astra v1 与 6.1 rc1 已归档到 historical-versions/。*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux
- Some setup. install via pip install; needs git clone (build from source), pip install -r requirements; configure config.json/yaml/toml

**Facts**

- Stars: **10,418** (+57.4/day over 5d)
- Health score: **69/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

#### [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)

> OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own.

**Core problems it solves**

- **Automatic failover**
- **Remote control** — *ongs to multiple workspaces without an active selection, search returns workspacerequired and the agent asks which workspace to use.*
- **Model / provider routing** — *MPATIBLEUSERESPONSESAPI=true is also set, the effort is sent through the Responses API reasoning field.*
- **API gateway / proxy** — *mail, and plan in ~/.openwiki/.env.*
- **Session persistence** — *yourself, for example from CI so a run's thread can be found from the commit that triggered it.*
- **Agent runtime** — *ur code, your agents, and you.*
- **MCP support** — *· Explore · Standalone CLI · Command reference*
- **Self-hostable**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 55/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g openwiki`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via global npm install; needs npm install/build; configure environment variables, API key configuration

**Facts**

- Stars: **17,291** (+23.0/day over 5d)
- Health score: **64/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 58.7k 🚀 +626/d | **90** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 44.4k 🚀 +69/d | **75** |
| ✅ **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 107.5k 🚀 +17/d | **70** |
| 🔹 **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k 🚀 +5/d | **61** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | ✅ | 377 🚀 +24/d | **57** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.5k 🚀 +43/d | **56** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 805 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 406 | **50** |
| 🔹 **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | The system of record for fintech wallets, payouts, marketplaces and billing — with spending limits that keep AI agents in check and an audit trail you can prove. | 🟡 Some setup | — | — | 414 | **49** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 432 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [decolua/9router](https://github.com/decolua/9router), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [erickochen/purple](https://github.com/erickochen/purple), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [Licoy/Quosparr](https://github.com/Licoy/Quosparr), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

> An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand.

**Core problems it solves**

- **Parallel execution** — *board a brand once, save the result as a named profile, then add a .diagram-design marker containing profile: to each client project.*
- **Billing & metering** — *atter covers bubble and beeswarm; Treemap covers marimekko.*
- **Skills & plugins** — *skills/diagram-design/SKILL.md, and installs the whole skill (references/, assets/, scripts/) into every host root you select, including Cursor's:*
- **Team collaboration**
- **Cross-agent support** — *Mentions Amp, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add cathrynlavery/diagram-design`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs git clone (build from source); configure OAuth login flow, database dependency; beginner-friendly

**Facts**

- Stars: **58,708** (+625.8/day over 5d)
- Health score: **90/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)

> AI API Gateway Platform for Subscription Quota Distribution

**Core problems it solves**

- **Multi-account switching** — *RS) with Codex CLI, add the following to the http block in your Nginx configuration:*
- **Automatic failover**
- **Multi-agent orchestration** — *targets and bridged to xAI HTTP/SSE Responses upstream*
- **Model / provider routing** — *.ai/v1 default are redirected to the subscription proxy at runtime.*
- **API gateway / proxy**
- **Billing & metering** — *tform designed to distribute and manage API quotas from AI product subscriptions.*
- **Usage analytics**
- **Security & isolation**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Some setup. install via curl | sh installer, global npm install; needs docker compose up, git clone (build from source); configure environment variables, API key configuration; one-click setup

**Facts**

- Stars: **44,426** (+69.0/day over 5d)
- Health score: **75/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

> Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal.

**Core problems it solves**

- **Model / provider routing** — *ist License from your organization, remember to set the Google Cloud Project*
- **Billing & metering**
- **Usage analytics**
- **Session persistence**
- **Skills & plugins**
- **MCP support** — *contributions! Gemini CLI is fully open source (Apache 2.0), and we*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx @google/gemini-cli`
- Platforms mentioned: macOS, Linux, Web
- Easy. install via npx one-liner, Homebrew install; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **107,463** (+16.8/day over 5d)
- Health score: **70/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Gemini CLI
- *Why it is seeded: Gemini's terminal agent, generous free tier.*

#### [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)

> Linear Chain-of-Thought anchors on whatever it says first.

**Core problems it solves**

- **Multi-agent orchestration** — *vs 6, novelty 8 vs 3, trap detection ~8 vs ~2.*
- **Billing & metering** — *ndpoints at 30s; daemonize the CLI with ticket IDs; race 3 LLM replicas, cache the winner.*
- **Skills & plugins** — *# ADHD — a skill for agents*
- **Agent runtime** — *zy debugging, naming, API surface design, strategy, and any prompt of the shape *"give me a few ways to…".*
- **Team collaboration** — *Open to collaboration with research labs and applied-AI teams working on reasoning, planning, and agentic systems.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `npx skills add UditAkhourii/adhd`
- Platforms mentioned: Linux
- Turnkey. install via npx one-liner, global npm install; needs npm install/build; one-click setup

**Facts**

- Stars: **4,442** (+4.8/day over 5d)
- Health score: **61/100**
- Documentation score: **58/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Cline / Roo

#### [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

> 简体中文 · English · 版本下载 · 问题反馈

**Core problems it solves**

- **Multi-account switching** — *Desktop 可在客户端内登录，也可选择 API / 第三方连接进入原生 Code / Cowork。*
- **Workspace isolation**
- **Multi-provider aggregation**
- **API gateway / proxy** — *e CLI 实例可使用管理器刷新后的订阅访问凭据；刷新令牌留在管理器安全存储，不写入实例。*
- **Billing & metering** — *CLI 实例时，自动补齐本机 ~/.codex/skills 中的个人技能入口，已有实例和会话副本同样适用。*
- **Agent runtime**
- **MCP support** — *ock / Vertex / Foundry 等云模式和 npm 包装启动器尚未接入。*
- **Team collaboration** — *oundry 等云模式和 npm 包装启动器尚未接入。*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 39/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npx electron-builder --mac --arm64 --publish never`
- Platforms mentioned: macOS, Windows, Linux
- Some setup. install via npx one-liner; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow; GUI application

**Facts**

- Stars: **377** (~23.6/day lifetime average)
- Health score: **57/100**
- Documentation score: **57/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 13.1k 🚀 +276/d | **82** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.4k 🚀 +7/d | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.5k 🚀 +20/d | **58** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 284 | **55** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4k | **54** |
| 🔹 **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 一个适配 Claude Code / Codex 等 Agent 环境的图文卡片技能,用于从文章、文案、截图、产品笔记、字幕、照片或用户视频生成小红书 / Rednote 图文组图、Live Photo 动态卡与公众号 21:9 + 1:1 封面对。 | 🟢 Easy | — | — | 7.6k 🚀 +13/d | **53** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Official agent skills/plugins for Power Platform development by Microsoft. Launch GitHub Copilot CLI or Claude Code with the plugin path: | 🟡 Some setup | — | — | 1k | **51** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 2.9k 🚀 +6/d | **49** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [loopx-project/loopx](https://github.com/loopx-project/loopx), [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [google/artemis](https://github.com/google/artemis)

> Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions.

**Core problems it solves**

- **Automatic failover**
- **Mobile access** — *standard Python library into existing automated testing frameworks (e.g., pytest) or CI/CD pipelines with strongly typed Pydantic structured outputs…*
- **Multi-agent orchestration** — *or notes, no pre-execution safety net, no checkpoint verification or final report, and no ADB shell.*
- **MCP support** — *Let AI assistants and test suites use real phones like a human.*
- **Notifications**
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 56/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Some setup. needs git clone (build from source); configure config.json/yaml/toml, sign-in required; one-click setup

**Facts**

- Stars: **13,112** (+275.8/day over 5d)
- Health score: **82/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)

> Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent.

**Core problems it solves**

- **Mobile access**
- **Skills & plugins** — *Recommended — the skills CLI.*
- **Agent runtime**
- **Self-hostable** — *r Mac App prompt was used in Cursor, Codex, Claude, and Claude Design.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add JimLiu/baoyu-design`
- Platforms mentioned: macOS, Linux, Web
- Turnkey. install via npx one-liner, native installer / package; needs npm install/build

**Facts**

- Stars: **4,422** (+7.2/day over 5d)
- Health score: **62/100**
- Documentation score: **61/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-23
- Works with: Claude Code, Codex, Cursor, Copilot, Cline / Roo

#### [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)

> A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。

**Core problems it solves**

- **Mobile access**
- **Memory & context**
- **Notifications**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 39/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install`
- Some setup. needs npm install/build

**Facts**

- Stars: **3,540** (+19.8/day over 5d)
- Health score: **58/100**
- Documentation score: **42/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19

#### [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)

> 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。

**Core problems it solves**

- **Quota & usage management** — *ion.mp3、.srt、.narrated.mp4、.final.mp4*
- **Automatic failover** — *KEY 是 DashScope API 密钥，用于翻译和 Wan 2.7 生图*
- **Mobile access** — *参考链**：主视觉文生图定调，后续每张图都以它作图生图参考，人物、地理、服饰、色彩与镜头语言整套锁死*
- **Multi-agent orchestration** — *播 = 一个动画场景，底部字幕逐词卡拉OK高亮——声音念到哪，画面切到哪*
- **Model / provider routing**
- **Multi-provider aggregation**
- **API gateway / proxy** — ***核心功能：** - ✅ **文学分镜**：按空间/时间/人物/动作/修辞/情绪转折拆 5–8 个视觉段落，不是机械地每两句配一张图 - ✅ **统一视觉圣经 + 参考链**：主视觉文生图定调，后续每张图都以它作图生图参考，人物、地理、服饰、色彩与镜头语言整套锁死 - ✅ **双服务商四档位**…*
- **Billing & metering** — *高风险 诱导分享/关注 "白嫖"、"薅羊毛"、"速转"、"分享给朋友"等*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 44/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via pip install; needs git clone (build from source), npm install/build; configure API key configuration, .env file; Chinese: beginner/one-click framing

**Facts**

- Stars: **284** (+0.0/day over 5d)
- Health score: **55/100**
- Documentation score: **91/100**
- Language: HTML
- Last push: 2026-10-16
- Works with: Claude Code, Codex, Cursor, Cline / Roo, Droid

#### [yetone/cumora](https://github.com/yetone/cumora)

> cumora.ai · Web app · Desktop download · iOS beta (TestFlight)

**Core problems it solves**

- **Mobile access** — *all-brain triage gate that shields the big model.*
- **Multi-agent orchestration**
- **Model / provider routing**
- **API gateway / proxy** — *DELSUPPORT big-brain / support-brain models*
- **Self-hostable** — *tale reply is HELD and shown the newer messages to re-decide), atomic claims on real units of work, and a small-brain triage gate that shields the bi…*
- **Team collaboration** — *n compatibility adapters, as an agent's brain.*
- **GUI / desktop app** — *Then open http://localhost:5180 (PWA mode) or run npm run electron:dev for the desktop window. Database migrations are applied via npm run migrate (r…*
- **Notifications**

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, iOS, Android, Web
- Easy. install via npx one-liner; configure OAuth login flow, sign-in required; GUI application

**Facts**

- Stars: **4,000** (+2.4/day over 5d)
- Health score: **54/100**
- Documentation score: **34/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Qwen Code

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 3.9k 🚀 +48/d | **72** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.3k 🚀 +10/d | **56** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 986 | **55** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁移。 工作台完整保留：任务看板、Git、文件交付、模型协作、桌宠、15 套皮肤、SSH 与远程访问继续提供；恢复 4.4.0 品牌图标。 | 🟢 Turnkey · OOTB | ✅ | — | 848 🚀 +7/d | **55** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 749 🚀 +5/d | **55** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 436 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 511 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 592 | **45** |

**Also does this:** [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [automazeio/ccpm](https://github.com/automazeio/ccpm), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)

> An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔…

**Core problems it solves**

- **Quota & usage management** — *平台适配的成品直接到对应平台，再通过**归因**分析表现并把有效经验沉淀回账号画像。*
- **Model / provider routing**
- **Multi-provider aggregation**
- **API gateway / proxy** — *API 不提供向量模型，请单独配置 Embedding API；否则 OpenClaw 会默认请求 text-embedding-3-small，可能得到“模型不可用”。*
- **Memory & context**
- **Skills & plugins** — *布与归因** 发布质量门禁、敏感与版权风险检查、平台搜索优化、发布 Checklist、多平台格式适配；小红书、抖音、快手、知乎、B 站、微信视频号、微信公众号登录与发布；内容日历回写、账号数据、评论洞察、内容复盘、ROI 与画像记忆*
- **GUI / desktop app** — *后安装器会创建项目内 .venv，安装 Python/Node 依赖、前端生产包和 Playwright Chromium，并使用独立的 easel OpenClaw profile。*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, native installer / package; needs git clone (build from source); configure API key configuration; Chinese: beginner/one-click framing

**Facts**

- Stars: **3,884** (+47.8/day over 5d)
- Health score: **72/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-20
- Works with: Claude Code, Codex

#### [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)

> Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具

**Core problems it solves**

- **Multi-agent orchestration**
- **Model / provider routing**
- **Multi-provider aggregation** — *导入前先预览现有 MCP Server，再决定哪些需要纳管；启用或禁用后由 Codex-X 自动维护 Codex 配置。*
- **Usage analytics** — *可视化查看 Skills 与 MCP，导入已有配置，从 ZIP 安装 Skill，逐项启用 / 禁用，并检查更新状态。*
- **MCP support** — *Codex 桌面端 / Codex CLI 的跨平台桌面工具。*
- **Team collaboration**
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Android, Web
- Easy. install via native installer / package; needs pnpm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **4,262** (+9.8/day over 5d)
- Health score: **56/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-20
- Works with: Codex

#### [routatic/proxy](https://github.com/routatic/proxy)

> route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation.

**Core problems it solves**

- **Automatic failover** — *Routing** — Configurable routing for streaming requests (see CONFIGURATION.md)*
- **Model / provider routing** — *enCode Go, OpenCode Zen, AWS Bedrock, or OpenRouter from a single config*
- **Multi-provider aggregation** — *ng Claude/GPT/Gemini access without multiple API keys*
- **GUI / desktop app** — *ch config file for changes and reload automatically*
- **Cross-agent support** — *Mentions Claude Code, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap routatic/tap && brew install routatic-proxy`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install; configure environment variables, config file; GUI application

**Facts**

- Stars: **986** (+0.0/day over 5d)
- Health score: **55/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-18
- Works with: Claude Code, OpenCode

#### [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)

> Open-source Windows desktop client and GUI for DeepSeek Harness — zero-setup installer with Codex, plugins, skills, SSH, mobile remote access, and 11 skins.

**Core problems it solves**

- **Automatic failover**
- **Remote control** — *### 任务看板与自动化 内置任务看板，可以管理： 待规划 → 待办 → 进行中 → 已完成 / 已失败 任务可以交给真实 DSH Agent Session 执行，并记录 Task Run 与 Evidence，方便查看结果和继续处理。*
- **Mobile access**
- **Multi-agent orchestration** — *插件稳定性继续加固：启动阶段可见、事务修复可回滚、第三方插件错误隔离，原有 DSH Home 与插件直接延续。*
- **Workspace isolation** — *g 或 .zip 后把应用放到 /Applications，用 xattr 去掉隔离属性；macOS 15 起没有「右键打开」。*
- **Model / provider routing** — *载安装 EXE 后即可启动完整 Harness 环境。*
- **Multi-provider aggregation** — *pSeek Harness Desktop 5.0.0 Windows bai 模型接入*
- **Billing & metering** — *L、域名、窗口名称、截图、Prompt、工具参数、路径或凭据，详见 隐私政策。*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via native installer / package; configure OAuth login flow; Chinese: beginner/one-click framing

**Facts**

- Stars: **848** (+6.8/day over 5d)
- Health score: **55/100**
- Documentation score: **43/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex

#### [erickochen/purple](https://github.com/erickochen/purple)

> purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman containers fleet-wide.

**Core problems it solves**

- **Multi-account switching** — *oment they boot, IPs follow instances as they move and decommissioned hosts gray out instead of lingering.*
- **Multi-provider aggregation** — *ommand on ten hosts? Write a loop or boot up Ansible for a one-liner.*
- **MCP support** — *Everything else you do over SSH lives in the same terminal: fuzzy search across hundreds of hosts, visual file transfer, multi-host SSH key push, sho…*
- **Security & isolation**
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL getpurple.sh | sh`
- Platforms mentioned: macOS, Linux, Web
- Easy. install via Homebrew install, cargo install; needs git clone (build from source), cargo build; configure sign-in required, API token/secret; one-click setup

**Facts**

- Stars: **749** (+4.8/day over 5d)
- Health score: **55/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-19
- Works with: Claude Code, Cursor

</details>

## Voice & Remote Control

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 161.9k 🚀 +352/d | **98** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 5.6k 🚀 +73/d | **75** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 5.2k 🚀 +67/d | **74** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 8.9k 🚀 +32/d | **69** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.7k 🚀 +7/d | **64** |
| 🔹 **[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)** | An open-source desktop AI agent workspace for work, design, and coding. Unified tool store for local MCP servers, remote MCP servers, CLI tools, and API connectors | 🔴 Involved | — | — | 2.6k 🚀 +20/d | **58** |

**Also does this:** [getpaseo/paseo](https://github.com/getpaseo/paseo), [slopus/happy](https://github.com/slopus/happy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

> Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities.

**Core problems it solves**

- **Multi-account switching** — *ll social strategy, multi-platform campaigns*
- **Automatic failover** — *atform Engineer API gateways & platforms Gateway design, versioning, rate limiting, developer portals*
- **Mobile access** — *rn web apps, pixel-perfect UIs, Core Web Vitals optimization*
- **Multi-agent orchestration** — *h agent becomes a skill in ~/.gemini/config/skills/agency- /.*
- **Parallel execution** — *plete example where 8 agents (Product Trend Researcher, Backend Architect, Brand Guardian, Growth Hacker, Support Responder, UX Researcher, Project S…*
- **API gateway / proxy** — *allocation, rightsizing, unit economics, budget & anomaly control*
- **Billing & metering** — *efronts Catalog, payments, checkout, orders on Drupal 10/11*
- **Memory & context**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 1/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install --cask msitarzewski/agency-agents/agency-agents`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Turnkey. install via Homebrew install, download a release binary; configure OAuth login flow, database dependency; no-code positioning

**Facts**

- Stars: **161,942** (+352.4/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)

> A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions.

**Core problems it solves**

- **Automatic failover** — *e permission requests show up with Allow / Deny / Always; AskUserQuestion prompts show the choices right in the notch (single or multi-select, up to…*
- **Remote control** — *hooting and build-it-yourself: docs/IPHONE.md.*
- **Mobile access** — *ries, no hook files, no recap history.*
- **Model / provider routing** — *open the exact terminal window of a session (macOS).*
- **Agent runtime**
- **Security & isolation** — *See what Claude is editing, live in the notch: each file modification shows the file name and +N −M counts in the ticker, tap to read the full diff*
- **GUI / desktop app** — *Coucou on the iPhone, allow notifications, and start a Claude Code session on the Mac.*
- **Notifications** — *your iPhone's Lock Screen and Dynamic Island with the agent's state, then comes back to the notch when you unlock.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap louis-cfm/coucou https://github.com/Louis-CFM/coucou`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, database dependency; one-click setup

**Facts**

- Stars: **5,614** (+72.6/day over 5d)
- Health score: **75/100**
- Documentation score: **67/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

> The open-source Grok Bot alternative: your own team of AI bots, in a chat app.

**Core problems it solves**

- **Mobile access** — *protected by pairing, an existing*
- **Multi-agent orchestration** — *n/ macOS, Windows, and Ubuntu shells with an embedded harness and platform capabilities; Apple speech stays macOS-only, Ubuntu Xorg has opt-in local…*
- **Model / provider routing** — *rs can add their own MCP tool servers with zero code via docs/custom-mcp-servers.md.*
- **API gateway / proxy** — *g — see docs/custom-engines.md.*
- **Usage analytics** — *s with zero code via docs/custom-mcp-servers.md.*
- **Skills & plugins** — *skills switched off and routines paused.*
- **MCP support** — *ure bots/channels/tasks, send work, wait for completion, switch models, and interrupt turns.*
- **Security & isolation** — *ks before a potentially billable test message.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g openmausbot`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via npx one-liner, global npm install; needs git clone (build from source), pnpm install/build; configure API key configuration, OAuth login flow; explicitly no coding required

**Facts**

- Stars: **5,232** (+67.4/day over 5d)
- Health score: **74/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Codex, Cursor, Cline / Roo

#### [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)

> Free, open source and performant.

**Core problems it solves**

- **Multi-agent orchestration** — *ts own node-pty PTY, rendered with xterm.js.*
- **Parallel execution** — *A GOD orchestrator you talk to.*
- **Workspace isolation** — *d avatar state reflects real work.*
- **Model / provider routing** — *led right, and you can add your own.*
- **Usage analytics** — *hareable hires and the Agent Gallery, observability and the circuit*
- **Session persistence** — *a built-in Monaco IDE with git rails, integrations registry + secret broker,*
- **Memory & context** — *al-agent CLIs as fully-capable agents,*
- **Skills & plugins** — *The floor - Every terminal is a real agent.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install        # postinstall rebuilds node-pty against Electron's ABI`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via native installer / package; needs git clone (build from source), npm install/build; configure sign-in required, database dependency; one-click setup

**Facts**

- Stars: **8,929** (+32.0/day over 5d)
- Health score: **69/100**
- Documentation score: **74/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)

> MiMoCode is a terminal-native AI coding assistant.

**Core problems it solves**

- **Multi-agent orchestration** — *emory (MEMORY.md) — persistent project knowledge, rules, and architecture decisions*
- **Parallel execution** — *terminal-native intelligence to desktop workflows.*
- **Model / provider routing** — *o/Plus) — OpenAI OAuth login*
- **API gateway / proxy** — *separates the provider ID from the model ID.*
- **Session persistence** — *omatically by the checkpoint-writer subagent*
- **Memory & context** — *e: Where Models and Agents Co-Evolve*
- **Skills & plugins** — *h-paper-writing Write and polish academic papers (ML/CV/NLP style)*
- **MCP support** — *multi-select dialog that persists the setting to config without hand-editing.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://mimo.xiaomi.com/install | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, curl | sh installer; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **13,692** (+6.8/day over 5d)
- Health score: **64/100**
- Documentation score: **62/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Cline / Roo

</details>

## Sessions

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.5k 🚀 +53/d | **70** |
| 🔹 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | This one is invisible to anti-bots. | 🟢 Turnkey · OOTB | ✅ | — | 2.8k | **57** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.8k 🚀 +11/d | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.1k | **55** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 492 | **49** |
| 👀 **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | Meet Tara, your 24/7 personal assistant powered by Claude Code and OpenAI Codex. | 🔴 Involved | — | — | 517 | **38** |

**Also does this:** [affaan-m/ECC](https://github.com/affaan-m/ECC), [garrytan/gstack](https://github.com/garrytan/gstack), [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [zai-org/ZCode](https://github.com/zai-org/ZCode), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [spinabot/brigade](https://github.com/spinabot/brigade), [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [yc-software/qm](https://github.com/yc-software/qm), [cwinvestments/memstack](https://github.com/cwinvestments/memstack) *(+7 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)

> Your AI coding agent forgets everything when the session ends.

**Core problems it solves**

- **Session persistence** — *ns, discoveries, accomplished work, next steps, and relevant files.*
- **Memory & context**
- **Agent runtime**
- **MCP support** — *-response failures remain safely blocked with distinct diagnostics; read-only and non-Engram calls are unaffected.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install gentleman-programming/tap/engram`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install; configure environment variables, database dependency

**Facts**

- Stars: **7,475** (+53.0/day over 5d)
- Health score: **70/100**
- Documentation score: **59/100**
- License: MIT
- Language: Go
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)

> This one is invisible to anti-bots.

**Core problems it solves**

- **Session persistence** — *p refuses: this skips the download, not the version check.*
- **MCP support** — *Other AI browser agents get captchas.*
- **GUI / desktop app** — *browser agent runs on your machine and has no server of its own.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 4/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Platforms mentioned: Windows, Linux, Web
- Turnkey. install via uvx one-liner, curl | sh installer; configure database dependency

**Facts**

- Stars: **2,773** (+4.0/day over 5d)
- Health score: **57/100**
- Documentation score: **33/100**
- License: MIT
- Language: Python
- Last push: 2026-10-17
- Works with: Claude Code, Codex, Gemini CLI

#### [zhnt/loushang](https://github.com/zhnt/loushang)

> Loushang is a method-native AI work system for running complex work from intent to verified delivery.

**Core problems it solves**

- **Model / provider routing**
- **Session persistence** — *g is a method-native AI work system for running complex work from intent to verified delivery.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux, Web
- Easy. install via pip install; needs git clone (build from source), make build

**Facts**

- Stars: **1,817** (+11.4/day over 5d)
- Health score: **56/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-20
- Works with: Codex

#### [hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)

> Monitor Claude Code, Cursor, and Codex sessions in real time.

**Core problems it solves**

- **Multi-agent orchestration** — *st control room for AI coding agents*
- **Session persistence** — *ds, and no automatic self-update.*
- **Skills & plugins** — *-driven dashboard queries and guarded operations MCP guide*
- **Agent runtime** — *# Agent Dashboard for Claude Code, Cursor & Codex*
- **MCP support** — *ns, tool-flow graphs, concurrency, delegation, and compaction analysis.*
- **GUI / desktop app**
- **Notifications** — *thentication, guarded mutations, backup-first edits, bounded uploads, and no automatic self-update.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add hoangsonww/Claude-Code-Agent-Monitor --list`
- Platforms mentioned: macOS, Windows, Web
- Easy. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure database dependency, server/reverse-proxy setup; GUI application

**Facts**

- Stars: **1,099** (+4.2/day over 5d)
- Health score: **55/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, Cursor

#### [chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)

> Persistent memory + session search + secret scanning for Pi

**Core problems it solves**

- **Automatic failover** — *d pi -p processes run with --tools memoryadd,memoryreplace,memoryremove and --exclude-tools mcp*, so a background child cannot edit files, run comman…*
- **Model / provider routing** — *es matching the *-oauth-adapter/*-auth-adapter naming convention (including scoped packages, via their package.json pi.extensions manifest) are detec…*
- **Session persistence** — *operators like OR still work when you need them.*
- **Memory & context** — *n (production install for Pi).*
- **Skills & plugins** — *do something, reusable across sessions Unlimited Discoverable by Pi + manageable via the skillmanage tool*
- **MCP support** — *hout extension-runtime access.*

**Getting it running**

- Setup: 🔴 **Involved** (friction 84/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install`
- Platforms mentioned: Linux, Web
- Involved setup. needs git clone (build from source), npm install/build; configure config.json/yaml/toml, OAuth login flow

**Facts**

- Stars: **492** (+1.0/day over 5d)
- Health score: **49/100**
- Documentation score: **71/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-17

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | The local-first harness & workspace for research agents. | 🟢 Turnkey · OOTB | ✅ | — | 7.4k (+55/d) | **70** |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 Some setup | — | — | 6.4k 🚀 +13/d | **64** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | Open Retrieval-Based Inference Toolkit | 🟡 Some setup | — | — | 355 | **48** |

**Also does this:** [decolua/9router](https://github.com/decolua/9router), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [Licoy/Quosparr](https://github.com/Licoy/Quosparr), [isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)

> The local-first harness & workspace for research agents.

**Core problems it solves**

- **Model / provider routing**
- **Usage analytics** — *orts, feature requests, and general frustrations about OpenResearch.*
- **Agent runtime**
- **GUI / desktop app** — *and produce research artifacts.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 6/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -LsSf https://openresearch.sh/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via curl | sh installer, native installer / package; configure database dependency; GUI application

**Facts**

- Stars: **7,408** (~54.9/day lifetime average)
- Health score: **70/100**
- Documentation score: **33/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [loopx-project/loopx](https://github.com/loopx-project/loopx)

> The workbench for long-horizon research.

**Core problems it solves**

- **Quota & usage management**
- **Mobile access** — *r Manager group conversations, LoopX keeps message visibility separate from*
- **Multi-agent orchestration** — *8 mean reward — +17.3% vs Plain Codex, +10.6% vs native Codex Goal.*
- **Usage analytics** — *dentials, internal project names, or goal contents:*
- **Team collaboration**
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 43/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via pip install; needs git clone (build from source); configure database dependency, database migration

**Facts**

- Stars: **6,373** (+12.8/day over 5d)
- Health score: **64/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)

> AgentOps helps developers build, evaluate, and monitor AI agents.

**Core problems it solves**

- **Multi-agent orchestration** — *All decorators support: - Input/Output Recording - Exception Handling - Async/await functions - Generator functions - Custom attributes and names ##…*
- **Usage analytics**
- **Self-hostable** — *n replays in 2 lines of code*

**Getting it running**

- Setup: 🟢 **Easy** (friction 31/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `pip install agentops`
- Easy. install via pip install; needs npm install/build; configure API key configuration

**Facts**

- Stars: **5,898** (+2.4/day over 5d)
- Health score: **51/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

#### [crshdn/mission-control](https://github.com/crshdn/mission-control)

> Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated.

**Core problems it solves**

- **Multi-agent orchestration** — *nd ideation agents on what to look for, what matters, and what to ignore.*
- **Parallel execution** — *il the model's context window was exhausted and the agent stalled.*
- **Workspace isolation**
- **Model / provider routing**
- **Usage analytics** — *njected at dispatch as primary instructions*
- **Memory & context** — *pend across all tasks for a product*
- **Security & isolation** — *est external checks where GitHub supports it.*
- **Self-hostable** — *no trackers, no centralized data collection*

**Getting it running**

- Setup: 🔴 **Involved** (friction 67/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install`
- Platforms mentioned: Linux, Web
- Involved setup. install via npx one-liner, global npm install; needs docker compose up, docker run; configure environment variables, API key configuration

**Facts**

- Stars: **2,154** (+0.6/day over 5d)
- Health score: **50/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-16
- Works with: Droid

#### [schmitech/orbit](https://github.com/schmitech/orbit)

> Open Retrieval-Based Inference Toolkit

**Core problems it solves**

- **Model / provider routing** — ***Your data, connected** Files, SQL, NoSQL, vector stores, APIs, and MCP tools through YAML-configured adapters.*
- **API gateway / proxy** — ***Your data, connected** Files, SQL, NoSQL, vector stores, APIs, and MCP tools through YAML-configured adapters.*
- **Usage analytics** — *uild agents MCP tools · Automatic skill routing · A2A · Adapter creation*
- **MCP support** — *o voice assistants and tool-using agents.*
- **Security & isolation** — *local or hosted models through one API.*
- **Self-hostable**
- **GUI / desktop app**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 52/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run -d --name orbit \`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via global npm install; needs docker run, npm install/build; configure API key configuration, config.json/yaml/toml

**Facts**

- Stars: **355** (+0.0/day over 5d)
- Health score: **48/100**
- Documentation score: **48/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-20

</details>

## Sharing

*Quota sharing / splitting*

A subscription's capacity is larger than one person needs; share it safely with others.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 102.7k 🚀 +281/d | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 558 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 242 | **39** |

**Also does this:** [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [future-agi/future-agi](https://github.com/future-agi/future-agi), [schmitech/orbit](https://github.com/schmitech/orbit), [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

#### [nexu-io/open-design](https://github.com/nexu-io/open-design)

> OpenDesign is the 1st collaborative AI design agent workspace.

**Core problems it solves**

- **Mobile access** — *read your DESIGN.md and render in a sandboxed iframe.*
- **Model / provider routing** — *No CLI installed? The BYOK proxy at POST /api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream gives you the same loop (no process spaw…*
- **API gateway / proxy** — *udio}/stream gives you the same loop (no process spawn) — paste baseUrl + apiKey + model, with presets for OpenAI, Atlas Cloud, Anthropic, Azure Open…*
- **Quota sharing / splitting**
- **Session persistence** — *ive runtime adapters for agents that OD launches directly.*
- **Skills & plugins** — *cial plugins plus 183 remixable reference examples live in plugins/official/.*
- **Agent runtime** — *then download or open it.*
- **MCP support** — *s — create motion graphics with your agent and export to MP4.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://open-design.ai/install.sh | sh -s <agent>`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Easy. install via npx one-liner, curl | sh installer; needs docker compose up, git clone (build from source); configure database dependency, database migration; one-click setup

**Facts**

- Stars: **102,652** (+280.6/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

> One proxy.

**Core problems it solves**

- **Quota & usage management**
- **Automatic failover** — *cation providing universal /v1/chat/completions (OpenAI) and /v1/messages (Anthropic) endpoints*
- **Model / provider routing** — *LiteLLM-supported provider once.*
- **API gateway / proxy**
- **Quota sharing / splitting**
- **Usage analytics**
- **Skills & plugins**
- **Security & isolation**

**Getting it running**

- Setup: 🔴 **Involved** (friction 66/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run -d \`
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via pip install, native installer / package; needs docker compose up, docker run; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **558** (+0.2/day over 5d)
- Health score: **49/100**
- Documentation score: **70/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-09-23
- Works with: Claude Code, Gemini CLI, OpenCode, Cursor

#### [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

> ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API.

**Core problems it solves**

- **Multi-account switching**
- **Model / provider routing** — *way endpoints for chat, responses, models, embeddings, image, and streaming workloads.*
- **API gateway / proxy**
- **Quota sharing / splitting** — *oarding, and configurable private-account access flows.*
- **Billing & metering** — *a self-hosted AI API gateway and subscription management platform based on Sub2API.*
- **Self-hostable** — *a resets, service interruptions, upstream policy changes, and billing errors are operational risks that must be handled by the deployer.*
- **GUI / desktop app** — *clients that send headers containing underscores, enable underscore headers in the Nginx http block:*
- **Cross-agent support** — *Mentions Codex, OpenCode*

**Getting it running**

- Setup: 🔴 **Involved** (friction 69/100)
- Out of the box: no
- Non-programmer friendly: no
- Involved setup. needs make build; configure API key configuration, config file

**Facts**

- Stars: **242** (+0.2/day over 5d)
- Health score: **39/100**
- Documentation score: **41/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-09-17
- Works with: Codex, OpenCode

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Voice & Remote Control | Desktop UI, Parallelism & Isolation |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Sharing | Desktop UI, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Sharing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile & Remote Control | Mobile, Parallelism & Isolation |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI |
| **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | Billing | Parallelism & Isolation |
| **[openai/codex](https://github.com/openai/codex)** | Sharing | Desktop UI |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Self-hosting & Security | Desktop UI, Sessions |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile & Remote Control | Security, Self-hosting & Security |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Desktop UI, Model Routing |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Parallelism & Isolation | Desktop UI, Sessions |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Parallelism & Isolation | Desktop UI, Self-hosting & Security |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile & Remote Control | Desktop UI, Voice & Remote Control |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Security | Self-hosting & Security |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Parallelism & Isolation | Desktop UI, Model Routing |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | Mobile & Remote Control | Desktop UI |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | Self-hosting & Security | Model Routing |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Self-hosting & Security | Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Security | Desktop UI |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Parallelism & Isolation | Providers, Self-hosting & Security |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Self-hosting & Security | Desktop UI, Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Providers, Sharing |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Model Routing | Desktop UI, Desktop UI |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Voice & Remote Control | Mobile & Remote Control, Security |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Voice & Remote Control | Mobile, Security |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Self-hosting & Security | Desktop UI, Desktop UI |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Model Routing, Sharing |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Parallelism & Isolation | Desktop UI, Desktop UI |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Analytics, Billing |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Billing | Sessions |
| **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | Analytics | Desktop UI, Model Routing |
| **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Sessions | Desktop UI, Self-hosting & Security |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Providers, Sharing |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Voice & Remote Control | Self-hosting & Security, Sessions |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Parallelism & Isolation | Desktop UI |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Mobile & Remote Control | Model Routing, Sessions |
| **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | Providers | Desktop UI |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Security | Self-hosting & Security, Sessions |
| **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Self-hosting & Security | Desktop UI |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Billing, Providers |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Mobile & Remote Control | Desktop UI, Model Routing |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Providers | Desktop UI |
| **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Parallelism & Isolation | Desktop UI, Model Routing |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile & Remote Control | Security, Voice & Remote Control |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | Mobile & Remote Control, Providers |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Voice & Remote Control | Self-hosting & Security, Sessions |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Mobile |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Security | Mobile & Remote Control, Self-hosting & Security |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Desktop UI, Mobile & Remote Control |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Providers | Desktop UI, Self-hosting & Security |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Self-hosting & Security | Mobile & Remote Control, Sessions |
| **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Billing | Desktop UI |
| **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | Self-hosting & Security | Desktop UI |
| **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Parallelism & Isolation | Desktop UI, Desktop UI |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Mobile & Remote Control | Security, Sharing |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | Self-hosting & Security | Model Routing, Sharing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Parallelism & Isolation | Desktop UI, Self-hosting & Security |
| **[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)** | Voice & Remote Control | Mobile & Remote Control, Self-hosting & Security |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Parallelism & Isolation | Mobile |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Parallelism & Isolation | Providers, Security |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI, Self-hosting & Security |
| **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | Sessions | Desktop UI |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Desktop UI | Desktop UI |
| **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | Parallelism & Isolation | Desktop UI, Sessions |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Parallelism & Isolation | Security, Sessions |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Parallelism & Isolation | Desktop UI, Voice & Remote Control |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Desktop UI, Providers |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Parallelism & Isolation | Security, Sessions |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI, Desktop UI |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Analytics, Desktop UI |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | Providers | Desktop UI, Model Routing |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Self-hosting & Security | Desktop UI, Parallelism & Isolation |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | Model Routing | Desktop UI, Self-hosting & Security |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Parallelism & Isolation | Desktop UI, Self-hosting & Security |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Desktop UI | Desktop UI, Security |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Sessions | Desktop UI, Desktop UI |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Security |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Security | Desktop UI, Self-hosting & Security |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Billing, Desktop UI |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Parallelism & Isolation | Desktop UI, Mobile |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Mobile | Billing, Providers |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Mobile | Mobile & Remote Control, Model Routing |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Providers | Desktop UI, Self-hosting & Security |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Parallelism & Isolation |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Parallelism & Isolation | Billing, Voice & Remote Control |
| **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | Parallelism & Isolation | Desktop UI, Sessions |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Security | Desktop UI |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Providers | Desktop UI, Self-hosting & Security |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI, Self-hosting & Security |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Parallelism & Isolation | Desktop UI, Desktop UI |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Security, Self-hosting & Security |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Desktop UI | Sessions |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Security | Desktop UI |
| **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | Security | Mobile & Remote Control, Sharing |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Analytics, Sessions |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile & Remote Control | Sessions, Voice & Remote Control |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Parallelism & Isolation | Desktop UI, Security |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile & Remote Control | Self-hosting & Security, Sessions |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Providers | Self-hosting & Security |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | Sharing | Sessions |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Parallelism & Isolation, Security |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Parallelism & Isolation | Desktop UI, Desktop UI |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Self-hosting & Security | Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Security | Analytics, Providers |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Desktop UI | Desktop UI |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Sharing | Analytics, Billing |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | Security | Desktop UI |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Sharing | Providers, Sharing |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Sessions | Self-hosting & Security |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Parallelism & Isolation | Desktop UI, Sessions |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | Billing | Security |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Parallelism & Isolation | Mobile & Remote Control, Voice & Remote Control |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Providers, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Parallelism & Isolation | Desktop UI, Security |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Analytics | Providers, Sharing |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Providers | Sessions |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Mobile & Remote Control | Parallelism & Isolation |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | Security | Desktop UI, Self-hosting & Security |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Self-hosting & Security | Desktop UI |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | Security | Desktop UI |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Desktop UI |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Self-hosting & Security | Desktop UI, Desktop UI |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Self-hosting & Security | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Providers | Self-hosting & Security, Sharing |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | Self-hosting & Security | Desktop UI |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Billing, Model Routing |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | Sharing | Analytics, Providers |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Sharing | Billing, Sharing |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | Sessions | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.12x the stars (17,595 vs 146,625) |

<details><summary><b>yetone/magpie vs farion1231/cc-switch</b></summary>

Both manage multiple accounts and providers for Claude Code and Codex, and magpie additionally routes other models through the same agent loop.

**Not covered:** Automatic failover, Billing & metering, Parallel execution, Multi-provider aggregation, Session persistence, Skills & plugins, Usage analytics

</details>

---

## 🪦 The Graveyard

There is always a dark horse. When a newer tool covers **every** capability of an incumbent, matches its traction and is no harder to set up, the incumbent is retired here rather than quietly left in the list. Full rules: [docs/SUPERSEDE.md](docs/SUPERSEDE.md).

### Recorded eliminations

| Retired | Replaced by | Why it lost | Source |
| --- | --- | --- | --- |
| **[AVIDS2/memorix](https://github.com/avids2/memorix)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 334.17x the stars (284,378 vs 851) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 58.52x the stars (19,136 vs 327) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 67.66x the stars (29,702 vs 439) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 19.95x the stars (10,915 vs 547) | 🤖 auto (high) |
| **[Dodaios/Dodaios](https://github.com/dodaios/dodaios)** | **[HarnessMD/munder-difflin](https://github.com/harnessmd/munder-difflin)** | 37.05x the stars (8,929 vs 241) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 27.34x the stars (10,388 vs 380) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 18.39x the stars (10,098 vs 549) | 🤖 auto (high) |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 8.96x the stars (2,096 vs 234) | 🤖 auto (high) |
| **[Orkas-AI/Orkas](https://github.com/orkas-ai/orkas)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.68x the stars (10,388 vs 2,222) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 888.68x the stars (284,378 vs 320) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.38x the stars (33,656 vs 925) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.07x the stars (21,495 vs 5,279) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 3.05x the stars (870 vs 285) | 🤖 auto (high) |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 55.72x the stars (33,656 vs 604) | 🤖 auto (high) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 173.83x the stars (284,378 vs 1,636) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.55x the stars (33,656 vs 345) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.60x the stars (27,544 vs 4,922) | 🤖 auto (high) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.66x the stars (13,692 vs 395) | 🤖 auto (high) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 11.19x the stars (4,824 vs 431) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.43x the stars (10,388 vs 353) | 🤖 auto (high) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 11.62x the stars (10,388 vs 894) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 46.33x the stars (21,495 vs 464) | 🤖 auto (high) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1184.91x the stars (284,378 vs 240) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.39x the stars (33,656 vs 275) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.37x the stars (146,625 vs 8,958) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 26.37x the stars (10,098 vs 383) | 🤖 auto (high) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 442.96x the stars (284,378 vs 642) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 14.26x the stars (5,303 vs 372) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 35.92x the stars (29,702 vs 827) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.00x the stars (284,378 vs 6,051) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 3.68x the stars (2,096 vs 569) | 🤖 auto (high) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 401.10x the stars (284,378 vs 709) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 598.69x the stars (284,378 vs 475) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.76x the stars (10,388 vs 2,765) | 🤖 auto (high) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 6.15x the stars (2,922 vs 475) | 🤖 auto (medium) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 7.97x the stars (10,388 vs 1,304) | 🤖 auto (medium) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.89x the stars (870 vs 301) | 🤖 auto (high) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 45.84x the stars (284,378 vs 6,204) | 🤖 auto (medium) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.00x the stars (19,136 vs 2,393) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 4.03x the stars (1,127 vs 280) | 🤖 auto (medium) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 10.42x the stars (4,824 vs 463) | 🤖 auto (medium) |
| **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 673.88x the stars (284,378 vs 422) | 🤖 auto (medium) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.42x the stars (870 vs 360) | 🤖 auto (high) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 7.65x the stars (10,388 vs 1,358) | 🤖 auto (medium) |
| **[AI-QL/tuui](https://github.com/ai-ql/tuui)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 25.63x the stars (29,702 vs 1,159) | 🤖 auto (medium) |
| **[Dataojitori/nocturne_memory](https://github.com/dataojitori/nocturne_memory)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 8.12x the stars (11,349 vs 1,398) | 🤖 auto (high) |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 6.16x the stars (29,702 vs 4,824) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.16x the stars (1,060 vs 490) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.23x the stars (870 vs 391) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.26x the stars (1,099 vs 486) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.55x the stars (782 vs 503) | 🤖 auto (medium) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.15x the stars (870 vs 755) | 🤖 auto (medium) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | 1.48x the stars (422 vs 285) | 🤖 auto (medium) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.16x the stars (312 vs 268) | 🤖 auto (medium) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.27x the stars (782 vs 614) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | providers | 9k | 🔻 Superseded | 16.37x the stars (146,625 vs 8,958) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | self-hosting-security | 6.2k | 🔻 Superseded | 45.84x the stars (284,378 vs 6,204) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | self-hosting-security | 6.1k | 🔻 Superseded | 47.00x the stars (284,378 vs 6,051) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | mobile-remote-control | 5.3k | 🔻 Superseded | 4.07x the stars (21,495 vs 5,279) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | parallelism-isolation | 4.9k | 🔻 Superseded | 5.60x the stars (27,544 vs 4,922) |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | self-hosting-security | 4.8k | 🔻 Superseded | 6.16x the stars (29,702 vs 4,824) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | parallelism-isolation | 2.8k | 🔻 Superseded | 3.76x the stars (10,388 vs 2,765) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 Superseded | 8.00x the stars (19,136 vs 2,393) |
| **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | parallelism-isolation | 2.2k | 🔻 Superseded | 4.68x the stars (10,388 vs 2,222) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | self-hosting-security | 1.6k | 🔻 Superseded | 173.83x the stars (284,378 vs 1,636) |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | self-hosting-security | 1.4k | 🔻 Superseded | 8.12x the stars (11,349 vs 1,398) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | parallelism-isolation | 1.4k | 🔻 Superseded | 7.65x the stars (10,388 vs 1,358) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | parallelism-isolation | 1.3k | 🔻 Superseded | 7.97x the stars (10,388 vs 1,304) |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | self-hosting-security | 1.2k | 🔻 Superseded | 25.63x the stars (29,702 vs 1,159) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism-isolation | 925 | 🔻 Superseded | 36.38x the stars (33,656 vs 925) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | parallelism-isolation | 894 | 🔻 Superseded | 11.62x the stars (10,388 vs 894) |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | self-hosting-security | 851 | 🔻 Superseded | 334.17x the stars (284,378 vs 851) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | self-hosting-security | 827 | 🔻 Superseded | 35.92x the stars (29,702 vs 827) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 Superseded | 1.15x the stars (870 vs 755) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | self-hosting-security | 709 | 🔻 Superseded | 401.10x the stars (284,378 vs 709) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | self-hosting-security | 642 | 🔻 Superseded | 442.96x the stars (284,378 vs 642) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | security | 614 | 🔻 Superseded | 1.27x the stars (782 vs 614) |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | parallelism-isolation | 604 | 🔻 Superseded | 55.72x the stars (33,656 vs 604) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism-isolation | 569 | 🔻 Superseded | 3.68x the stars (2,096 vs 569) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | self-hosting-security | 549 | 🔻 Superseded | 18.39x the stars (10,098 vs 549) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile-remote-control | 547 | 🔻 Superseded | 19.95x the stars (10,915 vs 547) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security | 503 | 🔻 Superseded | 1.55x the stars (782 vs 503) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 490 | 🔻 Superseded | 2.16x the stars (1,060 vs 490) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions | 486 | 🔻 Superseded | 2.26x the stars (1,099 vs 486) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | parallelism-isolation | 475 | 🔻 Superseded | 6.15x the stars (2,922 vs 475) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | self-hosting-security | 475 | 🔻 Superseded | 598.69x the stars (284,378 vs 475) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile-remote-control | 464 | 🔻 Superseded | 46.33x the stars (21,495 vs 464) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | self-hosting-security | 463 | 🔻 Superseded | 10.42x the stars (4,824 vs 463) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | self-hosting-security | 439 | 🔻 Superseded | 67.66x the stars (29,702 vs 439) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | self-hosting-security | 431 | 🔻 Superseded | 11.19x the stars (4,824 vs 431) |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | self-hosting-security | 422 | 🔻 Superseded | 673.88x the stars (284,378 vs 422) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice-remote-control | 395 | 🔻 Superseded | 34.66x the stars (13,692 vs 395) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 391 | 🔻 Superseded | 2.23x the stars (870 vs 391) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | self-hosting-security | 383 | 🔻 Superseded | 26.37x the stars (10,098 vs 383) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism-isolation | 380 | 🔻 Superseded | 27.34x the stars (10,388 vs 380) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | security | 372 | 🔻 Superseded | 14.26x the stars (5,303 vs 372) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 360 | 🔻 Superseded | 2.42x the stars (870 vs 360) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | parallelism-isolation | 353 | 🔻 Superseded | 29.43x the stars (10,388 vs 353) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | parallelism-isolation | 345 | 🔻 Superseded | 97.55x the stars (33,656 vs 345) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 Superseded | 58.52x the stars (19,136 vs 327) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | self-hosting-security | 320 | 🔻 Superseded | 888.68x the stars (284,378 vs 320) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 301 | 🔻 Superseded | 2.89x the stars (870 vs 301) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 285 | 🔻 Superseded | 3.05x the stars (870 vs 285) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | self-hosting-security | 285 | 🔻 Superseded | 1.48x the stars (422 vs 285) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | parallelism-isolation | 280 | 🔻 Superseded | 4.03x the stars (1,127 vs 280) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | parallelism-isolation | 275 | 🔻 Superseded | 122.39x the stars (33,656 vs 275) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | parallelism-isolation | 268 | 🔻 Superseded | 1.16x the stars (312 vs 268) |
| **[Dodaios/Dodaios](https://github.com/Dodaios/Dodaios)** | voice-remote-control | 241 | 🔻 Superseded | 37.05x the stars (8,929 vs 241) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | self-hosting-security | 240 | 🔻 Superseded | 1184.91x the stars (284,378 vs 240) |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | parallelism-isolation | 234 | 🔻 Superseded | 8.96x the stars (2,096 vs 234) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-20 09:29 UTC. 218 live tools · 127 candidates rejected by the quality gates.</sub>
