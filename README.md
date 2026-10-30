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

**205 tools** across **12 categories** · **68 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-30 10:55 UTC**

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

- [Desktop UI](#desktop-ui) — 39 tools
- [Memory & MCP](#memory-mcp) — 22 tools
- [Failover](#failover) — 32 tools
- [Teams & Isolation](#teams-isolation) — 18 tools
- [Mobile & Remote Control](#mobile-remote-control) — 18 tools
- [Sharing](#sharing) — 16 tools
- [Teams](#teams) — 11 tools
- [Desktop UI](#desktop-ui) — 12 tools
- [Billing](#billing) — 10 tools
- [Model Routing](#model-routing) — 10 tools
- [Analytics](#analytics) — 9 tools
- [Providers](#providers) — 8 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 2,877+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 48.8k (+169/d) | **92** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 153.9k 🚀 +117/d | **89** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | ✅ | 180.6k 🚀 +973/d | **88** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Taste Skill is an Agent Skill that makes coding agents design websites and app screens instead of assembling the average landing page. | 🟢 Easy | — | — | 105.9k 🚀 +750/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 15k 🚀 +295/d | **84** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 22.8k 🚀 +499/d | **83** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 53.3k 🚀 +1573/d | **82** |
| 🏆 **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 5.7k 🚀 +134/d | **79** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 5.3k 🚀 +157/d | **77** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.1k 🚀 +28/d | **70** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 5.1k 🚀 +75/d | **67** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.3k 🚀 +26/d | **64** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 4.2k 🚀 +44/d | **63** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.7k 🚀 +9/d | **62** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +17/d | **61** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4k 🚀 +24/d | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **56** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 911 🚀 +4/d | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 542 | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 910 | **53** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 767 | **53** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 513 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) External-content sanitizing (leyline) strips invisible | 🟢 Easy | — | — | 343 | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 441 | **52** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 291 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.4k 🚀 +5/d | **51** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [garrytan/gstack](https://github.com/garrytan/gstack), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) *(+30 more)*

*…and 9 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)

> Agentic Awesome Skills is a library of 2,877+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents.

**Core problems it solves**

- **Mobile access** — *digest-pinned 0.1.7 archive byte-identical to commit a8818c3 with self-update disabled before first use (MIT-0).*
- **Multi-agent orchestration** — *ity, and mobile attack surfaces (MIT, docs-only — helper scripts, commands, engine, and research assets not bundled).*
- **Model / provider routing** — *ommerce, travel, jobs, local business, and structured web data workflows.*
- **Usage analytics** — *-focused Claude agent skills (MIT).*
- **Memory & context** — *tomic, interlinked knowledge stores with explicit hygiene, provenance, expiry, and secret-handling boundaries (MIT).*
- **Skills & plugins** — *Agentic Awesome Skills — AI Skills & AAS Core*
- **Agent runtime** — *plete files, and keep an exact skill set you can review and reuse.***
- **MCP support** — *tool contracts, capability coverage, and limits.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via npx one-liner, native installer / package; configure API key configuration, OAuth login flow; GUI application

**Facts**

- Stars: **48,793** (~169.4/day lifetime average)
- Health score: **92/100**
- Documentation score: **82/100**
- License: MIT
- Language: Python
- Last push: 2026-10-29
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **153,913** (+117.2/day over 5d)
- Health score: **89/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-30
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

- Stars: **180,597** (+972.6/day over 5d)
- Health score: **88/100**
- Documentation score: **48/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-29
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

- Stars: **105,920** (+750.2/day over 5d)
- Health score: **86/100**
- Documentation score: **33/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex

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

- Stars: **14,963** (+294.8/day over 5d)
- Health score: **84/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-29
- Works with: Claude Code, Codex

</details>

## Memory & MCP

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 105k 🚀 +230/d | **95** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 293k 🚀 +936/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 21.7k 🚀 +221/d | **88** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 11.3k 🚀 +115/d | **85** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 6.5k 🚀 +94/d | **81** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.3k 🚀 +64/d | **73** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | More native integrations: installable Pi package, OMP and DeepSeek Harness plugins, and improved Cursor workspace attribution. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30k 🚀 +30/d | **71** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.8k 🚀 +8/d | **67** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.7k | **63** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **62** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟢 Easy | — | — | 4.2k 🚀 +8/d | **60** |
| 🔹 **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | English: README.en.md \| 中文: README.md | 🔴 Involved | — | — | 3.3k 🚀 +50/d | **60** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.4k 🚀 +13/d | **60** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k 🚀 +5/d | **59** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 786 | **55** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Easy · OOTB | ✅ | — | 558 🚀 +8/d | **55** |
| 🔹 **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | Try, compare, contribute: First-run reports · Context-compression evaluation note · Contribution guide | 🟢 Turnkey | — | — | 266 | **55** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 557 | **49** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 417 | **45** |

**Also does this:** [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [yetone/cumora](https://github.com/yetone/cumora), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [cordum-io/cordum](https://github.com/cordum-io/cordum), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher) *(+4 more)*

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

- Stars: **104,975** (+229.6/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **293,003** (+936.4/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-30
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

- Stars: **21,656** (+220.8/day over 5d)
- Health score: **88/100**
- Documentation score: **51/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-30

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

- Stars: **11,350** (+115.0/day over 5d)
- Health score: **85/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [superdesigndev/treg](https://github.com/superdesigndev/treg)

> OpenRouter, but for agent tools instead of models.

**Core problems it solves**

- **Automatic failover** — *secrets won't survive a restart)*
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

- Stars: **6,510** (+94.4/day over 5d)
- Health score: **81/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-30
- Works with: Claude Code

</details>

## Failover

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 17.6k 🚀 +445/d | **87** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 4.6k 🚀 +100/d | **84** |
| 🏆 **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 47.8k 🚀 +78/d | **78** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.3k 🚀 +142/d | **76** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 32.9k 🚀 +37/d | **71** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.6k 🚀 +15/d | **67** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 8.9k 🚀 +70/d | **67** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.7k 🚀 +18/d | **63** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance 3,985 archived projects -- full source code snapshots from the game security ecosystem (prefixed ags-) | 🟢 Easy | — | — | 447 🚀 +18/d | **58** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.8k 🚀 +13/d | **57** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 5.1k 🚀 +6/d | **56** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.8k | **55** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Conversations with AI agents reset when context windows close. Agent Action Grammar (AAG): Ultra-compact, deterministic ASCII micro-syntax saving ~78–85% tokens compared to natural language prompt instructions. | 🟡 Some setup | — | — | 845 | **55** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 413 | **55** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 427 | **54** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 885 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 442 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 913 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 673 | **51** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 499 | **51** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 288 | **51** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.8k 🚀 +8/d | **50** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 676 | **50** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Plugin-first long-term memory for every agent platform. Corrections that stick. | 🟢 Easy | — | ✅ | 550 | **50** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **49** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 508 | **49** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew brings task execution, human approvals, persistent memory, and scheduled work into one desktop application. | 🟡 Some setup | — | ✅ | 254 | **47** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 246 | **45** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 314 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 522 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [affaan-m/ECC](https://github.com/affaan-m/ECC), [garrytan/gstack](https://github.com/garrytan/gstack), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [spinabot/brigade](https://github.com/spinabot/brigade), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)

*…and 2 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [xerj-org/xerj](https://github.com/xerj-org/xerj)

> XERJ: the search engine for AI agents.

**Core problems it solves**

- **Memory & context** — *f the same primitive: xerj autoindex makes an agent*
- **Agent runtime** — *rity audit of WordPress core,*
- **MCP support** — *ith Claude Code, Cursor and any MCP client.*
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

- Stars: **17,622** (+445.4/day over 5d)
- Health score: **87/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **4,585** (+100.4/day over 5d)
- Health score: **84/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-10-29
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

> Understand your repository, from source code to the systems around it.

**Core problems it solves**

- **Multi-account switching** — *led hooks through /hooks.*
- **Automatic failover** — *d without contacting support; and every teammate needs git lfs install; without it their checkout leaves a pointer file where the artifact should be,…*
- **Multi-agent orchestration** — *y and fail-open: it does not replace or block the requested tool call.*
- **Workspace isolation** — *, with exact omission metadata.*
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

- Stars: **47,825** (+78.0/day over 5d)
- Health score: **78/100**
- Documentation score: **76/100**
- License: MIT
- Language: C
- Last push: 2026-10-29
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [memvid/memvid](https://github.com/memvid/memvid)

> src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" />

**Core problems it solves**

- **Model / provider routing**
- **Memory & context** — *Memvid is a single-file memory layer for AI agents with instant retrieval and long-term memory.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -L 'https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/onnx/model.onnx' \`
- Platforms mentioned: Linux
- Some setup. install via pip install, global npm install; needs git clone (build from source), npm install/build; configure API key configuration

**Facts**

- Stars: **17,319** (+142.4/day over 5d)
- Health score: **76/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-07-14

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

- Stars: **32,913** (+36.8/day over 5d)
- Health score: **71/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-29
- Works with: Claude Code, Codex, Cursor, Cline / Roo

</details>

## Teams & Isolation

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🔴 Involved | — | — | 138.2k 🚀 +126/d | **88** |
| 🏆 **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 84.7k 🚀 +63/d | **78** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.9k 🚀 +32/d | **74** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.8k 🚀 +26/d | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.6k 🚀 +19/d | **67** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 8.4k 🚀 +26/d | **64** |
| 🔹 **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | Give ChatGPT a secure connection to your own machine and Turn ChatGPT into Codex | 🟢 Easy | — | — | 5.3k | **59** |
| 🔹 **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 1.5k (+9/d) | **59** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **58** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 588 | **56** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 786 (+5/d) | **55** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 460 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 321 | **55** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 585 | **54** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 321 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [getpaseo/paseo](https://github.com/getpaseo/paseo), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun), [crshdn/mission-control](https://github.com/crshdn/mission-control), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **138,230** (+126.4/day over 5d)
- Health score: **88/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

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

- Stars: **84,714** (+63.4/day over 5d)
- Health score: **78/100**
- Documentation score: **80/100**
- License: MIT
- Language: Python
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Cursor, Droid

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

- Stars: **33,916** (+32.4/day over 5d)
- Health score: **74/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **27,763** (+25.8/day over 5d)
- Health score: **70/100**
- Documentation score: **73/100**
- License: MIT
- Language: Python
- Last push: 2026-10-28
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

- Stars: **9,560** (+19.2/day over 5d)
- Health score: **67/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-10-30
- Works with: Claude Code, Codex

</details>

## Mobile & Remote Control

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 110.6k 🚀 +1084/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 108.8k 🚀 +348/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 22.5k 🚀 +118/d | **86** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 7.9k 🚀 +460/d | **86** |
| 🏆 **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 5.4k 🚀 +171/d | **86** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 15.8k 🚀 +229/d | **82** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 6.8k 🚀 +77/d | **77** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 3.7k 🚀 +140/d | **73** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 11.1k 🚀 +20/d | **68** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Self-Improving Sovereign Agents — voices: @tom_doerr, @AIDailyGems | 🟢 Easy | — | — | 5k 🚀 +32/d | **67** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 1k 🚀 +40/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.4k 🚀 +22/d | **65** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟡 Some setup | — | — | 5.4k 🚀 +8/d | **63** |
| 🔹 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 997 🚀 +13/d | **57** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.7k 🚀 +11/d | **55** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **51** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [makecindy/cindy](https://github.com/makecindy/cindy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **110,623** (+1083.6/day over 5d)
- Health score: **92/100**
- Documentation score: **52/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
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

- Stars: **108,823** (+348.4/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
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

- Stars: **22,504** (+117.6/day over 5d)
- Health score: **86/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

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

- Stars: **7,877** (+459.8/day over 5d)
- Health score: **86/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Codex, Cursor, Cline / Roo

#### [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)

> Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent.

**Core problems it solves**

- **Mobile access**
- **Skills & plugins** — *mmended — the skills CLI.*
- **Agent runtime**
- **Self-hostable** — *nto its own store under /db/.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add JimLiu/baoyu-design`
- Platforms mentioned: Linux, Web
- Turnkey. install via npx one-liner, native installer / package; needs npm install/build

**Facts**

- Stars: **5,352** (+170.8/day over 5d)
- Health score: **86/100**
- Documentation score: **63/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Cursor, Copilot, Cline / Roo

</details>

## Sharing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 25.9k 🚀 +968/d | **90** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 131.7k 🚀 +163/d | **89** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 31.7k 🚀 +62/d | **72** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 19.5k 🚀 +46/d | **72** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 10.2k 🚀 +56/d | **70** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | and connect OpenCode, Pi, Qoder, WorkBuddy, Kilo, Cline, T3 Code and more through managed configs. | 🟡 Some setup | — | — | 18.1k 🚀 +36/d | **67** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.6k 🚀 +16/d | **56** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k | **56** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.8k 🚀 +11/d | **55** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 549 🚀 +12/d | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 282 🚀 +5/d | **53** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 911 | **51** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 592 🚀 +23/d | **51** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 505 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 312 | **51** |
| 🔹 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | Built with C++ / Win32 / WebView2 for stability and speed. Quota dashboard, auto-refresh (5H / 7D), low-quota alerts and switch prompts | 🟡 Some setup | — | — | 250 | **45** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **25,913** (+967.6/day over 5d)
- Health score: **90/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-10-30
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

- Stars: **131,654** (+163.2/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-30
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

- Stars: **31,681** (+61.8/day over 5d)
- Health score: **72/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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
- **API gateway / proxy** — *d，保留客户端 Thread；增量请求继续使用有效上游状态、完整检查点或 WebSocket 历史，缺失上下文或上游明确拒绝时仍可能失败并保留原历史。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **19,544** (+45.6/day over 5d)
- Health score: **72/100**
- Documentation score: **64/100**
- Language: Rust
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **10,190** (+55.6/day over 5d)
- Health score: **70/100**
- Documentation score: **57/100**
- License: AGPL-3.0
- Language: JavaScript
- Last push: 2026-09-12
- Works with: Claude Code, Codex, Cursor

</details>

## Teams

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 165.3k 🚀 +299/d | **98** |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 63.1k 🚀 +459/d | **91** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 14.5k 🚀 +230/d | **85** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 11.4k 🚀 +78/d | **79** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.6k 🚀 +9/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k 🚀 +6/d | **57** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.1k 🚀 +8/d | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 423 | **54** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 432 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 304 | **49** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |

**Also does this:** [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

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

- Stars: **165,300** (+299.2/day over 5d)
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
- **Billing & metering** — *rs bubble, beeswarm and box plot; Treemap covers marimekko.*
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

- Stars: **63,135** (+458.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **14,505** (+230.0/day over 5d)
- Health score: **85/100**
- Documentation score: **71/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-30
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

- Stars: **11,351** (+77.6/day over 5d)
- Health score: **79/100**
- Documentation score: **79/100**
- License: MIT
- Language: Python
- Last push: 2026-10-28
- Works with: Claude Code, Codex, OpenCode

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

- Stars: **15,580** (+9.4/day over 5d)
- Health score: **57/100**
- Documentation score: **54/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | ✅ | 78.8k 🚀 +337/d | **91** |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 223.2k 🚀 +373/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 12.2k 🚀 +394/d | **88** |
| ✅ **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 3.7k 🚀 +285/d | **75** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | Turn the browser you already use into a workspace for your AI agent. | 🟢 Easy | — | — | 9.8k 🚀 +57/d | **71** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.3k 🚀 +20/d | **64** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.9k 🚀 +14/d | **62** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 478 | **56** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 481 🚀 +21/d | **54** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 774 | **53** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | Scope Recall v3 is a bounded local memory core with SQLite as the authority and rebuildable vector companions. | 🟢 Easy | — | — | 504 🚀 +7/d | **53** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 641 | **38** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [yetone/magpie](https://github.com/yetone/magpie), [xerj-org/xerj](https://github.com/xerj-org/xerj), [getpaseo/paseo](https://github.com/getpaseo/paseo), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [google/artemis](https://github.com/google/artemis), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) *(+55 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)

> So I built the filter I&nbsp;needed.

**Core problems it solves**

- **Model / provider routing** — *s the same in longer words.*
- **API gateway / proxy** — *s the same in longer words.*
- **Skills & plugins** — *does not duplicate the full project instructions when it reads both AGENTS.md and GEMINI.md.*
- **GUI / desktop app** — *st use; creates a dedicated project folder.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 42/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npx @santifer/career-ops init`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, config file; GUI application

**Facts**

- Stars: **78,787** (+337.0/day over 5d)
- Health score: **91/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **223,169** (+373.0/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
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

- Stars: **12,187** (+393.6/day over 5d)
- Health score: **88/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-30
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

- Stars: **3,701** (~284.7/day lifetime average)
- Health score: **75/100**
- Documentation score: **30/100**
- License: MIT
- Language: Python
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

> Turn the browser you already use into a workspace for your AI agent.

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

- Stars: **9,806** (+57.2/day over 5d)
- Health score: **71/100**
- Documentation score: **60/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Cursor

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3.4k 🚀 +98/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 45.1k 🚀 +70/d | **75** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 10.9k 🚀 +41/d | **66** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.8k 🚀 +22/d | **56** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 288 | **56** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 直接找：接口一览 ｜ 五分钟上手 ｜ 易支付协议兼容接入 ｜ 到账账号与收款分配 ｜ 文档目录 ｜ 常见问题 | 🟢 Easy | — | — | 324 | **52** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 823 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 409 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 437 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [decolua/9router](https://github.com/decolua/9router), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [spinabot/brigade](https://github.com/spinabot/brigade), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [cordum-io/cordum](https://github.com/cordum-io/cordum)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **3,411** (+98.2/day over 5d)
- Health score: **78/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-29
- Works with: Claude Code, Codex, Cursor

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

- Stars: **45,144** (+69.8/day over 5d)
- Health score: **75/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-30
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

- Stars: **10,937** (+41.0/day over 5d)
- Health score: **66/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **11,768** (+22.4/day over 5d)
- Health score: **56/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28

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

- Setup: 🟡 **Some setup** (friction 41/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via pip install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, .env file; Chinese: beginner/one-click framing

**Facts**

- Stars: **288** (+0.6/day over 5d)
- Health score: **56/100**
- Documentation score: **91/100**
- Language: HTML
- Last push: 2026-10-29
- Works with: Claude Code, Codex, Cursor, Cline / Roo, Droid

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | A toolbox of film styles made in code: 66 ready to use, and your own. You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. | 🟡 Some setup | — | ✅ | 9.6k 🚀 +550/d | **83** |
| 🏆 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 4k 🚀 +142/d | **78** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11k 🚀 +54/d | **69** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.6k 🚀 +41/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.4k 🚀 +33/d | **67** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.3k 🚀 +13/d | **60** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.9k 🚀 +11/d | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 350 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 715 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 472 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch), [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram), [Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge), [yc-software/qm](https://github.com/yc-software/qm), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [AVIDS2/memorix](https://github.com/AVIDS2/memorix), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills) *(+4 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

> A toolbox of film styles made in code: 66 ready to use, and your own.

**Core problems it solves**

- **Model / provider routing** — *e or make one from scratch, bring your story, and let your coding agent direct.*
- **Agent runtime**
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 44/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Some setup. needs git clone (build from source); GUI application

**Facts**

- Stars: **9,609** (+550.0/day over 5d)
- Health score: **83/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-29
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

- Stars: **3,967** (~141.7/day lifetime average)
- Health score: **78/100**
- Documentation score: **36/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-10-29
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

- Stars: **10,957** (+54.2/day over 5d)
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

- Stars: **17,602** (+41.0/day over 5d)
- Health score: **68/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **8,378** (+33.4/day over 5d)
- Health score: **67/100**
- Documentation score: **44/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-30

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 51k 🚀 +73/d | **73** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 8.7k 🚀 +87/d | **72** |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | The local-first harness & workspace for research agents. | 🟢 Turnkey · OOTB | ✅ | — | 7.7k 🚀 +29/d | **65** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 15.2k 🚀 +16/d | **65** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 9.2k 🚀 +26/d | **65** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 525 | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 557 | **46** |

**Also does this:** [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [superdesigndev/treg](https://github.com/superdesigndev/treg), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [decolua/9router](https://github.com/decolua/9router), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher), [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow), [cita-777/metapi](https://github.com/cita-777/metapi)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [QuantumNous/new-api](https://github.com/QuantumNous/new-api)

> An AI gateway for models, applications, and agents

**Core problems it solves**

- **Model / provider routing**
- **API gateway / proxy** — *ure container variables in Compose's environment or env_file; copying .env.example alone does not inject variables into the container.*
- **Usage analytics** — *DeepSeek, Qwen, and other compatible services.*
- **Skills & plugins** — *plugin installation states, usage, prices, and costs shown below are simulated data.*
- **Security & isolation** — *Asynchronous tasks Extend image, video, and other task APIs with JavaScript plugins, including task status and output retrieval Web console Configure…*
- **Self-hostable**
- **GUI / desktop app** — *Go module for protocol DTOs and conversions*

**Getting it running**

- Setup: 🔴 **Involved** (friction 100/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run --name new-api -d --restart unless-stopped \`
- Platforms mentioned: Linux, Web
- Involved setup. needs docker compose up, docker run; configure API key configuration, OAuth login flow; GUI application

**Facts**

- Stars: **51,038** (+73.4/day over 23d)
- Health score: **73/100**
- Documentation score: **75/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-30

#### [makecindy/cindy](https://github.com/makecindy/cindy)

> Cindy is an open-source AI agent, ready out of the box and yours to shape.

**Core problems it solves**

- **Remote control**
- **Mobile access** — *ch Linux and Omarchy installation guide*
- **Multi-agent orchestration** — *utor setup, validation, and submission workflow*
- **Model / provider routing**
- **Billing & metering** — *supported subscription you already pay for,*
- **Usage analytics** — *this is not fully anonymous.*
- **MCP support** — *TML, not just a wall of text.*
- **Self-hostable** — *by default (endpoint manifests in*

**Getting it running**

- Setup: 🔴 **Involved** (friction 65/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Involved setup. needs git clone (build from source), pnpm install/build; configure sign-in required, database migration; GUI application

**Facts**

- Stars: **8,658** (~87.5/day lifetime average)
- Health score: **72/100**
- Documentation score: **54/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-30
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

- Stars: **7,688** (+29.0/day over 5d)
- Health score: **65/100**
- Documentation score: **33/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-30
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

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

- Stars: **15,236** (+16.0/day over 5d)
- Health score: **65/100**
- Documentation score: **57/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Claude Code

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

- Stars: **9,217** (+25.8/day over 5d)
- Health score: **65/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-10-30

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 150.3k 🚀 +368/d | **93** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.2k 🚀 +30/d | **69** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.4k 🚀 +9/d | **56** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 882 🚀 +4/d | **56** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 763 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 435 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 510 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 598 | **45** |

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

- Stars: **150,296** (+367.8/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-30
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **4,207** (+29.6/day over 5d)
- Health score: **69/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-25
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

- Stars: **4,354** (+9.4/day over 5d)
- Health score: **56/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-24
- Works with: Codex

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

- Stars: **882** (+4.4/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-10-30
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

- Stars: **763** (+1.0/day over 5d)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-28
- Works with: Claude Code, Cursor

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Teams | Desktop UI, Mobile & Remote Control |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Memory & MCP | Desktop UI, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Failover |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile & Remote Control | Sharing, Teams & Isolation |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | Analytics, Desktop UI |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Desktop UI |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Memory & MCP | Desktop UI, Failover |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile & Remote Control | Analytics, Desktop UI |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Teams & Isolation | Desktop UI, Failover |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Failover | Desktop UI |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile & Remote Control | Desktop UI, Teams & Isolation |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile & Remote Control | Analytics, Memory & MCP |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile & Remote Control | Desktop UI |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Desktop UI, Memory & MCP |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Memory & MCP | Analytics, Billing |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI |
| **[google/artemis](https://github.com/google/artemis)** | Mobile & Remote Control | Desktop UI |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Memory & MCP | Analytics |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Desktop UI, Desktop UI |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Memory & MCP, Sharing |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Teams & Isolation | Desktop UI, Failover |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Failover | Desktop UI, Desktop UI |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile & Remote Control | Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Analytics, Sharing |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Memory & MCP | Desktop UI |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Analytics | Memory & MCP |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Desktop UI, Mobile & Remote Control |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Analytics, Billing |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Billing, Desktop UI |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Memory & MCP | Desktop UI, Failover |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Teams & Isolation | Desktop UI, Failover |
| **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Desktop UI | Desktop UI |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Billing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | Failover, Memory & MCP |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Mobile & Remote Control | Desktop UI, Teams & Isolation |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Desktop UI, Memory & MCP |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile & Remote Control | Desktop UI, Memory & MCP |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | Desktop UI, Model Routing |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile & Remote Control | Desktop UI, Desktop UI |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile & Remote Control | Desktop UI |
| **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | Analytics | Model Routing |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Analytics | Desktop UI, Failover |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Analytics | Desktop UI |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Memory & MCP | Desktop UI, Failover |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Mobile & Remote Control | Desktop UI |
| **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Failover | Model Routing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Memory & MCP | Billing, Failover |
| **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | Memory & MCP | Desktop UI, Model Routing |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | Teams & Isolation | Desktop UI |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Teams & Isolation | Analytics, Desktop UI |
| **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | Failover | Desktop UI, Desktop UI |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams | Desktop UI, Model Routing |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams | Desktop UI |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Failover | Desktop UI, Model Routing |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile & Remote Control | Analytics, Memory & MCP |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Failover | Desktop UI |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Desktop UI |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Teams & Isolation | Desktop UI, Mobile & Remote Control |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Desktop UI, Sharing |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Desktop UI, Memory & MCP |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | Sharing | Model Routing |
| **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Desktop UI | Desktop UI |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Failover | Desktop UI, Desktop UI |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Failover | Desktop UI, Desktop UI |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Memory & MCP | Desktop UI, Failover |
| **[0sec-labs/0](https://github.com/0sec-labs/0)** | Memory & MCP | Desktop UI |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | Memory & MCP | Desktop UI |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Desktop UI |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Teams & Isolation | Desktop UI, Desktop UI |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Sharing | Billing, Providers |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Failover | Memory & MCP, Model Routing |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Teams | Desktop UI, Sharing |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Failover |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Mobile & Remote Control, Teams & Isolation |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Failover | Desktop UI, Model Routing |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Billing, Memory & MCP |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams | Desktop UI, Desktop UI |
| **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | Billing | Sharing |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile & Remote Control | Desktop UI, Teams & Isolation |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Model Routing, Sharing |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile & Remote Control | Model Routing, Teams & Isolation |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile & Remote Control | Model Routing, Teams & Isolation |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Failover | Desktop UI, Model Routing |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Failover | Desktop UI, Desktop UI |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Sharing | Analytics, Memory & MCP |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Analytics | Memory & MCP, Teams |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Sharing | Desktop UI |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Sharing | Desktop UI |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Failover | Desktop UI |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Memory & MCP, Teams & Isolation |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Failover | Desktop UI |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Failover | Desktop UI |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Teams & Isolation | Analytics, Desktop UI |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Failover | Teams & Isolation |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Failover | Model Routing |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams | Mobile & Remote Control, Teams & Isolation |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Desktop UI, Teams & Isolation |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | Failover | Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Memory & MCP | Desktop UI |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Analytics | Memory & MCP |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Desktop UI |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Memory & MCP | Desktop UI, Desktop UI |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Failover | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Failover | Desktop UI, Memory & MCP |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Failover | Desktop UI |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Failover | Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.17x the stars (25,913 vs 150,296) |

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
| **[AI-QL/tuui](https://github.com/ai-ql/tuui)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 11.85x the stars (13,737 vs 1,159) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 59.77x the stars (19,544 vs 327) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 20.12x the stars (11,129 vs 553) | 🤖 auto (high) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 95.30x the stars (48,793 vs 512) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.09x the stars (19,544 vs 2,417) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 222.93x the stars (84,714 vs 380) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | 3.48x the stars (1,798 vs 516) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.24x the stars (11,351 vs 2,165) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 907.13x the stars (293,003 vs 323) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 68.01x the stars (293,003 vs 4,308) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.59x the stars (33,916 vs 927) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 132.23x the stars (48,793 vs 369) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 171.81x the stars (48,793 vs 284) | 🤖 auto (high) |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 54.18x the stars (33,916 vs 626) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 98.31x the stars (33,916 vs 345) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.60x the stars (27,763 vs 4,958) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.21x the stars (48,793 vs 3,695) | 🤖 auto (high) |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 67.01x the stars (30,022 vs 448) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 10.70x the stars (13,737 vs 1,284) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 13.48x the stars (30,022 vs 2,227) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 133.31x the stars (48,793 vs 366) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.48x the stars (11,351 vs 385) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 6.93x the stars (48,793 vs 7,040) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 47.48x the stars (22,504 vs 474) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 28.32x the stars (13,737 vs 485) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 156.89x the stars (48,793 vs 311) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 633.33x the stars (165,300 vs 261) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.88x the stars (33,916 vs 276) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 59.69x the stars (30,022 vs 503) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 473.35x the stars (293,003 vs 619) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 29.48x the stars (11,350 vs 385) | 🤖 auto (high) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 24.09x the stars (33,916 vs 1,408) | 🤖 auto (high) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 100.39x the stars (108,823 vs 1,084) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 34.96x the stars (19,544 vs 559) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 5.34x the stars (1,500 vs 281) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 80.70x the stars (30,022 vs 372) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 12.42x the stars (17,622 vs 1,419) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.72x the stars (293,003 vs 6,140) | 🤖 auto (high) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 106.46x the stars (30,022 vs 282) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 152.90x the stars (150,296 vs 983) | 🤖 auto (high) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 400.28x the stars (293,003 vs 732) | 🤖 auto (high) |
| **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 4.60x the stars (48,793 vs 10,603) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 34.70x the stars (48,793 vs 1,406) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.04x the stars (11,351 vs 2,808) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.54x the stars (11,351 vs 1,329) | 🤖 auto (medium) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.76x the stars (30,022 vs 1,791) | 🤖 auto (medium) |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 26.52x the stars (30,022 vs 1,132) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.28x the stars (27,763 vs 575) | 🤖 auto (medium) |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 10.51x the stars (7,693 vs 732) | 🤖 auto (medium) |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | **[DeusData/codebase-memory-mcp](https://github.com/deusdata/codebase-memory-mcp)** | 8.76x the stars (47,825 vs 5,457) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.33x the stars (22,504 vs 5,194) | 🤖 auto (medium) |
| **[AndrewDryga/emisar](https://github.com/andrewdryga/emisar)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 90.98x the stars (30,022 vs 330) | 🤖 auto (medium) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.03x the stars (11,351 vs 3,747) | 🤖 auto (medium) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 36.52x the stars (293,003 vs 8,023) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 114.27x the stars (48,793 vs 427) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 41.46x the stars (17,622 vs 425) | 🤖 auto (medium) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 616.85x the stars (293,003 vs 475) | 🤖 auto (medium) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 29.29x the stars (13,737 vs 469) | 🤖 auto (medium) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 64.54x the stars (48,793 vs 756) | 🤖 auto (medium) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 102.78x the stars (33,916 vs 330) | 🤖 auto (high) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.81x the stars (22,504 vs 5,913) | 🤖 auto (medium) |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 72.71x the stars (293,003 vs 4,030) | 🤖 auto (medium) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 34.74x the stars (293,003 vs 8,435) | 🤖 auto (medium) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.77x the stars (48,793 vs 27,537) | 🤖 auto (medium) |
| **[Leonxlnx/earshot](https://github.com/leonxlnx/earshot)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 14.92x the stars (48,793 vs 3,270) | 🤖 auto (high) |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 7.65x the stars (48,793 vs 6,382) | 🤖 auto (high) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.16x the stars (1,074 vs 498) | 🤖 auto (medium) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.18x the stars (321 vs 272) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui | 27.5k | 🔻 Superseded | 1.77x the stars (48,793 vs 27,537) |
| **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | desktop-ui | 10.6k | 🔻 Superseded | 4.60x the stars (48,793 vs 10,603) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | memory-mcp | 8.4k | 🔻 Superseded | 34.74x the stars (293,003 vs 8,435) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | memory-mcp | 8k | 🔻 Superseded | 36.52x the stars (293,003 vs 8,023) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | desktop-ui | 7k | 🔻 Superseded | 6.93x the stars (48,793 vs 7,040) |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | desktop-ui | 6.4k | 🔻 Superseded | 7.65x the stars (48,793 vs 6,382) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | memory-mcp | 6.1k | 🔻 Superseded | 47.72x the stars (293,003 vs 6,140) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | mobile-remote-control | 5.9k | 🔻 Superseded | 3.81x the stars (22,504 vs 5,913) |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | failover | 5.5k | 🔻 Superseded | 8.76x the stars (47,825 vs 5,457) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile-remote-control | 5.2k | 🔻 Superseded | 4.33x the stars (22,504 vs 5,194) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | teams-isolation | 5k | 🔻 Superseded | 5.60x the stars (27,763 vs 4,958) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | memory-mcp | 4.3k | 🔻 Superseded | 68.01x the stars (293,003 vs 4,308) |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | memory-mcp | 4k | 🔻 Superseded | 72.71x the stars (293,003 vs 4,030) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 Superseded | 3.03x the stars (11,351 vs 3,747) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui | 3.7k | 🔻 Superseded | 13.21x the stars (48,793 vs 3,695) |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | desktop-ui | 3.3k | 🔻 Superseded | 14.92x the stars (48,793 vs 3,270) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.8k | 🔻 Superseded | 4.04x the stars (11,351 vs 2,808) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 Superseded | 8.09x the stars (19,544 vs 2,417) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | memory-mcp | 2.2k | 🔻 Superseded | 13.48x the stars (30,022 vs 2,227) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.2k | 🔻 Superseded | 5.24x the stars (11,351 vs 2,165) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | memory-mcp | 1.8k | 🔻 Superseded | 16.76x the stars (30,022 vs 1,791) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | failover | 1.4k | 🔻 Superseded | 12.42x the stars (17,622 vs 1,419) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | teams-isolation | 1.4k | 🔻 Superseded | 24.09x the stars (33,916 vs 1,408) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | desktop-ui | 1.4k | 🔻 Superseded | 34.70x the stars (48,793 vs 1,406) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 8.54x the stars (11,351 vs 1,329) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | memory-mcp | 1.3k | 🔻 Superseded | 10.70x the stars (13,737 vs 1,284) |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | memory-mcp | 1.2k | 🔻 Superseded | 11.85x the stars (13,737 vs 1,159) |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | memory-mcp | 1.1k | 🔻 Superseded | 26.52x the stars (30,022 vs 1,132) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile-remote-control | 1.1k | 🔻 Superseded | 100.39x the stars (108,823 vs 1,084) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 983 | 🔻 Superseded | 152.90x the stars (150,296 vs 983) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | teams-isolation | 927 | 🔻 Superseded | 36.59x the stars (33,916 vs 927) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 756 | 🔻 Superseded | 64.54x the stars (48,793 vs 756) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | memory-mcp | 732 | 🔻 Superseded | 400.28x the stars (293,003 vs 732) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | failover | 732 | 🔻 Superseded | 10.51x the stars (7,693 vs 732) |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | teams-isolation | 626 | 🔻 Superseded | 54.18x the stars (33,916 vs 626) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | memory-mcp | 619 | 🔻 Superseded | 473.35x the stars (293,003 vs 619) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | teams-isolation | 575 | 🔻 Superseded | 48.28x the stars (27,763 vs 575) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 559 | 🔻 Superseded | 34.96x the stars (19,544 vs 559) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile-remote-control | 553 | 🔻 Superseded | 20.12x the stars (11,129 vs 553) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | failover | 516 | 🔻 Superseded | 3.48x the stars (1,798 vs 516) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | desktop-ui | 512 | 🔻 Superseded | 95.30x the stars (48,793 vs 512) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | memory-mcp | 503 | 🔻 Superseded | 59.69x the stars (30,022 vs 503) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 498 | 🔻 Superseded | 2.16x the stars (1,074 vs 498) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | memory-mcp | 485 | 🔻 Superseded | 28.32x the stars (13,737 vs 485) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | memory-mcp | 475 | 🔻 Superseded | 616.85x the stars (293,003 vs 475) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile-remote-control | 474 | 🔻 Superseded | 47.48x the stars (22,504 vs 474) |
| **[oracle/mcp](https://github.com/oracle/mcp)** | memory-mcp | 469 | 🔻 Superseded | 29.29x the stars (13,737 vs 469) |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | memory-mcp | 448 | 🔻 Superseded | 67.01x the stars (30,022 vs 448) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 427 | 🔻 Superseded | 114.27x the stars (48,793 vs 427) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | failover | 425 | 🔻 Superseded | 41.46x the stars (17,622 vs 425) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | memory-mcp | 385 | 🔻 Superseded | 29.48x the stars (11,350 vs 385) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 385 | 🔻 Superseded | 29.48x the stars (11,351 vs 385) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | teams-isolation | 380 | 🔻 Superseded | 222.93x the stars (84,714 vs 380) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | memory-mcp | 372 | 🔻 Superseded | 80.70x the stars (30,022 vs 372) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui | 369 | 🔻 Superseded | 132.23x the stars (48,793 vs 369) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 366 | 🔻 Superseded | 133.31x the stars (48,793 vs 366) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | teams-isolation | 345 | 🔻 Superseded | 98.31x the stars (33,916 vs 345) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | teams-isolation | 330 | 🔻 Superseded | 102.78x the stars (33,916 vs 330) |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | memory-mcp | 330 | 🔻 Superseded | 90.98x the stars (30,022 vs 330) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 Superseded | 59.77x the stars (19,544 vs 327) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | memory-mcp | 323 | 🔻 Superseded | 907.13x the stars (293,003 vs 323) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 311 | 🔻 Superseded | 156.89x the stars (48,793 vs 311) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 Superseded | 171.81x the stars (48,793 vs 284) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | memory-mcp | 282 | 🔻 Superseded | 106.46x the stars (30,022 vs 282) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | teams-isolation | 281 | 🔻 Superseded | 5.34x the stars (1,500 vs 281) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | teams-isolation | 276 | 🔻 Superseded | 122.88x the stars (33,916 vs 276) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | teams-isolation | 272 | 🔻 Superseded | 1.18x the stars (321 vs 272) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 261 | 🔻 Superseded | 633.33x the stars (165,300 vs 261) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-30 10:55 UTC. 205 live tools · 127 candidates rejected by the quality gates.</sub>
