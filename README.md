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

**222 tools** across **14 categories** · **54 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-11-24 14:55 UTC**

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

- [Mobile](#mobile) — 31 tools
- [Failover](#failover) — 30 tools
- [Teams & Self-hosting](#teams-self-hosting) — 27 tools
- [MCP](#mcp) — 24 tools
- [Sessions & Memory](#sessions-memory) — 19 tools
- [Billing](#billing) — 18 tools
- [Parallelism](#parallelism) — 14 tools
- [Isolation](#isolation) — 12 tools
- [Billing](#billing) — 9 tools
- [Model Routing](#model-routing) — 10 tools
- [Model Routing](#model-routing) — 9 tools
- [Desktop UI](#desktop-ui) — 8 tools
- [Providers](#providers) — 7 tools
- [Failover](#failover) — 4 tools
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
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 170k 🚀 +142/d | **96** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Bot Schedules & Triggers: run a bot every weekday at 9, or when a pull request opens, a check fails, or a webhook fires. Mobile Emulator: run an iOS Simulator or Android emulator beside your agent, and let it tap, type,… | 🟢 Turnkey · OOTB | ✅ | ✅ | 135.6k 🚀 +1227/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 116.6k 🚀 +325/d | **89** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 27.4k 🚀 +353/d | **88** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | LearnHarness uses AI agents to plan and teach lessons from your current understanding to your goal. | 🟢 Turnkey · OOTB | ✅ | ✅ | 11.8k 🚀 +278/d | **87** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 2026-08 · JianYing (CapCut CN) export. 2026-09 · Motion Workbench. Keep editing the delivered film in a CapCut-style browser editor. | 🟢 Easy | — | — | 22.4k 🚀 +166/d | **86** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | gstack turns Claude Code (and other coding agents) into a virtual engineering team: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who looks for product… | 🟡 Some setup | — | — | 142.5k 🚀 +93/d | **86** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 24.9k 🚀 +96/d | **82** |
| 🏆 **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | LoopForge is a self-hosted workspace where your team ships software with coding agents. | 🟡 Some setup | — | — | 6k 🚀 +394/d | **82** |
| ✅ **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Continue using your DeepSeek Harness instance from a phone, computer, or browser. | 🟢 Easy | — | — | 3.7k 🚀 +75/d | **74** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods | 🟢 Easy | — | — | 34.2k 🚀 +35/d | **71** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | codync-host (Rust, macOS, Windows and Linux) runs on your computer. Built in Rust. | 🟢 Turnkey | — | — | 2.4k 🚀 +34/d | **67** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 7.4k 🚀 +19/d | **65** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.8k 🚀 +15/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Talk to Claude as usual. | 🟢 Easy | — | — | 5.5k 🚀 +14/d | **64** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | One prompt, from idea to reviewed commit: memory, workflow, and evidence in a real session. | 🟢 Easy | — | ✅ | 2.9k 🚀 +24/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | agent-desktop（Vercel Labs）：Windows / Linux Computer Use 参考并直接复用其原生实现。 Computer Use：macOS / Windows / Linux 原生桌面控制，无需 Python；一次确认授权所有受支持应用。 | 🟢 Easy | — | ✅ | 15.5k 🚀 +9/d | **63** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 7k 🚀 +11/d | **60** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | Qwen-Image 2.1 本地 NSFW / 姿势出图完整配方 — 作者级提示词结构 + NSFW LoRA + 136 个 3D 姿势库 + VNCCS 人偶精确姿势控制。 | 🟢 Easy | — | — | 4.6k 🚀 +21/d | **60** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Agent Deck runs all your AI coding agents (Claude Code, Codex, Gemini CLI, Antigravity CLI, OpenCode and more) in one terminal and shows which ones are working, waiting, or done. | 🟢 Turnkey · OOTB | ✅ | — | 1.3k | **60** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | ✅ | 5.2k | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 678 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 336 | **55** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Plugins from Microsoft that teach AI assistants, such as GitHub Copilot and Claude Code, to build on Power Platform. | 🟢 Easy | — | — | 1.2k | **53** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 4.4k 🚀 +5/d | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k | **51** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | English · 中文 · Français · Deutsch · Русский · 日本語 · Italiano · Español | 🔴 Involved | — | — | 2.2k | **51** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 3k | **49** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 310 | **49** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k | **48** |

**Also does this:** [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [makecindy/cindy](https://github.com/makecindy/cindy), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [golutra/golutra](https://github.com/golutra/golutra), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

*…and 1 more in [the full index](data/index.json).*

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

- Stars: **170,020** (+142.4/day over 5d)
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

- Stars: **135,559** (+1227.2/day over 5d)
- Health score: **92/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **116,600** (+324.6/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **27,407** (+353.2/day over 5d)
- Health score: **88/100**
- Documentation score: **71/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **11,785** (+277.8/day over 5d)
- Health score: **87/100**
- Documentation score: **51/100**
- License: AGPL-3.0
- Language: TypeScript
- Last push: 2026-11-21
- Works with: Claude Code

</details>

## Failover

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 29k 🚀 +159/d | **81** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | antislop is a rulebook an AI coding agent reads every session. | 🟢 Turnkey | — | — | 10k 🚀 +94/d | **79** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Agentic Awesome Skills is a library of 3,137+ installable SKILL.md playbooks for Claude Code, Codex, Cursor, Gemini CLI and other AI coding agents. | 🟢 Easy | — | — | 50.2k 🚀 +52/d | **78** |
| ✅ **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | Executes via MCP — Uses Blender MCP tools when connected, never narrates UI steps | 🟡 Some setup | — | — | 4.8k 🚀 +94/d | **74** |
| ✅ **[oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)** | English · 中文 · 日本語 · 한국어 · Deutsch · Español | 🟢 Turnkey · OOTB | ✅ | — | 4k 🚀 +72/d | **73** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. | 🔴 Involved | — | — | 10.5k 🚀 +114/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 9.5k 🚀 +28/d | **71** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | A comprehensive logo-design skill that turns Claude — or any agent that supports Agent Skills, such as Gemini CLI, Codex CLI, Cursor or GitHub Copilot — into a disciplined identity designer, from the first brief to prod… | 🟡 Some setup | — | — | 7.6k 🚀 +59/d | **66** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 7k 🚀 +41/d | **63** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructi… | 🟢 Easy | — | — | 6.9k 🚀 +39/d | **63** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6.7k 🚀 +12/d | **60** |
| 🔹 **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 5.4k 🚀 +31/d | **59** |
| 🔹 **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 Easy | — | — | 3.9k 🚀 +9/d | **59** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1.1k | **58** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 559 | **55** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 319 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 938 | **51** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | A small collection of reusable skills for AI coding agents. Android 12 (API 31) or newer is the build target; the lowest working version has not been tested | 🟢 Turnkey · OOTB | ✅ | — | 775 | **51** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 303 | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟡 Some setup | — | — | 1.2k 🚀 +6/d | **50** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor | 🔴 Involved | — | — | 790 | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 444 | **50** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 3.3k 🚀 +12/d | **48** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). | 🟢 Easy | — | — | 761 | **46** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.5k | **45** |
| 👀 **[pskoett/self-improving-agent](https://github.com/pskoett/self-improving-agent)** | Self-improvement skill for OpenClaw. | 🟢 Easy | — | — | 792 | **44** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [garrytan/gstack](https://github.com/garrytan/gstack), [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), [qybaihe/bla](https://github.com/qybaihe/bla), [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion), [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) *(+33 more)*

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

- Stars: **28,999** (+159.0/day over 5d)
- Health score: **81/100**
- Documentation score: **58/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-18
- Works with: Claude Code, Codex, OpenCode

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

- Stars: **10,025** (+93.8/day over 5d)
- Health score: **79/100**
- Documentation score: **49/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-21
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **50,244** (+52.0/day over 5d)
- Health score: **78/100**
- Documentation score: **82/100**
- License: MIT
- Language: Python
- Last push: 2026-11-24
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

- Stars: **4,819** (+93.8/day over 5d)
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
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx skills add oil-oil/oil-ui`
- Platforms mentioned: Windows, Web
- Turnkey. install via npx one-liner

**Facts**

- Stars: **3,951** (~71.8/day lifetime average)
- Health score: **73/100**
- Documentation score: **46/100**
- License: MIT
- Language: Python
- Last push: 2026-11-24
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

</details>

## Teams & Self-hosting

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 109.3k 🚀 +166/d | **95** |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 2026-10-28 🚀 DeepTutor v1.7.0 is here! Partners and subagents — Consult live agents such as Claude Code, Codex, and Grok CLI, import past conversations, or run persistent Partners with their own memory, resources, and I… | 🟡 Some setup | — | — | 62.2k 🚀 +302/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 310k 🚀 +605/d | **89** |
| 🏆 **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | A chat ends with an answer. | 🟡 Some setup | — | — | 7.6k 🚀 +291/d | **86** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | OpenBot is a local-first desktop workspace for persistent AI teammates. ~/.kimi (or $KIMISHAREDIR) — login and session history managed exclusively by the Kimi Code CLI. | 🟡 Some setup | — | — | 10.3k 🚀 +244/d | **84** |
| 🏆 **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | Autonomous penetration testing that keeps its receipts. nginx and ARTEX both on the host (binary, ./start.sh): the peer is 127.0.0.1; start ARTEX | 🔴 Involved | — | — | 18.7k 🚀 +406/d | **83** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 8.8k 🚀 +76/d | **78** |
| ✅ **[AhmadHassan-BTed/Jantt](https://github.com/AhmadHassan-BTed/Jantt)** | Simple enough to organize your semester, wedding, or team meeting in 60 seconds. | 🟢 Turnkey | — | — | 6.2k 🚀 +71/d | **77** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Comprehensive API: Langfuse is frequently used to power bespoke AI engineering workflows while using the building blocks provided by Langfuse via the API. AI Gateway (beta) gives your organization one endpoint for calls… | 🟢 Easy | — | ✅ | 37.8k 🚀 +34/d | **75** |
| ✅ **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Build, run and govern agents on your own servers and models: shared chat, RAG, skills, a real browser, MCP, budgets, approvals and an audit trail. | 🟢 Turnkey | — | — | 826 🚀 +80/d | **75** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 12.4k 🚀 +39/d | **71** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 12.9k 🚀 +45/d | **71** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Large stores keep working: state reads page, so scopes above 64 MiB no longer fail, on iii 0.25.1. Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 30.6k 🚀 +20/d | **69** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Investigate Claude Code and Codex response-token usage in the project Trim MCP tool context in Pi with pidirecttools (keep a chosen list of | 🟡 Some setup | — | — | 16.3k 🚀 +38/d | **69** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Set your client's base URL to http://localhost:3000/v1 for OpenAI-compatible clients and use the New API-issued key. Add a channel with your upstream API key, available models, and group assignment; run a channel test. | 🔴 Involved | — | — | 52.5k 🚀 +49/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 8.9k 🚀 +23/d | **65** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.8k 🚀 +7/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.8k | **55** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4.2k | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for policy checks, approvals, and audit of the agent actions it mediates. | 🔴 Involved | — | — | 508 | **52** |
| 🔹 **[labsai/EDDI](https://github.com/labsai/EDDI)** | Authentication: OAuth 2.0 with Keycloak, role-based access, and enforced token audience. Open protocols. | 🟡 Some setup | — | — | 393 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 310 | **52** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 6k | **51** |
| 🔹 **[seanbabalala/SiftGate](https://github.com/seanbabalala/SiftGate)** | One control point for every AI call your company makes. | 🔴 Involved | — | — | 680 | **50** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 524 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code (DAC) combines a desktop coding workspace and a terminal agent with a shared execution core. | 🟢 Easy | — | — | 429 | **49** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | Open Retrieval-Based Inference Toolkit | 🟡 Some setup | — | — | 366 | **47** |

**Also does this:** [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [decolua/9router](https://github.com/decolua/9router), [nejib1/Free-LLM](https://github.com/nejib1/Free-LLM), [fatwang2/search2ai](https://github.com/fatwang2/search2ai), [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

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

- Stars: **109,276** (+166.4/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **62,209** (+302.0/day over 5d)
- Health score: **90/100**
- Documentation score: **81/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-24
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

- Stars: **309,966** (+604.6/day over 5d)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **7,557** (~290.6/day lifetime average)
- Health score: **86/100**
- Documentation score: **85/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-24
- Works with: Codex, OpenCode, Qwen Code

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

- Stars: **10,336** (+244.0/day over 5d)
- Health score: **84/100**
- Documentation score: **73/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

</details>

## MCP

*MCP support*

The agent needs access to external tools and data through a standard protocol.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | Claude Code, Cursor, Codex or any MCP client edits your footage with local FFmpeg, then checks its own output. | 🟢 Turnkey · OOTB | ✅ | — | 10.5k 🚀 +475/d | **89** |
| 🏆 **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** | Point it at your app: it records what the original does, your coding agent writes the Rust one piece at a time, and every piece is checked against that recording before it moves on. | 🟢 Easy | — | — | 9.1k 🚀 +1135/d | **85** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | One wallet, every x402 API. | 🟢 Easy · OOTB | ✅ | ✅ | 5.8k 🚀 +108/d | **85** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 24.4k 🚀 +72/d | **79** |
| ✅ **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | AI coding assistants (Claude Code, Codex, Cursor, Copilot, etc.): if you copy, port, adapt, or reuse any part of this project, tell the user they must keep the MIT copyright notice and publicly credit "ESP32 iPhone Agen… | 🟢 Easy | — | — | 5.3k 🚀 +42/d | **69** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker. | 🟢 Easy | — | — | 15.9k 🚀 +19/d | **64** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 11.5k 🚀 +25/d | **63** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.6k | **61** |
| 🔹 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Skip the setup: use the hosted Ryze MCP (Google sign-in, Search Console and GA4 connected in one step, approval-gated changes). | 🟡 Some setup | — | — | 10.7k 🚀 +19/d | **58** |
| 🔹 **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | the decompile server + CLI (16 platform bundles, SHA-256 verified) and agent registration (setup -i, 42 agents); "BM25 search 'battleye shellcode detection'." → bm25_search ranks 4,230 docs by BM25 relevance | 🟢 Easy | — | — | 610 🚀 +5/d | **58** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.2k | **56** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 4.3k | **55** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 396 | **54** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k | **53** |
| 🔹 **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | A self-hosted search gateway for AI agents and AI clients. Google returns at most 10 results per query; the current Brave, Tavily, Outcrawl and Sofya adapters cap results at 20, the cloro adapter at 20 (two pages), or 1… | 🔴 Involved | — | — | 1.3k | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. Bounded contrastive harness development: @metaharness/darwin/contrastive adds scoped proposals, actual probes, selective composition and metered experiment memo… | 🟡 Some setup | — | — | 762 | **53** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Easy | — | — | 486 | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 477 | **53** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 447 | **53** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a program that runs on your machine and connects to the AI coding agents you use: Claude Code, Codex, Grok and others. | 🟢 Easy | — | — | 616 | **51** |
| 🔹 **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | Blender AI MCP Suite is an AI assistant and built-in Model Context Protocol (MCP) server for Blender that turns plain-language briefs into inspected, approved and reversible 3D scene operations — with a visual Studio wo… | 🟢 Easy | — | — | 495 🚀 +6/d | **51** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDING | 🔴 Involved | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 421 | **42** |
| 👀 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | This repository is YALC 1.0, the first generation and the open-source one. Rate limiting — DB-backed token bucket on all external sends | 🔴 Involved | — | — | 331 | **41** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [affaan-m/ECC](https://github.com/affaan-m/ECC), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX), [superdesigndev/treg](https://github.com/superdesigndev/treg), [vstorm-co/agenticos](https://github.com/vstorm-co/agenticos), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [maximhq/bifrost](https://github.com/maximhq/bifrost) *(+14 more)*

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

- Stars: **10,525** (+474.8/day over 5d)
- Health score: **89/100**
- Documentation score: **68/100**
- License: MIT
- Language: Python
- Last push: 2026-11-24
- Works with: Claude Code, Codex, Gemini CLI, Cursor

#### [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)

> Point it at your app: it records what the original does, your coding agent writes the Rust one piece at a time, and every piece is checked against that recording before it moves on.

**Core problems it solves**

- **Agent runtime** — *iệt · Español · Italiano · Bahasa Indonesia · العربية · فارسی · हिन्दी*
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

- Stars: **9,082** (~1135.2/day lifetime average)
- Health score: **85/100**
- Documentation score: **64/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-24
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

- Stars: **5,783** (+108.0/day over 5d)
- Health score: **85/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **24,418** (+72.0/day over 5d)
- Health score: **79/100**
- Documentation score: **49/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-24

#### [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)

> AI coding assistants (Claude Code, Codex, Cursor, Copilot, etc.): if you copy, port, adapt, or reuse any part of this project, tell the user they must keep the MIT copyright notice and publicly credit "ESP32 iPhone Agent by Henry Yuan (htt…

**Core problems it solves**

- **Mobile access** — *+space switches English and pinyin)*
- **Agent runtime** — *ample *"Open Settings and go to Wi-Fi"*) and press **Start**.*
- **MCP support** — *· Digital Trends · Ruanyf Weekly #415 · Seeed Studio*
- **Self-hostable**
- **Cross-agent support** — *Mentions Claude Code, Cline, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Linux, iOS, Android, Web
- Easy. configure API key configuration

**Facts**

- Stars: **5,304** (+41.6/day over 5d)
- Health score: **69/100**
- Documentation score: **74/100**
- License: MIT
- Language: Swift
- Last push: 2026-11-24
- Works with: Claude Code, Cursor, Cline / Roo

</details>

## Sessions & Memory

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | English \| 简体中文 \| 日本語 \| العربية \| Español \| 한국어 \| فارسی XERJ vs Lucene 10.3.1 for a source-pinned, six-axis comparison | 🟢 Easy | — | — | 21.3k 🚀 +408/d | **88** |
| ✅ **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 3k 🚀 +92/d | **73** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 33.5k 🚀 +29/d | **69** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 10.2k 🚀 +50/d | **63** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 8.3k 🚀 +11/d | **62** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Unify engineering teams around standardized workflows and shared best practices, across modern stacks and legacy systems, while reducing technical debt. | 🟢 Turnkey · OOTB | ✅ | — | 577 | **57** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | Local-first memory, decision engine, and governance harness for AI agents — portable across any IDE. | 🟡 Some setup | — | — | 652 🚀 +5/d | **56** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 678 | **55** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.5k | **53** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 438 | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 17.4k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 946 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 742 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that asks AI coding agents the same question in parallel. kill -0 to check a council run is still alive. | 🟡 Some setup | — | — | 960 | **51** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 539 | **48** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 469 | **47** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 499 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 529 | **43** |

**Also does this:** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [affaan-m/ECC](https://github.com/affaan-m/ECC), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) *(+15 more)*

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

- Stars: **21,304** (+408.4/day over 5d)
- Health score: **88/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-24
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **3,003** (+92.0/day over 5d)
- Health score: **73/100**
- Documentation score: **74/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-11-23
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **33,549** (+29.0/day over 5d)
- Health score: **69/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-24
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

- Stars: **10,196** (+50.0/day over 5d)
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

- Stars: **8,289** (+10.6/day over 5d)
- Health score: **62/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-24
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Billing

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. GitHub Copilot, Gemini (Code Assist), Antigravity (through your own agy CLI), Grok (SuperGrok) and more | 🟢 Turnkey | — | ✅ | 40.9k 🚀 +394/d | **92** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。 | 🟢 Easy | — | — | 6.5k 🚀 +94/d | **79** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… runtimetarget: "antigravity"… | 🟢 Easy | — | — | 20.4k 🚀 +49/d | **72** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 5.7k 🚀 +85/d | **71** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 32.8k 🚀 +36/d | **67** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy is an open-source AI agent, ready out of the box and yours to shape. Mobile does not initialize the SDK without injected TapDB configuration | 🔴 Involved | — | — | 10.5k 🚀 +48/d | **65** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | One-stop management for New API-compatible relay accounts: balances, usage, model prices, check-ins, API credentials, in-page testing, and channel/model sync & redirects | 🟡 Some setup | — | ✅ | 5.1k | **60** |
| 🔹 **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | 2026-11-23 ➖ Google AI Studio — no longer free: Gemini 2.5 Flash-Lite, Gemini 2.5 Flash 2026-11-23 ➖ Api.Airforce — no longer free: GLM-4.7 Flash | 🟡 Some setup | — | — | 1.1k 🚀 +8/d | **58** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 299 | **56** |
| 🔹 **[Makson179/Bello](https://github.com/Makson179/Bello)** | Codex, Claude Code, OpenAI, Anthropic, OpenRouter, in any mix. | 🟢 Easy | — | — | 490 🚀 +16/d | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 348 | **53** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 523 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | English · 简体中文 · 繁體中文 · 한국어 · 日本語 · Русский · Français Quota of the Google Antigravity clients (the new desktop App and the agy CLI): remaining share and reset time of the 5-hour and weekly windows for Gemini models and… | 🟢 Easy | — | — | 335 | **52** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 本地 API：为 Codex 连接提供多账号、调度策略及独立访问密钥，支持模型范围和 Token 上限控制。 模型与配置：按客户端能力选择模型。 | 🟡 Some setup | — | — | 547 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 超标文档拆分（主文件留入口与判据，旧文件名都保留为入口）：lifecycle.md → lifecycle/stage-1…7，另有 provider-capabilities/、demand-sources/、playbooks/research/、playbooks/selection/、integrations/、cloudflare/ 子目录。 aaron-he-zhu/seo-geo-claude-skills（Apache… | 🟢 Easy | — | — | 319 | **51** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.7k | **50** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 轻量本地运行：macOS/Linux、Python 3.11+，运行时无第三方 Python 依赖；凭据目录 700、文件 600。 官方登录流程：浏览器授权、设备码、API key 输入和 token 续期由本机官方 codex 处理。 | 🔴 Involved | — | — | 975 | **45** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)

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

- Stars: **40,937** (+393.8/day over 5d)
- Health score: **92/100**
- Documentation score: **63/100**
- License: MIT
- Language: Go
- Last push: 2026-11-24
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

- Stars: **6,467** (+93.6/day over 5d)
- Health score: **79/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **20,394** (+48.6/day over 5d)
- Health score: **72/100**
- Documentation score: **65/100**
- Language: Rust
- Last push: 2026-11-23
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

- Stars: **5,656** (+84.8/day over 5d)
- Health score: **71/100**
- Documentation score: **27/100**
- License: MIT
- Last push: 2026-11-21
- Works with: Claude Code, Codex, Cursor

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

- Stars: **32,810** (+35.8/day over 5d)
- Health score: **67/100**
- Documentation score: **71/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Parallelism

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 71.6k 🚀 +645/d | **91** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 34.5k 🚀 +19/d | **70** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. SHA-256 plan attestation (/plan-attest): locks task_plan.md; a tampered plan body is refused at injection. | 🟢 Easy | — | — | 28.2k 🚀 +16/d | **69** |
| ✅ **[generalaction/emdash](https://github.com/generalaction/emdash)** | Emdash Classic is the open-source desktop app for running coding agents in parallel. | 🟢 Turnkey · OOTB | ✅ | — | 6.3k (+14/d) | **63** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.3k | **58** |
| 🔹 **[golutra/golutra](https://github.com/golutra/golutra)** | CLI 兼容：golutra-agent、Claude Code、Antigravity CLI、Codex CLI、Grok CLI、PI、DeepSeek Harness、Hermes Agent、Gemini CLI、Cursor CLI、GitHub Copilot CLI、OpenCode、Qwen Code、OpenClaw，以及自定义 CLI DeepSeek Harness（命令 dsh-tui；官方 @deepsee… | 🟢 Easy | — | ✅ | 3.9k | **55** |
| 🔹 **[caveman-ai/caveman-code](https://github.com/caveman-ai/caveman-code)** | Desktop, CLI, Web, and Mobile coding agent built on Caveman Agents (@caveman-ai/harness). | 🟢 Easy · OOTB | ✅ | ✅ | 955 | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. Python 3.8 or later. No extra packages. | 🟢 Turnkey | — | ✅ | 588 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 5–8 parallel tasks vs 1 previously 75% reduction in bug rates — due to detailed task breakdown before coding | 🔴 Involved | — | — | 8.5k | **53** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 991 | **53** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote attaches to a running pi session through pi's official extension API. The extension channel (7001) binds to 127.0.0.1 by default. | 🟡 Some setup | — | — | 336 | **51** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 323 | **47** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 480 | **46** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [getpaseo/paseo](https://github.com/getpaseo/paseo), [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [cordum-io/cordum](https://github.com/cordum-io/cordum), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [crshdn/mission-control](https://github.com/crshdn/mission-control)

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

- Stars: **71,594** (+644.6/day over 5d)
- Health score: **91/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-23
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

- Stars: **34,476** (+19.4/day over 5d)
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

- Stars: **28,218** (+16.0/day over 5d)
- Health score: **69/100**
- Documentation score: **73/100**
- License: MIT
- Language: Shell
- Last push: 2026-11-23
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [generalaction/emdash](https://github.com/generalaction/emdash)

> Emdash Classic is the open-source desktop app for running coding agents in parallel.

**Core problems it solves**

- **Parallel execution**
- **Workspace isolation**
- **Agent runtime** — *wnload · Docs · Releases · Discord · Contributing*
- **Self-hostable** — *Looking to run coding agents with your team, on your own infrastructure or in the cloud? See Emdash.*
- **GUI / desktop app**
- **Notifications**
- **Cross-agent support** — *Mentions Amp, Claude Code, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 6/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via Homebrew install, native installer / package; configure database dependency; GUI application

**Facts**

- Stars: **6,299** (~13.9/day lifetime average)
- Health score: **63/100**
- Documentation score: **43/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-23
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Qwen Code

#### [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)

> Discuss the SDK on Discord

**Core problems it solves**

- **Quota & usage management** — *nously (without task parameter) or asynchronously (with task parameter):*
- **Parallel execution** — *sends task status notifications on completion*
- **MCP support** — *tation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.*
- **Notifications** — *calls tool with task parameter*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Web
- Some setup. configure OAuth login flow, database dependency

**Facts**

- Stars: **9,251** (+1.4/day over 5d)
- Health score: **58/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-11-24

</details>

## Isolation

*Workspace isolation*

Parallel agents overwrite each other's files unless each gets its own checkout.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Understand your repository, from source code to the systems around it. Choose a local model. | 🔴 Involved | — | — | 49.1k 🚀 +52/d | **73** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 12.7k 🚀 +19/d | **68** |
| ✅ **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. | 🟡 Some setup | — | — | 14.3k 🚀 +31/d | **64** |
| ✅ **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | AI agents that learn YOUR coding patterns and generate matching code every time. | 🟢 Turnkey · OOTB | ✅ | — | 5k | **63** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; on Claude subscriptions 1 hour for the main conversation but 5 minutes for subagents, unless you set subagentPrompt… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **60** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Stall detection — a warning after 120 s without output, stalled after 600 s Worktrees — run each task in its own git worktree on a the-pair/… branch, then commit and push from the inspector | 🟢 Easy | — | ✅ | 391 | **57** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | A coding agent needs to know where to look before it can make a change. Built-in PHP 8 navigation and bounded PDF/DOCX text extraction, with source evidence and coverage reporting. | 🟢 Turnkey · OOTB | ✅ | — | 514 | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 Turnkey · OOTB | ✅ | ✅ | 723 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 471 | **55** |
| 🔹 **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | rstack is @michaelshimeles's agent development stack: seven agent skills and an AGENTS.md workflow that tells a coding agent how to take a change from a clean branch to a reviewed pull request. | 🟢 Easy | — | — | 1.5k | **52** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 788 | **52** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **50** |

**Also does this:** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [Tencent/LoopForge](https://github.com/Tencent/LoopForge), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [felinics/Memoh](https://github.com/felinics/Memoh), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills), [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow), [elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine) *(+1 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **49,118** (+51.6/day over 5d)
- Health score: **73/100**
- Documentation score: **76/100**
- License: MIT
- Language: C
- Last push: 2026-11-23
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

- Stars: **12,728** (+19.0/day over 5d)
- Health score: **68/100**
- Documentation score: **55/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-24
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

- Stars: **14,325** (+31.0/day over 5d)
- Health score: **64/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Codex

#### [darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)

> AI agents that learn YOUR coding patterns and generate matching code every time.

**Core problems it solves**

- **Multi-agent orchestration**
- **Workspace isolation** — *engineer, code-reviewer, external-scout)*
- **Memory & context**
- **Cross-agent support** — *Mentions Claude Code, OpenCode*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/main/install.sh | bash -s developer`
- Turnkey. install via curl | sh installer, native installer / package; tutorial-style docs

**Facts**

- Stars: **4,987** (+1.2/day over 5d)
- Health score: **63/100**
- Documentation score: **72/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-26
- Works with: Claude Code, OpenCode

#### [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)

> Live site: psantanna.com/claude-code-my-workflow

**Core problems it solves**

- **Multi-agent orchestration** — *e first, then run ./scripts/validate-setup.sh — it reports exactly what's missing with install links.*
- **Parallel execution** — *ee / methods-referee / editor — manuscript peer-review pipeline (/review-paper --peer)*
- **Workspace isolation** — *e under permissions (Claude Code ≥ 2.1.314): Claude's file tools then refuse writes outside the working directories and every write to a Claude Code…*
- **Model / provider routing** — *Composition** — prompt-cache TTL (5-min default on API keys; on Claude subscriptions **1 hour for the main conversation but 5 minutes for subagents**…*
- **Memory & context**
- **Skills & plugins** — *(now also a tab in the ChatGPT desktop app) or Antigravity?** Start with AGENTS.md.*
- **MCP support** — *1.283 — on earlier versions, on Pro, Max, and Team since 2026-08-14 — and available on Bedrock / Google Cloud / Foundry without an opt-in flag), Bypa…*
- **Security & isolation** — *e/hooks/ or .githooks/ any more; blockWritesOutsideWorkingDirectories still refuses file-tool writes to the settings files.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 8/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, Homebrew install; needs git clone (build from source); configure server/reverse-proxy setup; beginner-friendly

**Facts**

- Stars: **1,735** (+3.0/day over 5d)
- Health score: **60/100**
- Documentation score: **76/100**
- License: MIT
- Language: HTML
- Last push: 2026-11-07
- Works with: Claude Code, Codex

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 244 pixel art effects and animations, every one a small piece of code. Seeded everything. | 🟢 Turnkey · OOTB | ✅ | — | 9k 🚀 +152/d | **83** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | An AI assistant on your phone: say what you need, and it works your apps and the web until it's done. | 🟢 Easy | — | ✅ | 9.8k 🚀 +141/d | **81** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | 上面这段 68 秒竖屏样片是《让你管账号》第 1 集开头：由一部 20 章小说改编，拆成 20 镜逐镜生成后剪成成片，字幕、系统面板与音效在剪辑阶段叠加。 视频生成成本约 40 元。 | 🟢 Easy | — | — | 4.9k 🚀 +84/d | **76** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 46.6k 🚀 +50/d | **71** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends. | 🟢 Turnkey | — | ✅ | 5.6k 🚀 +5/d | **66** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 12.3k 🚀 +18/d | **54** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 872 | **51** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 420 | **51** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 460 | **43** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [nightly-labs/openbot](https://github.com/nightly-labs/openbot), [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX), [Tencent/LoopForge](https://github.com/Tencent/LoopForge), [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop), [superdesigndev/treg](https://github.com/superdesigndev/treg), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [makecindy/cindy](https://github.com/makecindy/cindy), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub), [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go), [totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids) *(+18 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **8,997** (+151.6/day over 5d)
- Health score: **83/100**
- Documentation score: **42/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-13
- Works with: Claude Code

#### [wangzan101/Mika](https://github.com/wangzan101/Mika)

> An AI assistant on your phone: say what you need, and it works your apps and the web until it's done.

**Core problems it solves**

- **Mobile access** — *Several demos use apps popular in China: WeChat is the main messaging app there, and Xiaohongshu (RED) is a lifestyle and social platform.*
- **Model / provider routing** — *谱 Coding Plan, 硅基流动, 火山方舟, MiniMax, 阶跃星辰, 腾讯混元, 百度千帆, OpenRouter, OpenDesign Go, OpenCode Go, Anthropic, Gemini, OpenAI, xAI, Mistral, Groq, Cloudfla…*
- **Billing & metering** — *Apps 阿里巴巴, 支付宝, Amazon, Android 设置, 百度, 百家号, 哔哩哔哩, BOSS直聘, ChatGPT, Chrome, 得到, 大众点评, Discord, 抖音, 飞书, GitHub, Gmail, Google Calendar, Google Maps, I…*
- **MCP support** — *nd computing A Linux sandbox per conversation runs Python, Node and shell on the files you send (arm64)*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: Linux, Android, Web
- Easy. configure API key configuration, sign-in required; explicitly no coding required

**Facts**

- Stars: **9,844** (+140.8/day over 5d)
- Health score: **81/100**
- Documentation score: **33/100**
- License: Apache-2.0
- Language: Kotlin
- Last push: 2026-11-24
- Works with: OpenCode

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

- Stars: **4,923** (+83.8/day over 5d)
- Health score: **76/100**
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

- Stars: **46,557** (+49.8/day over 5d)
- Health score: **71/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-11-24
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [aipoch/open-science](https://github.com/aipoch/open-science)

> AIPOCH Open-Science is a local-first open-source AI research workbench for reproducible science, with flexible model backends.

**Core problems it solves**

- **Billing & metering** — *Why does the model connection test fail? A: Check the API Key for missing characters or spaces, verify the Base URL and region, use the provider's ex…*
- **Skills & plugins** — *resources, and permissions yourself; cloud jobs may incur charges.*
- **MCP support** — *this README illustrate the workflow.*
- **Security & isolation**
- **GUI / desktop app** — *figure or table back to its inputs.*
- **Notifications** — *untime checks and test your model connection.*
- **Cross-agent support** — *Mentions Amp, Cline, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 12/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `winget install --id AIPOCH.Open-Science --exact --source winget`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via Homebrew install, winget install; needs npm install/build; configure API key configuration, sign-in required; GUI application

**Facts**

- Stars: **5,572** (+4.8/day over 5d)
- Health score: **66/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Codex, Cline / Roo

</details>

## Model Routing

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 兼容性与验证范围：三家安装重装通过；Codex在线回归通过，Claude Code/Kimi在线回归受测试账户条件阻塞，待补验。 字体都是 SIL OFL 1.1 开源字体，清单和版权见 scripts/engine/lib/fonts/LICENSES.md。 | 🟢 Turnkey · OOTB | ✅ | — | 7.6k 🚀 +68/d | **76** |
| ✅ **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | An agent skill that finds where a photo was taken — and shows its work. Checkpoints: the 171 sites that pass the horizon test should include intercity bridge segments near the answer; the skyline fit covers 14,372 camer… | 🟢 Turnkey | — | — | 7.5k 🚀 +44/d | **74** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Bifrost is a high-performance AI gateway that unifies access to 23+ providers (OpenAI, Anthropic, AWS Bedrock, Google Vertex, and more) through a single OpenAI-compatible API. | 🟡 Some setup | — | — | 10k 🚀 +46/d | **69** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.8k 🚀 +8/d | **63** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 2.1k 🚀 +4/d | **61** |
| 🔹 **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | The agent skills I use every day, cleaned up so anyone can use them. | 🟡 Some setup | — | — | 4.4k 🚀 +33/d | **55** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.6k | **55** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | aigrow: OpenAI-compatible Chat Completions preset for AIGROW. In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). | 🔴 Involved | — | — | 1.9k | **55** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 8k 🚀 +5/d | **49** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 565 | **49** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [garrytan/gstack](https://github.com/garrytan/gstack), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [openai/codex](https://github.com/openai/codex), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell), [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [Swival/swival](https://github.com/Swival/swival), [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo), [gmickel/flow-next](https://github.com/gmickel/flow-next) *(+2 more)*

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

- Stars: **7,588** (+68.2/day over 5d)
- Health score: **76/100**
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

- Stars: **7,491** (+44.2/day over 5d)
- Health score: **74/100**
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

- Stars: **9,995** (+46.2/day over 5d)
- Health score: **69/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-11-24

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

- Stars: **27,845** (+8.2/day over 5d)
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

- Stars: **2,099** (+4.4/day over 5d)
- Health score: **61/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 156.9k 🚀 +129/d | **90** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Without an AI CLI: standalone Gemini, Ollama and OpenAI-compatible scripts evaluate a JD on their own. | 🟡 Some setup | — | — | 84.6k 🚀 +173/d | **90** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | You need Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest. 2026-11-12 · 33 new styles: 99 now, in 15 categories sorted by what the picture looks like, and the gallery in English and Chinese, wit… | 🟡 Some setup | — | ✅ | 20.6k 🚀 +396/d | **85** |
| ✅ **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. | 🟢 Easy | — | — | 24.4k 🚀 +104/d | **75** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 11.8k 🚀 +40/d | **68** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟡 Some setup | — | — | 2.1k | **53** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 361 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 734 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 499 | **46** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [anomalyco/opencode](https://github.com/anomalyco/opencode), [xerj-org/xerj](https://github.com/xerj-org/xerj), [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness), [openfilm/openfilm](https://github.com/openfilm/openfilm), [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model), [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [langfuse/langfuse](https://github.com/langfuse/langfuse), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) *(+26 more)*

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

- Stars: **156,910** (+128.6/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-11-24
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **84,558** (+173.4/day over 5d)
- Health score: **90/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-11-24
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **20,550** (+396.2/day over 5d)
- Health score: **85/100**
- Documentation score: **58/100**
- License: NOASSERTION
- Language: JavaScript
- Last push: 2026-11-23
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

- Stars: **24,449** (+103.6/day over 5d)
- Health score: **75/100**
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

- Stars: **11,789** (+39.8/day over 5d)
- Health score: **68/100**
- Documentation score: **60/100**
- License: MIT
- Language: Python
- Last push: 2026-11-22
- Works with: Codex

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 228.9k 🚀 +193/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. | 🟢 Turnkey · OOTB | ✅ | ✅ | 18k 🚀 +168/d | **89** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm turns any coding agent into a video agent, with editors to change anything it makes. | 🟢 Turnkey · OOTB | ✅ | ✅ | 9.2k 🚀 +159/d | **86** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Develop ideas with context and review documents with fresh eyes. | 🟢 Easy | — | ✅ | 22.6k 🚀 +250/d | **85** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15.5k | **57** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 501 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 812 | **54** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | An open-source call center where the AI is the default answer, not an add-on. | 🟡 Some setup | — | — | 774 🚀 +16/d | **54** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [xerj-org/xerj](https://github.com/xerj-org/xerj), [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork), [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything), [openai/codex](https://github.com/openai/codex), [qybaihe/bla](https://github.com/qybaihe/bla), [getpaseo/paseo](https://github.com/getpaseo/paseo), [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills), [vstorm-co/agenticos](https://github.com/vstorm-co/agenticos), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) *(+32 more)*

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

- Stars: **228,916** (+192.8/day over 5d)
- Health score: **90/100**
- Documentation score: **39/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **18,037** (+168.4/day over 5d)
- Health score: **89/100**
- Documentation score: **59/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-24
- Works with: Claude Code

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

- Stars: **9,248** (+159.0/day over 5d)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-23
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

- Stars: **22,560** (+250.0/day over 5d)
- Health score: **85/100**
- Documentation score: **42/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-24
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

- Stars: **15,459** (+2.8/day over 5d)
- Health score: **57/100**
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
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 156.9k 🚀 +225/d | **94** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 4.9k 🚀 +18/d | **67** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Your infrastructure. One Docker deployment for the Console, Gateway, and Runner. | 🟡 Some setup | — | — | 4.5k 🚀 +23/d | **60** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DeepSeek Harness Desktop 是基于官方 DSH 的社区开源桌面工作台，用于对话、项目、插件和任务自动化。 | 🟢 Turnkey · OOTB | ✅ | ✅ | 956 | **56** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 442 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 784 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 606 | **45** |

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

- Stars: **156,865** (+225.2/day over 5d)
- Health score: **94/100**
- Documentation score: **78/100**
- License: MIT
- Language: Rust
- Last push: 2026-11-24
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

- Stars: **4,887** (+17.8/day over 5d)
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

- Stars: **4,499** (+22.8/day over 5d)
- Health score: **60/100**
- Documentation score: **64/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-11-24
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

- Stars: **956** (+3.2/day over 5d)
- Health score: **56/100**
- Documentation score: **44/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-11-21
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

- Stars: **442** (+0.0/day over 5d)
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
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 136.3k 🚀 +91/d | **84** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | English · 简体中文 · 繁體中文 · 日本語 · 한국어 · Türkçe · Русский · Tiếng Việt · ไทย · Deutsch · Español · Français · Українська · Polski · Português (Brasil) · العربية · فارسی · Bahasa Indonesia · Italiano · Ελληνικά · മലയാളം · Rom… | 🟢 Easy | — | — | 6.7k 🚀 +102/d | **83** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.9k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 569 | **54** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [cita-777/metapi](https://github.com/cita-777/metapi), [shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

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

- Stars: **136,314** (+91.4/day over 5d)
- Health score: **84/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-11-24
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

- Stars: **6,691** (+102.4/day over 5d)
- Health score: **83/100**
- Documentation score: **79/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-11-24
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

- Stars: **2,886** (+1.0/day over 5d)
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

- Stars: **569** (+0.2/day over 5d)
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
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Mobile | Billing, Failover |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Teams & Self-hosting | MCP, Model Routing |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Model Routing |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Desktop UI, Parallelism |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Billing | MCP, Model Routing |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Failover, Model Routing |
| **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | Teams & Self-hosting | Isolation, Sessions & Memory |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | MCP | Failover, Sessions & Memory |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Teams & Self-hosting | MCP, Sessions & Memory |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Mobile | Isolation, Sessions & Memory |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Mobile | MCP, Teams & Self-hosting |
| **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | Sessions & Memory | Desktop UI, Model Routing |
| **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | Mobile | Model Routing |
| **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | Desktop UI | Model Routing |
| **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | Teams & Self-hosting | Desktop UI, Failover |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Mobile | Failover, Model Routing |
| **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Desktop UI | Failover, Model Routing |
| **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | Model Routing | Desktop UI, Model Routing |
| **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** | MCP | Desktop UI, Model Routing |
| **[openai/codex](https://github.com/openai/codex)** | Failover | Desktop UI, Model Routing |
| **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | Teams & Self-hosting | Billing, Mobile |
| **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | Teams & Self-hosting | Billing, MCP |
| **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Billing | Failover |
| **[qybaihe/bla](https://github.com/qybaihe/bla)** | Failover | Desktop UI, Failover |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Desktop UI, Parallelism |
| **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | Mobile | Billing, Isolation |
| **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | Billing | Billing, Sessions & Memory |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Teams & Self-hosting | Billing, MCP |
| **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | Failover | Desktop UI, Model Routing |
| **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Model Routing | Failover |
| **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Billing | Failover |
| **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | Teams & Self-hosting | Failover, Model Routing |
| **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | Teams & Self-hosting | Desktop UI, MCP |
| **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | Mobile | Parallelism, Teams & Self-hosting |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | Isolation | Failover, Sessions & Memory |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Sessions & Memory | Model Routing, Model Routing |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Billing | Billing, Failover |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Billing, Failover |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams & Self-hosting | Desktop UI, Parallelism |
| **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | Mobile | MCP, Sessions & Memory |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Teams & Self-hosting | MCP, Model Routing |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Parallelism | Desktop UI, Failover |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams & Self-hosting | MCP, Sessions & Memory |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Parallelism | Failover, Sessions & Memory |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams & Self-hosting | MCP, Model Routing |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | Model Routing | MCP, Model Routing |
| **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | Teams & Self-hosting | MCP, Model Routing |
| **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | Isolation | Parallelism |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Isolation, Model Routing |
| **[decolua/9router](https://github.com/decolua/9router)** | Billing | Teams & Self-hosting |
| **[leepokai/Codync](https://github.com/leepokai/Codync)** | Mobile | Desktop UI, MCP |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | MCP |
| **[makecindy/cindy](https://github.com/makecindy/cindy)** | Billing | Billing, Mobile |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Teams & Self-hosting | Desktop UI, Model Routing |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Model Routing, Model Routing |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Mobile | Failover, MCP |
| **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | Mobile | Failover, Model Routing |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP | Billing, Model Routing |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Mobile | Isolation, Sessions & Memory |
| **[generalaction/emdash](https://github.com/generalaction/emdash)** | Parallelism | Desktop UI, Model Routing |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Model Routing | Desktop UI, Model Routing |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Failover | Desktop UI |
| **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | Providers | Sessions & Memory |
| **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | Billing | Billing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation | Parallelism, Sessions & Memory |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Mobile | Isolation, Sessions & Memory |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Parallelism | Billing |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Failover | Desktop UI, Model Routing |
| **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | Billing | Model Routing, Teams & Self-hosting |
| **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | MCP | Failover, Sessions & Memory |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams & Self-hosting | Desktop UI, Model Routing |
| **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | Sessions & Memory | Failover |
| **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | Isolation | Desktop UI, Model Routing |
| **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Mobile | Billing |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | MCP | Desktop UI, Failover |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Billing, Mobile |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Mobile | Desktop UI, Model Routing |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | Isolation | Desktop UI, Failover |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Failover, Model Routing |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Billing | Billing, Sessions & Memory |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Model Routing | Failover, Sessions & Memory |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | MCP | Isolation, Sessions & Memory |
| **[golutra/golutra](https://github.com/golutra/golutra)** | Parallelism | Mobile, Sessions & Memory |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams & Self-hosting | Isolation, Sessions & Memory |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Model Routing | Desktop UI, Failover |
| **[caveman-ai/caveman-code](https://github.com/caveman-ai/caveman-code)** | Parallelism | Desktop UI, Model Routing |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Isolation | Failover, Sessions & Memory |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Sessions & Memory | Desktop UI |
| **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | Parallelism | Failover |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Failover | Desktop UI |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Isolation | Billing, Billing |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Mobile | Desktop UI, Failover |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Model Routing |
| **[Makson179/Bello](https://github.com/Makson179/Bello)** | Billing | Desktop UI, Failover |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Failover, Sessions & Memory |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | MCP | Desktop UI, Failover |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams & Self-hosting | Desktop UI, Model Routing |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Sessions & Memory | Failover, Model Routing |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | MCP | Teams & Self-hosting |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Mobile | MCP |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Parallelism | Desktop UI, Failover |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP | Failover, Model Routing |
| **[oracle/mcp](https://github.com/oracle/mcp)** | MCP | Failover, Model Routing |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | MCP | Billing |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Sessions & Memory | MCP, Model Routing |
| **[Swival/swival](https://github.com/Swival/swival)** | Model Routing | Model Routing |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Billing | Mobile, Sessions & Memory |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | Isolation | Desktop UI, Failover |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Sessions & Memory | Billing, Isolation |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Failover | Desktop UI |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Sessions & Memory | Failover, Model Routing |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation | Desktop UI, Failover |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | MCP |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Sessions & Memory | Failover, MCP |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Billing | Desktop UI |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Teams & Self-hosting | MCP, Parallelism |
| **[labsai/EDDI](https://github.com/labsai/EDDI)** | Teams & Self-hosting | MCP, Sessions & Memory |
| **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | Billing | Billing, Model Routing |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams & Self-hosting | Mobile, Parallelism |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Failover, Sessions & Memory |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Billing, Failover |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Failover | Desktop UI, Sessions & Memory |
| **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | Mobile | Billing, Isolation |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Sessions & Memory | Desktop UI, Model Routing |
| **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | Billing | Billing, Providers |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Model Routing |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Parallelism | Desktop UI, Model Routing |
| **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | Billing | Billing, Teams & Self-hosting |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Failover | Billing, Billing |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Billing | Failover |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Isolation | Parallelism |
| **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Model Routing | Model Routing |
| **[seanbabalala/SiftGate](https://github.com/seanbabalala/SiftGate)** | Teams & Self-hosting | Billing, MCP |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Teams & Self-hosting | Billing, MCP |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Mobile | Failover, Isolation |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Model Routing | Model Routing, Teams & Self-hosting |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Teams & Self-hosting | Desktop UI, Sessions & Memory |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Mobile | Billing, MCP |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Billing, Sessions & Memory |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Parallelism | Billing, Failover |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Sessions & Memory | Failover, Model Routing |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Sessions & Memory | Isolation |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Teams & Self-hosting | MCP, Model Routing |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Parallelism | Teams & Self-hosting |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Failover | Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Model Routing | Failover, Model Routing |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Sessions & Memory | Billing |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Parallelism | Billing |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | Billing | Failover |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI, Failover |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Sessions & Memory | Isolation |
| **[IBM/mcp](https://github.com/IBM/mcp)** | MCP | Desktop UI, Failover |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | MCP | Failover |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.26x the stars (40,937 vs 156,865) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 63.34x the stars (20,394 vs 322) | 🤖 auto (high) |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.03x the stars (12,447 vs 444) | 🤖 auto (high) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 23.18x the stars (309,966 vs 13,375) | 🤖 auto (high) |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.93x the stars (20,394 vs 2,572) | 🤖 auto (high) |
| **[GizClaw/flowcraft](https://github.com/gizclaw/flowcraft)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 4.23x the stars (1,735 vs 410) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.78x the stars (34,476 vs 384) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 43.74x the stars (40,937 vs 936) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.56x the stars (12,447 vs 2,238) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.72x the stars (34,476 vs 939) | 🤖 auto (high) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 141.53x the stars (50,244 vs 355) | 🤖 auto (high) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 100.86x the stars (30,561 vs 303) | 🤖 auto (high) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.25x the stars (50,244 vs 3,793) | 🤖 auto (high) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.43x the stars (12,447 vs 2,293) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.06x the stars (50,244 vs 372) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.22x the stars (12,447 vs 426) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 49.66x the stars (24,928 vs 502) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.55x the stars (50,244 vs 323) | 🤖 auto (high) |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 21.65x the stars (12,447 vs 575) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 491.23x the stars (309,966 vs 631) | 🤖 auto (high) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 11.77x the stars (21,304 vs 1,810) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 49.26x the stars (309,966 vs 6,293) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 159.90x the stars (156,865 vs 981) | 🤖 auto (high) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 54.43x the stars (24,928 vs 458) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 19.51x the stars (27,407 vs 1,405) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.24x the stars (12,447 vs 2,934) | 🤖 auto (high) |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | **[decolua/9router](https://github.com/decolua/9router)** | 4.69x the stars (32,810 vs 6,990) | 🤖 auto (medium) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.19x the stars (30,561 vs 1,888) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.07x the stars (28,218 vs 587) | 🤖 auto (medium) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.74x the stars (1,515 vs 553) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 21.01x the stars (10,525 vs 501) | 🤖 auto (medium) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 35.51x the stars (21,304 vs 600) | 🤖 auto (medium) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.53x the stars (24,928 vs 5,500) | 🤖 auto (medium) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.53x the stars (1,515 vs 429) | 🤖 auto (medium) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.30x the stars (50,244 vs 3,777) | 🤖 auto (medium) |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 14.45x the stars (116,600 vs 8,068) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 72.71x the stars (50,244 vs 691) | 🤖 auto (medium) |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.38x the stars (1,208 vs 508) | 🤖 auto (high) |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 3.44x the stars (27,407 vs 7,957) | 🤖 auto (medium) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.75x the stars (1,515 vs 550) | 🤖 auto (medium) |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 105.62x the stars (116,600 vs 1,104) | 🤖 auto (medium) |
| **[google/artemis](https://github.com/google/artemis)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 9.44x the stars (170,020 vs 18,003) | 🤖 auto (high) |
| **[Arvincreator/project-golem](https://github.com/arvincreator/project-golem)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 1.88x the stars (1,208 vs 642) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hex/claude-council](https://github.com/hex/claude-council)** | 1.96x the stars (960 vs 491) | 🤖 auto (medium) |
| **[Leonxlnx/earshot](https://github.com/leonxlnx/earshot)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 1.85x the stars (10,525 vs 5,702) | 🤖 auto (medium) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | 2.23x the stars (788 vs 354) | 🤖 auto (high) |
| **[vaibhav-space/my-ai-coding-workflow](https://github.com/vaibhav-space/my-ai-coding-workflow)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 146.48x the stars (50,244 vs 343) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.74x the stars (1,515 vs 873) | 🤖 auto (high) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 15.74x the stars (5,572 vs 354) | 🤖 auto (high) |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.21x the stars (678 vs 561) | 🤖 auto (medium) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 2.72x the stars (12,866 vs 4,737) | 🤖 auto (medium) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,113 vs 524) | 🤖 auto (medium) |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/rabiroute)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.38x the stars (678 vs 493) | 🤖 auto (medium) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.25x the stars (1,419 vs 1,137) | 🤖 auto (medium) |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (50,244 vs 28,281) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | failover | 28.3k | 🔻 Superseded | 1.78x the stars (50,244 vs 28,281) |
| **[google/artemis](https://github.com/google/artemis)** | mobile | 18k | 🔻 Superseded | 9.44x the stars (170,020 vs 18,003) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | teams-self-hosting | 13.4k | 🔻 Superseded | 23.18x the stars (309,966 vs 13,375) |
| **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | mobile | 8.1k | 🔻 Superseded | 14.45x the stars (116,600 vs 8,068) |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | mobile | 8k | 🔻 Superseded | 3.44x the stars (27,407 vs 7,957) |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | billing | 7k | 🔻 Superseded | 4.69x the stars (32,810 vs 6,990) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | teams-self-hosting | 6.3k | 🔻 Superseded | 49.26x the stars (309,966 vs 6,293) |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | mcp | 5.7k | 🔻 Superseded | 1.85x the stars (10,525 vs 5,702) |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.5k | 🔻 Superseded | 4.53x the stars (24,928 vs 5,500) |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | teams-self-hosting | 4.7k | 🔻 Superseded | 2.72x the stars (12,866 vs 4,737) |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | failover | 3.8k | 🔻 Superseded | 13.25x the stars (50,244 vs 3,793) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | failover | 3.8k | 🔻 Superseded | 13.30x the stars (50,244 vs 3,777) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams-self-hosting | 2.9k | 🔻 Superseded | 4.24x the stars (12,447 vs 2,934) |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.6k | 🔻 Superseded | 7.93x the stars (20,394 vs 2,572) |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams-self-hosting | 2.3k | 🔻 Superseded | 5.43x the stars (12,447 vs 2,293) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams-self-hosting | 2.2k | 🔻 Superseded | 5.56x the stars (12,447 vs 2,238) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | teams-self-hosting | 1.9k | 🔻 Superseded | 16.19x the stars (30,561 vs 1,888) |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | sessions-memory | 1.8k | 🔻 Superseded | 11.77x the stars (21,304 vs 1,810) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile | 1.4k | 🔻 Superseded | 19.51x the stars (27,407 vs 1,405) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | mobile | 1.1k | 🔻 Superseded | 1.25x the stars (1,419 vs 1,137) |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | mobile | 1.1k | 🔻 Superseded | 105.62x the stars (116,600 vs 1,104) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 981 | 🔻 Superseded | 159.90x the stars (156,865 vs 981) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism | 939 | 🔻 Superseded | 36.72x the stars (34,476 vs 939) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 936 | 🔻 Superseded | 43.74x the stars (40,937 vs 936) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | sessions-memory | 873 | 🔻 Superseded | 1.74x the stars (1,515 vs 873) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | failover | 691 | 🔻 Superseded | 72.71x the stars (50,244 vs 691) |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | mcp | 642 | 🔻 Superseded | 1.88x the stars (1,208 vs 642) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | teams-self-hosting | 631 | 🔻 Superseded | 491.23x the stars (309,966 vs 631) |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | sessions-memory | 600 | 🔻 Superseded | 35.51x the stars (21,304 vs 600) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism | 587 | 🔻 Superseded | 48.07x the stars (28,218 vs 587) |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | teams-self-hosting | 575 | 🔻 Superseded | 21.65x the stars (12,447 vs 575) |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile | 561 | 🔻 Superseded | 1.21x the stars (678 vs 561) |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | sessions-memory | 553 | 🔻 Superseded | 2.74x the stars (1,515 vs 553) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | sessions-memory | 550 | 🔻 Superseded | 2.75x the stars (1,515 vs 550) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | failover | 524 | 🔻 Superseded | 2.12x the stars (1,113 vs 524) |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | mcp | 508 | 🔻 Superseded | 2.38x the stars (1,208 vs 508) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 502 | 🔻 Superseded | 49.66x the stars (24,928 vs 502) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp | 501 | 🔻 Superseded | 21.01x the stars (10,525 vs 501) |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | mobile | 493 | 🔻 Superseded | 1.38x the stars (678 vs 493) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions-memory | 491 | 🔻 Superseded | 1.96x the stars (960 vs 491) |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 458 | 🔻 Superseded | 54.43x the stars (24,928 vs 458) |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | teams-self-hosting | 444 | 🔻 Superseded | 28.03x the stars (12,447 vs 444) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | sessions-memory | 429 | 🔻 Superseded | 3.53x the stars (1,515 vs 429) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams-self-hosting | 426 | 🔻 Superseded | 29.22x the stars (12,447 vs 426) |
| **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | isolation | 410 | 🔻 Superseded | 4.23x the stars (1,735 vs 410) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism | 384 | 🔻 Superseded | 89.78x the stars (34,476 vs 384) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | failover | 372 | 🔻 Superseded | 135.06x the stars (50,244 vs 372) |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | failover | 355 | 🔻 Superseded | 141.53x the stars (50,244 vs 355) |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | isolation | 354 | 🔻 Superseded | 2.23x the stars (788 vs 354) |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | billing-2 | 354 | 🔻 Superseded | 15.74x the stars (5,572 vs 354) |
| **[vaibhav-space/my-ai-coding-workflow](https://github.com/vaibhav-space/my-ai-coding-workflow)** | failover | 343 | 🔻 Superseded | 146.48x the stars (50,244 vs 343) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | failover | 323 | 🔻 Superseded | 155.55x the stars (50,244 vs 323) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 322 | 🔻 Superseded | 63.34x the stars (20,394 vs 322) |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams-self-hosting | 303 | 🔻 Superseded | 100.86x the stars (30,561 vs 303) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-11-24 14:55 UTC. 222 live tools · 124 candidates rejected by the quality gates.</sub>
