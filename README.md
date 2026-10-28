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

**212 tools** across **12 categories** · **61 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-28 10:38 UTC**

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

- [Desktop UI](#desktop-ui) — 43 tools
- [Memory & MCP](#memory-mcp) — 18 tools
- [Mobile & Remote Control](#mobile-remote-control) — 24 tools
- [Security & MCP](#security-mcp) — 28 tools
- [Isolation](#isolation) — 18 tools
- [Model Routing](#model-routing) — 15 tools
- [Sharing](#sharing) — 15 tools
- [Failover](#failover) — 13 tools
- [Billing](#billing) — 13 tools
- [Desktop UI](#desktop-ui) — 10 tools
- [Providers](#providers) — 8 tools
- [Analytics](#analytics) — 7 tools
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
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | ✅ | 178.6k 🚀 +876/d | **87** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Taste Skill is an Agent Skill that makes coding agents design websites and app screens instead of assembling the average landing page. | 🟢 Easy | — | — | 104k 🚀 +526/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 21.7k 🚀 +454/d | **83** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 50.8k 🚀 +2073/d | **82** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 14.3k 🚀 +229/d | **82** |
| 🏆 **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 5.6k 🚀 +125/d | **79** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 4.9k 🚀 +152/d | **77** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.1k 🚀 +28/d | **70** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 5k 🚀 +82/d | **68** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 27.5k 🚀 +30/d | **67** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 10.4k 🚀 +44/d | **66** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 4.1k 🚀 +47/d | **64** |
| ✅ **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 3.8k 🚀 +26/d | **62** |
| 🔹 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.7k 🚀 +7/d | **61** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +17/d | **61** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.2k 🚀 +26/d | **60** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | An open skill for agent-to-agent contracts. | 🟢 Easy | — | — | 7k 🚀 +12/d | **59** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4k 🚀 +28/d | **59** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | Claude Codeは仕様駆動の夢を見ない (Speaker Deck, Japanese) Kiroの仕様書駆動開発プロセスをClaude Codeで徹底的に再現した (Zenn, Japanese) | 🟢 Easy | — | — | 3.7k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.7k | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **56** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 905 🚀 +5/d | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 541 | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 512 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) External-content sanitizing (leyline) strips invisible | 🟢 Easy | — | — | 343 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **52** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CR… | 🟡 Some setup | — | — | 368 | **52** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [garrytan/gstack](https://github.com/garrytan/gstack), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code) *(+24 more)*

*…and 13 more in [the full index](data/index.json).*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **178,569** (+875.6/day over 5d)
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

- Stars: **103,964** (+526.2/day over 5d)
- Health score: **86/100**
- Documentation score: **33/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-28
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

- Stars: **21,658** (+454.4/day over 5d)
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

- Stars: **50,799** (+2073.4/day over 5d)
- Health score: **82/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

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

- Stars: **14,257** (+229.2/day over 5d)
- Health score: **82/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-17
- Works with: Claude Code, Codex

</details>

## Memory & MCP

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 291.3k 🚀 +894/d | **89** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 17.2k 🚀 +799/d | **87** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Website: aimemory.sh | 🟡 Some setup | — | — | 14.2k 🚀 +264/d | **84** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 11.2k 🚀 +90/d | **81** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 6.4k 🚀 +84/d | **79** |
| 🏆 **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 47.7k 🚀 +81/d | **79** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30k 🚀 +30/d | **71** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 32.8k 🚀 +31/d | **69** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.8k 🚀 +6/d | **67** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 8.8k 🚀 +68/d | **66** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17k 🚀 +74/d | **66** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.7k 🚀 +6/d | **63** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | Try, compare, contribute: First-run reports · Context-compression evaluation note · Contribution guide | 🟢 Turnkey | — | — | 265 🚀 +12/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k 🚀 +6/d | **56** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 414 | **54** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 433 | **51** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 247 | **45** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [cordum-io/cordum](https://github.com/cordum-io/cordum), [crshdn/mission-control](https://github.com/crshdn/mission-control), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside), [solo-agent/solo](https://github.com/solo-agent/solo), [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)

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

- Stars: **291,279** (+894.4/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-26
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **17,236** (+799.0/day over 5d)
- Health score: **87/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-28
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

- Stars: **14,195** (+263.8/day over 5d)
- Health score: **84/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-27
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

- Stars: **11,237** (+89.8/day over 5d)
- Health score: **81/100**
- Documentation score: **79/100**
- License: MIT
- Language: Python
- Last push: 2026-10-28
- Works with: Claude Code, Codex, OpenCode

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

- Stars: **6,424** (+84.4/day over 5d)
- Health score: **79/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-28
- Works with: Claude Code

</details>

## Mobile & Remote Control

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 164.7k 🚀 +256/d | **98** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 108.5k 🚀 +1057/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 108.1k 🚀 +359/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 22.3k 🚀 +99/d | **82** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 15.3k 🚀 +290/d | **82** |
| 🏆 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3.3k 🚀 +104/d | **79** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 6.6k 🚀 +74/d | **76** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 5.8k 🚀 +69/d | **75** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 84.5k 🚀 +46/d | **75** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 3.5k 🚀 +96/d | **68** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 11.1k 🚀 +19/d | **67** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Crew works without Obsidian. | 🟢 Easy | — | — | 5k 🚀 +29/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.4k 🚀 +19/d | **65** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟡 Some setup | — | — | 5.4k 🚀 +8/d | **63** |
| 🔹 **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.5k 🚀 +12/d | **60** |
| 🔹 **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 970 | **58** |
| 🔹 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 908 🚀 +12/d | **56** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 288 | **56** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.6k 🚀 +10/d | **54** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **51** |
| 🔹 **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | ~100 skills for Claude Code — meeting pipelines, research, image generation, TDD, publishing, personal analytics, and Claude Code ops. | 🟢 Easy | — | — | 401 | **51** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 304 | **49** |

**Also does this:** [makecindy/cindy](https://github.com/makecindy/cindy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

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

- Stars: **164,657** (+255.6/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-25
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **108,511** (+1056.8/day over 5d)
- Health score: **92/100**
- Documentation score: **52/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28
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

- Stars: **108,140** (+359.2/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28
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

- Stars: **22,260** (+99.2/day over 5d)
- Health score: **82/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

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

- Stars: **15,338** (+290.0/day over 5d)
- Health score: **82/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

</details>

## Security & MCP

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 21.3k 🚀 +211/d | **88** |
| 🏆 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 7.7k 🚀 +224/d | **79** |
| ✅ **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 3.1k 🚀 +58/d | **74** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 15.1k 🚀 +57/d | **72** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **61** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.4k 🚀 +15/d | **61** |
| 🔹 **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | English: README.en.md \| 中文: README.md | 🔴 Involved | — | — | 3.2k 🚀 +49/d | **60** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.8k | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **57** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.2k 🚀 +8/d | **57** |
| 🔹 **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | 111 MCP tools · 59 RE/debug backends · 4,200+ skills · multi-agent mesh · zero-dep native parsers | 🟢 Easy | — | — | 393 🚀 +17/d | **57** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.1k | **55** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 785 | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 469 | **55** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Easy · OOTB | ✅ | — | 531 🚀 +8/d | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 385 | **54** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 716 | **52** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | ⚠️ This project includes production-ready security features but is still under active development. | 🟡 Some setup | — | — | 372 | **52** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 330 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 497 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **51** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 550 | **49** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | This repository is essentially an LLM chat desktop application based on MCP. Windows: The MCP SDK includes a workaround specifically for Windows systems, as documented in ISSUE 101. | 🟢 Easy | — | ✅ | 1.2k | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 475 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 417 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [affaan-m/ECC](https://github.com/affaan-m/ECC), [garrytan/gstack](https://github.com/garrytan/gstack), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [superdesigndev/treg](https://github.com/superdesigndev/treg), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [aipoch/open-science](https://github.com/aipoch/open-science) *(+14 more)*

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

- Stars: **21,271** (+210.6/day over 5d)
- Health score: **88/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-28

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

- Stars: **7,690** (+224.2/day over 5d)
- Health score: **79/100**
- Documentation score: **43/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-27
- Works with: Claude Code, Cursor

#### [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

> Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output.

**Core problems it solves**

- **Automatic failover** — *It falls back to the CPU encoder — reported in the result's hw.fallback/hw.notes — only when VideoToolbox itself refuses a job (any other ffmpeg fail…*
- **Multi-agent orchestration** — *contract and the test suite (tests/testcontract.py,*
- **API gateway / proxy** — *GB source is converted to BT.709, not relabelled); --normalize meets the platform's loudness in the same call (render.py turns it on by default for p…*
- **Skills & plugins** — *uploaded; parakeet-mlx, faster-whisper and openai-whisper download their model weights the first time they run (parakeet-mlx's default from Hugging F…*
- **Agent runtime** — *Give your coding agent a video editor.*
- **MCP support** — *Give your coding agent a video editor.*
- **Security & isolation** — *re recorded in diagnostics and on stderr (codes: jsonoutput.diagnosticcodes); tools that draw text name the font they drew with (fontused).*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx ffmpeg-skill`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via npx one-liner, Homebrew install

**Facts**

- Stars: **3,129** (~57.9/day lifetime average)
- Health score: **74/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-10-28
- Works with: Claude Code, Codex, Cursor

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

- Stars: **15,147** (+56.6/day over 5d)
- Health score: **72/100**
- Documentation score: **50/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-26
- Works with: Codex

#### [getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)

> A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

**Core problems it solves**

- **Agent runtime** — *T Node.js Xcode 16 macOS MCP Ask DeepWiki AgentAudit Security pkg.pr.new*
- **MCP support** — *A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `brew tap getsentry/xcodebuildmcp`
- Platforms mentioned: macOS, iOS
- Turnkey. install via npx one-liner, Homebrew install; needs npm install/build

**Facts**

- Stars: **6,512** (+1.8/day over 5d)
- Health score: **61/100**
- Documentation score: **48/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Cursor

</details>

## Isolation

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🔴 Involved | — | — | 138k 🚀 +131/d | **88** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.8k 🚀 +25/d | **72** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.7k 🚀 +25/d | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.5k 🚀 +24/d | **68** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 8.4k 🚀 +30/d | **65** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **59** |
| 🔹 **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 1.5k (+9/d) | **59** |
| 🔹 **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | Give ChatGPT a secure connection to your own machine and Turn ChatGPT into Codex | 🟢 Easy | — | — | 5.3k | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **58** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.6k 🚀 +10/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 584 | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 584 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 460 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 320 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 788 | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **51** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 320 | **48** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [getpaseo/paseo](https://github.com/getpaseo/paseo), [spinabot/brigade](https://github.com/spinabot/brigade), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun), [crshdn/mission-control](https://github.com/crshdn/mission-control), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)

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

- Stars: **138,001** (+131.2/day over 5d)
- Health score: **88/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

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

- Stars: **33,848** (+25.2/day over 5d)
- Health score: **72/100**
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

- Stars: **27,726** (+24.6/day over 5d)
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

- Stars: **9,531** (+24.4/day over 5d)
- Health score: **68/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-10-28
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

- Stars: **8,367** (+29.8/day over 5d)
- Health score: **65/100**
- Documentation score: **52/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-28
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Model Routing

*Quota sharing / splitting*

A subscription's capacity is larger than one person needs; share it safely with others.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 104.5k 🚀 +208/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | ✅ | 78.1k 🚀 +275/d | **91** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 153.7k 🚀 +142/d | **90** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 11.2k 🚀 +112/d | **84** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | A toolbox of film styles made in code: 59 ready to use, and your own. Default output 1920×1080, 24 fps; other sizes on request. | 🟡 Some setup | — | ✅ | 8.9k 🚀 +605/d | **83** |
| 🏆 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 3.8k 🚀 +147/d | **78** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.5k 🚀 +38/d | **67** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 10.9k 🚀 +49/d | **67** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.3k 🚀 +36/d | **66** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.2k 🚀 +11/d | **59** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.9k 🚀 +10/d | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 344 | **53** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.6k | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 713 | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 557 | **46** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) *(+2 more)*

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

- Stars: **104,508** (+208.4/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **78,068** (+275.2/day over 5d)
- Health score: **91/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **153,668** (+141.8/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **11,162** (+112.2/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **8,914** (+605.0/day over 5d)
- Health score: **83/100**
- Documentation score: **55/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-24
- Works with: Claude Code, Cursor

</details>

## Sharing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 24.3k 🚀 +879/d | **89** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 131.4k 🚀 +166/d | **89** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 31.6k 🚀 +59/d | **72** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 10.1k 🚀 +53/d | **70** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 19.4k 🚀 +35/d | **69** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 31 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 18k 🚀 +38/d | **67** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k | **56** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.6k 🚀 +14/d | **55** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.8k 🚀 +11/d | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 505 | **52** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 267 | **52** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 908 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 312 | **51** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 392 🚀 +16/d | **49** |
| 🔹 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | Built with C++ / Win32 / WebView2 for stability and speed. Quota dashboard, auto-refresh (5H / 7D), low-quota alerts and switch prompts | 🟡 Some setup | — | — | 250 | **45** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [cita-777/metapi](https://github.com/cita-777/metapi), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

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

- Stars: **24,309** (+879.4/day over 5d)
- Health score: **89/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-10-28
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

- Stars: **131,373** (+165.6/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-28
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

- Stars: **31,560** (+58.6/day over 5d)
- Health score: **72/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-28
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

- Stars: **10,121** (+53.2/day over 5d)
- Health score: **70/100**
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

- Stars: **19,443** (+35.4/day over 5d)
- Health score: **69/100**
- Documentation score: **61/100**
- Language: Rust
- Last push: 2026-10-27
- Works with: Codex, OpenCode, Cursor, Copilot

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 149.6k 🚀 +344/d | **93** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 4.4k 🚀 +95/d | **83** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.6k 🚀 +15/d | **67** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi is a fast, self-contained terminal AI coding agent. | 🟢 Easy | — | — | 3.2k 🚀 +38/d | **66** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.8k 🚀 +15/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.4k 🚀 +5/d | **58** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 5.1k 🚀 +6/d | **56** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 440 | **52** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 288 | **51** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.8k 🚀 +9/d | **50** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 676 | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 314 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 522 | **43** |

**Also does this:** [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

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

- Stars: **149,625** (+344.2/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-28
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

- Stars: **4,386** (+94.8/day over 5d)
- Health score: **83/100**
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

- Stars: **27,586** (+15.4/day over 5d)
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

- Stars: **3,203** (~37.7/day lifetime average)
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

- Stars: **1,829** (+15.0/day over 5d)
- Health score: **62/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 62.2k 🚀 +392/d | **90** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 45k 🚀 +69/d | **75** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 10.8k 🚀 +30/d | **64** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.7k 🚀 +22/d | **56** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 549 🚀 +18/d | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 423 | **54** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 直接找：接口一览 ｜ 五分钟上手 ｜ 易支付协议兼容接入 ｜ 到账账号与收款分配 ｜ 文档目录 ｜ 常见问题 | 🟢 Easy | — | — | 323 | **52** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 821 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 407 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 436 | **43** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 242 | **39** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [decolua/9router](https://github.com/decolua/9router), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [spinabot/brigade](https://github.com/spinabot/brigade), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [erickochen/purple](https://github.com/erickochen/purple), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [Licoy/Quosparr](https://github.com/Licoy/Quosparr), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **62,160** (+392.4/day over 5d)
- Health score: **90/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-10-27
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

- Stars: **45,011** (+68.6/day over 5d)
- Health score: **75/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-28
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

- Stars: **10,833** (+29.6/day over 5d)
- Health score: **64/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-27
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

- Stars: **11,728** (+22.2/day over 5d)
- Health score: **56/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28

#### [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

> 简体中文 · English · 版本下载 · 问题反馈

**Core problems it solves**

- **Multi-account switching** — *Desktop 可在客户端内登录，也可选择 API / 第三方连接进入原生 Code / Cowork。*
- **Quota & usage management** — *Responses 的 imagegeneration 工具，两种上游路径独立。*
- **Workspace isolation**
- **Multi-provider aggregation**
- **API gateway / proxy** — *受管 Claude CLI 实例可使用管理器刷新后的订阅访问凭据；刷新令牌留在管理器安全存储，不写入实例。*
- **Billing & metering** — *CLI 实例时，自动补齐本机 ~/.codex/skills 中的个人技能入口，已有实例和会话副本同样适用。*
- **Agent runtime**
- **MCP support** — *ock / Vertex / Foundry 等云模式和 npm 包装启动器尚未接入。*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 45/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx electron-builder --mac --arm64 --publish never`
- Platforms mentioned: macOS, Windows, Linux
- Some setup. install via npx one-liner; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow; GUI application

**Facts**

- Stars: **549** (+17.6/day over 5d)
- Health score: **55/100**
- Documentation score: **58/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-27
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 222.5k 🚀 +434/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 11.4k 🚀 +390/d | **88** |
| ✅ **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 3.3k 🚀 +304/d | **75** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | Turn the browser you already use into a workspace for your AI agent. | 🟢 Easy | — | — | 9.7k 🚀 +57/d | **71** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.2k 🚀 +17/d | **63** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 476 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 772 | **53** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | Scope Recall v3 is a bounded local memory core with SQLite as the authority and rebuildable vector companions. | 🟢 Easy | — | — | 492 🚀 +8/d | **53** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. The domain model is Genesys-lineage. | 🟡 Some setup | — | — | 441 🚀 +21/d | **53** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [yetone/magpie](https://github.com/yetone/magpie), [xerj-org/xerj](https://github.com/xerj-org/xerj), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [getpaseo/paseo](https://github.com/getpaseo/paseo), [google/artemis](https://github.com/google/artemis), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) *(+56 more)*

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

- Stars: **222,549** (+433.8/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28
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

- Stars: **11,424** (+389.8/day over 5d)
- Health score: **88/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-28
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

- Stars: **3,339** (~303.6/day lifetime average)
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

- Stars: **9,718** (+57.0/day over 5d)
- Health score: **71/100**
- Documentation score: **60/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-28
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

- Stars: **15,223** (+17.0/day over 5d)
- Health score: **63/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.1k 🚀 +25/d | **68** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 876 | **56** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.3k 🚀 +6/d | **55** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 984 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 762 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 434 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 510 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 597 | **45** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

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

- Stars: **4,146** (+24.8/day over 5d)
- Health score: **68/100**
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

- Stars: **876** (+3.8/day over 5d)
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

- Stars: **4,329** (+6.4/day over 5d)
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

- Stars: **984** (+0.1/day over 19d)
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

- Stars: **762** (+1.4/day over 5d)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-27
- Works with: Claude Code, Cursor

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 50.9k 🚀 +72/d | **73** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 7.8k 🚀 +80/d | **71** |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | The local-first harness & workspace for research agents. | 🟢 Turnkey · OOTB | ✅ | — | 7.6k 🚀 +28/d | **65** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 15.2k 🚀 +15/d | **65** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [superdesigndev/treg](https://github.com/superdesigndev/treg), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [decolua/9router](https://github.com/decolua/9router), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher), [cita-777/metapi](https://github.com/cita-777/metapi), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

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

- Stars: **50,867** (+72.2/day over 21d)
- Health score: **73/100**
- Documentation score: **75/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-28

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

- Stars: **7,792** (~80.3/day lifetime average)
- Health score: **71/100**
- Documentation score: **54/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-28
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

- Stars: **7,622** (+27.8/day over 5d)
- Health score: **65/100**
- Documentation score: **33/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-28
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

- Stars: **15,207** (+15.4/day over 5d)
- Health score: **65/100**
- Documentation score: **57/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-28
- Works with: Claude Code

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

- Stars: **5,923** (+2.4/day over 5d)
- Health score: **51/100**
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile & Remote Control | Billing, Desktop UI |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Model Routing | Desktop UI, Security & MCP |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Failover | Billing, Providers |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile & Remote Control | Isolation, Sharing |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Desktop UI, Model Routing |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Memory & MCP | Desktop UI, Security & MCP |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile & Remote Control | Analytics, Memory & MCP |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Isolation | Desktop UI, Security & MCP |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Memory & MCP | Desktop UI |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Memory & MCP | Model Routing, Security & MCP |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Model Routing | Analytics, Memory & MCP |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI |
| **[google/artemis](https://github.com/google/artemis)** | Mobile & Remote Control | Desktop UI |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Memory & MCP | Desktop UI, Desktop UI |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Memory & MCP | Analytics, Security & MCP |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Mobile & Remote Control | Desktop UI, Sharing |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Memory & MCP | Desktop UI, Desktop UI |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Analytics, Sharing |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile & Remote Control | Analytics, Desktop UI |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Mobile & Remote Control | Failover, Memory & MCP |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Security & MCP | Desktop UI, Desktop UI |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Analytics | Model Routing |
| **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Security & MCP | Desktop UI |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Isolation | Desktop UI, Desktop UI |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Analytics, Billing |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Desktop UI, Mobile & Remote Control |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Memory & MCP | Desktop UI, Security & MCP |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation | Desktop UI, Security & MCP |
| **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Desktop UI | Desktop UI |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Billing, Model Routing |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Model Routing |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Desktop UI, Model Routing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | Memory & MCP, Security & MCP |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Mobile & Remote Control | Desktop UI, Model Routing |
| **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | Desktop UI | Desktop UI |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | Failover | Security & MCP |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile & Remote Control | Desktop UI, Model Routing |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile & Remote Control | Desktop UI |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Analytics | Failover, Security & MCP |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | Desktop UI, Model Routing |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Memory & MCP | Desktop UI, Security & MCP |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Mobile & Remote Control | Desktop UI, Security & MCP |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | Security & MCP | Model Routing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Memory & MCP | Billing, Isolation |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile & Remote Control | Desktop UI |
| **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | Security & MCP | Desktop UI, Model Routing |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | Desktop UI | Desktop UI |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Security & MCP | Desktop UI, Model Routing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation | Desktop UI, Security & MCP |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Isolation | Desktop UI, Desktop UI |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | Isolation | Desktop UI |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Failover | Desktop UI, Desktop UI |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Isolation | Analytics, Security & MCP |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile & Remote Control | Desktop UI, Security & MCP |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Isolation | Desktop UI, Security & MCP |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Desktop UI | Desktop UI |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | Security & MCP | Desktop UI, Desktop UI |
| **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | Memory & MCP | Desktop UI |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Failover | Desktop UI |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Memory & MCP | Desktop UI |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile & Remote Control | Analytics, Isolation |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation | Desktop UI, Mobile & Remote Control |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Isolation | Desktop UI, Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Mobile & Remote Control | Billing, Desktop UI |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Desktop UI |
| **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Desktop UI | Desktop UI |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Security & MCP | Desktop UI, Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Security & MCP | Desktop UI, Memory & MCP |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Providers, Sharing |
| **[oracle/mcp](https://github.com/oracle/mcp)** | Security & MCP | Desktop UI |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Isolation | Desktop UI, Desktop UI |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Isolation | Desktop UI, Failover |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Billing, Security & MCP |
| **[0sec-labs/0](https://github.com/0sec-labs/0)** | Security & MCP | Desktop UI |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Billing | Desktop UI, Memory & MCP |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | Security & MCP | Desktop UI, Desktop UI |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation | Desktop UI, Desktop UI |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Security & MCP |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Security & MCP | Desktop UI, Desktop UI |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Memory & MCP, Security & MCP |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Sharing | Desktop UI |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Failover | Security & MCP |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | Security & MCP | Desktop UI |
| **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | Billing | Sharing |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile & Remote Control | Isolation, Security & MCP |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Billing, Sharing |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Mobile & Remote Control, Security & MCP |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile & Remote Control | Isolation, Security & MCP |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation | Desktop UI, Security & MCP |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile & Remote Control | Desktop UI, Isolation |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Analytics | Providers, Security & MCP |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Memory & MCP | Desktop UI, Security & MCP |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | Mobile & Remote Control | Desktop UI, Desktop UI |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Sharing | Billing, Desktop UI |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Failover | Desktop UI |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Isolation, Memory & MCP |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Failover | Desktop UI |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Sharing | Analytics, Billing |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Mobile & Remote Control | Isolation, Memory & MCP |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Billing | Desktop UI, Isolation |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Isolation | Memory & MCP |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | Security & MCP | Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Security & MCP | Desktop UI |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Model Routing | Analytics, Failover |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Security & MCP | Desktop UI |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | Desktop UI | Desktop UI |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | Security & MCP | Desktop UI |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI, Memory & MCP |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Security & MCP | Desktop UI, Desktop UI |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Memory & MCP | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Failover | Memory & MCP, Model Routing |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Billing | Model Routing, Sharing |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.16x the stars (24,309 vs 149,625) |

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
| **[AVIDS2/memorix](https://github.com/avids2/memorix)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 332.89x the stars (291,279 vs 875) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 59.46x the stars (19,443 vs 327) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 25.54x the stars (11,237 vs 440) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 20.13x the stars (11,094 vs 551) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.06x the stars (19,443 vs 2,411) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.07x the stars (33,848 vs 380) | 🤖 auto (high) |
| **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 70.68x the stars (29,967 vs 424) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 564.49x the stars (291,279 vs 516) | 🤖 auto (high) |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/memtensor/memos-cloud-openclaw-plugin)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 81.43x the stars (29,967 vs 368) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.22x the stars (11,237 vs 2,153) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.51x the stars (33,848 vs 927) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 3.90x the stars (1,108 vs 284) | 🤖 auto (high) |
| **[YYHDBL/AgentCrew](https://github.com/yyhdbl/agentcrew)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 117.98x the stars (29,967 vs 254) | 🤖 auto (high) |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 54.16x the stars (33,848 vs 625) | 🤖 auto (high) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 164.56x the stars (291,279 vs 1,770) | 🤖 auto (high) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 222.36x the stars (104,508 vs 470) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 98.11x the stars (33,848 vs 345) | 🤖 auto (high) |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 574.51x the stars (291,279 vs 507) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.60x the stars (27,726 vs 4,952) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 8.70x the stars (11,162 vs 1,283) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.08x the stars (11,237 vs 2,212) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.89x the stars (11,237 vs 376) | 🤖 auto (high) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 32.89x the stars (29,967 vs 911) | 🤖 auto (high) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 166.15x the stars (104,508 vs 629) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 47.26x the stars (22,260 vs 471) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 630.87x the stars (164,657 vs 261) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.64x the stars (33,848 vs 276) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 472.09x the stars (291,279 vs 617) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.32x the stars (149,625 vs 9,167) | 🤖 auto (high) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 101.25x the stars (108,140 vs 1,068) | 🤖 auto (high) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 16.85x the stars (11,237 vs 667) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 34.97x the stars (19,443 vs 556) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 5.22x the stars (1,466 vs 281) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 12.41x the stars (17,236 vs 1,389) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 13.33x the stars (11,237 vs 843) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.66x the stars (291,279 vs 6,111) | 🤖 auto (high) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 105.89x the stars (29,967 vs 283) | 🤖 auto (high) |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 162.54x the stars (291,279 vs 1,792) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 608.10x the stars (291,279 vs 479) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 4.14x the stars (5,814 vs 1,404) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.01x the stars (11,237 vs 2,802) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.49x the stars (11,237 vs 1,323) | 🤖 auto (medium) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.93x the stars (905 vs 309) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.22x the stars (27,726 vs 575) | 🤖 auto (medium) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 24.32x the stars (33,848 vs 1,392) | 🤖 auto (high) |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 41.11x the stars (29,967 vs 729) | 🤖 auto (medium) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 6.21x the stars (3,129 vs 504) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.10x the stars (1,323 vs 427) | 🤖 auto (medium) |
| **[yetone/cumora](https://github.com/yetone/cumora)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 2.75x the stars (11,094 vs 4,033) | 🤖 auto (high) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 38.87x the stars (291,279 vs 7,494) | 🤖 auto (medium) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 20.43x the stars (11,237 vs 550) | 🤖 auto (medium) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.48x the stars (905 vs 365) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.32x the stars (1,125 vs 485) | 🤖 auto (high) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.77x the stars (22,260 vs 5,912) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.21x the stars (905 vs 409) | 🤖 auto (high) |
| **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 3.91x the stars (29,967 vs 7,662) | 🤖 auto (high) |
| **[Dataojitori/nocturne_memory](https://github.com/dataojitori/nocturne_memory)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 8.05x the stars (11,362 vs 1,412) | 🤖 auto (high) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.20x the stars (905 vs 755) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.16x the stars (1,073 vs 496) | 🤖 auto (medium) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.20x the stars (1,125 vs 512) | 🤖 auto (high) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.18x the stars (320 vs 272) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | failover | 9.2k | 🔻 Superseded | 16.32x the stars (149,625 vs 9,167) |
| **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | memory-mcp | 7.7k | 🔻 Superseded | 3.91x the stars (29,967 vs 7,662) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | memory-mcp | 7.5k | 🔻 Superseded | 38.87x the stars (291,279 vs 7,494) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | memory-mcp | 6.1k | 🔻 Superseded | 47.66x the stars (291,279 vs 6,111) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | mobile-remote-control | 5.9k | 🔻 Superseded | 3.77x the stars (22,260 vs 5,912) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation | 5k | 🔻 Superseded | 5.60x the stars (27,726 vs 4,952) |
| **[yetone/cumora](https://github.com/yetone/cumora)** | mobile-remote-control | 4k | 🔻 Superseded | 2.75x the stars (11,094 vs 4,033) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | memory-mcp | 2.8k | 🔻 Superseded | 4.01x the stars (11,237 vs 2,802) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 Superseded | 8.06x the stars (19,443 vs 2,411) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | memory-mcp | 2.2k | 🔻 Superseded | 5.08x the stars (11,237 vs 2,212) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | memory-mcp | 2.2k | 🔻 Superseded | 5.22x the stars (11,237 vs 2,153) |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | memory-mcp | 1.8k | 🔻 Superseded | 162.54x the stars (291,279 vs 1,792) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | memory-mcp | 1.8k | 🔻 Superseded | 164.56x the stars (291,279 vs 1,770) |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | memory-mcp | 1.4k | 🔻 Superseded | 8.05x the stars (11,362 vs 1,412) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile-remote-control | 1.4k | 🔻 Superseded | 4.14x the stars (5,814 vs 1,404) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation | 1.4k | 🔻 Superseded | 24.32x the stars (33,848 vs 1,392) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | memory-mcp | 1.4k | 🔻 Superseded | 12.41x the stars (17,236 vs 1,389) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | memory-mcp | 1.3k | 🔻 Superseded | 8.49x the stars (11,237 vs 1,323) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | model-routing | 1.3k | 🔻 Superseded | 8.70x the stars (11,162 vs 1,283) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile-remote-control | 1.1k | 🔻 Superseded | 101.25x the stars (108,140 vs 1,068) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation | 927 | 🔻 Superseded | 36.51x the stars (33,848 vs 927) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | memory-mcp | 911 | 🔻 Superseded | 32.89x the stars (29,967 vs 911) |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | memory-mcp | 875 | 🔻 Superseded | 332.89x the stars (291,279 vs 875) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | memory-mcp | 843 | 🔻 Superseded | 13.33x the stars (11,237 vs 843) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 Superseded | 1.20x the stars (905 vs 755) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | memory-mcp | 729 | 🔻 Superseded | 41.11x the stars (29,967 vs 729) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | memory-mcp | 667 | 🔻 Superseded | 16.85x the stars (11,237 vs 667) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 629 | 🔻 Superseded | 166.15x the stars (104,508 vs 629) |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | isolation | 625 | 🔻 Superseded | 54.16x the stars (33,848 vs 625) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | memory-mcp | 617 | 🔻 Superseded | 472.09x the stars (291,279 vs 617) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation | 575 | 🔻 Superseded | 48.22x the stars (27,726 vs 575) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 556 | 🔻 Superseded | 34.97x the stars (19,443 vs 556) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile-remote-control | 551 | 🔻 Superseded | 20.13x the stars (11,094 vs 551) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-mcp | 550 | 🔻 Superseded | 20.43x the stars (11,237 vs 550) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | memory-mcp | 516 | 🔻 Superseded | 564.49x the stars (291,279 vs 516) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | security-mcp | 512 | 🔻 Superseded | 2.20x the stars (1,125 vs 512) |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | memory-mcp | 507 | 🔻 Superseded | 574.51x the stars (291,279 vs 507) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security-mcp | 504 | 🔻 Superseded | 6.21x the stars (3,129 vs 504) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 496 | 🔻 Superseded | 2.16x the stars (1,073 vs 496) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | security-mcp | 485 | 🔻 Superseded | 2.32x the stars (1,125 vs 485) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | memory-mcp | 479 | 🔻 Superseded | 608.10x the stars (291,279 vs 479) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile-remote-control | 471 | 🔻 Superseded | 47.26x the stars (22,260 vs 471) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 470 | 🔻 Superseded | 222.36x the stars (104,508 vs 470) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | memory-mcp | 440 | 🔻 Superseded | 25.54x the stars (11,237 vs 440) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | memory-mcp | 427 | 🔻 Superseded | 3.10x the stars (1,323 vs 427) |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | memory-mcp | 424 | 🔻 Superseded | 70.68x the stars (29,967 vs 424) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 409 | 🔻 Superseded | 2.21x the stars (905 vs 409) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation | 380 | 🔻 Superseded | 89.07x the stars (33,848 vs 380) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | memory-mcp | 376 | 🔻 Superseded | 29.89x the stars (11,237 vs 376) |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | memory-mcp | 368 | 🔻 Superseded | 81.43x the stars (29,967 vs 368) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 365 | 🔻 Superseded | 2.48x the stars (905 vs 365) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | isolation | 345 | 🔻 Superseded | 98.11x the stars (33,848 vs 345) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 Superseded | 59.46x the stars (19,443 vs 327) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 309 | 🔻 Superseded | 2.93x the stars (905 vs 309) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 Superseded | 3.90x the stars (1,108 vs 284) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | memory-mcp | 283 | 🔻 Superseded | 105.89x the stars (29,967 vs 283) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | isolation | 281 | 🔻 Superseded | 5.22x the stars (1,466 vs 281) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | isolation | 276 | 🔻 Superseded | 122.64x the stars (33,848 vs 276) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | isolation | 272 | 🔻 Superseded | 1.18x the stars (320 vs 272) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | mobile-remote-control | 261 | 🔻 Superseded | 630.87x the stars (164,657 vs 261) |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | memory-mcp | 254 | 🔻 Superseded | 117.98x the stars (29,967 vs 254) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-28 10:38 UTC. 212 live tools · 127 candidates rejected by the quality gates.</sub>
