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

**230 tools** across **13 categories** · **48 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-11 11:55 UTC**

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
- [Isolation & Teams](#isolation-teams) — 26 tools
- [MCP & Security](#mcp-security) — 25 tools
- [Billing](#billing) — 21 tools
- [Memory & Failover](#memory-failover) — 21 tools
- [Mobile](#mobile) — 22 tools
- [Sharing](#sharing) — 11 tools
- [Model Routing](#model-routing) — 14 tools
- [Failover](#failover) — 13 tools
- [Analytics](#analytics) — 12 tools
- [Desktop UI](#desktop-ui) — 10 tools
- [Providers](#providers) — 9 tools
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
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 18.6k 🚀 +250/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 26.6k 🚀 +243/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 69.8k 🚀 +1418/d | **83** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 40 mandatory rules (R-01 to R-40) in three tiers: Hard Gate, Purpose-Gate, and Quality Locks. A Delivery Gate: a mandatory PASS/FAIL report in four blocks, run before anything ships. | 🟢 Turnkey · OOTB | ✅ | — | 8.9k 🚀 +96/d | **82** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 2,955+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 49.5k 🚀 +54/d | **79** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.8k 🚀 +61/d | **77** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 6.6k 🚀 +94/d | **74** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 8.9k 🚀 +206/d | **71** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 6.5k 🚀 +68/d | **69** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 4.9k 🚀 +59/d | **64** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.3k 🚀 +40/d | **63** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.8k 🚀 +14/d | **62** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +17/d | **62** |
| ✅ **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.3k 🚀 +30/d | **62** |
| ✅ **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.8k 🚀 +25/d | **62** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.3k 🚀 +12/d | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 952 | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 554 | **56** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.3k 🚀 +21/d | **55** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 925 | **53** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 559 🚀 +6/d | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor | 🔴 Involved | — | — | 787 | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 443 | **52** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) External-content sanitizing (leyline) strips invisible | 🟡 Some setup | — | — | 350 | **52** |

**Also does this:** [garrytan/gstack](https://github.com/garrytan/gstack), [anomalyco/opencode](https://github.com/anomalyco/opencode), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [qybaihe/bla](https://github.com/qybaihe/bla), [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell) *(+29 more)*

*…and 9 more in [the full index](data/index.json).*

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

- Stars: **18,630** (+249.6/day over 5d)
- Health score: **86/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-09
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

- Stars: **26,634** (+242.6/day over 5d)
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

- Stars: **69,835** (+1417.8/day over 5d)
- Health score: **83/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

#### [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)

> A filter, not a style guide.

**Core problems it solves**

- **Skills & plugins** — *e them, so adding one does not change the core.*
- **Agent runtime**
- **Cross-agent support** — *Mentions Amp, Claude Code, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 7/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx antislop-ai`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via npx one-liner, native installer / package

**Facts**

- Stars: **8,921** (+95.6/day over 5d)
- Health score: **82/100**
- Documentation score: **54/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-10
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)

> Agentic Awesome Skills is a library of 2,955+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents.

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

- Stars: **49,523** (+54.4/day over 5d)
- Health score: **79/100**
- Documentation score: **82/100**
- License: MIT
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Isolation & Teams

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🟡 Some setup | — | — | 141.2k 🚀 +175/d | **91** |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 2026-10-28 🚀 DeepTutor v1.7.0 is here! Partners and subagents — Consult live agents such as Claude Code, Codex, and Grok CLI, import past conversations, or run persistent Partners with their own memory, resources, and I… | 🟡 Some setup | — | — | 58.2k (+183/d) | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 113.1k 🚀 +291/d | **89** |
| 🏆 **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12.4k 🚀 +142/d | **88** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.cursor — login and session history managed exclusively by the Cursor CLI. | 🟡 Some setup | — | — | 7k 🚀 +211/d | **83** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 15.6k 🚀 +78/d | **77** |
| ✅ **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | ThinkRail is an agentic IDE that gets better every time you use it. Skills. | 🟢 Turnkey | — | ✅ | 8.2k (+65/d) | **74** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 48.5k 🚀 +56/d | **74** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.2k 🚀 +29/d | **73** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 11.9k 🚀 +36/d | **71** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | An open catalog of components for Claude Code, installable with one command. | 🟢 Easy | — | — | 33.3k 🚀 +29/d | **70** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 28k 🚀 +17/d | **69** |
| ✅ **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **62** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **58** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 615 | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 597 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 499 | **56** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 792 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 451 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 332 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.4k | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 786 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 309 | **52** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 428 | **51** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 3k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 323 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design), [getpaseo/paseo](https://github.com/getpaseo/paseo), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [felinics/Memoh](https://github.com/felinics/Memoh), [cordum-io/cordum](https://github.com/cordum-io/cordum), [crshdn/mission-control](https://github.com/crshdn/mission-control), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)

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

- Stars: **141,174** (+175.2/day over 5d)
- Health score: **91/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **58,162** (~183.5/day lifetime average)
- Health score: **90/100**
- Documentation score: **81/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-07
- Works with: Claude Code, Codex, OpenCode, Copilot

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

- Stars: **113,060** (+290.8/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **12,432** (+141.8/day over 5d)
- Health score: **88/100**
- Documentation score: **54/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-11-11
- Works with: Claude Code, Codex

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

- Stars: **6,966** (+211.0/day over 5d)
- Health score: **83/100**
- Documentation score: **73/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

</details>

## MCP & Security

*MCP support*

The agent needs access to external tools and data through a standard protocol.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 23.4k 🚀 +117/d | **88** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Rom… | 🟢 Easy | — | — | 5.2k 🚀 +307/d | **85** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 5.1k 🚀 +84/d | **80** |
| 🏆 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Easy · OOTB | ✅ | — | 1.3k 🚀 +137/d | **78** |
| ✅ **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Real vs code-synthesized: held-out ROC-AUC 0.92 with whole sound families held out. Listening through a soundtrack: 93% of the sound effects placed in a 60 s film mix are detected as events (89% | 🟡 Some setup | — | — | 4.5k 🚀 +91/d | **74** |
| ✅ **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 9.2k 🚀 +55/d | **65** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.7k 🚀 +24/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k | **62** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.9k | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **57** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k | **56** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance 3,985 archived projects -- full source code snapshots from the game security ecosystem (prefixed ags-) | 🟢 Easy | — | — | 564 | **56** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 478 | **55** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 392 | **55** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 375 🚀 +6/d | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 744 | **52** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | This checkout is 4.0.4.dev0, a development version; the newest release is 4.0.3. | 🟢 Easy | — | — | 540 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **51** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | ⚠️ This project includes production-ready security features but is still under active development. | 🟡 Some setup | — | — | 371 | **50** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.8k | **46** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 478 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 417 | **42** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [superdesigndev/treg](https://github.com/superdesigndev/treg), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [QuantumNous/new-api](https://github.com/QuantumNous/new-api) *(+17 more)*

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

- Stars: **23,373** (+117.4/day over 5d)
- Health score: **88/100**
- Documentation score: **51/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-11

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

- Stars: **5,213** (~306.6/day lifetime average)
- Health score: **85/100**
- Documentation score: **77/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **5,054** (+83.6/day over 5d)
- Health score: **80/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, Cursor

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

- Stars: **1,287** (+137.4/day over 5d)
- Health score: **78/100**
- Documentation score: **41/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-10

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

- Stars: **4,483** (+91.0/day over 5d)
- Health score: **74/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-06
- Works with: Claude Code

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 153.6k 🚀 +253/d | **93** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 34.4k 🚀 +688/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 4.5k 🚀 +562/d | **84** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.3k 🚀 +48/d | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 19.9k 🚀 +26/d | **68** |
| ✅ **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 本项目仅用于协议学习、研究与个人自用。请优先使用官方客户端，不要使用主账号，不要共享账号，也不要用于商业转售。 | 🟢 Easy | — | — | 3.9k 🚀 +57/d | **67** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | and connect OpenCode, Pi, Qoder, WorkBuddy, Kilo, Cline, T3 Code and more through managed configs. | 🟡 Some setup | — | — | 18.4k 🚀 +26/d | **65** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 3.6k 🚀 +17/d | **60** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5.1k 🚀 +34/d | **56** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 295 | **56** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 323 | **53** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.9k 🚀 +6/d | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 517 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k 🚀 +5/d | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 546 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 给做 SEO 和独立开发的人用的 Agent Skills。建站、选词、发外链、查数据、复盘迭代，一整条链路都在这个仓库里，装完就能跑。 | 🟢 Easy | — | — | 283 | **51** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 966 🚀 +12/d | **50** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 326 | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 560 | **49** |

**Also does this:** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [spinabot/brigade](https://github.com/spinabot/brigade)

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

- Stars: **153,562** (+252.8/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **34,441** (+688.0/day over 5d)
- Health score: **91/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-11
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

- Stars: **4,499** (~562.4/day lifetime average)
- Health score: **84/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **32,261** (+47.6/day over 5d)
- Health score: **69/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **19,900** (+25.8/day over 5d)
- Health score: **68/100**
- Documentation score: **64/100**
- Language: Rust
- Last push: 2026-11-09
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

</details>

## Memory & Failover

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.2k 🚀 +26/d | **68** |
| ✅ **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | English \| 简体中文 \| 日本語 \| العربية \| Español \| 한국어 \| فارسی XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 18.8k 🚀 +7/d | **66** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 9.5k 🚀 +48/d | **63** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.9k 🚀 +18/d | **63** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.4k 🚀 +13/d | **58** |
| 🔹 **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | Context that stays with the work — across sessions, agents, and people. Coding tasks (SWE-bench Pro paired comparison): approximately 225.32 million input tokens per 100 tasks with PowerContext on, versus 302.18 million… | 🔴 Involved | — | — | 1.6k 🚀 +18/d | **56** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | Turn stateless LLMs into a stateful, compounding AI agent — portable across any IDE. | 🟢 Easy | — | — | 622 | **56** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.9k 🚀 +6/d | **55** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 411 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **53** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟡 Some setup | — | — | 550 🚀 +8/d | **53** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 437 | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 926 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 715 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 456 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 929 | **51** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 528 | **50** |
| 🔹 **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | Maestro is a multi-agent development orchestration platform with 39 specialists, an Express path for simple work, a 4-phase standard workflow for medium and complex work, persistent session state, and standalone review/… | 🟡 Some setup | — | — | 488 | **49** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 487 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 525 | **43** |

**Also does this:** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [affaan-m/ECC](https://github.com/affaan-m/ECC), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [spinabot/brigade](https://github.com/spinabot/brigade), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [felinics/Memoh](https://github.com/felinics/Memoh) *(+19 more)*

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

- Stars: **33,239** (+25.6/day over 5d)
- Health score: **68/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Cursor, Cline / Roo

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

- Stars: **18,821** (+7.3/day over 9d)
- Health score: **66/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-11
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

- Stars: **9,534** (+47.8/day over 5d)
- Health score: **63/100**
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

- Stars: **7,909** (+17.6/day over 5d)
- Health score: **63/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **1,406** (+13.2/day over 5d)
- Health score: **58/100**
- Documentation score: **70/100**
- License: MIT
- Language: Python
- Last push: 2026-10-23
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Droid

</details>

## Mobile

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 167.7k 🚀 +175/d | **98** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree. | 🟢 Turnkey · OOTB | ✅ | ✅ | 121.9k 🚀 +934/d | **92** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 21k 🚀 +1342/d | **87** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal. | 🟢 Turnkey · OOTB | ✅ | ✅ | 8.5k 🚀 +341/d | **86** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 23.8k 🚀 +104/d | **84** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | An AI assistant on your phone: say what you need, and it works your apps and the web until it's done. | 🟢 Easy | — | ✅ | 8.2k 🚀 +682/d | **81** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟡 Some setup | — | — | 2.6k 🚀 +113/d | **79** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 2.2k 🚀 +74/d | **73** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.1k 🚀 +26/d | **66** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Talk to Claude as usual. | 🟢 Easy | — | — | 5.3k 🚀 +18/d | **65** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2k 🚀 +25/d | **65** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.4k 🚀 +14/d | **64** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.6k 🚀 +14/d | **63** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | ✅ | 5.2k | **56** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.8k 🚀 +9/d | **54** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.2k 🚀 +5/d | **53** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.1k | **53** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 309 | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 556 | **50** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **48** |

**Also does this:** [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [makecindy/cindy](https://github.com/makecindy/cindy), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **167,723** (+174.6/day over 5d)
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

- Stars: **121,941** (+934.4/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **20,991** (+1342.4/day over 5d)
- Health score: **87/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **8,515** (~340.6/day lifetime average)
- Health score: **86/100**
- Documentation score: **51/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **23,783** (+103.8/day over 5d)
- Health score: **84/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

</details>

## Sharing

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 301k 🚀 +565/d | **89** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 7.8k 🚀 +105/d | **84** |
| 🏆 **[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)** | Reverse-engineer any video. | 🟢 Turnkey | — | ✅ | 6.8k 🚀 +569/d | **84** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 12.1k 🚀 +64/d | **75** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Large stores keep working: state reads page, so scopes above 64 MiB no longer fail, on iii 0.25.1. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.3k 🚀 +23/d | **70** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.6k 🚀 +19/d | **64** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k | **60** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **56** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | English \| 简体中文 \| 日本語 | 🟢 Easy | — | — | 493 | **54** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 563 | **47** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [QuantumNous/new-api](https://github.com/QuantumNous/new-api), [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck) *(+9 more)*

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

- Stars: **301,030** (+565.0/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-09
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

- Stars: **7,806** (+105.0/day over 5d)
- Health score: **84/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code

#### [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)

> Reverse-engineer any video.

**Core problems it solves**

- **Self-hostable** — *a video down, the remake recipe in capsule-cinema generates a new version that keeps the original's camera, motion, pacing and transitions and swaps…*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `brew install ffmpeg            # or: sudo apt install ffmpeg`
- Platforms mentioned: Linux, Web
- Turnkey. install via Homebrew install; needs git clone (build from source); one-click setup

**Facts**

- Stars: **6,826** (~568.8/day lifetime average)
- Health score: **84/100**
- Documentation score: **49/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex

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

- Stars: **12,147** (+64.0/day over 5d)
- Health score: **75/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **30,286** (+23.4/day over 5d)
- Health score: **70/100**
- Documentation score: **73/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 107.1k 🚀 +183/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 81.8k 🚀 +251/d | **90** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 155.3k 🚀 +101/d | **86** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | A toolbox of film styles made in code: 66 ready to use, and your own. You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. | 🟡 Some setup | — | ✅ | 14.7k 🚀 +368/d | **84** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 22.4k 🚀 +476/d | **78** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.9k 🚀 +20/d | **64** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.4k 🚀 +30/d | **61** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.4k 🚀 +17/d | **60** |
| 🔹 **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | DeepSeek Harness, OpenClaw, Hermes, Claude Code, Codex, Cursor, WorkBuddy, OpenCode, Pi...they all work! | 🟡 Some setup | — | — | 2.2k | **56** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2k 🚀 +11/d | **55** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 358 | **53** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote attaches to a running pi session through pi's official extension API. The extension channel (7001) binds to 127.0.0.1 by default. | 🟢 Easy | — | — | 328 | **53** |
| 🔹 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 3.8k | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 722 | **50** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [anomalyco/opencode](https://github.com/anomalyco/opencode), [openai/codex](https://github.com/openai/codex), [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [openfilm/openfilm](https://github.com/openfilm/openfilm), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [0sec-labs/0](https://github.com/0sec-labs/0), [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) *(+23 more)*

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

- Stars: **107,137** (+182.6/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **81,850** (+251.4/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **155,253** (+101.4/day over 5d)
- Health score: **86/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **14,686** (+368.4/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-10
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

- Stars: **22,378** (+476.4/day over 5d)
- Health score: **78/100**
- Documentation score: **23/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-03

</details>

## Failover

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 134.9k 🚀 +285/d | **89** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 6.8k 🚀 +129/d | **89** |
| 🏆 **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 6.7k 🚀 +187/d | **86** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | Turn the browser you already use into a workspace for your AI agent. | 🟢 Easy | — | — | 10.3k 🚀 +42/d | **68** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.7k 🚀 +8/d | **63** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 9.5k 🚀 +19/d | **63** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2k 🚀 +14/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.5k 🚀 +5/d | **58** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.9k 🚀 +6/d | **56** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 285 | **55** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.9k 🚀 +9/d | **50** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 678 | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 316 | **44** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [garrytan/gstack](https://github.com/garrytan/gstack), [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [xerj-org/xerj](https://github.com/xerj-org/xerj), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness), [totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids), [thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills), [1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code) *(+10 more)*

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

- Stars: **134,860** (+284.8/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-11
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

- Stars: **6,848** (+128.6/day over 5d)
- Health score: **89/100**
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

- Stars: **6,729** (~186.9/day lifetime average)
- Health score: **86/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-10
- Works with: Claude Code

#### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

> Turn the browser you already use into a workspace for your AI agent.

**Core problems it solves**

- **Automatic failover**
- **Skills & plugins** — *ection settings → Pairing link.*
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

- Stars: **10,314** (+41.8/day over 5d)
- Health score: **68/100**
- Documentation score: **60/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex, Cursor

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

- Stars: **27,746** (+8.4/day over 5d)
- Health score: **63/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

</details>

## Analytics

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 66.4k 🚀 +206/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Turnkey · OOTB | ✅ | — | 6.9k 🚀 +278/d | **84** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | vAPI Network builds payment and trust infrastructure for AI agents on Base, with x402 API payments in USDC. | 🟡 Some setup | — | — | 4.1k 🚀 +104/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 45.8k 🚀 +52/d | **72** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 4.1k 🚀 +49/d | **68** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends. | 🟢 Easy | — | — | 5.5k 🚀 +8/d | **63** |
| 🔹 **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.2k 🚀 +17/d | **61** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.9k 🚀 +12/d | **53** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 415 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 837 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 448 | **43** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [automazeio/ccpm](https://github.com/automazeio/ccpm), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

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

- Stars: **66,436** (+205.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-10
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

- Stars: **6,863** (+277.6/day over 5d)
- Health score: **84/100**
- Documentation score: **42/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-09
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

- Stars: **4,059** (~104.1/day lifetime average)
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

- Stars: **45,837** (+52.4/day over 5d)
- Health score: **72/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-11
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

- Stars: **4,098** (+49.0/day over 5d)
- Health score: **68/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-11-10
- Works with: Claude Code, Codex

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 226k 🚀 +221/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.6k 🚀 +252/d | **88** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 17.4k 🚀 +925/d | **85** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm lets your coding agent make videos, and lets you edit them. | 🟢 Easy | — | ✅ | 5.7k 🚀 +148/d | **80** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.4k 🚀 +10/d | **61** |
| 🔹 **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 Turnkey · OOTB | ✅ | ✅ | 3.5k 🚀 +8/d | **59** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 4.2k 🚀 +33/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 490 | **56** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 592 🚀 +9/d | **52** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 642 | **38** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [openai/codex](https://github.com/openai/codex), [qybaihe/bla](https://github.com/qybaihe/bla), [getpaseo/paseo](https://github.com/getpaseo/paseo), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [0sec-labs/0](https://github.com/0sec-labs/0), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch), [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [TencentCloud/Octop](https://github.com/TencentCloud/Octop) *(+22 more)*

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

- Stars: **226,035** (+221.4/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-11
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

- Stars: **15,633** (+252.0/day over 5d)
- Health score: **88/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-11
- Works with: Claude Code

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

- Stars: **17,372** (+925.2/day over 5d)
- Health score: **85/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex

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

- Stars: **5,739** (+147.8/day over 5d)
- Health score: **80/100**
- Documentation score: **37/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-09
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

- Stars: **15,397** (+9.6/day over 5d)
- Health score: **61/100**
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
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.6k 🚀 +27/d | **69** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.3k 🚀 +14/d | **59** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 927 🚀 +5/d | **57** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.4k 🚀 +5/d | **55** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 980 | **55** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 775 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 440 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 510 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 602 | **45** |

**Also does this:** [automazeio/ccpm](https://github.com/automazeio/ccpm), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

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

- Stars: **4,594** (+27.0/day over 5d)
- Health score: **69/100**
- Documentation score: **80/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-09
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

- Stars: **4,323** (+14.4/day over 5d)
- Health score: **59/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-11
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

- Stars: **927** (+4.8/day over 5d)
- Health score: **57/100**
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

- Stars: **4,429** (+5.0/day over 5d)
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

- Stars: **980** (+0.2/day over 5d)
- Health score: **55/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-11-06
- Works with: Claude Code, OpenCode

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k 🚀 +73/d | **76** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 9.8k 🚀 +86/d | **72** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 51.8k 🚀 +51/d | **69** |
| ✅ **[scenario-labs/skills](https://github.com/scenario-labs/skills)** | "Make a seamless brick texture, then upscale it to 2048 without breaking the tiling" "Generate four style-matched potion icons with transparent backgrounds for my RPG inventory" | 🟡 Some setup | — | — | 3.7k 🚀 +40/d | **66** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 6k | **50** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 523 | **50** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [decolua/9router](https://github.com/decolua/9router), [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [zai-org/ZCode](https://github.com/zai-org/ZCode), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [cita-777/metapi](https://github.com/cita-777/metapi), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth) *(+3 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **4,368** (+73.0/day over 5d)
- Health score: **76/100**
- Documentation score: **55/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-11
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **9,806** (+86.0/day over 5d)
- Health score: **72/100**
- Documentation score: **54/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-11
- Works with: Claude Code, Codex

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

- Stars: **51,751** (+51.2/day over 5d)
- Health score: **69/100**
- Documentation score: **75/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-11-11

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

- Stars: **3,674** (~40.4/day lifetime average)
- Health score: **66/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-11-10
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

- Stars: **5,954** (+0.8/day over 5d)
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile | Analytics, Failover |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Model Routing | MCP & Security, Sharing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Billing | Analytics, Failover |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Desktop UI, Isolation & Teams |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | MCP & Security, Model Routing |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Isolation & Teams | Desktop UI, Failover |
| **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | Analytics | Isolation & Teams |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI, Model Routing |
| **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | Isolation & Teams | Memory & Failover, Sharing |
| **[openai/codex](https://github.com/openai/codex)** | Failover | Desktop UI, Model Routing |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Sharing | MCP & Security, Memory & Failover |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Isolation & Teams | Analytics, Sharing |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile | Analytics, MCP & Security |
| **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | Mobile | Failover, Model Routing |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Failover | Desktop UI |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Desktop UI | Desktop UI, Model Routing |
| **[qybaihe/bla](https://github.com/qybaihe/bla)** | MCP & Security | Desktop UI, Desktop UI |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Desktop UI, Isolation & Teams |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Sharing | MCP & Security |
| **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Analytics | Desktop UI |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | MCP & Security, Memory & Failover |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI, Model Routing |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Isolation & Teams | Mobile, Sharing |
| **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | Desktop UI | Model Routing |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | MCP & Security | Desktop UI |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | MCP & Security, Model Routing |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Isolation & Teams, Sharing |
| **[0sec-labs/0](https://github.com/0sec-labs/0)** | MCP & Security | Desktop UI, Model Routing |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Isolation & Teams | Desktop UI, MCP & Security |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Analytics | Desktop UI, Model Routing |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Sharing | MCP & Security, Model Routing |
| **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | MCP & Security | Desktop UI |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Mobile | Desktop UI, Failover |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Analytics | Billing, Model Routing |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Mobile, Model Routing |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Isolation & Teams | Analytics, Desktop UI |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Isolation & Teams | Desktop UI, MCP & Security |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Sharing | MCP & Security, Memory & Failover |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Billing, Model Routing |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Analytics | MCP & Security, Sharing |
| **[decolua/9router](https://github.com/decolua/9router)** | Billing | Analytics |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Analytics, MCP & Security |
| **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | Billing | Analytics, Sharing |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Memory & Failover | Desktop UI, Failover |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Desktop UI, Model Routing |
| **[scenario-labs/skills](https://github.com/scenario-labs/skills)** | Analytics | Desktop UI, Model Routing |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Billing | Analytics, Model Routing |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Desktop UI, MCP & Security |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, MCP & Security |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | MCP & Security, Sharing |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Sharing | Analytics, Model Routing |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Analytics, Sharing |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Analytics | Desktop UI, MCP & Security |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Failover | MCP & Security, Model Routing |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Failover | Desktop UI, Model Routing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Analytics | MCP & Security, Model Routing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Sharing | Billing, Memory & Failover |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Analytics, MCP & Security |
| **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | Sharing | Analytics |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Memory & Failover, Sharing |
| **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Desktop UI | Model Routing |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | MCP & Security | Failover, Sharing |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Failover | Desktop UI, Memory & Failover |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Memory & Failover | Desktop UI, Model Routing |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Isolation & Teams | Analytics, Sharing |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | MCP & Security | Memory & Failover |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Desktop UI |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Mobile | Failover |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Sharing | Isolation & Teams, Memory & Failover |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | Model Routing | Desktop UI, Memory & Failover |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Failover | Desktop UI, Model Routing |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | MCP & Security | Desktop UI, Memory & Failover |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Failover, Memory & Failover |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation & Teams | Desktop UI, Mobile |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | MCP & Security | Failover, Memory & Failover |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI, Model Routing |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Failover, Memory & Failover |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Model Routing |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Memory & Failover | Failover, Model Routing |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI, Memory & Failover |
| **[routatic/proxy](https://github.com/routatic/proxy)** | Providers | Failover, Model Routing |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Isolation & Teams | Memory & Failover, Sharing |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Isolation & Teams | Analytics, MCP & Security |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | MCP & Security | Desktop UI, Desktop UI |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Failover | Desktop UI, Memory & Failover |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Isolation & Teams | Analytics, Providers |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | MCP & Security |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Mobile | Model Routing |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Mobile | Desktop UI, MCP & Security |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Memory & Failover |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Memory & Failover | MCP & Security, Sharing |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Model Routing | Desktop UI |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Billing | Analytics, Mobile |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | Billing | Sharing |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Failover, Memory & Failover |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Memory & Failover | Desktop UI, Desktop UI |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation & Teams | Desktop UI, Desktop UI |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP & Security | Desktop UI, Model Routing |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Memory & Failover | Desktop UI, MCP & Security |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Billing | Failover |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Isolation & Teams, MCP & Security |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Memory & Failover | Failover |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Desktop UI, MCP & Security |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Isolation & Teams | Mobile, Sharing |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Desktop UI |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Desktop UI, Memory & Failover |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Memory & Failover | Desktop UI, Model Routing |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Desktop UI, Providers |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Isolation & Teams | Desktop UI, Memory & Failover |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Memory & Failover, Model Routing |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Mobile | Failover, Memory & Failover |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Isolation & Teams, Sharing |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Billing | Failover, Sharing |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Failover | Memory & Failover |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Analytics, Desktop UI |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Memory & Failover | Desktop UI, Failover |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Analytics | MCP & Security, Sharing |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | MCP & Security | Model Routing |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Billing | Memory & Failover, Model Routing |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation & Teams | Analytics, Desktop UI |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Billing | Failover, Sharing |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Memory & Failover, Model Routing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Analytics | Desktop UI, Isolation & Teams |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Isolation & Teams | Analytics, Analytics |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Memory & Failover | Failover, Sharing |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | MCP & Security | Desktop UI |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Failover | MCP & Security, Memory & Failover |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Memory & Failover | Failover |
| **[IBM/mcp](https://github.com/IBM/mcp)** | MCP & Security | Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.22x the stars (34,441 vs 153,562) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 61.61x the stars (19,900 vs 323) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 68.52x the stars (30,286 vs 442) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.99x the stars (19,900 vs 2,492) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 31.18x the stars (11,911 vs 382) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 37.19x the stars (34,441 vs 926) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 151.45x the stars (49,523 vs 327) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.83x the stars (34,211 vs 929) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.31x the stars (49,523 vs 366) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 173.16x the stars (49,523 vs 286) | 🤖 auto (high) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 219.99x the stars (107,137 vs 487) | 🤖 auto (high) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 33.84x the stars (11,911 vs 352) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 99.62x the stars (30,286 vs 304) | 🤖 auto (high) |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 105.90x the stars (30,286 vs 286) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.41x the stars (141,174 vs 4,969) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.24x the stars (49,523 vs 3,740) | 🤖 auto (high) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 233.72x the stars (301,030 vs 1,288) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 13.40x the stars (30,286 vs 2,260) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 133.85x the stars (49,523 vs 370) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.84x the stars (11,911 vs 413) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 6.98x the stars (49,523 vs 7,100) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.64x the stars (23,783 vs 489) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.73x the stars (49,523 vs 318) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 480.88x the stars (301,030 vs 626) | 🤖 auto (high) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 23.24x the stars (34,211 vs 1,472) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 35.10x the stars (19,900 vs 567) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.37x the stars (301,030 vs 6,223) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 87.50x the stars (34,211 vs 391) | 🤖 auto (high) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 91.71x the stars (49,523 vs 540) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 35.30x the stars (49,523 vs 1,403) | 🤖 auto (high) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 7.21x the stars (113,060 vs 15,683) | 🤖 auto (high) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 27.60x the stars (301,030 vs 10,905) | 🤖 auto (high) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.16x the stars (49,523 vs 3,762) | 🤖 auto (medium) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 10.11x the stars (5,054 vs 500) | 🤖 auto (medium) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 32.56x the stars (18,821 vs 578) | 🤖 auto (medium) |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | 21.88x the stars (17,372 vs 794) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.46x the stars (23,783 vs 5,328) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.30x the stars (1,406 vs 426) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 76.54x the stars (49,523 vs 647) | 🤖 auto (medium) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 10.59x the stars (30,286 vs 2,859) | 🤖 auto (high) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 65.25x the stars (49,523 vs 759) | 🤖 auto (medium) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.30x the stars (1,169 vs 508) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.56x the stars (1,406 vs 550) | 🤖 auto (medium) |
| **[google/artemis](https://github.com/google/artemis)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 9.73x the stars (167,723 vs 17,231) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.64x the stars (952 vs 580) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.63x the stars (1,406 vs 863) | 🤖 auto (high) |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 19.87x the stars (113,060 vs 5,689) | 🤖 auto (medium) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,523 vs 27,877) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,088 vs 512) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui | 27.9k | 🔻 Superseded | 1.78x the stars (49,523 vs 27,877) |
| **[google/artemis](https://github.com/google/artemis)** | mobile | 17.2k | 🔻 Superseded | 9.73x the stars (167,723 vs 17,231) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | isolation-teams | 15.7k | 🔻 Superseded | 7.21x the stars (113,060 vs 15,683) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | sharing | 10.9k | 🔻 Superseded | 27.60x the stars (301,030 vs 10,905) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | desktop-ui | 7.1k | 🔻 Superseded | 6.98x the stars (49,523 vs 7,100) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | sharing | 6.2k | 🔻 Superseded | 48.37x the stars (301,030 vs 6,223) |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | isolation-teams | 5.7k | 🔻 Superseded | 19.87x the stars (113,060 vs 5,689) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.3k | 🔻 Superseded | 4.46x the stars (23,783 vs 5,328) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-teams | 5k | 🔻 Superseded | 28.41x the stars (141,174 vs 4,969) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | desktop-ui | 3.8k | 🔻 Superseded | 13.16x the stars (49,523 vs 3,762) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui | 3.7k | 🔻 Superseded | 13.24x the stars (49,523 vs 3,740) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | sharing | 2.9k | 🔻 Superseded | 10.59x the stars (30,286 vs 2,859) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 Superseded | 7.99x the stars (19,900 vs 2,492) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | sharing | 2.3k | 🔻 Superseded | 13.40x the stars (30,286 vs 2,260) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation-teams | 1.5k | 🔻 Superseded | 23.24x the stars (34,211 vs 1,472) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | desktop-ui | 1.4k | 🔻 Superseded | 35.30x the stars (49,523 vs 1,403) |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | sharing | 1.3k | 🔻 Superseded | 233.72x the stars (301,030 vs 1,288) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-teams | 929 | 🔻 Superseded | 36.83x the stars (34,211 vs 929) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 926 | 🔻 Superseded | 37.19x the stars (34,441 vs 926) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | memory-failover | 863 | 🔻 Superseded | 1.63x the stars (1,406 vs 863) |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | desktop-ui-2 | 794 | 🔻 Superseded | 21.88x the stars (17,372 vs 794) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 759 | 🔻 Superseded | 65.25x the stars (49,523 vs 759) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 647 | 🔻 Superseded | 76.54x the stars (49,523 vs 647) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | sharing | 626 | 🔻 Superseded | 480.88x the stars (301,030 vs 626) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | desktop-ui | 580 | 🔻 Superseded | 1.64x the stars (952 vs 580) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | memory-failover | 578 | 🔻 Superseded | 32.56x the stars (18,821 vs 578) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | billing | 567 | 🔻 Superseded | 35.10x the stars (19,900 vs 567) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-failover | 550 | 🔻 Superseded | 2.56x the stars (1,406 vs 550) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | desktop-ui | 540 | 🔻 Superseded | 91.71x the stars (49,523 vs 540) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 512 | 🔻 Superseded | 2.12x the stars (1,088 vs 512) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | mcp-security | 508 | 🔻 Superseded | 2.30x the stars (1,169 vs 508) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-security | 500 | 🔻 Superseded | 10.11x the stars (5,054 vs 500) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 489 | 🔻 Superseded | 48.64x the stars (23,783 vs 489) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 487 | 🔻 Superseded | 219.99x the stars (107,137 vs 487) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | sharing | 442 | 🔻 Superseded | 68.52x the stars (30,286 vs 442) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | memory-failover | 426 | 🔻 Superseded | 3.30x the stars (1,406 vs 426) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | isolation-teams | 413 | 🔻 Superseded | 28.84x the stars (11,911 vs 413) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | isolation-teams | 391 | 🔻 Superseded | 87.50x the stars (34,211 vs 391) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-teams | 382 | 🔻 Superseded | 31.18x the stars (11,911 vs 382) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 370 | 🔻 Superseded | 133.85x the stars (49,523 vs 370) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui | 366 | 🔻 Superseded | 135.31x the stars (49,523 vs 366) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | isolation-teams | 352 | 🔻 Superseded | 33.84x the stars (11,911 vs 352) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | desktop-ui | 327 | 🔻 Superseded | 151.45x the stars (49,523 vs 327) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 323 | 🔻 Superseded | 61.61x the stars (19,900 vs 323) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 318 | 🔻 Superseded | 155.73x the stars (49,523 vs 318) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | sharing | 304 | 🔻 Superseded | 99.62x the stars (30,286 vs 304) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 286 | 🔻 Superseded | 173.16x the stars (49,523 vs 286) |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | sharing | 286 | 🔻 Superseded | 105.90x the stars (30,286 vs 286) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-11 11:55 UTC. 230 live tools · 122 candidates rejected by the quality gates.</sub>
