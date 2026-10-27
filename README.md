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

**220 tools** across **14 categories** · **51 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-27 09:54 UTC**

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

- [Memory & MCP](#memory-mcp) — 38 tools
- [Desktop UI](#desktop-ui) — 39 tools
- [Mobile & Remote Control](#mobile-remote-control) — 30 tools
- [Sharing](#sharing) — 19 tools
- [Isolation](#isolation) — 14 tools
- [Model Routing](#model-routing) — 13 tools
- [Teams](#teams) — 10 tools
- [Billing](#billing) — 12 tools
- [Failover](#failover) — 11 tools
- [Desktop UI](#desktop-ui) — 11 tools
- [Mobile](#mobile) — 7 tools
- [Providers](#providers) — 7 tools
- [Analytics](#analytics) — 6 tools
- [Security & Self-hosting](#security-self-hosting) — 3 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Memory & MCP

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 290.2k 🚀 +844/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 21k 🚀 +204/d | **88** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 17k 🚀 +801/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 11k 🚀 +120/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 13.9k 🚀 +217/d | **82** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 15.1k 🚀 +58/d | **72** |
| ✅ **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.7k 🚀 +61/d | **70** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 32.8k 🚀 +30/d | **69** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.8k 🚀 +6/d | **67** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 8.7k 🚀 +64/d | **66** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.6k 🚀 +8/d | **62** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **62** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +18/d | **61** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4k 🚀 +28/d | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **57** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.2k 🚀 +10/d | **57** |
| 🔹 **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | 111 MCP tools · 59 RE/debug backends · 4,200+ skills · multi-agent mesh · zero-dep native parsers | 🟢 Easy | — | — | 385 🚀 +18/d | **57** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.1k | **55** |
| 🔹 **[graygnatconsole/mcp-audit-tool](https://github.com/graygnatconsole/mcp-audit-tool)** | Scan your AI agent configs for tool poisoning, rug pulls, hardcoded secrets, command injection, and supply-chain risks — before the model runs something you regret. | 🟢 Turnkey | — | — | 544 | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 468 | **55** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.7k 🚀 +13/d | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 414 | **54** |
| 🔹 **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | Park, J.S. et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. UIST 2023. doi:10.1145/3586183.3606763 Liu, N.F. et al. (2024). Lost in the Middle: How Language Models Use Long Contexts. TACL 12, 1… | 🟡 Some setup | — | — | 224 | **53** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 440 | **52** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 330 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 497 | **51** |
| 🔹 **[GMaN1911/claude-cognitive](https://github.com/GMaN1911/claude-cognitive)** | WARM (0.25-0.8): Headers only - background awareness 1+ million line production codebase (3,200+ Python modules) | 🟡 Some setup | — | — | 451 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **51** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [garrytan/gstack](https://github.com/garrytan/gstack), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [superdesigndev/treg](https://github.com/superdesigndev/treg), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) *(+15 more)*

*…and 8 more in [the full index](data/index.json).*

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

- Stars: **290,229** (+844.2/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-26
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

- Stars: **21,048** (+204.0/day over 5d)
- Health score: **88/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-27

#### [xerj-org/xerj](https://github.com/xerj-org/xerj)

> XERJ: the search engine for AI agents.

**Core problems it solves**

- **Memory & context** — *f the same primitive: xerj autoindex makes an agent*
- **Agent runtime** — *rity audit of WordPress core,*
- **MCP support** — *ks with Claude Code, Cursor and any MCP client.*
- **GUI / desktop app** — *Shell installer (get.ps1) puts xerj.exe in %LOCALAPPDATA%\Programs\xerj and adds that directory to the user PATH ((Get-Command xerj).Source confirms;…*
- **Cross-agent support** — *Mentions Aider, Amp, Claude Code, Cline*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://xerj.org/get | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source), cargo build; configure API key configuration, config file; GUI application

**Facts**

- Stars: **16,964** (+801.4/day over 5d)
- Health score: **87/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **11,029** (+120.4/day over 5d)
- Health score: **86/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-27
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

- Stars: **13,946** (+217.4/day over 5d)
- Health score: **82/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-17
- Works with: Claude Code, Codex

</details>

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 153.5k 🚀 +139/d | **90** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | ✅ | 177.6k 🚀 +1040/d | **87** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Taste Skill is an Agent Skill that makes coding agents design websites and app screens instead of assembling the average landing page. | 🟢 Easy | — | — | 103.3k 🚀 +492/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 21.2k 🚀 +487/d | **83** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 49.1k 🚀 +2274/d | **82** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 38 mandatory rules (R-01 to R-38) in three tiers: Hard Gate, Purpose-Gate, and Quality Locks. A Delivery Gate: a mandatory PASS/FAIL report in four blocks, run before anything ships. | 🟢 Turnkey · OOTB | ✅ | — | 7.3k 🚀 +91/d | **80** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 5.5k 🚀 +103/d | **76** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 4.9k 🚀 +84/d | **69** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 10.8k 🚀 +51/d | **67** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 27.4k 🚀 +25/d | **66** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 4.1k 🚀 +50/d | **65** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | An open skill for agent-to-agent contracts. | 🟢 Easy | — | — | 7k 🚀 +25/d | **61** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.2k 🚀 +24/d | **59** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.7k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.7k | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 898 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 541 | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 510 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 343 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **52** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CR… | 🟡 Some setup | — | — | 368 | **52** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 292 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.4k 🚀 +5/d | **51** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 910 | **51** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 305 | **51** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [garrytan/gstack](https://github.com/garrytan/gstack), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [leepokai/Codync](https://github.com/leepokai/Codync), [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent), [1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking) *(+23 more)*

*…and 9 more in [the full index](data/index.json).*

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

- Stars: **153,516** (+139.4/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-26
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

- Stars: **177,577** (+1040.0/day over 5d)
- Health score: **87/100**
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

- Stars: **103,254** (+491.8/day over 5d)
- Health score: **86/100**
- Documentation score: **33/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-26
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

- Stars: **21,230** (+487.2/day over 5d)
- Health score: **83/100**
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

- Stars: **49,121** (+2274.4/day over 5d)
- Health score: **82/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

</details>

## Mobile & Remote Control

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 107.5k 🚀 +1105/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 107.8k 🚀 +385/d | **89** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🔴 Involved | — | — | 137.9k 🚀 +124/d | **88** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 22.2k 🚀 +103/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 6.6k 🚀 +88/d | **79** |
| ✅ **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. Routines: ask a Bot to do something on a schedule and it does, running as y… | 🟡 Some setup | — | — | 7.3k 🚀 +75/d | **74** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 5.7k 🚀 +65/d | **74** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 84.5k 🚀 +39/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.8k 🚀 +24/d | **72** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 9.1k 🚀 +28/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.3k 🚀 +39/d | **68** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 11.1k 🚀 +18/d | **67** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 15.2k 🚀 +16/d | **65** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.7k 🚀 +8/d | **63** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟡 Some setup | — | — | 5.4k 🚀 +9/d | **63** |
| 🔹 **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | English: README.en.md \| 中文: README.md | 🔴 Involved | — | — | 3k 🚀 +48/d | **59** |
| 🔹 **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 939 | **58** |
| 🔹 **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 한국어 \| 中文 \| Português \| 日本語 \| Français \| Español \| Nederlands \| Polski \| Русский \| Deutsch \| Tiếng Việt \| ภาษาไทย | 🟢 Easy | — | — | 1.4k | **57** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **57** |
| 🔹 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 888 🚀 +12/d | **56** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 785 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 320 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 423 | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 788 | **53** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **52** |
| 🔹 **[autohandai/code-cli](https://github.com/autohandai/code-cli)** | Cross-Platform: Works on macOS, Linux, and Windows Large command results retain the first and last portions of each output stream, up to 1,048,576 characters, with an omission marker. | 🟡 Some setup | — | — | 211 | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **51** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 304 | **49** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [slopus/happy](https://github.com/slopus/happy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)

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

- Stars: **107,492** (+1105.4/day over 5d)
- Health score: **92/100**
- Documentation score: **52/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
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

- Stars: **107,804** (+385.2/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who…

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *cause and re-verify before committing.*
- **Workspace isolation** — *es; blocks below 7/10), fail-closed secret redaction, dedupe against existing issues, archive to $GSTACK_STATE_ROOT/projects/$SLUG/specs/ for team-co…*
- **Model / provider routing** — *deterministic aside repl scripts.*
- **Memory & context** — *ice-input aliases many skills carry, have their own pages.*
- **Skills & plugins** — *--single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup then add a "gstack"…*
- **Agent runtime** — *gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architec…*
- **MCP support** — */gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup then add a "gstack" section to CLAUDE.md that says to use the /browse sk…*

**Getting it running**

- Setup: 🔴 **Involved** (friction 65/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Involved setup. needs git clone (build from source), go build; configure sign-in required, server/reverse-proxy setup; one-click setup

**Facts**

- Stars: **137,869** (+124.2/day over 5d)
- Health score: **88/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

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

- Stars: **22,186** (+103.0/day over 5d)
- Health score: **83/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

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

- Stars: **6,591** (+88.4/day over 5d)
- Health score: **79/100**
- Documentation score: **67/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Sharing

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 23.2k 🚀 +798/d | **89** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 131.1k 🚀 +142/d | **89** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 31.5k 🚀 +59/d | **72** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 10.1k 🚀 +51/d | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 19.4k 🚀 +35/d | **69** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 31 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 18k 🚀 +39/d | **67** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k | **56** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.6k 🚀 +15/d | **55** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.8k 🚀 +12/d | **55** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 549 🚀 +19/d | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 505 | **52** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 264 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 308 | **50** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Automatic Token Refresh: Claude Code manages token refresh internally. --max-retries N — Maximum retry attempts on rate limit (default: 1) | 🟡 Some setup | — | — | 210 | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 908 | **49** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 332 🚀 +14/d | **49** |
| 🔹 **[youssefvdel/qwengate](https://github.com/youssefvdel/qwengate)** | Multi-Account Rotation — Configure multiple Qwen accounts (3+ recommended). OpenAI-Compatible API — Drop-in replacement for /v1/chat/completions and /v1/models. | 🟢 Easy | — | — | 205 | **46** |
| 🔹 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | Built with C++ / Win32 / WebView2 for stability and speed. Quota dashboard, auto-refresh (5H / 7D), low-quota alerts and switch prompts | 🟡 Some setup | — | — | 250 | **45** |
| 👀 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 为 Sub2API 增加 账号级 STATE 票据管理，尝试应对最近 ChatGPT / Codex 账号的模型降质和降并发：请求的模型被路由到其他模型，或 OpenAI 上游限制账号可同时处理的请求数量。 | 🟡 Some setup | — | — | 219 | **43** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [spinabot/brigade](https://github.com/spinabot/brigade), [xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [cita-777/metapi](https://github.com/cita-777/metapi), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *one key that matters in the agent's own config.*
- **Multi-agent orchestration** — ***Sync** Back up to a file, or sync machines over WebDAV (Nutstore, Nextcloud…), S3, or an encrypted GitHub repository backup*
- **Model / provider routing** — *y, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to.*
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

- Stars: **23,215** (+798.4/day over 5d)
- Health score: **89/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

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

- Stars: **131,106** (+142.0/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-27
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

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

- Stars: **31,497** (+59.0/day over 5d)
- Health score: **72/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **10,077** (+51.0/day over 5d)
- Health score: **69/100**
- Documentation score: **57/100**
- License: AGPL-3.0
- Language: JavaScript
- Last push: 2026-09-12
- Works with: Claude Code, Codex, Cursor

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
- **API gateway / proxy** — *面板切回内置 Go CLIProxyAPI sidecar。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **19,400** (+35.2/day over 5d)
- Health score: **69/100**
- Documentation score: **61/100**
- Language: Rust
- Last push: 2026-10-27
- Works with: Codex, OpenCode, Cursor, Copilot

</details>

## Isolation

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.7k 🚀 +23/d | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.5k 🚀 +28/d | **69** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 8.3k 🚀 +34/d | **66** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **59** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 583 | **57** |
| 🔹 **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | Claude Code, Codex, OpenCode, Grok, Gemini CLI, Antigravity CLI, Pi, Command Code, Hermes Agent, Muse Code, Oh My Pi, and Cursor CLI run side by side. | 🟢 Turnkey · OOTB | ✅ | — | 625 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 460 | **55** |
| 🔹 **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | Big plans. Plan size predicts delivery. In an observational sample of 50 wishes, the share merged within 8h fell from 100% (n=9) for the smallest plans to 95% (n=19), 67% (n=12) and 30% (n=… Small, obvious edits. The ru… | 🟢 Turnkey · OOTB | ✅ | — | 345 | **55** |
| 🔹 **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | Uncommitted changes → [r] reopen the agent / [q] keep worktree Only commits → [m] merge into base branch / [q] keep worktree | 🟡 Some setup · OOTB | ✅ | — | 281 | **51** |
| 🔹 **[lanes-sh/app](https://github.com/lanes-sh/app)** | The model provider you choose. Gateway points a session at Ollama, LM Studio, vLLM, OpenRouter or z.ai, applied as real process environment so the request goes straight from the CLI to your… A git client, not just a dif… | 🟢 Turnkey | — | — | 276 | **48** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Run every AI coding agent in its own git worktree, in parallel. The desktop app embeds its server on 127.0.0.1 with a per-launch token; nothing is exposed to the network. | 🟢 Turnkey | — | ✅ | 272 | **43** |
| 👀 **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | 把 AI Coding 从 prompt 实验，升级为可审查、可验证、可交付的工程工作流。 读第 1-2 章，理解“写字符”到“管理 Agent 注意力”的角色变化。 | 🟢 Easy | — | — | 242 | **41** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | A macOS desktop app for running multiple AI agents in parallel. Run separate agent sessions side-by-side, each in its own workspace with an isolated git worktree | 🟢 Easy | — | ✅ | 217 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [getpaseo/paseo](https://github.com/getpaseo/paseo), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [yc-software/qm](https://github.com/yc-software/qm), [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [automazeio/ccpm](https://github.com/automazeio/ccpm), [tigicion/dao-code](https://github.com/tigicion/dao-code), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j) *(+9 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

> Persistent file-based planning for AI coding agents and long-running tasks.

**Core problems it solves**

- **Multi-agent orchestration** — *, Qoder CLI, Pi, Hermes Agent, OpenCode and DeepSeek Harness.*
- **Parallel execution** — *ry mechanism below is a file on disk plus a hook, so it works the same on hour ten as on turn one.*
- **Workspace isolation** — *** One orchestrator owns taskplan.md and the shared summaries; every worker appends to its own ledger or assigned file.*
- **Session persistence** — *d contributor-reported measurements (PRs #331, #333, #334).*
- **Memory & context**
- **Skills & plugins** — *ackage, wired up for you (skill, extension, status bar):*
- **Agent runtime** — *s every turn, a plan on disk that survives /clear , and 3 out of 3 blind A/B wins to show it works.*
- **Security & isolation**

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure environment variables, database dependency; one-click setup

**Facts**

- Stars: **27,695** (+23.4/day over 5d)
- Health score: **70/100**
- Documentation score: **73/100**
- License: MIT
- Language: Python
- Last push: 2026-10-24
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

> (renders "CRATES.IO: INVALID").

**Core problems it solves**

- **Parallel execution** — *r worktree** — hashport template filter gives each worktree a unique port*
- **Workspace isolation** — *llent, and the biggest help is folks posting problems they perceive.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `brew install worktrunk && wt config shell install`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via Homebrew install, winget install

**Facts**

- Stars: **9,516** (+27.6/day over 5d)
- Health score: **69/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code, Codex

#### [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)

> href="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square" src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-blue?style=flat-square" src="https://img.shields.io/badge/X-@kunchenguid-black?style=fla…

**Core problems it solves**

- **Automatic failover** — *ap visible session events since the prior real captain message plus visibly unanswered captain decisions, then guide the captain through any open dec…*
- **Parallel execution** — *T3 Code thread you can watch or interact with; the first mate reconciles.*
- **Workspace isolation** — *al Zellij tab, experimental cmux workspace, experimental Tern block, experimental Orca terminal, or experimental T3 Code thread you can watch or inte…*
- **Agent runtime** — *ate conventions that turns a general-purpose agent into a specialized one.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Linux
- Easy. install via npx one-liner, native installer / package; needs git clone (build from source); configure environment variables, sign-in required; no-code positioning

**Facts**

- Stars: **8,333** (+34.0/day over 5d)
- Health score: **66/100**
- Documentation score: **52/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)

> Live site: psantanna.com/claude-code-my-workflow

**Core problems it solves**

- **Multi-agent orchestration** — *e first, then run ./scripts/validate-setup.sh — it reports exactly what's missing with install links.*
- **Parallel execution** — *ee / methods-referee / editor — manuscript peer-review pipeline (/review-paper --peer)*
- **Workspace isolation** — *ks see effort.level and $CLAUDEEFFORT (Apr 2026 Week 19)*
- **Model / provider routing** — *een for parallel review work (/review-paper --peer, /slide-excellence).*
- **Memory & context**
- **Skills & plugins** — *- **Real gates, not reminders.** One command — ./scripts/backtest.sh — runs **ten gates**: surface-sync, skill integrity, model currency against the…*
- **MCP support** — *simulated peer review (/review-paper --peer [journal]), reviewer-disposition variance reporting (--variance N)*
- **Security & isolation** — ***Bypass** mode skips permission prompts and safety checks (deny rules still apply), and Anthropic scopes it to isolated containers and VMs; it takes…*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, Homebrew install; needs git clone (build from source); configure server/reverse-proxy setup; beginner-friendly

**Facts**

- Stars: **1,671** (+0.6/day over 5d)
- Health score: **59/100**
- Documentation score: **76/100**
- License: MIT
- Language: HTML
- Last push: 2026-09-27
- Works with: Claude Code

#### [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)

> Appearance follows your OS — see Appearance.

**Core problems it solves**

- **Mobile access** — *als so every pane can see its own running dev server without alt-tabbing.*
- **Multi-agent orchestration** — *it continues where it left off.*
- **Parallel execution** — *know how git worktrees work?"*
- **Workspace isolation** — *ack of which agent is on which branch.*
- **Session persistence**
- **Agent runtime** — *Pane — a pixel-art terminal workshop with separate agent workspaces*
- **MCP support** — *s only command names, arguments, and safe usage notes.*
- **Self-hostable** — *dinate Claude, Codex, or Cursor across repositories, panes, tabs, worktrees, and review loops.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npx --yes runpane@latest`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Easy. install via pip install, curl | sh installer; needs git clone (build from source), pnpm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **583** (+2.0/day over 5d)
- Health score: **57/100**
- Documentation score: **70/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode, Cursor, Aider, Goose

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | — | 77.7k 🚀 +252/d | **89** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | A toolbox of film styles made in code: 59 ready to use, and your own. Default output 1920×1080, 24 fps; other sizes on request. | 🟡 Some setup | — | ✅ | 8.4k 🚀 +651/d | **82** |
| 🏆 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 3.8k 🚀 +150/d | **78** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 10.8k 🚀 +50/d | **68** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.5k 🚀 +32/d | **66** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 10.8k 🚀 +37/d | **65** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.2k 🚀 +10/d | **59** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.9k 🚀 +10/d | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 344 | **53** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.6k | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 713 | **50** |
| 🔹 **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | A multi-provider gateway for Claude Code and other coding agents. Claude tier routing: Fable / Opus / Sonnet / Haiku | 🟢 Easy | — | — | 629 | **49** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 470 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [zai-org/ZCode](https://github.com/zai-org/ZCode), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi), [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) *(+9 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)

> So I built the filter I&nbsp;needed.

**Core problems it solves**

- **Model / provider routing** — *s the same in longer words.*
- **API gateway / proxy** — *s the same in longer words.*
- **Skills & plugins** — *does not duplicate the full project instructions when it reads both AGENTS.md and GEMINI.md.*
- **GUI / desktop app** — *terminal dashboard lets you browse your pipeline visually:*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx @santifer/career-ops init`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, config file

**Facts**

- Stars: **77,740** (+252.0/day over 5d)
- Health score: **89/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

> A toolbox of film styles made in code: 59 ready to use, and your own.

**Core problems it solves**

- **Model / provider routing** — *e or make one from scratch, bring your story, and let your coding agent direct.*
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

- Stars: **8,372** (+651.0/day over 5d)
- Health score: **82/100**
- Documentation score: **55/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-24
- Works with: Claude Code, Cursor

#### [Folkbench/folkbench](https://github.com/Folkbench/folkbench)

> 中转站实测评测，与 Folkbench Switch。

**Core problems it solves**

- **Model / provider routing** — *本地用量估算：按会话统计 Token 消耗量，并根据公开参考单价提供调用成本估算。*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Aider, Claude Code, Codex, Gemini CLI*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 41/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows
- Some setup. configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **3,761** (~150.4/day lifetime average)
- Health score: **78/100**
- Documentation score: **36/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-10-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Aider, Qwen Code

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

- Stars: **10,799** (+50.4/day over 5d)
- Health score: **68/100**
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

- Stars: **17,491** (+31.8/day over 5d)
- Health score: **66/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

</details>

## Teams

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 164.4k 🚀 +267/d | **98** |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 61.6k 🚀 +358/d | **90** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 11.2k 🚀 +103/d | **84** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Website: aimemory.sh | 🟡 Some setup | — | — | 13.9k 🚀 +265/d | **84** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.5k 🚀 +10/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k 🚀 +6/d | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4k | **54** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k | **54** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 320 | **48** |

**Also does this:** [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [jmagly/aiwg](https://github.com/jmagly/aiwg), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **164,380** (+267.4/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-25
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **61,552** (+358.2/day over 5d)
- Health score: **90/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-10-26
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

- Stars: **11,165** (+102.6/day over 5d)
- Health score: **84/100**
- Documentation score: **79/100**
- License: MIT
- Language: Python
- Last push: 2026-10-27
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

- Stars: **13,907** (+264.8/day over 5d)
- Health score: **84/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [yc-software/qm](https://github.com/yc-software/qm)

> A multiplayer agent harness for work.

**Core problems it solves**

- **Workspace isolation**
- **Model / provider routing** — *- Work in an existing repository: run tests, open PRs, monitor CI, check system logs*
- **Session persistence**
- **Skills & plugins**
- **Agent runtime** — *n harness and model and switch between*
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

- Stars: **15,546** (+9.8/day over 5d)
- Health score: **57/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 108.6k 🚀 +213/d | **91** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 6.3k 🚀 +74/d | **77** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 44.9k 🚀 +70/d | **75** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3k 🚀 +45/d | **67** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.7k 🚀 +25/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 286 | **55** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 直接找：接口一览 ｜ 五分钟上手 ｜ 易支付协议兼容接入 ｜ 到账账号与收款分配 ｜ 文档目录 ｜ 常见问题 | 🟢 Easy | — | — | 323 | **52** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 407 | **50** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 给做 SEO 和独立开发的人用的 Agent Skills。建站、选词、发外链、查数据、复盘迭代，一整条链路都在这个仓库里，装完就能跑。 | 🟢 Easy | — | — | 227 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 🔹 **[nextlevelbuilder/skillx](https://github.com/nextlevelbuilder/skillx)** | Rate skills (0-10) and write reviews HTTPS enforced (Cloudflare TLS 1.3) | 🟡 Some setup | — | — | 192 | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 434 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [decolua/9router](https://github.com/decolua/9router), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [Licoy/Quosparr](https://github.com/Licoy/Quosparr), [Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher), [wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **108,563** (+212.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Gemini CLI
- *Why it is seeded: Gemini's terminal agent, generous free tier.*

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
- **Notifications** — *ogle OAuth sign-in (redirect /auth/google/callback); empty hides the button*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://treg.to/install.sh | sh`
- Platforms mentioned: Linux, Web
- Easy. install via npx one-liner, pip install; configure environment variables, API key configuration; one-click setup

**Facts**

- Stars: **6,320** (+74.0/day over 5d)
- Health score: **77/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-27
- Works with: Claude Code

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

- Stars: **44,929** (+69.6/day over 5d)
- Health score: **75/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-26
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

> 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点

**Core problems it solves**

- **Quota & usage management** — *fig.json 写 provider.profile（如 cli-claude），或者添加时带上环境变量，例如 claude mcp add vibe-research -e VRAPROVIDER=cli-claude -- node …、codex mcp add vibe-research…*
- **Remote control**
- **Multi-agent orchestration** — *alc + gate 强制阶段、证据引用、确定性计算和合规边界*
- **API gateway / proxy** — *；三家订阅直接调用使用者本机的官方 CLI，模型 API 直接走 Chat Completions*
- **Billing & metering** — *上的对话、研究、辩论和回测都允许 AI 联网和调用产品工具。*
- **MCP support** — *gine、--codex-path 等）会报错并给出改法。*
- **Self-hostable** — *览器的本机 localStorage，方便下次直接使用；它不是系统钥匙串，也不承诺加密，只建议在可信的个人电脑上使用，共享电脑用完请主动清除。*
- **Notifications** — *都标出来），勾选的行要么全写、要么全不写，写之前先备份到 ledger/持仓导入备份-日期/。*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 43/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux
- Some setup. install via global npm install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, config.json/yaml/toml

**Facts**

- Stars: **2,999** (+44.8/day over 5d)
- Health score: **67/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-26
- Works with: Claude Code, Codex, Cursor

#### [trycompai/crm](https://github.com/trycompai/crm)

> Comp AI CRM is an open source, CRM designed for AI agents.

**Core problems it solves**

- **Model / provider routing** — *ur own identity provider on*
- **Billing & metering**
- **MCP support** — *SECRET Lets a rep talk to the agent from a contact's Agent tab.*
- **Self-hostable**

**Getting it running**

- Setup: 🔴 **Involved** (friction 90/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker compose up -d          # Postgres on :5432`
- Platforms mentioned: Linux, Web
- Involved setup. needs docker compose up, git clone (build from source); configure environment variables, OAuth login flow

**Facts**

- Stars: **11,717** (+25.0/day over 5d)
- Health score: **57/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-23

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 149.2k 🚀 +344/d | **93** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 4.3k 🚀 +106/d | **85** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.6k 🚀 +15/d | **67** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi is a fast, self-contained terminal AI coding agent. | 🟢 Easy | — | — | 3.2k 🚀 +38/d | **66** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.8k 🚀 +14/d | **62** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.8k | **59** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 5.1k 🚀 +6/d | **56** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.8k 🚀 +9/d | **50** |
| 🔹 **[api7/aisix](https://github.com/api7/aisix)** | MCP gateway — front registered upstream MCP servers at /mcp with gateway-held Inbound authentication — caller API keys (SHA-256 hashed, model allowlists, expiry, | 🟡 Some setup | — | — | 207 | **49** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 314 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 520 | **43** |

**Also does this:** [affaan-m/ECC](https://github.com/affaan-m/ECC), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [superdesigndev/treg](https://github.com/superdesigndev/treg), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) *(+7 more)*

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

- Stars: **149,223** (+344.4/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

#### [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)

> An agent skill that finds where a photo was taken — and shows its work.

**Core problems it solves**

- **Automatic failover** — *the complete skill folder, including data/ and the helper modules in scripts/.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add Oldcircle/geo-sleuth`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via npx one-liner, uvx one-liner; needs git clone (build from source)

**Facts**

- Stars: **4,313** (+105.6/day over 5d)
- Health score: **85/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-10-23
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

- Stars: **27,565** (+14.6/day over 5d)
- Health score: **67/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

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

- Stars: **3,204** (~38.1/day lifetime average)
- Health score: **66/100**
- Documentation score: **63/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-20

#### [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)

> English · 简体中文 · 日本語

**Core problems it solves**

- **Automatic failover** — *mands and access to secrets such as SSH keys and .env files before the tool call runs.*
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

- Stars: **1,810** (+13.6/day over 5d)
- Health score: **62/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 222.1k 🚀 +447/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 10.9k 🚀 +374/d | **88** |
| ✅ **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 3.1k 🚀 +314/d | **76** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 9.7k 🚀 +56/d | **71** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.2k 🚀 +16/d | **63** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 475 | **56** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Turnkey · OOTB | ✅ | — | 522 🚀 +8/d | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 767 | **54** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | Scope Recall v3 is a bounded local memory core with SQLite as the authority and rebuildable vector companions. | 🟢 Easy | — | — | 487 🚀 +9/d | **53** |
| 👀 **[wong2/diffx](https://github.com/wong2/diffx)** | A local code review tool designed for the coding agent workflow. Comment status tracker — Sidebar widget showing open, replied, and resolved comment counts with click-to-navigate links | 🟢 Turnkey · OOTB | ✅ | ✅ | 217 | **42** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [yetone/magpie](https://github.com/yetone/magpie), [xerj-org/xerj](https://github.com/xerj-org/xerj), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [getpaseo/paseo](https://github.com/getpaseo/paseo), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [google/artemis](https://github.com/google/artemis), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web), [makecindy/cindy](https://github.com/makecindy/cindy), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness) *(+43 more)*

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

- Stars: **222,146** (+447.2/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

#### [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)

> Sketch, constrain, and build solids with a parametric feature timeline.

**Core problems it solves**

- **MCP support** — *constrain, and build solids with a parametric feature timeline.*
- **GUI / desktop app** — *solidcraft -- solidcraft-cli mcp.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **10,914** (+373.6/day over 5d)
- Health score: **88/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code

#### [aicodeking/leanrea](https://github.com/aicodeking/leanrea)

> One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup.

**Core problems it solves**

- **MCP support** — *te recon commands, and lists the traps that REA's code handles for you.*
- **GUI / desktop app** — *less wall time, 35% lower cost, 56% fewer turns and 60% fewer tokens, at the same accuracy.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add aicodeking/leanrea`
- Platforms mentioned: macOS, Linux, Android, Web
- Easy. install via npx one-liner; needs git clone (build from source), go build; configure database dependency; GUI application

**Facts**

- Stars: **3,136** (~313.6/day lifetime average)
- Health score: **76/100**
- Documentation score: **30/100**
- License: MIT
- Language: Python
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **9,662** (+56.4/day over 5d)
- Health score: **71/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
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

- Stars: **15,199** (+16.2/day over 5d)
- Health score: **63/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 15.1k 🚀 +278/d | **82** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 3.3k 🚀 +85/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.3k 🚀 +16/d | **64** |
| 🔹 **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.5k 🚀 +12/d | **60** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.6k 🚀 +9/d | **54** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Official agent skills/plugins for Power Platform development by Microsoft. Launch GitHub Copilot CLI or Claude Code with the plugin path: | 🟡 Some setup | — | — | 1.1k | **51** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Control your Pi coding agent from your phone. | 🟢 Easy | — | — | 470 | **50** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [makecindy/cindy](https://github.com/makecindy/cindy), [loopx-project/loopx](https://github.com/loopx-project/loopx), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api), [yetone/cumora](https://github.com/yetone/cumora), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

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

- Stars: **15,090** (+277.6/day over 5d)
- Health score: **82/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)

> Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar.

**Core problems it solves**

- **Quota & usage management**
- **Mobile access** — *A builder, not just a researcher.*
- **Skills & plugins**
- **MCP support** — *Only want the app design skill?*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills@latest add appllama/appllama-skills`
- Platforms mentioned: Linux
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **3,324** (+85.0/day over 5d)
- Health score: **66/100**
- Documentation score: **27/100**
- License: MIT
- Last push: 2026-09-06
- Works with: Claude Code, Codex, Cursor

#### [slopus/happy](https://github.com/slopus/happy)

> Multi-provider.

**Core problems it solves**

- **Remote control** — *lopus/slopus.github.io The website and docs at happy.engineering*
- **Mobile access** — *Happy adds a harness, not another bill.*
- **Multi-agent orchestration**
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

- Stars: **24,339** (+16.0/day over 5d)
- Health score: **64/100**
- Documentation score: **29/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-27
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

- Stars: **4,510** (+11.8/day over 5d)
- Health score: **60/100**
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

- Stars: **3,623** (+9.4/day over 5d)
- Health score: **54/100**
- Documentation score: **42/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-19

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.1k 🚀 +29/d | **69** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 871 | **56** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.3k 🚀 +6/d | **55** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 983 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 760 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 434 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 511 | **52** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [loopx-project/loopx](https://github.com/loopx-project/loopx), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **4,126** (+28.8/day over 5d)
- Health score: **69/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-25
- Works with: Claude Code, Codex

#### [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)

> Open-source Windows desktop client and GUI for DeepSeek Harness — zero-setup installer with Codex, plugins, skills, SSH, mobile remote access, and 11 skins.

**Core problems it solves**

- **Automatic failover**
- **Remote control** — *### 任务看板与自动化 内置任务看板，可以管理： 待规划 → 待办 → 进行中 → 已完成 / 已失败 任务可以交给真实 DSH Agent Session 执行，并记录 Task Run 与 Evidence，方便查看结果和继续处理。*
- **Mobile access**
- **Multi-agent orchestration** — *插件稳定性继续加固：启动阶段可见、事务修复可回滚、第三方插件错误隔离，原有 DSH Home 与插件直接延续。*
- **Workspace isolation** — *、GitHub digest 与合并清单一致；Windows updater SHA-512 和 manifest 也已验证。*
- **Model / provider routing** — *载安装 EXE 后即可启动完整 Harness 环境。*
- **Multi-provider aggregation** — *pSeek Harness Desktop 5.0.0 Windows bai 模型接入*
- **Billing & metering** — *L、域名、窗口名称、截图、Prompt、工具参数、路径或凭据，详见 隐私政策。*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 8/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via native installer / package; configure OAuth login flow; GUI application

**Facts**

- Stars: **871** (+3.0/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-10-26
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

- Stars: **4,317** (+6.0/day over 5d)
- Health score: **55/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-24
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

- Stars: **983** (+0.1/day over 18d)
- Health score: **54/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-18
- Works with: Claude Code, OpenCode

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

- Stars: **760** (+1.4/day over 5d)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-26
- Works with: Claude Code, Cursor

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Source — audit, fork, extend, and contribute improvements back under Apache-2.0. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 7k 🚀 +73/d | **69** |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | The local-first harness & workspace for research agents. | 🟢 Turnkey · OOTB | ✅ | — | 7.6k 🚀 +29/d | **65** |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | 2026-10-20 · 🚀 LoopX 2.0 — A shared TypeScript control plane and long-horizon research workbench. 2026-08-02 · ⏱️ 200+ hour trajectories shared on X — Early owner-run examples spanning 200+ elapsed hours drew broad atte… | 🟢 Easy | — | — | 6.4k 🚀 +10/d | **65** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. Cline / Roo Code / Zoo Code / Kilo Code (VS Code extension + CLI) | 🟢 Turnkey · OOTB | ✅ | — | 226 | **51** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [makecindy/cindy](https://github.com/makecindy/cindy)

> Consider it done.

**Core problems it solves**

- **Mobile access**
- **Multi-agent orchestration** — *utor setup, validation, and submission workflow*
- **Model / provider routing**
- **Usage analytics** — *this is not fully anonymous.*
- **MCP support**
- **Self-hostable** — *by default (endpoint manifests in*
- **GUI / desktop app** — *apps/-bin Tool binaries shipped with the desktop app; none are committed — claude-code, codex, and ripgrep are downloaded per platform by pnpm instal…*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🔴 **Involved** (friction 65/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Linux, Android, Web
- Involved setup. needs git clone (build from source), pnpm install/build; configure sign-in required, database migration; GUI application

**Facts**

- Stars: **7,027** (~73.2/day lifetime average)
- Health score: **69/100**
- Documentation score: **53/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex

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

- Stars: **7,600** (+29.4/day over 5d)
- Health score: **65/100**
- Documentation score: **33/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [loopx-project/loopx](https://github.com/loopx-project/loopx)

> Turn long-horizon goals into verifiable results.

**Core problems it solves**

- **Quota & usage management**
- **Mobile access** — *r Manager group conversations, LoopX keeps message visibility separate from*
- **Multi-agent orchestration** — *goals, steer work and resolve decisions.*
- **Usage analytics** — *dentials, internal project names, or goal contents:*
- **Team collaboration** — *ecution still needs an available host and configured runtime.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via pip install, native installer / package; needs git clone (build from source); configure database dependency, database migration

**Facts**

- Stars: **6,444** (+10.4/day over 5d)
- Health score: **65/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-27
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

- Stars: **5,921** (+3.0/day over 5d)
- Health score: **51/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

#### [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

> Every tool call.

**Core problems it solves**

- **Model / provider routing** — *type, same decision merger, same audit / sink / transparency-log fan-out as built-ins.*
- **Billing & metering**
- **Usage analytics** — *d research assistant, fully integrated with AEGIS.*
- **MCP support** — *, AEGIS provides two proxy modes:*
- **Security & isolation** — *AEGIS is the missing layer: a pre-execution firewall that sits between your agent and its tools, classifies every call in real time, enforces policie…*
- **Self-hostable** — *Engineers Develop Tools to Audit and Monitor AI Agents (Aug 2026)*
- **Team collaboration** — *nce) via OpenAI/Anthropic/Gemini*
- **GUI / desktop app**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 44/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://aegistraces.com/install | sh`
- Platforms mentioned: macOS, Windows, Linux
- Some setup. install via pip install, curl | sh installer; needs docker compose up, kubectl apply; configure environment variables, API key configuration; no code needed

**Facts**

- Stars: **524** (+0.2/day over 5d)
- Health score: **51/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-25
- Works with: Claude Code

</details>

## Security & Self-hosting

*Quota sharing / splitting*

A subscription's capacity is larger than one person needs; share it safely with others.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 104.3k 🚀 +212/d | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 557 | **46** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 242 | **39** |

**Also does this:** [decolua/9router](https://github.com/decolua/9router), [spinabot/brigade](https://github.com/spinabot/brigade), [cordum-io/cordum](https://github.com/cordum-io/cordum), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace), [wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

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

- Stars: **104,267** (+212.2/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-27
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

- Stars: **557** (+0.0/day over 6d)
- Health score: **46/100**
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

- Stars: **242** (+0.0/day over 5d)
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Teams | Desktop UI, Mobile & Remote Control |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Security & Self-hosting | Memory & MCP, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Failover | Billing, Providers |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile & Remote Control | Isolation, Mobile |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Desktop UI, Model Routing |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Memory & MCP | Desktop UI, Failover |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile & Remote Control | Analytics, Memory & MCP |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Model Routing | Failover |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Memory & MCP | Desktop UI |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Memory & MCP | Model Routing, Teams |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Desktop UI, Memory & MCP |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Memory & MCP, Model Routing |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI |
| **[google/artemis](https://github.com/google/artemis)** | Mobile | Desktop UI |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile & Remote Control | Failover, Model Routing |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Billing | Failover, Memory & MCP |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Failover, Sharing |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Mobile & Remote Control | Failover, Memory & MCP |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile & Remote Control | Analytics, Desktop UI |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Mobile & Remote Control | Failover, Memory & MCP |
| **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Memory & MCP | Desktop UI |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Billing, Security & Self-hosting |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation | Desktop UI |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | Memory & MCP | Failover, Model Routing |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Desktop UI, Mobile |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Model Routing, Sharing |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Billing, Failover |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Mobile & Remote Control | Model Routing |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Failover, Model Routing |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Mobile & Remote Control | Desktop UI, Model Routing |
| **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | Desktop UI | Desktop UI |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Memory & MCP, Sharing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | Failover, Memory & MCP |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | Failover | Model Routing |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Model Routing | Desktop UI, Isolation |
| **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | Analytics | Model Routing |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Mobile, Providers |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI, Mobile & Remote Control |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Mobile & Remote Control | Desktop UI |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | Desktop UI | Desktop UI |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Memory & MCP | Security & Self-hosting, Sharing |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Desktop UI |
| **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | Mobile & Remote Control | Desktop UI, Model Routing |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Failover | Desktop UI, Memory & MCP |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation | Desktop UI, Memory & MCP |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile & Remote Control | Desktop UI, Desktop UI |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams | Isolation, Model Routing |
| **[trycompai/crm](https://github.com/trycompai/crm)** | Billing | Memory & MCP |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Desktop UI | Desktop UI |
| **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation | Desktop UI, Mobile & Remote Control |
| **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | Memory & MCP | Desktop UI, Desktop UI |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Failover | Desktop UI |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams | Desktop UI, Memory & MCP |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI, Memory & MCP |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile & Remote Control | Failover, Mobile |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI, Isolation |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Analytics, Desktop UI |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | Sharing | Mobile |
| **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Desktop UI | Desktop UI |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Memory & MCP | Desktop UI, Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Sharing | Billing, Providers |
| **[oracle/mcp](https://github.com/oracle/mcp)** | Memory & MCP | Desktop UI |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Isolation | Desktop UI, Desktop UI |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | Isolation | Desktop UI, Desktop UI |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Desktop UI, Failover |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Mobile, Model Routing |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Teams | Isolation |
| **[routatic/proxy](https://github.com/routatic/proxy)** | Providers | Failover |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Desktop UI |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Mobile & Remote Control | Desktop UI, Teams |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Isolation |
| **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | Memory & MCP | Desktop UI, Teams |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Memory & MCP, Security & Self-hosting |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Sharing | Desktop UI |
| **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | Billing | Model Routing, Sharing |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Memory & MCP, Model Routing |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Analytics, Mobile & Remote Control |
| **[autohandai/code-cli](https://github.com/autohandai/code-cli)** | Mobile & Remote Control | Desktop UI, Model Routing |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI, Memory & MCP |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Analytics | Providers, Teams |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | Isolation | Desktop UI, Desktop UI |
| **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | Analytics | Desktop UI, Isolation |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI, Isolation |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Mobile | Desktop UI, Mobile & Remote Control |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Failover |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Sharing | Billing, Desktop UI |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Billing | Security & Self-hosting, Sharing |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | Desktop UI | Isolation |
| **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Sharing | Billing, Desktop UI |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | Model Routing | Failover |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Sharing | Billing, Mobile |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Mobile & Remote Control | Memory & MCP, Teams |
| **[api7/aisix](https://github.com/api7/aisix)** | Failover | Memory & MCP, Model Routing |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Providers, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Desktop UI, Isolation |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Memory & MCP | Failover |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Teams | Isolation |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | Isolation | Desktop UI, Desktop UI |
| **[nextlevelbuilder/skillx](https://github.com/nextlevelbuilder/skillx)** | Billing | Desktop UI |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | Memory & MCP | Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Memory & MCP | Desktop UI |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Security & Self-hosting | Failover, Sharing |
| **[youssefvdel/qwengate](https://github.com/youssefvdel/qwengate)** | Sharing | Failover, Model Routing |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | Isolation | Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Desktop UI |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Memory & MCP | Desktop UI, Desktop UI |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Memory & MCP | Desktop UI, Isolation |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Failover | Memory & MCP, Security & Self-hosting |
| **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | Sharing | Billing, Security & Self-hosting |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | Isolation | Desktop UI, Memory & MCP |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Security & Self-hosting | Model Routing, Sharing |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.16x the stars (23,215 vs 149,223) |

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
| **[AVIDS2/memorix](https://github.com/avids2/memorix)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 332.83x the stars (290,229 vs 872) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 59.33x the stars (19,400 vs 327) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 20.09x the stars (11,072 vs 551) | 🤖 auto (high) |
| **[Digital-Process-Tools/claude-remember](https://github.com/digital-process-tools/claude-remember)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 135.76x the stars (27,695 vs 204) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.05x the stars (19,400 vs 2,409) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 72.88x the stars (27,695 vs 380) | 🤖 auto (high) |
| **[Karanjot786/agent-skills-cli](https://github.com/karanjot786/agent-skills-cli)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 4.61x the stars (898 vs 195) | 🤖 auto (high) |
| **[KbWen/agentic-os](https://github.com/kbwen/agentic-os)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 125.89x the stars (27,695 vs 220) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 20.05x the stars (11,029 vs 550) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 562.46x the stars (290,229 vs 516) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.20x the stars (11,165 vs 2,148) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 898.54x the stars (290,229 vs 323) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.19x the stars (22,186 vs 5,297) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 3.90x the stars (1,107 vs 284) | 🤖 auto (high) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 165.09x the stars (290,229 vs 1,758) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.59x the stars (27,695 vs 4,951) | 🤖 auto (high) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.34x the stars (13,737 vs 400) | 🤖 auto (high) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1209.29x the stars (290,229 vs 240) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 629.81x the stars (164,380 vs 261) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 44.11x the stars (22,186 vs 503) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 470.39x the stars (290,229 vs 617) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.33x the stars (149,223 vs 9,137) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 28.65x the stars (11,029 vs 385) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 34.89x the stars (19,400 vs 556) | 🤖 auto (high) |
| **[ndycode/oc-codex-multi-auth](https://github.com/ndycode/oc-codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 93.72x the stars (19,400 vs 207) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.57x the stars (290,229 vs 6,101) | 🤖 auto (high) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 405.91x the stars (290,229 vs 715) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 605.91x the stars (290,229 vs 479) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 4.08x the stars (5,723 vs 1,403) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.44x the stars (11,165 vs 1,323) | 🤖 auto (medium) |
| **[sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 54.33x the stars (11,029 vs 203) | 🤖 auto (medium) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.91x the stars (898 vs 309) | 🤖 auto (high) |
| **[ZipengWu365/TOMC](https://github.com/zipengwu365/tomc)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 41.62x the stars (11,029 vs 265) | 🤖 auto (medium) |
| **[YYHDBL/AgentCrew](https://github.com/yyhdbl/agentcrew)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 426.10x the stars (107,804 vs 253) | 🤖 auto (medium) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 599.65x the stars (290,229 vs 484) | 🤖 auto (medium) |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 94.08x the stars (290,229 vs 3,085) | 🤖 auto (medium) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 19.95x the stars (27,695 vs 1,388) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 39.64x the stars (16,964 vs 428) | 🤖 auto (medium) |
| **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 684.50x the stars (290,229 vs 424) | 🤖 auto (medium) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 318.23x the stars (290,229 vs 912) | 🤖 auto (medium) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 611.01x the stars (290,229 vs 475) | 🤖 auto (medium) |
| **[garagon/nanostack](https://github.com/garagon/nanostack)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 520.79x the stars (107,804 vs 207) | 🤖 auto (medium) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 38.60x the stars (290,229 vs 7,519) | 🤖 auto (medium) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.46x the stars (898 vs 365) | 🤖 auto (high) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 2.13x the stars (1,107 vs 519) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.56x the stars (898 vs 575) | 🤖 auto (high) |
| **[Dataojitori/nocturne_memory](https://github.com/dataojitori/nocturne_memory)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 8.05x the stars (11,360 vs 1,411) | 🤖 auto (high) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.51x the stars (22,186 vs 6,322) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.20x the stars (898 vs 408) | 🤖 auto (high) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.17x the stars (1,072 vs 495) | 🤖 auto (medium) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.19x the stars (898 vs 755) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | failover | 9.1k | 🔻 Superseded | 16.33x the stars (149,223 vs 9,137) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | memory-mcp | 7.5k | 🔻 Superseded | 38.60x the stars (290,229 vs 7,519) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | mobile-remote-control | 6.3k | 🔻 Superseded | 3.51x the stars (22,186 vs 6,322) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | memory-mcp | 6.1k | 🔻 Superseded | 47.57x the stars (290,229 vs 6,101) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | mobile-remote-control | 5.3k | 🔻 Superseded | 4.19x the stars (22,186 vs 5,297) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation | 5k | 🔻 Superseded | 5.59x the stars (27,695 vs 4,951) |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | memory-mcp | 3.1k | 🔻 Superseded | 94.08x the stars (290,229 vs 3,085) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 Superseded | 8.05x the stars (19,400 vs 2,409) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 Superseded | 5.20x the stars (11,165 vs 2,148) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | memory-mcp | 1.8k | 🔻 Superseded | 165.09x the stars (290,229 vs 1,758) |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | memory-mcp | 1.4k | 🔻 Superseded | 8.05x the stars (11,360 vs 1,411) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile-remote-control | 1.4k | 🔻 Superseded | 4.08x the stars (5,723 vs 1,403) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation | 1.4k | 🔻 Superseded | 19.95x the stars (27,695 vs 1,388) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 8.44x the stars (11,165 vs 1,323) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | memory-mcp | 912 | 🔻 Superseded | 318.23x the stars (290,229 vs 912) |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | memory-mcp | 872 | 🔻 Superseded | 332.83x the stars (290,229 vs 872) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 Superseded | 1.19x the stars (898 vs 755) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | memory-mcp | 715 | 🔻 Superseded | 405.91x the stars (290,229 vs 715) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | memory-mcp | 617 | 🔻 Superseded | 470.39x the stars (290,229 vs 617) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | desktop-ui | 575 | 🔻 Superseded | 1.56x the stars (898 vs 575) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 556 | 🔻 Superseded | 34.89x the stars (19,400 vs 556) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile-remote-control | 551 | 🔻 Superseded | 20.09x the stars (11,072 vs 551) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-mcp | 550 | 🔻 Superseded | 20.05x the stars (11,029 vs 550) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | desktop-ui | 519 | 🔻 Superseded | 2.13x the stars (1,107 vs 519) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | memory-mcp | 516 | 🔻 Superseded | 562.46x the stars (290,229 vs 516) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mobile-remote-control | 503 | 🔻 Superseded | 44.11x the stars (22,186 vs 503) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 495 | 🔻 Superseded | 2.17x the stars (1,072 vs 495) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | memory-mcp | 484 | 🔻 Superseded | 599.65x the stars (290,229 vs 484) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | memory-mcp | 479 | 🔻 Superseded | 605.91x the stars (290,229 vs 479) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | memory-mcp | 475 | 🔻 Superseded | 611.01x the stars (290,229 vs 475) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | memory-mcp | 428 | 🔻 Superseded | 39.64x the stars (16,964 vs 428) |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | memory-mcp | 424 | 🔻 Superseded | 684.50x the stars (290,229 vs 424) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 408 | 🔻 Superseded | 2.20x the stars (898 vs 408) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | mobile-remote-control | 400 | 🔻 Superseded | 34.34x the stars (13,737 vs 400) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | memory-mcp | 385 | 🔻 Superseded | 28.65x the stars (11,029 vs 385) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation | 380 | 🔻 Superseded | 72.88x the stars (27,695 vs 380) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 365 | 🔻 Superseded | 2.46x the stars (898 vs 365) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 Superseded | 59.33x the stars (19,400 vs 327) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | memory-mcp | 323 | 🔻 Superseded | 898.54x the stars (290,229 vs 323) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 309 | 🔻 Superseded | 2.91x the stars (898 vs 309) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 Superseded | 3.90x the stars (1,107 vs 284) |
| **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | memory-mcp | 265 | 🔻 Superseded | 41.62x the stars (11,029 vs 265) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 261 | 🔻 Superseded | 629.81x the stars (164,380 vs 261) |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | mobile-remote-control | 253 | 🔻 Superseded | 426.10x the stars (107,804 vs 253) |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | memory-mcp | 240 | 🔻 Superseded | 1209.29x the stars (290,229 vs 240) |
| **[KbWen/agentic-os](https://github.com/KbWen/agentic-os)** | isolation | 220 | 🔻 Superseded | 125.89x the stars (27,695 vs 220) |
| **[ndycode/oc-codex-multi-auth](https://github.com/ndycode/oc-codex-multi-auth)** | sharing | 207 | 🔻 Superseded | 93.72x the stars (19,400 vs 207) |
| **[garagon/nanostack](https://github.com/garagon/nanostack)** | mobile-remote-control | 207 | 🔻 Superseded | 520.79x the stars (107,804 vs 207) |
| **[Digital-Process-Tools/claude-remember](https://github.com/Digital-Process-Tools/claude-remember)** | isolation | 204 | 🔻 Superseded | 135.76x the stars (27,695 vs 204) |
| **[sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills)** | memory-mcp | 203 | 🔻 Superseded | 54.33x the stars (11,029 vs 203) |
| **[Karanjot786/agent-skills-cli](https://github.com/Karanjot786/agent-skills-cli)** | desktop-ui | 195 | 🔻 Superseded | 4.61x the stars (898 vs 195) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-27 09:54 UTC. 220 live tools · 129 candidates rejected by the quality gates.</sub>
