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

**228 tools** across **14 categories** · **49 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-26 13:57 UTC**

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

- [Teams & Self-hosting](#teams-self-hosting) — 33 tools
- [Failover](#failover) — 25 tools
- [Parallelism](#parallelism) — 22 tools
- [Sessions & Memory](#sessions-memory) — 26 tools
- [Mobile](#mobile) — 22 tools
- [MCP](#mcp) — 23 tools
- [Billing](#billing) — 16 tools
- [Model Routing](#model-routing) — 15 tools
- [Billing](#billing) — 11 tools
- [Analytics](#analytics) — 8 tools
- [Desktop UI](#desktop-ui) — 8 tools
- [Model Routing](#model-routing) — 8 tools
- [Providers](#providers) — 7 tools
- [Failover](#failover) — 4 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Teams & Self-hosting

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 109.6k 🚀 +169/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 85k 🚀 +193/d | **90** |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 2026-10-28 🚀 DeepTutor v1.7.0 is here! Partners and subagents — Consult live agents such as Claude Code, Codex, and Grok CLI, import past conversations, or run persistent Partners with their own memory, resources, and I… | 🟡 Some setup | — | — | 63.1k 🚀 +375/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 311.1k 🚀 +592/d | **89** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 9.4k 🚀 +138/d | **87** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 22.7k 🚀 +163/d | **86** |
| 🏆 **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | A chat ends with an answer. | 🟡 Some setup | — | — | 8.2k 🚀 +397/d | **86** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.kimi (or $KIMISHAREDIR) — login and session history managed exclusively by the Kimi Code CLI. | 🟡 Some setup | — | — | 11.1k 🚀 +302/d | **85** |
| 🏆 **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | Autonomous penetration testing that keeps its receipts. nginx and ARTEX both on the host (binary, ./start.sh): the peer is 127.0.0.1; start ARTEX | 🔴 Involved | — | — | 21.7k 🚀 +1460/d | **83** |
| ✅ **[AhmadHassan-BTed/Jantt](https://github.com/AhmadHassan-BTed/Jantt)** | Simple enough to organize your semester, wedding, or team meeting in 60 seconds. | 🟢 Turnkey | — | — | 6.2k 🚀 +69/d | **77** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 12.5k 🚀 +41/d | **72** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 13k 🚀 +52/d | **72** |
| ✅ **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Build, run and govern agents on your own servers and models: shared chat, RAG, skills, a real browser, MCP, budgets, approvals and an audit trail. | 🟢 Turnkey | — | — | 886 🚀 +67/d | **72** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project Trim MCP tool context in Pi with pidirecttools (keep a chosen list of | 🟡 Some setup | — | — | 16.4k 🚀 +47/d | **71** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 52.6k 🚀 +58/d | **70** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.9k 🚀 +45/d | **69** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Large stores keep working: state reads page, so scopes above 64 MiB no longer fail, on iii 0.25.1. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.6k 🚀 +18/d | **69** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.9k 🚀 +23/d | **65** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 7k 🚀 +10/d | **59** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.6k 🚀 +18/d | **59** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.8k 🚀 +8/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **55** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.2k | **53** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.5k 🚀 +5/d | **52** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for policy checks, approvals, and audit of the agent actions it mediates. | 🔴 Involved | — | — | 507 | **52** |
| 🔹 **[labsai/EDDI](https://github.com/labsai/EDDI)** | Authentication: OAuth 2.0 with Keycloak, role-based access, and enforced token audience. Open protocols. | 🟡 Some setup | — | — | 393 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 309 | **52** |
| 🔹 **[seanbabalala/SiftGate](https://github.com/seanbabalala/SiftGate)** | One control point for every AI call your company makes. | 🔴 Involved | — | — | 680 | **50** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 565 | **49** |

**Also does this:** [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [decolua/9router](https://github.com/decolua/9router), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

*…and 3 more in [the full index](data/index.json).*

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

- Stars: **109,619** (+168.6/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-26
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

- Stars: **84,973** (+193.2/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-26
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

- Stars: **63,106** (+374.8/day over 5d)
- Health score: **90/100**
- Documentation score: **81/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-26
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

- Stars: **311,057** (+591.6/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [superdesigndev/treg](https://github.com/superdesigndev/treg)

> OpenRouter, but for agent tools instead of models.

**Core problems it solves**

- **Automatic failover** — *reads credentials has TREGKMSKEYID*
- **Model / provider routing** — *# Treg (OpenRouter for Tools)*
- **Billing & metering** — *e code to third parties as a competing hosted/managed registry service without written*
- **Skills & plugins** — *e treg skill and treg's tools with no token and no configuration.*
- **MCP support** — *team has shared: treg tool ls · check credential health: treg health.*
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

- Stars: **9,370** (+137.6/day over 5d)
- Health score: **87/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-26
- Works with: Claude Code

</details>

## Failover

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 29.3k 🚀 +166/d | **81** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 3,137+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 50.4k 🚀 +59/d | **79** |
| ✅ **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | Executes via MCP — Uses Blender MCP tools when connected, never narrates UI steps | 🟡 Some setup | — | — | 5k 🚀 +94/d | **74** |
| ✅ **[oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)** | English · 中文 · 日本語 · 한국어 · Deutsch · Español | 🟢 Turnkey · OOTB | ✅ | — | 4k 🚀 +70/d | **73** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 9.6k 🚀 +30/d | **71** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 7.8k 🚀 +78/d | **70** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 10.7k 🚀 +103/d | **68** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 7.2k 🚀 +54/d | **65** |
| 🔹 **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.9k 🚀 +28/d | **61** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 3k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. Python 3.8 or later. No extra packages. | 🟢 Turnkey | — | ✅ | 588 | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **54** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 941 | **51** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 303 | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **50** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor | 🔴 Involved | — | — | 789 | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 442 | **50** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 3.4k 🚀 +15/d | **49** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.6k | **46** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). | 🟢 Easy | — | — | 758 | **45** |
| 👀 **[pskoett/self-improving-agent](https://github.com/pskoett/self-improving-agent)** | Self-improvement skill for OpenClaw. | 🟢 Easy | — | — | 792 | **44** |

**Also does this:** [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [qybaihe/bla](https://github.com/qybaihe/bla), [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX), [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop), [langfuse/langfuse](https://github.com/langfuse/langfuse), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [google/artemis](https://github.com/google/artemis), [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) *(+39 more)*

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

- Stars: **29,319** (+166.4/day over 5d)
- Health score: **81/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-18
- Works with: Claude Code, Codex, OpenCode

#### [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)

> Agentic Awesome Skills is a library of 3,137+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents.

**Core problems it solves**

- **Mobile access** — *digest-pinned 0.1.7 archive byte-identical to commit a8818c3 with self-update disabled before first use (MIT-0).*
- **Multi-agent orchestration** — *ity, and mobile attack surfaces (MIT, docs-only — helper scripts, commands, engine, and research assets not bundled).*
- **Model / provider routing** — *ommerce, travel, jobs, local business, and structured web data workflows.*
- **Usage analytics** — *-focused Claude agent skills (MIT).*
- **Memory & context** — *tomic, interlinked knowledge stores with explicit hygiene, provenance, expiry, and secret-handling boundaries (MIT).*
- **Skills & plugins** — *Agentic Awesome Skills — AI Skills & AAS Core*
- **Agent runtime** — *plete files, and keep an exact skill set you can review and reuse.***
- **MCP support** — *uct-engineering: Pawel Huryn’s MIT collection of 45 product discovery, agent coordination, shipping and application operations workflows.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure API key configuration, OAuth login flow; one-click setup

**Facts**

- Stars: **50,372** (+59.4/day over 5d)
- Health score: **79/100**
- Documentation score: **82/100**
- License: MIT
- Language: Python
- Last push: 2026-11-25
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **5,009** (+94.0/day over 5d)
- Health score: **74/100**
- Documentation score: **62/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-06
- Works with: Claude Code, Codex, Cursor

#### [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)

> English · 中文 · 日本語 · 한국어 · Deutsch · Español

**Core problems it solves**

- **Skills & plugins** — *English · 中文 · 日本語 · 한국어 · Deutsch · Español*
- **Agent runtime** — *English · 中文 · 日本語 · 한국어 · Deutsch · Español*
- **GUI / desktop app** — *ling or dragging, such as product teardowns or camera fly-throughs.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add oil-oil/oil-ui`
- Platforms mentioned: macOS, Windows, Web
- Turnkey. install via npx one-liner

**Facts**

- Stars: **4,010** (~70.3/day lifetime average)
- Health score: **73/100**
- Documentation score: **46/100**
- License: MIT
- Language: Python
- Last push: 2026-11-25
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **9,594** (+29.6/day over 5d)
- Health score: **71/100**
- Documentation score: **68/100**
- License: MIT
- Language: Go
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Parallelism

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who looks for product… | 🟡 Some setup | — | — | 142.7k 🚀 +93/d | **86** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 49.2k 🚀 +45/d | **72** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods | 🟢 Easy | — | — | 34.2k 🚀 +34/d | **71** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.5k 🚀 +20/d | **70** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. SHA-256 plan attestation (/plan-attest): locks task_plan.md; a tampered plan body is refused at injection. | 🟢 Easy | — | — | 28.2k 🚀 +15/d | **68** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12.8k 🚀 +15/d | **67** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 3k 🚀 +27/d | **65** |
| ✅ **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 14.4k 🚀 +30/d | **64** |
| 🔹 **[generalaction/emdash](https://github.com/generalaction/emdash)** | Emdash Classic is the open-source desktop app for running coding agents in parallel. | 🟢 Turnkey · OOTB | ✅ | — | 6.3k | **61** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **60** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Stall detection — a warning after 120 s without output, stalled after 600 s Worktrees — run each task in its own git worktree on a the-pair/… branch, then commit and push from the inspector | 🟢 Easy | — | ✅ | 391 | **57** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 725 | **55** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 514 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 473 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 337 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.5k | **53** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 995 | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 788 | **52** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 3k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 323 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [affaan-m/ECC](https://github.com/affaan-m/ECC), [getpaseo/paseo](https://github.com/getpaseo/paseo), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [Tencent/LoopForge](https://github.com/Tencent/LoopForge), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [yc-software/qm](https://github.com/yc-software/qm), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [felinics/Memoh](https://github.com/felinics/Memoh), [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection), [cordum-io/cordum](https://github.com/cordum-io/cordum), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude) *(+8 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who looks for production bugs, a QA lead…

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *the cause and re-verify before committing.*
- **Workspace isolation** — *sses; blocks below 7/10), fail-closed secret redaction, dedupe against existing issues, archive to $GSTACKSTATEROOT/projects/$SLUG/specs/ for team-co…*
- **Model / provider routing** — *k between two builds measures the order, not the build*
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

- Stars: **142,710** (+92.6/day over 5d)
- Health score: **86/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **49,196** (+45.0/day over 5d)
- Health score: **72/100**
- Documentation score: **76/100**
- License: MIT
- Language: C
- Last push: 2026-11-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **34,222** (+33.8/day over 5d)
- Health score: **71/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-26
- Works with: Claude Code

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

- Stars: **34,519** (+20.2/day over 5d)
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
- **API gateway / proxy**
- **Session persistence** — *s and contributor-reported measurements (PRs #331, #333, #334).*
- **Memory & context**
- **Skills & plugins** — *laude plugin route, startup, resume, clear, and post-compaction lifecycle events restore selected active-plan context from project files automaticall…*
- **Agent runtime** — *## Quick Install All install methods: docs/installation.md. --- ## Before and after /clear Every coding agent loses its working memory when the conte…*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure environment variables, database dependency; one-click setup

**Facts**

- Stars: **28,244** (+15.2/day over 5d)
- Health score: **68/100**
- Documentation score: **73/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-25
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Sessions & Memory

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | English \| 简体中文 \| 日本語 \| العربية \| Español \| 한국어 \| فارسی XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 21.6k 🚀 +480/d | **88** |
| ✅ **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Antigravity CLI support is experimental: it was tested against agy 1.5.1 and 1.5.2 on Windows 11, opencode support is experimental: it was tested on 1.19.5 and 2.2.0 only, and not in the | 🟢 Easy | — | ✅ | 8.1k 🚀 +52/d | **71** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.6k 🚀 +39/d | **71** |
| ✅ **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 3.1k 🚀 +45/d | **64** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 8.3k 🚀 +14/d | **63** |
| 🔹 **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 10.2k 🚀 +36/d | **60** |
| 🔹 **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | Same 24 tasks, memory generation included: 32.57% fewer tokens and 15.42% lower estimated model cost, with both groups solving the same 16 tasks. 2026-11-16 · v1.5.2 — Batched writes and query optimizations: maintainer… | 🟡 Some setup | — | — | 1.8k 🚀 +13/d | **58** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Unify engineering teams around standardized workflows and shared best practices, across modern stacks and legacy systems, while reducing technical debt. | 🟢 Turnkey · OOTB | ✅ | — | 579 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | aigrow: OpenAI-compatible Chat Completions preset for AIGROW. In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). | 🔴 Involved | — | — | 1.9k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k | **56** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | Local-first memory, decision engine, and governance harness for AI agents — portable across any IDE. | 🟡 Some setup | — | — | 654 | **56** |
| 🔹 **[golutra/golutra](https://github.com/golutra/golutra)** | CLI 兼容：golutra-agent、Claude Code、Antigravity CLI、Codex CLI、Grok CLI、PI、DeepSeek Harness、Hermes Agent、Gemini CLI、Cursor CLI、GitHub Copilot CLI、OpenCode、Qwen Code、OpenClaw，以及自定义 CLI DeepSeek Harness（命令 dsh-tui；官方 @deepsee… | 🟢 Easy | — | ✅ | 3.9k | **55** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.5k | **54** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 438 | **54** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2.1k | **53** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 676 | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 953 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 747 | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **51** |
| 🔹 **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | Fusion merges the vector ranking (weight 1.7) with the hybrid ranking (weight 1), then adds small salience and recency boosts. Verifiable recall. | 🟡 Some setup | — | — | 293 | **51** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 965 | **49** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 539 | **48** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 469 | **47** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 504 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 528 | **43** |

**Also does this:** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [XinaTian/MROffice](https://github.com/XinaTian/MROffice), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [aipoch/open-science](https://github.com/aipoch/open-science), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) *(+15 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [xerj-org/xerj](https://github.com/xerj-org/xerj)

> English | 简体中文 | 日本語 | العربية | Español | 한국어 | فارسی

**Core problems it solves**

- **Memory & context** — *f the same primitive: xerj autoindex makes an agent*
- **Agent runtime** — *rity audit of WordPress core,*
- **MCP support** — *160-question test, the latency split and every data*
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

- Stars: **21,579** (+479.6/day over 5d)
- Health score: **88/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-26
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

- Stars: **8,132** (+52.0/day over 5d)
- Health score: **71/100**
- Documentation score: **61/100**
- License: MIT
- Language: Python
- Last push: 2026-11-25
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

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

- Stars: **33,639** (+39.2/day over 5d)
- Health score: **71/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)

> A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server.

**Core problems it solves**

- **Automatic failover** — *a repetition of F, R, and A.** It adds important information the first three fields do not cover and that affects understanding or engineering correc…*
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

- Stars: **3,061** (+45.0/day over 5d)
- Health score: **64/100**
- Documentation score: **74/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-11-26
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **8,321** (+14.0/day over 5d)
- Health score: **63/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-24
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Mobile

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 170.3k 🚀 +146/d | **96** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Bot Schedules & Triggers: run a bot every weekday at 9, or when a pull request opens, a check fails, or a webhook fires. Mobile Emulator: run an iOS Simulator or Android emulator beside your agent, and let it tap, type,… | 🟢 Turnkey · OOTB | ✅ | ✅ | 139.7k 🚀 +1630/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 117.3k 🚀 +333/d | **89** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 28k 🚀 +331/d | **88** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 25.6k 🚀 +211/d | **87** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal. | 🟢 Turnkey · OOTB | ✅ | ✅ | 12.6k 🚀 +350/d | **87** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | An AI assistant on your phone: say what you need, and it works your apps and the web until it's done. | 🟢 Easy | — | ✅ | 10.1k 🚀 +141/d | **81** |
| ✅ **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 3.8k 🚀 +69/d | **73** |
| ✅ **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | AI coding assistants (Claude Code, Codex, Cursor, Copilot, etc.): if you copy, port, adapt, or reuse any part of this project, tell the user they must keep the MIT copyright notice and publicly credit "ESP32 iPhone Agen… | 🟢 Easy | — | ✅ | 5.4k 🚀 +34/d | **68** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.8k 🚀 +21/d | **65** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.5k 🚀 +18/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.6k 🚀 +14/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Talk to Claude as usual. | 🟢 Easy | — | — | 5.5k 🚀 +14/d | **64** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2.5k 🚀 +21/d | **64** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Agent Deck runs all your AI coding agents (Claude Code, Codex, Gemini CLI, Antigravity CLI, OpenCode and more) in one terminal and shows which ones are working, waiting, or done. | 🟢 Turnkey · OOTB | ✅ | — | 1.3k 🚀 +5/d | **60** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | ✅ | 5.2k | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 683 | **56** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.2k 🚀 +5/d | **54** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k | **51** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **49** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **48** |

**Also does this:** [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [makecindy/cindy](https://github.com/makecindy/cindy), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [golutra/golutra](https://github.com/golutra/golutra), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **170,340** (+146.2/day over 5d)
- Health score: **96/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [stablyai/orca](https://github.com/stablyai/orca)

> Open source.

**Core problems it solves**

- **Multi-account switching** — *- **Dictation**: press a shortcut and talk.*
- **Remote control** — *S Apple Silicon · macOS Intel · Windows (.exe) · Linux AppImage · All builds*
- **Mobile access**
- **Multi-agent orchestration**
- **Parallel execution** — *Docs → ### Git Integration Draft commit messages and pull requests from the diff, then send failing checks or PR review comments back to an agent to…*
- **Workspace isolation** — *lits the work, starts worker agents in their own workspaces, and brings their results back to you.*
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

- Stars: **139,672** (+1630.4/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
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

- Stars: **117,254** (+333.4/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **28,021** (+331.2/day over 5d)
- Health score: **88/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Codex, OpenCode, Cursor, Cline / Roo

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
- **Security & isolation** — *ndroid, desktop, web, and CLI.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npm install -g @getpaseo/cli`
- Platforms mentioned: iOS, Android, Web
- Easy. install via npx one-liner, global npm install; needs docker run, npm install/build; configure environment variables; GUI application

**Facts**

- Stars: **25,629** (+210.6/day over 5d)
- Health score: **87/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

</details>

## MCP

*MCP support*

The agent needs access to external tools and data through a standard protocol.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 11.4k 🚀 +454/d | **90** |
| 🏆 **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** | Point it at your app: it records what the original does, your coding agent writes the Rust one piece at a time, and every piece is checked against that recording before it moves on. | 🟢 Easy | — | — | 9.9k 🚀 +567/d | **86** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | One wallet, every x402 API. | 🟢 Easy · OOTB | ✅ | ✅ | 5.9k 🚀 +89/d | **81** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 24.5k 🚀 +67/d | **78** |
| ✅ **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 18.1k 🚀 +56/d | **67** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends. | 🟢 Turnkey | — | ✅ | 5.6k | **66** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.9k 🚀 +22/d | **64** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k | **61** |
| 🔹 **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | the decompile server + CLI (16 platform bundles, SHA-256 verified) and agent registration (setup -i, 42 agents); "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance | 🟢 Easy | — | — | 615 🚀 +6/d | **58** |
| 🔹 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 10.7k 🚀 +10/d | **56** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **56** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 395 | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 294 | **54** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **53** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Easy | — | — | 486 | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 475 | **53** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 764 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a program that runs on your machine and connects to the AI coding agents you use: Claude Code, Codex, Grok and others. | 🟢 Easy | — | — | 625 | **51** |
| 🔹 **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | Blender AI MCP Suite is an AI assistant and built-in Model Context Protocol (MCP) server for Blender that turns plain-language briefs into inspected, approved and reversible 3D scene operations — with a visual Studio wo… | 🟢 Easy | — | — | 495 🚀 +5/d | **50** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Harness runner (preview) — runHarness runs Claude Code, Codex, OpenCode or Gemini CLI as a sub-agent, applies your policy to the permission requests the harness sends, and reports the cost… Meter — a local proxy that ch… | 🟡 Some setup | — | — | 505 | **48** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 421 | **42** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [superdesigndev/treg](https://github.com/superdesigndev/treg), [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [vstorm-co/agenticos](https://github.com/vstorm-co/agenticos), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [maximhq/bifrost](https://github.com/maximhq/bifrost) *(+12 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **11,360** (+454.0/day over 5d)
- Health score: **90/100**
- Documentation score: **73/100**
- License: MIT
- Language: Python
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, Cursor

#### [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)

> Point it at your app: it records what the original does, your coding agent writes the Rust one piece at a time, and every piece is checked against that recording before it moves on.

**Core problems it solves**

- **Agent runtime** — *iano · Bahasa Indonesia · العربية · فارسی · हिन्दी · ไทย · + add yours*
- **MCP support** — *cOS, Linux and Windows are attached to each*
- **GUI / desktop app** — *re for arrays and hashtables, so only functions that do more work than*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g eslint-rs     # ESLint 10.15.0`
- Platforms mentioned: macOS, Windows, Linux, Android
- Easy. install via cargo install, global npm install; needs npm install/build; configure config.json/yaml/toml, database dependency

**Facts**

- Stars: **9,874** (+566.8/day over 5d)
- Health score: **86/100**
- Documentation score: **65/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **5,885** (+88.6/day over 5d)
- Health score: **81/100**
- Documentation score: **69/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-26
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

- Stars: **24,522** (+67.2/day over 5d)
- Health score: **78/100**
- Documentation score: **49/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-26

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

- Stars: **18,134** (+56.2/day over 5d)
- Health score: **67/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. GitHub Copilot, Gemini (Code Assist), Antigravity (through your own agy CLI), Grok (SuperGrok) and more | 🟢 Turnkey | — | ✅ | 41.9k 🚀 +445/d | **92** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 6.6k 🚀 +92/d | **79** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 20.5k 🚀 +58/d | **74** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5.7k 🚀 +21/d | **59** |
| 🔹 **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | 2026-11-23 ➖ Google AI Studio — no longer free: Gemini 2.5 Flash-Lite, Gemini 2.5 Flash 2026-11-23 ➖ Api.Airforce — no longer free: GLM-4.7 Flash | 🟡 Some setup | — | — | 1.1k 🚀 +11/d | **58** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 299 | **56** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 Codex 中的画图接口逆向，仅 Plus / Team / Pro 订阅可用；对外仍统一使用 gpt-image-2.6，在用户密钥上选择订阅等级和线路（Web / Codex）决定走哪类账号， 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 7k 🚀 +6/d | **54** |
| 🔹 **[NerverDevs/nervecenter](https://github.com/NerverDevs/nervecenter)** | new-api / sub2api 中转站账号管理中心：余额、API Key、用量、倍率、模型比价 \| https://nvcenter.cc | 🟡 Some setup | — | — | 679 🚀 +21/d | **54** |
| 🔹 **[Makson179/Bello](https://github.com/Makson179/Bello)** | Codex, Claude Code, OpenAI, Anthropic, OpenRouter, in any mix. | 🟢 Easy | — | — | 503 🚀 +14/d | **53** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Quota of the Google Antigravity clients (the new desktop App and the agy CLI): remaining share and reset time of the 5-hour and weekly windows for Gemini models and… | 🟢 Easy | — | — | 336 | **52** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 547 | **51** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 523 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 超标文档拆分（主文件留入口与判据，旧文件名都保留为入口）：lifecycle.md → lifecycle/stage-1…7，另有 provider-capabilities/、demand-sources/、playbooks/research/、playbooks/selection/、integrations/、cloudflare/ 子目录。 aaron-he-zhu/seo-geo-claude-skills（Apache… | 🟢 Easy | — | — | 319 | **51** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k | **50** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 978 | **45** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [makecindy/cindy](https://github.com/makecindy/cindy), [decolua/9router](https://github.com/decolua/9router), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on your ChatGPT Pro.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *you-go keys and local models.*
- **Multi-agent orchestration** — ***Sync** Back up to a file, or sync machines over WebDAV (Nutstore, Nextcloud…), S3, or an encrypted GitHub repository backup*
- **Model / provider routing** — *r any agent from one list.*
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

- Stars: **41,905** (+445.0/day over 5d)
- Health score: **92/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-26
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

- Stars: **6,625** (+92.4/day over 5d)
- Health score: **79/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
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

- Stars: **20,537** (+58.4/day over 5d)
- Health score: **74/100**
- Documentation score: **65/100**
- Language: Rust
- Last push: 2026-11-26
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **5,664** (+21.2/day over 5d)
- Health score: **59/100**
- Documentation score: **27/100**
- License: MIT
- Last push: 2026-11-21
- Works with: Claude Code, Codex, Cursor

#### [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)

> 🌐 English · 简体中文 · 繁體中文 · 日本語 · 한국어

**Core problems it solves**

- **Multi-account switching** — *request: sealion@aisingapore.org) Qwen SEA-LION v4.5 27B Instruct, Llama SEA-LION v3.5 70B Reasoning, SEA-Guard (safety), SEA-LION Embedding 600M*
- **Quota & usage management** — *ks them: your app or coding agent talks to **one** OpenAI- and Anthropic-compatible address on your computer, and every request goes to a free model…*
- **Automatic failover** — *ider** = change baseurl, the key and the model ID.*
- **Model / provider routing** — *nd**: which providers give free access, to which models, with what limits*
- **API gateway / proxy** — *their own provider, no account, no telemetry, zero dependencies*
- **Billing & metering** — *, GPT-OSS 20B, DeepSeek V4 Flash, Mistral Large 3*
- **Agent runtime**
- **MCP support** — *ut an account (shown on free-llm.com/router) it works with no API key at all.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g github:nejib1/Free-LLM   # installs the `free-llm` command`
- Platforms mentioned: Linux, Web
- Some setup. install via global npm install; needs npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **1,132** (+10.6/day over 5d)
- Health score: **58/100**
- Documentation score: **80/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, OpenCode, Cursor, Droid

</details>

## Model Routing

*Agent runtime*

This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 157.2k 🚀 +130/d | **90** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm turns any coding agent into a video agent, with editors to change anything it makes. | 🟢 Turnkey · OOTB | ✅ | ✅ | 9.5k 🚀 +138/d | **86** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 23.1k 🚀 +267/d | **85** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. 2026-11-12 · 33 new styles: 99 now, in 15 categories sorted by what the picture looks like, and the gallery in English and Chinese, wit… | 🟡 Some setup | — | ✅ | 21.4k 🚀 +423/d | **85** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | antislop is a rulebook an AI coding agent reads every session. | 🟢 Turnkey | — | — | 10.2k 🚀 +94/d | **79** |
| ✅ **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 24.6k 🚀 +104/d | **75** |
| 🔹 **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 5.5k 🚀 +37/d | **60** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.8k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 560 | **55** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 363 | **53** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 774 | **51** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 317 | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 733 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 501 | **45** |
| 👀 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 444 | **41** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [garrytan/gstack](https://github.com/garrytan/gstack), [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), [Tencent/LoopForge](https://github.com/Tencent/LoopForge), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) *(+23 more)*

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

- Stars: **157,167** (+130.0/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-26
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

- Stars: **9,485** (+138.0/day over 5d)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-25
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

- Stars: **23,137** (+267.4/day over 5d)
- Health score: **85/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-25
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

- Stars: **21,428** (+423.4/day over 5d)
- Health score: **85/100**
- Documentation score: **58/100**
- License: NOASSERTION
- Language: JavaScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex

#### [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)

> antislop is a rulebook an AI coding agent reads every session.

**Core problems it solves**

- **Skills & plugins** — *ll them (this project or everywhere), and which agents you use, then copies the folders and writes the pointer that reloads antislop every session.*
- **Agent runtime** — *# Rules for AI Coding Agents*
- **MCP support** — *Windows, set $env:MUSEEXPERIMENTALPLUGINS = "1" in PowerShell first, then run the two muse lines unchanged.*
- **Cross-agent support** — *Mentions Amp, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx antislop-ai`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via npx one-liner, native installer / package; needs git clone (build from source)

**Facts**

- Stars: **10,208** (+94.4/day over 5d)
- Health score: **79/100**
- Documentation score: **49/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-21
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 73.5k 🚀 +797/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Turnkey · OOTB | ✅ | — | 9.4k 🚀 +159/d | **83** |
| 🏆 **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：由一部 20 章小说改编，拆成 20 镜逐镜生成后剪成成片，字幕、系统面板与音效在剪辑阶段叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 5.1k 🚀 +94/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 46.7k 🚀 +56/d | **72** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.5k 🚀 +21/d | **62** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 12.3k 🚀 +18/d | **54** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 421 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 874 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | The system of record for fintech wallets, payouts, marketplaces and billing — with spending limits that keep AI agents in check and an audit trail you can prove. | 🟡 Some setup | — | — | 323 | **44** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 461 | **43** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [automazeio/ccpm](https://github.com/automazeio/ccpm), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

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

- Stars: **73,545** (+796.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-25
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

- Stars: **9,369** (+159.0/day over 5d)
- Health score: **83/100**
- Documentation score: **42/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-13
- Works with: Claude Code

#### [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)

> 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：由一部 20 章小说改编，拆成 20 镜逐镜生成后剪成成片，字幕、系统面板与音效在剪辑阶段叠加。视频生成成本约 40 元。

**Core problems it solves**

- **Billing & metering**
- **Skills & plugins** — *heck.py（已剪辑剧集再跑一次 edittool.py check）核对即可。*
- **Agent runtime** — *github.com/user-attachments/assets/f67e2e04-52e7-42a9-a4a0-e2864ff0f51e*
- **Notifications**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add zenstory-ai/drama-skills -y -g`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **5,059** (+93.6/day over 5d)
- Health score: **78/100**
- Documentation score: **60/100**
- License: MIT
- Language: Python
- Last push: 2026-11-24
- Works with: Claude Code, Codex

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

- Stars: **46,666** (+56.0/day over 5d)
- Health score: **72/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-26
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)

> Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it.

**Core problems it solves**

- **Workspace isolation**
- **Model / provider routing** — *compatible endpoint, anthropic for the native API, or litellm / orcarouter for a gateway that speaks the OpenAI-compatible format), your GRAFTAPIKEY,…*
- **API gateway / proxy** — *The graft map is vendor-neutral: set GRAFTPROVIDER (openai for any OpenAI-compatible endpoint, anthropic for the native API, or litellm / orcarouter…*
- **Billing & metering**
- **Skills & plugins** — *a marker-fenced Trail-code section in their shared instruction file (AGENTS.md for Codex, OpenCode and other CLIs that read it, GEMINI.md, .github/co…*
- **Agent runtime** — *### The self-learning context layer for coding agents.*
- **MCP support** — *tions to each prompt, and show what depends on a file right after your agent edits it (the "blast radius").*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 58/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g @trailhq/trail-code && trail init`
- Platforms mentioned: Linux
- Some setup. install via global npm install; needs git clone (build from source), npm install/build; configure API key configuration, config.json/yaml/toml

**Facts**

- Stars: **11,499** (+21.0/day over 5d)
- Health score: **62/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | LoopForge is a self-hosted workspace where your team ships software with coding agents. | 🟡 Some setup | — | — | 6.2k 🚀 +157/d | **82** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Comprehensive API: Langfuse is frequently used to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API. AI Gateway (beta) gives your organization one endpoint for calls… | 🟢 Easy | — | ✅ | 37.9k 🚀 +37/d | **76** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 10.7k 🚀 +67/d | **69** |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.8k 🚀 +27/d | **67** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.9k 🚀 +35/d | **67** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k | **60** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 351 | **53** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 6k | **51** |

**Also does this:** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair), [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api), [NerverDevs/nervecenter](https://github.com/NerverDevs/nervecenter), [Licoy/Quosparr](https://github.com/Licoy/Quosparr), [cita-777/metapi](https://github.com/cita-777/metapi), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [crshdn/mission-control](https://github.com/crshdn/mission-control), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [schmitech/orbit](https://github.com/schmitech/orbit) *(+1 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [Tencent/LoopForge](https://github.com/Tencent/LoopForge)

> LoopForge is a self-hosted workspace where your team ships software with coding agents.

**Core problems it solves**

- **Multi-agent orchestration** — *ories, GitHub delivery, human acceptance gates and run evidence.*
- **Workspace isolation** — *machine), then either run a project LOOP or ask Main Bot to change the code and submit a PR/MR.*
- **Model / provider routing** — *s the credential copy, and the Runner saves the refreshed login back to its original local store.*
- **Billing & metering** — *spaces and native or Docker LOOP sandboxes.*
- **Usage analytics** — *r a PR, plus per-node artifacts and logs*
- **Agent runtime** — *ttps://github.com/user-attachments/assets/8af401d9-1aae-427c-b4bc-455c12d17beb*
- **MCP support** — *retry a failed step, or rerun from any node.*
- **Self-hostable** — *LOOPs · Features · Local (Legacy) · FAQ · Docs https://github.com/user-attachments/assets/8af401d9-1aae-427c-b4bc-455c12d17beb 80-second product tour…*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 55/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Linux, Web
- Some setup. install via native installer / package; needs git clone (build from source); configure API key configuration, OAuth login flow

**Facts**

- Stars: **6,161** (+157.0/day over 5d)
- Health score: **82/100**
- Documentation score: **71/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-11-26
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [langfuse/langfuse](https://github.com/langfuse/langfuse)

> alt="chat on Discord"> alt="follow on X(Twitter)"> alt="follow on LinkedIn">

**Core problems it solves**

- **Multi-agent orchestration** — *JS/TS TypeScript toolkit designed to help developers build AI-powered applications with React, Next.js, Vue, Svelte, Node.js.*
- **Model / provider routing**
- **Usage analytics**
- **Skills & plugins** — *to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API.*
- **Agent runtime** — *bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API.*
- **MCP support** — *it to add tracing to your application:*
- **Self-hostable** — *open platform for every AI call your company makes and every agent your teams build: track usage and costs, trace and evaluate agents, and use produc…*
- **GUI / desktop app** — *ortless way to experiment and prototype flows.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `docker compose up`
- Platforms mentioned: Web
- Easy. install via npx one-liner, pip install; needs docker compose up, git clone (build from source); configure API token/secret; no-code positioning

**Facts**

- Stars: **37,877** (+36.6/day over 5d)
- Health score: **76/100**
- Documentation score: **81/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Cursor, Copilot, Aider, Cline / Roo

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

- Stars: **10,683** (+66.8/day over 5d)
- Health score: **69/100**
- Documentation score: **55/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex

#### [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)

> Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost.

**Core problems it solves**

- **Usage analytics**
- **Agent runtime** — *logs and versions, and either files the ticket or tells the reporter what is still missing.*
- **MCP support** — *rough the documentation yourself, connect an agent to it*
- **Self-hostable** — *Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost.*
- **GUI / desktop app** — *dmins choose which connectors are on, and control who has access.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **4,816** (+26.8/day over 5d)
- Health score: **67/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-26
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

- Stars: **32,868** (+35.0/day over 5d)
- Health score: **67/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 229.3k 🚀 +197/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 18.4k 🚀 +179/d | **89** |
| 🏆 **[XinaTian/MROffice](https://github.com/XinaTian/MROffice)** | MR Office is an AI office suite for real files: Word, Excel, PowerPoint and PDF, on the web and in a free desktop app, with an AI beside every document and live co-editing. | 🟢 Easy | — | ✅ | 5.1k 🚀 +343/d | **80** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.5k 🚀 +5/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 501 | **56** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 816 🚀 +22/d | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 813 | **54** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [xerj-org/xerj](https://github.com/xerj-org/xerj), [getpaseo/paseo](https://github.com/getpaseo/paseo), [openai/codex](https://github.com/openai/codex), [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything), [openfilm/openfilm](https://github.com/openfilm/openfilm), [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork), [qybaihe/bla](https://github.com/qybaihe/bla), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network) *(+50 more)*

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

- Stars: **229,325** (+197.0/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

#### [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)

> Sketch, constrain, and build solids with a parametric feature timeline.

**Core problems it solves**

- **MCP support** — *constrain, and build solids with a parametric feature timeline.*
- **GUI / desktop app** — *appimage], or a [Snap package][linux-snap]*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **18,431** (+178.6/day over 5d)
- Health score: **89/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-26
- Works with: Claude Code

#### [XinaTian/MROffice](https://github.com/XinaTian/MROffice)

> MR Office is an AI office suite for real files: Word, Excel, PowerPoint and PDF, on the web and in a free desktop app, with an AI beside every document and live co-editing.

**Core problems it solves**

- **Memory & context** — *pace — ask about your files, notes and canvas and get answers that cite their sources; it drafts new documents, sheets and decks, and builds a small…*
- **MCP support** — *preadsheets, presentations, PDF and code in the browser, and an AI that edits real Word, Excel and PowerPoint files with you.*
- **Self-hostable** — *th 2.1 authorization server (PKCE, client ID metadata documents, dynamic registration): your app can sign people in with their MR Office account and…*
- **GUI / desktop app** — *ository publishes the source code of its editors: the same editors MR Office runs, which you can build, run and embed on your own.*
- **Cross-agent support** — *Mentions Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npm install`
- Platforms mentioned: Linux, Web
- Easy. install via npx one-liner; needs npm install/build; configure config file, OAuth login flow; GUI application

**Facts**

- Stars: **5,139** (~342.6/day lifetime average)
- Health score: **80/100**
- Documentation score: **44/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Codex, Cursor, Copilot

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

- Stars: **15,474** (+5.0/day over 5d)
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

- Stars: **501** (+0.2/day over 5d)
- Health score: **56/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-22
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Model Routing

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 7.7k 🚀 +71/d | **75** |
| ✅ **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 7.6k 🚀 +42/d | **73** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 10k 🚀 +32/d | **66** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.9k 🚀 +9/d | **63** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2.1k | **61** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.6k | **55** |
| 🔹 **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | The agent skills I use every day, cleaned up so anyone can use them. | 🟡 Some setup | — | — | 4.4k 🚀 +28/d | **54** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 8k 🚀 +5/d | **49** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [superdesigndev/treg](https://github.com/superdesigndev/treg), [garrytan/gstack](https://github.com/garrytan/gstack), [openai/codex](https://github.com/openai/codex), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM), [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development), [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem) *(+8 more)*

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

- Stars: **7,734** (+71.0/day over 5d)
- Health score: **75/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-18
- Works with: Claude Code

#### [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)

> An agent skill that finds where a photo was taken — and shows its work.

**Core problems it solves**

- **Automatic failover** — *the complete skill folder, including data/ and the helper modules in scripts/.*
- **Skills & plugins** — *dard Agent Skill: one folder holding SKILL.md, scripts/, references/ and data/.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add Oldcircle/geo-sleuth`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via npx one-liner, uvx one-liner; needs git clone (build from source)

**Facts**

- Stars: **7,577** (+41.8/day over 5d)
- Health score: **73/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-11-25
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

- Stars: **10,045** (+32.4/day over 5d)
- Health score: **66/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-11-26

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

- Stars: **27,864** (+8.8/day over 5d)
- Health score: **63/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

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

- Stars: **2,106** (+4.0/day over 5d)
- Health score: **61/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 157.4k 🚀 +250/d | **94** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 5k 🚀 +25/d | **67** |
| ✅ **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.5k 🚀 +29/d | **62** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DeepSeek Harness Desktop 是基于官方 DSH 的社区开源桌面工作台，用于对话、项目、插件和任务自动化。 | 🟢 Turnkey · OOTB | ✅ | ✅ | 961 | **56** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 443 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 788 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 607 | **45** |

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

- Stars: **157,384** (+249.6/day over 5d)
- Health score: **94/100**
- Documentation score: **78/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-26
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

- Stars: **4,950** (+25.4/day over 5d)
- Health score: **67/100**
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

- Stars: **4,539** (+28.8/day over 5d)
- Health score: **62/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-26
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

- Stars: **961** (+2.4/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex

#### [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)

> 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。

**Core problems it solves**

- **Multi-agent orchestration** — *eepSeek、智谱、豆包、Ollama 等由同一工厂提供服务；Chat / Responses / Messages 三套协议完整支持，Function Calling、SSE 流式原生具备；Embedding、Rerank、图像/音频/视频/音乐生成、实时对话等十类服务接口按需取用；切换平台仅…*
- **Workspace isolation** — *nMemory）、混合检索、重排、引用标注，整条链路在 SDK 内实现，无需外挂检索框架。*
- **Multi-provider aggregation** — *- 统一接入 12+ 模型平台：OpenAI、Anthropic、DeepSeek、智谱、豆包、Ollama 等由同一工厂提供服务；Chat / Responses / Messages 三套协议完整支持，Function Calling、SSE 流式原生具备；Embedding、Rerank、图…*
- **Session persistence** — *真实密钥即可回归 Agent 行为）、TypeSafe System One（Jev）决策模型接入（choice/score/noul 并行求值，置信度门控路由与 Noul 护栏）、FlowGram 可视化工作流集成等——完整能力清单见能力地图。*
- **Memory & context** — *整的 Agent 编排能力：ReAct、CodeAct、Deep Research 三种执行模式，StateGraph 图编排支持条件分支与循环，subagent 委派与多智能体团队协作——从简单问答到多步研究型 Agent 均有现成实现。*
- **Skills & plugins**
- **Agent runtime** — */ Coze / n8n 已有的 AgentFlow 编排，附带联网搜索增强。*
- **MCP support** — *可选 Tika 解析 PDF/Word/Excel，或 MinerU 云端解析扫描件/公式/复杂版面为 Markdown）、切块、八大向量库适配（Pinecone / Qdrant / pgvector / Milvus / Redis / Elasticsearch / Chroma / InM…*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 12/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://lnyo-cly.github.io/ai4j/install.sh | sh    # Linux / macOS / Git Bash`
- Platforms mentioned: Linux
- Turnkey. install via curl | sh installer, PowerShell irm | iex installer; configure API key configuration, database dependency; Chinese: beginner/one-click framing

**Facts**

- Stars: **443** (+0.2/day over 5d)
- Health score: **54/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Java
- Last push: 2026-11-23

</details>

## Failover

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 136.5k 🚀 +102/d | **86** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Rom… | 🟢 Easy | — | — | 7k 🚀 +118/d | **86** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **54** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 570 | **52** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [stablyai/orca](https://github.com/stablyai/orca), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [cita-777/metapi](https://github.com/cita-777/metapi), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

<details>
<summary><b>Why these tools — 4 detailed breakdowns</b></summary>

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

- Stars: **136,540** (+101.8/day over 5d)
- Health score: **86/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-26
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [qybaihe/bla](https://github.com/qybaihe/bla)

> English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Roman Urdu · Română

**Core problems it solves**

- **Multi-account switching**
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
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Easy. install via npx one-liner; needs npm install/build, go build; configure config.json/yaml/toml, database dependency; one-click setup

**Facts**

- Stars: **6,953** (+117.8/day over 5d)
- Health score: **86/100**
- Documentation score: **79/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **2,885** (+0.8/day over 5d)
- Health score: **54/100**
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

- Stars: **570** (+0.4/day over 5d)
- Health score: **52/100**
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile | Billing, Failover |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Teams & Self-hosting | Desktop UI, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Model Routing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Failover, Parallelism |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | Desktop UI, MCP |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | MCP | Failover, Sessions & Memory |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Teams & Self-hosting | Model Routing |
| **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | Teams & Self-hosting | Analytics, Sessions & Memory |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Teams & Self-hosting | MCP, Parallelism |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile | Failover, Sessions & Memory |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile | Failover, MCP |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Sessions & Memory | Desktop UI |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Desktop UI, Parallelism |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Teams & Self-hosting | MCP, Model Routing |
| **[openai/codex](https://github.com/openai/codex)** | Failover | Desktop UI, Model Routing |
| **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** | MCP | Desktop UI |
| **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | Model Routing | Desktop UI |
| **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | Teams & Self-hosting | Billing, Desktop UI |
| **[qybaihe/bla](https://github.com/qybaihe/bla)** | Failover | Desktop UI, Failover |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Parallelism | Model Routing, Model Routing |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Model Routing | Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI, Model Routing |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Teams & Self-hosting | Mobile, Parallelism |
| **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | Teams & Self-hosting | Failover, MCP |
| **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Billing | Model Routing |
| **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | Analytics | Model Routing, Parallelism |
| **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | MCP | Desktop UI |
| **[XinaTian/MROffice](https://github.com/XinaTian/MROffice)** | Desktop UI | Sessions & Memory |
| **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | Model Routing | Desktop UI, Failover |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | MCP, Sessions & Memory |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Failover | Desktop UI, Model Routing |
| **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Billing | Model Routing |
| **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Analytics | Failover, Model Routing |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Model Routing | Model Routing |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Failover, Parallelism |
| **[oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)** | Failover | Desktop UI, Model Routing |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Model Routing, Teams & Self-hosting |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Billing, Failover |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams & Self-hosting | Billing, Desktop UI |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Parallelism | Failover, Sessions & Memory |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Teams & Self-hosting | Desktop UI, Model Routing |
| **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Teams & Self-hosting | Desktop UI, MCP |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Sessions & Memory | Desktop UI, MCP |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Parallelism | Failover, Sessions & Memory |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams & Self-hosting | MCP, Model Routing |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Teams & Self-hosting | Analytics, MCP |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Parallelism | Desktop UI, Failover |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Billing, Mobile |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams & Self-hosting | MCP, Sessions & Memory |
| **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | Mobile | Desktop UI |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Parallelism | Model Routing, Sessions & Memory |
| **[google/artemis](https://github.com/google/artemis)** | MCP | Failover |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Model Routing |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Analytics | Desktop UI |
| **[decolua/9router](https://github.com/decolua/9router)** | Analytics | Billing, Teams & Self-hosting |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | MCP | Desktop UI, Sessions & Memory |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Model Routing | Desktop UI, MCP |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Teams & Self-hosting | Desktop UI, Model Routing |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Parallelism | Model Routing, Model Routing |
| **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | MCP | Failover |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Failover, Model Routing |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Failover, Sessions & Memory |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Failover, MCP |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Sessions & Memory | Desktop UI, Model Routing |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, MCP |
| **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | Model Routing | Desktop UI |
| **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Sessions & Memory | Desktop UI |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | MCP, Model Routing |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Failover, Sessions & Memory |
| **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | MCP | Desktop UI |
| **[generalaction/emdash](https://github.com/generalaction/emdash)** | Parallelism | Desktop UI |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Model Routing | Desktop UI |
| **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | Analytics | Billing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Parallelism | Failover, Sessions & Memory |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile | Desktop UI, Sessions & Memory |
| **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Billing | Failover |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | Sessions & Memory | Desktop UI, Failover |
| **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | Billing | Desktop UI, Model Routing |
| **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | MCP | Failover, Sessions & Memory |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams & Self-hosting | Model Routing, Parallelism |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Failover | Model Routing, Model Routing |
| **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Sessions & Memory | Failover |
| **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Parallelism | Analytics |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | MCP | Failover, Model Routing |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Mobile | Desktop UI |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | MCP | Sessions & Memory |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Sessions & Memory | Model Routing, Model Routing |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Sessions & Memory | Desktop UI, Failover |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Failover, Mobile |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Mobile | Desktop UI, Parallelism |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Failover |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Failover, Sessions & Memory |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Model Routing | Failover, Sessions & Memory |
| **[golutra/golutra](https://github.com/golutra/golutra)** | Sessions & Memory | Desktop UI, Mobile |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Model Routing | Failover |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams & Self-hosting | Parallelism, Sessions & Memory |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Parallelism | Desktop UI, Model Routing |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Parallelism | Desktop UI, Failover |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Parallelism | Billing, Failover |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Parallelism | Desktop UI, Failover |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | Billing | Analytics |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Sessions & Memory | Failover, Model Routing |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Mobile | Failover, MCP |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Failover | Desktop UI, Parallelism |
| **[NerverDevs/nervecenter](https://github.com/NerverDevs/nervecenter)** | Billing | Analytics, Desktop UI |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Failover, Sessions & Memory |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Sessions & Memory | MCP, Model Routing |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | MCP | Desktop UI, Failover |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | MCP | Desktop UI, Sessions & Memory |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Parallelism | Billing |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Parallelism | Desktop UI, Failover |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Sessions & Memory | Desktop UI, Failover |
| **[oracle/mcp](https://github.com/oracle/mcp)** | MCP | Failover, Model Routing |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | MCP | Desktop UI |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | MCP | Failover |
| **[Swival/swival](https://github.com/Swival/swival)** | Model Routing | Model Routing |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Analytics | Billing, Mobile |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Failover | Desktop UI, Model Routing |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Sessions & Memory | Failover, Model Routing |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Desktop UI, MCP |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Parallelism | Desktop UI, Failover |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP | Failover, Model Routing |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Sessions & Memory | Failover, MCP |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Teams & Self-hosting | MCP, Parallelism |
| **[labsai/EDDI](https://github.com/labsai/EDDI)** | Teams & Self-hosting | MCP, Sessions & Memory |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Billing | Analytics, Sessions & Memory |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams & Self-hosting | Mobile, Parallelism |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Parallelism, Sessions & Memory |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics, Failover |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Failover | Desktop UI, Sessions & Memory |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Mobile | Failover, Parallelism |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Sessions & Memory | Parallelism |
| **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | MCP | Desktop UI |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Desktop UI, Providers |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Model Routing, Parallelism |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Billing | Parallelism, Teams & Self-hosting |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Failover | Analytics, Model Routing |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | Sessions & Memory | Failover |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Failover, Model Routing |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Parallelism | Analytics |
| **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Model Routing | Model Routing |
| **[seanbabalala/SiftGate](https://github.com/seanbabalala/SiftGate)** | Teams & Self-hosting | MCP, Model Routing |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Teams & Self-hosting | Analytics, Billing |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | MCP | Failover |
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Model Routing | Model Routing |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Parallelism | Failover, Model Routing |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Sessions & Memory | Desktop UI, Model Routing |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Teams & Self-hosting | Analytics, Model Routing |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams & Self-hosting | Desktop UI, Sessions & Memory |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Desktop UI, Parallelism |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Parallelism, Sessions & Memory |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Billing | Model Routing, Parallelism |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Sessions & Memory | Failover, Model Routing |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | MCP | Failover, Model Routing |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Teams & Self-hosting | Analytics, MCP |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Parallelism | Billing, Teams & Self-hosting |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Sessions & Memory | Desktop UI |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | MCP | Desktop UI |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Billing | Analytics, Failover |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Failover | Desktop UI, Model Routing |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Model Routing |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | Billing | MCP |
| **[IBM/mcp](https://github.com/IBM/mcp)** | MCP | Desktop UI, Failover |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Failover |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.27x the stars (41,905 vs 157,384) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 63.78x the stars (20,537 vs 322) | 🤖 auto (high) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 22.90x the stars (311,057 vs 13,586) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.90x the stars (20,537 vs 2,598) | 🤖 auto (high) |
| **[GizClaw/flowcraft](https://github.com/gizclaw/flowcraft)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 4.24x the stars (1,738 vs 410) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.89x the stars (34,519 vs 384) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 44.58x the stars (41,905 vs 940) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 152.18x the stars (50,372 vs 331) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.72x the stars (34,519 vs 940) | 🤖 auto (high) |
| **[Xpropel/Pi-Remote](https://github.com/xpropel/pi-remote)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 8.93x the stars (2,999 vs 336) | 🤖 auto (high) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 141.49x the stars (50,372 vs 356) | 🤖 auto (high) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.79x the stars (34,519 vs 353) | 🤖 auto (high) |
| **[caveman-ai/caveman-code](https://github.com/caveman-ai/caveman-code)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 26.70x the stars (25,629 vs 960) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 102.00x the stars (30,601 vs 300) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.58x the stars (142,710 vs 4,993) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.25x the stars (50,372 vs 3,801) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 9.73x the stars (12,522 vs 1,287) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.44x the stars (12,522 vs 2,300) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.41x the stars (50,372 vs 372) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.33x the stars (12,522 vs 427) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 50.45x the stars (25,629 vs 508) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | 16.53x the stars (8,132 vs 492) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.95x the stars (50,372 vs 323) | 🤖 auto (high) |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 21.70x the stars (12,522 vs 577) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 492.96x the stars (311,057 vs 631) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 160.27x the stars (157,384 vs 982) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 55.47x the stars (25,629 vs 462) | 🤖 auto (high) |
| **[skyelan1999/aide](https://github.com/skyelan1999/aide)** | **[HKUDS/DeepTutor](https://github.com/hkuds/deeptutor)** | 207.59x the stars (63,106 vs 304) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 101.65x the stars (142,710 vs 1,404) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.25x the stars (12,522 vs 2,945) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 2.96x the stars (1,738 vs 587) | 🤖 auto (high) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 6.19x the stars (2,972 vs 480) | 🤖 auto (medium) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.16x the stars (30,601 vs 1,894) | 🤖 auto (medium) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.75x the stars (1,525 vs 554) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 22.67x the stars (11,360 vs 501) | 🤖 auto (medium) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 35.85x the stars (21,579 vs 602) | 🤖 auto (medium) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[HKUDS/DeepTutor](https://github.com/hkuds/deeptutor)** | 26.80x the stars (63,106 vs 2,355) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.64x the stars (25,629 vs 5,519) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.55x the stars (1,525 vs 429) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 72.37x the stars (50,372 vs 696) | 🤖 auto (medium) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.78x the stars (1,525 vs 549) | 🤖 auto (medium) |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 106.02x the stars (117,254 vs 1,106) | 🤖 auto (medium) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 21.94x the stars (34,519 vs 1,573) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | 2.10x the stars (1,831 vs 873) | 🤖 auto (medium) |
| **[Leonxlnx/earshot](https://github.com/leonxlnx/earshot)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 1.94x the stars (11,360 vs 5,862) | 🤖 auto (medium) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.22x the stars (683 vs 560) | 🤖 auto (medium) |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 3.32x the stars (28,021 vs 8,431) | 🤖 auto (medium) |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/rabiroute)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.38x the stars (683 vs 494) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,113 vs 524) | 🤖 auto (medium) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (50,372 vs 28,339) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | failover | 28.3k | 🔻 Superseded | 1.78x the stars (50,372 vs 28,339) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | teams-self-hosting | 13.6k | 🔻 Superseded | 22.90x the stars (311,057 vs 13,586) |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | mobile | 8.4k | 🔻 Superseded | 3.32x the stars (28,021 vs 8,431) |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | mcp | 5.9k | 🔻 Superseded | 1.94x the stars (11,360 vs 5,862) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.5k | 🔻 Superseded | 4.64x the stars (25,629 vs 5,519) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | parallelism | 5k | 🔻 Superseded | 28.58x the stars (142,710 vs 4,993) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | failover | 3.8k | 🔻 Superseded | 13.25x the stars (50,372 vs 3,801) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams-self-hosting | 2.9k | 🔻 Superseded | 4.25x the stars (12,522 vs 2,945) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.6k | 🔻 Superseded | 7.90x the stars (20,537 vs 2,598) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams-self-hosting | 2.4k | 🔻 Superseded | 26.80x the stars (63,106 vs 2,355) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams-self-hosting | 2.3k | 🔻 Superseded | 5.44x the stars (12,522 vs 2,300) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | teams-self-hosting | 1.9k | 🔻 Superseded | 16.16x the stars (30,601 vs 1,894) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | parallelism | 1.6k | 🔻 Superseded | 21.94x the stars (34,519 vs 1,573) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | parallelism | 1.4k | 🔻 Superseded | 101.65x the stars (142,710 vs 1,404) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | teams-self-hosting | 1.3k | 🔻 Superseded | 9.73x the stars (12,522 vs 1,287) |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | mobile | 1.1k | 🔻 Superseded | 106.02x the stars (117,254 vs 1,106) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 982 | 🔻 Superseded | 160.27x the stars (157,384 vs 982) |
| **[caveman-ai/caveman-code](https://github.com/caveman-ai/caveman-code)** | mobile | 960 | 🔻 Superseded | 26.70x the stars (25,629 vs 960) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 940 | 🔻 Superseded | 44.58x the stars (41,905 vs 940) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism | 940 | 🔻 Superseded | 36.72x the stars (34,519 vs 940) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | sessions-memory | 873 | 🔻 Superseded | 2.10x the stars (1,831 vs 873) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | failover | 696 | 🔻 Superseded | 72.37x the stars (50,372 vs 696) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | teams-self-hosting | 631 | 🔻 Superseded | 492.96x the stars (311,057 vs 631) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | sessions-memory | 602 | 🔻 Superseded | 35.85x the stars (21,579 vs 602) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism | 587 | 🔻 Superseded | 2.96x the stars (1,738 vs 587) |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | teams-self-hosting | 577 | 🔻 Superseded | 21.70x the stars (12,522 vs 577) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile | 560 | 🔻 Superseded | 1.22x the stars (683 vs 560) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | sessions-memory | 554 | 🔻 Superseded | 2.75x the stars (1,525 vs 554) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | sessions-memory | 549 | 🔻 Superseded | 2.78x the stars (1,525 vs 549) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | failover | 524 | 🔻 Superseded | 2.12x the stars (1,113 vs 524) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 508 | 🔻 Superseded | 50.45x the stars (25,629 vs 508) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp | 501 | 🔻 Superseded | 22.67x the stars (11,360 vs 501) |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | mobile | 494 | 🔻 Superseded | 1.38x the stars (683 vs 494) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions-memory | 492 | 🔻 Superseded | 16.53x the stars (8,132 vs 492) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | parallelism | 480 | 🔻 Superseded | 6.19x the stars (2,972 vs 480) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 462 | 🔻 Superseded | 55.47x the stars (25,629 vs 462) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | sessions-memory | 429 | 🔻 Superseded | 3.55x the stars (1,525 vs 429) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams-self-hosting | 427 | 🔻 Superseded | 29.33x the stars (12,522 vs 427) |
| **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | parallelism | 410 | 🔻 Superseded | 4.24x the stars (1,738 vs 410) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism | 384 | 🔻 Superseded | 89.89x the stars (34,519 vs 384) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | failover | 372 | 🔻 Superseded | 135.41x the stars (50,372 vs 372) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | failover | 356 | 🔻 Superseded | 141.49x the stars (50,372 vs 356) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | parallelism | 353 | 🔻 Superseded | 97.79x the stars (34,519 vs 353) |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | parallelism | 336 | 🔻 Superseded | 8.93x the stars (2,999 vs 336) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | failover | 331 | 🔻 Superseded | 152.18x the stars (50,372 vs 331) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | failover | 323 | 🔻 Superseded | 155.95x the stars (50,372 vs 323) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 322 | 🔻 Superseded | 63.78x the stars (20,537 vs 322) |
| **[skyelan1999/aide](https://github.com/skyelan1999/aide)** | teams-self-hosting | 304 | 🔻 Superseded | 207.59x the stars (63,106 vs 304) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams-self-hosting | 300 | 🔻 Superseded | 102.00x the stars (30,601 vs 300) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-26 13:57 UTC. 228 live tools · 123 candidates rejected by the quality gates.</sub>
