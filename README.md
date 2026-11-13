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

**230 tools** across **13 categories** · **47 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-13 12:15 UTC**

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

- [Desktop UI](#desktop-ui) — 41 tools
- [Sharing](#sharing) — 23 tools
- [Isolation & Teams](#isolation-teams) — 24 tools
- [Memory & Failover](#memory-failover) — 22 tools
- [Billing](#billing) — 21 tools
- [MCP & Security](#mcp-security) — 22 tools
- [Mobile](#mobile) — 19 tools
- [Failover](#failover) — 11 tools
- [Analytics](#analytics) — 11 tools
- [Model Routing](#model-routing) — 11 tools
- [Desktop UI](#desktop-ui) — 10 tools
- [Providers](#providers) — 9 tools
- [Analytics](#analytics) — 6 tools
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
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 19.1k 🚀 +271/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 27k 🚀 +234/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 71.5k 🚀 +1047/d | **83** |
| 🏆 **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 9.1k 🚀 +92/d | **83** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 40 mandatory rules (R-01 to R-40) in three tiers: Hard Gate, Purpose-Gate, and Quality Locks. A Delivery Gate: a mandatory PASS/FAIL report in four blocks, run before anything ships. | 🟢 Turnkey · OOTB | ✅ | — | 9.1k 🚀 +92/d | **81** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 2,957+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟡 Some setup | — | — | 49.6k 🚀 +58/d | **78** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 6.8k 🚀 +98/d | **75** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 9.2k 🚀 +174/d | **71** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 6.6k 🚀 +68/d | **69** |
| ✅ **[AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer)** | Some of us write a lot of papers and grant proposals, and our team started using AI to help with drafts. | 🟡 Some setup | — | — | 4.8k 🚀 +200/d | **66** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.4k 🚀 +42/d | **64** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +18/d | **63** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 5k 🚀 +55/d | **63** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.8k 🚀 +17/d | **62** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.4k 🚀 +27/d | **61** |
| 🔹 **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.8k 🚀 +23/d | **61** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.8k | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 963 🚀 +4/d | **57** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | Built for graduate students, PhDs, postdocs, research support staff, and agent/harness builders who need inspectable research workflows rather than a black box. | 🟢 Easy | — | — | 654 🚀 +9/d | **57** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | Local-first search across your workspace, built for humans and AI agents. It was carnivorous because it climbed the curtain toward a canary's cage | 🟡 Some setup | — | — | 4.3k | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 555 | **56** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.3k 🚀 +21/d | **55** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 560 🚀 +6/d | **54** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor | 🔴 Involved | — | — | 787 | **52** |

**Also does this:** [garrytan/gstack](https://github.com/garrytan/gstack), [anomalyco/opencode](https://github.com/anomalyco/opencode), [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [qybaihe/bla](https://github.com/qybaihe/bla), [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), [langfuse/langfuse](https://github.com/langfuse/langfuse), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) *(+34 more)*

*…and 11 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **19,102** (+271.0/day over 5d)
- Health score: **86/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **27,041** (+233.8/day over 5d)
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

- Stars: **71,523** (+1046.8/day over 5d)
- Health score: **83/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

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

- Stars: **9,052** (+92.2/day over 5d)
- Health score: **83/100**
- Documentation score: **68/100**
- License: MIT
- Language: Go
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)

> A filter, not a style guide.

**Core problems it solves**

- **Skills & plugins** — *ll them (this project or everywhere), and which agents you use, then copies the folders and writes the pointer that reloads antislop every session.*
- **Agent runtime**
- **MCP support** — *Windows, set $env:MUSEEXPERIMENTALPLUGINS = "1" in PowerShell first, then run the two muse lines unchanged.*
- **Cross-agent support** — *Mentions Amp, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx antislop-ai`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via npx one-liner, native installer / package

**Facts**

- Stars: **9,088** (+92.4/day over 5d)
- Health score: **81/100**
- Documentation score: **55/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Sharing

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 107.5k 🚀 +180/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 82.3k 🚀 +257/d | **90** |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 2026-10-28 🚀 DeepTutor v1.7.0 is here! Partners and subagents — Consult live agents such as Claude Code, Codex, and Grok CLI, import past conversations, or run persistent Partners with their own memory, resources, and I… | 🟡 Some setup | — | — | 58.8k (+184/d) | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 302.2k 🚀 +566/d | **89** |
| 🏆 **[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)** | Reverse-engineer any video. | 🟢 Turnkey · OOTB | ✅ | ✅ | 7.7k 🚀 +553/d | **86** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.cursor — login and session history managed exclusively by the Cursor CLI. | 🟡 Some setup | — | — | 7.4k 🚀 +214/d | **84** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 15.8k 🚀 +82/d | **78** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 12.3k 🚀 +70/d | **76** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 7.9k 🚀 +58/d | **74** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | An open catalog of components for Claude Code, installable with one command. | 🟢 Easy | — | — | 33.5k 🚀 +52/d | **74** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 12k 🚀 +48/d | **73** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 51.9k 🚀 +64/d | **71** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Large stores keep working: state reads page, so scopes above 64 MiB no longer fail, on iii 0.25.1. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.3k 🚀 +28/d | **70** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.7k 🚀 +22/d | **65** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.9k 🚀 +24/d | **64** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.2k 🚀 +7/d | **54** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | English \| 简体中文 \| 日本語 | 🟢 Easy | — | — | 493 | **54** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 309 | **52** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 523 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 428 | **49** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 566 | **47** |

**Also does this:** [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub), [decolua/9router](https://github.com/decolua/9router), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [cordum-io/cordum](https://github.com/cordum-io/cordum), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside), [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)

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

- Stars: **107,463** (+180.2/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-13
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

- Stars: **82,308** (+256.6/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-13
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

- Stars: **58,816** (~184.4/day lifetime average)
- Health score: **90/100**
- Documentation score: **81/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-07
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

- Stars: **302,226** (+565.8/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)

> Reverse-engineer any video.

**Core problems it solves**

- **Self-hostable** — *a video down, the remake recipe in capsule-cinema generates a new version that keeps the original's camera, motion, pacing and transitions and swaps…*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: Linux, Web
- Turnkey. install via pip install; one-click setup

**Facts**

- Stars: **7,740** (~552.9/day lifetime average)
- Health score: **86/100**
- Documentation score: **49/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-13
- Works with: Claude Code, Codex

</details>

## Isolation & Teams

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🟡 Some setup | — | — | 141.4k 🚀 +142/d | **91** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 113.5k 🚀 +273/d | **89** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 18.4k 🚀 +810/d | **85** |
| 🏆 **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12.5k 🚀 +95/d | **83** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 12.8k 🚀 +297/d | **81** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 2.5k 🚀 +94/d | **77** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 48.6k 🚀 +55/d | **74** |
| ✅ **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | ThinkRail is an agentic IDE that gets better every time you use it. Skills. | 🟢 Turnkey | — | ✅ | 8.2k 🚀 +58/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.3k 🚀 +31/d | **72** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 28k 🚀 +18/d | **69** |
| ✅ **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **62** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 691 🚀 +19/d | **60** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.3k 🚀 +5/d | **58** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Stall detection — a warning after 120 s without output, stalled after 600 s Worktrees — run each task in its own git worktree on a the-pair/… branch, then commit and push from the inspector | 🟢 Easy | — | ✅ | 389 | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 624 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 505 | **56** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 453 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 333 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 787 | **52** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **52** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 3k | **49** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 323 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [affaan-m/ECC](https://github.com/affaan-m/ECC), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [getpaseo/paseo](https://github.com/getpaseo/paseo), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go), [felinics/Memoh](https://github.com/felinics/Memoh), [abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) *(+3 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who…

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *the cause and re-verify before committing.*
- **Workspace isolation** — *sses; blocks below 7/10), fail-closed secret redaction, dedupe against existing issues, archive to $GSTACKSTATEROOT/projects/$SLUG/specs/ for team-co…*
- **Model / provider routing** — *deterministic aside repl scripts.*
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

- Stars: **141,427** (+142.4/day over 5d)
- Health score: **91/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
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

- Stars: **113,522** (+273.0/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **18,380** (+809.6/day over 5d)
- Health score: **85/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-13
- Works with: Claude Code, Codex

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

- Stars: **12,494** (+95.2/day over 5d)
- Health score: **83/100**
- Documentation score: **54/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-11-13
- Works with: Claude Code, Codex

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

- Stars: **12,810** (+296.6/day over 5d)
- Health score: **81/100**
- Documentation score: **41/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Codex

</details>

## Memory & Failover

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | English \| 简体中文 \| 日本語 \| العربية \| Español \| 한국어 \| فارسی XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 19k 🚀 +82/d | **80** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.3k 🚀 +32/d | **70** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 8.1k 🚀 +48/d | **69** |
| 🔹 **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 9.6k 🚀 +39/d | **61** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.4k 🚀 +17/d | **59** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Unify engineering teams around standardized workflows and shared best practices, across modern stacks and legacy systems, while reducing technical debt. | 🟢 Turnkey · OOTB | ✅ | — | 556 | **57** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | Turn stateless LLMs into a stateful, compounding AI agent — portable across any IDE. | 🟢 Easy | — | — | 622 | **56** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.9k 🚀 +7/d | **55** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Your corrections, remembered by Claude Code, Codex and Cursor. Decay tied with decay switched off. | 🟡 Some setup | — | — | 792 | **55** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 438 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 411 | **54** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k 🚀 +5/d | **53** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟡 Some setup | — | — | 557 🚀 +9/d | **53** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 930 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 458 | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **51** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 936 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 717 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 679 | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 530 | **49** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 490 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 525 | **43** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [spinabot/brigade](https://github.com/spinabot/brigade) *(+14 more)*

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

- Stars: **19,008** (+81.6/day over 5d)
- Health score: **80/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-13
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

- Stars: **33,292** (+32.2/day over 5d)
- Health score: **70/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-13
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

- Stars: **8,089** (+47.8/day over 5d)
- Health score: **69/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-12
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

- Stars: **9,596** (+39.2/day over 5d)
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

- Stars: **1,426** (+16.6/day over 5d)
- Health score: **59/100**
- Documentation score: **70/100**
- License: MIT
- Language: Python
- Last push: 2026-10-23
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Droid

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 35.9k 🚀 +772/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 5k 🚀 +202/d | **84** |
| ✅ **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 本项目仅用于协议学习、研究与个人自用。请优先使用官方客户端，不要使用主账号，不要共享账号，也不要用于商业转售。 | 🟢 Easy | — | — | 4k 🚀 +65/d | **71** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.4k 🚀 +51/d | **70** |
| ✅ **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | OmniGet is a free, open source (GPL-3.0) desktop app for Windows, macOS and Linux. | 🟢 Easy | — | — | 14.4k (+53/d) | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 20k 🚀 +28/d | **68** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | and connect OpenCode, Pi, Qoder, WorkBuddy, Kilo, Cline, T3 Code and more through managed configs. | 🟡 Some setup | — | — | 18.5k 🚀 +34/d | **66** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3.6k 🚀 +15/d | **62** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k | **60** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5.2k 🚀 +39/d | **58** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 296 | **56** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.9k 🚀 +6/d | **54** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 328 | **53** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 517 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Quota of the Google Antigravity clients (the new desktop App and the agy CLI): remaining share and reset time of the 5-hour and weekly windows for Gemini models and… | 🟢 Easy | — | — | 326 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k 🚀 +4/d | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 546 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 给做 SEO 和独立开发的人用的 Agent Skills。建站、选词、发外链、查数据、复盘迭代，一整条链路都在这个仓库里，装完就能跑。 | 🟢 Easy | — | — | 304 🚀 +5/d | **51** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 561 | **49** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)

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

- Stars: **35,914** (+771.6/day over 5d)
- Health score: **91/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-13
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

- Stars: **5,050** (+202.0/day over 5d)
- Health score: **84/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)

> 本项目仅用于协议学习、研究与个人自用。请优先使用官方客户端，不要使用主账号，不要共享账号，也不要用于商业转售。

**Core problems it solves**

- **Multi-account switching** — *：将 WorkBuddy（国际版/国内版）与 CodeArts 封装为标准 OpenAI 格式（Chat Completions / Responses），无缝支持 Codex、Claude Code、NextChat 等各类客户端。*
- **Quota & usage management**
- **Automatic failover** — *（Chat Completions / Responses），无缝支持 Codex、Claude Code、NextChat 等各类客户端。*
- **Mobile access** — *（Windows 自带精简运行时），支持 Docker、NAS（群晖/飞牛）一键部署及 OpenWrt 路由器固件。*
- **Model / provider routing** — *绑定**：可固定走国际版、国内版或 CodeArts；*
- **API gateway / proxy** — *# WorkBuddy2API-Hub — 国际版、国内版多账号网关中枢*
- **Quota sharing / splitting**
- **Billing & metering** — *x-stainless-os（如 Linux / Windows）*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/ardeyouxipianyi/workbuddy2api-hub/main/quick-deploy.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer; needs docker compose up; configure API key configuration, OAuth login flow; one-click setup

**Facts**

- Stars: **4,022** (+64.8/day over 5d)
- Health score: **71/100**
- Documentation score: **56/100**
- License: MIT
- Language: Python
- Last push: 2026-11-13
- Works with: Claude Code, Codex

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

- Stars: **32,355** (+51.4/day over 5d)
- Health score: **70/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-12
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [tonhowtf/omniget](https://github.com/tonhowtf/omniget)

> OmniGet is a free, open source (GPL-3.0) desktop app for Windows, macOS and Linux.

**Core problems it solves**

- **Quota & usage management** — *el, and its permission requests show up in OmniGet.*
- **Automatic failover** — *opy the Pairing token from OmniGet and paste it there.*
- **Agent runtime**
- **MCP support** — *Or ask Claude to do it for you.*
- **Security & isolation** — *the terminal: omniget-cli*
- **GUI / desktop app** — *Every build is on the Releases page.*
- **Notifications** — *k exits 0 or the rounds or minutes run out.*
- **Cross-agent support** — *Mentions Aider, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 20/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, winget install; needs git clone (build from source), pnpm install/build; configure sign-in required, database dependency; one-click setup

**Facts**

- Stars: **14,393** (~52.5/day lifetime average)
- Health score: **69/100**
- Documentation score: **62/100**
- License: GPL-3.0
- Language: Rust
- Last push: 2026-09-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Aider

</details>

## MCP & Security

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 23.6k 🚀 +128/d | **89** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 5.4k 🚀 +118/d | **87** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Rom… | 🟢 Easy | — | — | 5.5k 🚀 +290/d | **85** |
| 🏆 **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | opencode support is experimental: it was tested on 1.19.5 and 2.2.0 only, and not in the Cursor Agent support is experimental. | 🟢 Easy | — | ✅ | 6k 🚀 +205/d | **84** |
| 🏆 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Easy · OOTB | ✅ | — | 1.3k 🚀 +146/d | **79** |
| ✅ **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Real vs code-synthesized: held-out ROC-AUC 0.92 with whole sound families held out. Listening through a soundtrack: 93% of the sound effects placed in a 60 s film mix are detected as events (89% | 🟡 Some setup | — | — | 4.7k 🚀 +97/d | **76** |
| ✅ **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 9.5k 🚀 +104/d | **74** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.7k 🚀 +25/d | **65** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k | **62** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k 🚀 +4/d | **56** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance 3,985 archived projects -- full source code snapshots from the game security ecosystem (prefixed ags-) | 🟢 Easy | — | — | 568 | **56** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 478 | **55** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 392 | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 375 🚀 +5/d | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 745 | **52** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | ⚠️ This project includes production-ready security features but is still under active development. | 🟡 Some setup | — | — | 371 | **52** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **51** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 478 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 419 | **42** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [garrytan/gstack](https://github.com/garrytan/gstack), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [superdesigndev/treg](https://github.com/superdesigndev/treg), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [tonhowtf/omniget](https://github.com/tonhowtf/omniget), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) *(+23 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **23,631** (+128.2/day over 5d)
- Health score: **89/100**
- Documentation score: **51/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-13

#### [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

> Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output.

**Core problems it solves**

- **Automatic failover** — *It falls back to the CPU encoder — reported in the result's hw.fallback/hw.notes — only when VideoToolbox itself refuses a job (any other ffmpeg fail…*
- **Multi-agent orchestration** — *contract and the test suite (tests/testcontract.py,*
- **API gateway / proxy** — *-pass encode and measures it ; --preset copy --repair remuxes a damaged file (timestamps regenerated, corrupt packets dropped) and counts the errors…*
- **Skills & plugins** — *. The footage is synthetic (FFmpeg's own test sources) except in three demos, reframetalk, filleren and pausesen, which use two AI-generated clips of…*
- **Agent runtime** — *Give your coding agent a video editor.*
- **MCP support** — *Give your coding agent a video editor.*
- **Security & isolation** — *re recorded in diagnostics and on stderr (codes: jsonoutput.diagnosticcodes); tools that draw text name the font they drew with (fontused).*
- **Voice input**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx ffmpeg-skill`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via npx one-liner, pip install

**Facts**

- Stars: **5,369** (+117.8/day over 5d)
- Health score: **87/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, Cursor

#### [qybaihe/bla](https://github.com/qybaihe/bla)

> English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Roman Urdu · Română

**Core problems it solves**

- **Multi-agent orchestration** — *ur coding agent (**Claude Code, Cursor, Codex, Windsurf, Gemini CLI, GitHub Copilot CLI, VS Code, OpenCode, Antigravity**):*
- **Agent runtime** — *al property and release artifacts.*
- **MCP support** — *aliano · Ελληνικά · മലയാളം · Roman Urdu · Română*
- **GUI / desktop app** — *et Breakers) Trips exact analyzer limits (primitive-candidates, alias-selections, ASAR 16 MiB header, WASM Wabt representation, SQLite virtual column…*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx bla-agents harden .`
- Platforms mentioned: Windows, Linux, Android
- Easy. install via npx one-liner; needs npm install/build, go build; configure config.json/yaml/toml, database dependency; one-click setup

**Facts**

- Stars: **5,513** (~290.2/day lifetime average)
- Health score: **85/100**
- Documentation score: **77/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
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

- Stars: **5,997** (+204.8/day over 5d)
- Health score: **84/100**
- Documentation score: **61/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-12
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

#### [0sec-labs/0](https://github.com/0sec-labs/0)

> Investigate vulnerabilities, review findings, and work on fixes in your browser.

**Core problems it solves**

- **Agent runtime** — *The open-source AI security harness*
- **MCP support** — *source AI security harness*
- **GUI / desktop app**

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/0sec-labs/0/main/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer; needs pnpm install/build

**Facts**

- Stars: **1,336** (+146.4/day over 5d)
- Health score: **79/100**
- Documentation score: **41/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-10

</details>

## Mobile

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 168k 🚀 +168/d | **98** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree. | 🟢 Turnkey · OOTB | ✅ | ✅ | 124k 🚀 +1022/d | **92** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 22k 🚀 +882/d | **88** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal. | 🟢 Turnkey · OOTB | ✅ | ✅ | 9.1k 🚀 +338/d | **86** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 24k 🚀 +102/d | **83** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | An AI assistant on your phone: say what you need, and it works your apps and the web until it's done. | 🟢 Easy | — | ✅ | 8.5k 🚀 +607/d | **81** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟡 Some setup | — | — | 2.8k 🚀 +107/d | **78** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.2k 🚀 +22/d | **65** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Talk to Claude as usual. | 🟢 Easy | — | — | 5.3k 🚀 +19/d | **65** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.6k 🚀 +16/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.4k 🚀 +14/d | **64** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2.1k 🚀 +18/d | **63** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | ✅ | 5.2k 🚀 +5/d | **56** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.8k 🚀 +9/d | **54** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.1k | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 557 | **50** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **48** |

**Also does this:** [makecindy/cindy](https://github.com/makecindy/cindy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **168,031** (+167.6/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **124,004** (+1021.8/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

#### [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

> The open-source Grok Bot alternative: your own team of AI bots, in a chat app.

**Core problems it solves**

- **Mobile access** — *protected by pairing, an existing*
- **Multi-agent orchestration** — *n/ macOS, Windows, and Ubuntu shells with an embedded harness and platform capabilities; Apple speech stays macOS-only, Ubuntu Xorg has opt-in local…*
- **Model / provider routing** — *configuration switches, defaults and model-call implications, see Feature switches.*
- **API gateway / proxy** — *via docs/custom-mcp-servers.md.*
- **Usage analytics** — *d model-call implications, see Feature switches.*
- **Skills & plugins** — *skills switched off and routines paused.*
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

- Stars: **21,977** (+881.6/day over 5d)
- Health score: **88/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-13
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

- Stars: **9,135** (~338.3/day lifetime average)
- Health score: **86/100**
- Documentation score: **51/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-12
- Works with: Claude Code

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

- Stars: **23,964** (+102.0/day over 5d)
- Health score: **83/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 154.1k 🚀 +294/d | **94** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 135.2k 🚀 +306/d | **89** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 7k 🚀 +93/d | **83** |
| ✅ **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 6.9k 🚀 +70/d | **76** |
| ✅ **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | The agent skills I use every day, cleaned up so anyone can use them. | 🟡 Some setup | — | — | 3.6k 🚀 +181/d | **74** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.8k 🚀 +9/d | **63** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2k 🚀 +12/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.5k | **58** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.9k | **56** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 8k 🚀 +10/d | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 316 | **44** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness), [xerj-org/xerj](https://github.com/xerj-org/xerj), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids), [1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [routatic/proxy](https://github.com/routatic/proxy), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) *(+9 more)*

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

- Stars: **154,149** (+293.6/day over 5d)
- Health score: **94/100**
- Documentation score: **78/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **135,157** (+306.2/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-13
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

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

- Stars: **6,950** (+93.4/day over 5d)
- Health score: **83/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-11-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)

> 让你的coding agent，把艺术风格写成会动的画。

**Core problems it solves**

- **Automatic failover** — *dex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。*
- **Skills & plugins** — *e glad to see this approach to art animation used in another open-source project, and thank the Open Design team.*
- **Agent runtime** — *；《Clawd 博物馆奇妙夜》是非官方的同人示范，与 Anthropic 无关，GIF 与成片同样不随 MIT 授权。*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add alchaincyf/huashu-art-motion`
- Turnkey. install via npx one-liner

**Facts**

- Stars: **6,853** (+69.8/day over 5d)
- Health score: **76/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-10
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

- Stars: **3,615** (~180.8/day lifetime average)
- Health score: **74/100**
- Documentation score: **25/100**
- License: MIT
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex

</details>

## Analytics

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 66.8k 🚀 +215/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.3k 🚀 +260/d | **84** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | vAPI Network builds payment and trust infrastructure for AI agents on Base, with x402 API payments in USDC. | 🟡 Some setup | — | — | 4.3k 🚀 +105/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 46k 🚀 +64/d | **74** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 4.2k 🚀 +48/d | **68** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends. | 🟢 Easy | — | ✅ | 5.5k 🚀 +6/d | **64** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.2k 🚀 +21/d | **62** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 12k 🚀 +28/d | **56** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 415 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 840 | **50** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 450 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [wangzan101/Mika](https://github.com/wangzan101/Mika), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [makecindy/cindy](https://github.com/makecindy/cindy), [superdesigndev/treg](https://github.com/superdesigndev/treg), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch), [topoteretes/cognee](https://github.com/topoteretes/cognee), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [spinabot/brigade](https://github.com/spinabot/brigade) *(+11 more)*

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

- Stars: **66,825** (+214.8/day over 5d)
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

- Stars: **7,269** (+259.6/day over 5d)
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

- Stars: **4,302** (~104.9/day lifetime average)
- Health score: **78/100**
- Documentation score: **62/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-10
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

- Stars: **45,978** (+64.2/day over 5d)
- Health score: **74/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-13
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)

> 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。视频生成成本约 40 元。

**Core problems it solves**

- **Billing & metering**
- **Agent runtime** — */user-attachments/assets/f67e2e04-52e7-42a9-a4a0-e2864ff0f51e*
- **Self-hostable** — *提交后可能已产生费用，内置 adapter 拿到供应商任务 ID 就会立刻写入本地文件。*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add zenstory-ai/drama-skills -y -g`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **4,185** (+48.0/day over 5d)
- Health score: **68/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-11-10
- Works with: Claude Code, Codex

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 155.5k 🚀 +114/d | **88** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. 2026-11-12 · 33 new styles: 99 now, in 15 categories sorted by what the picture looks like, and the gallery in English and Chinese, wit… | 🟡 Some setup | — | ✅ | 15.5k 🚀 +393/d | **84** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 22.9k 🚀 +385/d | **78** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.4k 🚀 +32/d | **61** |
| 🔹 **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | DeepSeek Harness, OpenClaw, Hermes, Claude Code, Codex, Cursor, WorkBuddy, OpenCode, Pi...they all work! | 🟡 Some setup | — | — | 2.2k | **56** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2.1k 🚀 +11/d | **55** |
| 🔹 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 3.8k | **54** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 358 | **53** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote attaches to a running pi session through pi's official extension API. The extension channel (7001) binds to 127.0.0.1 by default. | 🟢 Easy | — | — | 328 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 723 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 487 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [anomalyco/opencode](https://github.com/anomalyco/opencode), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [openai/codex](https://github.com/openai/codex), [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [openfilm/openfilm](https://github.com/openfilm/openfilm), [0sec-labs/0](https://github.com/0sec-labs/0), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [langfuse/langfuse](https://github.com/langfuse/langfuse) *(+23 more)*

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

- Stars: **155,516** (+113.6/day over 5d)
- Health score: **88/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **15,516** (+393.2/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: NOASSERTION
- Language: JavaScript
- Last push: 2026-11-12
- Works with: Claude Code, Codex

#### [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)

> dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness.

**Core problems it solves**

- **Agent runtime** — *t Design: Towards a More Autonomous Agent System.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux, Web
- Easy. configure server/reverse-proxy setup

**Facts**

- Stars: **22,944** (+385.4/day over 5d)
- Health score: **78/100**
- Documentation score: **23/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-03

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

- Stars: **11,420** (+31.8/day over 5d)
- Health score: **61/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

#### [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)

> DeepSeek Harness, OpenClaw, Hermes, Claude Code, Codex, Cursor, WorkBuddy, OpenCode, Pi...they all work!

**Core problems it solves**

- **Model / provider routing** — *complete Memory + Agent Runtime.*
- **Memory & context** — *assistants; its exploration of multi-platform messaging channels directly inspired Memmy's channel connection design.*
- **Agent runtime** — *details about the architecture, memory service, and integration methods, see the Memmy documentation.*
- **MCP support** — *Agent can "understand you better the more you use it".*
- **Team collaboration** — *ory infrastructure, and its scope goes beyond coding Agents:*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 42/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/MemTensor/memmy-agent/main/scripts/install.sh | bash`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via curl | sh installer, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, .env file; GUI application

**Facts**

- Stars: **2,214** (+2.0/day over 5d)
- Health score: **56/100**
- Documentation score: **61/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 226.6k 🚀 +234/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 16.1k 🚀 +236/d | **89** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm lets your coding agent make videos, and lets you edit them. | 🟢 Easy | — | ✅ | 6.2k 🚀 +186/d | **80** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.4k 🚀 +6/d | **61** |
| 🔹 **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 Turnkey · OOTB | ✅ | ✅ | 3.6k 🚀 +12/d | **60** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 4.2k 🚀 +30/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 492 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 798 | **53** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 612 🚀 +11/d | **52** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [yetone/magpie](https://github.com/yetone/magpie), [openai/codex](https://github.com/openai/codex), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [qybaihe/bla](https://github.com/qybaihe/bla), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [getpaseo/paseo](https://github.com/getpaseo/paseo), [xerj-org/xerj](https://github.com/xerj-org/xerj), [0sec-labs/0](https://github.com/0sec-labs/0) *(+36 more)*

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

- Stars: **226,563** (+234.2/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
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

- Stars: **16,072** (+236.4/day over 5d)
- Health score: **89/100**
- Documentation score: **59/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-13
- Works with: Claude Code

#### [openfilm/openfilm](https://github.com/openfilm/openfilm)

> OpenFilm lets your coding agent make videos, and lets you edit them.

**Core problems it solves**

- **Agent runtime** — *The open source AI video agent.*
- **GUI / desktop app** — *video for my CLI, with music.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npx skills add openfilm/openfilm`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner; needs git clone (build from source), pnpm install/build; configure sign-in required; GUI application

**Facts**

- Stars: **6,202** (+186.2/day over 5d)
- Health score: **80/100**
- Documentation score: **37/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex

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

- Stars: **15,406** (+6.4/day over 5d)
- Health score: **61/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

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

- Stars: **3,589** (+11.6/day over 26d)
- Health score: **60/100**
- Documentation score: **35/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Cursor

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.7k 🚀 +31/d | **70** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.3k 🚀 +12/d | **58** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.4k 🚀 +6/d | **55** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 981 | **55** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 930 | **55** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 776 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 441 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 605 | **45** |

**Also does this:** [automazeio/ccpm](https://github.com/automazeio/ccpm), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)

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
- **Skills & plugins** — *list、多平台格式适配；小红书、抖音、快手、知乎、B 站、微信视频号、微信公众号、推特 X、掘金、今日头条登录与发布；内容日历回写、账号数据、评论洞察（掘金走公开 JSON 接口、X 走网页 DOM 采集）、内容复盘、ROI 与画像记忆*
- **GUI / desktop app** — *后安装器会创建项目内 .venv，安装 Python/Node 依赖、前端生产包和 Playwright Chromium，并使用独立的 easel OpenClaw profile。*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, native installer / package; needs git clone (build from source); configure API key configuration; Chinese: beginner/one-click framing

**Facts**

- Stars: **4,656** (+31.4/day over 5d)
- Health score: **70/100**
- Documentation score: **80/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-12
- Works with: Claude Code, Codex

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

- Stars: **4,347** (+12.2/day over 5d)
- Health score: **58/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Aider, Cline / Roo

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

- Stars: **4,440** (+5.8/day over 5d)
- Health score: **55/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-09
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

- Stars: **981** (+0.2/day over 5d)
- Health score: **55/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-11-13
- Works with: Claude Code, OpenCode

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

- Stars: **930** (+2.8/day over 5d)
- Health score: **55/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-04
- Works with: Claude Code, Codex

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 10k 🚀 +106/d | **76** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Comprehensive API: Langfuse is frequently used to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API. AI Gateway (beta) gives your organization one endpoint for calls… | 🟢 Easy | — | ✅ | 37.4k (+29/d) | **75** |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.5k 🚀 +49/d | **71** |
| ✅ **[scenario-labs/skills](https://github.com/scenario-labs/skills)** | "Make a seamless brick texture, then upscale it to 2048 without breaking the tiling" "Generate four style-matched potion icons with transparent backgrounds for my RPG inventory" | 🟡 Some setup | — | — | 3.7k 🚀 +40/d | **66** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 6k | **50** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub), [decolua/9router](https://github.com/decolua/9router), [zai-org/ZCode](https://github.com/zai-org/ZCode), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair), [cita-777/metapi](https://github.com/cita-777/metapi), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [BennyKok/omg.dev](https://github.com/BennyKok/omg.dev) *(+1 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [makecindy/cindy](https://github.com/makecindy/cindy)

> Cindy is an open-source AI agent, ready out of the box and yours to shape.

**Core problems it solves**

- **Remote control**
- **Mobile access** — *up and migration from a manual install.*
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

- Stars: **10,020** (+105.6/day over 5d)
- Health score: **76/100**
- Documentation score: **54/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex

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

- Stars: **37,388** (~29.4/day lifetime average)
- Health score: **75/100**
- Documentation score: **81/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-13
- Works with: Claude Code, Codex, Cursor, Copilot, Aider, Cline / Roo

#### [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)

> Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost.

**Core problems it solves**

- **Usage analytics** — *Run your team with confidence**.*
- **Agent runtime** — *logs and versions, and either files the ticket or tells the reporter what is still missing.*
- **MCP support** — *rough the documentation yourself, connect an agent to it*
- **Self-hostable** — *Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost.*
- **GUI / desktop app** — *gets, choose which connectors are on, and control who has access.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **4,489** (+49.2/day over 5d)
- Health score: **71/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-13
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [scenario-labs/skills](https://github.com/scenario-labs/skills)

> Scenario Agent Skills

**Core problems it solves**

- **Remote control**
- **Model / provider routing** — *, add look directions to a v1 sheet, a new outfit or color, a rename, a check and GIF preview*
- **Usage analytics**
- **Skills & plugins** — *tutorials, conference talks, and*
- **Agent runtime**
- **MCP support** — *machine (ZBrush, Blender, Maya, Unreal*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add scenario-labs/skills --skill scenario scenario-inspiration scenario-image scenario-multi-refer…`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Some setup. install via npx one-liner, native installer / package; needs pnpm install/build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **3,747** (~40.3/day lifetime average)
- Health score: **66/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-11-12
- Works with: Claude Code, Codex, Cursor, Copilot

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

- Stars: **5,952** (+0.6/day over 5d)
- Health score: **50/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile | Failover, MCP & Security |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Sharing | Memory & Failover, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Failover | Analytics, Billing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Desktop UI, Isolation & Teams |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | Desktop UI, Model Routing |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Isolation & Teams | Desktop UI, MCP & Security |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI, Model Routing |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Sharing | Model Routing |
| **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | Sharing | Desktop UI, Memory & Failover |
| **[openai/codex](https://github.com/openai/codex)** | Failover | Desktop UI, Model Routing |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Sharing | Isolation & Teams, MCP & Security |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Isolation & Teams | Analytics, Memory & Failover |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile | MCP & Security, Sharing |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | MCP & Security | Desktop UI, Desktop UI |
| **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | Mobile | Failover, Model Routing |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[qybaihe/bla](https://github.com/qybaihe/bla)** | MCP & Security | Desktop UI, Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Sharing | Analytics, Isolation & Teams |
| **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Analytics | Desktop UI |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | MCP & Security | Desktop UI, Memory & Failover |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | MCP & Security, Memory & Failover |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Desktop UI, Isolation & Teams |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI, Model Routing |
| **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | Mobile | Analytics |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Memory & Failover | Desktop UI, Failover |
| **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | Desktop UI | Model Routing |
| **[0sec-labs/0](https://github.com/0sec-labs/0)** | MCP & Security | Desktop UI, Model Routing |
| **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | Analytics | MCP & Security |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | Desktop UI, MCP & Security |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Sharing | Memory & Failover, Model Routing |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Failover, Sharing |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Isolation & Teams | Desktop UI, Failover |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Analytics, Mobile |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Failover | Desktop UI |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | MCP & Security | Desktop UI |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Sharing | Analytics, Model Routing |
| **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Analytics | Desktop UI, Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Analytics | Billing, Model Routing |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Sharing | Analytics, MCP & Security |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Sharing | Desktop UI, MCP & Security |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Sharing | Analytics, Desktop UI |
| **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Analytics | Analytics, Desktop UI |
| **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | Billing | Analytics, Sharing |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Sharing | Analytics, Model Routing |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Failover, Model Routing |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | Memory & Failover | Analytics |
| **[decolua/9router](https://github.com/decolua/9router)** | Billing | Analytics, Sharing |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Sharing | MCP & Security, Memory & Failover |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | Billing | Desktop UI, MCP & Security |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Isolation & Teams, MCP & Security |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Billing | Desktop UI, Model Routing |
| **[scenario-labs/skills](https://github.com/scenario-labs/skills)** | Analytics | Desktop UI, Model Routing |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Sharing | Analytics, Model Routing |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Desktop UI, Model Routing |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Desktop UI, MCP & Security |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI, MCP & Security |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Sharing | Memory & Failover, Model Routing |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Analytics | MCP & Security |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Analytics, Analytics |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Desktop UI | Desktop UI |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, MCP & Security |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Analytics | Desktop UI, Model Routing |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Analytics, Sharing |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Failover | Desktop UI, Model Routing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Sharing | Analytics, Memory & Failover |
| **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Desktop UI | Model Routing |
| **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | Billing | Analytics, Analytics |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Memory & Failover | Desktop UI, Model Routing |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Analytics, Memory & Failover |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | MCP & Security | Isolation & Teams |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Failover | Desktop UI, Memory & Failover |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Desktop UI | Desktop UI |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Isolation & Teams | Analytics, MCP & Security |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI, Memory & Failover |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | Desktop UI | Desktop UI |
| **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Memory & Failover | Desktop UI |
| **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Isolation & Teams | Analytics, Desktop UI |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Mobile | Failover, MCP & Security |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Sharing | Isolation & Teams, Memory & Failover |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | Model Routing | Desktop UI, Memory & Failover |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Failover | Desktop UI, Desktop UI |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | MCP & Security | Desktop UI, Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation & Teams | Desktop UI, Mobile |
| **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | MCP & Security | Failover, Memory & Failover |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Desktop UI | Desktop UI |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI, Model Routing |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Failover, Memory & Failover |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Desktop UI, Model Routing |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Memory & Failover | Failover, Model Routing |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI, Isolation & Teams |
| **[routatic/proxy](https://github.com/routatic/proxy)** | Providers | Failover, Model Routing |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, MCP & Security |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Memory & Failover | Failover, MCP & Security |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Isolation & Teams | Analytics, Billing |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Sharing | Desktop UI, Model Routing |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | MCP & Security |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Memory & Failover | MCP & Security, Sharing |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Isolation & Teams | MCP & Security, Providers |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics, Analytics |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Mobile | MCP & Security |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI, Model Routing |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Memory & Failover |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | MCP & Security | Desktop UI, Desktop UI |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Model Routing | Desktop UI |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Billing | Analytics, Mobile |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Failover, Memory & Failover |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Memory & Failover | Desktop UI, Model Routing |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation & Teams | Desktop UI, MCP & Security |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP & Security | Desktop UI, Model Routing |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Billing | Desktop UI, Failover |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | MCP & Security, Sharing |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Memory & Failover | Failover |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | MCP & Security | Model Routing |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Billing | Analytics, Model Routing |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Isolation & Teams | Desktop UI, MCP & Security |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Sharing | Isolation & Teams, Mobile |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Desktop UI |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Isolation & Teams, Memory & Failover |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Memory & Failover | Isolation & Teams, MCP & Security |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Memory & Failover | Desktop UI, Model Routing |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Memory & Failover | Desktop UI |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Analytics, Providers |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Analytics | Isolation & Teams, MCP & Security |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Billing | Analytics, Sharing |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Analytics, MCP & Security |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Mobile | Analytics, Failover |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Isolation & Teams, MCP & Security |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Memory & Failover | Desktop UI, Failover |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Analytics, Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Sharing | Analytics, MCP & Security |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation & Teams | Desktop UI, MCP & Security |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Billing | Failover, Sharing |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Memory & Failover | Desktop UI, Failover |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Sharing | MCP & Security, Memory & Failover |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Isolation & Teams, Memory & Failover |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Isolation & Teams | Desktop UI, Providers |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | Sharing | Analytics |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Isolation & Teams | Analytics, Sharing |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Memory & Failover | Failover, MCP & Security |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | MCP & Security | Isolation & Teams |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI, Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Failover | Memory & Failover, Sharing |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Memory & Failover | Failover |
| **[IBM/mcp](https://github.com/IBM/mcp)** | MCP & Security | Desktop UI, Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.23x the stars (35,914 vs 154,149) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 12.45x the stars (4,022 vs 323) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 27.19x the stars (12,017 vs 442) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.99x the stars (19,955 vs 2,497) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.45x the stars (34,261 vs 383) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 38.83x the stars (35,914 vs 925) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 151.79x the stars (49,634 vs 327) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.84x the stars (34,261 vs 930) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.24x the stars (49,634 vs 367) | 🤖 auto (high) |
| **[Tencent/BrowserSkill](https://github.com/tencent/browserskill)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 14.86x the stars (154,149 vs 10,373) | 🤖 auto (high) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 322.51x the stars (113,522 vs 352) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 99.79x the stars (30,335 vs 304) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.44x the stars (141,427 vs 4,972) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.27x the stars (49,634 vs 3,741) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 9.33x the stars (12,017 vs 1,288) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.30x the stars (12,017 vs 2,269) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.15x the stars (49,634 vs 370) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.75x the stars (12,017 vs 418) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.81x the stars (23,964 vs 491) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.59x the stars (49,634 vs 319) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | 11.99x the stars (5,997 vs 500) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 482.02x the stars (302,226 vs 627) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.17x the stars (154,149 vs 9,535) | 🤖 auto (high) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 23.13x the stars (34,261 vs 1,481) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 35.26x the stars (19,955 vs 566) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.43x the stars (302,226 vs 6,241) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 85.44x the stars (34,261 vs 401) | 🤖 auto (high) |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 4.15x the stars (4,022 vs 970) | 🤖 auto (high) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 3.65x the stars (15,772 vs 4,316) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 100.52x the stars (141,427 vs 1,407) | 🤖 auto (high) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 7.23x the stars (113,522 vs 15,694) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.19x the stars (12,017 vs 2,868) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 2.94x the stars (1,705 vs 580) | 🤖 auto (high) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.20x the stars (30,335 vs 1,872) | 🤖 auto (medium) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 32.72x the stars (19,008 vs 581) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.46x the stars (23,964 vs 5,370) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.35x the stars (1,426 vs 426) | 🤖 auto (medium) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.61x the stars (1,426 vs 547) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 11.59x the stars (19,008 vs 1,640) | 🤖 auto (high) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.32x the stars (1,181 vs 508) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.59x the stars (1,426 vs 550) | 🤖 auto (medium) |
| **[google/artemis](https://github.com/google/artemis)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 9.67x the stars (168,031 vs 17,374) | 🤖 auto (high) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 25.23x the stars (302,226 vs 11,980) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.65x the stars (1,426 vs 866) | 🤖 auto (high) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.27x the stars (963 vs 759) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,092 vs 514) | 🤖 auto (medium) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,634 vs 27,954) | 🤖 auto (medium) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.62x the stars (792 vs 488) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui-2 | 28k | 🔻 Superseded | 1.78x the stars (49,634 vs 27,954) |
| **[google/artemis](https://github.com/google/artemis)** | mobile | 17.4k | 🔻 Superseded | 9.67x the stars (168,031 vs 17,374) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | isolation-teams | 15.7k | 🔻 Superseded | 7.23x the stars (113,522 vs 15,694) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | sharing | 12k | 🔻 Superseded | 25.23x the stars (302,226 vs 11,980) |
| **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | failover | 10.4k | 🔻 Superseded | 14.86x the stars (154,149 vs 10,373) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | failover | 9.5k | 🔻 Superseded | 16.17x the stars (154,149 vs 9,535) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | sharing | 6.2k | 🔻 Superseded | 48.43x the stars (302,226 vs 6,241) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.4k | 🔻 Superseded | 4.46x the stars (23,964 vs 5,370) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-teams | 5k | 🔻 Superseded | 28.44x the stars (141,427 vs 4,972) |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | sharing | 4.3k | 🔻 Superseded | 3.65x the stars (15,772 vs 4,316) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui-2 | 3.7k | 🔻 Superseded | 13.27x the stars (49,634 vs 3,741) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | sharing | 2.9k | 🔻 Superseded | 4.19x the stars (12,017 vs 2,868) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 Superseded | 7.99x the stars (19,955 vs 2,497) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | sharing | 2.3k | 🔻 Superseded | 5.30x the stars (12,017 vs 2,269) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | sharing | 1.9k | 🔻 Superseded | 16.20x the stars (30,335 vs 1,872) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | memory-failover | 1.6k | 🔻 Superseded | 11.59x the stars (19,008 vs 1,640) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation-teams | 1.5k | 🔻 Superseded | 23.13x the stars (34,261 vs 1,481) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | isolation-teams | 1.4k | 🔻 Superseded | 100.52x the stars (141,427 vs 1,407) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | sharing | 1.3k | 🔻 Superseded | 9.33x the stars (12,017 vs 1,288) |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | billing | 970 | 🔻 Superseded | 4.15x the stars (4,022 vs 970) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-teams | 930 | 🔻 Superseded | 36.84x the stars (34,261 vs 930) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 925 | 🔻 Superseded | 38.83x the stars (35,914 vs 925) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | memory-failover | 866 | 🔻 Superseded | 1.65x the stars (1,426 vs 866) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui-2 | 759 | 🔻 Superseded | 1.27x the stars (963 vs 759) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | sharing | 627 | 🔻 Superseded | 482.02x the stars (302,226 vs 627) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | memory-failover | 581 | 🔻 Superseded | 32.72x the stars (19,008 vs 581) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-teams | 580 | 🔻 Superseded | 2.94x the stars (1,705 vs 580) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | billing | 566 | 🔻 Superseded | 35.26x the stars (19,955 vs 566) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-failover | 550 | 🔻 Superseded | 2.59x the stars (1,426 vs 550) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | memory-failover | 547 | 🔻 Superseded | 2.61x the stars (1,426 vs 547) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui-2 | 514 | 🔻 Superseded | 2.12x the stars (1,092 vs 514) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | mcp-security | 508 | 🔻 Superseded | 2.32x the stars (1,181 vs 508) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-security | 500 | 🔻 Superseded | 11.99x the stars (5,997 vs 500) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 491 | 🔻 Superseded | 48.81x the stars (23,964 vs 491) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | memory-failover | 488 | 🔻 Superseded | 1.62x the stars (792 vs 488) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | sharing | 442 | 🔻 Superseded | 27.19x the stars (12,017 vs 442) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | memory-failover | 426 | 🔻 Superseded | 3.35x the stars (1,426 vs 426) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | sharing | 418 | 🔻 Superseded | 28.75x the stars (12,017 vs 418) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | isolation-teams | 401 | 🔻 Superseded | 85.44x the stars (34,261 vs 401) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-teams | 383 | 🔻 Superseded | 89.45x the stars (34,261 vs 383) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui-2 | 370 | 🔻 Superseded | 134.15x the stars (49,634 vs 370) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui-2 | 367 | 🔻 Superseded | 135.24x the stars (49,634 vs 367) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | isolation-teams | 352 | 🔻 Superseded | 322.51x the stars (113,522 vs 352) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | desktop-ui-2 | 327 | 🔻 Superseded | 151.79x the stars (49,634 vs 327) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 323 | 🔻 Superseded | 12.45x the stars (4,022 vs 323) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui-2 | 319 | 🔻 Superseded | 155.59x the stars (49,634 vs 319) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | sharing | 304 | 🔻 Superseded | 99.79x the stars (30,335 vs 304) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-13 12:15 UTC. 230 live tools · 123 candidates rejected by the quality gates.</sub>
