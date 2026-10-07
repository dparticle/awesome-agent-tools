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

**209 tools** across **15 categories** · **62 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-07 16:31 UTC**

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

- [MCP & Failover](#mcp-failover) — 25 tools
- [Isolation & Parallelism](#isolation-parallelism) — 22 tools
- [Skills](#skills) — 31 tools
- [Sessions & Memory](#sessions-memory) — 23 tools
- [Desktop UI](#desktop-ui) — 20 tools
- [Teams](#teams) — 13 tools
- [Accounts](#accounts) — 13 tools
- [Model Routing](#model-routing) — 13 tools
- [Mobile](#mobile) — 11 tools
- [Quota](#quota) — 12 tools
- [Providers](#providers) — 8 tools
- [Billing](#billing) — 8 tools
- [Analytics](#analytics) — 4 tools
- [Voice](#voice) — 3 tools
- [Sharing](#sharing) — 3 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## MCP & Failover

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.2k 🚀 +324/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot uses .github/copilot-instructions.md instead) Available in release 2.2: guided package setup for Claud… | 🟡 Some setup | — | — | 274.6k (+1048/d) | **89** |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine | 🟢 Easy | — | — | 29.2k (+130/d) | **88** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | media="(prefers-color-scheme: dark)" srcset="assets/moli-browser-banner-dark.jpg" media="(prefers-color-scheme: light)" srcset="assets/moli-browser-banner.jpg" src="assets/moli-browser-banner.jpg" alt="Moli Browser — St… | 🟢 Turnkey · OOTB | ✅ | ✅ | 12k 🚀 +206/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. Yours to run. Native apps for macOS, Windows and Linux; files stay on your | 🟢 Easy | — | — | 8.8k 🚀 +130/d | **85** |
| 🏆 **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. Run Verify runtime to confirm th… | 🟢 Easy | — | — | 13.6k 🚀 +187/d | **84** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. The supervisor binds there too, because it ho… Routines: ask a Bot to do so… | 🟡 Some setup | — | — | 6.2k 🚀 +121/d | **83** |
| 🏆 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.3k 🚀 +103/d | **80** |
| 🏆 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | Other AI browser agents get captchas. | 🟢 Turnkey · OOTB | ✅ | — | 2.6k 🚀 +377/d | **80** |
| 🏆 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.4k 🚀 +95/d | **79** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Respect limits and access decisions. Workers, Goal/Loop, Compact & Resume and finish checkpoints organize work; they do not grant extra quota or model access and must not be used to evade r… Unsigned beta: Windows is no… | 🟢 Easy · OOTB | ✅ | — | 4.2k 🚀 +92/d | **75** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. Appwrite Storage - Store files with compression, encryption, image transformations, and access control. | 🟢 Easy | — | — | 57.6k (+21/d) | **70** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Data visualization Skill for AI Agents, turning data into polished, interactive HTML charts. 面向 AI Agents 的数据可视化 Skill，将数据快速生成精致、可交互的 HTML 图表。 | 🟢 Turnkey · OOTB | ✅ | — | 6k 🚀 +72/d | **69** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Self-Improving Sovereign Agents — voices: @tom_doerr, @AIDailyGems | 🟢 Easy | — | — | 4.7k (+24/d) | **65** |
| ✅ **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. It was carnivorous because it climbed the curtain toward a canary's cage | 🟡 Some setup | — | — | 4k 🚀 +45/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. MCP clients: https://github.com/getsentry/xcodebuildmcp.com/blob/main/app/docs/_content/clients.mdx | 🟢 Turnkey · OOTB | ✅ | — | 6.5k (+11/d) | **63** |
| 🔹 **[Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith)** | Keysmith 给本机的 AI 编程工具装指令：先预览，再写入，能验证，能撤走。 | 🟡 Some setup | — | — | 4.7k 🚀 +47/d | **61** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. On hippo's synthetic lifecycle test, full@365 minus decay-off is -0.7 points [-1.4, 0.1] on currentR5, no measurable effect. That test runs 20 sessions,… Sequential Learning Benchmark… | 🟡 Some setup | — | — | 773 | **56** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | alt="marm-memory - persistent local memory server for AI agents (Model Context Protocol)" Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Do not read that as paralle… | 🟡 Some setup | — | — | 419 | **54** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 677 | **51** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | PAXM carries decisions, conventions, and working context into later Codex, Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP sessions. Write-provider routes default to a 30-second timeout;… | 🟡 Some setup | — | — | 422 🚀 +5/d | **49** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Enable your AI agents to read, analyze, and modify Figma designs. Get document information, current selection, styles | 🟢 Turnkey · OOTB | ✅ | — | 666 | **48** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. IBM API Connect MCP Server - IBM APIC MCP server exposes API Connect capabilities to your MCP clients and AI Agent workflows. | 🟡 Some setup | — | — | 410 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. 🪪 MCP OAuth: Exposed endpoints have options to use standard OAuth in MCP Spec 2025-06-18, easy to connect. | 🔴 Involved | — | — | 2.7k | **46** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 535 | **40** |

**Also does this:** [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [getpaseo/paseo](https://github.com/getpaseo/paseo), [aipoch/open-science](https://github.com/aipoch/open-science), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [topoteretes/cognee](https://github.com/topoteretes/cognee), [KunAgent/Kun](https://github.com/KunAgent/Kun), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase), [felinics/Memoh](https://github.com/felinics/Memoh) *(+11 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **27,250** (~324.4/day lifetime average)
- Health score: **90/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

#### [affaan-m/ECC](https://github.com/affaan-m/ECC)

> Use the guided setup or native plugin commands.

**Core problems it solves**

- **Multi-agent orchestration** — *s and evidence live under docs/releases/.*
- **Parallel execution**
- **Workspace isolation**
- **Model / provider routing** — *shims such as /tdd and /eval live in legacy-command-shims/ for explicit opt-in only.*
- **API gateway / proxy** — *eway remaps model names, configure that in Claude Code rather than in ECC.*
- **Memory & context** — *r debugging, before continuing feature work*
- **Skills & plugins** — *tokens use macOS Keychain by default; explicit file fallback must retain owner-only directory/file permissions.*
- **Agent runtime** — *te ECC, change scope, or change its hook profile.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx ecc-universal@2.2.3 setup`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, bunx one-liner; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **274,608** (~1048.1/day lifetime average)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> Your coding agent remembers everything.

**Core problems it solves**

- **Automatic failover** — *y, paste the block inside { "mcpServers": { ...*
- **Multi-agent orchestration** — *ep / vector / agentmemory adapters score side-by-side, NDJSON output, published scorecards land in docs/benchmarks/.*
- **Model / provider routing** — *inference is on-device afterward.*
- **API gateway / proxy**
- **Billing & metering**
- **Memory & context** — *By default, agentmemory stores iii-engine state outside the repository you start it from: ~/Library/Application Support/agentmemory on macOS, $XDGDAT…*
- **Skills & plugins** — *agentmemory ships 17 skills in the Claude-Code-style /SKILL.md format: 9 invocable action skills (remember, recall, recap, handoff, forget, lesson, c…*
- **Agent runtime** — *Your coding agent remembers everything.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx -y @agentmemory/agentmemory@latest`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no code needed

**Facts**

- Stars: **29,204** (~130.4/day lifetime average)
- Health score: **88/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-06
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

- Stars: **11,975** (~206.5/day lifetime average)
- Health score: **87/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-07

#### [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)

> Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats.

**Core problems it solves**

- **Parallel execution**
- **Model / provider routing** — *n in with Genspark and skip keys, or bring your own*
- **API gateway / proxy** — *n in with Genspark and skip keys, or bring your own*
- **Billing & metering** — *export as PDF or a native editable Word document.*
- **Usage analytics** — *ub Copilot, OpenCode and Windsurf*
- **Skills & plugins** — *Grok, Mistral, OpenRouter, Requesty, Opper, Cheaper Inference, or any OpenAI-compatible endpoint, local*
- **Agent runtime** — *hing that overflows or overlaps before genoffice create assembles the .pptx and slides render hands back a PNG per slide to look at.*
- **MCP support** — *Brasil) · Deutsch · Français · 简体中文 · 繁體中文 · 한국어 · 日本語 · العربية · Русский · Italiano · Nederlands · Polski · Čeština · Bahasa Indonesia · Bahasa Mel…*

**Getting it running**

- Setup: 🟢 **Easy** (friction 20/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -T report.docx -H "Authorization: Bearer $GENOFFICE_MCP_TOKEN" http://server:3093/files/`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **8,836** (~129.9/day lifetime average)
- Health score: **85/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Isolation & Parallelism

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow Outbound images/files enforce maxoutboundimagebytes / maxoutboundfilebytes (20 MiB / 50 MiB defaults) while reading, including… | 🟡 Some setup | — | — | 83.5k (+161/d) | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 98.3k (+449/d) | **89** |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.3k (+99/d) | **85** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! Cron expression — standard 5-field cron with timezone support (e.g. 0 9 * * 1, Asia/Shanghai) | 🟢 Turnkey | — | — | 33.4k (+78/d) | **81** |
| 🏆 **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 14.9k (+79/d) | **78** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is a desktop, mobile, web, and CLI app for coding agents. Cross-device: iOS, Android, desktop, web, and CLI. Start work at your desk, check in from your phone, script it from the terminal. | 🟢 Easy | — | ✅ | 20k (+56/d) | **73** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Website · Documentation · 中文 | 🟢 Turnkey | — | — | 5.3k (+38/d) | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 8.9k (+25/d) | **68** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. Mixture-of-… | 🟢 Turnkey · OOTB | ✅ | — | 3.2k (+25/d) | **67** |
| ✅ **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | module outlines: 7 of 12 modules with 3+ nodes in view (cap 12; 3 dropped as too thin to read as a region; 2 dropped as enclosing mostly other modules) — three separate truncations, each wi… PageRank is a bad co-change… | 🟢 Easy | — | — | 2.4k 🚀 +35/d | **66** |
| ✅ **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. Recover Claude Code and Codex sessions and search source-linked project knowledge. | 🟢 Turnkey | — | ✅ | 2.1k (+6/d) | **62** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.6k (+7/d) | **60** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. Go beyond code — video, slides, and more — the Commander drives open-source tools like HyperFrames and hands off to CLI agents — the coding agents Cla… | 🟡 Some setup | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. Before the prompt, the CLI shows (1) the public URL th… | 🟡 Some setup | — | — | 1k | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 519 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. Integrate through your agent. Claude Code, Codex & co. alre… | 🟢 Turnkey | — | — | 307 | **55** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. playwright &mdash; browser automation (most token-efficient) | 🟡 Some setup | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | The structured skill framework for Claude Code: 131 professional skills for deployment, security, databases, content, marketing, and more. TokenStack™ integration: Context compression proxy for token savings | 🟢 Easy | — | — | 423 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. Claude Haiku 45 Speed Optimizer Agent - Agents - A… | 🟢 Easy | — | — | 299 | **49** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Run every AI coding agent in its own git worktree, in parallel. The desktop app embeds its server on 127.0.0.1 with a per-launch token; nothing is exposed to the network. | 🟢 Turnkey | — | ✅ | 267 | **47** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | A macOS desktop app for running multiple AI agents in parallel. Run separate agent sessions side-by-side, each in its own workspace with an isolated git worktree | 🟢 Easy | — | ✅ | 216 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory), [hex/claude-council](https://github.com/hex/claude-council), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

> English | 中文 | 日本語 | Français | Русский | Português

**Core problems it solves**

- **Automatic failover** — *d X-Forwarded-Proto: https) or localhost HTTP.*
- **Multi-agent orchestration** — *llion to our incredible community — you made this happen! 💪🔥*
- **Parallel execution** — *x plus Docker is the recommended deployment target for a persistent server.*
- **Workspace isolation** — *ame matches the payload's type field.*
- **Model / provider routing** — *u configure an optional web search provider, or skip it for now.*
- **API gateway / proxy** — *Optional per-model requestadmission paces requests to help stay within provider request-per-minute limits. It is disabled by default; see the linked…*
- **Usage analytics** — *ent cards show the effective model and, when the provider returns usage metadata, a cumulative token total that updates after each completed sub-agen…*
- **Session persistence** — *es to DeerFlow and get streaming responses*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @minimax-ai/code`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **83,464** (~161.1/day lifetime average)
- Health score: **90/100**
- Documentation score: **80/100**
- License: MIT
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Cursor, Droid

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

- Stars: **98,271** (~448.7/day lifetime average)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

> Persistent file-based planning for AI coding agents and long-running tasks.

**Core problems it solves**

- **Multi-agent orchestration** — *plugins for Claude Code, Codex CLI, Pi, Hermes Agent, OpenCode and DeepSeek Harness.*
- **Parallel execution** — *ry mechanism below is a file on disk plus a hook, so it works the same on hour ten as on turn one.*
- **Workspace isolation** — *** One orchestrator owns taskplan.md and the shared summaries; every worker appends to its own ledger or assigned file.*
- **Memory & context**
- **Skills & plugins** — *ackage, wired up for you (skill, extension, status bar):*
- **Agent runtime** — *s every turn, a plan on disk that survives /clear , and 3 out of 3 blind A/B wins to show it works.*
- **Security & isolation**
- **Cross-agent support** — *Mentions Amp, Claude Code, Codex, Continue*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure environment variables, database dependency; one-click setup

**Facts**

- Stars: **27,318** (~98.6/day lifetime average)
- Health score: **85/100**
- Documentation score: **73/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)

> 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors!

**Core problems it solves**

- **Remote control** — *, docx, pdf, xlsx, mermaid, and more.*
- **Multi-agent orchestration** — *tasks, and delegates to **Teammate** agents via a built-in Team MCP Server.*
- **Parallel execution** — *results immediately without switching apps*
- **Workspace isolation** — *AionUi coordinates the team*
- **API gateway / proxy** — *tforms** — DeepSeek, MiniMax, Novita, OpenRouter, SiliconFlow, xAI, Ark (Volcengine), Poe*
- **Skills & plugins** — *eate and manage your own assistants and skills.*
- **Agent runtime** — *sable Excel (.xlsx/.xlsm/.csv)*
- **MCP support** — *- **No CLI tools to install** — the agent engine is built in - **No complex setup** — paste any API key to get started - **Full agent capabilities**…*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 2/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install aionui`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via Homebrew install, download a release binary; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **33,351** (~78.3/day lifetime average)
- Health score: **81/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-09-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)

> cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动态 Workflow 编排、模型请求追踪、Computer Use、技能市场、多主题、桌面宠物、H5 远程访问、IM 接入和定时任务，集中在一…

**Core problems it solves**

- **Automatic failover** — *图片生成：聊天中直接生成和编辑图片——ChatGPT / Grok 授权登录即可使用，也支持接入任意 OpenAI 兼容的 Images API。*
- **Remote control** — *de Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动…*
- **Multi-agent orchestration** — *GitHub Pull Requests License 中文 English Docs 简体中文 · English cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Cla…*
- **Workspace isolation** — *cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、…*
- **Billing & metering** — *过程中有问题、想反馈 Bug，或者想看看别人怎么用，欢迎扫码加入 cc-haha 企业微信用户群。*
- **Usage analytics**
- **Session persistence** — */ Agent 定制需求，请联系作者 NanmiCoder。*
- **Memory & context** — *端功能 功能总览 · Computer Use · 桌面宠物 · 手机 H5 与 IM 接力*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Easy. configure API key configuration; GUI application

**Facts**

- Stars: **14,892** (~78.8/day lifetime average)
- Health score: **78/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code

</details>

## Skills

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | English \| 简体中文 \| 日本語 \| 한국어 \| Русский | 🟡 Some setup | — | — | 44.2k (+311/d) | **89** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | — | 157.3k 🚀 +1344/d | **88** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 26.8k (+122/d) | **85** |
| 🏆 **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** | Copy/paste into your CLI prompt: | 🟢 Easy | — | — | 54.8k (+375/d) | **84** |
| 🏆 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. One dominant silhouette built from roughly 4–7 large basic shapes | 🟢 Turnkey · OOTB | ✅ | — | 5.8k 🚀 +116/d | **78** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 9.2k 🚀 +77/d | **72** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.6k (+34/d) | **71** |
| ✅ **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.3k 🚀 +84/d | **66** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. ⚡ High Performance: Built with Rust and Tauri 2.0 for a lightweight, blazing-fast experience. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace If it still fails, delete the plugin by hand: remove its folder under %USERPROFILE%\.copilot\installed-plugins\ (or %COPILOT_HO… | 🟢 Easy | — | — | 1k | **57** |
| 🔹 **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 3.3k (+27/d) | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.8k (+8/d) | **56** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | "A skill forgotten is a power lost." — The Code Architect Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ — AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and migration digest for 4.6→4.7… | 🟢 Easy | — | — | 804 | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 885 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 342 | **53** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). A wrapper CLI. No daemon, no server, no runtime state. run.sh is 8 lines. | 🟢 Easy | — | — | 756 🚀 +8/d | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. Claude Code. No subagents are used, so this skill runs in a single context. | 🟢 Turnkey | — | ✅ | 491 | **52** |
| 🔹 **[zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills)** | 引文管理：DOI → BibTeX，文献元数据提取，引文验证 审稿意见回复（Rebuttal / Peer-review response） | 🟡 Some setup | — | — | 4.6k (+32/d) | **51** |
| 🔹 **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | An advanced Distributed Automation Platform for high-concurrency account registration and full-lifecycle inventory management. Docker-aware proxy adaptation: Rewrites 127.0.0.1 / localhost to host.docker.internal inside… | 🟡 Some setup | — | — | 1.4k (+7/d) | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 Easy | — | — | 1.1k | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **48** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. 75% of resumes rejected by ATS before humans see them | 🟢 Easy | — | — | 2.6k (+10/d) | **47** |
| 🔹 **[JimLiu/baocut](https://github.com/JimLiu/baocut)** | Give your AI coding agent the power to drive BaoCut — transcribe, add and translate subtitles, review speakers, edit timelines and overlays, and export — all from natural language. Codex — reference the baocut skill in… | 🟢 Easy | — | — | 529 🚀 +6/d | **45** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | GRACE means Graph-RAG Anchored Code Engineering: a contract-first AI engineering methodology built around semantic markup, .grace XML artifacts, knowledge-graph navigation, assertions, scopes, and log-driven verificatio… | 🟡 Some setup | — | — | 252 | **44** |
| 👀 **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | A curated collection of Claude Code skills for academic research in economics, finance, and the broader social sciences — organized by the common types of skills a researcher needs across a project's lifecycle. excalidr… | 🟡 Some setup | — | — | 223 | **44** |
| 👀 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor Overall… | 🔴 Involved | — | — | 777 | **43** |

**Also does this:** [garrytan/gstack](https://github.com/garrytan/gstack), [affaan-m/ECC](https://github.com/affaan-m/ECC), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [google/artemis](https://github.com/google/artemis), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [spinabot/brigade](https://github.com/spinabot/brigade), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [nexu-io/html-anything](https://github.com/nexu-io/html-anything), [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd), [redhat-et/ripwire](https://github.com/redhat-et/ripwire), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) *(+18 more)*

*…and 1 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

> English | 简体中文 | 日本語 | 한국어 | Русский

**Core problems it solves**

- **Multi-agent orchestration** — *no important change is missed.*
- **Model / provider routing**
- **Skills & plugins**
- **Agent runtime**
- **MCP support** — *forms and package managers*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g @alibaba-group/open-code-review`
- Platforms mentioned: Linux, Web
- Some setup. install via global npm install; needs npm install/build; configure environment variables, API key configuration

**Facts**

- Stars: **44,160** (~311.0/day lifetime average)
- Health score: **89/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-10-05
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

> You know him.

**Core problems it solves**

- **Skills & plugins**
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Easy. install via npx one-liner; configure config file, config.json/yaml/toml

**Facts**

- Stars: **157,284** (~1344.3/day lifetime average)
- Health score: **88/100**
- Documentation score: **47/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [phuryn/pm-skills](https://github.com/phuryn/pm-skills)

> Designed for Claude Code and Cowork.

**Core problems it solves**

- **Usage analytics** — *gles that differentiate us from Notion*
- **Skills & plugins** — *edge), you can force loading skills with /plugin-name:skill-name or /skill-name (Claude will add the prefix).*
- **Notifications** — *framework should I use for a 50-item backlog?*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Linux
- Easy. install via native installer / package; configure database dependency, database migration; beginner-friendly

**Facts**

- Stars: **26,818** (~122.5/day lifetime average)
- Health score: **85/100**
- Documentation score: **56/100**
- License: MIT
- Last push: 2026-09-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

> Copy/paste into your CLI prompt:

**Core problems it solves**

- **Skills & plugins**

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Easy. No setup signals found in the README.

**Facts**

- Stars: **54,766** (~375.1/day lifetime average)
- Health score: **84/100**
- Documentation score: **31/100**
- License: MIT
- Language: Python
- Last push: 2026-10-06

#### [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)

> ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots.

**Core problems it solves**

- **Multi-agent orchestration** — *. Bottom or side cropping may strengthen the corner emergence, but the Skill does not prescribe exact edge contact or a fixed crop.*
- **Skills & plugins** — *er falls back to SVG; another image model may be used only with explicit user consent, with no guarantee of equivalent quality.*
- **Agent runtime** — *d image without filtering or automatic retries*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 13/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills@latest add s1dashu/ip-as-logo-skill`
- Turnkey. install via npx one-liner, native installer / package; configure API key configuration

**Facts**

- Stars: **5,825** (~116.5/day lifetime average)
- Health score: **78/100**
- Documentation score: **36/100**
- License: MIT
- Last push: 2026-08-22
- Works with: Codex

</details>

## Sessions & Memory

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 7.3k 🚀 +92/d | **74** |
| ✅ **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。 Awesome Claude Code Skills — Claude Code Skills / Agents / Plugins 精选合集 | 🟡 Some setup | — | — | 12.4k (+94/d) | **72** |
| ✅ **[pacifio/atlas](https://github.com/pacifio/atlas)** | Switching agents loses the thread. Claude Code cannot read Codex's history, and Codex cannot read Claude Code's. Changing agent mid-task means starting the explanation over. Nothing is locked in. Notes are markdown, can… | 🟢 Easy | — | — | 9.3k (+64/d) | **72** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 31.5k (+27/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | sealed_token is a GitHub fine-grained token encrypted against Star History's public key, so only the encrypted value is published here. | 🟢 Easy · OOTB | ✅ | — | 7.1k (+30/d) | **67** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. Fault-injection scenarios — 64 scenarios covering cursor tampering, | 🔴 Involved | — | — | 1.2k 🚀 +21/d | **58** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Conversations with AI agents reset when context windows close. Agent Action Grammar (AAG): Ultra-compact, deterministic ASCII micro-syntax saving ~78–85% tokens compared to natural language prompt instructions. | 🟡 Some setup | — | — | 757 🚀 +24/d | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | Decomposed retrieval evaluation: ARES (NAACL 2024), RAGChecker (2024) Memory and knowledge-base poisoning: AgentPoison (NeurIPS 2024), PoisonedRAG (USENIX Security 2025) | 🟢 Easy · OOTB | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. Delegation — core/delegation: backend-neutral | 🟢 Easy | — | — | 416 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 如果使用 SQLite，系统会在应用迁移之前自动备份你的数据库文件（如 yourdb.db.20260303143000.bak）。 如果是 Antigravity：args 必须指向 backend/mcp_wrapper.py（解决 Windows CRLF 问题）。 | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 835 | **52** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Plugin-first long-term memory for every agent platform. Corrections that stick. Superseding a record retires the old value from recall and from prompt injection, while git keeps the history. | 🟢 Easy | — | ✅ | 547 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 427 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 611 | **51** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. MCP surface. Tools, tool profiles for hosts with tool limits, and the always-loaded writer server: docs/mcp.md. | 🟢 Easy | — | — | 430 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Intelligent LLM Routing (omega-pro) — Classifies tasks and routes to the optimal model. Coding → Claude Sonnet. Quick edit → Llama 8b at 1/60th the cost. 1M token context → Gemini Flash. 5… Secure Profile (omega-pro) —… | 🟡 Some setup | — | — | 219 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | LycheeMemory is a compact memory framework for LLM agents. GET /mcp exposes the SSE stream used by some MCP clients | 🟡 Some setup | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 473 | **49** |
| 🔹 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. 2026-03-05: api-auth-refactor, JWT + refresh tokens | 🔴 Involved | — | — | 514 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself… | 🟢 Easy | — | — | 247 | **46** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 474 | **42** |
| 👀 **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | Manages collaboration — agents communicate directly, persist state to files, follow built-in protocols Sets up everything — planning files, docs/ knowledge base, CLAUDE.md operations guide, agent onboarding | 🟡 Some setup | — | — | 307 | **39** |

**Also does this:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [garrytan/gstack](https://github.com/garrytan/gstack), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [spinabot/brigade](https://github.com/spinabot/brigade), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory), [hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code), [pax-beehive/paxm](https://github.com/pax-beehive/paxm)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)

> 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。

**Core problems it solves**

- **Multi-agent orchestration**
- **Memory & context** — *异地、再婚、跨文化关系，以及建立在知情同意基础上的非单偶关系。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Easy. No setup signals found in the README.

**Facts**

- Stars: **7,257** (~91.9/day lifetime average)
- Health score: **74/100**
- Documentation score: **42/100**
- License: MIT
- Language: Python
- Last push: 2026-09-20
- Works with: Codex

#### [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)

> Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。

**Core problems it solves**

- **Memory & context**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Some setup. needs git clone (build from source)

**Facts**

- Stars: **12,397** (~93.9/day lifetime average)
- Health score: **72/100**
- Documentation score: **40/100**
- License: MIT
- Last push: 2026-09-24
- Works with: Claude Code, Codex

#### [pacifio/atlas](https://github.com/pacifio/atlas)

> Source control for coding agents.

**Core problems it solves**

- **Multi-agent orchestration** — *cupy the context window for the rest of the session.*
- **Usage analytics**
- **Session persistence** — *gent session produced which commit), which is SQLite in the project's gitignored .atlas/, because it is queried, not read.*
- **Memory & context** — *ts, tool calls, and reasoning.*
- **Agent runtime**
- **GUI / desktop app** — *. Code, notes, and sessions stay on your machine. Sign in and create an organisation when you want to sync across a team.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Kilo Code*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source); configure sign-in required, database dependency; GUI application

**Facts**

- Stars: **9,263** (~63.9/day lifetime average)
- Health score: **72/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [topoteretes/cognee](https://github.com/topoteretes/cognee)

> We rely on free small models that use your CPU.

**Core problems it solves**

- **Model / provider routing** — *natively, create a .env file using our template.*
- **Memory & context** — *ion, conversations, tickets, code, and agent work into shared memory.*
- **MCP support** — *gins, and source connectors.*
- **Self-hostable**
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run --rm -it -p 8000:8000 \`
- Platforms mentioned: Linux
- Some setup. install via pip install, native installer / package; needs docker run; configure config.json/yaml/toml, OAuth login flow

**Facts**

- Stars: **31,529** (~27.5/day lifetime average)
- Health score: **69/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)

> sealed_token is a GitHub fine-grained token encrypted against Star History's public key, so only the encrypted value is published here.

**Core problems it solves**

- **Session persistence** — *ns, discoveries, accomplished work, next steps, and relevant files.*
- **Memory & context** — *Persistent memory for AI coding agents*
- **Agent runtime** — *Persistent memory for AI coding agents*
- **MCP support** — *ace of a memory in the brain.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 22/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `brew install gentleman-programming/tap/engram`
- Platforms mentioned: Windows, Linux, Web
- Easy. install via Homebrew install; configure database dependency

**Facts**

- Stars: **7,070** (~30.3/day lifetime average)
- Health score: **67/100**
- Documentation score: **54/100**
- License: MIT
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Desktop UI

*Agent runtime*

This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 212.1k (+405/d) | **90** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 149.7k (+253/d) | **90** |
| 🏆 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 14.9k 🚀 +178/d | **85** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | An agent skill for crafting cinematic product videos: 157 shot recipe cards · 214 styles · 214 motion previews · a production-ready template 🌟 2026-08 · 48 new shot recipe cards — the library grows from 104 to | 🟢 Turnkey | — | ✅ | 10.6k 🚀 +132/d | **85** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 25.7k 🚀 +231/d | **83** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 8.3k 🚀 +77/d | **75** |
| ✅ **[nexu-io/html-anything](https://github.com/nexu-io/html-anything)** | The eight skills that surface at the top of the picker's Featured / 推荐 group — sorted by their recommended: rank in SKILL.md frontmatter (lower = higher). alchaincyf/huashu-md-html — the anti-AI-slop discipline that map… | 🔴 Involved | — | — | 9k (+61/d) | **69** |
| ✅ **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 Turnkey · OOTB | ✅ | ✅ | 3.1k 🚀 +39/d | **65** |
| ✅ **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.5k (+44/d) | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.6k (+6/d) | **60** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 530 | **57** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. Cross-agent deployment — See which agents have the extension and which don't — deploy to any missing agent with one click. HarnessKit h… | 🟢 Turnkey | — | — | 451 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | A persistent memory system for AI coding agents that enables long-term context retention across sessions using local vector database technology. In later sessions, relevant memories are injected into context (see chatMe… | 🔴 Involved | — | — | 1.7k (+6/d) | **55** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 564 🚀 +5/d | **55** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code The url-shortener example — fresh-context runs that never saw our list of known problems found 12 of 13 cross-document pro… | 🟢 Easy | — | — | 298 | **52** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Evolve — evolutionary program search with a mandatory budget and zero-call resume. | 🟢 Easy · OOTB | ✅ | — | 687 (+5/d) | **51** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 731 | **50** |
| 🔹 **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | Claudable is a powerful Next.js-based web app builder that combines Claude Code's (Cursor CLI also supported!) advanced AI agent capabilities with Lovable's simple and intuitive app building experience. Features: 256K-1… | 🟡 Some setup | — | — | 4.1k (+10/d) | **49** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? flow.browser_identity: browser-specific identity API behavior. | 🟡 Some setup | — | — | 436 | **47** |
| 👀 **[wong2/diffx](https://github.com/wong2/diffx)** | A local code review tool designed for the coding agent workflow. Comment status tracker — Sidebar widget showing open, replied, and resolved comment counts with click-to-navigate links | 🟢 Turnkey · OOTB | ✅ | ✅ | 208 | **42** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [openai/codex](https://github.com/openai/codex), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [yetone/magpie](https://github.com/yetone/magpie), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [yc-software/qm](https://github.com/yc-software/qm), [trailhq/Graft](https://github.com/trailhq/Graft) *(+32 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [anomalyco/opencode](https://github.com/anomalyco/opencode)

> curl -fsSL https://opencode.ai/install | bash

**Core problems it solves**

- **Multi-agent orchestration** — *alysis and code exploration*
- **Agent runtime** — *The open source AI coding agent.*
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://opencode.ai/install | bash`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via Homebrew install, scoop install; GUI application

**Facts**

- Stars: **212,140** (~404.9/day lifetime average)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

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

- Stars: **149,710** (~253.3/day lifetime average)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **14,925** (~177.7/day lifetime average)
- Health score: **85/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-05
- Works with: Codex

#### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)

> An agent skill for crafting cinematic product videos: 157 shot recipe cards · 214 styles · 214 motion previews · a production-ready template

**Core problems it solves**

- **Skills & plugins**
- **Agent runtime** — *communities whose published principles (e.g.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npx skills add Vincentwei1021/video-shotcraft`
- Platforms mentioned: macOS, Linux, Web
- Turnkey. install via npx one-liner; needs git clone (build from source); one-click setup

**Facts**

- Stars: **10,576** (~132.2/day lifetime average)
- Health score: **85/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex

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

- Stars: **25,678** (~231.3/day lifetime average)
- Health score: **83/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

</details>

## Teams

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. 👔 Senior Project Manager - Scope and task planning | 🟢 Turnkey | — | — | 158.1k (+440/d) | **98** |
| 🏆 **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 10.6k 🚀 +90/d | **80** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 7.6k 🚀 +84/d | **80** |
| 🏆 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.4k 🚀 +223/d | **79** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Your coding agent already has a memory feature. | 🔴 Involved | — | — | 8.9k (+65/d) | **70** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. single-shot by Shichinomiya (@shichinomiya_s) — independent blind-scored benchmark (2 problems, LLM-as-judge, A/B positions swapped). ADHD w… | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k (+32/d) | **68** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. UI — A Vue 3 design system for AI agent management interfaces, including a component library, design tokens, and skills that… | 🟡 Some setup | — | — | 2.6k (+10/d) | **57** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that consults multiple AI coding agents in parallel and shows you their answers side-by-side. kimi-cli (Kimi Code CLI, kimi) shadows the kimi API provider, using the kimi CLI's own configured model… | 🟡 Some setup | — | — | 843 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. 2,060+ production helpers and supporting modules, excluding tests | 🟡 Some setup | — | — | 406 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Hots are tater-tots now. v1.1.7 called them hots. The first time a newer veil runs while you are logged in Windows. The first time veil binds a port, Windows Defender Firewall pops up *"Allow this app | 🟢 Easy | — | — | 215 | **54** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM It uses the premium AI model only where it matters. Code-writing uses the top model. Planning, research, review, and checki… | 🟢 Easy | — | — | 1.1k (+9/d) | **49** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models SHA-256 hash-chained — each trace commits to the previous, tamper-evident | 🟡 Some setup | — | — | 503 | **47** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. AI-ready devcontainers: Claude Code,… | 🔴 Involved | — | — | 322 | **47** |

**Also does this:** [loopx-project/loopx](https://github.com/loopx-project/loopx), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **158,113** (~440.4/day lifetime average)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)

> Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, enforce policies and…

**Core problems it solves**

- **Remote control** — *ode, point at OpenRouter's Anthropic-compatible endpoint*
- **Mobile access**
- **Multi-agent orchestration** — *agents ship with the repo, and they make good first sessions:*
- **Workspace isolation**
- **Model / provider routing** — *switch models in the middle of a session with the /model command.*
- **API gateway / proxy** — *A first-party vendor key for Anthropic, OpenAI, and similar providers*
- **Agent runtime** — *quires agy 1.1.13 or newer.*
- **MCP support** — *ies, searches the live web and reads*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, curl | sh installer; needs docker compose up, npm install/build; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **10,643** (~90.2/day lifetime average)
- Health score: **80/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [TencentCloud/Octop](https://github.com/TencentCloud/Octop)

> Octop is an open-source, self-hosted AI assistant.

**Core problems it solves**

- **Automatic failover** — *h OCTOPDEFAULTPASSWORD unset a strong random password is generated; a password you set must be ≥8 characters with letters and digits (weak/common pas…*
- **Mobile access** — *Linux alongside the web dashboard and IM channels.*
- **Multi-agent orchestration** — *A smarter, self-hosted AI assistant — multi-user, multi-agent.*
- **Parallel execution**
- **Workspace isolation** — *dows scripts\install.bat or install.ps1*
- **Model / provider routing** — *ild / quality** hatchling · ruff · mypy · pytest*
- **API gateway / proxy** — *ays back up first (octop backup) before a cross-version upgrade.*
- **Billing & metering** — *Docker Any docker/docker-compose.yml*

**Getting it running**

- Setup: 🟢 **Easy** (friction 26/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs docker run, make build; configure config.json/yaml/toml, OAuth login flow; one-click setup

**Facts**

- Stars: **7,628** (~83.8/day lifetime average)
- Health score: **80/100**
- Documentation score: **78/100**
- License: MIT
- Language: Python
- Last push: 2026-10-06
- Works with: Claude Code, Codex, OpenCode

#### [yc-software/qm](https://github.com/yc-software/qm)

> A multiplayer agent harness for work.

**Core problems it solves**

- **Workspace isolation**
- **Model / provider routing** — *- Work in an existing repository: run tests, open PRs, monitor CI, check system logs*
- **Session persistence**
- **Skills & plugins**
- **Agent runtime** — *store, sandbox, memory) sits behind an interface.*
- **Security & isolation** — *observe, or enforce, with securityScreen.classifier choosing the built-in*
- **Team collaboration** — *e designed like personal assistants.*
- **GUI / desktop app** — *is an optional in-process plugin that core starts*

**Getting it running**

- Setup: 🔴 **Involved** (friction 72/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install`
- Platforms mentioned: Linux, Web
- Involved setup. needs git clone (build from source), npm install/build; configure database dependency, database migration

**Facts**

- Stars: **15,359** (~222.6/day lifetime average)
- Health score: **79/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex, OpenCode

#### [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

> Your coding agent already has a memory feature.

**Core problems it solves**

- **Workspace isolation** — *box/queue plus the on-start "you have mail" notice.*
- **Model / provider routing**
- **API gateway / proxy**
- **Memory & context** — *> Long-term memory for AI coding agents.*
- **Agent runtime** — *> Long-term memory for AI coding agents.*
- **MCP support** — *unchd-without-the-app paths:*
- **Security & isolation** — *t one server and what one*
- **Team collaboration** — *here reachable — a homelab box, a LAN host — and*

**Getting it running**

- Setup: 🔴 **Involved** (friction 64/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL "$wrapper_base" -o "$wrapper_tmp/ai-memory-wrapper"`
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via native installer / package; needs docker run, git clone (build from source); configure config.json/yaml/toml, OAuth login flow

**Facts**

- Stars: **8,903** (~64.5/day lifetime average)
- Health score: **70/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Accounts

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 128.1k (+236/d) | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code on Kimi, Codex on DeepSeek, Gemini CLI on GLM, OpenCode on your ChatGPT plan. Share it on your network. Turn on Share on local network, then create a named gateway key for each client, each with its own dail… | 🟢 Turnkey | — | — | 5.7k 🚀 +405/d | **84** |
| 🏆 **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 28 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 17k 🚀 +155/d | **83** |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 30.4k (+111/d) | **81** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth，以及 Grok apply_patch 协议兼容方向亦参考其开源实现：router-f… Grok CLI 凭据不加密：access token/… | 🟢 Easy | — | — | 18.7k (+71/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls.… | 🟢 Easy | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 支持四种导入方式：本地 CPA JSON 文件导入、远程 CPA 服务器导入、sub2api 服务器导入、access_token 导入 | 🔴 Involved | — | — | 6.5k (+38/d) | **56** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 官方预设：阿里云 / 智谱 / 豆包 Coding Plan，DeepSeek，Moonshot(Kimi)，MiniMax，ModelScope，OrcaRouter，无限星河 | 🔴 Involved | — | — | 3.3k (+15/d) | **54** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. Account pool — OAuth login for multiple ChatGPT accounts, stored locally under ~/.codex/multi-auth (files 0600, directories 0700), wi… | 🟡 Some setup | — | ✅ | 534 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. 📊 Monitor live 5h / 7d ra… | 🟢 Easy | — | — | 271 | **52** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota Timed – pick specific times of day (e.g. 08:00, 13:00… | 🟢 Easy | — | ✅ | 881 | **51** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Automatic Token Refresh: Claude Code manages token refresh internally. CAAM cannot refresh Claude tokens—use /login in Claude Code if tokens expire. --max-retries N — Maximum retry attempts on rate limit (default: 1) | 🟡 Some setup | — | — | 208 | **51** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 为 Sub2API 增加 账号级 STATE 票据管理，尝试应对最近 ChatGPT / Codex 账号的模型降质和降并发：请求的模型被路由到其他模型，或 OpenAI 上游限制账号可同时处理的请求数量。 特别感谢 gylive/ccodex-sleep-state 带来的生命周期管理与状态展示思路参考。 | 🟡 Some setup | — | — | 214 🚀 +11/d | **48** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [stablyai/orca](https://github.com/stablyai/orca), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [gary23w/nl-veil](https://github.com/gary23w/nl-veil), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

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

- Stars: **128,146** (~236.4/day lifetime average)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-07
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi, Codex on DeepSeek, Gemini CLI on GLM, OpenCode on your ChatGPT plan.

**Core problems it solves**

- **Multi-account switching**
- **Quota & usage management**
- **Automatic failover**
- **Model / provider routing** — *sonix planner default restores Plan.*
- **API gateway / proxy** — *ncent Cloud · Huawei Cloud MaaS · Volcengine Ark · Mistral · Groq · xAI · OpenRouter · Together · Fireworks · SiliconFlow · NVIDIA NIM · ModelScope ·…*
- **Usage analytics** — *in magpie as they do in their own apps.*
- **Agent runtime**
- **MCP support** — *magpie offers it as a provider.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://usemagpie.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via go install, curl | sh installer; configure config file, sign-in required; one-click setup

**Facts**

- Stars: **5,667** (~404.8/day lifetime average)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

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

- Stars: **17,044** (~154.9/day lifetime average)
- Health score: **83/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **30,405** (~110.6/day lifetime average)
- Health score: **81/100**
- Documentation score: **66/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

> English · Portuguese (BR) · 简体中文

**Core problems it solves**

- **Multi-account switching** — *surf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Quota & usage management** — *目前支持 Antigravity IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，…*
- **Automatic failover**
- **Multi-agent orchestration** — *测速与已有连接处理的设计也参考其源码，当前运行内核仍为 Mihomo，不代表官方合作关系。*
- **Parallel execution** — *ty IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Model / provider routing**
- **Multi-provider aggregation** — *어 · 🇧🇷 Português · 🇷🇺 Русский · 🇹🇷 Türkçe · 🇵🇱 Polski · 🇨🇿 Čeština · 🇸🇦 العربية · 🇻🇳 Tiếng Việt · 🇮🇩 Bahasa Indonesia*
- **API gateway / proxy** — *ity 账号切号逻辑参考：Antigravity-Manager*

**Getting it running**

- Setup: 🟢 **Easy** (friction 26/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **18,691** (~70.8/day lifetime average)
- Health score: **77/100**
- Documentation score: **60/100**
- Language: Rust
- Last push: 2026-10-01
- Works with: Codex, OpenCode, Cursor, Copilot

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | — | 73.7k (+398/d) | **89** |
| 🏆 **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. More coding-agent integrations: Oh My Pi, Antigravity, IBM Bob / Bob Shell, and Kiro join Codex, Claude Code, OpenCode, GitHub… | 🟡 Some setup | — | — | 17k 🚀 +160/d | **83** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. cron: "23 7 * * 1" # Mondays at 07:23 UTC | 🟡 Some setup | — | — | 11k 🚀 +129/d | **81** |
| 🏆 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 9.3k 🚀 +106/d | **80** |
| 🏆 **[trailhq/Graft](https://github.com/trailhq/Graft)** | You correct it, and by the next session it has forgotten. Entry-point trace — Trace end-to-end what happens when a client creates a record via the REST API, from route handler to database write. | 🟡 Some setup | — | — | 9.7k 🚀 +101/d | **79** |
| ✅ **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.5k 🚀 +373/d | **75** |
| ✅ **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens. Grok 4.5 / 4.6 (opt-in): native 14px / 84 cols / maxH 512 (100/100 arith… | 🟢 Easy · OOTB | ✅ | — | 7.5k (+54/d) | **71** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. loushang code: a coding-focused CLI and terminal workbench. | 🟢 Easy | — | — | 1.7k (+13/d) | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 342 | **53** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CR… | 🟡 Some setup | — | — | 372 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 706 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code is an AI coding workspace for work that lasts longer than one prompt. On the harder tasks, the average fix-to-pass rate rises from 71.8% to 98.4%. | 🟡 Some setup | — | — | 436 | **50** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 Easy | — | — | 367 | **47** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [affaan-m/ECC](https://github.com/affaan-m/ECC), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [yetone/magpie](https://github.com/yetone/magpie), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [yc-software/qm](https://github.com/yc-software/qm) *(+17 more)*

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

- Stars: **73,682** (~398.3/day lifetime average)
- Health score: **89/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **17,006** (~160.4/day lifetime average)
- Health score: **83/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [openai/codex-security](https://github.com/openai/codex-security)

> @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code.

**Core problems it solves**

- **Model / provider routing**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install @openai/codex-security`
- Some setup. install via npx one-liner; needs npm install/build; configure API key configuration, sign-in required

**Facts**

- Stars: **10,995** (~129.3/day lifetime average)
- Health score: **81/100**
- Documentation score: **40/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Codex

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

- Stars: **9,298** (~105.7/day lifetime average)
- Health score: **80/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

#### [trailhq/Graft](https://github.com/trailhq/Graft)

> You correct it, and by the next session it has forgotten.

**Core problems it solves**

- **Model / provider routing** — *mpatible endpoint, anthropic for the native API, or litellm / orcarouter for a gateway that speaks the OpenAI-compatible format), your GRAFTAPIKEY, G…*
- **API gateway / proxy** — *graft is vendor-neutral: set GRAFTPROVIDER (openai for any OpenAI-compatible endpoint, anthropic for the native API, or litellm / orcarouter for a ga…*
- **Billing & metering**
- **Skills & plugins** — *gents get a marker-fenced Graft section in their shared instruction file — AGENTS.md (Codex, OpenCode and other CLIs that read it), GEMINI.md, .githu…*
- **Agent runtime** — *### Turbocharge Claude Code, Cursor, Codex, Gemini & every coding agent: faster, cheaper, with contextual understanding specific to your codebase.*
- **MCP support** — *d artifact.** graft build writes graft/ and adds it to .gitignore — it's a regenerable local cache, like nodemodules.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g @nanonets/graft   # install the CLI, once`
- Platforms mentioned: Linux
- Some setup. install via npx one-liner, global npm install; needs git clone (build from source), npm install/build; configure config.json/yaml/toml, database dependency

**Facts**

- Stars: **9,660** (~100.6/day lifetime average)
- Health score: **79/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. Account switcher & usage tracking — See Claude and Codex usage and rate-limit resets, and hot-swap accounts without re… | 🟢 Turnkey · OOTB | ✅ | ✅ | 86.9k (+426/d) | **92** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. AndroidWorld Results: 99%+ task completion on Google Research's AndroidWorld benchmark (100+ multi-step… | 🟡 Some setup | — | — | 11.1k 🚀 +205/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. 🤖 Claude Code, Cursor, Codex, Gemini CLI, Antigravity, Copilot CLI, M… | 🟢 Easy | — | — | 3.9k 🚀 +436/d | **83** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Left your desk? The same sessions are Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24k (+54/d) | **71** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. Best with Opus 4.8. The skill is a long, demanding design brief; the stronger the model, the better the… | 🟢 Turnkey · OOTB | ✅ | — | 4.3k (+35/d) | **67** |
| ✅ **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 一个适配 Claude Code / Codex 等 Agent 环境的图文卡片技能,用于从文章、文案、截图、产品笔记、字幕、照片或用户视频生成小红书 / Rednote 图文组图、Live Photo 动态卡与公众号 21:9 + 1:1 封面对。 📐 3 个画板尺寸:.poster.xhs 1080×1440(小红书 3:4)、.poster.wide 2100×900(公众号 21:9)、.poster.square 1080×… | 🟢 Easy | — | — | 7.4k (+56/d) | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.3k 🚀 +37/d | **60** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | A professional dashboard to track and visualize Claude Code, Cursor, and Codex agent sessions, tool usage, conversation history, cost, and subagent orchestration in real time. Tray icon — always-on status surface (macOS… | 🟡 Some setup | — | — | 1k | **55** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Gunshi downgraded Opus → Sonnet 4.6. All Ashigaru default to Sonnet 4.6. One YAML line change, no restarts requi… Agent self-watch + escalatio… | 🟡 Some setup | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 547 🚀 +5/d | **51** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [getpaseo/paseo](https://github.com/getpaseo/paseo), [nexu-io/html-anything](https://github.com/nexu-io/html-anything), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)

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
- **Parallel execution**
- **Workspace isolation** — *agent finishes and send follow-ups from anywhere.*
- **Usage analytics**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `brew install --cask stablyai/orca/orca`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via Homebrew install, native installer / package; GUI application

**Facts**

- Stars: **86,867** (~425.8/day lifetime average)
- Health score: **92/100**
- Documentation score: **52/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

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

- Stars: **11,084** (~205.3/day lifetime average)
- Health score: **83/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)

> A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions.

**Core problems it solves**

- **Automatic failover** — *e permission requests show up with Allow / Deny / Always; AskUserQuestion prompts show the choices right in the notch (single or multi-select, up to…*
- **Remote control**
- **Mobile access** — *your macOS Keychain, Windows Credential Manager or Linux Secret Service (GNOME Keyring, KWallet).*
- **Model / provider routing** — *p to the right terminal — open the exact terminal window of a session (macOS).*
- **Agent runtime**
- **Security & isolation** — *See what Claude is editing, live in the notch: each file modification shows the file name and +N −M counts in the ticker, tap to read the full diff*
- **GUI / desktop app** — *out as a beta: download it from Coucou for Linux 0.1.1 (beta), x8664 only for now.*
- **Notifications** — *your iPhone's Lock Screen and Dynamic Island with the agent's state, then comes back to the notch when you unlock.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install xcodegen`
- Platforms mentioned: macOS, Windows, Linux, iOS
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, database dependency; one-click setup

**Facts**

- Stars: **3,920** (~435.6/day lifetime average)
- Health score: **83/100**
- Documentation score: **59/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [slopus/happy](https://github.com/slopus/happy)

> Multi-provider within one session.

**Core problems it solves**

- **Remote control** — *lopus/slopus.github.io The website and docs at happy.engineering*
- **Mobile access** — *Happy adds a harness, not another bill.*
- **Multi-agent orchestration**
- **Model / provider routing** — *.com/user-attachments/assets/b3580704-f9e0-441e-80be-3f83f6a08ab5*
- **Security & isolation**
- **GUI / desktop app** — *Android, web), the original CLI, and the relay server*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `npm install -g happy`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via global npm install; needs npm install/build; configure sign-in required; GUI application

**Facts**

- Stars: **24,042** (~53.9/day lifetime average)
- Health score: **71/100**
- Documentation score: **29/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex
- *Why it is seeded: Drive Claude Code / Codex from a phone with end-to-end encryption.*

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

- Stars: **4,258** (~34.9/day lifetime average)
- Health score: **67/100**
- Documentation score: **61/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-23
- Works with: Claude Code, Codex, Cursor, Copilot, Cline / Roo

</details>

## Quota

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。不用 API Key、不搞逆向代理——官方网页 + 只读 MCP 桥接。 Knowing the URL grants nothing: the public MCP endpoint requires OAuth 2.1 | 🔴 Involved | — | — | 7.1k 🚀 +177/d | **78** |
| 🏆 **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 3.2k 🚀 +80/d | **78** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 9.2k 🚀 +77/d | **77** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 让 AI 在真实项目中规划、执行、验证并交付。 | 🟢 Easy | — | ✅ | 6.3k (+45/d) | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | AI 短剧制作的 skill 集合：从一本小说到直接喂生成管线的制作素材——拆角色、排大纲、出场景与道具设定、写剧本、切分镜。给 AI 编码 agent 用，Claude Code 和 codex 都能跑。 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 | 🟡 Some setup | — | — | 4.2k 🚀 +68/d | **64** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | orchestrator：Node 26 串行 853 项：852 通过、1 项 Windows ACL 专项跳过；类型检查通过。历史并发测试的等待超时记录仍保留，不以串行结果抹掉。 desktop：84/84，类型检查与生产构建通过；Python（计算库、回测、数据脚本）：754/754。 | 🟢 Easy | — | — | 2.6k 🚀 +28/d | **64** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k (+13/d) | **59** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 2.4k 🚀 +44/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | ✅ 三画幅封面一次出：同一个 coverLayout 出 4:3（1440×1080）／ 3:4（1080×1440）／ 9:16（1080×1920 抖音，内容压在中央安全区），标题 ≤2 行、钩子行自动马克笔高亮 github-trending-wan: v1.0.0 (2026-04-08) - 初始版本，GitHub Trending Top 5 中文信息图海报生成器，抓取热门项目→翻译中文摘要→生成 Wan 2.7 海报 P… | 🟡 Some setup | — | — | 282 | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 406 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 10-06 系统沙箱：AI 跑的命令和脚本在 macOS、Windows 上读不到 Key 和账本、改不了应用；设置 → 安全 能关，每条多花 7–16 毫秒 10-07 闲着更省电：没任务、没人用时，服务每秒醒来从约 40 次降到 2 次；窗口不在前台也不再盯卡顿 | 🟡 Some setup | — | — | 275 🚀 +5/d | **50** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 给做 SEO 和独立开发的人用的 Agent Skills。建站、选词、发外链、查数据、复盘迭代，一整条链路都在这个仓库里，装完就能跑。 aaron-he-zhu/seo-geo-claude-skills（Apache-2.0）——backlink/references/ 下的质量评分矩阵、分析模板与外联模板。 | 🟢 Easy | — | — | 208 | **50** |

**Also does this:** [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API), [cita-777/metapi](https://github.com/cita-777/metapi), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)

> 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。不用 API Key、不搞逆向代理——官方网页 + 只读 MCP 桥接。

**Core problems it solves**

- **Quota & usage management** — *ouble? First ask Codex to “Update Codex with ChatGPT” and try again.*
- **Skills & plugins**
- **Agent runtime** — *One-paste install · 一段话安装*
- **MCP support** — *e latest version resolves most known issues.*

**Getting it running**

- Setup: 🔴 **Involved** (friction 63/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Web
- Involved setup. needs pnpm install/build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **7,089** (~177.2/day lifetime average)
- Health score: **78/100**
- Documentation score: **50/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-01
- Works with: Codex

#### [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)

> An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔…

**Core problems it solves**

- **Quota & usage management** — *平台适配的成品直接到对应平台，再通过**归因**分析表现并把有效经验沉淀回账号画像。*
- **Multi-provider aggregation**
- **API gateway / proxy** — *装 OpenClaw，并创建独立的 easel profile，不覆盖用户已有的 ~/.openclaw/。*
- **Memory & context**
- **Skills & plugins** — *布与归因** 发布质量门禁、敏感与版权风险检查、平台搜索优化、发布 Checklist、多平台格式适配；小红书、抖音、快手、知乎、B 站、微信视频号、微信公众号登录与发布；内容日历回写、账号数据、评论洞察、内容复盘、ROI 与画像记忆*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, native installer / package; needs git clone (build from source); configure API key configuration; Chinese: beginner/one-click framing

**Facts**

- Stars: **3,190** (~79.8/day lifetime average)
- Health score: **78/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex

#### [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)

> 一个真正适合职场人的 PPT Skill。把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。

**Core problems it solves**

- **Quota & usage management** — *用这个 skill 生成 PPT 格式的文件"，从提示词一步到 PPTX。*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx dashi-ppt-skill@latest`
- Turnkey. install via npx one-liner; Chinese: beginner/one-click framing

**Facts**

- Stars: **9,216** (~77.5/day lifetime average)
- Health score: **77/100**
- Documentation score: **57/100**
- License: AGPL-3.0
- Language: JavaScript
- Last push: 2026-09-12
- Works with: Claude Code, Codex, Cursor

#### [KunAgent/Kun](https://github.com/KunAgent/Kun)

> 让 AI 在真实项目中规划、执行、验证并交付。

**Core problems it solves**

- **Quota & usage management** — *，提示、附件和任务上下文会发送给所选 Provider；使用前请确认该服务的数据政策。*
- **Workspace isolation** — *建一个房间，为成员选择 Agent 档案、模型和授权的本地仓库，然后用 IM 式的私聊或群聊推进工作。*
- **MCP support** — *arkdown，预览、引用和分析 PDF / Office 文档，分析电子表格，并从大纲创建演示文稿；Office 文件保持只读。*
- **Security & isolation** — *esign 画布；Work 面向写作、资料整理、文档分析和演示产出；Rooms 把多个 Agent 放进同一个协作空间，用私聊和群聊完成讨论、分工、执行与评审。*
- **Self-hostable**
- **GUI / desktop app** — *是把 AI 从“回答问题”推进到“完成工作”的本地优先工作台。*
- **Cross-agent support** — *Mentions Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via native installer / package; needs git clone (build from source), npm install/build; GUI application

**Facts**

- Stars: **6,317** (~45.5/day lifetime average)
- Health score: **67/100**
- Documentation score: **41/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Codex, Cursor

#### [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)

> AI 短剧制作的 skill 集合：从一本小说到直接喂生成管线的制作素材——拆角色、排大纲、出场景与道具设定、写剧本、切分镜。给 AI 编码 agent 用，Claude Code 和 codex 都能跑。

**Core problems it solves**

- **Quota & usage management** — *laude Code 还是 codex，把所有 skill 软链过去——git pull 之后立刻生效，不用重装。*
- **Skills & plugins** — *dex CLI 可选 只是一个能跑这些 skill 的运行环境，跟 Claude Code 等价。*
- **Agent runtime**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Linux
- Some setup. needs git clone (build from source); configure API key configuration

**Facts**

- Stars: **4,218** (~68.0/day lifetime average)
- Health score: **64/100**
- Documentation score: **41/100**
- License: Apache-2.0
- Language: JavaScript
- Last push: 2026-09-26
- Works with: Claude Code, Codex

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. Notes — Aggregation doesn't provide failover; Claude Code requires version 2.1.2… | 🟢 Easy | — | — | 140.7k (+328/d) | **93** |
| ✅ **[HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)** | 同花顺金融数据服务（hithink-finance） 是由同花顺官方提供和维护的 A 股金融数据服务，面向 AI Agent、量化研究者和应用开发者。 | 🟢 Easy | — | — | 4.1k 🚀 +34/d | **64** |
| ✅ **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 在同一页面编辑 Base URL、API Key、Model、Wire API 和完整 TOML | 🟢 Easy | — | — | 4.1k 🚀 +43/d | **63** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Claude Code / Codex 项目导入：只读发现项目和历史会话，预览后导入 Harness 工作区；敏感信息脱敏，历史工具调用不会重新执行。 模型接入更省步骤：bai 登录后优先选择真实目录中的 deepseek-flash，定期更新目录；缺少授权或密钥失效时引导浏览器登录，不自动充值、付费或重发消息。第三方 API 仍可独立接入。 | 🟢 Turnkey · OOTB | ✅ | — | 777 🚀 +14/d | **58** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 722 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 内置完整 RAG：文档加载（可选 Tika 解析 PDF/Word/Excel，或 MinerU 云端解析扫描件/公式/复杂版面为 Markdown）、切块、八大向量库适配（Pinecone /… | 🟢 Turnkey | — | — | 434 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. Daemon (:8081) - registers the machine and manages agent subprocesses. | 🟡 Some setup | — | — | 697 🚀 +6/d | **49** |

**Also does this:** [loopx-project/loopx](https://github.com/loopx-project/loopx)

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

- Stars: **140,685** (~327.9/day lifetime average)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

#### [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)

> 同花顺金融数据服务（hithink-finance） 是由同花顺官方提供和维护的 A 股金融数据服务，面向 AI Agent、量化研究者和应用开发者。

**Core problems it solves**

- **Quota & usage management**
- **Multi-provider aggregation** — *数据服务（hithink-finance） 是由同花顺官方提供和维护的 A 股金融数据服务，面向 AI Agent、量化研究者和应用开发者。*
- **Session persistence** — *码一次后完成 Key 签发、安全交接、用户级环境变量、credentials.env、CLI 凭据库和真实请求验证；其他场景可按同一 runbook 逐步操作。*
- **MCP support** — *公募基金、公开期货期权和特色数据，并通过 REST API、MCP、CLI、Python SDK、本地 DuckDB 或 Agent Skill 接入现有工作流。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 19/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add HiThink-Tech/Financial-API --skill hithink-finance -g --yes`
- Easy. install via npx one-liner, pip install; needs npm install/build; configure API key configuration, .env file

**Facts**

- Stars: **4,092** (~34.1/day lifetime average)
- Health score: **64/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-22
- Works with: Cursor

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

- Stars: **4,091** (~43.1/day lifetime average)
- Health score: **63/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-06
- Works with: Codex

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

- Stars: **777** (~14.4/day lifetime average)
- Health score: **58/100**
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

- Stars: **722** (~3.1/day lifetime average)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-02
- Works with: Claude Code, Cursor

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. 🎯 Free tier: 60 requests/min and 1,000 requests/day with personal Google | 🟢 Easy | — | — | 107.2k (+200/d) | **91** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 43.4k (+148/d) | **85** |
| ✅ **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.1k 🚀 +166/d | **74** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 5.4k 🚀 +57/d | **73** |
| 🔹 **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file… | 🔴 Involved | — | — | 3.7k (+26/d) | **59** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 776 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. 📊 Server-side aggregation — group, sum, and count without pulling raw rows | 🟡 Some setup | — | — | 398 | **50** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 411 | **46** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [decolua/9router](https://github.com/decolua/9router), [trailhq/Graft](https://github.com/trailhq/Graft), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [cita-777/metapi](https://github.com/cita-777/metapi), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine), [cwinvestments/memstack](https://github.com/cwinvestments/memstack), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth) *(+5 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

> Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal.

**Core problems it solves**

- **Model / provider routing**
- **Billing & metering** — *pers who need specific model control or paid tier access*
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

- Stars: **107,242** (~199.7/day lifetime average)
- Health score: **91/100**
- Documentation score: **69/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Gemini CLI
- *Why it is seeded: Gemini's terminal agent, generous free tier.*

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

- Stars: **43,392** (~148.1/day lifetime average)
- Health score: **85/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [trycompai/crm](https://github.com/trycompai/crm)

> Comp AI CRM is an open source, CRM designed for AI agents.

**Core problems it solves**

- **Model / provider routing** — *ur own identity provider on*
- **Billing & metering**
- **Self-hostable**

**Getting it running**

- Setup: 🔴 **Involved** (friction 90/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker compose up -d          # Postgres on :5432`
- Platforms mentioned: Linux, Web
- Involved setup. needs docker compose up, git clone (build from source); configure environment variables, OAuth login flow

**Facts**

- Stars: **11,116** (~165.9/day lifetime average)
- Health score: **74/100**
- Documentation score: **48/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-11

#### [aipoch/open-science](https://github.com/aipoch/open-science)

> AI research workbench for reproducible science — open-source, local-first, and model-agnostic.

**Core problems it solves**

- **Remote control** — *greatly appreciate a star on GitHub.*
- **Model / provider routing** — *overview - Node.js quick start and package entry point*
- **Billing & metering** — *### Why does the model connection test fail? A: Check the API Key for missing characters or spaces, verify the Base URL and region, use the provider'…*
- **Skills & plugins** — *nabled” refers to the skill, not to the availability of every registered host.*
- **MCP support** — *Marketplace contributions are published after review; local imports do not publish skills.*
- **Security & isolation**
- **GUI / desktop app** — *date active remote sessions.*
- **Cross-agent support** — *Mentions Claude Code, Codex, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install --cask open-science`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **5,448** (~56.8/day lifetime average)
- Health score: **73/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode

#### [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)

> Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file storage, RAG, durab…

**Core problems it solves**

- **Multi-agent orchestration** — *— full production-shaped apps: butterSupport, butterbaseCRM.*
- **Billing & metering** — *ers, lease-based quota enforcement, and ops dashboards (those live in a private repo that consumes this one as a submodule).*
- **Memory & context** — *AI-native, open-source backend-as-a-service.*
- **Skills & plugins** — *QuotaEnforcer, and RouterAdapter interfaces in packages/shared.*
- **MCP support** — *AI-native, open-source backend-as-a-service.*
- **Security & isolation** — *endpoints (/auto-api), and migrations.*
- **Self-hostable** — *AI-native, open-source backend-as-a-service.*
- **Notifications** — *, GitHub, Apple, X, …), JWT tuning, post-login hooks, service keys (/auth, /oauth-config, /api-keys).*

**Getting it running**

- Setup: 🔴 **Involved** (friction 67/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -sf http://localhost:4000/health/ready`
- Platforms mentioned: Linux, Web
- Involved setup. install via npx one-liner; needs docker compose up, git clone (build from source); configure API key configuration, OAuth login flow

**Facts**

- Stars: **3,686** (~26.3/day lifetime average)
- Health score: **59/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-06
- Works with: Claude Code

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. A LoopX-attributed Engine refactor is continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 Some setup | — | — | 6.2k (+48/d) | **71** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. Cline / Roo Code / Zoo Code / Kilo Code (VS Code extension + CLI) | 🟢 Turnkey · OOTB | ✅ | — | 222 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons,… | 🟡 Some setup | — | — | 722 | **44** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)

<details>
<summary><b>Why these tools — 4 detailed breakdowns</b></summary>

#### [loopx-project/loopx](https://github.com/loopx-project/loopx)

> Give your agents a goal.

**Core problems it solves**

- **Quota & usage management**
- **Mobile access** — *r Manager group conversations, LoopX keeps message visibility separate from*
- **Multi-agent orchestration** — *goals, steer work and resolve decisions.*
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

- Stars: **6,171** (~47.8/day lifetime average)
- Health score: **71/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-07
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

- Stars: **5,886** (~5.1/day lifetime average)
- Health score: **51/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

#### [Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)

> We've released Piebald, the ultimate agentic AI developer experience.

**Core problems it solves**

- **Usage analytics**
- **Agent runtime** — *e / Zoo Code / Kilo Code (VS Code extension + CLI)*
- **MCP support** — *epository to show your support!** ⭐*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `winget install --id LLVM.LLVM`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via winget install, download a release binary

**Facts**

- Stars: **222** (~0.5/day lifetime average)
- Health score: **50/100**
- Documentation score: **32/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-04
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot, Cline / Roo

#### [nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)

> A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons, and a rule-based ti…

**Core problems it solves**

- **Automatic failover**
- **Multi-agent orchestration**
- **Parallel execution** — *000 python3 cli.py dashboard.*
- **Usage analytics**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via winget install; needs git clone (build from source); configure environment variables, database dependency

**Facts**

- Stars: **722** (~4.2/day lifetime average)
- Health score: **44/100**
- Documentation score: **54/100**
- License: MIT
- Language: Python
- Last push: 2026-04-20
- Works with: Claude Code

</details>

## Voice

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. Optionally pai… | 🟡 Some setup | — | — | 135.6k (+649/d) | **90** |
| 🏆 **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.6k 🚀 +114/d | **84** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 8.5k (+66/d) | **75** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [pax-beehive/paxm](https://github.com/pax-beehive/paxm)

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> When I heard Karpathy say this, I wanted to find out how.

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *the cause and re-verify before committing.*
- **Parallel execution** — *etext patterns depending on whether it's a landing page, dashboard, form, or card layout.*
- **Workspace isolation** — *hand, and gstack-uninstall*
- **Model / provider routing** — *deterministic aside repl scripts.*
- **Usage analytics** — *try flows through validated edge functions that enforce schema checks, event type allowlists, and field length limits.*
- **Session persistence** — *Browse my kid's school parent portal and add all the other parents' names, phone numbers, and photos to my Google Contacts." Two ways to get authenti…*
- **Memory & context** — *Come work at YC — ycombinator.com/software*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Some setup. install via native installer / package; needs git clone (build from source), go build; configure API key configuration, config file; one-click setup

**Facts**

- Stars: **135,636** (~649.0/day lifetime average)
- Health score: **90/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)

> MiMoCode is a terminal-native AI coding assistant.

**Core problems it solves**

- **Multi-agent orchestration** — *emory (MEMORY.md) — persistent project knowledge, rules, and architecture decisions*
- **Parallel execution** — *terminal-native intelligence to desktop workflows.*
- **Workspace isolation**
- **Model / provider routing** — *o/Plus) — OpenAI OAuth login*
- **API gateway / proxy** — *separates the provider ID from the model ID.*
- **Session persistence** — *omatically by the checkpoint-writer subagent*
- **Memory & context** — *e: Where Models and Agents Co-Evolve*
- **Skills & plugins** — *ble/Sol-class), which internalize most of the workflow and work best from one compact contract.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://mimo.xiaomi.com/install | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, curl | sh installer; needs npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **13,603** (~114.3/day lifetime average)
- Health score: **84/100**
- Documentation score: **63/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-03
- Works with: Claude Code, Codex, OpenCode, Cursor, Cline / Roo

#### [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)

> Free, open source and performant.

**Core problems it solves**

- **Multi-agent orchestration** — *Everything is visible: you watch avatars move, envelopes fly, and the live terminal stream;*
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

- Stars: **8,548** (~66.3/day lifetime average)
- Health score: **75/100**
- Documentation score: **74/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Sharing

*Quota sharing / splitting*

A subscription's capacity is larger than one person needs; share it safely with others.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 🤖 Agent-native, model-agnostic. We don't ship an agent. The claude / codex / cursor-agent / copilot / hermes / kimi already on your PATH are the design engine. Swap with one click. Hand off to engineering. The artifact… | 🟢 Easy | — | — | 99.8k (+616/d) | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 556 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. Merged upstream sub2api v0.2.4 (519 commits / 876 files) and unified the frontend and backend versions at 1.0.4. | 🔴 Involved | — | — | 241 | **42** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [decolua/9router](https://github.com/decolua/9router), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

#### [nexu-io/open-design](https://github.com/nexu-io/open-design)

> OpenDesign is a collaborative design agent workspace.

**Core problems it solves**

- **Mobile access** — *read your DESIGN.md and render in a sandboxed iframe.*
- **Model / provider routing** — *No CLI installed? The BYOK proxy at POST /api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream gives you the same loop (no process spaw…*
- **API gateway / proxy** — *udio}/stream gives you the same loop (no process spawn) — paste baseUrl + apiKey + model, with presets for OpenAI, Atlas Cloud, Anthropic, Azure Open…*
- **Quota sharing / splitting** — *## What is OpenDesign OpenDesign is a collaborative design agent workspace.*
- **Billing & metering** — *0+ functional skills · rendering templates · 277 plugins*
- **Session persistence** — *ive runtime adapters for agents that OD launches directly.*
- **Skills & plugins** — *eedback, and let your agent refine it in the same project.*
- **Agent runtime** — *ais · 简体中文 · 繁體中文 · 한국어 · 日本語 · العربية · Русский · Українська · Türkçe · ภาษาไทย*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://open-design.ai/install.sh | sh -s <agent>`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Easy. install via npx one-liner, curl | sh installer; needs docker compose up, git clone (build from source); configure database dependency, database migration; one-click setup

**Facts**

- Stars: **99,811** (~616.1/day lifetime average)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-07
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

- Stars: **556** (~1.1/day lifetime average)
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

- Stars: **241** (~2.3/day lifetime average)
- Health score: **42/100**
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Teams | Accounts, Voice |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Sharing | Desktop UI, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Accounts, Billing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Accounts, Isolation & Parallelism |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Billing | Sessions & Memory |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Voice | Sessions & Memory, Skills |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Isolation & Parallelism | Model Routing, Sessions & Memory |
| **[openai/codex](https://github.com/openai/codex)** | Accounts | Desktop UI |
| **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | Skills | Desktop UI, Model Routing |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | MCP & Failover | Model Routing, Skills |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Isolation & Parallelism | Analytics, Mobile |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Model Routing | Desktop UI |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP & Failover | Desktop UI, Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Accounts, Sharing |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation & Parallelism | Desktop UI, Skills |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP & Failover | Billing, Model Routing |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Accounts | Desktop UI, Model Routing |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Voice | Isolation & Parallelism, MCP & Failover |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Skills |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Accounts | Model Routing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | MCP & Failover |
| **[google/artemis](https://github.com/google/artemis)** | Mobile | Skills |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | MCP & Failover | Voice |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Desktop UI, Model Routing |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Isolation & Parallelism | Desktop UI, Skills |
| **[decolua/9router](https://github.com/decolua/9router)** | Accounts | Billing, Sharing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | MCP & Failover | Sessions & Memory, Skills |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Teams | Mobile, Model Routing |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Desktop UI, Model Routing |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams | Desktop UI, Model Routing |
| **[trailhq/Graft](https://github.com/trailhq/Graft)** | Model Routing | Billing, Desktop UI |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Quota | Desktop UI |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Skills | Desktop UI |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Quota | Desktop UI |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Isolation & Parallelism | Billing, MCP & Failover |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Accounts | Model Routing, Quota |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Voice | Desktop UI, Sessions & Memory |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Isolation & Parallelism | MCP & Failover, Mobile |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | Desktop UI, MCP & Failover |
| **[pacifio/atlas](https://github.com/pacifio/atlas)** | Sessions & Memory | Desktop UI |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Providers, Teams |
| **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Isolation & Parallelism | Model Routing, Skills |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | MCP & Failover, Model Routing |
| **[nexu-io/html-anything](https://github.com/nexu-io/html-anything)** | Desktop UI | Mobile, Skills |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | Sessions & Memory | MCP & Failover |
| **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Teams | Desktop UI, Skills |
| **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | Quota | MCP & Failover |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Desktop UI |
| **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Isolation & Parallelism | Model Routing |
| **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | Isolation & Parallelism | Desktop UI, Skills |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | MCP & Failover | Model Routing, Skills |
| **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Quota | Desktop UI |
| **[HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)** | Providers | Quota |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Quota | MCP & Failover, Skills |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Analytics, Billing |
| **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Isolation & Parallelism | Desktop UI, Skills |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation & Parallelism | MCP & Failover, Skills |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Billing | MCP & Failover, Skills |
| **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills | Desktop UI |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Skills | Desktop UI |
| **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Isolation & Parallelism | Desktop UI, Model Routing |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Sessions & Memory | Desktop UI, Model Routing |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Billing, Mobile |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams | MCP & Failover, Skills |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Skills | Desktop UI |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Skills | Desktop UI |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Isolation & Parallelism | Desktop UI, Skills |
| **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | Skills | Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | MCP & Failover | Isolation & Parallelism, Sessions & Memory |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation & Parallelism | MCP & Failover, Voice |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Desktop UI | Model Routing, Skills |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Skills | Desktop UI |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Mobile | MCP & Failover, Sessions & Memory |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Isolation & Parallelism | Desktop UI, Mobile |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Quota | Mobile, Skills |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Accounts | Billing, Quota |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation & Parallelism | MCP & Failover, Skills |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation & Parallelism | Desktop UI, Skills |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Teams | Isolation & Parallelism, MCP & Failover |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | MCP & Failover |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | MCP & Failover, Sessions & Memory |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | MCP & Failover | Model Routing, Sessions & Memory |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Teams | Billing, Voice |
| **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Teams | Accounts, Model Routing |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Isolation & Parallelism, Voice |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Isolation & Parallelism, Skills |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Sessions & Memory | Isolation & Parallelism, Mobile |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Sessions & Memory | Desktop UI, Model Routing |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Skills | Desktop UI |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Sessions & Memory | Desktop UI |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | MCP & Failover, Skills |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Sessions & Memory | Billing |
| **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | Isolation & Parallelism | Billing, Skills |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Model Routing | Skills |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Accounts | Billing, Sessions & Memory |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Sessions & Memory | Skills |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Desktop UI |
| **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Sessions & Memory | Model Routing |
| **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Accounts | Billing, Model Routing |
| **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | Sessions & Memory | Billing, Model Routing |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Model Routing | Desktop UI, Sessions & Memory |
| **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | Quota | MCP & Failover, Sharing |
| **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | Analytics | Billing, Desktop UI |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Quota | Accounts, Sharing |
| **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | Desktop UI | Skills |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Isolation & Parallelism, Skills |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Sharing | Model Routing, Quota |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | MCP & Failover | Sessions & Memory, Voice |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Isolation & Parallelism | MCP & Failover, Teams |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Skills | Billing, Desktop UI |
| **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | Accounts | Model Routing, Sharing |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Teams | Billing, MCP & Failover |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Teams | Isolation & Parallelism |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Isolation & Parallelism | Desktop UI |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Sessions & Memory | Desktop UI |
| **[JimLiu/baocut](https://github.com/JimLiu/baocut)** | Skills | Desktop UI |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Sessions & Memory | MCP & Failover |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Sharing | Accounts, Model Routing |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | Sessions & Memory | Skills |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 62% | 0.04x the stars (5,667 vs 140,685) |

<details><summary><b>yetone/magpie vs farion1231/cc-switch</b></summary>

Both manage multiple accounts and providers for Claude Code and Codex, and magpie additionally routes other models through the same agent loop.

**Not covered:** Billing & metering, Parallel execution, Multi-provider aggregation, Session persistence, Skills & plugins

</details>

---

## 🪦 The Graveyard

There is always a dark horse. When a newer tool covers **every** capability of an incumbent, matches its traction and is no harder to set up, the incumbent is retired here rather than quietly left in the list. Full rules: [docs/SUPERSEDE.md](docs/SUPERSEDE.md).

### Recorded eliminations

| Retired | Replaced by | Why it lost | Source |
| --- | --- | --- | --- |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.92x the stars (7,070 vs 713) | 🤖 auto (high) |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/agi-is-going-to-arrive/memory-palace)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 93.30x the stars (29,204 vs 313) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 57.16x the stars (18,691 vs 327) | 🤖 auto (high) |
| **[AndrewDryga/emisar](https://github.com/andrewdryga/emisar)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 13.92x the stars (4,691 vs 337) | 🤖 auto (high) |
| **[Arvincreator/project-golem](https://github.com/arvincreator/project-golem)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 45.70x the stars (29,204 vs 639) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 6.36x the stars (2,417 vs 380) | 🤖 auto (high) |
| **[LerianStudio/ring](https://github.com/lerianstudio/ring)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 11.14x the stars (2,417 vs 217) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[pacifio/atlas](https://github.com/pacifio/atlas)** | 17.99x the stars (9,263 vs 515) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 866.27x the stars (274,608 vs 317) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 63.85x the stars (274,608 vs 4,301) | 🤖 auto (high) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 61.75x the stars (274,608 vs 4,447) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.17x the stars (33,351 vs 922) | 🤖 auto (high) |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 58.10x the stars (33,351 vs 574) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 96.67x the stars (33,351 vs 345) | 🤖 auto (high) |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 5.92x the stars (29,204 vs 4,930) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 20.09x the stars (98,271 vs 4,891) | 🤖 auto (high) |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 65.63x the stars (29,204 vs 445) | 🤖 auto (high) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.97x the stars (13,603 vs 389) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 23.62x the stars (7,628 vs 323) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 6.05x the stars (7,628 vs 1,261) | 🤖 auto (high) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 22.49x the stars (5,667 vs 252) | 🤖 auto (high) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1144.20x the stars (274,608 vs 240) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 24.26x the stars (11,280 vs 465) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 574.96x the stars (158,113 vs 275) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.16x the stars (33,351 vs 273) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 58.18x the stars (29,204 vs 502) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 23.13x the stars (8,836 vs 382) | 🤖 auto (high) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 26.49x the stars (33,351 vs 1,259) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 8.66x the stars (2,417 vs 279) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 78.29x the stars (29,204 vs 373) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 143.56x the stars (140,685 vs 980) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[EverMind-AI/Raven](https://github.com/evermind-ai/raven)** | 9.66x the stars (5,257 vs 544) | 🤖 auto (high) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 399.14x the stars (274,608 vs 688) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[FrancyJGLisboa/agent-skills-platform](https://github.com/francyjglisboa/agent-skills-platform)** | 8.17x the stars (2,403 vs 294) | 🤖 auto (high) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[trailhq/Graft](https://github.com/trailhq/graft)** | 21.14x the stars (9,660 vs 457) | 🤖 auto (medium) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 41.31x the stars (98,271 vs 2,379) | 🤖 auto (medium) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 17.48x the stars (29,204 vs 1,671) | 🤖 auto (medium) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[trailhq/Graft](https://github.com/trailhq/graft)** | 15.51x the stars (9,660 vs 623) | 🤖 auto (medium) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.80x the stars (7,628 vs 2,725) | 🤖 auto (high) |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 9.02x the stars (2,083 vs 231) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 6.90x the stars (44,160 vs 6,400) | 🤖 auto (medium) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 452.40x the stars (274,608 vs 607) | 🤖 auto (medium) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.85x the stars (804 vs 282) | 🤖 auto (high) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 10.33x the stars (4,691 vs 454) | 🤖 auto (medium) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 579.34x the stars (274,608 vs 474) | 🤖 auto (medium) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.69x the stars (7,628 vs 2,066) | 🤖 auto (high) |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 103.93x the stars (29,204 vs 281) | 🤖 auto (medium) |
| **[AI-QL/tuui](https://github.com/ai-ql/tuui)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 25.28x the stars (29,204 vs 1,155) | 🤖 auto (medium) |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 6.87x the stars (274,608 vs 39,997) | 🤖 auto (medium) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.70x the stars (33,351 vs 3,833) | 🤖 auto (high) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.06x the stars (7,628 vs 3,708) | 🤖 auto (medium) |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/fuxi)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 8.72x the stars (29,204 vs 3,351) | 🤖 auto (medium) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 4.90x the stars (29,204 vs 5,955) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.26x the stars (804 vs 355) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 2.86x the stars (14,892 vs 5,208) | 🤖 auto (medium) |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 6.26x the stars (29,204 vs 4,667) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.63x the stars (804 vs 306) | 🤖 auto (high) |
| **[MoonshotAI/kimi-code](https://github.com/moonshotai/kimi-code)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 4.28x the stars (33,351 vs 7,789) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.33x the stars (1,423 vs 427) | 🤖 auto (medium) |
| **[yetone/cumora](https://github.com/yetone/cumora)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 2.70x the stars (10,643 vs 3,939) | 🤖 auto (high) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.47x the stars (1,423 vs 969) | 🤖 auto (medium) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.31x the stars (1,423 vs 1,090) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | mcp-failover | 40k | 🔻 Superseded | 6.87x the stars (274,608 vs 39,997) |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | isolation-parallelism | 7.8k | 🔻 Superseded | 4.28x the stars (33,351 vs 7,789) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.4k | 🔻 Superseded | 6.90x the stars (44,160 vs 6,400) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | mcp-failover | 6k | 🔻 Superseded | 4.90x the stars (29,204 vs 5,955) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | isolation-parallelism | 5.2k | 🔻 Superseded | 2.86x the stars (14,892 vs 5,208) |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | mcp-failover | 4.9k | 🔻 Superseded | 5.92x the stars (29,204 vs 4,930) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-parallelism | 4.9k | 🔻 Superseded | 20.09x the stars (98,271 vs 4,891) |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | mcp-failover | 4.7k | 🔻 Superseded | 6.26x the stars (29,204 vs 4,667) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | mcp-failover | 4.4k | 🔻 Superseded | 61.75x the stars (274,608 vs 4,447) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | mcp-failover | 4.3k | 🔻 Superseded | 63.85x the stars (274,608 vs 4,301) |
| **[yetone/cumora](https://github.com/yetone/cumora)** | teams | 3.9k | 🔻 Superseded | 2.70x the stars (10,643 vs 3,939) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | isolation-parallelism | 3.8k | 🔻 Superseded | 8.70x the stars (33,351 vs 3,833) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 Superseded | 2.06x the stars (7,628 vs 3,708) |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | mcp-failover | 3.4k | 🔻 Superseded | 8.72x the stars (29,204 vs 3,351) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 Superseded | 2.80x the stars (7,628 vs 2,725) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | isolation-parallelism | 2.4k | 🔻 Superseded | 41.31x the stars (98,271 vs 2,379) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 Superseded | 3.69x the stars (7,628 vs 2,066) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | mcp-failover | 1.7k | 🔻 Superseded | 17.48x the stars (29,204 vs 1,671) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 6.05x the stars (7,628 vs 1,261) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | isolation-parallelism | 1.3k | 🔻 Superseded | 26.49x the stars (33,351 vs 1,259) |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | mcp-failover | 1.2k | 🔻 Superseded | 25.28x the stars (29,204 vs 1,155) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | mobile | 1.1k | 🔻 Superseded | 1.31x the stars (1,423 vs 1,090) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers | 980 | 🔻 Superseded | 143.56x the stars (140,685 vs 980) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile | 969 | 🔻 Superseded | 1.47x the stars (1,423 vs 969) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-parallelism | 922 | 🔻 Superseded | 36.17x the stars (33,351 vs 922) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | sessions-memory | 713 | 🔻 Superseded | 9.92x the stars (7,070 vs 713) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | mcp-failover | 688 | 🔻 Superseded | 399.14x the stars (274,608 vs 688) |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | mcp-failover | 639 | 🔻 Superseded | 45.70x the stars (29,204 vs 639) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 623 | 🔻 Superseded | 15.51x the stars (9,660 vs 623) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | mcp-failover | 607 | 🔻 Superseded | 452.40x the stars (274,608 vs 607) |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | isolation-parallelism | 574 | 🔻 Superseded | 58.10x the stars (33,351 vs 574) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-parallelism | 544 | 🔻 Superseded | 9.66x the stars (5,257 vs 544) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | sessions-memory | 515 | 🔻 Superseded | 17.99x the stars (9,263 vs 515) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-failover | 502 | 🔻 Superseded | 58.18x the stars (29,204 vs 502) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | mcp-failover | 474 | 🔻 Superseded | 579.34x the stars (274,608 vs 474) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | mcp-failover | 465 | 🔻 Superseded | 24.26x the stars (11,280 vs 465) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 457 | 🔻 Superseded | 21.14x the stars (9,660 vs 457) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | mcp-failover | 454 | 🔻 Superseded | 10.33x the stars (4,691 vs 454) |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | mcp-failover | 445 | 🔻 Superseded | 65.63x the stars (29,204 vs 445) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 427 | 🔻 Superseded | 3.33x the stars (1,423 vs 427) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice | 389 | 🔻 Superseded | 34.97x the stars (13,603 vs 389) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | mcp-failover | 382 | 🔻 Superseded | 23.13x the stars (8,836 vs 382) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-parallelism | 380 | 🔻 Superseded | 6.36x the stars (2,417 vs 380) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | mcp-failover | 373 | 🔻 Superseded | 78.29x the stars (29,204 vs 373) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 355 | 🔻 Superseded | 2.26x the stars (804 vs 355) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | isolation-parallelism | 345 | 🔻 Superseded | 96.67x the stars (33,351 vs 345) |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | mcp-failover | 337 | 🔻 Superseded | 13.92x the stars (4,691 vs 337) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | accounts | 327 | 🔻 Superseded | 57.16x the stars (18,691 vs 327) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 323 | 🔻 Superseded | 23.62x the stars (7,628 vs 323) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | mcp-failover | 317 | 🔻 Superseded | 866.27x the stars (274,608 vs 317) |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | mcp-failover | 313 | 🔻 Superseded | 93.30x the stars (29,204 vs 313) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | skills | 306 | 🔻 Superseded | 2.63x the stars (804 vs 306) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills | 294 | 🔻 Superseded | 8.17x the stars (2,403 vs 294) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 Superseded | 2.85x the stars (804 vs 282) |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | mcp-failover | 281 | 🔻 Superseded | 103.93x the stars (29,204 vs 281) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | isolation-parallelism | 279 | 🔻 Superseded | 8.66x the stars (2,417 vs 279) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 275 | 🔻 Superseded | 574.96x the stars (158,113 vs 275) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | isolation-parallelism | 273 | 🔻 Superseded | 122.16x the stars (33,351 vs 273) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | accounts | 252 | 🔻 Superseded | 22.49x the stars (5,667 vs 252) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | mcp-failover | 240 | 🔻 Superseded | 1144.20x the stars (274,608 vs 240) |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | isolation-parallelism | 231 | 🔻 Superseded | 9.02x the stars (2,083 vs 231) |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | isolation-parallelism | 217 | 🔻 Superseded | 11.14x the stars (2,417 vs 217) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-07 16:31 UTC. 209 live tools · 129 candidates rejected by the quality gates.</sub>
