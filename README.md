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

**206 tools** across **14 categories** · **63 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-09 11:23 UTC**

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

- [Self-hosting & Security](#self-hosting-security) — 27 tools
- [Skills](#skills) — 33 tools
- [Isolation & Parallelism](#isolation-parallelism) — 18 tools
- [Mobile](#mobile) — 18 tools
- [Analytics](#analytics) — 23 tools
- [Teams](#teams) — 17 tools
- [Accounts](#accounts) — 13 tools
- [Agent Runtime & Desktop UI](#agent-runtime-desktop-ui) — 12 tools
- [Model Routing](#model-routing) — 11 tools
- [Billing](#billing) — 9 tools
- [Providers](#providers) — 8 tools
- [Quota](#quota) — 8 tools
- [Analytics](#analytics) — 6 tools
- [Sharing](#sharing) — 3 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Self-hosting & Security

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot uses .github/copilot-instructions.md instead) Available in release 2.2: guided package setup for Claud… | 🟡 Some setup | — | — | 275.6k (+1044/d) | **89** |
| 🏆 **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.3k 🚀 +317/d | **88** |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine | 🟢 Easy | — | — | 29.3k (+129/d) | **88** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 14.5k 🚀 +245/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 9.1k 🚀 +130/d | **85** |
| 🏆 **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 13.8k 🚀 +186/d | **84** |
| 🏆 **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17k 🚀 +158/d | **83** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. Routines: ask a Bot to do something on a schedule and it does, running as y… | 🟡 Some setup | — | — | 6.2k 🚀 +118/d | **83** |
| 🏆 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.3k 🚀 +102/d | **80** |
| 🏆 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | This one is invisible to anti-bots. | 🟢 Turnkey · OOTB | ✅ | — | 2.7k 🚀 +299/d | **80** |
| 🏆 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.4k (+94/d) | **79** |
| 🏆 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 3.2k 🚀 +323/d | **79** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Respect limits and access decisions. Unsigned beta: Windows is not publisher-signed; macOS is unsigned and unnotarized. | 🟢 Easy · OOTB | ✅ | — | 4.3k 🚀 +91/d | **75** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.6k (+21/d) | **70** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6k 🚀 +71/d | **69** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Self-Improving Sovereign Agents — voices: @tom_doerr, @AIDailyGems "Automation executes. Autonomy reasons." — @NVIDIAAP | 🟢 Easy | — | — | 4.7k (+24/d) | **65** |
| ✅ **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4k 🚀 +44/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k (+11/d) | **63** |
| 🔹 **[Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith)** | Keysmith 给本机的 AI 编程工具装指令：先预览，再写入，能验证，能撤走。 | 🟡 Some setup | — | — | 4.7k 🚀 +46/d | **61** |
| 🔹 **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | ╔═════════════════════════════════════════════════════════════════════════════╗ ║ MARKETING NOTES FOR IMAGE ASSETS ║ ║ All images below live under .github/assets/. | 🟡 Some setup | — | — | 2.1k (+13/d) | **61** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 774 | **56** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 418 | **54** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Evolve — evolutionary program search with a mandatory budget and zero-call resume. | 🟢 Easy · OOTB | ✅ | — | 687 (+5/d) | **51** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | PAXM carries decisions, conventions, and working context into later Codex, Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP sessions. | 🟡 Some setup | — | — | 422 🚀 +5/d | **49** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 410 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 535 | **40** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [getpaseo/paseo](https://github.com/getpaseo/paseo), [aipoch/open-science](https://github.com/aipoch/open-science), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [topoteretes/cognee](https://github.com/topoteretes/cognee), [KunAgent/Kun](https://github.com/KunAgent/Kun), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase), [felinics/Memoh](https://github.com/felinics/Memoh) *(+10 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **275,647** (~1044.1/day lifetime average)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **27,296** (~317.4/day lifetime average)
- Health score: **88/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

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

- Stars: **29,256** (~129.4/day lifetime average)
- Health score: **88/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-09
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

- Stars: **14,459** (~245.1/day lifetime average)
- Health score: **87/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-09

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

- Stars: **9,068** (~129.5/day lifetime average)
- Health score: **85/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Skills

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 149.8k (+253/d) | **90** |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | English \| 简体中文 \| 日本語 \| 한국어 \| Русский | 🟡 Some setup | — | — | 44.8k (+311/d) | **89** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟡 Some setup | — | — | 159.1k 🚀 +1337/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | An agent skill for crafting cinematic product videos: 157 shot recipe cards · 214 styles · 214 motion previews · a production-ready template | 🟢 Turnkey | — | ✅ | 11k 🚀 +135/d | **85** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 26.9k (+122/d) | **85** |
| 🏆 **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** | A skill to stop your coding agent from burying the answer. ADHD-friendly output. | 🟢 Easy | — | — | 56k (+378/d) | **84** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 5.9k 🚀 +115/d | **77** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 10.7k (+89/d) | **75** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.6k (+34/d) | **70** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 4.3k 🚀 +67/d | **68** |
| ✅ **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.3k 🚀 +82/d | **66** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1k | **57** |
| 🔹 **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | "A skill forgotten is a power lost." — The Code Architect Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ — AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and migration digest for 4.6→4.7… | 🟢 Easy | — | — | 817 | **57** |
| 🔹 **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 3.4k (+27/d) | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.8k (+8/d) | **56** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 890 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 341 | **53** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). | 🟢 Easy | — | — | 755 🚀 +7/d | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. | 🟢 Turnkey | — | ✅ | 496 | **52** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 298 | **52** |
| 🔹 **[zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills)** | 审稿意见回复（Rebuttal / Peer-review response） 引文管理：DOI → BibTeX，文献元数据提取，引文验证 | 🟡 Some setup | — | — | 4.7k (+32/d) | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 Easy | — | — | 1.1k | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **48** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 2.6k (+10/d) | **47** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 436 | **47** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | GRACE means Graph-RAG Anchored Code Engineering: a contract-first AI engineering methodology built around semantic markup, .grace XML artifacts, knowledge-graph navigation, assertions, scopes, and log-driven verificatio… | 🟡 Some setup | — | — | 251 | **44** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [garrytan/gstack](https://github.com/garrytan/gstack), [affaan-m/ECC](https://github.com/affaan-m/ECC), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [trailhq/Graft](https://github.com/trailhq/Graft), [yc-software/qm](https://github.com/yc-software/qm), [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt), [pacifio/atlas](https://github.com/pacifio/atlas), [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) *(+24 more)*

*…and 3 more in [the full index](data/index.json).*

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

- Stars: **149,803** (~252.6/day lifetime average)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **44,783** (~311.0/day lifetime average)
- Health score: **89/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

> You know him.

**Core problems it solves**

- **Skills & plugins** — *, a parser, money or security leaves one small test behind.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 42/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Web
- Some setup. configure config file, config.json/yaml/toml

**Facts**

- Stars: **159,112** (~1337.1/day lifetime average)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **10,967** (~135.4/day lifetime average)
- Health score: **85/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex

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

- Stars: **26,852** (~121.5/day lifetime average)
- Health score: **85/100**
- Documentation score: **56/100**
- License: MIT
- Last push: 2026-09-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

</details>

## Isolation & Parallelism

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. | 🟡 Some setup | — | — | 135.7k (+643/d) | **90** |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.4k (+98/d) | **85** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.4k (+78/d) | **81** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 7.7k 🚀 +65/d | **72** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Website · Documentation · 中文 | 🟢 Turnkey | — | — | 5.3k (+38/d) | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.1k (+26/d) | **68** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. | 🟢 Turnkey · OOTB | ✅ | — | 3.2k (+25/d) | **67** |
| ✅ **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | module outlines: 7 of 12 modules with 3+ nodes in view (cap 12; 3 dropped as too thin to read as a region; 2 dropped as enclosing mostly other modules) — three separate truncations, each wi… PageRank is a bad co-change… | 🟢 Easy | — | — | 2.4k 🚀 +34/d | **66** |
| ✅ **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.6k (+44/d) | **64** |
| ✅ **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. | 🟢 Turnkey | — | ✅ | 2.1k (+6/d) | **62** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k (+7/d) | **60** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. Go beyond code — video, slides, and more — the Commander drives open-source tools like HyperFrames and hands off to CLI agents — the coding agents Cla… | 🟡 Some setup | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 531 | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 522 | **56** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Run every AI coding agent in its own git worktree, in parallel. The desktop app embeds its server on 127.0.0.1 with a per-launch token; nothing is exposed to the network. | 🟢 Turnkey | — | ✅ | 267 | **47** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | A macOS desktop app for running multiple AI agents in parallel. Run separate agent sessions side-by-side, each in its own workspace with an isolated git worktree | 🟢 Easy | — | ✅ | 216 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [affaan-m/ECC](https://github.com/affaan-m/ECC), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [getpaseo/paseo](https://github.com/getpaseo/paseo), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [felinics/Memoh](https://github.com/felinics/Memoh), [thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills), [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck) *(+11 more)*

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

- Stars: **135,686** (~643.1/day lifetime average)
- Health score: **90/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **27,355** (~98.0/day lifetime average)
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

- Stars: **33,397** (~78.0/day lifetime average)
- Health score: **81/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-09-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)

> href="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square" src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square" src="https://img.shields.io/badge/X-@kunchenguid-black?style=fla…

**Core problems it solves**

- **Automatic failover** — *ap visible session events since the prior real captain message plus visibly unanswered captain decisions, then guide the captain through any open dec…*
- **Parallel execution** — *ental Orca terminal you can watch or type into; the first mate reconciles.*
- **Workspace isolation** — *s in its own tmux window or Herdr tab, or in an experimental Zellij tab, experimental cmux workspace, or experimental Orca terminal you can watch or…*
- **Agent runtime** — *ate conventions that turns a general-purpose agent into a specialized one.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux
- Easy. install via npx one-liner, native installer / package; needs git clone (build from source); configure environment variables, sign-in required; no-code positioning

**Facts**

- Stars: **7,714** (~64.8/day lifetime average)
- Health score: **72/100**
- Documentation score: **52/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)

> Website · Documentation · 中文

**Core problems it solves**

- **Multi-agent orchestration** — *ll support research, coding, visual design, and unattended workflow automation.*
- **Parallel execution** — *Raven on the documentation site.*
- **Model / provider routing** — *istant, keeps improving it while you work, and afterwards a sentence is enough to put it to work again.*
- **API gateway / proxy** — *istant, keeps improving it while you work, and afterwards a sentence is enough to put it to work again.*
- **Memory & context** — *ncy, error avoidance, and skill use.*
- **Skills & plugins** — *at outperform the baseline in reproducible evaluations.*
- **Self-hostable**
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 13/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raven.evermind.ai/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source); configure server/reverse-proxy setup

**Facts**

- Stars: **5,325** (~37.8/day lifetime average)
- Health score: **70/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-09
- Works with: Claude Code, Codex

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 88.3k (+428/d) | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 99k (+450/d) | **89** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 11.2k 🚀 +200/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 4.3k 🚀 +395/d | **83** |
| 🏆 **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 10.7k 🚀 +90/d | **80** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 14.9k (+78/d) | **77** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 20.2k (+56/d) | **74** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Reuse current subscriptions. Sign in with the Claude, Codex, and Grok | 🟢 Easy · OOTB | ✅ | ✅ | 24.1k (+54/d) | **71** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.3k (+34/d) | **67** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.4k 🚀 +37/d | **60** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. | 🟡 Some setup | — | — | 1k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | A professional dashboard to track and visualize Claude Code, Cursor, and Codex agent sessions, tool usage, conversation history, cost, and subagent orchestration in real time. | 🟡 Some setup | — | — | 1.1k | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 308 | **55** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 283 | **55** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | The structured skill framework for Claude Code: 131 professional skills for deployment, security, databases, content, marketing, and more. | 🟢 Easy | — | — | 423 | **52** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 322 | **47** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [yetone/cumora](https://github.com/yetone/cumora), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **88,264** (~428.5/day lifetime average)
- Health score: **92/100**
- Documentation score: **51/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
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

- Stars: **99,034** (~450.1/day lifetime average)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **11,208** (~200.1/day lifetime average)
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
- **GUI / desktop app** — *ting from 0.1.0? macOS may ask you, once for each key you saved, to let Coucou use it: enter your Mac password and click Always Allow.*
- **Notifications** — *your iPhone's Lock Screen and Dynamic Island with the agent's state, then comes back to the notch when you unlock.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install xcodegen`
- Platforms mentioned: macOS, Windows, Linux, iOS
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, database dependency; one-click setup

**Facts**

- Stars: **4,345** (~395.0/day lifetime average)
- Health score: **83/100**
- Documentation score: **60/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-09
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

- Stars: **10,698** (~89.9/day lifetime average)
- Health score: **80/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

</details>

## Analytics

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 7.4k 🚀 +93/d | **74** |
| ✅ **[pacifio/atlas](https://github.com/pacifio/atlas)** | Switching agents loses the thread. Nothing is locked in. | 🟢 Easy | — | — | 9.5k (+65/d) | **73** |
| ✅ **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。 | 🟡 Some setup | — | — | 12.4k (+93/d) | **72** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 31.8k (+28/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.1k (+30/d) | **65** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.4k 🚀 +23/d | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | Decomposed retrieval evaluation: ARES (NAACL 2024), RAGChecker (2024) Memory and knowledge-base poisoning: AgentPoison (NeurIPS 2024), PoisonedRAG (USENIX Security 2025) | 🟢 Easy · OOTB | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Conversations with AI agents reset when context windows close. Agent Action Grammar (AAG): Ultra-compact, deterministic ASCII micro-syntax saving ~78–85% tokens compared to natural language prompt instructions. | 🟡 Some setup | — | — | 758 🚀 +23/d | **57** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 417 | **55** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 837 | **52** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Plugin-first long-term memory for every agent platform. Corrections that stick. | 🟢 Easy | — | ✅ | 547 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 428 | **52** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 678 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 614 | **51** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 445 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Intelligent LLM Routing (omega-pro) — Classifies tasks and routes to the optimal model. Secure Profile (omega-pro) — AES-256 encrypted personal data storage with macOS Keychain integration. | 🟡 Some setup | — | — | 220 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | LycheeMemory is a compact memory framework for LLM agents. GET /mcp exposes the SSE stream used by some MCP clients | 🟡 Some setup | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 476 | **49** |
| 🔹 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 514 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 247 | **46** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 476 | **42** |

**Also does this:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [garrytan/gstack](https://github.com/garrytan/gstack), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [spinabot/brigade](https://github.com/spinabot/brigade), [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) *(+7 more)*

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

- Stars: **7,445** (~93.1/day lifetime average)
- Health score: **74/100**
- Documentation score: **42/100**
- License: MIT
- Language: Python
- Last push: 2026-09-20
- Works with: Codex

#### [pacifio/atlas](https://github.com/pacifio/atlas)

> Source control for coding agents.

**Core problems it solves**

- **Multi-agent orchestration** — *cupy the context window for the rest of the session.*
- **Usage analytics**
- **Session persistence** — *gent session produced which commit), which is SQLite in the project's gitignored .atlas/, because it is queried, not read.*
- **Memory & context** — *ts, tool calls, and reasoning.*
- **Agent runtime**
- **GUI / desktop app** — *. Code, notes, and sessions stay on your machine. Sign in and create an organization when you want to sync across a team.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Kilo Code*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source); configure sign-in required, database dependency; GUI application

**Facts**

- Stars: **9,540** (~64.9/day lifetime average)
- Health score: **73/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **12,450** (~92.9/day lifetime average)
- Health score: **72/100**
- Documentation score: **40/100**
- License: MIT
- Last push: 2026-09-24
- Works with: Claude Code, Codex

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

- Stars: **31,837** (~27.7/day lifetime average)
- Health score: **69/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)

> Your AI coding agent forgets everything when the session ends.

**Core problems it solves**

- **Session persistence** — *ns, discoveries, accomplished work, next steps, and relevant files.*
- **Memory & context** — *ehavior, manual MCP setup, compaction resilience, and troubleshooting: Agent Setup → · Pi users can also find the package at gentle-engram.*
- **Agent runtime**
- **MCP support** — *any MCP-compatible agent · per-agent setup →*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install gentleman-programming/tap/engram`
- Platforms mentioned: Windows, Linux, Web
- Easy. install via Homebrew install; configure environment variables, database dependency

**Facts**

- Stars: **7,101** (~30.4/day lifetime average)
- Health score: **65/100**
- Documentation score: **57/100**
- License: MIT
- Language: Go
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Teams

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 158.4k (+440/d) | **98** |
| 🏆 **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 83.6k (+161/d) | **90** |
| 🏆 **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.6k 🚀 +113/d | **84** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 8.2k 🚀 +89/d | **81** |
| 🏆 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.4k 🚀 +216/d | **79** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 8.6k (+66/d) | **75** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Your coding agent already has a memory feature. | 🔴 Involved | — | — | 9.1k (+65/d) | **70** |
| ✅ **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4k 🚀 +75/d | **69** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k (+32/d) | **68** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.7k (+10/d) | **57** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that consults multiple AI coding agents in parallel and shows you their answers side-by-side. | 🟡 Some setup | — | — | 853 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 408 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Hots are tater-tots now. v1.1.7 called them hots. The first time a newer veil runs while you are logged in Windows. The first time veil binds a port, Windows Defender Firewall pops up *"Allow this app | 🟢 Easy | — | — | 215 | **54** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 514 | **52** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.1k (+8/d) | **49** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 300 | **49** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code is an AI coding workspace for work that lasts longer than one prompt. | 🟡 Some setup | — | — | 436 | **48** |

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

- Stars: **158,420** (~440.1/day lifetime average)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **83,573** (~160.7/day lifetime average)
- Health score: **90/100**
- Documentation score: **80/100**
- License: MIT
- Language: Python
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Cursor, Droid

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

- Stars: **13,617** (~113.5/day lifetime average)
- Health score: **84/100**
- Documentation score: **63/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode, Cursor, Cline / Roo

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

- Stars: **8,156** (~88.7/day lifetime average)
- Health score: **81/100**
- Documentation score: **78/100**
- License: MIT
- Language: Python
- Last push: 2026-10-09
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

- Stars: **15,370** (~216.5/day lifetime average)
- Health score: **79/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode

</details>

## Accounts

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 128.3k (+236/d) | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 7.2k 🚀 +482/d | **86** |
| 🏆 **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 31 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 17.2k 🚀 +153/d | **83** |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 30.5k (+110/d) | **81** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth，以及 Grok apply_patch 协议兼容方向，以及账号池错误分类与状态恢复边界… Grok CLI 凭据不加密：access token/… | 🟢 Easy | — | — | 18.8k (+70/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.6k (+38/d) | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 535 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 283 | **52** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k (+15/d) | **51** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 884 | **51** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Automatic Token Refresh: Claude Code manages token refresh internally. --max-retries N — Maximum retry attempts on rate limit (default: 1) | 🟡 Some setup | — | — | 209 | **50** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 为 Sub2API 增加 账号级 STATE 票据管理，尝试应对最近 ChatGPT / Codex 账号的模型降质和降并发：请求的模型被路由到其他模型，或 OpenAI 上游限制账号可同时处理的请求数量。 | 🟡 Some setup | — | — | 215 🚀 +11/d | **48** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

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

- Stars: **128,341** (~235.9/day lifetime average)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-09
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *one key that matters in the agent's own config.*
- **Model / provider routing** — *e · Pencil · T3 Code · OpenHanako · AtomCode · Alma · Cindy*
- **API gateway / proxy** — *anfan · Tencent Cloud · Huawei Cloud MaaS · Volcengine Ark · Mistral · Groq · xAI · OpenRouter · Together · Fireworks · SiliconFlow · NVIDIA NIM · Mo…*
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

- Stars: **7,237** (~482.5/day lifetime average)
- Health score: **86/100**
- Documentation score: **57/100**
- License: MIT
- Language: Go
- Last push: 2026-10-09
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

- Stars: **17,163** (~153.2/day lifetime average)
- Health score: **83/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
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

- Stars: **30,502** (~110.1/day lifetime average)
- Health score: **81/100**
- Documentation score: **66/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-08
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
- **API gateway / proxy** — *和 JSON／纯文本返回，model 仅作为兼容字段，实际模型由 backend 决定；字幕时间戳、流式转写及其他音频操作需使用支持相应接口的 API Key 供应商。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 26/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **18,752** (~70.5/day lifetime average)
- Health score: **77/100**
- Documentation score: **60/100**
- Language: Rust
- Last push: 2026-10-07
- Works with: Codex, OpenCode, Cursor, Copilot

</details>

## Agent Runtime & Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 212.3k (+404/d) | **90** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | — | 73.9k (+395/d) | **89** |
| 🏆 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 14.9k 🚀 +176/d | **85** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 26.8k 🚀 +239/d | **84** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 8.5k 🚀 +78/d | **75** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.6k (+6/d) | **60** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **59** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 453 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | A persistent memory system for AI coding agents that enables long-term context retention across sessions using local vector database technology. | 🔴 Involved | — | — | 1.7k (+6/d) | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 734 | **50** |
| 👀 **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | A curated collection of agent skills (for Claude Code and OpenAI Codex) for developing ComfyUI custom nodes. | 🟡 Some setup | — | — | 295 | **41** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 639 | **39** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [stablyai/orca](https://github.com/stablyai/orca), [openai/codex](https://github.com/openai/codex), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [yc-software/qm](https://github.com/yc-software/qm) *(+33 more)*

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

- Stars: **212,303** (~403.6/day lifetime average)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

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

- Stars: **73,872** (~395.0/day lifetime average)
- Health score: **89/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **14,939** (~175.8/day lifetime average)
- Health score: **85/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-09
- Works with: Codex

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

- Stars: **26,770** (~239.0/day lifetime average)
- Health score: **84/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

#### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

> BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into.

**Core problems it solves**

- **Skills & plugins**
- **GUI / desktop app** — *the last update attempt; update-state.json in the bsk home keeps its stage, result and error.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs pnpm install/build, cargo build; configure sign-in required, process manager

**Facts**

- Stars: **8,503** (~78.0/day lifetime average)
- Health score: **75/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Cursor

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. | 🟡 Some setup | — | — | 11k 🚀 +127/d | **81** |
| 🏆 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 9.6k 🚀 +107/d | **80** |
| ✅ **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.5k 🚀 +343/d | **75** |
| ✅ **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens. | 🟢 Easy · OOTB | ✅ | — | 7.5k (+53/d) | **71** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.7k (+13/d) | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 343 | **53** |
| 🔹 **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | A multi-provider gateway for Claude Code and other coding agents. Claude tier routing: Fable / Opus / Sonnet / Haiku | 🟢 Easy | — | — | 623 🚀 +15/d | **52** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CR… | 🟡 Some setup | — | — | 371 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 709 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 458 | **48** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 Easy | — | — | 368 | **47** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [trailhq/Graft](https://github.com/trailhq/Graft), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill), [slopus/happy](https://github.com/slopus/happy), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) *(+21 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [openai/codex-security](https://github.com/openai/codex-security)

> @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code.

**Core problems it solves**

- **Model / provider routing**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @openai/codex-security`
- Some setup. install via npx one-liner; needs npm install/build; configure API key configuration, sign-in required

**Facts**

- Stars: **11,044** (~126.9/day lifetime average)
- Health score: **81/100**
- Documentation score: **41/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-09
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

- Stars: **9,612** (~106.8/day lifetime average)
- Health score: **80/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

#### [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)

> Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

**Core problems it solves**

- **Automatic failover**
- **Model / provider routing**
- **Skills & plugins**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install fast-jev-compaction`
- Platforms mentioned: macOS
- Some setup. needs npm install/build; configure API key configuration, .env file

**Facts**

- Stars: **7,543** (~342.9/day lifetime average)
- Health score: **75/100**
- Documentation score: **30/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-18
- Works with: Claude Code

#### [teamchong/pxpipe](https://github.com/teamchong/pxpipe)

> Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens.

**Core problems it solves**

- **Multi-agent orchestration** — *okens, not every identifier.*
- **Model / provider routing** — *pipe compresses the *request* only, never the model's output.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx pxpipe-proxy                                  # proxy on 127.0.0.1:47821`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via npx one-liner; needs pnpm install/build

**Facts**

- Stars: **7,503** (~53.2/day lifetime average)
- Health score: **71/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **1,701** (~12.9/day lifetime average)
- Health score: **56/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-09
- Works with: Codex

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 107.3k (+199/d) | **91** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 43.6k (+148/d) | **85** |
| 🏆 **[trailhq/Graft](https://github.com/trailhq/Graft)** | You correct it, and by the next session it has forgotten. Entry-point trace — Trace end-to-end what happens when a client creates a record via the REST API, from route handler to database write. | 🟡 Some setup | — | — | 9.8k 🚀 +101/d | **80** |
| ✅ **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.2k 🚀 +162/d | **74** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 5.5k 🚀 +56/d | **73** |
| 🔹 **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file… | 🔴 Involved | — | — | 3.7k (+26/d) | **59** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 778 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 399 | **50** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 416 | **46** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [yetone/magpie](https://github.com/yetone/magpie), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [spinabot/brigade](https://github.com/spinabot/brigade), [topoteretes/cognee](https://github.com/topoteretes/cognee), [future-agi/future-agi](https://github.com/future-agi/future-agi), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [hex/claude-council](https://github.com/hex/claude-council) *(+10 more)*

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

- Stars: **107,269** (~199.0/day lifetime average)
- Health score: **91/100**
- Documentation score: **69/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-08
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

- Stars: **43,558** (~147.7/day lifetime average)
- Health score: **85/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

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

- Stars: **9,826** (~101.3/day lifetime average)
- Health score: **80/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **11,167** (~161.8/day lifetime average)
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

- Stars: **5,503** (~56.1/day lifetime average)
- Health score: **73/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 141.8k (+330/d) | **93** |
| 🏆 **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 3.3k 🚀 +79/d | **78** |
| ✅ **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.1k 🚀 +42/d | **62** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁移。 工作台完整保留：任务看板、Git、文件交付、模型协作、桌宠、15 套皮肤、SSH 与远程访问继续提供；恢复 4.4.0 品牌图标。 | 🟢 Turnkey · OOTB | ✅ | — | 786 🚀 +14/d | **58** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 723 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 434 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 697 🚀 +6/d | **49** |

**Also does this:** [loopx-project/loopx](https://github.com/loopx-project/loopx), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **141,777** (~329.7/day lifetime average)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

#### [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)

> An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔…

**Core problems it solves**

- **Quota & usage management** — *平台适配的成品直接到对应平台，再通过**归因**分析表现并把有效经验沉淀回账号画像。*
- **Multi-provider aggregation**
- **API gateway / proxy** — *API 不提供向量模型，请单独配置 Embedding API；否则 OpenClaw 会默认请求 text-embedding-3-small，可能得到“模型不可用”。*
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

- Stars: **3,325** (~79.2/day lifetime average)
- Health score: **78/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-09
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

- Stars: **4,118** (~42.5/day lifetime average)
- Health score: **62/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-09
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

- Stars: **786** (~14.0/day lifetime average)
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

- Stars: **723** (~3.1/day lifetime average)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-02
- Works with: Claude Code, Cursor

</details>

## Quota

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 9.3k (+77/d) | **77** |
| ✅ **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.2k 🚀 +175/d | **76** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 人保留最终决策。 Agent 可以起草提案卡片——固定约定、请求执行、添加成员——但只有你能采纳或忽略。 执行隔离且有证据。 每个执行任务在独立 Git worktree 中运行，交付固定为不可变版本再交 Reviewer 评审；声明的验证检查、Diff、日志与集成面板都留在房间内。 | 🟢 Easy | — | ✅ | 6.3k (+45/d) | **67** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | orchestrator：Node 26 串行 853 项：852 通过、1 项 Windows ACL 专项跳过；类型检查通过。 desktop：84/84，类型检查与生产构建通过；Python（计算库、回测、数据脚本）：754/754。 | 🟢 Easy | — | — | 2.6k 🚀 +27/d | **64** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k (+13/d) | **60** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 2.5k 🚀 +44/d | **57** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 410 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 交代一句话，它自己规划、动手、验收，把 PPT / Word / Excel / 网页落到你硬盘上。 10-06 系统沙箱：AI 跑的命令和脚本在 macOS、Windows 上读不到 Key 和账本、改不了应用；设置 → 安全 能关，每条多花 7–16 毫秒 | 🟡 Some setup | — | — | 279 🚀 +5/d | **51** |

**Also does this:** [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **9,288** (~76.8/day lifetime average)
- Health score: **77/100**
- Documentation score: **57/100**
- License: AGPL-3.0
- Language: JavaScript
- Last push: 2026-09-12
- Works with: Claude Code, Codex, Cursor

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

- Stars: **7,159** (~174.6/day lifetime average)
- Health score: **76/100**
- Documentation score: **50/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-01
- Works with: Codex

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

- Stars: **6,318** (~45.1/day lifetime average)
- Health score: **67/100**
- Documentation score: **41/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Codex, Cursor

#### [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

> Codex / Claude Code / WorkBuddy 订阅或模型 API 一次接入 · Agent 默认关闭 · 左上角一键开启

**Core problems it solves**

- **Quota & usage management** — *装并登录的 WorkBuddy，或腾讯官方 CodeBuddy Code CLI*
- **Multi-agent orchestration** — *排层 orchestrator + validator + calc + gate 强制阶段、证据引用、确定性计算和合规边界*
- **Workspace isolation**
- **MCP support** — *odex 订阅走 Codex Harness；Claude 订阅走 Claude Code Agent；WorkBuddy / CodeBuddy 走 CodeBuddy Code Agent，三者不会混叫。*
- **Self-hostable** — *- API 模式的 key 会持久保存在当前浏览器的本机 localStorage，方便下次直接使用；它不是系统钥匙串，*
- **Notifications**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 31/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via global npm install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration

**Facts**

- Stars: **2,636** (~27.5/day lifetime average)
- Health score: **64/100**
- Documentation score: **68/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex

#### [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)

> Discuss the SDK on Discord

**Core problems it solves**

- **Quota & usage management** — *nously (without task parameter) or asynchronously (with task parameter):*
- **Parallel execution** — *sends task status notifications on completion*
- **MCP support** — *tation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.*
- **Notifications** — *calls tool with task parameter*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Web
- Some setup. configure OAuth login flow, database dependency

**Facts**

- Stars: **9,157** (~13.5/day lifetime average)
- Health score: **60/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-10-09

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 Some setup | — | — | 6.2k (+48/d) | **71** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.1k (+9/d) | **54** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. Cline / Roo Code / Zoo Code / Kilo Code (VS Code extension + CLI) | 🟢 Turnkey · OOTB | ✅ | — | 223 | **50** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | The self-hosted AI backend for private data and tool-using agents. | 🟡 Some setup | — | — | 353 | **49** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons,… | 🟡 Some setup | — | — | 723 | **44** |

**Also does this:** [decolua/9router](https://github.com/decolua/9router), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **6,216** (~47.8/day lifetime average)
- Health score: **71/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-09
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **2,149** (~8.6/day lifetime average)
- Health score: **54/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-16
- Works with: Droid

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

- Stars: **5,888** (~5.1/day lifetime average)
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

- Stars: **223** (~0.5/day lifetime average)
- Health score: **50/100**
- Documentation score: **32/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot, Cline / Roo

#### [schmitech/orbit](https://github.com/schmitech/orbit)

> The self-hosted AI backend for private data and tool-using agents.

**Core problems it solves**

- **Model / provider routing**
- **API gateway / proxy**
- **Usage analytics** — *uild agents MCP tools · Automatic skill routing · A2A · Adapter creation*
- **MCP support** — *private documents, an agent that calls your tools, or a triage workflow—with the same backend.*
- **Security & isolation** — *behind one OpenAI-compatible API.*
- **Self-hostable** — *vector stores, APIs, and MCP tools through YAML-configured adapters.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 43/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -LO https://github.com/schmitech/orbit/releases/download/v2.18.1/orbit-2.18.1.tar.gz`
- Platforms mentioned: Windows, Web
- Some setup. install via global npm install; needs npm install/build; configure API key configuration, config.json/yaml/toml

**Facts**

- Stars: **353** (~0.6/day lifetime average)
- Health score: **49/100**
- Documentation score: **46/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-08

</details>

## Sharing

*Quota sharing / splitting*

A subscription's capacity is larger than one person needs; share it safely with others.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 🤖 Agent-native, model-agnostic. Hand off to engineering. | 🟢 Easy | — | — | 100.1k (+611/d) | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 556 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 241 | **42** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [decolua/9router](https://github.com/decolua/9router), [future-agi/future-agi](https://github.com/future-agi/future-agi), [cita-777/metapi](https://github.com/cita-777/metapi), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy), [wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

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

- Stars: **100,137** (~610.6/day lifetime average)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-09
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Teams | Agent Runtime & Desktop UI, Mobile |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Sharing | Billing, Self-hosting & Security |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Accounts, Billing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Billing | Analytics |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Agent Runtime & Desktop UI | Model Routing, Skills |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Isolation & Parallelism | Analytics, Skills |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Teams | Analytics, Isolation & Parallelism |
| **[openai/codex](https://github.com/openai/codex)** | Accounts | Agent Runtime & Desktop UI |
| **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | Skills | Agent Runtime & Desktop UI, Model Routing |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Self-hosting & Security | Isolation & Parallelism, Skills |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile | Analytics, Self-hosting & Security |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Self-hosting & Security | Agent Runtime & Desktop UI, Billing |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Accounts | Billing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Accounts, Sharing |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Self-hosting & Security | Billing, Sharing |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Agent Runtime & Desktop UI | Model Routing, Skills |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Teams | Analytics, Isolation & Parallelism |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Accounts | Agent Runtime & Desktop UI, Model Routing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Self-hosting & Security | Analytics, Model Routing |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Self-hosting & Security | Analytics, Billing |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Agent Runtime & Desktop UI, Model Routing |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[decolua/9router](https://github.com/decolua/9router)** | Accounts | Analytics, Sharing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Self-hosting & Security | Analytics, Billing |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Mobile | Agent Runtime & Desktop UI, Model Routing |
| **[trailhq/Graft](https://github.com/trailhq/Graft)** | Billing | Model Routing, Skills |
| **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | Self-hosting & Security | Analytics |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams | Agent Runtime & Desktop UI, Skills |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Skills | Agent Runtime & Desktop UI, Model Routing |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Accounts | Agent Runtime & Desktop UI, Model Routing |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Analytics, Self-hosting & Security |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Quota | Skills |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Teams | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Isolation & Parallelism, Self-hosting & Security |
| **[pacifio/atlas](https://github.com/pacifio/atlas)** | Analytics | Agent Runtime & Desktop UI, Skills |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | Self-hosting & Security |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Agent Runtime & Desktop UI, Model Routing |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Providers |
| **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Model Routing |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Analytics, Self-hosting & Security |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Agent Runtime & Desktop UI, Mobile |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | Analytics | Billing, Self-hosting & Security |
| **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Teams | Agent Runtime & Desktop UI, Skills |
| **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | Quota | Self-hosting & Security |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Skills |
| **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Isolation & Parallelism | Model Routing, Skills |
| **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Self-hosting & Security | Model Routing, Skills |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Quota | Isolation & Parallelism, Self-hosting & Security |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Agent Runtime & Desktop UI, Analytics |
| **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | Self-hosting & Security | Billing, Sharing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation & Parallelism | Self-hosting & Security, Skills |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Billing | Analytics, Self-hosting & Security |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Skills | Agent Runtime & Desktop UI |
| **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Model Routing |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Analytics | Billing, Model Routing |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Agent Runtime & Desktop UI, Mobile |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams | Isolation & Parallelism, Self-hosting & Security |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Skills | Agent Runtime & Desktop UI, Model Routing |
| **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | Skills | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Analytics | Model Routing, Skills |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Isolation & Parallelism | Model Routing, Skills |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Agent Runtime & Desktop UI | Isolation & Parallelism, Skills |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Skills | Agent Runtime & Desktop UI, Analytics |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Self-hosting & Security | Agent Runtime & Desktop UI, Analytics |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Self-hosting & Security |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Agent Runtime & Desktop UI | Model Routing, Skills |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Mobile | Agent Runtime & Desktop UI, Self-hosting & Security |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Skills | Agent Runtime & Desktop UI, Model Routing |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Mobile | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Mobile | Accounts, Billing |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation & Parallelism | Model Routing, Skills |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Isolation & Parallelism, Self-hosting & Security |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Teams | Billing, Isolation & Parallelism |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Self-hosting & Security |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Analytics, Skills |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Self-hosting & Security | Analytics, Model Routing |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Teams | Billing, Isolation & Parallelism |
| **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Teams | Agent Runtime & Desktop UI, Billing |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Isolation & Parallelism, Model Routing |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Isolation & Parallelism, Model Routing |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Analytics | Mobile |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Analytics | Model Routing, Skills |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Skills | Agent Runtime & Desktop UI, Model Routing |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Analytics | Skills |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Teams | Billing, Self-hosting & Security |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Self-hosting & Security |
| **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | Mobile | Isolation & Parallelism, Skills |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Model Routing | Skills |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Accounts | Analytics, Analytics |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Accounts | Providers, Sharing |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Analytics | Agent Runtime & Desktop UI |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Analytics | Skills |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Quota | Agent Runtime & Desktop UI |
| **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | Quota | Self-hosting & Security, Sharing |
| **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Analytics | Billing, Model Routing |
| **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | Analytics | Billing |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Agent Runtime & Desktop UI | Model Routing, Skills |
| **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | Analytics | Agent Runtime & Desktop UI |
| **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Accounts | Billing, Model Routing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Isolation & Parallelism, Skills |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Model Routing, Skills |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Sharing | Analytics, Quota |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | Self-hosting & Security | Analytics, Billing |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Analytics | Billing, Self-hosting & Security |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams | Mobile, Self-hosting & Security |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Skills |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams | Analytics, Model Routing |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Skills | Billing, Model Routing |
| **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | Accounts | Quota, Sharing |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Self-hosting & Security | Agent Runtime & Desktop UI, Skills |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Mobile | Isolation & Parallelism |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Isolation & Parallelism | Agent Runtime & Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Self-hosting & Security | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Analytics | Agent Runtime & Desktop UI |
| **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | Analytics | Isolation & Parallelism |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Analytics | Self-hosting & Security |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Sharing | Accounts, Billing |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | Agent Runtime & Desktop UI | Skills |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Agent Runtime & Desktop UI | Skills |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.05x the stars (7,237 vs 141,777) |

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
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.88x the stars (7,101 vs 719) | 🤖 auto (high) |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/agi-is-going-to-arrive/memory-palace)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 93.47x the stars (29,256 vs 313) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 57.35x the stars (18,752 vs 327) | 🤖 auto (high) |
| **[AndrewDryga/emisar](https://github.com/andrewdryga/emisar)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 13.96x the stars (4,705 vs 337) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 19.56x the stars (10,698 vs 547) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 6.37x the stars (2,428 vs 381) | 🤖 auto (high) |
| **[LerianStudio/ring](https://github.com/lerianstudio/ring)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 11.19x the stars (2,428 vs 217) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[pacifio/atlas](https://github.com/pacifio/atlas)** | 18.49x the stars (9,540 vs 516) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 869.55x the stars (275,647 vs 317) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 64.07x the stars (275,647 vs 4,302) | 🤖 auto (high) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 59.77x the stars (275,647 vs 4,612) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.18x the stars (33,397 vs 923) | 🤖 auto (high) |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 57.78x the stars (33,397 vs 578) | 🤖 auto (high) |
| **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 50.07x the stars (33,397 vs 667) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 96.52x the stars (33,397 vs 346) | 🤖 auto (high) |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 5.88x the stars (29,256 vs 4,975) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.59x the stars (27,355 vs 4,895) | 🤖 auto (high) |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 65.74x the stars (29,256 vs 445) | 🤖 auto (high) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.83x the stars (13,617 vs 391) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 24.64x the stars (8,156 vs 331) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 6.44x the stars (8,156 vs 1,267) | 🤖 auto (high) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 74.71x the stars (18,752 vs 251) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 46.60x the stars (20,224 vs 434) | 🤖 auto (high) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1148.53x the stars (275,647 vs 240) | 🤖 auto (high) |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/ccteam-creator)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 441.97x the stars (135,686 vs 307) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 24.30x the stars (11,300 vs 465) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 578.18x the stars (158,420 vs 274) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.33x the stars (33,397 vs 273) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 58.28x the stars (29,256 vs 502) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 23.74x the stars (9,068 vs 382) | 🤖 auto (high) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 26.19x the stars (33,397 vs 1,275) | 🤖 auto (high) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 101.26x the stars (99,034 vs 978) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 8.70x the stars (2,428 vs 279) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 78.43x the stars (29,256 vs 373) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 46.16x the stars (275,647 vs 5,972) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 144.38x the stars (141,777 vs 982) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[EverMind-AI/Raven](https://github.com/evermind-ai/raven)** | 9.56x the stars (5,325 vs 557) | 🤖 auto (high) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 397.19x the stars (275,647 vs 694) | 🤖 auto (high) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 81.38x the stars (275,647 vs 3,387) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 70.54x the stars (99,034 vs 1,404) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.99x the stars (8,156 vs 2,729) | 🤖 auto (high) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 17.15x the stars (29,256 vs 1,706) | 🤖 auto (medium) |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 9.03x the stars (2,085 vs 231) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 6.87x the stars (44,783 vs 6,517) | 🤖 auto (medium) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 451.88x the stars (275,647 vs 610) | 🤖 auto (medium) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.90x the stars (817 vs 282) | 🤖 auto (high) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 10.30x the stars (4,705 vs 457) | 🤖 auto (medium) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.92x the stars (8,156 vs 2,082) | 🤖 auto (high) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 581.53x the stars (275,647 vs 474) | 🤖 auto (medium) |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 104.11x the stars (29,256 vs 281) | 🤖 auto (medium) |
| **[AI-QL/tuui](https://github.com/ai-ql/tuui)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 25.33x the stars (29,256 vs 1,155) | 🤖 auto (medium) |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 6.83x the stars (275,647 vs 40,367) | 🤖 auto (medium) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.20x the stars (8,156 vs 3,708) | 🤖 auto (medium) |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/fuxi)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 8.73x the stars (29,256 vs 3,350) | 🤖 auto (medium) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.29x the stars (817 vs 356) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 2.87x the stars (14,930 vs 5,208) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.66x the stars (817 vs 307) | 🤖 auto (high) |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 5.97x the stars (29,256 vs 4,900) | 🤖 auto (medium) |
| **[MoonshotAI/kimi-code](https://github.com/moonshotai/kimi-code)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 4.28x the stars (33,397 vs 7,811) | 🤖 auto (high) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.31x the stars (20,224 vs 4,691) | 🤖 auto (medium) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 3.68x the stars (2,085 vs 566) | 🤖 auto (medium) |
| **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 1.44x the stars (10,698 vs 7,425) | 🤖 auto (medium) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.30x the stars (1,424 vs 1,092) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | self-hosting-security | 40.4k | 🔻 Superseded | 6.83x the stars (275,647 vs 40,367) |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | isolation-parallelism | 7.8k | 🔻 Superseded | 4.28x the stars (33,397 vs 7,811) |
| **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | mobile | 7.4k | 🔻 Superseded | 1.44x the stars (10,698 vs 7,425) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.5k | 🔻 Superseded | 6.87x the stars (44,783 vs 6,517) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | self-hosting-security | 6k | 🔻 Superseded | 46.16x the stars (275,647 vs 5,972) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | mobile | 5.2k | 🔻 Superseded | 2.87x the stars (14,930 vs 5,208) |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | self-hosting-security | 5k | 🔻 Superseded | 5.88x the stars (29,256 vs 4,975) |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | self-hosting-security | 4.9k | 🔻 Superseded | 5.97x the stars (29,256 vs 4,900) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-parallelism | 4.9k | 🔻 Superseded | 5.59x the stars (27,355 vs 4,895) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | mobile | 4.7k | 🔻 Superseded | 4.31x the stars (20,224 vs 4,691) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | self-hosting-security | 4.6k | 🔻 Superseded | 59.77x the stars (275,647 vs 4,612) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | self-hosting-security | 4.3k | 🔻 Superseded | 64.07x the stars (275,647 vs 4,302) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 Superseded | 2.20x the stars (8,156 vs 3,708) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | self-hosting-security | 3.4k | 🔻 Superseded | 81.38x the stars (275,647 vs 3,387) |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | self-hosting-security | 3.4k | 🔻 Superseded | 8.73x the stars (29,256 vs 3,350) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 Superseded | 2.99x the stars (8,156 vs 2,729) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 Superseded | 3.92x the stars (8,156 vs 2,082) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | self-hosting-security | 1.7k | 🔻 Superseded | 17.15x the stars (29,256 vs 1,706) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile | 1.4k | 🔻 Superseded | 70.54x the stars (99,034 vs 1,404) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | isolation-parallelism | 1.3k | 🔻 Superseded | 26.19x the stars (33,397 vs 1,275) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 6.44x the stars (8,156 vs 1,267) |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | self-hosting-security | 1.2k | 🔻 Superseded | 25.33x the stars (29,256 vs 1,155) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | mobile | 1.1k | 🔻 Superseded | 1.30x the stars (1,424 vs 1,092) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers | 982 | 🔻 Superseded | 144.38x the stars (141,777 vs 982) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile | 978 | 🔻 Superseded | 101.26x the stars (99,034 vs 978) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-parallelism | 923 | 🔻 Superseded | 36.18x the stars (33,397 vs 923) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | analytics | 719 | 🔻 Superseded | 9.88x the stars (7,101 vs 719) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | self-hosting-security | 694 | 🔻 Superseded | 397.19x the stars (275,647 vs 694) |
| **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | isolation-parallelism | 667 | 🔻 Superseded | 50.07x the stars (33,397 vs 667) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | self-hosting-security | 610 | 🔻 Superseded | 451.88x the stars (275,647 vs 610) |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | isolation-parallelism | 578 | 🔻 Superseded | 57.78x the stars (33,397 vs 578) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | isolation-parallelism | 566 | 🔻 Superseded | 3.68x the stars (2,085 vs 566) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-parallelism | 557 | 🔻 Superseded | 9.56x the stars (5,325 vs 557) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile | 547 | 🔻 Superseded | 19.56x the stars (10,698 vs 547) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | analytics | 516 | 🔻 Superseded | 18.49x the stars (9,540 vs 516) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | self-hosting-security | 502 | 🔻 Superseded | 58.28x the stars (29,256 vs 502) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | self-hosting-security | 474 | 🔻 Superseded | 581.53x the stars (275,647 vs 474) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | self-hosting-security | 465 | 🔻 Superseded | 24.30x the stars (11,300 vs 465) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | self-hosting-security | 457 | 🔻 Superseded | 10.30x the stars (4,705 vs 457) |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | self-hosting-security | 445 | 🔻 Superseded | 65.74x the stars (29,256 vs 445) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 434 | 🔻 Superseded | 46.60x the stars (20,224 vs 434) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | teams | 391 | 🔻 Superseded | 34.83x the stars (13,617 vs 391) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | self-hosting-security | 382 | 🔻 Superseded | 23.74x the stars (9,068 vs 382) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-parallelism | 381 | 🔻 Superseded | 6.37x the stars (2,428 vs 381) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | self-hosting-security | 373 | 🔻 Superseded | 78.43x the stars (29,256 vs 373) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 356 | 🔻 Superseded | 2.29x the stars (817 vs 356) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | isolation-parallelism | 346 | 🔻 Superseded | 96.52x the stars (33,397 vs 346) |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | self-hosting-security | 337 | 🔻 Superseded | 13.96x the stars (4,705 vs 337) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 331 | 🔻 Superseded | 24.64x the stars (8,156 vs 331) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | accounts | 327 | 🔻 Superseded | 57.35x the stars (18,752 vs 327) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | self-hosting-security | 317 | 🔻 Superseded | 869.55x the stars (275,647 vs 317) |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | self-hosting-security | 313 | 🔻 Superseded | 93.47x the stars (29,256 vs 313) |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | isolation-parallelism | 307 | 🔻 Superseded | 441.97x the stars (135,686 vs 307) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | skills | 307 | 🔻 Superseded | 2.66x the stars (817 vs 307) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 Superseded | 2.90x the stars (817 vs 282) |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | self-hosting-security | 281 | 🔻 Superseded | 104.11x the stars (29,256 vs 281) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | isolation-parallelism | 279 | 🔻 Superseded | 8.70x the stars (2,428 vs 279) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 274 | 🔻 Superseded | 578.18x the stars (158,420 vs 274) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | isolation-parallelism | 273 | 🔻 Superseded | 122.33x the stars (33,397 vs 273) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | accounts | 251 | 🔻 Superseded | 74.71x the stars (18,752 vs 251) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | self-hosting-security | 240 | 🔻 Superseded | 1148.53x the stars (275,647 vs 240) |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | isolation-parallelism | 231 | 🔻 Superseded | 9.03x the stars (2,085 vs 231) |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | isolation-parallelism | 217 | 🔻 Superseded | 11.19x the stars (2,428 vs 217) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-09 11:23 UTC. 206 live tools · 131 candidates rejected by the quality gates.</sub>
