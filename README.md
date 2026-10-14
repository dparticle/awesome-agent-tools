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

**222 tools** across **14 categories** · **51 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-14 09:34 UTC**

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

- [Skills](#skills) — 38 tools
- [Self-hosting & Security](#self-hosting-security) — 25 tools
- [Voice & Remote Control](#voice-remote-control) — 23 tools
- [Teams](#teams) — 22 tools
- [Agent Runtime & Desktop UI](#agent-runtime-desktop-ui) — 17 tools
- [Analytics](#analytics) — 20 tools
- [Sharing](#sharing) — 15 tools
- [Model Routing](#model-routing) — 10 tools
- [Providers](#providers) — 11 tools
- [Desktop UI](#desktop-ui) — 11 tools
- [Mobile](#mobile) — 9 tools
- [Providers](#providers) — 8 tools
- [Analytics](#analytics) — 7 tools
- [Sessions](#sessions) — 6 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Skills

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 150.7k 🚀 +185/d | **90** |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | English \| 简体中文 \| 日本語 \| 한국어 \| Русский | 🟡 Some setup | — | — | 47.1k 🚀 +456/d | **89** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Taste Skill is a set of Agent Skills that make coding agents design websites instead of assembling the average landing page. | 🟢 Easy | — | — | 95.8k (+406/d) | **88** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟡 Some setup | — | — | 163.1k 🚀 +793/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template | 🟢 Easy | — | — | 11.8k 🚀 +175/d | **83** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 8.9k 🚀 +1774/d | **82** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 11.1k 🚀 +72/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.8k 🚀 +25/d | **69** |
| ✅ **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 3.6k 🚀 +64/d | **68** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 27k 🚀 +28/d | **68** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 3.4k 🚀 +65/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 4.5k 🚀 +50/d | **65** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.5k 🚀 +17/d | **63** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 3.6k 🚀 +54/d | **62** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.1k 🚀 +21/d | **59** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6k 🚀 +22/d | **59** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.7k | **59** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 850 | **58** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.6k 🚀 +5/d | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1k | **57** |
| 🔹 **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | the current dotnet-skills CLI remains skill-first; repo-owned agents can evolve and ship on their own track. | 🟢 Easy · OOTB | ✅ | — | 486 | **57** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | Built for graduate students, PhDs, postdocs, research support staff, and agent/harness builders who need inspectable research workflows rather than a black box. | 🟢 Easy | — | — | 383 🚀 +15/d | **57** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.8k | **55** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **54** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 341 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 300 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.3k 🚀 +8/d | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 895 | **51** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. | 🟢 Turnkey | — | ✅ | 499 | **51** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [garrytan/gstack](https://github.com/garrytan/gstack), [affaan-m/ECC](https://github.com/affaan-m/ECC), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) *(+31 more)*

*…and 8 more in [the full index](data/index.json).*

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

- Stars: **150,730** (+185.4/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-14
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

- Stars: **47,061** (+455.6/day over 5d)
- Health score: **89/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

> Taste Skill is a set of Agent Skills that make coding agents design websites instead of assembling the average landing page.

**Core problems it solves**

- **Skills & plugins** — */plugin update upgrades it later. Codex plugin Start a new Codex session afterwards so the skills are loaded. From a clone, linked instead of copied…*
- **Agent runtime** — *ts for creative interfaces*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add https://github.com/Leonxlnx/taste-skill`
- Platforms mentioned: iOS, Android, Web
- Easy. install via npx one-liner; configure API key configuration, server/reverse-proxy setup; no-code positioning

**Facts**

- Stars: **95,817** (~406.0/day lifetime average)
- Health score: **88/100**
- Documentation score: **41/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-13
- Works with: Claude Code, Codex

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

- Stars: **163,075** (+792.6/day over 5d)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-13
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)

> AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template

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

- Stars: **11,841** (+174.8/day over 5d)
- Health score: **83/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-13
- Works with: Claude Code, Codex

</details>

## Self-hosting & Security

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 278.8k 🚀 +638/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 18.2k 🚀 +744/d | **88** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 5.3k 🚀 +75/d | **77** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 14.2k 🚀 +83/d | **76** |
| ✅ **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k 🚀 +91/d | **75** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.7k 🚀 +11/d | **68** |
| ✅ **[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)** | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. | 🟢 Turnkey · OOTB | ✅ | — | 2.5k 🚀 +48/d | **67** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 本地优先的 AI 工作台：写代码、做文档、和 Agent 一起推进事情。 模型随你换。 DeepSeek、Kimi、GLM、Qwen、Ollama 等预设，也可自定义 Provider。 | 🟢 Easy | — | ✅ | 6.3k (+44/d) | **66** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **61** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.1k 🚀 +17/d | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.7k 🚀 +8/d | **57** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.7k 🚀 +6/d | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 460 | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 383 | **54** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Interop — the MCP 2026-07-28 client, an MCP server, and A2A in both directions. Models — realtime voice on OpenAI Realtime and Gemini Live, provider batch requests, model profiles, a stable request prefix for Claude 5.x… | 🟢 Easy · OOTB | ✅ | — | 682 (+5/d) | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 337 | **52** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 446 | **51** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | Scope Recall v3 is a bounded local memory core with SQLite as the authority and rebuildable vector companions. | 🟢 Easy | — | — | 318 | **49** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | The self-hosted AI backend for private data and tool-using agents. | 🟡 Some setup | — | — | 354 | **48** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | This repository is essentially an LLM chat desktop application based on MCP. Windows: The MCP SDK includes a workaround specifically for Windows systems, as documented in ISSUE 101. | 🟢 Easy | — | ✅ | 1.2k | **47** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | PAXM carries decisions, conventions, and working context into later Codex, Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP sessions. | 🟡 Some setup | — | — | 285 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 413 | **45** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 542 | **40** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [getpaseo/paseo](https://github.com/getpaseo/paseo), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [topoteretes/cognee](https://github.com/topoteretes/cognee), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [aipoch/open-science](https://github.com/aipoch/open-science), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) *(+15 more)*

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

- Stars: **278,839** (+638.4/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-12
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

- Stars: **18,177** (+743.6/day over 5d)
- Health score: **88/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-14

#### [superdesigndev/treg](https://github.com/superdesigndev/treg)

> OpenRouter, but for agent tools instead of models.

**Core problems it solves**

- **Automatic failover** — *(secrets won't survive a restart)*
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

- Stars: **5,277** (+75.4/day over 5d)
- Health score: **77/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-14
- Works with: Claude Code

#### [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)

> Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota.

**Core problems it solves**

- **Multi-agent orchestration** — *veloper mode and MCP apps.*
- **API gateway / proxy** — *urrent Codex task through the official*
- **MCP support** — *thout spending your Work or Codex quota.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source); configure environment variables, API key configuration

**Facts**

- Stars: **14,214** (+82.8/day over 5d)
- Health score: **76/100**
- Documentation score: **45/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Codex

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

- Stars: **8,461** (~91.0/day lifetime average)
- Health score: **75/100**
- Documentation score: **28/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-14
- Works with: Claude Code, Codex

</details>

## Voice & Remote Control

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 92k 🚀 +743/d | **92** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. | 🟡 Some setup | — | — | 136.4k 🚀 +133/d | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 101.8k 🚀 +554/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 20.8k 🚀 +123/d | **86** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 5.2k 🚀 +161/d | **84** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 4.8k 🚀 +77/d | **76** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 83.8k 🚀 +54/d | **76** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.5k 🚀 +23/d | **72** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 4.8k 🚀 +47/d | **71** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 7.8k 🚀 +44/d | **69** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 8.7k 🚀 +27/d | **67** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 10.8k 🚀 +20/d | **66** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 15k 🚀 +15/d | **65** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.7k 🚀 +7/d | **64** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.3k 🚀 +6/d | **61** |
| 🔹 **[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)** | An open-source desktop AI agent workspace for work, design, and coding. Unified tool store for local MCP servers, remote MCP servers, CLI tools, and API connectors | 🔴 Involved | — | — | 2.5k 🚀 +30/d | **60** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. | 🟡 Some setup | — | — | 1.1k 🚀 +7/d | **57** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 776 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 311 | **55** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 305 | **54** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **51** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 320 | **47** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [slopus/happy](https://github.com/slopus/happy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **91,978** (+742.8/day over 5d)
- Health score: **92/100**
- Documentation score: **51/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

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

- Stars: **136,353** (+133.4/day over 5d)
- Health score: **90/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
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

- Stars: **101,804** (+554.0/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
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

- Stars: **20,837** (+122.6/day over 5d)
- Health score: **86/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

#### [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)

> A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions.

**Core problems it solves**

- **Automatic failover** — *e permission requests show up with Allow / Deny / Always; AskUserQuestion prompts show the choices right in the notch (single or multi-select, up to…*
- **Remote control** — *hooting and build-it-yourself: docs/IPHONE.md.*
- **Mobile access** — *your macOS Keychain, Windows Credential Manager or Linux Secret Service (GNOME Keyring, KWallet).*
- **Model / provider routing** — *open the exact terminal window of a session (macOS).*
- **Agent runtime**
- **Security & isolation** — *See what Claude is editing, live in the notch: each file modification shows the file name and +N −M counts in the ticker, tap to read the full diff*
- **GUI / desktop app** — *Coucou on the iPhone, allow notifications, and start a Claude Code session on the Mac.*
- **Notifications** — *your iPhone's Lock Screen and Dynamic Island with the agent's state, then comes back to the notch when you unlock.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install xcodegen`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, database dependency; one-click setup

**Facts**

- Stars: **5,152** (+161.4/day over 5d)
- Health score: **84/100**
- Documentation score: **62/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Teams

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 160k 🚀 +311/d | **98** |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 54.9k (+305/d) | **90** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 9.3k 🚀 +221/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 9.6k 🚀 +114/d | **84** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 44k 🚀 +83/d | **78** |
| 🏆 **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | You correct it, and by the next session it has forgotten. Entry-point trace — Trace end-to-end what happens when a client creates a record via the REST API, from route handler to database write. | 🟡 Some setup | — | — | 10k 🚀 +98/d | **78** |
| ✅ **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 107.3k 🚀 +14/d | **70** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine | 🟢 Easy | — | — | 29.4k 🚀 +30/d | **70** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Website: aimemory.sh | 🟡 Some setup | — | — | 9.2k 🚀 +33/d | **65** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k 🚀 +8/d | **62** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 2.7k 🚀 +13/d | **60** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4k 🚀 +6/d | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 408 | **54** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.3k 🚀 +24/d | **52** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | The structured skill framework for Claude Code: 131 professional skills for deployment, security, databases, content, marketing, and more. | 🟢 Easy | — | — | 426 | **52** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 404 | **51** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **50** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 792 | **50** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 301 | **49** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.1k | **48** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 424 | **46** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [decolua/9router](https://github.com/decolua/9router), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [spinabot/brigade](https://github.com/spinabot/brigade), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [cordum-io/cordum](https://github.com/cordum-io/cordum), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

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

- Stars: **159,974** (+310.8/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-13
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

- Stars: **54,852** (~304.7/day lifetime average)
- Health score: **90/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-10-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [TencentCloud/Octop](https://github.com/TencentCloud/Octop)

> Octop is an open-source, self-hosted AI assistant.

**Core problems it solves**

- **Mobile access** — *Linux alongside the web dashboard and IM channels.*
- **Multi-agent orchestration** — *A smarter, self-hosted AI assistant — multi-user, multi-agent.*
- **Parallel execution**
- **Workspace isolation** — *dows scripts\install.bat or install.ps1*
- **Model / provider routing** — *ild / quality** hatchling · ruff · mypy · pytest*
- **API gateway / proxy** — *ays back up first (octop backup) before a cross-version upgrade.*
- **Billing & metering** — *Docker Any docker/docker-compose.yml*
- **Memory & context** — *e notes, and manage your schedule; memory persists with the workspace.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs docker run, make build; configure config.json/yaml/toml, OAuth login flow; one-click setup

**Facts**

- Stars: **9,260** (+220.8/day over 5d)
- Health score: **87/100**
- Documentation score: **78/100**
- License: MIT
- Language: Python
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode

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

- Stars: **9,639** (+114.2/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-14
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

- Stars: **43,974** (+83.2/day over 5d)
- Health score: **78/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

</details>

## Agent Runtime & Desktop UI

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.4k 🚀 +18/d | **69** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.2k 🚀 +29/d | **69** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | 📣 2026-09-30 — Raven's technical report is #1 Paper of the day on Hugging Face. | 🟢 Turnkey | — | — | 5.4k 🚀 +21/d | **67** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. | 🟢 Turnkey · OOTB | ✅ | — | 3.4k 🚀 +26/d | **67** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 7.9k 🚀 +34/d | **66** |
| 🔹 **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. | 🟢 Turnkey | — | ✅ | 2.1k | **61** |
| 🔹 **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | Editor & IDE integration (ACP). AI-native MCP configuration. | 🟡 Some setup | — | — | 7.9k 🚀 +11/d | **60** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **59** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 539 | **57** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.6k 🚀 +4/d | **56** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. Go beyond code — video, slides, and more — the Commander drives open-source tools like HyperFrames and hands off to CLI agents — the coding agents Cla… | 🟡 Some setup | — | — | 2.2k | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 536 | **56** |
| 🔹 **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | Claude Code, Codex, OpenCode, Grok, Gemini CLI, Antigravity CLI, Pi, Command Code, Hermes Agent, Muse Code, and Oh My Pi run side by side. | 🟢 Turnkey · OOTB | ✅ | — | 594 | **55** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 787 (+6/d) | **53** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Enable your AI agents to read, analyze, and modify Figma designs. Get document information, current selection, styles | 🟢 Turnkey · OOTB | ✅ | — | 671 | **48** |
| 🔹 **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | Uncommitted changes → [r] reopen the agent / [q] keep worktree Only commits → [m] merge into base branch / [q] keep worktree | 🟡 Some setup · OOTB | ✅ | — | 280 | **47** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Run every AI coding agent in its own git worktree, in parallel. The desktop app embeds its server on 127.0.0.1 with a per-launch token; nothing is exposed to the network. | 🟢 Turnkey | — | ✅ | 268 | **47** |

**Also does this:** [garrytan/gstack](https://github.com/garrytan/gstack), [affaan-m/ECC](https://github.com/affaan-m/ECC), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [getpaseo/paseo](https://github.com/getpaseo/paseo), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal), [crshdn/mission-control](https://github.com/crshdn/mission-control) *(+8 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

> Persistent file-based planning for AI coding agents and long-running tasks.

**Core problems it solves**

- **Multi-agent orchestration** — *ull list of everyone who made this project better: CONTRIBUTORS.md.*
- **Parallel execution** — *ry mechanism below is a file on disk plus a hook, so it works the same on hour ten as on turn one.*
- **Workspace isolation**
- **Memory & context**
- **Skills & plugins** — *wired up for you (skill, extension, status bar):*
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

- Stars: **27,443** (+17.6/day over 5d)
- Health score: **69/100**
- Documentation score: **73/100**
- License: MIT
- Language: Python
- Last push: 2026-10-12
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

- Stars: **9,229** (+29.0/day over 5d)
- Health score: **69/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-10-14
- Works with: Claude Code, Codex

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

- Stars: **5,429** (+20.8/day over 5d)
- Health score: **67/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-14
- Works with: Claude Code, Codex

#### [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)

> request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it.

**Core problems it solves**

- **Multi-agent orchestration** — *tched tool calls run concurrently in Hermes,*
- **Parallel execution** — *D (live rows with category, turns, cost, cache), the phase todo above the prompt, parallel shot ×N, full-row diff bands, and managed skins — installe…*
- **Workspace isolation**
- **Model / provider routing**
- **Memory & context** — *s such as reconciling a --full install back to core live in*
- **Agent runtime** — *to follow whichever Opus the*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 13/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/rlaope/oh-my-hermes/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via Homebrew install, curl | sh installer; needs npm install/build; configure sign-in required

**Facts**

- Stars: **3,365** (+26.2/day over 5d)
- Health score: **67/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-14
- Works with: Claude Code, Codex

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

- Stars: **7,886** (+34.4/day over 5d)
- Health score: **66/100**
- Documentation score: **52/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Analytics

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 32.2k 🚀 +82/d | **80** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 7.9k 🚀 +84/d | **72** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.2k 🚀 +16/d | **62** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | "Automation executes. Autonomy reasons." — @NVIDIAAP | 🟢 Easy | — | — | 4.8k 🚀 +10/d | **62** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.5k 🚀 +30/d | **60** |
| 🔹 **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。 | 🟡 Some setup | — | — | 12.6k 🚀 +22/d | **58** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.3k | **56** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 420 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 417 | **54** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 479 🚀 +7/d | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 840 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Intelligent LLM Routing (omega-pro) — Classifies tasks and routes to the optimal model. Secure Profile (omega-pro) — AES-256 encrypted personal data storage with macOS Keychain integration. | 🟡 Some setup | — | — | 224 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 677 | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 487 | **49** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 438 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 246 | **46** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | GRACE means Graph-RAG Anchored Code Engineering: a contract-first AI engineering methodology built around semantic markup, .grace XML artifacts, knowledge-graph navigation, assertions, scopes, and log-driven verificatio… | 🟡 Some setup | — | — | 253 | **44** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 476 | **41** |

**Also does this:** [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [spinabot/brigade](https://github.com/spinabot/brigade), [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp), [felinics/Memoh](https://github.com/felinics/Memoh), [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory), [FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [oleksiijko/pmb](https://github.com/oleksiijko/pmb) *(+8 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **32,247** (+82.0/day over 5d)
- Health score: **80/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Cursor, Cline / Roo

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

- Stars: **7,863** (+83.6/day over 5d)
- Health score: **72/100**
- Documentation score: **42/100**
- License: MIT
- Language: Python
- Last push: 2026-09-20
- Works with: Codex

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
- Platforms mentioned: Windows, Linux, Web
- Easy. install via Homebrew install; configure environment variables, database dependency

**Facts**

- Stars: **7,180** (+15.8/day over 5d)
- Health score: **62/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)

> You use Claude every day.

**Core problems it solves**

- **Quota & usage management** — *ess, dated, or a pointer - so your knowledge base never fills with facts that used to be true.*
- **Automatic failover** — *prefer hermes-4-405b (or Claude) for those.*
- **Multi-agent orchestration** — *de, so this is honest, not a promise of parity): the core commands - /obsidian-save, /obsidian-daily, /obsidian-capture, /obsidian-find, /obsidian-ta…*
- **Model / provider routing** — *how you installed, and the plugin's MCP server already runs under uv run --no-project --with 'mcp " --build.*
- **API gateway / proxy** — *how you installed, and the plugin's MCP server already runs under uv run --no-project --with 'mcp " --build.*
- **Memory & context** — *on, weekly review, vault-health check*
- **Skills & plugins** — *'s GEMINI.md as passive context, but only detects active skills under .agents/skills/, so install this build (not gemini-cli) if you want Antigravity…*
- **Agent runtime** — *Antigravity to surface the commands as skills.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/eugeniughelbur/obsidian-second-brain/main/scripts/quick-install.…`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, curl | sh installer; needs git clone (build from source); configure API key configuration, config file; no-code positioning

**Facts**

- Stars: **4,756** (+10.2/day over 5d)
- Health score: **62/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-10
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)

> A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server.

**Core problems it solves**

- **Automatic failover**
- **Model / provider routing** — *CP host, such as Codex, Claude Code, Cursor, or OpenCode.*
- **API gateway / proxy** — *The current host model reads evidence and writes the entries; AOCI-CODE does not require a second model API*
- **Session persistence**
- **Memory & context** — *isting authoritative assets and require no graph database, vector database, or remote graph service.*
- **Agent runtime** — *AOCI-CODE logo — AI-Oriented Cognition Infrastructure*
- **MCP support** — *AOCI-CODE logo — AI-Oriented Cognition Infrastructure*
- **GUI / desktop app** — *ou only need a direct build, run:*

**Getting it running**

- Setup: 🔴 **Involved** (friction 64/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via download a release binary, native installer / package; needs git clone (build from source), make build; configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **1,536** (+30.0/day over 5d)
- Health score: **60/100**
- Documentation score: **74/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-10-13
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Sharing

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 129.1k 🚀 +160/d | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 12.3k 🚀 +1012/d | **87** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… Grok CLI 凭据不加密：access token/… | 🟢 Easy | — | ✅ | 19k 🚀 +41/d | **72** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 30.8k 🚀 +55/d | **70** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 31 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 17.4k 🚀 +45/d | **68** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 9.5k 🚀 +43/d | **68** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.4k 🚀 +41/d | **61** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 542 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 241 | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 413 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 交代一句话，它自己规划、动手、验收，把 PPT / Word / Excel / 网页落到你硬盘上。 10-13 「本机/内网放行」支持通配符：192.168.1.: 放一整个网段，*.local:8080 放一类主机名 | 🟡 Some setup | — | — | 314 🚀 +7/d | **51** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.6k 🚀 +11/d | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 894 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 241 | **42** |

**Also does this:** [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **129,143** (+160.4/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-14
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *one key that matters in the agent's own config.*
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

- Stars: **12,298** (+1012.2/day over 5d)
- Health score: **87/100**
- Documentation score: **61/100**
- License: MIT
- Language: Go
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

#### [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

> English · Portuguese (BR) · 简体中文

**Core problems it solves**

- **Multi-account switching** — *surf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Quota & usage management** — *目前支持 Antigravity IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，…*
- **Automatic failover** — *aude CLI 与 Claude Desktop Gateway 第三方供应商预设、模型映射，以及从会话 JSONL 汇总真实用量的方向参考：CC Switch*
- **Multi-agent orchestration**
- **Parallel execution** — *ty IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Model / provider routing**
- **Multi-provider aggregation** — *어 · 🇧🇷 Português · 🇷🇺 Русский · 🇹🇷 Türkçe · 🇵🇱 Polski · 🇨🇿 Čeština · 🇸🇦 العربية · 🇻🇳 Tiếng Việt · 🇮🇩 Bahasa Indonesia*
- **API gateway / proxy** — *和 JSON／纯文本返回，model 仅作为兼容字段，实际模型由 backend 决定；字幕时间戳、流式转写及其他音频操作需使用支持相应接口的 API Key 供应商。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 20/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **18,955** (+40.6/day over 5d)
- Health score: **72/100**
- Documentation score: **59/100**
- Language: Rust
- Last push: 2026-10-12
- Works with: Codex, OpenCode, Cursor, Copilot

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

- Stars: **30,775** (+54.6/day over 5d)
- Health score: **70/100**
- Documentation score: **66/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-08
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

- Stars: **17,387** (+44.8/day over 5d)
- Health score: **68/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 101.1k 🚀 +183/d | **95** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 10.1k 🚀 +90/d | **75** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.2k 🚀 +22/d | **64** |
| 🔹 **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens. | 🟢 Easy · OOTB | ✅ | — | 7.5k | **61** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. | 🟡 Some setup | — | — | 11.1k 🚀 +11/d | **59** |
| 🔹 **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | DeepSeek Harness, OpenClaw, Hermes, Claude Code, Codex, Cursor, WorkBuddy, OpenCode, Pi...they all work! | 🟡 Some setup | — | — | 2.1k | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 342 | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. a CI-passed aggregator; single-command releases (`node scripts/release.mjs | 🟡 Some setup | — | — | 701 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 708 | **50** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 Easy | — | — | 367 | **47** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [decolua/9router](https://github.com/decolua/9router), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [yetone/cumora](https://github.com/yetone/cumora), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [schmitech/orbit](https://github.com/schmitech/orbit) *(+1 more)*

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

- Stars: **101,051** (+182.8/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **10,061** (+89.8/day over 5d)
- Health score: **75/100**
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

- Stars: **17,151** (+22.0/day over 5d)
- Health score: **64/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **7,513** (+2.0/day over 5d)
- Health score: **61/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [openai/codex-security](https://github.com/openai/codex-security)

> @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code.

**Core problems it solves**

- **Model / provider routing**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @openai/codex-security`
- Platforms mentioned: Web
- Some setup. install via npx one-liner; needs npm install/build; configure API key configuration, sign-in required

**Facts**

- Stars: **11,098** (+10.8/day over 5d)
- Health score: **59/100**
- Documentation score: **41/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Codex

</details>

## Providers

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 144.1k 🚀 +459/d | **93** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 4.8k 🚀 +99/d | **74** |
| ✅ **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.3k 🚀 +66/d | **72** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.4k 🚀 +14/d | **67** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi is a fast, self-contained terminal AI coding agent. | 🟢 Easy | — | — | 3.3k 🚀 +47/d | **66** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.6k 🚀 +16/d | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 282 | **53** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 430 | **52** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 557 | **49** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 516 | **43** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 313 | **43** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory), [nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)

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

- Stars: **144,070** (+458.6/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **4,750** (+98.6/day over 5d)
- Health score: **74/100**
- Documentation score: **33/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
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

- Stars: **5,306** (+66.2/day over 5d)
- Health score: **72/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Copilot

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

- Stars: **27,365** (+13.8/day over 5d)
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

- Stars: **3,341** (~47.1/day lifetime average)
- Health score: **66/100**
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
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 213.4k 🚀 +212/d | **90** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 29.4k 🚀 +528/d | **84** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 8.8k 🚀 +68/d | **73** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15k 🚀 +13/d | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.6k 🚀 +8/d | **61** |
| 🔹 **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 Turnkey · OOTB | ✅ | ✅ | 3.2k 🚀 +10/d | **59** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 462 | **56** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). orcarouter: OpenAI-compatible model gateway with namespaced model IDs. | 🔴 Involved | — | — | 1.7k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 744 | **50** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 641 | **38** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [anthropics/claude-code](https://github.com/anthropics/claude-code), [openai/codex](https://github.com/openai/codex), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [aipoch/open-science](https://github.com/aipoch/open-science), [zai-org/ZCode](https://github.com/zai-org/ZCode), [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) *(+35 more)*

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

- Stars: **213,362** (+211.8/day over 5d)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

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

- Stars: **29,408** (+527.6/day over 5d)
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

- Stars: **8,842** (+67.8/day over 5d)
- Health score: **73/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
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

- Stars: **15,002** (+12.6/day over 5d)
- Health score: **64/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-09
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

- Stars: **1,622** (+7.8/day over 5d)
- Health score: **61/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 11.7k 🚀 +91/d | **75** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.4k 🚀 +21/d | **64** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.1k 🚀 +13/d | **63** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 2.8k 🚀 +68/d | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.4k 🚀 +13/d | **55** |
| 🔹 **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 一个适配 Claude Code / Codex 等 Agent 环境的图文卡片技能,用于从文章、文案、截图、产品笔记、字幕、照片或用户视频生成小红书 / Rednote 图文组图、Live Photo 动态卡与公众号 21:9 + 1:1 封面对。 | 🟢 Easy | — | — | 7.5k 🚀 +16/d | **54** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 284 | **53** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Official agent skills/plugins for Power Platform development by Microsoft. Launch GitHub Copilot CLI or Claude Code with the plugin path: | 🟡 Some setup | — | — | 1k 🚀 +5/d | **51** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Control your Pi coding agent from your phone. | 🟢 Easy | — | — | 443 | **50** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [stablyai/orca](https://github.com/stablyai/orca), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [loopx-project/loopx](https://github.com/loopx-project/loopx), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go), [yetone/cumora](https://github.com/yetone/cumora)

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

- Stars: **11,662** (+90.8/day over 5d)
- Health score: **75/100**
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

- Stars: **4,374** (+21.0/day over 5d)
- Health score: **64/100**
- Documentation score: **61/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-23
- Works with: Claude Code, Codex, Cursor, Copilot, Cline / Roo

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

- Stars: **24,133** (+12.8/day over 5d)
- Health score: **63/100**
- Documentation score: **29/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex
- *Why it is seeded: Drive Claude Code / Codex from a phone with end-to-end encryption.*

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

- Stars: **2,837** (+68.2/day over 5d)
- Health score: **62/100**
- Documentation score: **27/100**
- License: MIT
- Last push: 2026-09-06
- Works with: Claude Code, Codex, Cursor

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

- Stars: **3,426** (+13.0/day over 5d)
- Health score: **55/100**
- Documentation score: **42/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-18

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 3.6k 🚀 +55/d | **74** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.2k 🚀 +18/d | **58** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁移。 工作台完整保留：任务看板、Git、文件交付、模型协作、桌宠、15 套皮肤、SSH 与远程访问继续提供；恢复 4.4.0 品牌图标。 | 🟢 Turnkey · OOTB | ✅ | — | 812 🚀 +5/d | **56** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 985 | **55** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 726 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 435 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 587 | **46** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [loopx-project/loopx](https://github.com/loopx-project/loopx), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **3,599** (+54.8/day over 5d)
- Health score: **74/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-12
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

- Stars: **4,206** (+17.6/day over 5d)
- Health score: **58/100**
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

- Stars: **812** (+5.2/day over 5d)
- Health score: **56/100**
- Documentation score: **43/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex

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

- Stars: **985** (+0.6/day over 5d)
- Health score: **55/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-09
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

- Stars: **726** (+0.6/day over 5d)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-12
- Works with: Claude Code, Cursor

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 Some setup | — | — | 6.3k 🚀 +16/d | **65** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.1k | **53** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 542 🚀 +6/d | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **52** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. Cline / Roo Code / Zoo Code / Kilo Code (VS Code extension + CLI) | 🟢 Turnkey · OOTB | ✅ | — | 223 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons,… | 🟡 Some setup | — | — | 729 | **43** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes), [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [tigicion/dao-code](https://github.com/tigicion/dao-code), [cwinvestments/memstack](https://github.com/cwinvestments/memstack), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth) *(+4 more)*

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

- Stars: **6,295** (+15.8/day over 5d)
- Health score: **65/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-14
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

- Stars: **2,148** (+0.2/day over 6d)
- Health score: **53/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-16
- Works with: Droid

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

- Stars: **542** (+5.6/day over 5d)
- Health score: **53/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-09
- Works with: Claude Code

#### [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)

> Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store.

**Core problems it solves**

- **Remote control** — *+ Cursor together, skills add cross-agent*
- **Multi-agent orchestration** — *ences/system-one-classifiers.md.*
- **Parallel execution** — *search / /list Search and list stored learnings*
- **Workspace isolation** — *hase Research → Plan → Implement → Review*
- **Model / provider routing**
- **Usage analytics** — *on disk + FTS5 shadow index, queryable from any session, optionally grown by an auto-research loop.*
- **Memory & context**
- **Skills & plugins**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add rohitg00/pro-workflow`
- Platforms mentioned: Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure config.json/yaml/toml, database dependency

**Facts**

- Stars: **2,916** (+1.6/day over 5d)
- Health score: **52/100**
- Documentation score: **46/100**
- Language: JavaScript
- Last push: 2026-09-29
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **5,883** (~5.1/day lifetime average)
- Health score: **51/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

</details>

## Sessions

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🔹 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | This one is invisible to anti-bots. | 🟢 Turnkey · OOTB | ✅ | — | 2.8k 🚀 +15/d | **60** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.8k 🚀 +11/d | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.1k | **55** |
| 🔹 **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | Park, J.S. et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. UIST 2023. doi:10.1145/3586183.3606763 Liu, N.F. et al. (2024). Lost in the Middle: How Language Models Use Long Contexts. TACL 12, 1… | 🟡 Some setup | — | — | 224 | **53** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew brings task execution, human approvals, persistent memory, and scheduled work into one desktop application. | 🟡 Some setup | — | ✅ | 251 | **49** |
| 👀 **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | Meet Tara, your 24/7 personal assistant powered by Claude Code and OpenAI Codex. | 🔴 Involved | — | — | 516 | **38** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [anomalyco/opencode](https://github.com/anomalyco/opencode), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [zai-org/ZCode](https://github.com/zai-org/ZCode), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [slopus/happy](https://github.com/slopus/happy), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude) *(+15 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **2,769** (+14.8/day over 5d)
- Health score: **60/100**
- Documentation score: **33/100**
- License: MIT
- Language: Python
- Last push: 2026-10-13
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

- Stars: **1,755** (+10.8/day over 5d)
- Health score: **56/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-14
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

- Stars: **1,073** (+3.8/day over 5d)
- Health score: **55/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-11
- Works with: Claude Code, Codex, Cursor

#### [jmagly/aiwg](https://github.com/jmagly/aiwg)

> source of truth; network connecting AI tools" width="1000">

**Core problems it solves**

- **Multi-agent orchestration** — *artifact and check that it is still applicable, but the team has a concrete record to work from rather*
- **Parallel execution** — *skills, rules, and templates reference one another, while .aiwg/*
- **Model / provider routing** — *pace needs them, and verify the connection.*
- **Session persistence** — *results to guide the next attempt.*
- **Memory & context** — *- Anthropic Applied AI Team (2026).*
- **Skills & plugins** — *tant interprets your intent, searches AIWG's capability graphs, reads the matching assets, and follows their*
- **Agent runtime** — *vider deployment — Google Antigravity CLI, Claude Code, OpenAI Codex, GitHub Copilot, Cursor, DeepSeek*
- **MCP support** — *text decomposition for tasks whose source material needs to be divided into smaller working sets.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm i -g aiwg`
- Platforms mentioned: macOS, Linux, Web
- Some setup. install via npx one-liner, global npm install; needs npm install/build; configure sign-in required, database dependency

**Facts**

- Stars: **224** (~0.5/day lifetime average)
- Health score: **53/100**
- Documentation score: **76/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

#### [YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)

> AgentCrew brings task execution, human approvals, persistent memory, and scheduled work into one desktop application.

**Core problems it solves**

- **Session persistence** — *follow the steps, tool calls, and results as the work progresses.*
- **Memory & context** — *onses, and queue or cancel instructions.*
- **MCP support** — *ecords remain available for inspection.*
- **Security & isolation** — *, follow streamed responses, and queue or cancel instructions.*
- **GUI / desktop app** — *ompleted work and its execution record.*
- **Notifications** — *pted work and inspect recorded steps, tool results, approvals, and audit events in the Run Center.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 39/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS
- Some setup. install via native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, config file; GUI application

**Facts**

- Stars: **251** (~0.9/day lifetime average)
- Health score: **49/100**
- Documentation score: **45/100**
- Language: Python
- Last push: 2026-10-12
- Works with: OpenCode

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Teams | Mobile, Voice & Remote Control |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Model Routing | Desktop UI, Sessions |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Providers, Teams |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Voice & Remote Control | Analytics, Mobile |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Sessions, Skills |
| **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Skills | Desktop UI |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Voice & Remote Control | Agent Runtime & Desktop UI, Skills |
| **[openai/codex](https://github.com/openai/codex)** | Sharing | Desktop UI |
| **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | Skills | Desktop UI |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Self-hosting & Security | Agent Runtime & Desktop UI, Skills |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Voice & Remote Control | Self-hosting & Security, Sessions |
| **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Skills | Desktop UI |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Model Routing |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Agent Runtime & Desktop UI, Desktop UI |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Voice & Remote Control | Agent Runtime & Desktop UI, Self-hosting & Security |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Sessions, Skills |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Voice & Remote Control | Desktop UI, Mobile |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Teams | Desktop UI, Self-hosting & Security |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | Analytics | Self-hosting & Security |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Teams | Model Routing, Providers |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Teams | Model Routing, Skills |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Voice & Remote Control | Mobile, Self-hosting & Security |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Voice & Remote Control | Agent Runtime & Desktop UI, Providers |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Desktop UI, Model Routing |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Voice & Remote Control | Agent Runtime & Desktop UI, Skills |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Providers, Teams |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Providers | Analytics, Skills |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Voice & Remote Control | Desktop UI, Self-hosting & Security |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Teams | Analytics, Providers |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Model Routing, Teams |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams | Self-hosting & Security, Skills |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Voice & Remote Control | Desktop UI, Sessions |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Agent Runtime & Desktop UI | Analytics, Skills |
| **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | Agent Runtime & Desktop UI | Analytics |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Model Routing, Sessions |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Voice & Remote Control | Analytics, Sessions |
| **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Agent Runtime & Desktop UI | Model Routing, Skills |
| **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | Skills | Desktop UI |
| **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Agent Runtime & Desktop UI | Analytics, Skills |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Voice & Remote Control | Model Routing, Teams |
| **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Agent Runtime & Desktop UI | Analytics |
| **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | Self-hosting & Security | Desktop UI |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | Providers | Self-hosting & Security |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Mobile, Providers |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Voice & Remote Control | Providers, Self-hosting & Security |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Desktop UI, Self-hosting & Security |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | Providers, Teams |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Voice & Remote Control | Analytics, Sessions |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Desktop UI, Skills |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Sessions, Voice & Remote Control |
| **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Teams | Desktop UI, Skills |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Analytics | Self-hosting & Security, Skills |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Voice & Remote Control | Analytics, Teams |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI, Skills |
| **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Agent Runtime & Desktop UI | Desktop UI, Skills |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | Agent Runtime & Desktop UI | Desktop UI, Skills |
| **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | Sessions | Analytics |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Teams | Mobile, Self-hosting & Security |
| **[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)** | Voice & Remote Control | Self-hosting & Security, Skills |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Analytics | Providers, Sessions |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Skills | Desktop UI |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Skills | Desktop UI |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Agent Runtime & Desktop UI | Analytics, Skills |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Sessions |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Self-hosting & Security | Mobile |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Skills | Agent Runtime & Desktop UI, Desktop UI |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Skills | Desktop UI, Sessions |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Self-hosting & Security | Analytics, Sessions |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Voice & Remote Control | Agent Runtime & Desktop UI, Analytics |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Skills | Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Agent Runtime & Desktop UI | Sessions, Voice & Remote Control |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | Skills | Desktop UI |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | Skills | Desktop UI, Sessions |
| **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Agent Runtime & Desktop UI | Desktop UI, Skills |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | Model Routing | Analytics, Desktop UI |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Analytics | Desktop UI, Skills |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Skills |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Agent Runtime & Desktop UI | Skills |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Agent Runtime & Desktop UI, Sessions |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Mobile, Model Routing |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Desktop UI | Sessions, Skills |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Self-hosting & Security | Model Routing |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Sessions | Desktop UI, Skills |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Voice & Remote Control | Analytics, Self-hosting & Security |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Voice & Remote Control | Agent Runtime & Desktop UI, Analytics |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Skills | Analytics, Desktop UI |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Self-hosting & Security |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Analytics, Skills |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Analytics | Providers, Self-hosting & Security |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Teams | Analytics, Self-hosting & Security |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | Self-hosting & Security | Desktop UI, Skills |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Voice & Remote Control | Agent Runtime & Desktop UI, Self-hosting & Security |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Agent Runtime & Desktop UI, Self-hosting & Security |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Agent Runtime & Desktop UI | Analytics, Skills |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Analytics | Self-hosting & Security, Teams |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Mobile | Skills, Teams |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Providers | Analytics, Desktop UI |
| **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | Sessions | Analytics, Self-hosting & Security |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Analytics | Agent Runtime & Desktop UI, Skills |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Skills | Desktop UI |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Model Routing | Desktop UI, Skills |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Self-hosting & Security, Teams |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Providers | Analytics |
| **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | Teams | Agent Runtime & Desktop UI, Analytics |
| **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Skills | Desktop UI |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Analytics, Providers |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Voice & Remote Control | Agent Runtime & Desktop UI, Sessions |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Voice & Remote Control | Agent Runtime & Desktop UI, Sessions |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Analytics | Sessions, Skills |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Sharing | Sessions |
| **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | Sharing | Self-hosting & Security, Teams |
| **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Analytics | Sessions, Skills |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Teams | Desktop UI, Skills |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Sessions, Skills |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Analytics | Sessions |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Mobile | Skills, Voice & Remote Control |
| **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | Analytics | Agent Runtime & Desktop UI, Desktop UI |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Providers | Model Routing, Sharing |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Analytics | Providers |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams | Analytics, Voice & Remote Control |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | Sessions | Analytics, Self-hosting & Security |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Teams | Providers, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Agent Runtime & Desktop UI, Skills |
| **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Agent Runtime & Desktop UI | Skills |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Self-hosting & Security | Model Routing |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | Self-hosting & Security | Sessions |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Voice & Remote Control | Agent Runtime & Desktop UI, Analytics |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | Self-hosting & Security | Analytics |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | Agent Runtime & Desktop UI | Analytics, Desktop UI |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Agent Runtime & Desktop UI | Analytics, Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Self-hosting & Security | Sessions |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Skills |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Analytics | Desktop UI, Skills |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Analytics | Agent Runtime & Desktop UI, Desktop UI |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Skills | Desktop UI |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Self-hosting & Security | Skills |
| **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | Analytics | Skills |
| **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | Analytics | Providers |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Providers | Analytics |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Providers | Analytics, Self-hosting & Security |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Skills | Analytics, Desktop UI |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Sharing | Model Routing, Teams |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Analytics | Self-hosting & Security |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | Skills | Desktop UI, Self-hosting & Security |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Sessions, Skills |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | Sessions | Analytics, Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.09x the stars (12,298 vs 144,070) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 57.97x the stars (18,955 vs 327) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 19.71x the stars (10,800 vs 548) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 72.03x the stars (27,443 vs 381) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 876.85x the stars (278,839 vs 318) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 64.80x the stars (278,839 vs 4,303) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.98x the stars (20,837 vs 5,238) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 3.01x the stars (850 vs 282) | 🤖 auto (high) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 217.78x the stars (101,051 vs 464) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.60x the stars (27,443 vs 4,903) | 🤖 auto (high) |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 233.50x the stars (101,804 vs 436) | 🤖 auto (high) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 390.18x the stars (159,974 vs 410) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.31x the stars (9,260 vs 2,147) | 🤖 auto (high) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.92x the stars (13,653 vs 391) | 🤖 auto (high) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 11.16x the stars (4,756 vs 426) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 26.92x the stars (9,260 vs 344) | 🤖 auto (high) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | 3.85x the stars (3,365 vs 873) | 🤖 auto (high) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 161.68x the stars (101,051 vs 625) | 🤖 auto (high) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 75.52x the stars (18,955 vs 251) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 583.85x the stars (159,974 vs 274) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 455.62x the stars (278,839 vs 612) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.42x the stars (144,070 vs 8,774) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 46.38x the stars (278,839 vs 6,012) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[EverMind-AI/Raven](https://github.com/evermind-ai/raven)** | 9.57x the stars (5,429 vs 567) | 🤖 auto (high) |
| **[spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** | **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | 14.82x the stars (5,277 vs 356) | 🤖 auto (high) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 77.95x the stars (278,839 vs 3,577) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 3.43x the stars (4,821 vs 1,404) | 🤖 auto (high) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 6.61x the stars (101,804 vs 15,408) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.38x the stars (9,260 vs 2,743) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 8.68x the stars (4,756 vs 548) | 🤖 auto (medium) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 29.70x the stars (27,443 vs 924) | 🤖 auto (medium) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.85x the stars (850 vs 298) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 747.56x the stars (278,839 vs 373) | 🤖 auto (medium) |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.92x the stars (7,180 vs 724) | 🤖 auto (medium) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 6.99x the stars (47,061 vs 6,736) | 🤖 auto (medium) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 43.14x the stars (278,839 vs 6,464) | 🤖 auto (medium) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 6.03x the stars (2,088 vs 346) | 🤖 auto (medium) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 588.27x the stars (278,839 vs 474) | 🤖 auto (medium) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 52.57x the stars (278,839 vs 5,304) | 🤖 auto (medium) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 7.56x the stars (4,756 vs 629) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.37x the stars (850 vs 358) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 555.46x the stars (278,839 vs 502) | 🤖 auto (medium) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.30x the stars (1,073 vs 467) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 7.62x the stars (2,088 vs 274) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 6.11x the stars (4,756 vs 778) | 🤖 auto (high) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 3.68x the stars (2,088 vs 567) | 🤖 auto (medium) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 20.81x the stars (27,443 vs 1,319) | 🤖 auto (high) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.26x the stars (20,837 vs 4,888) | 🤖 auto (medium) |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 8.96x the stars (2,088 vs 233) | 🤖 auto (high) |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 9.45x the stars (29,404 vs 3,112) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 1.88x the stars (701 vs 373) | 🤖 auto (medium) |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 1.36x the stars (101,051 vs 74,449) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | model-routing | 74.4k | 🔻 Superseded | 1.36x the stars (101,051 vs 74,449) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | voice-remote-control | 15.4k | 🔻 Superseded | 6.61x the stars (101,804 vs 15,408) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | providers | 8.8k | 🔻 Superseded | 16.42x the stars (144,070 vs 8,774) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.7k | 🔻 Superseded | 6.99x the stars (47,061 vs 6,736) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | self-hosting-security | 6.5k | 🔻 Superseded | 43.14x the stars (278,839 vs 6,464) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | self-hosting-security | 6k | 🔻 Superseded | 46.38x the stars (278,839 vs 6,012) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | self-hosting-security | 5.3k | 🔻 Superseded | 52.57x the stars (278,839 vs 5,304) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | voice-remote-control | 5.2k | 🔻 Superseded | 3.98x the stars (20,837 vs 5,238) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | agent-runtime-desktop-ui | 4.9k | 🔻 Superseded | 5.60x the stars (27,443 vs 4,903) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | voice-remote-control | 4.9k | 🔻 Superseded | 4.26x the stars (20,837 vs 4,888) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | self-hosting-security | 4.3k | 🔻 Superseded | 64.80x the stars (278,839 vs 4,303) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | self-hosting-security | 3.6k | 🔻 Superseded | 77.95x the stars (278,839 vs 3,577) |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | teams | 3.1k | 🔻 Superseded | 9.45x the stars (29,404 vs 3,112) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 Superseded | 3.38x the stars (9,260 vs 2,743) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams | 2.1k | 🔻 Superseded | 4.31x the stars (9,260 vs 2,147) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | voice-remote-control | 1.4k | 🔻 Superseded | 3.43x the stars (4,821 vs 1,404) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | agent-runtime-desktop-ui | 1.3k | 🔻 Superseded | 20.81x the stars (27,443 vs 1,319) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | agent-runtime-desktop-ui | 924 | 🔻 Superseded | 29.70x the stars (27,443 vs 924) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | agent-runtime-desktop-ui | 873 | 🔻 Superseded | 3.85x the stars (3,365 vs 873) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | analytics | 778 | 🔻 Superseded | 6.11x the stars (4,756 vs 778) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | analytics | 724 | 🔻 Superseded | 9.92x the stars (7,180 vs 724) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | analytics | 629 | 🔻 Superseded | 7.56x the stars (4,756 vs 629) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 625 | 🔻 Superseded | 161.68x the stars (101,051 vs 625) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | self-hosting-security | 612 | 🔻 Superseded | 455.62x the stars (278,839 vs 612) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | agent-runtime-desktop-ui | 567 | 🔻 Superseded | 9.57x the stars (5,429 vs 567) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | agent-runtime-desktop-ui | 567 | 🔻 Superseded | 3.68x the stars (2,088 vs 567) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | voice-remote-control | 548 | 🔻 Superseded | 19.71x the stars (10,800 vs 548) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | analytics | 548 | 🔻 Superseded | 8.68x the stars (4,756 vs 548) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | self-hosting-security | 502 | 🔻 Superseded | 555.46x the stars (278,839 vs 502) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | self-hosting-security | 474 | 🔻 Superseded | 588.27x the stars (278,839 vs 474) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions | 467 | 🔻 Superseded | 2.30x the stars (1,073 vs 467) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 464 | 🔻 Superseded | 217.78x the stars (101,051 vs 464) |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | voice-remote-control | 436 | 🔻 Superseded | 233.50x the stars (101,804 vs 436) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | analytics | 426 | 🔻 Superseded | 11.16x the stars (4,756 vs 426) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | teams | 410 | 🔻 Superseded | 390.18x the stars (159,974 vs 410) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice-remote-control | 391 | 🔻 Superseded | 34.92x the stars (13,653 vs 391) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | agent-runtime-desktop-ui | 381 | 🔻 Superseded | 72.03x the stars (27,443 vs 381) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | model-routing | 373 | 🔻 Superseded | 1.88x the stars (701 vs 373) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | self-hosting-security | 373 | 🔻 Superseded | 747.56x the stars (278,839 vs 373) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 358 | 🔻 Superseded | 2.37x the stars (850 vs 358) |
| **[spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** | self-hosting-security | 356 | 🔻 Superseded | 14.82x the stars (5,277 vs 356) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | agent-runtime-desktop-ui | 346 | 🔻 Superseded | 6.03x the stars (2,088 vs 346) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 344 | 🔻 Superseded | 26.92x the stars (9,260 vs 344) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 Superseded | 57.97x the stars (18,955 vs 327) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | self-hosting-security | 318 | 🔻 Superseded | 876.85x the stars (278,839 vs 318) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills | 298 | 🔻 Superseded | 2.85x the stars (850 vs 298) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 Superseded | 3.01x the stars (850 vs 282) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | agent-runtime-desktop-ui | 274 | 🔻 Superseded | 7.62x the stars (2,088 vs 274) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 274 | 🔻 Superseded | 583.85x the stars (159,974 vs 274) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | sharing | 251 | 🔻 Superseded | 75.52x the stars (18,955 vs 251) |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | agent-runtime-desktop-ui | 233 | 🔻 Superseded | 8.96x the stars (2,088 vs 233) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-14 09:34 UTC. 222 live tools · 127 candidates rejected by the quality gates.</sub>
