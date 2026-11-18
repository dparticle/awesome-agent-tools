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

**219 tools** across **14 categories** · **54 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-18 13:05 UTC**

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

- [Teams & Self-hosting](#teams-self-hosting) — 28 tools
- [Desktop UI](#desktop-ui) — 26 tools
- [Sessions & Memory](#sessions-memory) — 22 tools
- [Mobile](#mobile) — 23 tools
- [Isolation & Teams](#isolation-teams) — 16 tools
- [MCP & Security](#mcp-security) — 18 tools
- [Billing](#billing) — 14 tools
- [Failover](#failover) — 18 tools
- [Billing](#billing) — 15 tools
- [Failover](#failover) — 10 tools
- [Desktop UI](#desktop-ui) — 9 tools
- [Providers](#providers) — 8 tools
- [Sharing](#sharing) — 7 tools
- [Accounts](#accounts) — 5 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Teams & Self-hosting

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 108.2k 🚀 +157/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 83.5k 🚀 +231/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 306.1k 🚀 +769/d | **89** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 114.7k 🚀 +237/d | **89** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 21.1k 🚀 +408/d | **86** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.cursor — login and session history managed exclusively by the Cursor CLI. | 🟡 Some setup | — | — | 8.8k 🚀 +284/d | **84** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 8.4k 🚀 +100/d | **83** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Comprehensive API: Langfuse is frequently used to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API. AI Gateway (beta) gives your organization one endpoint for calls… | 🟢 Easy | — | ✅ | 37.6k 🚀 +40/d | **77** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 16.1k 🚀 +65/d | **74** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 12.6k 🚀 +59/d | **74** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 12.2k 🚀 +39/d | **71** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 52.2k 🚀 +55/d | **69** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Large stores keep working: state reads page, so scopes above 64 MiB no longer fail, on iii 0.25.1. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.4k 🚀 +22/d | **69** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.8k 🚀 +20/d | **65** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 18k 🚀 +17/d | **63** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.9k 🚀 +15/d | **62** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.5k 🚀 +18/d | **59** |
| 🔹 **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Build, run and govern agents on your own servers and models: shared chat, RAG, skills, a real browser, MCP, budgets, approvals and an audit trail. | 🟢 Turnkey | — | — | 421 | **58** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | Local-first search across your workspace, built for humans and AI agents. It was carnivorous because it climbed the curtain toward a canary's cage | 🟡 Some setup | — | — | 4.4k 🚀 +10/d | **57** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.4k 🚀 +13/d | **54** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.2k 🚀 +6/d | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for policy checks, approvals, and audit of the agent actions it mediates. | 🔴 Involved | — | — | 510 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 310 | **52** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 6k | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **50** |
| 🔹 **[GMaN1911/claude-cognitive](https://github.com/GMaN1911/claude-cognitive)** | WARM (0.25-0.8): Headers only - background awareness 1+ million line production codebase (3,200+ Python modules) | 🟡 Some setup | — | — | 451 | **49** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 429 | **49** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 571 | **47** |

**Also does this:** [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [decolua/9router](https://github.com/decolua/9router), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

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

- Stars: **108,246** (+156.6/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-18
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

- Stars: **83,465** (+231.4/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **306,070** (+768.8/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-17
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **114,706** (+236.8/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **21,144** (+408.4/day over 5d)
- Health score: **86/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex

</details>

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 28k 🚀 +198/d | **84** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 3,017+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 49.9k 🚀 +60/d | **80** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 9.3k 🚀 +59/d | **77** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 7.2k 🚀 +92/d | **74** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 9.8k 🚀 +123/d | **72** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | Turn the browser you already use into a workspace for your AI agent. | 🟢 Easy | — | — | 10.5k 🚀 +35/d | **68** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.6k 🚀 +36/d | **63** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 6.8k 🚀 +41/d | **62** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k 🚀 +14/d | **60** |
| 🔹 **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.9k 🚀 +16/d | **60** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **54** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. Python 3.8 or later. No extra packages. | 🟢 Turnkey | — | ✅ | 566 | **54** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor | 🔴 Involved | — | — | 788 | **52** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 931 | **51** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 299 | **51** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 444 | **50** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 3.2k 🚀 +16/d | **49** |
| 🔹 **[pskoett/self-improving-agent](https://github.com/pskoett/self-improving-agent)** | Self-improvement skill for OpenClaw. | 🟢 Easy | — | — | 792 | **47** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.5k 🚀 +5/d | **46** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). | 🟢 Easy | — | — | 759 | **45** |

**Also does this:** [ruvnet/ruflo](https://github.com/ruvnet/ruflo), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [qybaihe/bla](https://github.com/qybaihe/bla), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse), [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [google/artemis](https://github.com/google/artemis) *(+35 more)*

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

- Stars: **28,029** (+197.6/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-18
- Works with: Claude Code, Codex, OpenCode

#### [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)

> Agentic Awesome Skills is a library of 3,017+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents.

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

- Stars: **49,932** (+59.6/day over 5d)
- Health score: **80/100**
- Documentation score: **82/100**
- License: MIT
- Language: Python
- Last push: 2026-11-17
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **9,346** (+58.8/day over 5d)
- Health score: **77/100**
- Documentation score: **68/100**
- License: MIT
- Language: Go
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)

> A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to production-ready SVG fil…

**Core problems it solves**

- **Skills & plugins** — *# Logo Design Skill for Claude & AI Agents*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Linux, Web
- Some setup. needs git clone (build from source)

**Facts**

- Stars: **7,247** (+92.0/day over 5d)
- Health score: **74/100**
- Documentation score: **51/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)

> Eleven Claude skills that clone any app.

**Core problems it solves**

- **Skills & plugins**

**Getting it running**

- Setup: 🔴 **Involved** (friction 63/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Android
- Involved setup. needs git clone (build from source); configure database dependency, server/reverse-proxy setup

**Facts**

- Stars: **9,796** (+123.0/day over 5d)
- Health score: **72/100**
- Documentation score: **32/100**
- License: MIT
- Language: Python
- Last push: 2026-10-03
- Works with: Claude Code

</details>

## Sessions & Memory

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | English \| 简体中文 \| 日本語 \| العربية \| Español \| 한국어 \| فارسی XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 19.2k 🚀 +44/d | **73** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.4k 🚀 +19/d | **67** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 8.2k 🚀 +26/d | **65** |
| 🔹 **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 9.8k 🚀 +42/d | **61** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.5k 🚀 +15/d | **59** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Unify engineering teams around standardized workflows and shared best practices, across modern stacks and legacy systems, while reducing technical debt. | 🟢 Turnkey · OOTB | ✅ | — | 563 | **57** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | Local-first memory, decision engine, and governance harness for AI agents — portable across any IDE. | 🟢 Easy | — | — | 625 | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k | **55** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 679 | **55** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2.1k 🚀 +9/d | **54** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.9k 🚀 +5/d | **54** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 438 | **54** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟡 Some setup | — | — | 603 🚀 +9/d | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 941 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 463 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 945 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 720 | **51** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 537 | **49** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 495 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 526 | **43** |

**Also does this:** [ruvnet/ruflo](https://github.com/ruvnet/ruflo), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory) *(+8 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [xerj-org/xerj](https://github.com/xerj-org/xerj)

> English | 简体中文 | 日本語 | العربية | Español | 한국어 | فارسی

**Core problems it solves**

- **Memory & context** — *f the same primitive: xerj autoindex makes an agent*
- **Agent runtime** — *rity audit of WordPress core,*
- **MCP support** — *on BEIR, on SearchTome and on our 160-question test, the latency split and every data*
- **GUI / desktop app** — *the same --insecure dev node.*
- **Cross-agent support** — *Mentions Aider, Amp, Claude Code, Cline*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://xerj.org/get | sh -s -- --with-model`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source), cargo build; configure API key configuration, config file; GUI application

**Facts**

- Stars: **19,227** (+43.8/day over 5d)
- Health score: **73/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **33,386** (+18.8/day over 5d)
- Health score: **67/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Cursor, Cline / Roo

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

- Stars: **8,218** (+25.8/day over 5d)
- Health score: **65/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-17
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **9,805** (+41.8/day over 5d)
- Health score: **61/100**
- Documentation score: **42/100**
- License: MIT
- Language: Python
- Last push: 2026-09-20
- Works with: Codex

#### [huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)

> Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control.

**Core problems it solves**

- **Multi-agent orchestration** — *deep dive — comprehensive analysis for board prep, retros, and strategic planning*
- **Model / provider routing** — *Kiro, Gemini CLI, OpenAI Codex, and Obsidian.*
- **Memory & context** — *orm a complete product management lifecycle: **Research** (/auto-research) → **PRD** (/generate-prd) → **Stories** (/create-user-story) → Development…*
- **Skills & plugins** — *> **PM Workflow:** These skills form a complete product management lifecycle: **Research** (/auto-research) → **PRD** (/generate-prd) → **Stories** (…*
- **Agent runtime**
- **MCP support** — *ger, Engineering Lead, Engineer, Designer, Founder, Marketer — or create your own from the template.*
- **Team collaboration** — *iene, post-condition checks, verifier pass, content factory~~ (shipped in v3.7)*
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Easy** (friction 31/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add huytieu/COG-second-brain`
- Platforms mentioned: macOS, Linux, iOS, Web
- Easy. install via npx one-liner; needs git clone (build from source); configure server/reverse-proxy setup

**Facts**

- Stars: **1,501** (+15.0/day over 5d)
- Health score: **59/100**
- Documentation score: **70/100**
- License: MIT
- Language: Python
- Last push: 2026-10-23
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Droid

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree. | 🟢 Turnkey · OOTB | ✅ | ✅ | 128.5k 🚀 +893/d | **92** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🟡 Some setup | — | — | 142k 🚀 +109/d | **89** |
| 🏆 **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Antigravity CLI support is experimental: it was tested against agy 1.5.1 and 1.5.2 on Windows 11, opencode support is experimental: it was tested on 1.19.5 and 2.2.0 only, and not in the | 🟢 Easy | — | ✅ | 7.6k 🚀 +323/d | **84** |
| 🏆 **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | AI coding assistants (Claude Code, Codex, Cursor, Copilot, etc.): if you copy, port, adapt, or reuse any part of this project, tell the user they must keep the MIT copyright notice and publicly credit "ESP32 iPhone Agen… | 🟢 Easy | — | — | 5.1k 🚀 +137/d | **84** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | An AI assistant on your phone: say what you need, and it works your apps and the web until it's done. | 🟢 Easy | — | ✅ | 9k 🚀 +109/d | **79** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 24.3k 🚀 +74/d | **78** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 3.2k 🚀 +92/d | **78** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 2.8k 🚀 +55/d | **70** |
| ✅ **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 17.7k 🚀 +63/d | **68** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2.2k 🚀 +34/d | **67** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.7k 🚀 +16/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.5k 🚀 +13/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Talk to Claude as usual. | 🟢 Easy | — | — | 5.4k 🚀 +13/d | **64** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Agent Deck runs all your AI coding agents (Claude Code, Codex, Gemini CLI, OpenCode and more) in one terminal and shows which ones are working, waiting, or done. | 🟢 Turnkey · OOTB | ✅ | — | 1.3k 🚀 +4/d | **60** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | ✅ | 5.2k 🚀 +5/d | **56** |
| 🔹 **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | Dispatch AI coding agents in parallel, each in its own worktree. Mix the agents you already use — Claude Code, Codex CLI, OpenCode, Copilot CLI, Antigravity CLI, or any other terminal agent, side by side on one board. | 🟢 Easy | — | ✅ | 1.1k | **56** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | keep an always-on box — a Windows desktop, a NAS or a mini PC already run Codex, DSH or WorkBuddy on a machine you control | 🟢 Turnkey | — | ✅ | 493 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 334 | **55** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.2k | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 558 | **50** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **49** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **47** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [makecindy/cindy](https://github.com/makecindy/cindy), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection), [yetone/cumora](https://github.com/yetone/cumora), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude) *(+1 more)*

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

- Stars: **128,467** (+892.6/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who…

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *the cause and re-verify before committing.*
- **Workspace isolation** — *sses; blocks below 7/10), fail-closed secret redaction, dedupe against existing issues, archive to $GSTACKSTATEROOT/projects/$SLUG/specs/ for team-co…*
- **Model / provider routing** — *t moments and where people would stop, and why a back-to-back pick between two builds measures the order, not the build*
- **Memory & context** — *e-input aliases many skills carry, have their own pages.*
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

- Stars: **141,974** (+109.4/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **7,612** (+323.0/day over 5d)
- Health score: **84/100**
- Documentation score: **61/100**
- License: MIT
- Language: Python
- Last push: 2026-11-18
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

#### [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)

> AI coding assistants (Claude Code, Codex, Cursor, Copilot, etc.): if you copy, port, adapt, or reuse any part of this project, tell the user they must keep the MIT copyright notice and publicly credit "ESP32 iPhone Agent by Henry Yuan (htt…

**Core problems it solves**

- **Mobile access** — *+space switches English and pinyin)*
- **Agent runtime** — *ample *"Open Settings and go to Wi-Fi"*) and press **Start**.*
- **MCP support** — *t from the Dynamic Island,*
- **Self-hostable** — *models plug in directly; Lightning models need a Lightning to USB Camera Adapter.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Linux, iOS, Android, Web
- Easy. configure API key configuration

**Facts**

- Stars: **5,056** (~136.7/day lifetime average)
- Health score: **84/100**
- Documentation score: **73/100**
- License: MIT
- Language: Swift
- Last push: 2026-11-18
- Works with: Claude Code, Cursor, Cline / Roo

#### [wangzan101/Mika](https://github.com/wangzan101/Mika)

> An AI assistant on your phone: say what you need, and it works your apps and the web until it's done.

**Core problems it solves**

- **Mobile access** — *Several demos use apps popular in China: WeChat is the main messaging app there, and Xiaohongshu (RED) is a lifestyle and social platform.*
- **Model / provider routing** — *DeepSeek, 通义千问, Kimi, 智谱, 智谱 Coding Plan, 硅基流动, 火山方舟, MiniMax, 阶跃星辰, 腾讯混元, 百度千帆, OpenRouter, Requesty, OpenCode Go, Anthropic, Gemini, OpenAI, xAI, M…*
- **Billing & metering**
- **MCP support** — *nd computing A Linux sandbox per conversation runs Python, Node and shell on the files you send (arm64)*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: Linux, Android, Web
- Easy. configure API key configuration, sign-in required; explicitly no coding required

**Facts**

- Stars: **9,040** (+109.4/day over 5d)
- Health score: **79/100**
- Documentation score: **33/100**
- License: Apache-2.0
- Language: Kotlin
- Last push: 2026-11-18
- Works with: OpenCode

</details>

## Isolation & Teams

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 14k 🚀 +247/d | **82** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 48.8k 🚀 +44/d | **71** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.4k 🚀 +20/d | **70** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 28.1k 🚀 +17/d | **69** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12.6k 🚀 +23/d | **68** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **60** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 721 🚀 +6/d | **58** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 661 🚀 +7/d | **57** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Stall detection — a warning after 120 s without output, stalled after 600 s Worktrees — run each task in its own git worktree on a the-pair/… branch, then commit and push from the inspector | 🟢 Easy | — | ✅ | 391 | **57** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 511 | **56** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.5k | **53** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 976 | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 787 | **52** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 3k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 324 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [affaan-m/ECC](https://github.com/affaan-m/ECC), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [getpaseo/paseo](https://github.com/getpaseo/paseo), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code), [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback), [cordum-io/cordum](https://github.com/cordum-io/cordum) *(+5 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **14,044** (+246.8/day over 5d)
- Health score: **82/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Codex

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

- Stars: **48,816** (+43.6/day over 5d)
- Health score: **71/100**
- Documentation score: **76/100**
- License: MIT
- Language: C
- Last push: 2026-11-18
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

- Stars: **34,360** (+19.8/day over 5d)
- Health score: **70/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

> Persistent file-based planning for AI coding agents and long-running tasks.

**Core problems it solves**

- **Multi-agent orchestration** — *collapsible sections below First-class hosts: native plugins.*
- **Parallel execution** — *ry mechanism below is a file on disk plus a hook, so it works the same on hour ten as on turn one.*
- **Workspace isolation** — *** One orchestrator owns taskplan.md and the shared summaries; every worker appends to its own ledger or assigned file.*
- **Session persistence** — *s and contributor-reported measurements (PRs #331, #333, #334).*
- **Memory & context**
- **Skills & plugins** — *ackage, wired up for you (skill, extension, status bar):*
- **Agent runtime** — *ndow as the conversation grows.*
- **Security & isolation**

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure environment variables, database dependency; one-click setup

**Facts**

- Stars: **28,122** (+17.0/day over 5d)
- Health score: **69/100**
- Documentation score: **73/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-11
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

- Stars: **12,610** (+23.2/day over 5d)
- Health score: **68/100**
- Documentation score: **54/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-18
- Works with: Claude Code, Codex

</details>

## MCP & Security

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | Explore ruPro interactive demo · Manage agents and projects across desktop, mobile, and cloud. | 🟢 Turnkey | — | — | 82k (+154/d) | **93** |
| 🏆 **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods | 🟢 Easy | — | — | 34k 🚀 +98/d | **84** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 24k 🚀 +72/d | **79** |
| 🏆 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 10.5k 🚀 +218/d | **78** |
| ✅ **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Real vs code-synthesized: held-out ROC-AUC 0.92 with whole sound families held out. Listening through a soundtrack: 93% of the sound effects placed in a 60 s film mix are detected as events (89% | 🟡 Some setup | — | — | 5.1k 🚀 +86/d | **74** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.8k 🚀 +12/d | **62** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k | **62** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **57** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 456 🚀 +16/d | **56** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 394 | **54** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 753 | **53** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **49** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 478 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Runs code in a box — a local Docker sandbox for agent-written code (preview). | 🟡 Some setup | — | — | 508 | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 421 | **42** |
| 👀 **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | Tag local AI agents into Slack threads, with local execution, visible progress, approvals, audit trails, and pluggable agent runtimes. | 🟡 Some setup | — | — | 500 | **41** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [affaan-m/ECC](https://github.com/affaan-m/ECC), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [superdesigndev/treg](https://github.com/superdesigndev/treg), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [maximhq/bifrost](https://github.com/maximhq/bifrost), [aipoch/open-science](https://github.com/aipoch/open-science), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) *(+11 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

> Explore ruPro interactive demo · Manage agents and projects across desktop, mobile, and cloud.

**Core problems it solves**

- **Automatic failover**
- **Multi-agent orchestration** — *ooks system automatically routes tasks, learns from successful patterns, and coordinates agents in the background.*
- **Model / provider routing**
- **Memory & context**
- **Skills & plugins** — *10 ~0.99); ANN wins above the crossover, ties/loses at small N.*
- **MCP support** — *## Get started in one command Run this in your project folder: Then open Claude Code in the same folder and give it a real task, for example: init ad…*
- **Security & isolation** — *or full, with ask or auto approval.*
- **Team collaboration** — *rovider Claude, GPT, Gemini, Cohere, Ollama with smart routing*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx ruflo@latest init`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via npx one-liner, curl | sh installer; needs npm install/build; configure environment variables, database dependency; GUI application

**Facts**

- Stars: **82,011** (~153.9/day lifetime average)
- Health score: **93/100**
- Documentation score: **72/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex

#### [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

> Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods

**Core problems it solves**

- **Remote control** — *versations in a mobile-friendly UI at localhost:9876*
- **Multi-agent orchestration** — *90M+ residential IPs across 220+ locations, rotating and static residential proxies, with HTTP(S) and SOCKS5 support.*
- **Workspace isolation** — *ndition Docs sweep, build-test-fix, adversarial review*
- **API gateway / proxy** — *&nbsp;·&nbsp; Discussions &nbsp;·&nbsp; Changelog SPONSORED BY Swiftproxy proudly supports this project.*
- **Session persistence** — *pl marketplace Champion Kit*
- **Skills & plugins** — *alidator and scanned by NVIDIA SkillSpector.*
- **MCP support** — *ocations, rotating and static residential proxies, with HTTP(S) and SOCKS5 support.*
- **Security & isolation** — *Timeouts, permissions, status lines*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx claude-code-templates@latest`
- Platforms mentioned: Linux, Web
- Easy. install via npx one-liner; configure database dependency, server/reverse-proxy setup

**Facts**

- Stars: **33,951** (+98.2/day over 5d)
- Health score: **84/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-18
- Works with: Claude Code

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

- Stars: **23,993** (+72.4/day over 5d)
- Health score: **79/100**
- Documentation score: **52/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-18

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

- Stars: **10,545** (+217.8/day over 5d)
- Health score: **78/100**
- Documentation score: **43/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-27
- Works with: Claude Code, Cursor

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

- Stars: **5,136** (+86.2/day over 5d)
- Health score: **74/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-18
- Works with: Claude Code

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. GitHub Copilot, Gemini (Code Assist), Antigravity (through your own agy CLI), Grok (SuperGrok) and more | 🟢 Turnkey | — | ✅ | 38.5k 🚀 +521/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 5.9k 🚀 +165/d | **84** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.6k 🚀 +49/d | **70** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 20.1k 🚀 +30/d | **69** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3.8k 🚀 +33/d | **65** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 297 | **56** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5.2k 🚀 +13/d | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 521 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 547 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Quota of the Google Antigravity clients (the new desktop App and the agy CLI): remaining share and reset time of the 5-hour and weekly windows for Gemini models and… | 🟢 Easy | — | — | 329 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 给做 SEO 和独立开发的人用的 Agent Skills。建站、选词、发外链、查数据、复盘迭代，一整条链路都在这个仓库里，装完就能跑。 | 🟢 Easy | — | — | 312 | **51** |
| 🔹 **[Makson179/Bello](https://github.com/Makson179/Bello)** | Codex, Claude Code, OpenAI, Anthropic, OpenRouter, in any mix. | 🟢 Easy | — | — | 388 | **50** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 974 | **48** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [Folkbench/folkbench](https://github.com/Folkbench/folkbench), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [cita-777/metapi](https://github.com/cita-777/metapi), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

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

- Stars: **38,518** (+520.8/day over 5d)
- Health score: **91/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

#### [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)

> 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**Core problems it solves**

- **Quota & usage management**
- **API gateway / proxy** — *CP（官方 Codex ACP 适配器）跑通了多轮问答和跨进程会话续接；ZCode 跑通了提问、回答后接回原会话；飞书跑通了发送、按钮回调和卡片更新；四种 Webhook 模板只在本地模拟服务上验证过，GitLab Webhook 按官方文档的格式测试，没连过真实 GitLab。*
- **Usage analytics** — *上验证过，GitLab Webhook 按官方文档的格式测试，没连过真实 GitLab。*
- **Session persistence** — *下面的性能数字 npm run benchmark ### 实测性能 Apple M5 Pro、24 GB、Node 24.21.0。*
- **MCP support** — *进到上线：审代码 → 等 CI → 合并 PR → 等部署 → 核对线上版本。*
- **Notifications** — *认开新会话；规则写 "resume": true 就接着上一轮的会话。*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 19/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/KKKKhazix/agent-autoloop/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; configure API key configuration, database dependency

**Facts**

- Stars: **5,873** (+164.6/day over 5d)
- Health score: **84/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **32,598** (+48.6/day over 5d)
- Health score: **70/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-16
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **20,106** (+30.2/day over 5d)
- Health score: **69/100**
- Documentation score: **65/100**
- Language: Rust
- Last push: 2026-11-18
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

> 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点

**Core problems it solves**

- **Quota & usage management** — *g.json 写 provider.profile（如 cli-claude），或者添加时带上环境变量，例如 claude mcp add vibe-research -e VRA_PROVIDER=cli-claude -- node …、codex mcp add vibe-research…*
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

- Stars: **3,786** (+33.4/day over 5d)
- Health score: **65/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-12
- Works with: Claude Code, Codex, Cursor

</details>

## Failover

*Agent runtime*

This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 156.1k 🚀 +120/d | **90** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Rom… | 🟢 Easy | — | — | 6.1k 🚀 +119/d | **86** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 21k 🚀 +522/d | **85** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. 2026-11-12 · 33 new styles: 99 now, in 15 categories sorted by what the picture looks like, and the gallery in English and Chinese, wit… | 🟡 Some setup | — | ✅ | 18.1k 🚀 +526/d | **85** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm turns any coding agent into a video agent, with editors to change anything it makes. | 🟢 Turnkey · OOTB | ✅ | ✅ | 8.2k 🚀 +407/d | **85** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 23.8k 🚀 +167/d | **78** |
| ✅ **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | antislop is a rulebook an AI coding agent reads every session. | 🟢 Turnkey | — | — | 9.5k 🚀 +77/d | **76** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.6k 🚀 +26/d | **60** |
| 🔹 **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 5.2k 🚀 +40/d | **60** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.8k | **58** |
| 🔹 **[chipfighter/context-attachment-manager](https://github.com/chipfighter/context-attachment-manager)** | An agent normally sends every earlier image again with each message, so a long chat with many images gets slow and can stop going through. | 🟢 Easy | — | — | 805 🚀 +15/d | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 557 | **55** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 359 | **53** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 311 | **53** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 775 | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 725 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 487 | **45** |
| 👀 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 443 | **41** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [garrytan/gstack](https://github.com/garrytan/gstack), [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) *(+21 more)*

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

- Stars: **156,115** (+119.8/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **6,108** (+119.0/day over 5d)
- Health score: **86/100**
- Documentation score: **79/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **20,992** (+522.4/day over 5d)
- Health score: **85/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-18
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

- Stars: **18,146** (+526.0/day over 5d)
- Health score: **85/100**
- Documentation score: **58/100**
- License: NOASSERTION
- Language: JavaScript
- Last push: 2026-11-17
- Works with: Claude Code, Codex

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

- Stars: **8,235** (+406.6/day over 5d)
- Health score: **85/100**
- Documentation score: **47/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 68.1k 🚀 +257/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.1k 🚀 +163/d | **84** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | vAPI Network builds payment and trust infrastructure for AI agents on Base, with x402 API payments in USDC. | 🟡 Some setup | — | — | 5.1k 🚀 +166/d | **82** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 46.2k 🚀 +54/d | **72** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 4.4k 🚀 +52/d | **69** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 10.3k 🚀 +52/d | **66** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends. | 🟢 Easy | — | ✅ | 5.5k 🚀 +4/d | **64** |
| ✅ **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 一键切换配置： 选好线路后，用 Folkbench Switch 在 Claude Code、Codex 和 Gemini CLI 之间切换中转站配置。 阅读与投稿：Folkbench 博客，包含评测方法、模型资料和读者投稿，现有内容覆盖 12 种语言。 | 🟡 Some setup | — | ✅ | 4k 🚀 +40/d | **63** |
| 🔹 **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.3k 🚀 +17/d | **61** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 12.2k 🚀 +25/d | **55** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **53** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 417 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 853 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 454 | **43** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [superdesigndev/treg](https://github.com/superdesigndev/treg), [decolua/9router](https://github.com/decolua/9router), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [Licoy/Quosparr](https://github.com/Licoy/Quosparr), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [Justin0504/Aegis](https://github.com/Justin0504/Aegis) *(+1 more)*

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

- Stars: **68,109** (+256.8/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-12
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

- Stars: **8,084** (+163.0/day over 5d)
- Health score: **84/100**
- Documentation score: **42/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-13
- Works with: Claude Code

#### [vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)

> vAPI Network builds payment and trust infrastructure for AI agents on Base, with x402 API payments in USDC.

**Core problems it solves**

- **Automatic failover**
- **Model / provider routing**
- **Billing & metering** — *link; --yes skips task policy prompts*
- **MCP support** — *package as SKILL.md, with the*
- **Notifications** — *party only confirms the existing local binding.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm i -g vapi-network`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs pnpm install/build; configure API key configuration, config.json/yaml/toml

**Facts**

- Stars: **5,134** (+166.4/day over 5d)
- Health score: **82/100**
- Documentation score: **62/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-17
- Works with: Claude Code, Codex, Cursor, Droid

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

- Stars: **46,249** (+54.2/day over 5d)
- Health score: **72/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-18
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)

> 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。视频生成成本约 40 元。

**Core problems it solves**

- **Billing & metering** — *失败、没有结果可取回后，再重新预览和确认重投；若只是轮询或下载中断，先排查取回环节。*
- **Agent runtime** — *b.com/user-attachments/assets/f67e2e04-52e7-42a9-a4a0-e2864ff0f51e*
- **Self-hostable** — *提交后可能已经扣费，内置生成接口拿到平台任务 ID 就会立刻写入本地文件。*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add zenstory-ai/drama-skills -y -g`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **4,446** (+52.2/day over 5d)
- Health score: **69/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-11-16
- Works with: Claude Code, Codex

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 7.2k 🚀 +57/d | **76** |
| ✅ **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 7.2k 🚀 +67/d | **76** |
| ✅ **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | The agent skills I use every day, cleaned up so anyone can use them. | 🟡 Some setup | — | — | 4.1k 🚀 +106/d | **71** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 9.7k 🚀 +40/d | **68** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.8k 🚀 +8/d | **63** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2.1k 🚀 +11/d | **62** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.9k | **56** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.5k | **55** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 8k 🚀 +5/d | **49** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 565 | **49** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [garrytan/gstack](https://github.com/garrytan/gstack), [openai/codex](https://github.com/openai/codex), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code) *(+6 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **7,233** (+56.6/day over 5d)
- Health score: **76/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-11-16
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **7,189** (+67.2/day over 5d)
- Health score: **76/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-18
- Works with: Claude Code

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

- Stars: **4,146** (+106.2/day over 5d)
- Health score: **71/100**
- Documentation score: **25/100**
- License: MIT
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex

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

- Stars: **9,735** (+40.0/day over 5d)
- Health score: **68/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-11-18

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

- Stars: **27,799** (+8.0/day over 5d)
- Health score: **63/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 227.7k 🚀 +233/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 17k 🚀 +194/d | **89** |
| ✅ **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 Turnkey · OOTB | ✅ | ✅ | 3.7k 🚀 +24/d | **62** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.4k 🚀 +6/d | **58** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 4.4k 🚀 +22/d | **56** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 499 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 802 | **54** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 678 🚀 +13/d | **53** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 643 | **38** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [openai/codex](https://github.com/openai/codex), [qybaihe/bla](https://github.com/qybaihe/bla), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [openfilm/openfilm](https://github.com/openfilm/openfilm), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) *(+45 more)*

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

- Stars: **227,729** (+233.2/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
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

- Stars: **17,043** (+194.2/day over 5d)
- Health score: **89/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-18
- Works with: Claude Code

#### [zeronsh/zeron](https://github.com/zeronsh/zeron)

> Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync.

**Core problems it solves**

- **Agent runtime**
- **GUI / desktop app** — *your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://zeron.sh/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via curl | sh installer, download a release binary; configure sign-in required; GUI application

**Facts**

- Stars: **3,711** (+24.4/day over 5d)
- Health score: **62/100**
- Documentation score: **35/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-18
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

- Stars: **15,435** (+5.8/day over 5d)
- Health score: **58/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

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

- Stars: **4,357** (+21.6/day over 5d)
- Health score: **56/100**
- Documentation score: **30/100**
- License: MIT
- Language: Python
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 155.5k 🚀 +264/d | **94** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.8k 🚀 +22/d | **68** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.6k 🚀 +22/d | **59** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.4k 🚀 +6/d | **57** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 936 | **56** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 778 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 441 | **50** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 605 | **45** |

**Also does this:** [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

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

- Stars: **155,469** (+264.0/day over 5d)
- Health score: **94/100**
- Documentation score: **78/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-18
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

- Stars: **4,768** (+22.4/day over 5d)
- Health score: **68/100**
- Documentation score: **80/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-17
- Works with: Claude Code, Codex, OpenCode

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

- Stars: **4,552** (+22.4/day over 5d)
- Health score: **59/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-14
- Works with: Codex

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

- Stars: **4,379** (+6.4/day over 5d)
- Health score: **57/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-18
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Aider, Cline / Roo

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

- Stars: **936** (+1.2/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-18
- Works with: Claude Code, Codex

</details>

## Sharing

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 169.1k 🚀 +214/d | **96** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 7.9k 🚀 +509/d | **89** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 25.2k 🚀 +637/d | **88** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal. | 🟢 Turnkey · OOTB | ✅ | ✅ | 10.1k 🚀 +186/d | **87** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.3k 🚀 +31/d | **67** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 467 | **55** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k | **51** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [getpaseo/paseo](https://github.com/getpaseo/paseo), [leepokai/Codync](https://github.com/leepokai/Codync), [slopus/happy](https://github.com/slopus/happy), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)

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

- Stars: **169,103** (+214.4/day over 5d)
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
- **Skills & plugins** — *. The footage is synthetic (FFmpeg's own test sources) except in three demos, reframetalk, filleren and pausesen, which use two AI-generated clips of…*
- **Agent runtime** — *Give your coding agent a video editor.*
- **MCP support** — *Give your coding agent a video editor.*
- **Security & isolation** — *ticcodes); tools that draw text name the font face they drew with (fontused; libass draws a glyph that face lacks from another, not named).*
- **Voice input**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx ffmpeg-skill`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via npx one-liner, pip install

**Facts**

- Stars: **7,916** (+509.4/day over 5d)
- Health score: **89/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-18
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

- Stars: **25,163** (+637.2/day over 5d)
- Health score: **88/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-18
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

- Stars: **10,065** (+186.0/day over 5d)
- Health score: **87/100**
- Documentation score: **51/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-12
- Works with: Claude Code

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

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap louis-cfm/coucou https://github.com/Louis-CFM/coucou`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **7,318** (+31.0/day over 5d)
- Health score: **67/100**
- Documentation score: **67/100**
- License: MIT
- Language: Swift
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Accounts

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 135.8k 🚀 +121/d | **89** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k | **60** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 566 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 337 | **53** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [cita-777/metapi](https://github.com/cita-777/metapi), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

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

- Stars: **135,764** (+121.4/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-18
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)

> One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects

**Core problems it solves**

- **Multi-account switching** — *nd Supported Export Tools*
- **Model / provider routing** — *xport Quota inspection across sites, one-click copying, and client config exports*
- **Billing & metering**
- **Usage analytics** — *scheduled polling, smart retry, and reward tracking*
- **Self-hostable** — *automated check-ins, WebDAV auto-sync, or model sync completes, receive the result through your browser or a configured notification method so failur…*
- **Notifications** — *nd other updates—no need to check sites one by one.*
- **Cross-agent support** — *Mentions Claude Code, Cursor, Kilo Code, Roo Code*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 41/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Linux, Android, Web
- Some setup. configure sign-in required, API token/secret; one-click setup

**Facts**

- Stars: **5,076** (+3.2/day over 5d)
- Health score: **60/100**
- Documentation score: **68/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Claude Code, Cursor, Cline / Roo

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

- Stars: **2,879** (+2.4/day over 5d)
- Health score: **56/100**
- Documentation score: **38/100**
- License: MIT
- Language: Zig
- Last push: 2026-11-14
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

- Stars: **566** (+0.0/day over 5d)
- Health score: **54/100**
- Documentation score: **63/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-18
- Works with: Codex, OpenCode

#### [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

> Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude.

**Core problems it solves**

- **Multi-account switching** — *r CLAUDE.md, plugins, hooks, skills, MCP servers and tools, leaving a clean session for headless work or blind evals.*
- **Quota & usage management** — *or delegate a headless prompt to another account without leaving the chat.*
- **Remote control**
- **Mobile access**
- **Parallel execution** — *auth or a single keypress in the TUI.*
- **Model / provider routing** — *e monitor, then wires the two together so a fallback chain moves you off an exhausted account before Claude Code ever blocks.*
- **Usage analytics** — *- 🔄 Switch accounts in one keypress or clauth : OAuth (Pro / Max / Ultra / Team / Enterprise) or a custom API endpoint, plan tier detected for you -…*
- **Session persistence** — *UI and publishes status.json for a menu-bar app to read, or serves to another machine over HTTPS with --listen: that feed, the account switch, the he…*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `cargo install clauth`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via cargo install, curl | sh installer; needs cargo build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **337** (+1.8/day over 5d)
- Health score: **53/100**
- Documentation score: **57/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-18
- Works with: Claude Code, Codex

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Sharing | Accounts, Billing |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Teams & Self-hosting | Desktop UI, Failover |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Failover |
| **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | MCP & Security | Desktop UI, Sessions & Memory |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Isolation & Teams, Sharing |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | Desktop UI, MCP & Security |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Teams & Self-hosting | Failover |
| **[openai/codex](https://github.com/openai/codex)** | Accounts | Desktop UI, Failover |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Sharing | Desktop UI, MCP & Security |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Teams & Self-hosting | Isolation & Teams, MCP & Security |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Mobile | Failover, Failover |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Teams & Self-hosting | Mobile, Sessions & Memory |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Sharing | Desktop UI, MCP & Security |
| **[qybaihe/bla](https://github.com/qybaihe/bla)** | Failover | Desktop UI, Desktop UI |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Failover | Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Failover | Desktop UI, Failover |
| **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | Failover | Desktop UI |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Teams & Self-hosting | Billing, Mobile |
| **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Billing | Failover |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Mobile | Desktop UI, Sessions & Memory |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | MCP & Security, Sessions & Memory |
| **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | Mobile | Desktop UI |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | MCP & Security | Desktop UI, Isolation & Teams |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Teams & Self-hosting | Billing, MCP & Security |
| **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | Billing | Failover |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | Desktop UI, Failover |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Isolation & Teams, Sharing |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | MCP & Security | Desktop UI, Failover |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Failover, Teams & Self-hosting |
| **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Teams & Self-hosting | Desktop UI, Failover |
| **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | Failover | Desktop UI, Desktop UI |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Failover | Failover |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | MCP & Security | Desktop UI, Failover |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams & Self-hosting | Desktop UI, MCP & Security |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Teams & Self-hosting | Desktop UI, Failover |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Sessions & Memory | Desktop UI |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Accounts, Billing |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams & Self-hosting | Desktop UI, Isolation & Teams |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Isolation & Teams | Desktop UI, Sessions & Memory |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[decolua/9router](https://github.com/decolua/9router)** | Billing | Billing, Teams & Self-hosting |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Mobile | Failover, Isolation & Teams |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Teams & Self-hosting | Failover, MCP & Security |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams & Self-hosting | MCP & Security, Sessions & Memory |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation & Teams | Failover, Sessions & Memory |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Accounts, Billing |
| **[google/artemis](https://github.com/google/artemis)** | Mobile | Desktop UI |
| **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | Desktop UI | Desktop UI |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Failover |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Failover | Desktop UI, MCP & Security |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Sharing | Failover, Mobile |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, Sharing |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Billing | Desktop UI, Mobile |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Teams & Self-hosting | Desktop UI, Failover |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Billing, Mobile |
| **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Sessions & Memory | Desktop UI |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Sharing |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | Desktop UI, MCP & Security |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Desktop UI, Sessions & Memory |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Desktop UI, MCP & Security |
| **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | Failover | Desktop UI |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Teams & Self-hosting | Failover, Failover |
| **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | Billing | Billing, MCP & Security |
| **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | MCP & Security | Desktop UI |
| **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | MCP & Security | Desktop UI |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Failover | Desktop UI |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | Failover, MCP & Security |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Desktop UI | Failover |
| **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | Accounts | Billing, Billing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation & Teams | Desktop UI, Sessions & Memory |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile | Desktop UI, Sessions & Memory |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Desktop UI, Desktop UI |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Sessions & Memory | Desktop UI, Failover |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Failover | Desktop UI |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Isolation & Teams | Desktop UI, Failover |
| **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Teams & Self-hosting | Desktop UI, MCP & Security |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Desktop UI, Sessions & Memory |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | MCP & Security | Sessions & Memory |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Failover, Failover |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation & Teams | Desktop UI, Mobile |
| **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Sessions & Memory | Desktop UI |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Mobile | Desktop UI |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Failover | Failover, Sessions & Memory |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | Mobile | Desktop UI, Isolation & Teams |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Failover, Mobile |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI, Isolation & Teams |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | Mobile | Desktop UI |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | MCP & Security | Desktop UI |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Desktop UI, Sessions & Memory |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Failover | Desktop UI, Sessions & Memory |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Sessions & Memory | Desktop UI, Desktop UI |
| **[chipfighter/context-attachment-manager](https://github.com/chipfighter/context-attachment-manager)** | Failover | Desktop UI |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Sessions & Memory | Desktop UI, Desktop UI |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Sharing | Desktop UI, Isolation & Teams |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Mobile | Desktop UI, Isolation & Teams |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Sessions & Memory | Desktop UI, Failover |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI, Mobile |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Desktop UI, MCP & Security |
| **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | Desktop UI | Isolation & Teams |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Sessions & Memory | Failover, MCP & Security |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | MCP & Security | Desktop UI, Desktop UI |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams & Self-hosting | Mobile |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Accounts, Billing |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Mobile | Desktop UI, MCP & Security |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP & Security | Desktop UI, Failover |
| **[Swival/swival](https://github.com/Swival/swival)** | Failover | Failover |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Accounts | Billing, Mobile |
| **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Billing | Desktop UI |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI, Sessions & Memory |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Sessions & Memory | Mobile |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI, Failover |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Sessions & Memory | Desktop UI, Failover |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation & Teams | Desktop UI, Failover |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Teams & Self-hosting | Isolation & Teams, MCP & Security |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams & Self-hosting | Isolation & Teams, Mobile |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Desktop UI, Failover |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Isolation & Teams, Sharing |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Sharing | Desktop UI, Mobile |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Sessions & Memory | Desktop UI, Failover |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Sessions & Memory | Desktop UI, MCP & Security |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Desktop UI, Providers |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Desktop UI, Failover |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Billing | Billing, Sessions & Memory |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Billing | Billing, Teams & Self-hosting |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Billing, Failover |
| **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Failover | Failover |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Teams & Self-hosting | Billing, MCP & Security |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Sessions & Memory |
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Failover | Failover |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation & Teams | Desktop UI, Failover |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Failover | MCP & Security, Teams & Self-hosting |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Sessions & Memory | Desktop UI, Failover |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | MCP & Security | Desktop UI |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams & Self-hosting | Desktop UI, Sessions & Memory |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Desktop UI, MCP & Security |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Billing | Failover, Isolation & Teams |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Billing | Accounts, Billing |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Isolation & Teams, Sessions & Memory |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Isolation & Teams | Teams & Self-hosting |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Sessions & Memory | Desktop UI |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | MCP & Security | Desktop UI, Isolation & Teams |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | MCP & Security | Desktop UI |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Desktop UI | Desktop UI, Failover |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | MCP & Security | Desktop UI, Failover |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Failover | Failover |
| **[IBM/mcp](https://github.com/IBM/mcp)** | MCP & Security | Desktop UI, Desktop UI |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | MCP & Security | Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.25x the stars (38,518 vs 155,469) |

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
| **[1llu50ry/Decompile](https://github.com/1llu50ry/decompile)** | **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 141.40x the stars (82,011 vs 580) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 62.25x the stars (20,106 vs 323) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.96x the stars (20,106 vs 2,526) | 🤖 auto (high) |
| **[GizClaw/flowcraft](https://github.com/gizclaw/flowcraft)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 4.18x the stars (1,717 vs 411) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.48x the stars (34,360 vs 384) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 41.37x the stars (38,518 vs 931) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.49x the stars (12,211 vs 2,224) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 151.31x the stars (49,932 vs 330) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.95x the stars (34,360 vs 930) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 133.87x the stars (49,932 vs 373) | 🤖 auto (high) |
| **[Tencent/LoopForge](https://github.com/tencent/loopforge)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 30.86x the stars (114,706 vs 3,717) | 🤖 auto (high) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 142.66x the stars (49,932 vs 350) | 🤖 auto (high) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.06x the stars (34,360 vs 354) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 100.48x the stars (30,446 vs 303) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.65x the stars (28,122 vs 4,980) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.28x the stars (49,932 vs 3,759) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 9.48x the stars (12,211 vs 1,288) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.35x the stars (12,211 vs 2,282) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.23x the stars (49,932 vs 372) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.80x the stars (12,211 vs 424) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.96x the stars (24,335 vs 497) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 156.53x the stars (49,932 vs 319) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 486.60x the stars (306,070 vs 629) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.84x the stars (306,070 vs 6,267) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 158.32x the stars (155,469 vs 982) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 56.07x the stars (24,335 vs 434) | 🤖 auto (high) |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 11.67x the stars (169,103 vs 14,494) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 101.05x the stars (141,974 vs 1,405) | 🤖 auto (high) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 7.29x the stars (114,706 vs 15,738) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.21x the stars (12,211 vs 2,899) | 🤖 auto (high) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.22x the stars (30,446 vs 1,877) | 🤖 auto (medium) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 169.44x the stars (82,011 vs 484) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.24x the stars (28,122 vs 583) | 🤖 auto (medium) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 23.88x the stars (306,070 vs 12,817) | 🤖 auto (high) |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | **[decolua/9router](https://github.com/decolua/9router)** | 4.69x the stars (32,598 vs 6,947) | 🤖 auto (medium) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.72x the stars (1,501 vs 551) | 🤖 auto (high) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 32.53x the stars (19,227 vs 591) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.47x the stars (24,335 vs 5,440) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.52x the stars (1,501 vs 427) | 🤖 auto (medium) |
| **[felinics/Memoh](https://github.com/felinics/memoh)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 40.65x the stars (114,706 vs 2,822) | 🤖 auto (medium) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.43x the stars (1,187 vs 489) | 🤖 auto (high) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 73.86x the stars (49,932 vs 676) | 🤖 auto (medium) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.73x the stars (1,501 vs 550) | 🤖 auto (medium) |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 2.18x the stars (20,106 vs 9,244) | 🤖 auto (high) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 2.77x the stars (12,578 vs 4,546) | 🤖 auto (medium) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 16.50x the stars (5,545 vs 336) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 11.11x the stars (19,227 vs 1,731) | 🤖 auto (high) |
| **[Xpropel/Pi-Remote](https://github.com/xpropel/pi-remote)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.98x the stars (661 vs 333) | 🤖 auto (high) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 22.53x the stars (34,360 vs 1,525) | 🤖 auto (high) |
| **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 11.85x the stars (49,932 vs 4,215) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.73x the stars (1,501 vs 868) | 🤖 auto (high) |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/blender-ai-mcp-suite)** | **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 164.68x the stars (82,011 vs 498) | 🤖 auto (high) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,932 vs 28,129) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,098 vs 518) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui-2 | 28.1k | 🔻 Superseded | 1.78x the stars (49,932 vs 28,129) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | teams-self-hosting | 15.7k | 🔻 Superseded | 7.29x the stars (114,706 vs 15,738) |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | sharing | 14.5k | 🔻 Superseded | 11.67x the stars (169,103 vs 14,494) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | teams-self-hosting | 12.8k | 🔻 Superseded | 23.88x the stars (306,070 vs 12,817) |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | billing | 9.2k | 🔻 Superseded | 2.18x the stars (20,106 vs 9,244) |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | billing | 6.9k | 🔻 Superseded | 4.69x the stars (32,598 vs 6,947) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | teams-self-hosting | 6.3k | 🔻 Superseded | 48.84x the stars (306,070 vs 6,267) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.4k | 🔻 Superseded | 4.47x the stars (24,335 vs 5,440) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-teams | 5k | 🔻 Superseded | 5.65x the stars (28,122 vs 4,980) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | teams-self-hosting | 4.5k | 🔻 Superseded | 2.77x the stars (12,578 vs 4,546) |
| **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | desktop-ui-2 | 4.2k | 🔻 Superseded | 11.85x the stars (49,932 vs 4,215) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui-2 | 3.8k | 🔻 Superseded | 13.28x the stars (49,932 vs 3,759) |
| **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | teams-self-hosting | 3.7k | 🔻 Superseded | 30.86x the stars (114,706 vs 3,717) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams-self-hosting | 2.9k | 🔻 Superseded | 4.21x the stars (12,211 vs 2,899) |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | teams-self-hosting | 2.8k | 🔻 Superseded | 40.65x the stars (114,706 vs 2,822) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 Superseded | 7.96x the stars (20,106 vs 2,526) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams-self-hosting | 2.3k | 🔻 Superseded | 5.35x the stars (12,211 vs 2,282) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams-self-hosting | 2.2k | 🔻 Superseded | 5.49x the stars (12,211 vs 2,224) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | teams-self-hosting | 1.9k | 🔻 Superseded | 16.22x the stars (30,446 vs 1,877) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | sessions-memory | 1.7k | 🔻 Superseded | 11.11x the stars (19,227 vs 1,731) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation-teams | 1.5k | 🔻 Superseded | 22.53x the stars (34,360 vs 1,525) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile | 1.4k | 🔻 Superseded | 101.05x the stars (141,974 vs 1,405) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | teams-self-hosting | 1.3k | 🔻 Superseded | 9.48x the stars (12,211 vs 1,288) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 982 | 🔻 Superseded | 158.32x the stars (155,469 vs 982) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 931 | 🔻 Superseded | 41.37x the stars (38,518 vs 931) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-teams | 930 | 🔻 Superseded | 36.95x the stars (34,360 vs 930) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | sessions-memory | 868 | 🔻 Superseded | 1.73x the stars (1,501 vs 868) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui-2 | 676 | 🔻 Superseded | 73.86x the stars (49,932 vs 676) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | teams-self-hosting | 629 | 🔻 Superseded | 486.60x the stars (306,070 vs 629) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | sessions-memory | 591 | 🔻 Superseded | 32.53x the stars (19,227 vs 591) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-teams | 583 | 🔻 Superseded | 48.24x the stars (28,122 vs 583) |
| **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | mcp-security | 580 | 🔻 Superseded | 141.40x the stars (82,011 vs 580) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | sessions-memory | 551 | 🔻 Superseded | 2.72x the stars (1,501 vs 551) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | sessions-memory | 550 | 🔻 Superseded | 2.73x the stars (1,501 vs 550) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui-2 | 518 | 🔻 Superseded | 2.12x the stars (1,098 vs 518) |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | mcp-security | 498 | 🔻 Superseded | 164.68x the stars (82,011 vs 498) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 497 | 🔻 Superseded | 48.96x the stars (24,335 vs 497) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions-memory | 489 | 🔻 Superseded | 2.43x the stars (1,187 vs 489) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | mcp-security | 484 | 🔻 Superseded | 169.44x the stars (82,011 vs 484) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 434 | 🔻 Superseded | 56.07x the stars (24,335 vs 434) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | sessions-memory | 427 | 🔻 Superseded | 3.52x the stars (1,501 vs 427) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams-self-hosting | 424 | 🔻 Superseded | 28.80x the stars (12,211 vs 424) |
| **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | isolation-teams | 411 | 🔻 Superseded | 4.18x the stars (1,717 vs 411) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-teams | 384 | 🔻 Superseded | 89.48x the stars (34,360 vs 384) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui-2 | 373 | 🔻 Superseded | 133.87x the stars (49,932 vs 373) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui-2 | 372 | 🔻 Superseded | 134.23x the stars (49,932 vs 372) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | isolation-teams | 354 | 🔻 Superseded | 97.06x the stars (34,360 vs 354) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | desktop-ui-2 | 350 | 🔻 Superseded | 142.66x the stars (49,932 vs 350) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | billing-2 | 336 | 🔻 Superseded | 16.50x the stars (5,545 vs 336) |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | isolation-teams | 333 | 🔻 Superseded | 1.98x the stars (661 vs 333) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | desktop-ui-2 | 330 | 🔻 Superseded | 151.31x the stars (49,932 vs 330) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 323 | 🔻 Superseded | 62.25x the stars (20,106 vs 323) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui-2 | 319 | 🔻 Superseded | 156.53x the stars (49,932 vs 319) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams-self-hosting | 303 | 🔻 Superseded | 100.48x the stars (30,446 vs 303) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-18 13:05 UTC. 219 live tools · 127 candidates rejected by the quality gates.</sub>
