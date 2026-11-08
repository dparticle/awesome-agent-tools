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

**219 tools** across **11 categories** · **58 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-08 11:20 UTC**

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

- [Mobile](#mobile) — 45 tools
- [Desktop UI](#desktop-ui) — 36 tools
- [Teams](#teams) — 20 tools
- [MCP & Security](#mcp-security) — 29 tools
- [Sharing](#sharing) — 21 tools
- [Billing](#billing) — 16 tools
- [Billing](#billing) — 14 tools
- [Model Routing](#model-routing) — 12 tools
- [Desktop UI](#desktop-ui) — 9 tools
- [Analytics](#analytics) — 8 tools
- [Providers](#providers) — 9 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Mobile

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 167.2k 🚀 +195/d | **98** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree. | 🟢 Turnkey · OOTB | ✅ | ✅ | 118.9k 🚀 +966/d | **92** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production… | 🟡 Some setup | — | — | 140.7k 🚀 +390/d | **91** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 112.2k 🚀 +292/d | **89** |
| 🏆 **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12k 🚀 +353/d | **87** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 23.5k 🚀 +112/d | **85** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 17.7k 🚀 +275/d | **83** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.cursor — login and session history managed exclusively by the Cursor CLI. | 🟡 Some setup | — | — | 6.3k 🚀 +250/d | **83** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟡 Some setup | — | — | 2.2k 🚀 +165/d | **80** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | An open catalog of components for Claude Code, installable with one command. | 🟢 Easy | — | — | 33.2k (+67/d) | **77** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 2k 🚀 +99/d | **77** |
| ✅ **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | ThinkRail is the agentic IDE that gets better every time you use it — learning your project through living specs today, and building its own capabilities tomorrow. | 🟢 Turnkey | — | ✅ | 7.9k (+64/d) | **75** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 48.3k 🚀 +56/d | **74** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 85.1k 🚀 +38/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.1k 🚀 +18/d | **71** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.9k 🚀 +19/d | **69** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2k 🚀 +40/d | **67** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.1k 🚀 +27/d | **66** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 8.7k 🚀 +29/d | **65** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.5k 🚀 +14/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.4k 🚀 +15/d | **64** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.8k 🚀 +20/d | **63** |
| ✅ **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **62** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.2k 🚀 +27/d | **61** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.3k 🚀 +15/d | **58** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.2k 🚀 +22/d | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Nothing is sent until you explicitly type y at the confirmation prompt. Or run agent-deck feedback from the CLI (rating 1-5) | 🟡 Some setup | — | — | 1.2k 🚀 +5/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 604 | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 594 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 490 | **56** |

**Also does this:** [spinabot/brigade](https://github.com/spinabot/brigade), [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)

*…and 15 more in [the full index](data/index.json).*

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

- Stars: **167,193** (+195.0/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [stablyai/orca](https://github.com/stablyai/orca)

> Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree.

**Core problems it solves**

- **Multi-account switching** — *- **Dictation**: press a shortcut and talk.*
- **Remote control** — *S Apple Silicon · macOS Intel · Windows (.exe) · Linux AppImage · All builds*
- **Mobile access**
- **Multi-agent orchestration** — *r coding agent in parallel, each in its own worktree.*
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

- Stars: **118,895** (+966.2/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

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

- Stars: **140,715** (+390.4/day over 5d)
- Health score: **91/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08
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

- Stars: **112,157** (+291.6/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08
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

- Stars: **12,018** (+353.4/day over 5d)
- Health score: **87/100**
- Documentation score: **54/100**
- License: NOASSERTION
- Language: Rust
- Last push: 2026-11-08
- Works with: Claude Code, Codex

</details>

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 Easy | — | ✅ | 186.6k 🚀 +657/d | **87** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 40 mandatory rules (R-01 to R-40) in three tiers: Hard Gate, Purpose-Gate, and Quality Locks. A Delivery Gate: a mandatory PASS/FAIL report in four blocks, run before anything ships. | 🟢 Turnkey · OOTB | ✅ | — | 8.6k 🚀 +112/d | **85** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 25.9k 🚀 +318/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 66.3k 🚀 +1700/d | **83** |
| 🏆 **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 8.6k 🚀 +80/d | **81** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 2,926+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 49.3k 🚀 +53/d | **78** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 6.3k 🚀 +89/d | **73** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 8.3k 🚀 +238/d | **71** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 6.3k 🚀 +63/d | **67** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.2k 🚀 +42/d | **64** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 4.7k 🚀 +60/d | **64** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +21/d | **63** |
| ✅ **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.7k 🚀 +18/d | **62** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **57** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k 🚀 +4/d | **56** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 941 | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 553 | **56** |
| 🔹 **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | the current dotnet-skills CLI remains skill-first; repo-owned agents can evolve and ship on their own track. | 🟢 Easy · OOTB | ✅ | — | 509 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. name -- Use kebab-case, 1-64 characters (e.g., csv-data-summarizer, not CSV Data Summarizer). | 🟡 Some setup | — | — | 1.1k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 920 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 770 | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 532 | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 442 | **52** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 295 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.5k 🚀 +6/d | **51** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **51** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) External-content sanitizing (leyline) strips invisible | 🟡 Some setup | — | — | 348 | **51** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [garrytan/gstack](https://github.com/garrytan/gstack), [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) *(+32 more)*

*…and 6 more in [the full index](data/index.json).*

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

- Stars: **186,603** (+657.2/day over 5d)
- Health score: **87/100**
- Documentation score: **48/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-29
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)

> A filter, not a style guide.

**Core problems it solves**

- **Skills & plugins** — *ll them (this project or everywhere), and which agents you use, then copies the folders and writes the pointer that reloads antislop every session.*
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

- Stars: **8,626** (+112.2/day over 12d)
- Health score: **85/100**
- Documentation score: **54/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **25,872** (+317.8/day over 5d)
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

- Stars: **66,289** (+1699.6/day over 5d)
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

- Stars: **8,591** (+80.0/day over 5d)
- Health score: **81/100**
- Documentation score: **67/100**
- License: MIT
- Language: Go
- Last push: 2026-11-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Teams

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 299.4k 🚀 +661/d | **89** |
| 🏆 **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | opencode support is experimental: it was tested on 1.19.5 and 2.2.0 only, and not in the Cursor Agent support is experimental. | 🟢 Easy | — | ✅ | 5k 🚀 +191/d | **83** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. Routines: ask a Bot to do something on a schedule and it does, running as y… | 🟢 Easy | — | — | 10.4k 🚀 +92/d | **80** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project | 🟡 Some setup | — | — | 15.4k 🚀 +76/d | **76** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 11.8k 🚀 +51/d | **74** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 11.9k 🚀 +63/d | **74** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.1k 🚀 +21/d | **68** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.2k 🚀 +18/d | **68** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 9.4k 🚀 +65/d | **66** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.6k 🚀 +22/d | **65** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.8k 🚀 +19/d | **63** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.4k | **60** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.1k 🚀 +6/d | **55** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Z0 round 2, 16 repositories, Claude Code with hippo against its built-in memory: no extra cost (ratio 0.999 [0.962, 1.037]) and about 12% less spent on teach and correction turns. Decay tied with decay switched off. | 🟡 Some setup | — | — | 790 | **55** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 410 | **55** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **54** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | English \| 简体中文 \| 日本語 | 🟢 Easy | — | — | 492 | **54** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k 🚀 +6/d | **53** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 428 | **52** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) *(+5 more)*

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

- Stars: **299,397** (+660.6/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-06
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

- Stars: **4,973** (~191.3/day lifetime average)
- Health score: **83/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)

> OpenBot is a self-hostable workspace for AI coworkers.

**Core problems it solves**

- **Automatic failover** — *et responses and the rest get chat.*
- **Model / provider routing**
- **Session persistence**
- **MCP support** — *- **Governed MCP**: Google Drive, Notion and the public-web research providers Parallel, Exa and Firecrawl ship in the catalogue, and Composio broker…*
- **Security & isolation** — *who gets in**: /admin/people lists everybody who has signed in, promotes and demotes them, and removes access, which ends the session they are using…*
- **Self-hostable** — *Defaults to ../examples/fintech.*
- **GUI / desktop app** — *your own coworkers, channels, and skills.*
- **Notifications**

**Getting it running**

- Setup: 🟢 **Easy** (friction 33/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx --yes copilotkit@latest login`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs docker run; configure sign-in required, database dependency; GUI application

**Facts**

- Stars: **10,432** (+92.4/day over 5d)
- Health score: **80/100**
- Documentation score: **69/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08

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
- Some setup. install via Homebrew install, scoop install; needs docker run, git clone (build from source); configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **15,362** (+75.6/day over 5d)
- Health score: **76/100**
- Documentation score: **71/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-08
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

- Stars: **11,775** (+50.8/day over 5d)
- Health score: **74/100**
- Documentation score: **79/100**
- License: MIT
- Language: Python
- Last push: 2026-11-07
- Works with: Claude Code, Codex, OpenCode

</details>

## MCP & Security

*Security & isolation*

Agents run arbitrary code and hold credentials; blast radius must be contained.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 23k 🚀 +125/d | **89** |
| 🏆 **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Real vs code-synthesized: held-out ROC-AUC 0.92 with whole sound families held out. Listening through a soundtrack: 93% of the sound effects placed in a 60 s film mix are detected as events (89% | 🟡 Some setup | — | — | 4.2k 🚀 +118/d | **80** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 17k 🚀 +132/d | **79** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 4.8k 🚀 +71/d | **78** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.6k 🚀 +26/d | **63** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **62** |
| 🔹 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 8.9k 🚀 +39/d | **61** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **56** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance 3,985 archived projects -- full source code snapshots from the game security ecosystem (prefixed ags-) | 🟢 Easy | — | — | 555 🚀 +5/d | **56** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 474 | **55** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Investigate vulnerabilities, review findings, and work on fixes in your browser. | 🟢 Easy · OOTB | ✅ | — | 604 | **54** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 392 🚀 +12/d | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 389 | **54** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.1k | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 740 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 514 | **52** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | ⚠️ This project includes production-ready security features but is still under active development. | 🟡 Some setup | — | — | 371 | **52** |
| 🔹 **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | A self-hosted search gateway for AI agents and AI clients. Client API compatibility: v0.3.1 includes the first SearXNG, Exa, Tavily, Search1API and Firecrawl single-page adapters. | 🔴 Involved | — | — | 1.3k | **51** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | This checkout is 4.0.3. | 🟢 Easy | — | — | 534 | **51** |
| 🔹 **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | Maestro is a multi-agent development orchestration platform with 39 specialists, an Express path for simple work, a 4-phase standard workflow for medium and complex work, persistent session state, and standalone review/… | 🟡 Some setup | — | — | 486 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **51** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | This repository is essentially an LLM chat desktop application based on MCP. Windows: The MCP SDK includes a workaround specifically for Windows systems, as documented in ISSUE 101. | 🟢 Easy | — | ✅ | 1.2k | **47** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 560 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.8k | **46** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | This repository is YALC 1.0, the first generation and the open-source one. Rate limiting — DB-backed token bucket on all external sends | 🔴 Involved | — | — | 326 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 417 | **42** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [garrytan/gstack](https://github.com/garrytan/gstack), [yetone/magpie](https://github.com/yetone/magpie), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [superdesigndev/treg](https://github.com/superdesigndev/treg), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [QuantumNous/new-api](https://github.com/QuantumNous/new-api) *(+14 more)*

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

- Stars: **22,990** (+125.2/day over 5d)
- Health score: **89/100**
- Documentation score: **51/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-08

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

- Stars: **4,220** (+117.6/day over 5d)
- Health score: **80/100**
- Documentation score: **62/100**
- License: MIT
- Language: Python
- Last push: 2026-11-06
- Works with: Claude Code

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

- Stars: **16,981** (+132.4/day over 5d)
- Health score: **79/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

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

- Stars: **4,780** (+71.2/day over 5d)
- Health score: **78/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-07
- Works with: Claude Code, Codex, Cursor

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

- Stars: **15,591** (+26.0/day over 5d)
- Health score: **63/100**
- Documentation score: **45/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-30
- Works with: Codex

</details>

## Sharing

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 106.6k 🚀 +183/d | **95** |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 152.7k 🚀 +247/d | **93** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 81k 🚀 +264/d | **90** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 6.5k 🚀 +154/d | **89** |
| 🏆 **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 6.5k 🚀 +197/d | **85** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.8k 🚀 +22/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Crew works without Obsidian. | 🟢 Easy | — | — | 5.2k 🚀 +18/d | **64** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.7k 🚀 +9/d | **63** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2k 🚀 +10/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.5k 🚀 +6/d | **59** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.9k 🚀 +4/d | **58** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 292 | **56** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 5.1k | **55** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). api-route: OpenAI-compatible Chat Completions preset for API Route. | 🔴 Involved | — | — | 1.8k 🚀 +5/d | **55** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 452 | **52** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.9k 🚀 +16/d | **51** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 559 | **51** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 284 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 676 | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 316 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 524 | **43** |

**Also does this:** [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [cordum-io/cordum](https://github.com/cordum-io/cordum)

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

- Stars: **106,562** (+183.4/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **152,681** (+246.8/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **81,025** (+263.8/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-08
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **6,483** (+153.8/day over 5d)
- Health score: **89/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-11-05
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

- Stars: **6,504** (~197.1/day lifetime average)
- Health score: **85/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-16
- Works with: Claude Code

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 32.1k 🚀 +634/d | **91** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 133.6k 🚀 +130/d | **89** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 4k 🚀 +808/d | **83** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5k 🚀 +199/d | **74** |
| ✅ **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 本项目仅用于协议学习、研究与个人自用。请优先使用官方客户端，不要使用主账号，不要共享账号，也不要用于商业转售。 | 🟡 Some setup | — | — | 3.7k 🚀 +65/d | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 19.8k 🚀 +28/d | **68** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.1k 🚀 +44/d | **67** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | and connect OpenCode, Pi, Qoder, WorkBuddy, Kilo, Cline, T3 Code and more through managed configs. | 🟡 Some setup | — | — | 18.3k 🚀 +23/d | **64** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 311 🚀 +4/d | **53** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.9k 🚀 +8/d | **52** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 545 🚀 +5/d | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k 🚀 +7/d | **51** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 921 | **51** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 512 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Local token usage, API-equivalent cost (anthropic-builtin-2026-10-14), recent sessions, and output speed from Claude Code session logs. | 🟡 Some setup | — | — | 321 | **50** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [cita-777/metapi](https://github.com/cita-777/metapi)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching** — *count can go through a proxy of its own.*
- **Quota & usage management** — *one key that matters in the agent's own config.*
- **Multi-agent orchestration** — ***Sync** Back up to a file, or sync machines over WebDAV (Nutstore, Nextcloud…), S3, or an encrypted GitHub repository backup*
- **Model / provider routing** — *y, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to.*
- **API gateway / proxy** — *awei Cloud MaaS · Volcengine Ark · Mistral · Voyage AI · Groq · Nous Portal · xAI · OpenRouter · Together · Fireworks · SiliconFlow · NVIDIA NIM · Mo…*
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

- Stars: **32,056** (+633.6/day over 5d)
- Health score: **91/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-08
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

- Stars: **133,626** (+129.6/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-08
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)

> 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。

**Core problems it solves**

- **Quota & usage management**
- **API gateway / proxy** — *Claude Code、Codex 和 ACP（官方 Codex ACP 适配器）跑通了多轮问答和跨进程会话续接；飞书跑通了发送、按钮回调和卡片更新；四种 Webhook 模板只在本地模拟服务上验证过，GitLab Webhook 按官方文档的格式测试，没连过真实 GitLab。*
- **Usage analytics** — *上验证过，GitLab Webhook 按官方文档的格式测试，没连过真实 GitLab。*
- **Session persistence** — *下面的性能数字 npm run benchmark ### 实测性能 Apple M5 Pro、24 GB、Node 24.21.0。*
- **MCP support** — *。 给 GitHub PR 打上 deliver 标签后，它会自己跟进到上线：审代码 → 等 CI → 合并 PR → 等部署 → 核对线上版本。审查和交付配置只从 main 读取，绝不在接单电脑上检出或运行 PR 里的代码；排队、并发和重试直接复用内核。*
- **Notifications** — *则写 "resume": true 就接着上一轮的会话。*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 19/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/KKKKhazix/agent-autoloop/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via curl | sh installer, PowerShell irm | iex installer; configure API key configuration, database dependency

**Facts**

- Stars: **4,040** (~808.0/day lifetime average)
- Health score: **83/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **4,964** (+199.2/day over 5d)
- Health score: **74/100**
- Documentation score: **27/100**
- License: MIT
- Last push: 2026-09-06
- Works with: Claude Code, Codex, Cursor

#### [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)

> 本项目仅用于协议学习、研究与个人自用。请优先使用官方客户端，不要使用主账号，不要共享账号，也不要用于商业转售。

**Core problems it solves**

- **Multi-account switching** — *：将 WorkBuddy（国际版/国内版）与 CodeArts 封装为标准 OpenAI 格式（Chat Completions / Responses），无缝支持 Codex、Claude Code、NextChat 等各类客户端。*
- **Quota & usage management**
- **Automatic failover** — *（Chat Completions / Responses），无缝支持 Codex、Claude Code、NextChat 等各类客户端。*
- **Mobile access** — *adge()，三种出口各回各的；「模型准入」的候选清单也补上 ?realm=codearts（它的 13 个模型与 intl / cn 完全不交集，以前一个都选不到、只能手填 id），绑定了出口的 Key 只列该出口的目录并在清单上方标出出口，未绑定（跟随面板切换）的才取全量；清单按出口分别缓存，…*
- **Model / provider routing** — *在改用 i18n 翻译前保留的原文比对，三种语言的分组结果一致；另补上漏归的「选择网页活跃提示词」（原来被归到「日志与系统」）。*
- **API gateway / proxy** — *# WorkBuddy2API-Hub — 国际版、国内版多账号网关中枢*
- **Quota sharing / splitting**
- **Billing & metering**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 42/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/ardeyouxipianyi/workbuddy2api-hub/main/quick-deploy.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via curl | sh installer; needs docker compose up; configure API key configuration, OAuth login flow; Chinese: beginner/one-click framing

**Facts**

- Stars: **3,698** (~64.9/day lifetime average)
- Health score: **69/100**
- Documentation score: **54/100**
- License: MIT
- Language: Python
- Last push: 2026-11-08
- Works with: Claude Code, Codex

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 65.8k 🚀 +245/d | **91** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 7.6k 🚀 +109/d | **84** |
| ✅ **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Easy | — | — | 6k 🚀 +425/d | **77** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 45.7k 🚀 +58/d | **73** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：从一部 20 章的原著改编，分镜 20 镜，逐镜生成后剪成成片， 字幕、系统面板与音效在剪辑时叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 3.9k 🚀 +47/d | **68** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 5.5k 🚀 +11/d | **64** |
| 🔹 **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.1k 🚀 +16/d | **61** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.9k 🚀 +16/d | **55** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 直接找：接口一览 ｜ 五分钟上手 ｜ 易支付协议兼容接入 ｜ 到账账号与收款分配 ｜ 微信 JSAPI 公众号配置 ｜ 文档目录 ｜ 常见问题 | 🟢 Easy | — | — | 330 | **52** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 831 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 413 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 447 | **43** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [decolua/9router](https://github.com/decolua/9router), [spinabot/brigade](https://github.com/spinabot/brigade), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

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

- Stars: **65,751** (+244.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-06
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

- Stars: **7,616** (+108.8/day over 5d)
- Health score: **84/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-08
- Works with: Claude Code

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

- Stars: **5,971** (+424.8/day over 5d)
- Health score: **77/100**
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

- Stars: **45,657** (+58.2/day over 5d)
- Health score: **73/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-07
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

- Stars: **3,945** (+46.6/day over 5d)
- Health score: **68/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-11-08
- Works with: Claude Code, Codex

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 154.9k 🚀 +116/d | **89** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | A toolbox of film styles made in code: 66 ready to use, and your own. You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. | 🟡 Some setup | — | ✅ | 13.6k 🚀 +418/d | **84** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 21k 🚀 +1102/d | **80** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.3k 🚀 +30/d | **61** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 11.3k 🚀 +7/d | **58** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2k 🚀 +10/d | **55** |
| 🔹 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 🔄 一键切换服务商：保存多家服务的 Base URL 与 API Key，点击即可将配置应用到目标工具，支持随时切换与还原。 🛡️ 配置无损与状态保护：修改前提供配置差异预览。 | 🟡 Some setup | — | ✅ | 3.8k | **54** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 355 | **53** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote attaches to a running pi session through pi's official extension API. The extension channel (7001) binds to 127.0.0.1 by default. | 🟢 Easy | — | — | 313 🚀 +7/d | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 718 | **50** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 477 | **46** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 481 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate), [zai-org/ZCode](https://github.com/zai-org/ZCode), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills), [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [tigicion/dao-code](https://github.com/tigicion/dao-code) *(+9 more)*

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

- Stars: **154,948** (+115.6/day over 5d)
- Health score: **89/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-06
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

- Stars: **13,550** (+418.2/day over 5d)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-08
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

- Stars: **21,017** (+1102.4/day over 5d)
- Health score: **80/100**
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

- Stars: **11,261** (+29.8/day over 5d)
- Health score: **61/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

#### [openai/codex-security](https://github.com/openai/codex-security)

> Codex Security helps you find, investigate, and fix vulnerabilities in your code.

**Core problems it solves**

- **Model / provider routing**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @openai/codex-security`
- Platforms mentioned: Linux, Web
- Some setup. install via npx one-liner; needs npm install/build; configure API key configuration, sign-in required

**Facts**

- Stars: **11,327** (+7.0/day over 5d)
- Health score: **58/100**
- Documentation score: **41/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-08
- Works with: Codex

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 225.4k 🚀 +232/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 14.9k 🚀 +320/d | **88** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 14.3k 🚀 +670/d | **84** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm lets your coding agent make videos, and lets you edit them. | 🟢 Easy | — | ✅ | 5.3k 🚀 +151/d | **80** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.4k 🚀 +11/d | **62** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | One 8 KB skill file that does what REA does: no MCP server, no 207 tools, no setup. | 🟢 Easy | — | — | 4.1k 🚀 +29/d | **57** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 485 | **56** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 558 🚀 +8/d | **51** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 641 | **38** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [stablyai/orca](https://github.com/stablyai/orca), [yetone/magpie](https://github.com/yetone/magpie), [openai/codex](https://github.com/openai/codex), [getpaseo/paseo](https://github.com/getpaseo/paseo), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [TencentCloud/Octop](https://github.com/TencentCloud/Octop) *(+45 more)*

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

- Stars: **225,392** (+232.4/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08
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

- Stars: **14,890** (+319.8/day over 5d)
- Health score: **88/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-08
- Works with: Claude Code

#### [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

> Develop ideas with context and review documents with fresh eyes.

**Core problems it solves**

- **Multi-agent orchestration** — *xed command (#220), but 1.4.8 does not (#196), so keep the prefix.*
- **Agent runtime** — *orkflow targets software specifications.*
- **GUI / desktop app**
- **Notifications** — *For **Claude Cowork** and **ChatGPT Work**, see the setup guide.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Easy. GUI application

**Facts**

- Stars: **14,332** (+670.0/day over 5d)
- Health score: **84/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-08
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

- Stars: **5,271** (~150.6/day lifetime average)
- Health score: **80/100**
- Documentation score: **37/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-08
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

- Stars: **15,374** (+11.4/day over 5d)
- Health score: **62/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Codex

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 17.6k 🚀 +1205/d | **88** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 9.5k 🚀 +78/d | **71** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 51.6k 🚀 +56/d | **70** |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.2k 🚀 +37/d | **68** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k 🚀 +4/d | **61** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 523 | **50** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [getpaseo/paseo](https://github.com/getpaseo/paseo), [superdesigndev/treg](https://github.com/superdesigndev/treg), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub), [decolua/9router](https://github.com/decolua/9router), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck) *(+3 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **17,569** (+1205.0/day over 5d)
- Health score: **88/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-08
- Works with: Codex, Cursor, Cline / Roo

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

- Stars: **9,492** (+78.4/day over 5d)
- Health score: **71/100**
- Documentation score: **54/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-08
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

- Stars: **51,559** (+56.4/day over 5d)
- Health score: **70/100**
- Documentation score: **75/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-11-08

#### [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)

> Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost.

**Core problems it solves**

- **Usage analytics** — *your company, so you can change agents, models or vendors at any time without losing it.*
- **Agent runtime** — *logs and versions, and either files the ticket or tells the reporter what is still missing.*
- **MCP support** — *rough the documentation yourself, connect an agent to it*
- **Self-hostable** — *Open-source AI teammates, working alongside your team in Slack, Teams, Discord, Telegram and Mattermost.*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex, OpenCode*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via native installer / package; GUI application

**Facts**

- Stars: **4,243** (~36.9/day lifetime average)
- Health score: **68/100**
- Documentation score: **54/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-11-08
- Works with: Claude Code, Codex, OpenCode

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

- Stars: **5,053** (+4.4/day over 32d)
- Health score: **61/100**
- Documentation score: **68/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-08
- Works with: Claude Code, Cursor, Cline / Roo

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.3k 🚀 +74/d | **70** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.5k 🚀 +29/d | **69** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Windows core 28/28、packaged-full 44/44，无豁免；真实 Setup 新装、4.3.0/5.0.0/5.0.1 分别升级、同版覆盖、重启、卸载与旧 provider/会话数据保全通过。 DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁… | 🟢 Turnkey · OOTB | ✅ | ✅ | 916 🚀 +5/d | **57** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 980 | **55** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.4k 🚀 +6/d | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 772 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 438 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 510 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 601 | **45** |

**Also does this:** [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [automazeio/ccpm](https://github.com/automazeio/ccpm), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite), [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **4,286** (+73.6/day over 5d)
- Health score: **70/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Aider, Cline / Roo

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

- Stars: **4,499** (+29.2/day over 5d)
- Health score: **69/100**
- Documentation score: **80/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-02
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

- Stars: **916** (+4.8/day over 5d)
- Health score: **57/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-04
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

- Stars: **980** (+0.0/day over 32d)
- Health score: **55/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-11-06
- Works with: Claude Code, OpenCode

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

- Stars: **4,411** (+6.0/day over 5d)
- Health score: **54/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-24
- Works with: Codex

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile | Desktop UI, MCP & Security |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Sharing | Model Routing, Teams |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Sharing | Billing, Billing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Desktop UI, Desktop UI |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | Desktop UI, MCP & Security |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Mobile | Desktop UI, MCP & Security |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI |
| **[openai/codex](https://github.com/openai/codex)** | Billing | Desktop UI |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Teams | Desktop UI, MCP & Security |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile | Analytics, Teams |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Analytics | Desktop UI, MCP & Security |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Analytics, Desktop UI |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Sharing | Desktop UI |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Desktop UI | Desktop UI |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Billing | Analytics, MCP & Security |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Desktop UI | Desktop UI |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Mobile | Billing, Teams |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | Teams | Desktop UI, MCP & Security |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | MCP & Security |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Teams | Analytics, MCP & Security |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | MCP & Security | Desktop UI |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Analytics, Providers |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | MCP & Security | Desktop UI, Sharing |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Desktop UI | Analytics, Desktop UI |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Mobile | Desktop UI, MCP & Security |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Mobile | Desktop UI, Model Routing |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | MCP & Security, Providers |
| **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | Mobile | Desktop UI, Desktop UI |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Desktop UI, Desktop UI |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Mobile | Desktop UI, Desktop UI |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Teams | Analytics, Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Billing, Sharing |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Mobile | Desktop UI, Teams |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Analytics | Desktop UI |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Mobile | Desktop UI, Desktop UI |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Teams |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Analytics | MCP & Security |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Billing, Billing |
| **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | Billing | Analytics, Sharing |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Mobile | Desktop UI, Teams |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | Analytics | Desktop UI |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams | Desktop UI, MCP & Security |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Billing, MCP & Security |
| **[decolua/9router](https://github.com/decolua/9router)** | Billing | Analytics, Billing |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, MCP & Security |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Desktop UI, Model Routing |
| **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Mobile | Model Routing |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Teams | Desktop UI, Model Routing |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Billing | Desktop UI, Sharing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Sharing | Model Routing, Teams |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | MCP & Security |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Analytics, Teams |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Sharing | Desktop UI, MCP & Security |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Desktop UI | Desktop UI |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Sharing | Desktop UI |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Mobile | Desktop UI, MCP & Security |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Billing | MCP & Security, Model Routing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Teams | Billing, Mobile |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Sharing | Desktop UI, Desktop UI |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Sharing | Analytics, MCP & Security |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile | Analytics, Desktop UI |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Desktop UI |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams | Desktop UI |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Desktop UI | Desktop UI |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Desktop UI, Model Routing |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Mobile | Desktop UI, Teams |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Mobile | Desktop UI, Desktop UI |
| **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | MCP & Security | Desktop UI, Desktop UI |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Desktop UI | Desktop UI |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | Desktop UI | Desktop UI |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Mobile | Desktop UI, Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Sharing | Billing, Billing |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Desktop UI |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Sharing | Desktop UI, Model Routing |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Desktop UI | Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Teams | Desktop UI, Mobile |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Mobile | Desktop UI, Desktop UI |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Desktop UI |
| **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | Mobile | Providers |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Teams | Mobile |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | MCP & Security |
| **[0sec-labs/0](https://github.com/0sec-labs/0)** | MCP & Security | Desktop UI |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Mobile | MCP & Security, Providers |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | MCP & Security | Desktop UI, Desktop UI |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Desktop UI, Teams |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Model Routing | Desktop UI |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Billing | Model Routing |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Mobile | Analytics, Teams |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | Billing | Teams |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Mobile | Desktop UI, Model Routing |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP & Security | Desktop UI, Model Routing |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Billing, Providers |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | MCP & Security, Sharing |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Sharing | Teams |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams | Desktop UI, Desktop UI |
| **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | Billing | Billing |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Desktop UI, MCP & Security |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Desktop UI, Model Routing |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Desktop UI |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Desktop UI, Model Routing |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Desktop UI |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | MCP & Security | Model Routing |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Sharing | Analytics, Billing |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Billing | Desktop UI |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Sharing | Desktop UI |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Mobile | Desktop UI, Desktop UI |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Model Routing, Teams |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Sharing | Desktop UI |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Analytics | MCP & Security, Providers |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Mobile | Desktop UI, Model Routing |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Analytics, Billing |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Model Routing, Teams |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Billing | Desktop UI, Model Routing |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Mobile | Model Routing |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | MCP & Security | Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | MCP & Security | Desktop UI |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | MCP & Security | Desktop UI |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI, Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Sharing | MCP & Security, Teams |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Sharing | Teams |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | Mobile | Desktop UI |
| **[IBM/mcp](https://github.com/IBM/mcp)** | MCP & Security | Desktop UI, Desktop UI |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.21x the stars (32,056 vs 152,681) |

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
| **[AVIDS2/memorix](https://github.com/avids2/memorix)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 325.79x the stars (299,397 vs 919) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 60.78x the stars (19,814 vs 326) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 26.70x the stars (11,775 vs 441) | 🤖 auto (high) |
| **[Derpyu520/qq-bridge](https://github.com/derpyu520/qq-bridge)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 4.89x the stars (17,569 vs 3,594) | 🤖 auto (high) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 97.14x the stars (49,346 vs 508) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 223.43x the stars (85,125 vs 381) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 21.74x the stars (11,934 vs 549) | 🤖 auto (high) |
| **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 69.58x the stars (30,197 vs 434) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 577.99x the stars (299,397 vs 518) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.34x the stars (11,775 vs 2,204) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.79x the stars (34,107 vs 927) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.19x the stars (49,346 vs 365) | 🤖 auto (high) |
| **[Tencent/BrowserSkill](https://github.com/tencent/browserskill)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 15.01x the stars (152,681 vs 10,173) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.32x the stars (23,454 vs 5,426) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 173.14x the stars (49,346 vs 285) | 🤖 auto (high) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 159.68x the stars (299,397 vs 1,875) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 319.54x the stars (112,157 vs 351) | 🤖 auto (high) |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 576.87x the stars (299,397 vs 519) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 99.66x the stars (30,197 vs 303) | 🤖 auto (high) |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 41.46x the stars (11,775 vs 284) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.33x the stars (140,715 vs 4,967) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.22x the stars (49,346 vs 3,732) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.22x the stars (11,775 vs 2,255) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.46x the stars (49,346 vs 367) | 🤖 auto (high) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 32.72x the stars (30,197 vs 923) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 6.98x the stars (49,346 vs 7,074) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.46x the stars (23,454 vs 484) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.67x the stars (49,346 vs 317) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 123.13x the stars (34,107 vs 277) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 479.80x the stars (299,397 vs 624) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.19x the stars (152,681 vs 9,432) | 🤖 auto (high) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 16.82x the stars (11,775 vs 700) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 35.01x the stars (19,814 vs 566) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 7.20x the stars (2,031 vs 282) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 7.73x the stars (11,775 vs 1,524) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 13.71x the stars (11,775 vs 859) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.30x the stars (299,397 vs 6,199) | 🤖 auto (high) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 106.70x the stars (30,197 vs 283) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 62.38x the stars (23,454 vs 376) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 617.31x the stars (299,397 vs 485) | 🤖 auto (high) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 91.89x the stars (49,346 vs 537) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 35.17x the stars (49,346 vs 1,403) | 🤖 auto (high) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 7.16x the stars (112,157 vs 15,654) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.15x the stars (11,775 vs 2,834) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.77x the stars (11,775 vs 1,343) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 2.92x the stars (1,685 vs 577) | 🤖 auto (high) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.13x the stars (49,346 vs 3,758) | 🤖 auto (medium) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 9.58x the stars (4,780 vs 499) | 🤖 auto (medium) |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | 18.21x the stars (14,332 vs 787) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.43x the stars (23,454 vs 5,297) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.16x the stars (1,343 vs 425) | 🤖 auto (medium) |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 3.88x the stars (3,698 vs 954) | 🤖 auto (high) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 23.38x the stars (34,107 vs 1,459) | 🤖 auto (high) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 81.03x the stars (49,346 vs 609) | 🤖 auto (medium) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 65.19x the stars (49,346 vs 757) | 🤖 auto (medium) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.99x the stars (19,814 vs 2,479) | 🤖 auto (high) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,346 vs 27,768) | 🤖 auto (medium) |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 1.62x the stars (30,197 vs 18,600) | 🤖 auto (high) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui | 27.8k | 🔻 Superseded | 1.78x the stars (49,346 vs 27,768) |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | teams | 18.6k | 🔻 Superseded | 1.62x the stars (30,197 vs 18,600) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | mobile | 15.7k | 🔻 Superseded | 7.16x the stars (112,157 vs 15,654) |
| **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | sharing | 10.2k | 🔻 Superseded | 15.01x the stars (152,681 vs 10,173) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | sharing | 9.4k | 🔻 Superseded | 16.19x the stars (152,681 vs 9,432) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | desktop-ui | 7.1k | 🔻 Superseded | 6.98x the stars (49,346 vs 7,074) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | teams | 6.2k | 🔻 Superseded | 48.30x the stars (299,397 vs 6,199) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | mobile | 5.4k | 🔻 Superseded | 4.32x the stars (23,454 vs 5,426) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.3k | 🔻 Superseded | 4.43x the stars (23,454 vs 5,297) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | mobile | 5k | 🔻 Superseded | 28.33x the stars (140,715 vs 4,967) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | desktop-ui | 3.8k | 🔻 Superseded | 13.13x the stars (49,346 vs 3,758) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui | 3.7k | 🔻 Superseded | 13.22x the stars (49,346 vs 3,732) |
| **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | analytics-3 | 3.6k | 🔻 Superseded | 4.89x the stars (17,569 vs 3,594) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.8k | 🔻 Superseded | 4.15x the stars (11,775 vs 2,834) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 Superseded | 7.99x the stars (19,814 vs 2,479) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams | 2.3k | 🔻 Superseded | 5.22x the stars (11,775 vs 2,255) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.2k | 🔻 Superseded | 5.34x the stars (11,775 vs 2,204) |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | teams | 1.9k | 🔻 Superseded | 159.68x the stars (299,397 vs 1,875) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | teams | 1.5k | 🔻 Superseded | 7.73x the stars (11,775 vs 1,524) |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | mobile | 1.5k | 🔻 Superseded | 23.38x the stars (34,107 vs 1,459) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | desktop-ui | 1.4k | 🔻 Superseded | 35.17x the stars (49,346 vs 1,403) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 8.77x the stars (11,775 vs 1,343) |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | billing | 954 | 🔻 Superseded | 3.88x the stars (3,698 vs 954) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | mobile | 927 | 🔻 Superseded | 36.79x the stars (34,107 vs 927) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | teams | 923 | 🔻 Superseded | 32.72x the stars (30,197 vs 923) |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | teams | 919 | 🔻 Superseded | 325.79x the stars (299,397 vs 919) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | teams | 859 | 🔻 Superseded | 13.71x the stars (11,775 vs 859) |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | desktop-ui-2 | 787 | 🔻 Superseded | 18.21x the stars (14,332 vs 787) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 757 | 🔻 Superseded | 65.19x the stars (49,346 vs 757) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | teams | 700 | 🔻 Superseded | 16.82x the stars (11,775 vs 700) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | teams | 624 | 🔻 Superseded | 479.80x the stars (299,397 vs 624) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 609 | 🔻 Superseded | 81.03x the stars (49,346 vs 609) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | mobile | 577 | 🔻 Superseded | 2.92x the stars (1,685 vs 577) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | billing | 566 | 🔻 Superseded | 35.01x the stars (19,814 vs 566) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | teams | 549 | 🔻 Superseded | 21.74x the stars (11,934 vs 549) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | desktop-ui | 537 | 🔻 Superseded | 91.89x the stars (49,346 vs 537) |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | teams | 519 | 🔻 Superseded | 576.87x the stars (299,397 vs 519) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | teams | 518 | 🔻 Superseded | 577.99x the stars (299,397 vs 518) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | desktop-ui | 508 | 🔻 Superseded | 97.14x the stars (49,346 vs 508) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-security | 499 | 🔻 Superseded | 9.58x the stars (4,780 vs 499) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | teams | 485 | 🔻 Superseded | 617.31x the stars (299,397 vs 485) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 484 | 🔻 Superseded | 48.46x the stars (23,454 vs 484) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | teams | 441 | 🔻 Superseded | 26.70x the stars (11,775 vs 441) |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | teams | 434 | 🔻 Superseded | 69.58x the stars (30,197 vs 434) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | teams | 425 | 🔻 Superseded | 3.16x the stars (1,343 vs 425) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | mobile | 381 | 🔻 Superseded | 223.43x the stars (85,125 vs 381) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 376 | 🔻 Superseded | 62.38x the stars (23,454 vs 376) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 367 | 🔻 Superseded | 134.46x the stars (49,346 vs 367) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui | 365 | 🔻 Superseded | 135.19x the stars (49,346 vs 365) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | mobile | 351 | 🔻 Superseded | 319.54x the stars (112,157 vs 351) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 326 | 🔻 Superseded | 60.78x the stars (19,814 vs 326) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 317 | 🔻 Superseded | 155.67x the stars (49,346 vs 317) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams | 303 | 🔻 Superseded | 99.66x the stars (30,197 vs 303) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 285 | 🔻 Superseded | 173.14x the stars (49,346 vs 285) |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | teams | 284 | 🔻 Superseded | 41.46x the stars (11,775 vs 284) |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | teams | 283 | 🔻 Superseded | 106.70x the stars (30,197 vs 283) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | mobile | 282 | 🔻 Superseded | 7.20x the stars (2,031 vs 282) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | mobile | 277 | 🔻 Superseded | 123.13x the stars (34,107 vs 277) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-08 11:20 UTC. 219 live tools · 123 candidates rejected by the quality gates.</sub>
