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

**223 tools** across **14 categories** · **52 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-20 12:56 UTC**

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

- [Sessions & Memory](#sessions-memory) — 37 tools
- [Teams & Self-hosting](#teams-self-hosting) — 28 tools
- [Desktop UI](#desktop-ui) — 27 tools
- [Parallelism](#parallelism) — 22 tools
- [Billing](#billing) — 19 tools
- [Mobile](#mobile) — 19 tools
- [Failover](#failover) — 19 tools
- [Billing](#billing) — 11 tools
- [Failover](#failover) — 10 tools
- [Providers](#providers) — 7 tools
- [Security](#security) — 7 tools
- [Sharing](#sharing) — 7 tools
- [Desktop UI](#desktop-ui) — 7 tools
- [Accounts](#accounts) — 3 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Sessions & Memory

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | One wallet, every x402 API. | 🟢 Easy · OOTB | ✅ | ✅ | 5.3k 🚀 +135/d | **87** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 21.8k 🚀 +389/d | **86** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 24.1k 🚀 +68/d | **78** |
| 🏆 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 10.6k 🚀 +137/d | **78** |
| 🏆 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 2.7k 🚀 +165/d | **78** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.4k 🚀 +21/d | **68** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 10k 🚀 +66/d | **66** |
| ✅ **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | English \| 简体中文 \| 日本語 \| العربية \| Español \| 한국어 \| فارسی XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 19k | **64** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.8k 🚀 +16/d | **63** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 8.2k 🚀 +16/d | **63** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k | **62** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.9k 🚀 +14/d | **60** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.5k 🚀 +19/d | **60** |
| 🔹 **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance 3,985 archived projects -- full source code snapshots from the game security ecosystem (prefixed ags-) | 🟢 Easy | — | — | 584 🚀 +13/d | **58** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.5k 🚀 +7/d | **57** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | Local-first memory, decision engine, and governance harness for AI agents — portable across any IDE. | 🟢 Easy | — | — | 643 | **57** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Unify engineering teams around standardized workflows and shared best practices, across modern stacks and legacy systems, while reducing technical debt. | 🟢 Turnkey · OOTB | ✅ | — | 568 | **57** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k | **55** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 680 | **55** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 395 | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Easy | — | — | 485 | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 290 | **54** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.4k 🚀 +7/d | **53** |
| 🔹 **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | Blender AI MCP Suite is an AI assistant and built-in Model Context Protocol (MCP) server for Blender that turns plain-language briefs into inspected, approved and reversible 3D scene operations — with a visual Studio wo… | 🟢 Easy | — | — | 497 🚀 +12/d | **53** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 437 | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 943 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟡 Some setup | — | — | 608 | **52** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [affaan-m/ECC](https://github.com/affaan-m/ECC), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) *(+16 more)*

*…and 7 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)

> One wallet, every x402 API.

**Core problems it solves**

- **MCP support** — *package as SKILL.md, with the*
- **GUI / desktop app** — *our machine is in this repository under the Apache-2.0*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `npm i -g vapi-network`
- Platforms mentioned: macOS, Linux
- Easy. install via npx one-liner; needs pnpm install/build; configure sign-in required; GUI application

**Facts**

- Stars: **5,329** (+134.6/day over 5d)
- Health score: **87/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-19
- Works with: Claude Code, Codex

#### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)

> English | 中文 | 繁體中文 | 日本語 | Русский

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

- Stars: **21,755** (+388.8/day over 5d)
- Health score: **86/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-19
- Works with: Claude Code, Codex

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

- Stars: **24,129** (+68.4/day over 5d)
- Health score: **78/100**
- Documentation score: **49/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-20

#### [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)

> Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes).

**Core problems it solves**

- **Model / provider routing**
- **Skills & plugins** — *# Open SEO MCP Skills: a free SEO MCP server + GEO skills for Claude*
- **MCP support** — *# Open SEO MCP Skills: a free SEO MCP server + GEO skills for Claude*
- **Cross-agent support** — *Mentions Claude Code, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 50/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux
- Some setup. needs git clone (build from source); configure sign-in required; one-click setup

**Facts**

- Stars: **10,565** (+137.2/day over 5d)
- Health score: **78/100**
- Documentation score: **43/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-27
- Works with: Claude Code, Cursor

#### [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)

> A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server.

**Core problems it solves**

- **Automatic failover**
- **Model / provider routing** — *CP host, such as Codex, Claude Code, Cursor, or OpenCode.*
- **Session persistence**
- **Memory & context** — *isting authoritative assets and require no graph database, vector database, or remote graph service.*
- **Agent runtime** — *AOCI-CODE logo — AI-Oriented Cognition Infrastructure*
- **MCP support** — *AOCI-CODE logo — AI-Oriented Cognition Infrastructure*
- **GUI / desktop app** — *ou only need a direct build, run:*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🔴 **Involved** (friction 73/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via native installer / package; needs git clone (build from source), make build; configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **2,743** (+164.6/day over 5d)
- Health score: **78/100**
- Documentation score: **74/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Teams & Self-hosting

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 108.6k 🚀 +182/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 83.9k 🚀 +245/d | **90** |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 2026-10-28 🚀 DeepTutor v1.7.0 is here! Partners and subagents — Consult live agents such as Claude Code, Codex, and Grok CLI, import past conversations, or run persistent Partners with their own memory, resources, and I… | 🟡 Some setup | — | — | 61k 🚀 +324/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 307.5k 🚀 +811/d | **89** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.cursor — login and session history managed exclusively by the Cursor CLI. | 🟡 Some setup | — | — | 9.3k 🚀 +298/d | **84** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 8.6k 🚀 +103/d | **84** |
| 🏆 **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | Autonomous penetration testing that keeps its receipts. nginx and ARTEX both on the host (binary, ./start.sh): the peer is 127.0.0.1; start ARTEX | 🔴 Involved | — | — | 12.9k 🚀 +307/d | **78** |
| 🏆 **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Comprehensive API: Langfuse is frequently used to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API. AI Gateway (beta) gives your organization one endpoint for calls… | 🟢 Easy | — | ✅ | 37.7k 🚀 +44/d | **78** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 12.3k 🚀 +50/d | **74** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 12.7k 🚀 +60/d | **74** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 52.3k 🚀 +66/d | **72** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 16.2k 🚀 +52/d | **72** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Large stores keep working: state reads page, so scopes above 64 MiB no longer fail, on iii 0.25.1. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.5k 🚀 +24/d | **70** |
| ✅ **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | LoopForge is a self-hosted workspace where your team ships software with coding agents. | 🟡 Some setup | — | — | 5.2k 🚀 +45/d | **67** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.6k 🚀 +30/d | **66** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.8k 🚀 +22/d | **65** |
| 🔹 **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Build, run and govern agents on your own servers and models: shared chat, RAG, skills, a real browser, MCP, budgets, approvals and an audit trail. | 🟢 Turnkey | — | — | 435 | **58** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.7k 🚀 +8/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.2k 🚀 +7/d | **54** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2.1k | **53** |
| 🔹 **[labsai/EDDI](https://github.com/labsai/EDDI)** | Authentication: OAuth 2.0 with Keycloak, role-based access, and enforced token audience. Open protocols. | 🟡 Some setup | — | — | 393 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for policy checks, approvals, and audit of the agent actions it mediates. | 🔴 Involved | — | — | 507 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 309 | **52** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 6k | **51** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 565 | **49** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 429 | **49** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 572 | **47** |

**Also does this:** [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [decolua/9router](https://github.com/decolua/9router), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [nexu-io/open-design](https://github.com/nexu-io/open-design)

> OpenDesign is the 1st collaborative AI design agent workspace.

**Core problems it solves**

- **Mobile access** — *read your DESIGN.md and render in a sandboxed iframe.*
- **Model / provider routing** — *No CLI installed? The BYOK proxy at POST /api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream gives you the same loop (no process spaw…*
- **API gateway / proxy** — *udio}/stream gives you the same loop (no process spawn) — paste baseUrl + apiKey + model, with presets for OpenAI, Atlas Cloud, Anthropic, Azure Open…*
- **Quota sharing / splitting**
- **Session persistence** — *ive runtime adapters for agents that OD launches directly.*
- **Skills & plugins** — *reuse it for your next release, campaign, or update.*
- **Agent runtime** — *the generated project, then reuse it for your next release, campaign, or update.*
- **MCP support** — *r next release, campaign, or update.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://open-design.ai/install.sh | sh -s <agent>`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Easy. install via npx one-liner, curl | sh installer; needs docker compose up, git clone (build from source); configure database dependency, database migration; one-click setup

**Facts**

- Stars: **108,615** (+181.6/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)

> So I built the filter I&nbsp;needed.

**Core problems it solves**

- **Model / provider routing** — *s the same in longer words.*
- **API gateway / proxy** — *s the same in longer words.*
- **Skills & plugins** — *d seeded reminders (followup-cadence.mjs, followup-seed.mjs); turn them off with follow_ups.enabled: false in config/profile.yml; employer reply clas…*
- **GUI / desktop app** — *terminal dashboard lets you browse your pipeline visually:*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 43/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx @santifer/career-ops init`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, config file

**Facts**

- Stars: **83,890** (+244.6/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

> 2026-10-28 🚀 DeepTutor v1.7.0 is here!

**Core problems it solves**

- **Multi-account switching** — *v1.5.8 — Memory: a real heap ceiling for the dev server, source installs serve a production build, bounded LLM client and index caches, and a keep-al…*
- **Multi-agent orchestration** — *ld versioned libraries with LlamaIndex, PageIndex, GraphRAG, or LightRAG, connect external knowledge sources, and learn beside documents, video, and…*
- **Workspace isolation** — *icy, adds an adaptive profile, and supports revocable device credentials with expiry and daily limits; authorized guardians can view reports, approve…*
- **Model / provider routing** — *Docker CORS recovery, DISABLESSLVERIFY across SDK providers, safer code-block citations, and optional Matrix E2EE add-on.*
- **Billing & metering** — *engine, visible truncation, and unfiltered provider choices.*
- **Usage analytics** — *Its searchable navigator links to independent pages: Personal covers Workspaces, Data migration, Appearance, and Usage statistics; Learning & convers…*
- **Session persistence** — *arer streaming conversations, persistent usage accounting, and recoverable archives with explicit permanent deletion.*
- **Memory & context** — *inese, and book creation no longer times out.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run --rm --name deeptutor \`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, pip install; needs docker run, git clone (build from source); configure environment variables, API key configuration; one-click setup

**Facts**

- Stars: **60,982** (+324.4/day over 5d)
- Health score: **90/100**
- Documentation score: **81/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Copilot

#### [affaan-m/ECC](https://github.com/affaan-m/ECC)

> Use the guided setup or native plugin commands.

**Core problems it solves**

- **Automatic failover**
- **Multi-agent orchestration** — *s and evidence live under docs/releases/.*
- **Parallel execution**
- **Workspace isolation**
- **Model / provider routing** — *shims such as /tdd and /eval live in legacy-command-shims/ for explicit opt-in only.*
- **API gateway / proxy** — *eway remaps model names, configure that in Claude Code rather than in ECC.*
- **Session persistence** — *ions/ecc/, applyTo: globs)*
- **Memory & context** — *r debugging, before continuing feature work*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx ecc-universal@2.2.3 setup`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, bunx one-liner; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **307,529** (+811.0/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [nightly-labs/openbot](https://github.com/nightly-labs/openbot)

> OpenBot is a local-first desktop workspace for persistent AI teammates.

**Core problems it solves**

- **Remote control**
- **Mobile access** — *municates with local CLI processes*
- **Workspace isolation** — *codex:doctor checks the CLI version, App Server handshake, and ChatGPT login without starting a model turn.*
- **Model / provider routing** — *ter and gives it only to the local CLI.*
- **API gateway / proxy** — *to .openbot-build/workspace-only-smoke/.*
- **Billing & metering**
- **Session persistence** — *ta-dir keeps the store in that directory*
- **Skills & plugins** — *r separately through the marketplace.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/nightly-labs/openbot/main/scripts/install-server.sh | sudo bash`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Some setup. install via curl | sh installer, native installer / package; needs docker run, git clone (build from source); configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **9,339** (+297.6/day over 5d)
- Health score: **84/100**
- Documentation score: **73/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

</details>

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 28.3k 🚀 +189/d | **81** |
| 🏆 **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | Executes via MCP — Uses Blender MCP tools when connected, never narrates UI steps | 🟡 Some setup | — | — | 4.5k 🚀 +196/d | **79** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 3,022+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 50k 🚀 +58/d | **79** |
| ✅ **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Real vs code-synthesized: held-out ROC-AUC 0.92 with whole sound families held out. Listening through a soundtrack: 93% of the sound effects placed in a 60 s film mix are detected as events (89% | 🟡 Some setup | — | — | 5.3k 🚀 +86/d | **74** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 9.4k 🚀 +44/d | **74** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 7.4k 🚀 +88/d | **73** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 10.1k 🚀 +135/d | **72** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.8k 🚀 +57/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 6.9k 🚀 +40/d | **62** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.7k 🚀 +17/d | **61** |
| 🔹 **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.9k 🚀 +18/d | **60** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. Python 3.8 or later. No extra packages. | 🟢 Turnkey | — | ✅ | 578 | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **54** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 934 | **51** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 300 | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟡 Some setup | — | — | 1.2k | **50** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor | 🔴 Involved | — | — | 788 | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 444 | **50** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 3.3k 🚀 +15/d | **49** |
| 🔹 **[pskoett/self-improving-agent](https://github.com/pskoett/self-improving-agent)** | Self-improvement skill for OpenClaw. | 🟢 Easy | — | — | 792 | **47** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.5k | **46** |

**Also does this:** [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [google/artemis](https://github.com/google/artemis), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [aipoch/open-science](https://github.com/aipoch/open-science), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) *(+23 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **28,346** (+189.2/day over 5d)
- Health score: **81/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-18
- Works with: Claude Code, Codex, OpenCode

#### [arjun988/blender-skills](https://github.com/arjun988/blender-skills)

> 94 Specialized Skills for Blender Artists.

**Core problems it solves**

- **Multi-agent orchestration** — *art styles, horror packs, worlds, moods, and gameplay genre direction.*
- **Skills & plugins** — *Website --- ## Quick Start > Marketplace listing is currently under review by Anthropic. > Install directly from GitHub in the meantime. Works with C…*
- **MCP support** — *# Blender Skills 94 Specialized Skills for Blender Artists. Transform Cursor, Claude Code, Kiro, and Codex into your Senior Technical Art team — not…*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows
- Some setup. needs git clone (build from source)

**Facts**

- Stars: **4,450** (+196.4/day over 5d)
- Health score: **79/100**
- Documentation score: **62/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-06
- Works with: Claude Code, Codex, Cursor

#### [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)

> Agentic Awesome Skills is a library of 3,022+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents.

**Core problems it solves**

- **Mobile access** — *digest-pinned 0.1.7 archive byte-identical to commit a8818c3 with self-update disabled before first use (MIT-0).*
- **Multi-agent orchestration** — *ity, and mobile attack surfaces (MIT, docs-only — helper scripts, commands, engine, and research assets not bundled).*
- **Model / provider routing** — *ommerce, travel, jobs, local business, and structured web data workflows.*
- **Usage analytics** — *-focused Claude agent skills (MIT).*
- **Memory & context** — *tomic, interlinked knowledge stores with explicit hygiene, provenance, expiry, and secret-handling boundaries (MIT).*
- **Skills & plugins** — *Agentic Awesome Skills — AI Skills & AAS Core*
- **Agent runtime** — *plete files, and keep an exact skill set you can review and reuse.***
- **MCP support** — *uptime-monitoring) - content checks confirmed from a second location, heartbeats for scheduled jobs, certificate and domain expiry, status pages and…*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure API key configuration, OAuth login flow; one-click setup

**Facts**

- Stars: **50,028** (+58.2/day over 5d)
- Health score: **79/100**
- Documentation score: **82/100**
- License: MIT
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)

> Ears for coding agents.

**Core problems it solves**

- **Skills & plugins** — */skills/ (or a project's .claude/skills/).*
- **Agent runtime** — *placed with the launch kit, plus the one CC0 recording it shows being re-made, over a*
- **MCP support** — *one line on stderr (earshot : error: ..., exit 1).*
- **Notifications** — *pes come as families of named characters: 34 motion-design categories (whooshes, swishes,*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 52/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux
- Some setup. install via pip install; needs git clone (build from source), create a Python venv; configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **5,290** (+86.4/day over 5d)
- Health score: **74/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-19
- Works with: Claude Code

#### [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)

> Your agent writes code, then forgets everything.

**Core problems it solves**

- **Multi-agent orchestration** — *ub.com/user-attachments/assets/857a2195-34b8-4720-87af-f71bca3dec92*
- **Skills & plugins** — *tion uses that agent's native capabilities, so available features such as delegation and RDD review can differ.*
- **MCP support** — *egation and RDD review can differ.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 4/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `brew install gentleman-programming/tap/gentle-ai`
- Platforms mentioned: macOS, Linux
- Turnkey. install via Homebrew install, go install; configure database migration

**Facts**

- Stars: **9,424** (+43.6/day over 5d)
- Health score: **74/100**
- Documentation score: **68/100**
- License: MIT
- Language: Go
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Parallelism

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🟡 Some setup | — | — | 142.2k 🚀 +114/d | **90** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 14.2k 🚀 +126/d | **82** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods | 🟢 Easy | — | — | 34k 🚀 +64/d | **77** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 48.9k 🚀 +50/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.4k 🚀 +23/d | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12.7k 🚀 +24/d | **68** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 28.2k 🚀 +18/d | **67** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 2.8k 🚀 +36/d | **67** |
| ✅ **[generalaction/emdash](https://github.com/generalaction/emdash)** | Emdash Classic is the open-source desktop app for running coding agents in parallel. | 🟢 Turnkey · OOTB | ✅ | — | 6.3k (+14/d) | **63** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **60** |
| 🔹 **[golutra/golutra](https://github.com/golutra/golutra)** | CLI 兼容：golutra-agent、Claude Code、Antigravity CLI、Codex CLI、Grok CLI、PI、DeepSeek Harness、Hermes Agent、Gemini CLI、Cursor CLI、GitHub Copilot CLI、OpenCode、Qwen Code、OpenClaw，以及自定义 CLI DeepSeek Harness（命令 dsh-tui；官方 @deepsee… | 🟢 Easy | — | ✅ | 3.9k (+14/d) | **58** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 722 | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 668 🚀 +8/d | **57** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Stall detection — a warning after 120 s without output, stalled after 600 s Worktrees — run each task in its own git worktree on a the-pair/… branch, then commit and push from the inspector | 🟢 Easy | — | ✅ | 391 | **57** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 513 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 335 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.5k | **53** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 979 | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 787 | **52** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 3k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 323 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [affaan-m/ECC](https://github.com/affaan-m/ECC), [getpaseo/paseo](https://github.com/getpaseo/paseo), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [Tencent/LoopForge](https://github.com/Tencent/LoopForge), [felinics/Memoh](https://github.com/felinics/Memoh), [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code), [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit), [claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection), [cordum-io/cordum](https://github.com/cordum-io/cordum) *(+5 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who…

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *the cause and re-verify before committing.*
- **Workspace isolation** — *sses; blocks below 7/10), fail-closed secret redaction, dedupe against existing issues, archive to $GSTACKSTATEROOT/projects/$SLUG/specs/ for team-co…*
- **Model / provider routing** — *t moments and where people would stop, and why a back-to-back pick between two builds measures the order, not the build*
- **Memory & context** — *voice-input aliases many skills carry, have their own pages.*
- **Skills & plugins** — *--single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup then add a "gstack"…*
- **Agent runtime** — *gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architec…*
- **MCP support** — */gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup then add a "gstack" section to CLAUDE.md that says to use the /browse sk…*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 39/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Some setup. install via native installer / package; needs git clone (build from source), go build; configure sign-in required, server/reverse-proxy setup; one-click setup

**Facts**

- Stars: **142,186** (+113.6/day over 5d)
- Health score: **90/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [openai/codex-security](https://github.com/openai/codex-security)

> Codex Security helps you find, investigate, and fix vulnerabilities in your code.

**Core problems it solves**

- **Workspace isolation** — *ackage locally in your TypeScript project:*
- **Model / provider routing**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @openai/codex-security`
- Platforms mentioned: Linux, Web
- Some setup. install via npx one-liner; needs npm install/build; configure API key configuration, sign-in required

**Facts**

- Stars: **14,211** (+126.0/day over 5d)
- Health score: **82/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Codex

#### [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

> Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods

**Core problems it solves**

- **Remote control** — *versations in a mobile-friendly UI at localhost:9876*
- **Multi-agent orchestration**
- **Workspace isolation** — *ndition Docs sweep, build-test-fix, adversarial review*
- **Session persistence** — *pl marketplace Champion Kit*
- **Skills & plugins** — *alidator and scanned by NVIDIA SkillSpector.*
- **MCP support** — *al IPs across 220+ locations, targeting by country, city, or ISP, and 24/7 support.*
- **Security & isolation** — *Timeouts, permissions, status lines*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx claude-code-templates@latest`
- Platforms mentioned: Linux, Web
- Easy. install via npx one-liner; configure database dependency, server/reverse-proxy setup

**Facts**

- Stars: **34,024** (+64.2/day over 5d)
- Health score: **77/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code

#### [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

> Understand your repository, from source code to the systems around it.

**Core problems it solves**

- **Multi-account switching** — *debase-memory-mcp install --hooks to re-enable them, or inspect the current preference with codebase-memory-mcp config get installhooks.*
- **Automatic failover** — *d without contacting support; and every teammate needs git lfs install; without it their checkout leaves a pointer file where the artifact should be,…*
- **Multi-agent orchestration** — *y and fail-open: it does not replace or block the requested tool call.*
- **Workspace isolation** — *oo, set config set watchnongit true (default false, read when the daemon starts): they are then checked on the same cadence with a file-tree scan tha…*
- **Memory & context** — *Understand your repository, from source code to the systems around it.*
- **Skills & plugins** — *- - .tar.gz (macOS/Linux) or .zip (Windows)*
- **Agent runtime** — *codebase-memory-mcp- - .tar.gz (macOS/Linux) or .zip (Windows)*
- **MCP support** — *# codebase-memory-mcp: local code intelligence for AI agents via MCP*

**Getting it running**

- Setup: 🔴 **Involved** (friction 64/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via pip install, curl | sh installer; needs kubectl apply, helm install; configure environment variables, config file

**Facts**

- Stars: **48,914** (+50.4/day over 5d)
- Health score: **73/100**
- Documentation score: **76/100**
- License: MIT
- Language: C
- Last push: 2026-11-19
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

- Stars: **34,403** (+23.2/day over 5d)
- Health score: **70/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. GitHub Copilot, Gemini (Code Assist), Antigravity (through your own agy CLI), Grok (SuperGrok) and more | 🟢 Turnkey | — | ✅ | 39.4k 🚀 +536/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 6.1k 🚀 +134/d | **84** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 20.2k 🚀 +38/d | **70** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.7k 🚀 +40/d | **68** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 10.3k 🚀 +37/d | **63** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3.8k 🚀 +21/d | **63** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k | **60** |
| 🔹 **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | Claude Code — speaks the Anthropic API, so use a provider with a native Anthropic endpoint (OpenRouter, Z.AI, FreeInference, Ollama) or a LiteLLM proxy. Codex CLI — set OPENAIBASEURL + OPENAIAPIKEY. | 🟡 Some setup | — | — | 1.1k | **57** |
| 🔹 **[Makson179/Bello](https://github.com/Makson179/Bello)** | Codex, Claude Code, OpenAI, Anthropic, OpenRouter, in any mix. | 🟢 Easy | — | — | 417 🚀 +22/d | **54** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 297 | **54** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 339 | **53** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5.2k 🚀 +10/d | **52** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 547 | **51** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 521 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Quota of the Google Antigravity clients (the new desktop App and the agy CLI): remaining share and reset time of the 5-hour and weekly windows for Gemini models and… | 🟢 Easy | — | — | 330 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 超标文档拆分（主文件留入口与判据，旧文件名都保留为入口）：lifecycle.md → lifecycle/stage-1…7，另有 provider-capabilities/、demand-sources/、playbooks/research/、playbooks/selection/、integrations/、cloudflare/ 子目录。 aaron-he-zhu/seo-geo-claude-skills（Apache… | 🟢 Easy | — | — | 313 | **51** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k | **50** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 977 | **45** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *one key that matters in the agent's own config.*
- **Multi-agent orchestration** — ***Sync** Back up to a file, or sync machines over WebDAV (Nutstore, Nextcloud…), S3, or an encrypted GitHub repository backup*
- **Model / provider routing** — *y, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to.*
- **API gateway / proxy** — *e AI · Groq · Nous Portal · xAI · OpenRouter · Vercel AI Gateway · GMI Cloud · Together · Fireworks · Fireworks Nexus · SiliconFlow · NVIDIA NIM · Mo…*
- **MCP support** — *ers it as a provider to every other agent.*
- **GUI / desktop app** — *f you use more than one agent, more than one provider, or more than one account.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 11/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://usemagpie.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via go install, curl | sh installer; configure API key configuration, config file; one-click setup

**Facts**

- Stars: **39,424** (+536.0/day over 5d)
- Health score: **91/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

#### [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)

> 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**Core problems it solves**

- **Quota & usage management**
- **API gateway / proxy** — *了提问、回答后接回原会话；Agentica 1.6.1 用 use: "acp" 跑通了多轮问答和跨进程会话续接；飞书跑通了发送、按钮回调和卡片更新；四种 Webhook 模板只在本地模拟服务上验证过，GitLab Webhook 按官方文档的格式测试，没连过真实 GitLab。*
- **Usage analytics** — *上验证过，GitLab Webhook 按官方文档的格式测试，没连过真实 GitLab。*
- **Session persistence** — *下面的性能数字 npm run benchmark ### 实测性能 Apple M5 Pro、24 GB、Node 24.21.0。*
- **MCP support** — *进到上线：审代码 → 等 CI → 合并 PR → 等部署 → 核对线上版本。*
- **Notifications** — *也失败时，保留原结论并通知你回执没有生效（通用命令没有会话，直接走这一步）。*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 19/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/KKKKhazix/agent-autoloop/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; configure API key configuration, database dependency

**Facts**

- Stars: **6,100** (+134.0/day over 5d)
- Health score: **84/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

> English · Portuguese (BR) · 한국어 · 简体中文

**Core problems it solves**

- **Multi-account switching** — *ursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TraeWork、Trae CN、TraeWork CN、Zed、ZCode 和 WorkBuddy AI，并支持多账号多实例并行运行。*
- **Quota & usage management** — *avity IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TraeWork、Trae CN、TraeWork CN、Zed、ZCode 和 WorkBuddy AI，…*
- **Automatic failover** — *aude CLI 与 Claude Desktop Gateway 第三方供应商预设、模型映射，以及从会话 JSONL 汇总真实用量的方向参考：CC Switch*
- **Multi-agent orchestration**
- **Parallel execution** — *x、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TraeWork、Trae CN、TraeWork CN、Zed、ZCode 和 WorkBuddy AI，并支持多账号多实例并行运行。*
- **Workspace isolation** — *ns/Cockpit Tools.app'），请先删除旧版本再安装：*
- **Model / provider routing** — *Codex API 服务**：在 **Grok CLI** 页面完成 OAuth 授权，再打开 **Codex → API 服务 → 添加账号**，按 **Grok** 筛选、勾选账号并保存。*
- **Multi-provider aggregation** — *어 · 🇧🇷 Português · 🇷🇺 Русский · 🇹🇷 Türkçe · 🇵🇱 Polski · 🇨🇿 Čeština · 🇸🇦 العربية · 🇻🇳 Tiếng Việt · 🇮🇩 Bahasa Indonesia*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **20,198** (+38.2/day over 5d)
- Health score: **70/100**
- Documentation score: **65/100**
- Language: Rust
- Last push: 2026-11-18
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **32,661** (+40.4/day over 5d)
- Health score: **68/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-16
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [makecindy/cindy](https://github.com/makecindy/cindy)

> Cindy is an open-source AI agent, ready out of the box and yours to shape.

**Core problems it solves**

- **Multi-account switching**
- **Remote control**
- **Mobile access** — *up and migration from a manual install.*
- **Multi-agent orchestration** — *utor setup, validation, and submission workflow*
- **Model / provider routing**
- **Billing & metering** — *supported subscription you already pay for,*
- **Usage analytics** — *cords may be able to link the new*
- **MCP support** — *TML, not just a wall of text.*

**Getting it running**

- Setup: 🔴 **Involved** (friction 65/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Involved setup. needs git clone (build from source), pnpm install/build; configure sign-in required, database migration; GUI application

**Facts**

- Stars: **10,327** (+36.6/day over 5d)
- Health score: **63/100**
- Documentation score: **55/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree. | 🟢 Turnkey · OOTB | ✅ | ✅ | 130.5k 🚀 +1028/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 115.4k 🚀 +266/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 24.5k 🚀 +84/d | **80** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | An AI assistant on your phone: say what you need, and it works your apps and the web until it's done. | 🟢 Easy | — | ✅ | 9.3k 🚀 +117/d | **80** |
| ✅ **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | 🇺🇸 EN · 🇨🇳 简中 · 🇯🇵 日本語 · 🇰🇷 한국어 · 🇫🇷 FR · 🇧🇷 PT-BR · 🇹🇷 TR · 🇮🇩 ID B sound library — already available: 774 sound effects and transitions, 31 music tracks and 85 short musical stingers, licensed and ready to use | 🟢 Easy | — | ✅ | 7.1k 🚀 +66/d | **76** |
| ✅ **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 17.8k 🚀 +70/d | **70** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2.3k 🚀 +44/d | **69** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.7k 🚀 +14/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Talk to Claude as usual. | 🟢 Easy | — | — | 5.4k 🚀 +13/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.5k 🚀 +11/d | **63** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Agent Deck runs all your AI coding agents (Claude Code, Codex, Gemini CLI, OpenCode and more) in one terminal and shows which ones are working, waiting, or done. | 🟢 Turnkey · OOTB | ✅ | — | 1.3k 🚀 +4/d | **60** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | ✅ | 5.2k | **56** |
| 🔹 **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | Dispatch AI coding agents in parallel, each in its own worktree. Mix the agents you already use — Claude Code, Codex CLI, OpenCode, Copilot CLI, Antigravity CLI, or any other terminal agent, side by side on one board. | 🟢 Easy | — | ✅ | 1.1k | **56** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | keep an always-on box — a Windows desktop, a NAS or a mini PC already run Codex, DSH or WorkBuddy on a machine you control | 🟢 Turnkey | — | ✅ | 493 | **56** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.2k | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 560 | **50** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **49** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **47** |

**Also does this:** [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [makecindy/cindy](https://github.com/makecindy/cindy), [golutra/golutra](https://github.com/golutra/golutra), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [stablyai/orca](https://github.com/stablyai/orca)

> Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree.

**Core problems it solves**

- **Multi-account switching** — *- **Dictation**: press a shortcut and talk.*
- **Remote control** — *S Apple Silicon · macOS Intel · Windows (.exe) · Linux AppImage · All builds*
- **Mobile access**
- **Multi-agent orchestration**
- **Parallel execution**
- **Workspace isolation** — *中文 · 日本語 · 한국어 · Español · Français · Português · Türkçe · Русский The AI Orchestrator for 100x builders.*
- **Agent runtime** — *e desktop apps and external browsers.*
- **Self-hostable** — *rivacy & telemetry docs for what anonymous usage data Orca collects and how to opt out.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `brew install --cask stablyai/orca/orca`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Turnkey. install via Homebrew install, native installer / package; GUI application

**Facts**

- Stars: **130,512** (+1027.6/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
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

- Stars: **115,360** (+266.2/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
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

- Stars: **24,512** (+83.6/day over 5d)
- Health score: **80/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

#### [wangzan101/Mika](https://github.com/wangzan101/Mika)

> An AI assistant on your phone: say what you need, and it works your apps and the web until it's done.

**Core problems it solves**

- **Mobile access** — *Several demos use apps popular in China: WeChat is the main messaging app there, and Xiaohongshu (RED) is a lifestyle and social platform.*
- **Model / provider routing** — *resets for DeepSeek, 通义千问, Kimi, 智谱, 智谱 Coding Plan, 硅基流动, 火山方舟, MiniMax, 阶跃星辰, 腾讯混元, 百度千帆, OpenRouter, OpenCode Go, Anthropic, Gemini, OpenAI, xAI,…*
- **Billing & metering**
- **MCP support** — *nd computing A Linux sandbox per conversation runs Python, Node and shell on the files you send (arm64)*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: Linux, Android, Web
- Easy. configure API key configuration, sign-in required; explicitly no coding required

**Facts**

- Stars: **9,258** (+117.0/day over 5d)
- Health score: **80/100**
- Documentation score: **33/100**
- License: Apache-2.0
- Language: Kotlin
- Last push: 2026-11-20
- Works with: OpenCode

#### [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)

> 🇺🇸 EN · 🇨🇳 简中 · 🇯🇵 日本語 · 🇰🇷 한국어 · 🇫🇷 FR · 🇧🇷 PT-BR · 🇹🇷 TR · 🇮🇩 ID

**Core problems it solves**

- **Mobile access** — *n language—it writes prompts, breaks your idea into shots, and generates videos in batches, keeping the same character or product consistent across s…*
- **Multi-agent orchestration** — *al animations are in preparation.*
- **MCP support** — *erates videos in batches, keeping the same character or product consistent across shots.*
- **Self-hostable** — *with reusable assets; precise timeline pacing, layout control, and easy local fine-tuning.*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: Linux, iOS, Android, Web
- Easy. GUI application

**Facts**

- Stars: **7,144** (~65.5/day lifetime average)
- Health score: **76/100**
- Documentation score: **70/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex

</details>

## Failover

*Agent runtime*

This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 156.4k 🚀 +133/d | **90** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm turns any coding agent into a video agent, with editors to change anything it makes. | 🟢 Turnkey · OOTB | ✅ | ✅ | 8.6k 🚀 +264/d | **86** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 21.6k 🚀 +433/d | **85** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. 2026-11-12 · 33 new styles: 99 now, in 15 categories sorted by what the picture looks like, and the gallery in English and Chinese, wit… | 🟡 Some setup | — | ✅ | 18.9k 🚀 +489/d | **85** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Rom… | 🟢 Easy | — | — | 6.3k 🚀 +109/d | **84** |
| 🏆 **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** | Point it at your app: it records what the original does, your coding agent writes the Rust one piece at a time, and every piece is checked against that recording before it moves on. | 🟢 Easy | — | — | 6k 🚀 +1500/d | **83** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 24k 🚀 +167/d | **78** |
| ✅ **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | antislop is a rulebook an AI coding agent reads every session. | 🟢 Turnkey | — | — | 9.7k 🚀 +76/d | **75** |
| 🔹 **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 5.3k 🚀 +38/d | **60** |
| 🔹 **[vaibhav-space/my-ai-coding-workflow](https://github.com/vaibhav-space/my-ai-coding-workflow)** | What it is: one global rules file (CLAUDE.md) and three prompts: plan, critique the plan, audit the result. | 🟡 Some setup | — | — | 303 🚀 +61/d | **60** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.8k | **58** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 557 | **55** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 360 | **53** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 315 | **53** |
| 🔹 **[chipfighter/context-attachment-manager](https://github.com/chipfighter/context-attachment-manager)** | An agent normally sends every earlier image again with each message, so a long chat with many images gets slow and can stop going through. | 🟢 Easy | — | — | 808 | **52** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 775 | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 727 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 497 | **46** |
| 👀 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 444 | **41** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [garrytan/gstack](https://github.com/garrytan/gstack), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse), [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) *(+27 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [anthropics/claude-code](https://github.com/anthropics/claude-code)

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Core problems it solves**

- **Agent runtime** — *Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, e…*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://claude.ai/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via Homebrew install, winget install; needs npm install/build

**Facts**

- Stars: **156,404** (+133.2/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

#### [openfilm/openfilm](https://github.com/openfilm/openfilm)

> OpenFilm turns any coding agent into a video agent, with editors to change anything it makes.

**Core problems it solves**

- **Agent runtime**
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `npx skills add openfilm/openfilm`
- Platforms mentioned: macOS, Windows, Web
- Turnkey. install via npx one-liner; GUI application

**Facts**

- Stars: **8,638** (+264.4/day over 5d)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex

#### [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

> Develop ideas with context and review documents with fresh eyes.

**Core problems it solves**

- **Multi-agent orchestration** — *xed command (#220), but 1.4.8 does not (#196), so keep the prefix.*
- **Agent runtime** — *d standards with /egm-review-loop.*
- **GUI / desktop app**
- **Notifications**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Easy. GUI application

**Facts**

- Stars: **21,575** (+433.0/day over 5d)
- Health score: **85/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-19
- Works with: Claude Code, Codex

#### [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

> 99 film styles for your coding agent.

**Core problems it solves**

- **Model / provider routing** — *e Opus 5.5, apart from two styles contributed from outside: Memphis Diorama by @EianLu and Crayon World 3D by @2nd1st.*
- **Agent runtime**
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 44/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Linux
- Some setup. needs git clone (build from source); GUI application

**Facts**

- Stars: **18,929** (+488.6/day over 5d)
- Health score: **85/100**
- Documentation score: **58/100**
- License: NOASSERTION
- Language: JavaScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex

#### [qybaihe/bla](https://github.com/qybaihe/bla)

> English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Roman Urdu · Română

**Core problems it solves**

- **Multi-agent orchestration** — *ur coding agent (**Claude Code, Cursor, Codex, Windsurf, Gemini CLI, GitHub Copilot CLI, VS Code, OpenCode, Antigravity**):*
- **Agent runtime** — *al property and release artifacts.*
- **MCP support** — *aliano · Ελληνικά · മലയാളം · Roman Urdu · Română*
- **GUI / desktop app** — *lyzer's default limits (primitive-candidates, alias-selections, ASAR 16 MiB header, WASM Wabt representation, SQLite virtual column eval, Model 32-le…*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx bla-agents harden .            # writes a partial mirror to .bla-hardened/ — nothing ships yet`
- Platforms mentioned: macOS, Windows, Linux, Android
- Easy. install via npx one-liner; needs npm install/build, go build; configure config.json/yaml/toml, database dependency; one-click setup

**Facts**

- Stars: **6,287** (+109.2/day over 5d)
- Health score: **84/100**
- Documentation score: **79/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 69k 🚀 +347/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.4k 🚀 +185/d | **84** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 46.3k 🚀 +61/d | **73** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：由一部 20 章小说改编，拆成 20 镜逐镜生成后剪成成片，字幕、系统面板与音效在剪辑阶段叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 4.6k 🚀 +57/d | **70** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends. | 🟢 Easy | — | ✅ | 5.6k 🚀 +5/d | **65** |
| 🔹 **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.4k 🚀 +14/d | **61** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 12.2k 🚀 +18/d | **54** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 861 | **51** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 417 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 458 | **44** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [superdesigndev/treg](https://github.com/superdesigndev/treg), [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [Tencent/LoopForge](https://github.com/Tencent/LoopForge), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [cita-777/metapi](https://github.com/cita-777/metapi), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills) *(+4 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

> An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand.

**Core problems it solves**

- **Parallel execution** — *board a brand once, save the result as a named profile, then add a .diagram-design marker containing profile: to each client project.*
- **Billing & metering** — *t; Treemap covers marimekko; Dependency covers arc diagram.*
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

- Stars: **69,006** (+346.8/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)

> 244 pixel art effects and animations, every one a small piece of code.

**Core problems it solves**

- **Billing & metering** — *iming is plain data: read slash.act, or meta.pixelfx.act in a sprite sheet's*
- **Skills & plugins** — *e) gives you each part drawn on its own.*
- **Agent runtime**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npm i -g @patchgg/cli      # or: curl -fsSL https://patch.gg/install.sh | sh`
- Platforms mentioned: Windows, Web
- Turnkey. install via curl | sh installer

**Facts**

- Stars: **8,448** (+184.8/day over 5d)
- Health score: **84/100**
- Documentation score: **42/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-13
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

- Stars: **46,349** (+60.8/day over 5d)
- Health score: **73/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)

> 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：由一部 20 章小说改编，拆成 20 镜逐镜生成后剪成成片，字幕、系统面板与音效在剪辑阶段叠加。视频生成成本约 40 元。

**Core problems it solves**

- **Billing & metering**
- **Skills & plugins** — *eck.py（已剪辑剧集再跑一次 edit_tool.py check）核对即可。*
- **Agent runtime** — *github.com/user-attachments/assets/f67e2e04-52e7-42a9-a4a0-e2864ff0f51e*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add zenstory-ai/drama-skills -y -g`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **4,560** (+57.2/day over 5d)
- Health score: **70/100**
- Documentation score: **54/100**
- License: MIT
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code, Codex

#### [aipoch/open-science](https://github.com/aipoch/open-science)

> AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends.

**Core problems it solves**

- **Billing & metering** — *Why does the model connection test fail? A: Check the API Key for missing characters or spaces, verify the Base URL and region, use the provider's ex…*
- **Skills & plugins** — *, resources, and permissions yourself; cloud jobs may incur charges.*
- **MCP support** — *this README illustrate the workflow.*
- **Security & isolation**
- **GUI / desktop app** — *figure or table back to its inputs.*
- **Notifications** — *untime checks and test your model connection.*
- **Cross-agent support** — *Mentions Amp, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `brew install --cask open-science`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, sign-in required; GUI application

**Facts**

- Stars: **5,553** (+4.8/day over 5d)
- Health score: **65/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Cline / Roo

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 7.3k 🚀 +76/d | **78** |
| ✅ **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 7.3k 🚀 +56/d | **76** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 9.8k 🚀 +48/d | **69** |
| ✅ **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | The agent skills I use every day, cleaned up so anyone can use them. | 🟡 Some setup | — | — | 4.2k 🚀 +80/d | **65** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.8k 🚀 +6/d | **62** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2.1k 🚀 +7/d | **61** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.9k | **56** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.6k | **55** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 8k 🚀 +6/d | **49** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 527 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [garrytan/gstack](https://github.com/garrytan/gstack), [openai/codex](https://github.com/openai/codex), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [superdesigndev/treg](https://github.com/superdesigndev/treg), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development), [oleksiijko/pmb](https://github.com/oleksiijko/pmb) *(+7 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)

> 简体中文 | English | Bahasa Indonesia

**Core problems it solves**

- **Automatic failover** — *dex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。*
- **Skills & plugins** — *e glad to see this approach to art animation used in another open-source project, and thank the Open Design team.*
- **Agent runtime** — *简体中文 English Bahasa Indonesia*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add alchaincyf/huashu-art-motion`
- Turnkey. install via npx one-liner

**Facts**

- Stars: **7,325** (+76.0/day over 5d)
- Health score: **78/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-18
- Works with: Claude Code

#### [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)

> An agent skill that finds where a photo was taken — and shows its work.

**Core problems it solves**

- **Automatic failover** — *the complete skill folder, including data/ and the helper modules in scripts/.*
- **Skills & plugins** — *Agent Skill: one folder holding SKILL.md, scripts/, references/ and data/.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add Oldcircle/geo-sleuth`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via npx one-liner, uvx one-liner; needs git clone (build from source)

**Facts**

- Stars: **7,334** (+56.2/day over 5d)
- Health score: **76/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-11-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [maximhq/bifrost](https://github.com/maximhq/bifrost)

> Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API.

**Core problems it solves**

- **Automatic failover** — *eway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API.*
- **Model / provider routing**
- **API gateway / proxy** — *y to build AI applications that never go down*
- **Usage analytics** — *pport - Support for text, images, audio, and streaming, all behind a common interface.*
- **Skills & plugins** — *Caching - Intelligent response caching based on semantic similarity to reduce costs and latency*
- **MCP support** — *s failover between providers and models with zero downtime*
- **GUI / desktop app** — *semantic caching, and enterprise-grade features.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx -y @maximhq/bifrost`
- Platforms mentioned: Linux, Web
- Some setup. install via npx one-liner; needs docker run; configure environment variables, API key configuration

**Facts**

- Stars: **9,804** (+47.8/day over 5d)
- Health score: **69/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-11-20

#### [t3dotgg/tstack](https://github.com/t3dotgg/tstack)

> The agent skills I use every day, cleaned up so anyone can use them.

**Core problems it solves**

- **Automatic failover**
- **Multi-agent orchestration** — *file-pr, babysit-pr, and modernize use leaving-pr-comments.*
- **Model / provider routing** — *sit-pr, and modernize use leaving-pr-comments.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Some setup. needs git clone (build from source)

**Facts**

- Stars: **4,219** (+80.4/day over 5d)
- Health score: **65/100**
- Documentation score: **25/100**
- License: MIT
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex

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

- Stars: **27,814** (+6.0/day over 5d)
- Health score: **62/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 156k 🚀 +288/d | **94** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.8k 🚀 +23/d | **68** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.4k 🚀 +6/d | **57** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DeepSeek Harness Desktop 是基于官方 DSH 的社区开源桌面工作台，用于对话、项目、插件和任务自动化。 | 🟢 Turnkey · OOTB | ✅ | ✅ | 946 | **56** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 779 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 441 | **50** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 605 | **45** |

**Also does this:** [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

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

- Stars: **155,990** (+288.0/day over 5d)
- Health score: **94/100**
- Documentation score: **78/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

#### [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)

> An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔…

**Core problems it solves**

- **Quota & usage management**
- **Workspace isolation** — *asel --no-skills，随后用 hermes --profile easel setup 配置。*
- **Model / provider routing**
- **Multi-provider aggregation**
- **API gateway / proxy** — *API 不提供向量模型，请单独配置 Embedding API；否则 OpenClaw 会默认请求 text-embedding-3-small，可能得到“模型不可用”。*
- **Memory & context**
- **Skills & plugins** — *list、多平台格式适配；小红书、抖音、快手、知乎、B 站、微信视频号、微信公众号、推特 X、掘金、今日头条登录与发布；内容日历回写、账号数据、评论洞察（掘金走公开 JSON 接口、X 走网页 DOM 采集）、内容复盘、ROI 与画像记忆*
- **GUI / desktop app** — *后安装器会创建项目内 .venv，安装 Python/Node 依赖、前端生产包和 Playwright Chromium，并使用独立的 easel OpenClaw profile。*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, native installer / package; needs git clone (build from source); configure API key configuration; Chinese: beginner/one-click framing

**Facts**

- Stars: **4,813** (+23.2/day over 5d)
- Health score: **68/100**
- Documentation score: **80/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-17
- Works with: Claude Code, Codex, OpenCode

#### [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)

> The unified interface for agent harnesses.

**Core problems it solves**

- **Model / provider routing**
- **Multi-provider aggregation** — *The unified interface for agent harnesses.*
- **Session persistence** — *s, retrieve results, and switch harnesses through one API.*
- **Skills & plugins** — *a recorded run and the image it made*
- **MCP support** — *ing that leaves the sandbox, the response, the stream, the trace and the stored record, even when the agent prints it.*
- **Self-hostable** — *h a browsable copy at /v1/docs.*
- **Cross-agent support** — *Mentions Aider, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run -d --name harnessrouter \`
- Platforms mentioned: Web
- Some setup. needs docker run; configure API key configuration, sign-in required

**Facts**

- Stars: **4,394** (+6.4/day over 5d)
- Health score: **57/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Aider, Cline / Roo

#### [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)

> DeepSeek Harness Desktop 是基于官方 DSH 的社区开源桌面工作台，用于对话、项目、插件和任务自动化。

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

- Stars: **946** (+2.4/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-20
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

- Stars: **779** (+0.8/day over 5d)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-16
- Works with: Claude Code, Cursor

</details>

## Security

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | A chat ends with an answer. | 🟡 Some setup | — | — | 5.3k 🚀 +242/d | **85** |
| 🏆 **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Antigravity CLI support is experimental: it was tested against agy 1.5.1 and 1.5.2 on Windows 11, opencode support is experimental: it was tested on 1.19.5 and 2.2.0 only, and not in the | 🟢 Easy | — | ✅ | 7.8k 🚀 +334/d | **84** |
| ✅ **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 3.4k 🚀 +91/d | **76** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 481 🚀 +21/d | **57** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | The World's First Git for AI Agent Memory | 🔴 Involved | — | — | 630 | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **50** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [leepokai/Codync](https://github.com/leepokai/Codync), [slopus/happy](https://github.com/slopus/happy), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [yc-software/qm](https://github.com/yc-software/qm), [automazeio/ccpm](https://github.com/automazeio/ccpm), [labsai/EDDI](https://github.com/labsai/EDDI), [cordum-io/cordum](https://github.com/cordum-io/cordum), [robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)

> A chat ends with an answer.

**Core problems it solves**

- **Mobile access**
- **Multi-agent orchestration** — *ide a team workspace and adds what they don't have: issues that flow from request to execution to sign-off, independent AI review, plugin review and…*
- **Parallel execution** — *The requester and the assignee or their agent A request goes to a colleague, their agent does the work, the requester signs off*
- **Billing & metering** — *ose requests to its operator.*
- **Skills & plugins** — *n sets the method, process, rules and what counts as done A review plugin tells the agent which checks to run and what evidence to attach*
- **Agent runtime** — *sn't stay in one person's chat history.*
- **Security & isolation** — *and adds the layer they don't have: one shared issue pool from request to sign-off, acceptance criteria built into every issue, an independent AI rev…*
- **Self-hostable** — *Runners and skills are not a general-purpose sandbox: actual isolation depends on the harness and your environment.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 42/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via native installer / package; needs git clone (build from source); configure API key configuration, sign-in required; GUI application

**Facts**

- Stars: **5,315** (~241.6/day lifetime average)
- Health score: **85/100**
- Documentation score: **84/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-20
- Works with: Codex, OpenCode, Qwen Code

#### [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)

> Aaron J.

**Core problems it solves**

- **Multi-agent orchestration**
- **Session persistence**
- **Agent runtime** — *# TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents*
- **MCP support** — *Agent Tool pruning leaves out Written to --- --- --- Claude Code single tools .claude/settings.local.json Codex capability packages .codex/config.tom…*
- **Security & isolation** — *is repository; add --global for every repository*
- **GUI / desktop app** — *n the classic CLI and one-shot runs only.*
- **Notifications** — *s reply Esc in the final reply Ctrl+C*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner; needs git clone (build from source); configure environment variables, config.json/yaml/toml; GUI application

**Facts**

- Stars: **7,819** (+334.2/day over 5d)
- Health score: **84/100**
- Documentation score: **61/100**
- License: MIT
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

#### [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)

> Continue using your DeepSeek Harness instance from a phone, computer, or browser.

**Core problems it solves**

- **Automatic failover** — *public IP is required on the Harness Host.*
- **Remote control** — *while preserving messages and tool status.*
- **Mobile access** — ***Bot mode**, powered by Fei2411/DS-Bot.*
- **Parallel execution** — *ther tools through ACP integrations, with remote file browsing and terminals.*
- **Model / provider routing** — *Claude and Hermes also support direct file and terminal access, subject to the Host's workspace boundaries and terminal settings. Setup and adapter d…*
- **Security & isolation** — *onversation models with the same smooth workflow as local use.*
- **Self-hostable** — *once, and use **Bot mode**, powered by Fei2411/DS-Bot.*
- **Team collaboration** — *nt keeps its own workspaces and sessions; only session translation for DSH is performed, without writing to Harness storage.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via native installer / package; configure sign-in required, process manager

**Facts**

- Stars: **3,401** (+91.4/day over 5d)
- Health score: **76/100**
- Documentation score: **61/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)

> Leave the agent working.

**Core problems it solves**

- **Remote control**
- **Agent runtime**
- **MCP support** — *is online in the console, then dispatch*
- **Security & isolation**
- **Cross-agent support** — *Mentions Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://emisar.dev/install.sh \`
- Platforms mentioned: macOS, Linux, Web
- Easy. install via Homebrew install, native installer / package; configure OAuth login flow, database dependency

**Facts**

- Stars: **481** (+21.0/day over 5d)
- Health score: **57/100**
- Documentation score: **53/100**
- License: NOASSERTION
- Language: Elixir
- Last push: 2026-11-20
- Works with: Codex, Cursor

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

- Stars: **8,457** (+0.0/day over 10d)
- Health score: **56/100**
- Documentation score: **28/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-22
- Works with: Claude Code, Codex

</details>

## Sharing

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 169.4k 🚀 +202/d | **96** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 8.6k 🚀 +571/d | **89** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 26k 🚀 +607/d | **88** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal. | 🟢 Turnkey · OOTB | ✅ | ✅ | 10.6k 🚀 +228/d | **85** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.4k 🚀 +31/d | **67** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 469 | **55** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k | **51** |

**Also does this:** [yetone/cumora](https://github.com/yetone/cumora), [ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)

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

- Stars: **169,449** (+202.0/day over 5d)
- Health score: **96/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

> Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output.

**Core problems it solves**

- **Automatic failover** — *It falls back to the CPU encoder — reported in the result's hw.fallback/hw.notes — only when VideoToolbox itself refuses a job (any other ffmpeg fail…*
- **Multi-agent orchestration** — *contract and the test suite (tests/testcontract.py,*
- **API gateway / proxy** — *-pass encode and measures it ; --preset copy --repair remuxes a damaged file (timestamps regenerated, corrupt packets dropped) and counts the errors…*
- **Memory & context** — *ly selected material, trim before reframing, adding*
- **Skills & plugins** — *otage/: clips AI-generated with Google Veo (the people and places do not exist) and a few shot on a phone.*
- **Agent runtime** — *Give your coding agent a video editor.*
- **MCP support** — *Give your coding agent a video editor.*
- **Security & isolation** — *ticcodes); tools that draw text name the font face they drew with (fontused; libass draws a glyph that face lacks from another, not named).*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx ffmpeg-skill`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via npx one-liner, pip install

**Facts**

- Stars: **8,615** (+571.4/day over 5d)
- Health score: **89/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-20
- Works with: Claude Code, Codex, Gemini CLI, Cursor

#### [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

> The open-source Grok Bot alternative: your own team of AI bots, in a chat app.

**Core problems it solves**

- **Mobile access** — *protected by pairing, an existing*
- **Multi-agent orchestration** — *n/ macOS, Windows, and Ubuntu shells with an embedded harness and platform capabilities; Apple speech stays macOS-only, Ubuntu Xorg has opt-in local…*
- **Model / provider routing** — *configuration switches, defaults and model-call implications, see Feature switches.*
- **API gateway / proxy** — *via docs/custom-mcp-servers.md.*
- **Usage analytics** — *d model-call implications, see Feature switches.*
- **Skills & plugins**
- **MCP support** — *ure bots/channels/tasks, send work, wait for completion, switch models, and interrupt turns.*
- **Security & isolation** — *MCP header values in plaintext (a key a bot set from a secret card is kept*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g openmausbot`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via npx one-liner, global npm install; needs git clone (build from source), pnpm install/build; configure API key configuration, config.json/yaml/toml; explicitly no coding required

**Facts**

- Stars: **26,046** (+607.0/day over 5d)
- Health score: **88/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-20
- Works with: Codex, OpenCode, Cursor, Cline / Roo

#### [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)

> LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal.

**Core problems it solves**

- **Model / provider routing** — *ose your models, then start a session with what you want to understand.*
- **API gateway / proxy** — *ose your models, then start a session with what you want to understand.*
- **Memory & context** — *d of just giving you an explanation, it uses your answers and thinking to decide what you need next.*
- **GUI / desktop app** — *tainties, and reactions in your own words.*
- **Voice input** — *let you explain your reasoning, uncertainties, and reactions in your own words.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **10,639** (+227.6/day over 5d)
- Health score: **85/100**
- Documentation score: **51/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-12
- Works with: Claude Code

#### [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)

> A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions.

**Core problems it solves**

- **Automatic failover** — *e permission requests show up with Allow / Deny / Always; AskUserQuestion prompts show the choices right in the notch (single or multi-select, up to…*
- **Remote control** — *too? That's Botan: the founders list is open.*
- **Mobile access** — *ries, no hook files, no recap history.*
- **Model / provider routing** — *open the exact terminal window of a session (macOS).*
- **Agent runtime**
- **Security & isolation** — *See what Claude is editing, live in the notch: each file modification shows the file name and +N −M counts in the ticker, tap to read the full diff*
- **GUI / desktop app** — *Coucou on the iPhone, allow notifications, and start a Claude Code session on the Mac.*
- **Notifications** — *your iPhone's Lock Screen and Dynamic Island with the agent's state, then comes back to the notch when you unlock.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap louis-cfm/coucou https://github.com/Louis-CFM/coucou`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **7,358** (+31.4/day over 5d)
- Health score: **67/100**
- Documentation score: **67/100**
- License: MIT
- Language: Swift
- Last push: 2026-11-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 228.2k 🚀 +239/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 17.4k 🚀 +198/d | **89** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.4k 🚀 +7/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 499 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 806 | **54** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 700 🚀 +14/d | **53** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [yetone/magpie](https://github.com/yetone/magpie), [openai/codex](https://github.com/openai/codex), [openfilm/openfilm](https://github.com/openfilm/openfilm), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [qybaihe/bla](https://github.com/qybaihe/bla), [getpaseo/paseo](https://github.com/getpaseo/paseo), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse) *(+42 more)*

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

- Stars: **228,158** (+239.4/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-20
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

#### [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)

> Sketch, constrain, and build solids with a parametric feature timeline.

**Core problems it solves**

- **MCP support** — *constrain, and build solids with a parametric feature timeline.*
- **GUI / desktop app** — *lidcraft -- solidcraft-cli mcp.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **17,393** (+198.2/day over 5d)
- Health score: **89/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-20
- Works with: Claude Code

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

- Stars: **15,448** (+6.8/day over 5d)
- Health score: **58/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

#### [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)

> A free, open-source app to manage all your AI coding agents — desktop, CLI, or web.

**Core problems it solves**

- **Multi-agent orchestration**
- **Workspace isolation** — *ically discovers every agent's config files — both global and per-project.*
- **Agent runtime** — *eractions throughout the app make daily use feel alive.*
- **MCP support** — *nage everything across every agent, from one place.*
- **GUI / desktop app** — *ommand-line interface (hk) for terminal-first workflows, available on macOS, Linux, and Windows:*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 2/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/RealZST/HarnessKit/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via curl | sh installer, PowerShell irm | iex installer; configure environment variables, config file; one-click setup

**Facts**

- Stars: **499** (+0.6/day over 5d)
- Health score: **56/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)

> 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。

**Core problems it solves**

- **Agent runtime**
- **GUI / desktop app** — *be-rs 可自由正交组合，六种搭配均可开箱即用。*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add https://github.com/zhinkgit/embeddedskills -g -y`
- Platforms mentioned: Windows, Linux
- Turnkey. install via npx one-liner, native installer / package; needs git clone (build from source), cmake build; Chinese: beginner/one-click framing

**Facts**

- Stars: **806** (+1.4/day over 5d)
- Health score: **54/100**
- Documentation score: **49/100**
- License: MIT
- Language: Python
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Cursor

</details>

## Accounts

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 136k 🚀 +123/d | **89** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 568 | **54** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [cita-777/metapi](https://github.com/cita-777/metapi), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

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

- Stars: **135,965** (+122.6/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-20
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)

> codex-auth is a command-line tool for switching Codex accounts.

**Core problems it solves**

- **Multi-account switching** — *nction MenuComplete to your profile.*
- **GUI / desktop app** — *napshot from hours ago instead of your latest state.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npm install -g @loongphy/codex-auth`
- Easy. install via npx one-liner, global npm install; needs npm install/build; configure environment variables, sign-in required; GUI application

**Facts**

- Stars: **2,881** (+2.4/day over 5d)
- Health score: **56/100**
- Documentation score: **38/100**
- License: MIT
- Language: Zig
- Last push: 2026-11-18
- Works with: Codex

#### [ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)

> codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI.

**Core problems it solves**

- **Multi-account switching** — *OpenAI install keeps owning that command.*
- **Automatic failover** — *pports Global and US endpoints per credential.*
- **API gateway / proxy** — *h, including the local real-time web dashboard.*
- **GUI / desktop app** — *witch, forecast, rotation, fix, ...).*
- **Voice input** — *let health- and quota-aware hybrid selection rotate for you.*
- **Cross-agent support** — *Mentions Codex, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 41/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npm i -g codex-multi-auth`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. configure OAuth login flow, sign-in required; GUI application

**Facts**

- Stars: **568** (+0.4/day over 5d)
- Health score: **54/100**
- Documentation score: **63/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Codex, OpenCode

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Sharing | Accounts, Billing |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Teams & Self-hosting | Failover, Sessions & Memory |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Failover |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Desktop UI, Parallelism |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | Desktop UI |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Parallelism | Failover, Failover |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Teams & Self-hosting | Failover |
| **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | Teams & Self-hosting | Failover, Sessions & Memory |
| **[openai/codex](https://github.com/openai/codex)** | Accounts | Desktop UI, Failover |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Sharing | Desktop UI, Sessions & Memory |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Teams & Self-hosting | Parallelism, Sessions & Memory |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile | Security, Sessions & Memory |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Sharing | Desktop UI, Teams & Self-hosting |
| **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | Failover | Desktop UI |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Failover | Desktop UI, Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Failover | Desktop UI, Failover |
| **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | Security | Desktop UI, Teams & Self-hosting |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Teams & Self-hosting | Mobile, Providers |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Teams & Self-hosting | Billing, Failover |
| **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Billing | Failover |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Security | Desktop UI, Sessions & Memory |
| **[qybaihe/bla](https://github.com/qybaihe/bla)** | Failover | Desktop UI |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | Sessions & Memory |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Desktop UI, Parallelism |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | Desktop UI, Failover |
| **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | Teams & Self-hosting | Billing, Desktop UI |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Sessions & Memory | Failover |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Failover | Failover |
| **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Teams & Self-hosting | Desktop UI, Failover |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Sessions & Memory | Failover, Failover |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Parallelism | Desktop UI, Security |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | Mobile | Desktop UI |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Security | Mobile, Teams & Self-hosting |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams & Self-hosting | Desktop UI, Parallelism |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Desktop UI | Failover |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Teams & Self-hosting | Failover, Sessions & Memory |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Accounts, Billing |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Parallelism | Desktop UI, Sessions & Memory |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Teams & Self-hosting | Failover |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams & Self-hosting | Failover, Security |
| **[google/artemis](https://github.com/google/artemis)** | Mobile | Desktop UI |
| **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Billing | Failover |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Parallelism | Desktop UI, Desktop UI |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams & Self-hosting | Billing, Sessions & Memory |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Accounts, Billing |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Failover | Failover |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, Security |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Failover |
| **[decolua/9router](https://github.com/decolua/9router)** | Billing | Teams & Self-hosting |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Sharing | Failover, Mobile |
| **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | Teams & Self-hosting | Billing, Parallelism |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Parallelism | Desktop UI, Failover |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Parallelism | Desktop UI, Failover |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Teams & Self-hosting | Desktop UI, Failover |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | Desktop UI |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI, Security |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Sessions & Memory | Desktop UI |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Desktop UI, Failover |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Billing | Desktop UI, Mobile |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Billing, Teams & Self-hosting |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Security, Sessions & Memory |
| **[generalaction/emdash](https://github.com/generalaction/emdash)** | Parallelism | Desktop UI |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | Failover, Failover |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Desktop UI | Desktop UI, Failover |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Failover | Desktop UI |
| **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | Billing | Billing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Parallelism | Desktop UI, Sessions & Memory |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile | Desktop UI, Sessions & Memory |
| **[vaibhav-space/my-ai-coding-workflow](https://github.com/vaibhav-space/my-ai-coding-workflow)** | Failover | Desktop UI, Desktop UI |
| **[golutra/golutra](https://github.com/golutra/golutra)** | Parallelism | Mobile, Sessions & Memory |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Failover | Desktop UI, Desktop UI |
| **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | Sessions & Memory | Desktop UI, Desktop UI |
| **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Teams & Self-hosting | Desktop UI, Failover |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams & Self-hosting | Failover, Security |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Failover, Sessions & Memory |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Sessions & Memory | Desktop UI, Failover |
| **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | Billing | Failover, Teams & Self-hosting |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Parallelism | Failover, Sessions & Memory |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Parallelism | Desktop UI, Mobile |
| **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Sessions & Memory | Desktop UI |
| **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Parallelism | Desktop UI |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams & Self-hosting | Parallelism, Sessions & Memory |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Failover | Desktop UI, Desktop UI |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Failover, Failover |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | Mobile | Desktop UI, Parallelism |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Billing, Desktop UI |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Parallelism | Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Parallelism |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Failover | Desktop UI, Sessions & Memory |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Sessions & Memory | Desktop UI, Desktop UI |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Sessions & Memory | Desktop UI |
| **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | Desktop UI | Parallelism |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Failover | Desktop UI |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Sharing | Billing, Parallelism |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | Sessions & Memory | Desktop UI, Failover |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Parallelism | Desktop UI, Desktop UI |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams & Self-hosting | Desktop UI, Sharing |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI, Parallelism |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | Accounts | Sharing |
| **[Makson179/Bello](https://github.com/Makson179/Bello)** | Billing | Desktop UI |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Desktop UI, Sessions & Memory |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Sessions & Memory | Desktop UI, Failover |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Parallelism | Desktop UI, Security |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Accounts, Billing |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Parallelism | Desktop UI, Desktop UI |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Sessions & Memory | Failover, Teams & Self-hosting |
| **[labsai/EDDI](https://github.com/labsai/EDDI)** | Teams & Self-hosting | Security, Sessions & Memory |
| **[Swival/swival](https://github.com/Swival/swival)** | Failover | Failover |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Billing | Mobile, Sessions & Memory |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI, Sessions & Memory |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI, Failover |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Sessions & Memory | Desktop UI, Failover |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Parallelism | Desktop UI, Failover |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Teams & Self-hosting | Parallelism, Security |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams & Self-hosting | Parallelism, Sharing |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Parallelism, Sharing |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Sharing | Desktop UI, Mobile |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Sessions & Memory | Desktop UI, Failover |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Sessions & Memory | Desktop UI |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | Security | Sessions & Memory |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Providers, Teams & Self-hosting |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Billing | Desktop UI |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Billing | Failover, Sessions & Memory |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Billing | Billing, Teams & Self-hosting |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Billing, Failover |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Failover |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Parallelism | Billing, Desktop UI |
| **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Failover | Failover |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Desktop UI, Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Security | Billing, Teams & Self-hosting |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Parallelism, Sessions & Memory |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Desktop UI, Failover |
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Failover | Failover |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Parallelism | Desktop UI, Failover |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Teams & Self-hosting | Failover, Failover |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams & Self-hosting | Desktop UI, Sessions & Memory |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Desktop UI, Security |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Billing | Desktop UI, Parallelism |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Parallelism, Sessions & Memory |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Sessions & Memory | Desktop UI, Failover |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Parallelism | Security, Teams & Self-hosting |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Failover | Failover |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Billing | Accounts, Billing |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Failover | Sessions & Memory |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Sessions & Memory | Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.25x the stars (39,424 vs 155,990) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 62.73x the stars (20,198 vs 322) | 🤖 auto (high) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 23.61x the stars (307,529 vs 13,025) | 🤖 auto (high) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 98.48x the stars (50,028 vs 508) | 🤖 auto (high) |
| **[GizClaw/flowcraft](https://github.com/gizclaw/flowcraft)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 4.21x the stars (1,725 vs 410) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.59x the stars (34,403 vs 384) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 42.35x the stars (39,424 vs 931) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.52x the stars (12,299 vs 2,227) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 151.60x the stars (50,028 vs 330) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 71.50x the stars (307,529 vs 4,301) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.83x the stars (34,403 vs 934) | 🤖 auto (high) |
| **[Xpropel/Pi-Remote](https://github.com/xpropel/pi-remote)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 8.50x the stars (2,838 vs 334) | 🤖 auto (high) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 143.35x the stars (50,028 vs 349) | 🤖 auto (high) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.18x the stars (34,403 vs 354) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 100.65x the stars (30,496 vs 303) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.55x the stars (142,186 vs 4,980) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.24x the stars (50,028 vs 3,778) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 9.56x the stars (12,299 vs 1,286) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.38x the stars (12,299 vs 2,288) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.48x the stars (50,028 vs 372) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.94x the stars (12,299 vs 425) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 49.12x the stars (24,512 vs 499) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 156.34x the stars (50,028 vs 320) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | 15.64x the stars (7,819 vs 500) | 🤖 auto (high) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 22.49x the stars (34,403 vs 1,530) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 49.01x the stars (307,529 vs 6,275) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 159.01x the stars (155,990 vs 981) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 54.71x the stars (24,512 vs 448) | 🤖 auto (high) |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 11.68x the stars (169,449 vs 14,509) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 35.61x the stars (50,028 vs 1,405) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.22x the stars (12,299 vs 2,913) | 🤖 auto (high) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 6.19x the stars (2,966 vs 479) | 🤖 auto (medium) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.94x the stars (20,198 vs 2,545) | 🤖 auto (high) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.20x the stars (30,496 vs 1,882) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.05x the stars (28,155 vs 586) | 🤖 auto (medium) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.72x the stars (1,506 vs 553) | 🤖 auto (high) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.48x the stars (24,512 vs 5,469) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.52x the stars (1,506 vs 428) | 🤖 auto (medium) |
| **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 22.44x the stars (115,360 vs 5,141) | 🤖 auto (medium) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.44x the stars (1,195 vs 489) | 🤖 auto (high) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 73.46x the stars (50,028 vs 681) | 🤖 auto (medium) |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | **[decolua/9router](https://github.com/decolua/9router)** | 4.69x the stars (32,661 vs 6,967) | 🤖 auto (medium) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.74x the stars (1,506 vs 550) | 🤖 auto (medium) |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 2.18x the stars (20,198 vs 9,245) | 🤖 auto (high) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.54x the stars (1,506 vs 594) | 🤖 auto (medium) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.00x the stars (1,506 vs 753) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.73x the stars (1,506 vs 872) | 🤖 auto (high) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 16.93x the stars (5,553 vs 328) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | 1.56x the stars (2,743 vs 1,756) | 🤖 auto (medium) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 2.72x the stars (12,677 vs 4,661) | 🤖 auto (medium) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 1.39x the stars (1,052 vs 759) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,101 vs 519) | 🤖 auto (medium) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.77x the stars (50,028 vs 28,193) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui-2 | 28.2k | 🔻 Superseded | 1.77x the stars (50,028 vs 28,193) |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | sharing | 14.5k | 🔻 Superseded | 11.68x the stars (169,449 vs 14,509) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | teams-self-hosting | 13k | 🔻 Superseded | 23.61x the stars (307,529 vs 13,025) |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | billing | 9.2k | 🔻 Superseded | 2.18x the stars (20,198 vs 9,245) |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | billing | 7k | 🔻 Superseded | 4.69x the stars (32,661 vs 6,967) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | teams-self-hosting | 6.3k | 🔻 Superseded | 49.01x the stars (307,529 vs 6,275) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.5k | 🔻 Superseded | 4.48x the stars (24,512 vs 5,469) |
| **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | mobile | 5.1k | 🔻 Superseded | 22.44x the stars (115,360 vs 5,141) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | parallelism | 5k | 🔻 Superseded | 28.55x the stars (142,186 vs 4,980) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | teams-self-hosting | 4.7k | 🔻 Superseded | 2.72x the stars (12,677 vs 4,661) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | teams-self-hosting | 4.3k | 🔻 Superseded | 71.50x the stars (307,529 vs 4,301) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui-2 | 3.8k | 🔻 Superseded | 13.24x the stars (50,028 vs 3,778) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams-self-hosting | 2.9k | 🔻 Superseded | 4.22x the stars (12,299 vs 2,913) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 Superseded | 7.94x the stars (20,198 vs 2,545) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams-self-hosting | 2.3k | 🔻 Superseded | 5.38x the stars (12,299 vs 2,288) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams-self-hosting | 2.2k | 🔻 Superseded | 5.52x the stars (12,299 vs 2,227) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | teams-self-hosting | 1.9k | 🔻 Superseded | 16.20x the stars (30,496 vs 1,882) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | sessions-memory | 1.8k | 🔻 Superseded | 1.56x the stars (2,743 vs 1,756) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | parallelism | 1.5k | 🔻 Superseded | 22.49x the stars (34,403 vs 1,530) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | desktop-ui-2 | 1.4k | 🔻 Superseded | 35.61x the stars (50,028 vs 1,405) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | teams-self-hosting | 1.3k | 🔻 Superseded | 9.56x the stars (12,299 vs 1,286) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 981 | 🔻 Superseded | 159.01x the stars (155,990 vs 981) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism | 934 | 🔻 Superseded | 36.83x the stars (34,403 vs 934) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 931 | 🔻 Superseded | 42.35x the stars (39,424 vs 931) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | sessions-memory | 872 | 🔻 Superseded | 1.73x the stars (1,506 vs 872) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui-2 | 759 | 🔻 Superseded | 1.39x the stars (1,052 vs 759) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | sessions-memory | 753 | 🔻 Superseded | 2.00x the stars (1,506 vs 753) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui-2 | 681 | 🔻 Superseded | 73.46x the stars (50,028 vs 681) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | sessions-memory | 594 | 🔻 Superseded | 2.54x the stars (1,506 vs 594) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism | 586 | 🔻 Superseded | 48.05x the stars (28,155 vs 586) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | sessions-memory | 553 | 🔻 Superseded | 2.72x the stars (1,506 vs 553) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | sessions-memory | 550 | 🔻 Superseded | 2.74x the stars (1,506 vs 550) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui-2 | 519 | 🔻 Superseded | 2.12x the stars (1,101 vs 519) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | desktop-ui-2 | 508 | 🔻 Superseded | 98.48x the stars (50,028 vs 508) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security | 500 | 🔻 Superseded | 15.64x the stars (7,819 vs 500) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 499 | 🔻 Superseded | 49.12x the stars (24,512 vs 499) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions-memory | 489 | 🔻 Superseded | 2.44x the stars (1,195 vs 489) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | parallelism | 479 | 🔻 Superseded | 6.19x the stars (2,966 vs 479) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 448 | 🔻 Superseded | 54.71x the stars (24,512 vs 448) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | sessions-memory | 428 | 🔻 Superseded | 3.52x the stars (1,506 vs 428) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams-self-hosting | 425 | 🔻 Superseded | 28.94x the stars (12,299 vs 425) |
| **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | parallelism | 410 | 🔻 Superseded | 4.21x the stars (1,725 vs 410) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism | 384 | 🔻 Superseded | 89.59x the stars (34,403 vs 384) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui-2 | 372 | 🔻 Superseded | 134.48x the stars (50,028 vs 372) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | parallelism | 354 | 🔻 Superseded | 97.18x the stars (34,403 vs 354) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | desktop-ui-2 | 349 | 🔻 Superseded | 143.35x the stars (50,028 vs 349) |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | parallelism | 334 | 🔻 Superseded | 8.50x the stars (2,838 vs 334) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | desktop-ui-2 | 330 | 🔻 Superseded | 151.60x the stars (50,028 vs 330) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | billing-2 | 328 | 🔻 Superseded | 16.93x the stars (5,553 vs 328) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 322 | 🔻 Superseded | 62.73x the stars (20,198 vs 322) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui-2 | 320 | 🔻 Superseded | 156.34x the stars (50,028 vs 320) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams-self-hosting | 303 | 🔻 Superseded | 100.65x the stars (30,496 vs 303) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-20 12:56 UTC. 223 live tools · 125 candidates rejected by the quality gates.</sub>
