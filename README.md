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

**227 tools** across **14 categories** · **51 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-05 12:23 UTC**

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
- [Analytics](#analytics) — 21 tools
- [Memory & MCP](#memory-mcp) — 24 tools
- [Mobile](#mobile) — 19 tools
- [Failover](#failover) — 19 tools
- [Analytics](#analytics) — 12 tools
- [Sharing](#sharing) — 16 tools
- [Teams](#teams) — 11 tools
- [Billing](#billing) — 14 tools
- [Failover](#failover) — 13 tools
- [Model Routing](#model-routing) — 11 tools
- [Providers](#providers) — 9 tools
- [Security](#security) — 9 tools
- [Desktop UI](#desktop-ui) — 8 tools
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
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | ✅ | 184.9k 🚀 +737/d | **88** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 17.2k 🚀 +377/d | **85** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 25.1k 🚀 +394/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 60.2k 🚀 +1123/d | **83** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Thousands of Google engineers use EGM, an open-source plugin, to draft specs with deep-context agents and stress-test them with zero-context subagents before writing code. | 🟢 Easy | — | — | 12.1k 🚀 +1073/d | **82** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 2,926+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 49.2k 🚀 +64/d | **81** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 6k 🚀 +109/d | **77** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.3k 🚀 +35/d | **72** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.7k 🚀 +43/d | **68** |
| ✅ **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.2k 🚀 +60/d | **68** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.1k 🚀 +57/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 6k 🚀 +59/d | **66** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.4k 🚀 +21/d | **63** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 4.6k 🚀 +53/d | **63** |
| ✅ **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.7k 🚀 +23/d | **63** |
| 🔹 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.7k 🚀 +6/d | **61** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.2k 🚀 +19/d | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | the current dotnet-skills CLI remains skill-first; repo-owned agents can evolve and ship on their own track. | 🟢 Easy · OOTB | ✅ | — | 507 | **57** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.2k | **56** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 929 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 550 | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 913 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) External-content sanitizing (leyline) strips invisible | 🟢 Easy | — | — | 348 | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 769 | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 528 | **52** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [garrytan/gstack](https://github.com/garrytan/gstack), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) *(+25 more)*

*…and 11 more in [the full index](data/index.json).*

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

- Stars: **184,890** (+737.2/day over 5d)
- Health score: **88/100**
- Documentation score: **48/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-29
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **17,171** (+376.6/day over 5d)
- Health score: **85/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-29
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

- Stars: **25,103** (+393.6/day over 5d)
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

- Stars: **60,238** (+1123.4/day over 5d)
- Health score: **83/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

#### [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

> Thousands of Google engineers use EGM, an open-source plugin, to draft specs with deep-context agents and stress-test them with zero-context subagents before writing code.

**Core problems it solves**

- **Multi-agent orchestration** — *xed command (#220), but 1.4.8 does not (#196), so keep the prefix.*
- **Agent runtime** — *prove the specification before implementing.*
- **Notifications** — *For **Claude Cowork** and **ChatGPT Work**, see the setup guide.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Easy. No setup signals found in the README.

**Facts**

- Stars: **12,091** (+1073.0/day over 5d)
- Health score: **82/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-04
- Works with: Claude Code, Codex

</details>

## Analytics

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 116.1k 🚀 +946/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 111.3k 🚀 +431/d | **89** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🔴 Involved | — | — | 139.6k 🚀 +245/d | **88** |
| 🏆 **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 11.3k 🚀 +346/d | **87** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 48.2k 🚀 +53/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34k 🚀 +22/d | **72** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.9k 🚀 +22/d | **70** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 8.6k 🚀 +29/d | **65** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 1.7k 🚀 +39/d | **65** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **61** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.2k 🚀 +5/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 602 | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 595 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 483 | **56** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 439 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 326 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 787 | **52** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 321 | **48** |

**Also does this:** [getpaseo/paseo](https://github.com/getpaseo/paseo), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit), [yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)

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

- Stars: **116,111** (+945.8/day over 5d)
- Health score: **92/100**
- Documentation score: **52/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
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

- Stars: **111,268** (+431.4/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who…

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *use and re-verify before committing.*
- **Workspace isolation** — *sses; blocks below 7/10), fail-closed secret redaction, dedupe against existing issues, archive to $GSTACKSTATEROOT/projects/$SLUG/specs/ for team-co…*
- **Model / provider routing** — *deterministic aside repl scripts.*
- **Memory & context** — *voice-input aliases many skills carry, have their own pages.*
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

- Stars: **139,623** (+244.6/day over 5d)
- Health score: **88/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
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

- Stars: **11,316** (+346.2/day over 5d)
- Health score: **87/100**
- Documentation score: **54/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-11-05
- Works with: Claude Code, Codex

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

- Stars: **48,152** (+53.2/day over 5d)
- Health score: **73/100**
- Documentation score: **76/100**
- License: MIT
- Language: C
- Last push: 2026-11-04
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Memory & MCP

*MCP support*

The agent needs access to external tools and data through a standard protocol.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 22.7k 🚀 +173/d | **89** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 4.6k 🚀 +88/d | **81** |
| ✅ **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 8.8k 🚀 +120/d | **77** |
| ✅ **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Real vs code-synthesized: held-out ROC-AUC 0.92 with whole sound families held out. Listening through a soundtrack: 93% of the sound effects placed in a 60 s film mix are detected as events (89% | 🟡 Some setup | — | — | 3.9k 🚀 +120/d | **77** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.5k 🚀 +40/d | **68** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | With autoharness, we're building the self-learning layer next-gen agents will ship with, learning skills from real work. | 🟢 Easy | — | — | 10.7k 🚀 +43/d | **66** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **62** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **58** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance 3,985 archived projects -- full source code snapshots from the game security ecosystem (prefixed ags-) | 🟢 Easy | — | — | 548 🚀 +9/d | **57** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.1k | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 474 | **55** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Easy · OOTB | ✅ | — | 597 🚀 +6/d | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 387 | **54** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 738 | **52** |
| 🔹 **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | I got tired of re-explaining my project to every new AI chat, and then getting the old version of a decision back. | 🟢 Easy | — | — | 267 | **52** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | This checkout is 4.0.1.dev1. | 🟢 Easy | — | — | 529 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **51** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Runs code in a box — a local Docker sandbox for agent-written code (preview). | 🟡 Some setup | — | — | 508 | **48** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | This repository is essentially an LLM chat desktop application based on MCP. Windows: The MCP SDK includes a workaround specifically for Windows systems, as documented in ISSUE 101. | 🟢 Easy | — | ✅ | 1.2k | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.8k | **46** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 477 | **46** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | This repository is YALC 1.0, the first generation and the open-source one. Rate limiting — DB-backed token bucket on all external sends | 🔴 Involved | — | — | 325 | **46** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 417 | **42** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [superdesigndev/treg](https://github.com/superdesigndev/treg), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) *(+24 more)*

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

- Stars: **22,672** (+173.2/day over 5d)
- Health score: **89/100**
- Documentation score: **51/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-05

#### [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

> Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output.

**Core problems it solves**

- **Automatic failover** — *It falls back to the CPU encoder — reported in the result's hw.fallback/hw.notes — only when VideoToolbox itself refuses a job (any other ffmpeg fail…*
- **Multi-agent orchestration** — *contract and the test suite (tests/testcontract.py,*
- **API gateway / proxy** — *-pass encode and measures it ; --preset copy --repair remuxes a damaged file (timestamps regenerated, corrupt packets dropped) and counts the errors…*
- **Skills & plugins** — *uploaded; parakeet-mlx, faster-whisper and openai-whisper download their model weights the first time they run (parakeet-mlx's default from Hugging F…*
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

- Stars: **4,573** (+87.8/day over 5d)
- Health score: **81/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Cursor

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

- Stars: **8,845** (+119.6/day over 5d)
- Health score: **77/100**
- Documentation score: **43/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-27
- Works with: Claude Code, Cursor

#### [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)

> Ears for coding agents.

**Core problems it solves**

- **Skills & plugins** — */skills/ (or a project's .claude/skills/).*
- **Agent runtime**
- **MCP support** — *one line on stderr (earshot : error: ..., exit 1).*
- **Notifications** — *pes come as families of named characters: 34 motion-design categories (whooshes, swishes,*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 52/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux
- Some setup. install via pip install; needs git clone (build from source), create a Python venv; configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **3,947** (+120.0/day over 5d)
- Health score: **77/100**
- Documentation score: **57/100**
- License: MIT
- Language: Python
- Last push: 2026-10-22
- Works with: Claude Code

#### [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)

> Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker.

**Core problems it solves**

- **Multi-agent orchestration** — *veloper mode and MCP apps.*
- **API gateway / proxy** — *urrent Codex task through the official*
- **MCP support** — *t to the limits applied to that account.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source); configure environment variables, API key configuration

**Facts**

- Stars: **15,521** (+40.2/day over 5d)
- Health score: **68/100**
- Documentation score: **45/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Codex

</details>

## Mobile

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 166.7k 🚀 +217/d | **96** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 12.5k 🚀 +679/d | **87** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 23.2k 🚀 +118/d | **86** |
| 🏆 **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 1.9k 🚀 +155/d | **83** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 1.9k 🚀 +157/d | **80** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 9.3k 🚀 +110/d | **77** |
| ✅ **[zhongerxin/iPhone-use](https://github.com/zhongerxin/iPhone-use)** | 让 Codex、WorkBuddy 或豆包工作通过 USB 操作你的真实 iPhone。 用自然语言描述任务，助手就能打开 App、读取页面、点击、滚动、输入文字、整理列表，并在侧边栏展示手机屏幕。 | 🔴 Involved | — | — | 4.9k 🚀 +169/d | **77** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7k 🚀 +31/d | **68** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.5k 🚀 +14/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.3k 🚀 +14/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Crew works without Obsidian. | 🟢 Easy | — | — | 5.2k 🚀 +19/d | **64** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.8k | **63** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.7k 🚀 +16/d | **56** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k (+9/d) | **52** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Official agent skills/plugins for Power Platform development by Microsoft. Launch GitHub Copilot CLI or Claude Code with the plugin path: | 🟡 Some setup | — | — | 1.1k 🚀 +4/d | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 555 | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

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

- Stars: **166,661** (+216.6/day over 5d)
- Health score: **96/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-25
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **12,546** (+679.4/day over 5d)
- Health score: **87/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Codex, Cursor, Cline / Roo

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

- Stars: **23,163** (+118.2/day over 5d)
- Health score: **86/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

#### [leepokai/Codync](https://github.com/leepokai/Codync)

> The open-source Grok Bot alternative.

**Core problems it solves**

- **Remote control** — *help, approval cards, per-bot memory, remote screen, voice calls and "needs you / done" notifications — the same features, without being tied to one…*
- **Mobile access** — *> **Why the iPhone app can be a version behind:** every iPhone release goes through Apple's App Review first, which usually takes a day or more, so t…*
- **Multi-agent orchestration** — *other visible bots and message one; the reply comes back to it as a new turn, and it answers you then.*
- **Agent runtime** — *Codync turns the coding agents on your computer — Claude Code, Codex, Cursor, Pi, OpenCode, Grok Build, Gemini, Copilot, Hermes Agent and ~40 more —…*
- **MCP support** — *in its own session, and can react to each other, up to 3 rounds.*
- **Security & isolation** — *ut being tied to one model or one subscription.*
- **GUI / desktop app** — *OS, Windows and Linux (static on Linux, runs on any distro) that drives every agent, keeps the transcripts and serves every client.*
- **Notifications** — *40 more — into persistent *bots* you delegate to from your iPhone, Mac, Windows PC, Linux desktop or any terminal, the way you'd message a colleague.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/leepokai/Codync/main/packaging/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Turnkey. install via uvx one-liner, Homebrew install; configure sign-in required, database dependency; GUI application

**Facts**

- Stars: **1,888** (+154.6/day over 5d)
- Health score: **83/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)

> Continue using your DeepSeek Harness instance from a phone, computer, or browser.

**Core problems it solves**

- **Automatic failover** — *public IP is required on the Harness Host.*
- **Remote control** — *while preserving messages and tool status.*
- **Mobile access** — *use Bot mode, powered by Fei2411/DS-Bot.*
- **Parallel execution** — *ther tools through ACP integrations, with remote file browsing and terminals.*
- **Model / provider routing** — *nt through its own ACP server (hermes acp); opt-in in Remote settings.*
- **Security & isolation** — *onversation models with the same smooth workflow as local use.*
- **Self-hostable**
- **GUI / desktop app** — *bar Supported Install ds-harness-remote@0.6.3; this computer can also be the Host*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via native installer / package; configure sign-in required, process manager

**Facts**

- Stars: **1,879** (+156.8/day over 5d)
- Health score: **80/100**
- Documentation score: **57/100**
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Failover

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 19.2k 🚀 +266/d | **87** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.1k 🚀 +29/d | **69** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 9.2k 🚀 +60/d | **65** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.8k 🚀 +19/d | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.9k 🚀 +10/d | **55** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 410 | **55** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k 🚀 +10/d | **54** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Conversations with AI agents reset when context windows close. Agent Action Grammar (AAG): Ultra-compact, deterministic ASCII micro-syntax saving ~78–85% tokens compared to natural language prompt instructions. | 🟡 Some setup | — | — | 852 | **54** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 430 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **53** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 900 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 512 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 444 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 921 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 692 | **51** |
| 🔹 **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | Fusion merges the vector ranking (weight 1.7) with the hybrid ranking (weight 1), then adds small salience and recency boosts. Verifiable recall. | 🟡 Some setup | — | — | 285 | **51** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 514 | **49** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Plugin-first long-term memory for every agent platform. Corrections that stick. | 🟢 Easy | — | ✅ | 550 | **47** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 524 | **43** |

**Also does this:** [affaan-m/ECC](https://github.com/affaan-m/ECC), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [spinabot/brigade](https://github.com/spinabot/brigade), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse) *(+13 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [xerj-org/xerj](https://github.com/xerj-org/xerj)

> XERJ: the search engine for AI agents.

**Core problems it solves**

- **Memory & context** — *f the same primitive: xerj autoindex makes an agent*
- **Agent runtime** — *rity audit of WordPress core,*
- **MCP support** — *de Code, Cursor and any MCP client.*
- **GUI / desktop app** — *the same --insecure dev node.*
- **Cross-agent support** — *Mentions Aider, Amp, Claude Code, Cline*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://xerj.org/get | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source), cargo build; configure API key configuration, config file; GUI application

**Facts**

- Stars: **19,155** (+265.6/day over 5d)
- Health score: **87/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-05
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

- Stars: **33,090** (+29.4/day over 5d)
- Health score: **69/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-05
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

- Stars: **9,228** (+59.6/day over 5d)
- Health score: **65/100**
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
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install; configure environment variables, database dependency

**Facts**

- Stars: **7,807** (+19.2/day over 5d)
- Health score: **63/100**
- Documentation score: **59/100**
- License: MIT
- Language: Go
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **1,858** (+10.0/day over 5d)
- Health score: **55/100**
- Documentation score: **74/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Analytics

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 297.5k 🚀 +780/d | **89** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 7.2k 🚀 +80/d | **79** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 11.8k 🚀 +68/d | **75** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.2k 🚀 +22/d | **69** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.9k 🚀 +13/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.5k 🚀 +22/d | **65** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5k 🚀 +5/d | **61** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **56** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | English \| 简体中文 \| 日本語 | 🟢 Easy | — | — | 492 | **54** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **51** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 559 | **49** |

**Also does this:** [makecindy/cindy](https://github.com/makecindy/cindy), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [decolua/9router](https://github.com/decolua/9router), [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher), [trycompai/crm](https://github.com/trycompai/crm), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [crshdn/mission-control](https://github.com/crshdn/mission-control), [Licoy/Quosparr](https://github.com/Licoy/Quosparr) *(+1 more)*

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

- Stars: **297,544** (+780.0/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-02
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

- Stars: **7,166** (+79.6/day over 5d)
- Health score: **79/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-05
- Works with: Claude Code

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

- Stars: **11,757** (+68.4/day over 5d)
- Health score: **75/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> Persistent memory across coding sessions and agents.

**Core problems it solves**

- **Quota & usage management**
- **Automatic failover** — *y, paste the block inside { "mcpServers": { ...*
- **Multi-agent orchestration** — *er's current pricing before enabling it.*
- **Model / provider routing** — *inference is on-device afterward.*
- **API gateway / proxy** — *UTOCOMPRESS=true; it can make a request for each captured observation, so check your provider's current pricing before enabling it.*
- **Billing & metering**
- **Session persistence** — *s and lessons searchable from the agent you are using now.*
- **Memory & context** — *Persistent memory across coding sessions and agents.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx -y @agentmemory/agentmemory@latest`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, global npm install; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no code needed

**Facts**

- Stars: **30,152** (+22.0/day over 5d)
- Health score: **69/100**
- Documentation score: **73/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [appwrite/appwrite](https://github.com/appwrite/appwrite)

> Appwrite is an MCP and agent-first, open-source platform for building and scaling apps.

**Core problems it solves**

- **Agent runtime** — *Realtime, and Hosting, all in one place.*
- **MCP support** — *r building and scaling apps.*
- **Self-hostable** — *-first, open-source platform for building and scaling apps.*
- **Notifications** — *ed runtimes and event-driven execution.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run -it --rm \`
- Platforms mentioned: Windows, Linux, Android, Web
- Easy. install via npx one-liner, native installer / package; needs docker run; configure environment variables, OAuth login flow; one-click setup

**Facts**

- Stars: **57,866** (+13.0/day over 5d)
- Health score: **68/100**
- Documentation score: **67/100**
- License: BSD-3-Clause
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Cursor

</details>

## Sharing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 30.2k 🚀 +725/d | **91** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 133.3k 🚀 +192/d | **89** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 4.9k 🚀 +201/d | **74** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 19.7k 🚀 +33/d | **69** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32k 🚀 +48/d | **68** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 10.4k 🚀 +38/d | **67** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | and connect OpenCode, Pi, Qoder, WorkBuddy, Kilo, Cline, T3 Code and more through managed configs. | 🟡 Some setup | — | — | 18.2k 🚀 +27/d | **65** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 894 🚀 +50/d | **57** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.8k 🚀 +10/d | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 302 | **53** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 510 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k 🚀 +7/d | **51** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 920 | **51** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 559 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 319 | **50** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Setup: 🟢 **Turnkey** (friction 11/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://usemagpie.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via go install, curl | sh installer; configure API key configuration, config file; one-click setup

**Facts**

- Stars: **30,245** (+725.0/day over 5d)
- Health score: **91/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-05
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

- Stars: **133,287** (+192.2/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-05
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

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

- Stars: **4,892** (+201.4/day over 5d)
- Health score: **74/100**
- Documentation score: **27/100**
- License: MIT
- Last push: 2026-09-06
- Works with: Claude Code, Codex, Cursor

#### [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

> English · Portuguese (BR) · 简体中文

**Core problems it solves**

- **Multi-account switching** — *surf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Quota & usage management** — *目前支持 Antigravity IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，…*
- **Automatic failover** — *aude CLI 与 Claude Desktop Gateway 第三方供应商预设、模型映射，以及从会话 JSONL 汇总真实用量的方向参考：CC Switch*
- **Multi-agent orchestration**
- **Parallel execution** — *ty IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Workspace isolation** — *ns/Cockpit Tools.app'），请先删除旧版本再安装：*
- **Model / provider routing**
- **Multi-provider aggregation** — *어 · 🇧🇷 Português · 🇷🇺 Русский · 🇹🇷 Türkçe · 🇵🇱 Polski · 🇨🇿 Čeština · 🇸🇦 العربية · 🇻🇳 Tiếng Việt · 🇮🇩 Bahasa Indonesia*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **19,740** (+32.8/day over 5d)
- Health score: **69/100**
- Documentation score: **64/100**
- Language: Rust
- Last push: 2026-11-05
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

- Stars: **31,969** (+47.6/day over 5d)
- Health score: **68/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-28
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Teams

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 106k 🚀 +186/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 80.3k 🚀 +273/d | **90** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 15.2k 🚀 +106/d | **83** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 11.7k 🚀 +62/d | **76** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 85k 🚀 +54/d | **76** |
| ✅ **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.cursor — login and session history managed exclusively by the Cursor CLI. | 🟡 Some setup | — | — | 5.7k 🚀 +68/d | **73** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Goose, Antigravity, GitHub Copilot, Devin, Kiro, Qwen Code, Kimi Code, Grok Build, Jcode, He… | 🟢 Easy | — | — | 11.2k 🚀 +18/d | **67** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.8k 🚀 +27/d | **65** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.6k 🚀 +10/d | **58** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 306 | **53** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 428 | **52** |

**Also does this:** [cordum-io/cordum](https://github.com/cordum-io/cordum), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

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

- Stars: **106,047** (+186.2/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
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

- Stars: **80,333** (+273.2/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode, Cursor

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
- Some setup. install via scoop install, curl | sh installer; needs docker run, git clone (build from source); configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **15,174** (+106.4/day over 5d)
- Health score: **83/100**
- Documentation score: **71/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-05
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
- Quickest install: `curl -fsSL https://download.octop.cloud/octop/scripts/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs docker run, make build; configure config.json/yaml/toml, OAuth login flow; one-click setup

**Facts**

- Stars: **11,693** (+61.8/day over 5d)
- Health score: **76/100**
- Documentation score: **79/100**
- License: MIT
- Language: Python
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode

#### [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

> English | 中文 | 日本語 | Français | Русский | Português | 한국어

**Core problems it solves**

- **Automatic failover** — *d X-Forwarded-Proto: https) or localhost HTTP.*
- **Multi-agent orchestration** — *llion to our incredible community — you made this happen! 💪🔥*
- **Parallel execution** — *x plus Docker is the recommended deployment target for a persistent server.*
- **Workspace isolation** — *ame matches the payload's type field.*
- **Model / provider routing** — *urn a format error instead of exposing the raw provider payload.*
- **API gateway / proxy** — *es pass through request admission again.*
- **Usage analytics** — *m, memory, skills, sandbox-aware execution, and the ability to plan and spawn sub-agents for complex, multi-step tasks.*
- **Session persistence** — *, and publish a new app version.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @minimax-ai/code`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **85,021** (+53.8/day over 5d)
- Health score: **76/100**
- Documentation score: **80/100**
- License: MIT
- Language: Python
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Cursor, Droid

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 65.2k 🚀 +368/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Easy | — | — | 5.1k 🚀 +847/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 45.5k 🚀 +62/d | **73** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 3.8k 🚀 +34/d | **65** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.1k 🚀 +25/d | **63** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 290 | **56** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.9k 🚀 +16/d | **55** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 直接找：接口一览 ｜ 五分钟上手 ｜ 易支付协议兼容接入 ｜ 到账账号与收款分配 ｜ 微信 JSAPI 公众号配置 ｜ 文档目录 ｜ 常见问题 | 🟢 Easy | — | — | 326 | **52** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 547 | **51** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 412 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 829 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 442 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [decolua/9router](https://github.com/decolua/9router)

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

- Stars: **65,190** (+367.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-03
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)

> 244 pixel art effects and animations, every one a small piece of code.

**Core problems it solves**

- **Billing & metering** — *iming is plain data: read slash.act, or meta.pixelfx.act in a sprite sheet's*
- **Skills & plugins** — *e) gives you each part drawn on its own.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Web
- Easy. No setup signals found in the README.

**Facts**

- Stars: **5,081** (~846.8/day lifetime average)
- Health score: **78/100**
- Documentation score: **29/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-31
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

- Stars: **45,500** (+61.8/day over 5d)
- Health score: **73/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)

> 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。视频生成成本约 40 元。

**Core problems it solves**

- **Billing & metering**
- **Agent runtime** — */user-attachments/assets/f67e2e04-52e7-42a9-a4a0-e2864ff0f51e*
- **Self-hostable**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx skills add zenstory-ai/drama-skills -y -g`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via npx one-liner; needs git clone (build from source)

**Facts**

- Stars: **3,812** (~34.3/day lifetime average)
- Health score: **65/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-11-04
- Works with: Claude Code, Codex

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

- Stars: **11,096** (+24.6/day over 5d)
- Health score: **63/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 6.1k 🚀 +285/d | **88** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | Turn the browser you already use into a workspace for your AI agent. | 🟢 Easy | — | — | 10.1k 🚀 +42/d | **68** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 9.4k 🚀 +29/d | **65** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.7k 🚀 +13/d | **64** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.9k 🚀 +11/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.5k 🚀 +6/d | **59** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.9k 🚀 +12/d | **59** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 5.1k | **55** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.8k | **55** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.9k 🚀 +13/d | **51** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 288 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 676 | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 315 | **44** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [openai/codex](https://github.com/openai/codex), [garrytan/gstack](https://github.com/garrytan/gstack), [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft), [xerj-org/xerj](https://github.com/xerj-org/xerj), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [aicodeking/leanrea](https://github.com/aicodeking/leanrea) *(+24 more)*

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

- Stars: **6,051** (+284.8/day over 5d)
- Health score: **88/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

> Turn the browser you already use into a workspace for your AI agent.

**Core problems it solves**

- **Automatic failover**
- **Skills & plugins** — *uire the sync's observationid as --observation.*
- **MCP support** — *skipped unless you explicitly replace them with --force.*
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

- Stars: **10,050** (+42.2/day over 5d)
- Health score: **68/100**
- Documentation score: **60/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Cursor

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

- Stars: **9,382** (+28.6/day over 5d)
- Health score: **65/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-11-05

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

- Stars: **27,695** (+13.2/day over 5d)
- Health score: **64/100**
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

- Stars: **1,917** (+10.8/day over 5d)
- Health score: **62/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 154.6k 🚀 +121/d | **90** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | A toolbox of film styles made in code: 66 ready to use, and your own. You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. | 🟡 Some setup | — | ✅ | 12.5k 🚀 +515/d | **84** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 19.2k 🚀 +3836/d | **79** |
| ✅ **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 4.3k 🚀 +58/d | **66** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.2k 🚀 +35/d | **62** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote attaches to a running pi session through pi's official extension API. The extension channel (7001) binds to 127.0.0.1 by default. | 🟢 Easy | — | — | 299 🚀 +37/d | **59** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.3k 🚀 +8/d | **58** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2k 🚀 +10/d | **54** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 353 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 717 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 478 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [anomalyco/opencode](https://github.com/anomalyco/opencode), [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [maximhq/bifrost](https://github.com/maximhq/bifrost) *(+12 more)*

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

- Stars: **154,616** (+120.6/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-04
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **12,491** (+515.2/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-31
- Works with: Claude Code, Cursor

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

- Stars: **19,179** (~3835.8/day lifetime average)
- Health score: **79/100**
- Documentation score: **23/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-03

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

- Stars: **4,323** (+57.6/day over 5d)
- Health score: **66/100**
- Documentation score: **36/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-11-01
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

- Stars: **11,169** (+34.8/day over 5d)
- Health score: **62/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 152k 🚀 +299/d | **93** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.4k 🚀 +42/d | **72** |
| ✅ **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.2k 🚀 +82/d | **72** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 898 | **56** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.4k 🚀 +8/d | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 768 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 437 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 600 | **45** |

**Also does this:** [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [automazeio/ccpm](https://github.com/automazeio/ccpm), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

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

- Stars: **152,034** (+299.0/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-05
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

- Stars: **4,437** (+42.2/day over 5d)
- Health score: **72/100**
- Documentation score: **80/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-02
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

- Stars: **4,201** (+81.6/day over 5d)
- Health score: **72/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-05
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

- Stars: **898** (+2.4/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-04
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

- Stars: **4,393** (+8.2/day over 5d)
- Health score: **54/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-24
- Works with: Codex

</details>

## Security

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 51.4k 🚀 +67/d | **72** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 5.5k 🚀 +13/d | **65** |
| 🔹 **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | English · 安装指南 · 问题反馈 | 🔴 Involved | — | — | 3.6k 🚀 +41/d | **59** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 463 🚀 +27/d | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Z0 round 2, 16 repositories, Claude Code with hippo against its built-in memory: no extra cost (ratio 0.999 [0.962, 1.037]) and about 12% less spent on teach and correction turns. Decay tied with decay switched off. | 🟡 Some setup | — | — | 790 | **55** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **51** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | Tag local AI agents into Slack threads, with local execution, visible progress, approvals, audit trails, and pluggable agent runtimes. | 🟡 Some setup | — | — | 499 | **42** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [leepokai/Codync](https://github.com/leepokai/Codync), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [superdesigndev/treg](https://github.com/superdesigndev/treg), [makecindy/cindy](https://github.com/makecindy/cindy), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas) *(+9 more)*

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

- Stars: **51,423** (+67.2/day over 5d)
- Health score: **72/100**
- Documentation score: **75/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-11-04

#### [aipoch/open-science](https://github.com/aipoch/open-science)

> AI research workbench for reproducible science — open-source, local-first, and model-agnostic.

**Core problems it solves**

- **Remote control** — *e host to stay on and online, with AIPOCH Open-Science and the Remote.It agent running, and the host added to a signed-in Remote.It account.*
- **Model / provider routing** — *d-to-path operations, or a remote HTTP MCP endpoint.*
- **Billing & metering** — *Why does the model connection test fail? A: Check the API Key for missing characters or spaces, verify the Base URL and region, use the provider's ex…*
- **Skills & plugins** — *fers to the skill, not to the availability of every registered host.*
- **MCP support** — *cts, output formats, and exit codes*
- **Security & isolation** — *that profile's existing permissions; it is not a separate sandbox or read-only view, so connected clients can persist changes and incur model costs.*
- **GUI / desktop app** — *de.js, so you can run the CLI without installing Node.js, npm, or Homebrew.*
- **Notifications** — *untime checks and test your model connection.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 35/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install --cask open-science`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow; one-click setup

**Facts**

- Stars: **5,468** (+12.6/day over 5d)
- Health score: **65/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-05
- Works with: Claude Code, Codex, OpenCode

#### [Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)

> English · 安装指南 · 问题反馈

**Core problems it solves**

- **Model / provider routing** — *nowLuma：请自行按上游文档安装、启动并登录，开启 OneBot WebSocket 服务端和 HTTP API。*
- **Usage analytics** — *用二代仿真模式（reserved2），会选择性发言；测试收发时可先切到 chat，再从白名单会话发送消息。*
- **MCP support**
- **Security & isolation**

**Getting it running**

- Setup: 🔴 **Involved** (friction 66/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install`
- Platforms mentioned: Windows, Web
- Involved setup. needs git clone (build from source), npm install/build; configure config.json/yaml/toml

**Facts**

- Stars: **3,555** (+41.2/day over 5d)
- Health score: **59/100**
- Documentation score: **45/100**
- License: NOASSERTION
- Language: JavaScript
- Last push: 2026-11-05

#### [AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)

> Leave the agent working.

**Core problems it solves**

- **Agent runtime**
- **MCP support** — *er checks the action again on the host*
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

- Stars: **463** (+26.6/day over 5d)
- Health score: **58/100**
- Documentation score: **53/100**
- License: NOASSERTION
- Language: Elixir
- Last push: 2026-11-05
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

- Stars: **8,459** (+0.2/day over 5d)
- Health score: **56/100**
- Documentation score: **28/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-22
- Works with: Claude Code, Codex

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 224.7k 🚀 +258/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 13.9k 🚀 +295/d | **88** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.3k 🚀 +15/d | **62** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 4k 🚀 +50/d | **61** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 483 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 785 | **53** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 534 🚀 +6/d | **51** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 641 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [openai/codex](https://github.com/openai/codex), [xerj-org/xerj](https://github.com/xerj-org/xerj), [getpaseo/paseo](https://github.com/getpaseo/paseo), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [leepokai/Codync](https://github.com/leepokai/Codync), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) *(+30 more)*

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

- Stars: **224,716** (+257.6/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-05
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

- Stars: **13,948** (+295.0/day over 5d)
- Health score: **88/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-05
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

- Stars: **15,336** (+14.6/day over 5d)
- Health score: **62/100**
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

- Stars: **4,014** (+50.0/day over 5d)
- Health score: **61/100**
- Documentation score: **30/100**
- License: MIT
- Language: Python
- Last push: 2026-10-19
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **483** (+1.0/day over 5d)
- Health score: **56/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-01
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile | Failover, Memory & MCP |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Teams | Memory & MCP, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Failover |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Analytics | Desktop UI, Mobile |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Memory & MCP, Model Routing |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI, Model Routing |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Teams | Model Routing |
| **[openai/codex](https://github.com/openai/codex)** | Sharing | Desktop UI, Failover |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Analytics | Failover, Memory & MCP |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Analytics | Failover, Security |
| **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Desktop UI | Failover |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Analytics | Desktop UI, Failover |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Failover | Desktop UI, Failover |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile | Memory & MCP, Security |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Analytics, Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI, Model Routing |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Model Routing, Security |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, Security |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Desktop UI | Desktop UI |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Memory & MCP | Desktop UI, Failover |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | Desktop UI, Security |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Analytics, Failover |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Analytics | Memory & MCP, Security |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Mobile | Analytics, Security |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Memory & MCP | Desktop UI |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Desktop UI, Desktop UI |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Teams | Failover, Memory & MCP |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Analytics | Memory & MCP, Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Analytics, Sharing |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Teams | Analytics, Memory & MCP |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Analytics | Desktop UI, Failover |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Model Routing, Sharing |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Failover |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Security | Analytics, Model Routing |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Analytics | Desktop UI, Memory & MCP |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Analytics | Desktop UI, Failover |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Analytics | Failover, Memory & MCP |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Billing, Memory & MCP |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Desktop UI, Model Routing |
| **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Analytics | Memory & MCP |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Analytics, Billing |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Teams | Desktop UI, Memory & MCP |
| **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | Memory & MCP | Desktop UI |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Desktop UI, Failover |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Teams | Memory & MCP, Model Routing |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Analytics | Desktop UI, Model Routing |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Security | Memory & MCP, Model Routing |
| **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Billing | Analytics |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Failover | Memory & MCP, Model Routing |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Analytics | Desktop UI, Failover |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Analytics, Security |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Desktop UI, Memory & MCP |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Mobile | Failover, Memory & MCP |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | Memory & MCP, Model Routing |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Desktop UI | Desktop UI |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Failover | Desktop UI, Model Routing |
| **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | Desktop UI | Failover |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Analytics | Desktop UI, Failover |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Analytics | Failover, Memory & MCP |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Failover | Desktop UI, Failover |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Failover | Memory & MCP, Security |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Model Routing | Desktop UI |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams | Desktop UI, Model Routing |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | Memory & MCP | Failover |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Analytics | Failover, Security |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI, Failover |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Sharing | Analytics, Failover |
| **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | Memory & MCP | Failover, Failover |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | Desktop UI | Desktop UI, Failover |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Analytics | Failover, Memory & MCP |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI, Failover |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Security |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Analytics | Desktop UI, Mobile |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Analytics | Desktop UI, Failover |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Analytics | Desktop UI, Security |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI, Failover |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Failover, Memory & MCP |
| **[trycompai/crm](https://github.com/trycompai/crm)** | Billing | Analytics |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Failover | Failover, Model Routing |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Failover | Desktop UI, Desktop UI |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Memory & MCP | Desktop UI, Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Security | Failover, Failover |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Desktop UI | Desktop UI |
| **[oracle/mcp](https://github.com/oracle/mcp)** | Memory & MCP | Security |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Analytics | Providers, Security |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Analytics | Desktop UI, Failover |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Desktop UI, Security |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Analytics | Providers |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Failover | Desktop UI, Desktop UI |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Failover, Security |
| **[0sec-labs/0](https://github.com/0sec-labs/0)** | Memory & MCP | Desktop UI, Failover |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Failover | Failover, Memory & MCP |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | Memory & MCP | Desktop UI, Security |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Failover | Analytics, Memory & MCP |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI, Model Routing |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Failover |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams | Analytics, Analytics |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Analytics, Mobile |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Failover, Failover |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Mobile | Failover, Failover |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Failover | Desktop UI, Model Routing |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Analytics | Desktop UI, Security |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Memory & MCP | Desktop UI, Model Routing |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Sharing | Desktop UI |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Memory & MCP, Teams |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Failover | Failover, Security |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams | Desktop UI, Failover |
| **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | Billing | Memory & MCP, Sharing |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Analytics, Memory & MCP |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Failover, Memory & MCP |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Analytics, Memory & MCP |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Failover | Desktop UI, Model Routing |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Failover | Desktop UI, Memory & MCP |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Sharing | Failover, Teams |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Desktop UI, Model Routing |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Providers, Sharing |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Security | Analytics, Providers |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | Memory & MCP | Failover |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Failover, Memory & MCP |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Failover | Desktop UI, Failover |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Analytics, Security |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI, Memory & MCP |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Failover | Desktop UI, Failover |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Sharing | Analytics, Model Routing |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Analytics | Desktop UI, Security |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Failover | Failover |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Billing | Analytics, Desktop UI |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Memory & MCP | Desktop UI |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Analytics, Failover |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | Memory & MCP | Desktop UI, Failover |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Failover | Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Memory & MCP | Desktop UI, Failover |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | Memory & MCP | Desktop UI |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | Security | Failover, Memory & MCP |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI, Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Failover | Failover, Memory & MCP |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Memory & MCP | Desktop UI, Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI, Failover |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.20x the stars (30,245 vs 152,034) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 60.55x the stars (19,740 vs 326) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 68.37x the stars (30,152 vs 441) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.14x the stars (34,050 vs 382) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | 3.59x the stars (1,858 vs 518) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.32x the stars (11,693 vs 2,200) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.73x the stars (34,050 vs 927) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 132.24x the stars (49,193 vs 372) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 173.21x the stars (49,193 vs 284) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 316.10x the stars (111,268 vs 352) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 22.40x the stars (111,268 vs 4,968) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.21x the stars (49,193 vs 3,725) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 231.19x the stars (297,544 vs 1,287) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 13.40x the stars (30,152 vs 2,250) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.41x the stars (49,193 vs 366) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.01x the stars (11,693 vs 403) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 6.97x the stars (49,193 vs 7,058) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.16x the stars (23,163 vs 481) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.67x the stars (49,193 vs 316) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.48x the stars (34,050 vs 278) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 476.83x the stars (297,544 vs 624) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 35.12x the stars (19,740 vs 562) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 6.05x the stars (1,705 vs 282) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 14.74x the stars (5,468 vs 371) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 12.93x the stars (19,155 vs 1,482) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.10x the stars (297,544 vs 6,186) | 🤖 auto (high) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 106.54x the stars (30,152 vs 283) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 154.98x the stars (152,034 vs 981) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.01x the stars (34,050 vs 351) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 614.76x the stars (297,544 vs 484) | 🤖 auto (high) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 91.27x the stars (49,193 vs 539) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 8.94x the stars (12,546 vs 1,404) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.14x the stars (11,693 vs 2,821) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.72x the stars (11,693 vs 1,341) | 🤖 auto (medium) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.10x the stars (49,193 vs 3,756) | 🤖 auto (medium) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.02x the stars (19,740 vs 2,461) | 🤖 auto (high) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.39x the stars (23,163 vs 5,276) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 45.07x the stars (19,155 vs 425) | 🤖 auto (medium) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 44.80x the stars (11,693 vs 261) | 🤖 auto (medium) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 280.60x the stars (85,021 vs 303) | 🤖 auto (medium) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 23.55x the stars (34,050 vs 1,446) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.36x the stars (1,146 vs 486) | 🤖 auto (high) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 64.98x the stars (49,193 vs 757) | 🤖 auto (medium) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 29.13x the stars (297,544 vs 10,213) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 81.72x the stars (49,193 vs 602) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.61x the stars (929 vs 577) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 6.29x the stars (34,050 vs 5,411) | 🤖 auto (high) |
| **[google/artemis](https://github.com/google/artemis)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 10.00x the stars (166,661 vs 16,661) | 🤖 auto (high) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 3.02x the stars (11,757 vs 3,894) | 🤖 auto (medium) |
| **[yetone/cumora](https://github.com/yetone/cumora)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 2.72x the stars (11,230 vs 4,129) | 🤖 auto (high) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,193 vs 27,708) | 🤖 auto (medium) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.19x the stars (326 vs 273) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui | 27.7k | 🔻 Superseded | 1.78x the stars (49,193 vs 27,708) |
| **[google/artemis](https://github.com/google/artemis)** | mobile | 16.7k | 🔻 Superseded | 10.00x the stars (166,661 vs 16,661) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | analytics-3 | 10.2k | 🔻 Superseded | 29.13x the stars (297,544 vs 10,213) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | desktop-ui | 7.1k | 🔻 Superseded | 6.97x the stars (49,193 vs 7,058) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | analytics-3 | 6.2k | 🔻 Superseded | 48.10x the stars (297,544 vs 6,186) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | analytics | 5.4k | 🔻 Superseded | 6.29x the stars (34,050 vs 5,411) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.3k | 🔻 Superseded | 4.39x the stars (23,163 vs 5,276) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | analytics | 5k | 🔻 Superseded | 22.40x the stars (111,268 vs 4,968) |
| **[yetone/cumora](https://github.com/yetone/cumora)** | teams | 4.1k | 🔻 Superseded | 2.72x the stars (11,230 vs 4,129) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | analytics-3 | 3.9k | 🔻 Superseded | 3.02x the stars (11,757 vs 3,894) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | desktop-ui | 3.8k | 🔻 Superseded | 13.10x the stars (49,193 vs 3,756) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui | 3.7k | 🔻 Superseded | 13.21x the stars (49,193 vs 3,725) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.8k | 🔻 Superseded | 4.14x the stars (11,693 vs 2,821) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.5k | 🔻 Superseded | 8.02x the stars (19,740 vs 2,461) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | analytics-3 | 2.2k | 🔻 Superseded | 13.40x the stars (30,152 vs 2,250) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.2k | 🔻 Superseded | 5.32x the stars (11,693 vs 2,200) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | failover | 1.5k | 🔻 Superseded | 12.93x the stars (19,155 vs 1,482) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | analytics | 1.4k | 🔻 Superseded | 23.55x the stars (34,050 vs 1,446) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile | 1.4k | 🔻 Superseded | 8.94x the stars (12,546 vs 1,404) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 8.72x the stars (11,693 vs 1,341) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | analytics-3 | 1.3k | 🔻 Superseded | 231.19x the stars (297,544 vs 1,287) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 981 | 🔻 Superseded | 154.98x the stars (152,034 vs 981) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | analytics | 927 | 🔻 Superseded | 36.73x the stars (34,050 vs 927) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 757 | 🔻 Superseded | 64.98x the stars (49,193 vs 757) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | analytics-3 | 624 | 🔻 Superseded | 476.83x the stars (297,544 vs 624) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 602 | 🔻 Superseded | 81.72x the stars (49,193 vs 602) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | desktop-ui | 577 | 🔻 Superseded | 1.61x the stars (929 vs 577) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 562 | 🔻 Superseded | 35.12x the stars (19,740 vs 562) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | desktop-ui | 539 | 🔻 Superseded | 91.27x the stars (49,193 vs 539) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | failover | 518 | 🔻 Superseded | 3.59x the stars (1,858 vs 518) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | memory-mcp | 486 | 🔻 Superseded | 2.36x the stars (1,146 vs 486) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | analytics-3 | 484 | 🔻 Superseded | 614.76x the stars (297,544 vs 484) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 481 | 🔻 Superseded | 48.16x the stars (23,163 vs 481) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | analytics-3 | 441 | 🔻 Superseded | 68.37x the stars (30,152 vs 441) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | failover | 425 | 🔻 Superseded | 45.07x the stars (19,155 vs 425) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 403 | 🔻 Superseded | 29.01x the stars (11,693 vs 403) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | analytics | 382 | 🔻 Superseded | 89.14x the stars (34,050 vs 382) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui | 372 | 🔻 Superseded | 132.24x the stars (49,193 vs 372) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | security | 371 | 🔻 Superseded | 14.74x the stars (5,468 vs 371) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 366 | 🔻 Superseded | 134.41x the stars (49,193 vs 366) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | analytics | 352 | 🔻 Superseded | 316.10x the stars (111,268 vs 352) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | analytics | 351 | 🔻 Superseded | 97.01x the stars (34,050 vs 351) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 326 | 🔻 Superseded | 60.55x the stars (19,740 vs 326) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 316 | 🔻 Superseded | 155.67x the stars (49,193 vs 316) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams | 303 | 🔻 Superseded | 280.60x the stars (85,021 vs 303) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 Superseded | 173.21x the stars (49,193 vs 284) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | analytics-3 | 283 | 🔻 Superseded | 106.54x the stars (30,152 vs 283) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | analytics | 282 | 🔻 Superseded | 6.05x the stars (1,705 vs 282) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | analytics | 278 | 🔻 Superseded | 122.48x the stars (34,050 vs 278) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | analytics | 273 | 🔻 Superseded | 1.19x the stars (326 vs 273) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 261 | 🔻 Superseded | 44.80x the stars (11,693 vs 261) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-05 12:23 UTC. 227 live tools · 122 candidates rejected by the quality gates.</sub>
