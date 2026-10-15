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

**216 tools** across **16 categories** · **56 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-15 09:12 UTC**

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

- [Remote Control & Isolation](#remote-control-isolation) — 35 tools
- [Desktop UI](#desktop-ui) — 33 tools
- [Self-hosting & Security](#self-hosting-security) — 24 tools
- [Analytics](#analytics) — 19 tools
- [Sharing](#sharing) — 14 tools
- [Skills](#skills) — 13 tools
- [Teams](#teams) — 8 tools
- [Providers](#providers) — 11 tools
- [Billing](#billing) — 11 tools
- [Mobile](#mobile) — 10 tools
- [Desktop UI](#desktop-ui) — 9 tools
- [Providers](#providers) — 8 tools
- [Sessions](#sessions) — 7 tools
- [Voice & Remote Control](#voice-remote-control) — 7 tools
- [Analytics](#analytics) — 4 tools
- [Sharing](#sharing) — 3 tools
- [Cross-listed tools](#cross-listed-tools) — tools that span several categories
- [Challengers](#-challengers) — newer tools that may overtake an incumbent
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Remote Control & Isolation

*Remote control*

Your agent runs on a desktop, but you want to drive it from somewhere else.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 92.9k 🚀 +794/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 102.4k 🚀 +582/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 20.9k 🚀 +117/d | **86** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 29.7k 🚀 +513/d | **84** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | AI video skill for Claude Code & Codex — cinematic product videos with Remotion: 152 shot recipe cards, 209 motion previews, a production-ready template | 🟢 Easy | — | — | 12k 🚀 +178/d | **83** |
| 🏆 **[edenfunf/reelmimic](https://github.com/edenfunf/reelmimic)** | It takes a while. A 30–60 second video usually takes 1–3.5 hours after you approve the plan, depending on the Three languages. 繁體中文, English and 简体中文, switch in the top right. | 🟡 Some setup | — | ✅ | 3.3k 🚀 +206/d | **82** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português \| 한국어 We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 83.9k 🚀 +52/d | **76** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.5k 🚀 +27/d | **73** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.5k 🚀 +18/d | **69** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 10.8k 🚀 +21/d | **67** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | 📣 2026-09-30 — Raven's technical report is #1 Paper of the day on Hugging Face. | 🟢 Turnkey | — | — | 5.5k 🚀 +20/d | **67** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 7.9k 🚀 +33/d | **66** |
| ✅ **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | “Pause learning.” Resume with /vibe-wise:learn. | 🟢 Easy | — | ✅ | 3.6k 🚀 +57/d | **66** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9.2k 🚀 +15/d | **66** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 15k 🚀 +15/d | **65** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.5k 🚀 +18/d | **64** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6.1k 🚀 +20/d | **63** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.3k | **61** |
| 🔹 **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. | 🟢 Turnkey | — | ✅ | 2.1k | **61** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.7k | **59** |
| 🔹 **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 한국어 \| 中文 \| Português \| 日本語 \| Français \| Español \| Nederlands \| Polski \| Русский \| Deutsch \| Tiếng Việt \| ภาษาไทย | 🟢 Easy | — | — | 1.3k (+5/d) | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. | 🟡 Some setup | — | — | 1.1k 🚀 +7/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 541 | **57** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. Go beyond code — video, slides, and more — the Commander drives open-source tools like HyperFrames and hands off to CLI agents — the coding agents Cla… | 🟡 Some setup | — | — | 2.2k 🚀 +5/d | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 536 | **56** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 779 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 311 | **55** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 787 (+6/d) | **53** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | The native macOS terminal that keeps your sessions running and tells you the moment a coding agent needs you. | 🟢 Easy | — | ✅ | 305 | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k | **52** |

**Also does this:** [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes), [crshdn/mission-control](https://github.com/crshdn/mission-control), [Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

*…and 5 more in [the full index](data/index.json).*

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

- Stars: **92,870** (+793.6/day over 5d)
- Health score: **92/100**
- Documentation score: **51/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
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

- Stars: **102,352** (+582.0/day over 5d)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
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

- Stars: **20,939** (+117.0/day over 5d)
- Health score: **86/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

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

- Stars: **29,701** (+512.6/day over 5d)
- Health score: **84/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-14

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

- Stars: **11,996** (+178.0/day over 5d)
- Health score: **83/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-13
- Works with: Claude Code, Codex

</details>

## Desktop UI

*Skills & plugins*

The base agent lacks your workflows; you need to extend it.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 151k 🚀 +197/d | **90** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | Taste Skill is a set of Agent Skills that make coding agents design websites instead of assembling the average landing page. | 🟢 Easy | — | — | 96.8k (+409/d) | **88** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟡 Some setup | — | — | 163.9k 🚀 +774/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working is the concept. | 🟡 Some setup | — | — | 11.6k 🚀 +1936/d | **83** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 27.1k 🚀 +40/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.8k 🚀 +26/d | **70** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | An agent skill for building premium, scroll-driven websites, with a real design standard. | 🟢 Easy | — | — | 3.5k 🚀 +65/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Style bleed. The five reports share 57 class names, 13 of which mean different things in different reports (.copy, .kpis, .badge, .chip…), so every selector gets a scope prefix Asset paths. Each report's images are rela… | 🟢 Easy | — | — | 4.6k 🚀 +49/d | **65** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 11.1k 🚀 +37/d | **64** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 3.7k 🚀 +60/d | **63** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | An open skill for agent-to-agent contracts. | 🟢 Easy | — | — | 6.7k 🚀 +35/d | **59** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 6k 🚀 +24/d | **59** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Game Dev Agentic Skills (GDAS) - agent library for Godot 4.7+ and Bevy 0.20+ Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ - AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and a version… | 🟢 Easy | — | — | 854 | **58** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.6k 🚀 +5/d | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1k | **57** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | Built for graduate students, PhDs, postdocs, research support staff, and agent/harness builders who need inspectable research workflows rather than a black box. | 🟢 Easy | — | — | 384 🚀 +15/d | **57** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.8k | **55** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k | **54** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for academic research. audit-analysis: Adversarial audit of changed analysis code, run by an isolated subagent. | 🟢 Turnkey | — | ✅ | 502 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 342 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Genuine utility for developers | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **52** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 301 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.3k 🚀 +8/d | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 897 | **51** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 2.7k 🚀 +17/d | **49** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **47** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 Easy | — | — | 1.1k | **46** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | GRACE means Graph-RAG Anchored Code Engineering: a contract-first AI engineering methodology built around semantic markup, .grace XML artifacts, knowledge-graph navigation, assertions, scopes, and log-driven verificatio… | 🟡 Some setup | — | — | 253 | **44** |
| 👀 **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | A curated collection of Claude Code skills for academic research in economics, finance, and the broader social sciences — organized by the common types of skills a researcher needs across a project's lifecycle. | 🟡 Some setup | — | — | 223 | **44** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [garrytan/gstack](https://github.com/garrytan/gstack), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design), [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) *(+24 more)*

*…and 3 more in [the full index](data/index.json).*

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

- Stars: **150,954** (+196.6/day over 5d)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **96,820** (~408.5/day lifetime average)
- Health score: **88/100**
- Documentation score: **41/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-14
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

- Stars: **163,909** (+773.8/day over 5d)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **11,616** (~1936.0/day lifetime average)
- Health score: **83/100**
- Documentation score: **57/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode

#### [phuryn/pm-skills](https://github.com/phuryn/pm-skills)

> Designed for Claude Code and Cowork.

**Core problems it solves**

- **Usage analytics** — *gles that differentiate us from Notion*
- **Skills & plugins** — *edge), you can force loading skills with /plugin-name:skill-name or /skill-name (Claude will add the prefix).*
- **Notifications** — *framework should I use for a 50-item backlog?*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Linux
- Easy. install via native installer / package; configure database dependency, database migration; beginner-friendly

**Facts**

- Stars: **27,067** (+40.2/day over 5d)
- Health score: **71/100**
- Documentation score: **57/100**
- License: MIT
- Last push: 2026-10-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

</details>

## Self-hosting & Security

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Skills format (SKILL.md with YAML frontmatter) works across Claude Code, Codex, OpenCode, and GitHub Copilot CLI AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitH… | 🟡 Some setup | — | — | 279.8k 🚀 +714/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 18.5k 🚀 +654/d | **88** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 9.7k 🚀 +111/d | **83** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 14.3k 🚀 +84/d | **76** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 5.3k 🚀 +71/d | **76** |
| ✅ **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | AOS gives AI agents a shared local environment for tools, permissions and services. | 🟢 Easy · OOTB | ✅ | — | 8.5k 🚀 +90/d | **75** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine Auth uses JWT middleware in src/middleware/auth.ts | 🟢 Easy | — | — | 29.5k 🚀 +41/d | **73** |
| ✅ **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🟡 Some setup | — | — | 3.7k 🚀 +63/d | **70** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.7k 🚀 +13/d | **68** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 本地优先的 AI 工作台：写代码、做文档、和 Agent 一起推进事情。 模型随你换。 DeepSeek、Kimi、GLM、Qwen、Ollama 等预设，也可自定义 Provider。 | 🟢 Easy | — | ✅ | 6.3k (+43/d) | **66** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k | **61** |
| 🔹 **[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)** | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. | 🟢 Turnkey · OOTB | ✅ | — | 2.5k 🚀 +16/d | **60** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4.1k 🚀 +17/d | **59** |
| 🔹 **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | ╔═════════════════════════════════════════════════════════════════════════════╗ ║ MARKETING NOTES FOR IMAGE ASSETS ║ ║ All images below live under .github/assets/. | 🟡 Some setup | — | — | 2.1k | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k | **58** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 461 | **54** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Interop — the MCP 2026-07-28 client, an MCP server, and A2A in both directions. Models — realtime voice on OpenAI Realtime and Gemini Live, provider batch requests, model profiles, a stable request prefix for Claude 5.x… | 🟢 Easy · OOTB | ✅ | — | 682 | **52** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models Press: USC Viterbi News — Giving AI Agents the Keys? | 🟡 Some setup | — | — | 542 🚀 +5/d | **52** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | Scope Recall v3 is a bounded local memory core with SQLite as the authority and rebuildable vector companions. | 🟢 Easy | — | — | 338 | **49** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | The self-hosted AI backend for private data and tool-using agents. | 🟡 Some setup | — | — | 355 | **48** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | PAXM carries decisions, conventions, and working context into later Codex, Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP sessions. | 🟡 Some setup | — | — | 285 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 414 | **45** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 542 | **40** |

**Also does this:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [getpaseo/paseo](https://github.com/getpaseo/paseo), [topoteretes/cognee](https://github.com/topoteretes/cognee), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [aipoch/open-science](https://github.com/aipoch/open-science), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [spinabot/brigade](https://github.com/spinabot/brigade), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research) *(+16 more)*

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

- Stars: **279,766** (+714.4/day over 5d)
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

- Stars: **18,543** (+654.2/day over 5d)
- Health score: **88/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-15

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

- Stars: **9,719** (+110.6/day over 5d)
- Health score: **83/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **14,287** (+83.8/day over 5d)
- Health score: **76/100**
- Documentation score: **45/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Codex

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

- Stars: **5,309** (+71.4/day over 5d)
- Health score: **76/100**
- Documentation score: **72/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-15
- Works with: Claude Code

</details>

## Analytics

*Memory & context*

Every new session starts from zero and forgets your project's conventions.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 32.3k 🚀 +79/d | **79** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 7.9k 🚀 +78/d | **71** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. | 🟢 Turnkey · OOTB | ✅ | — | 3.4k 🚀 +27/d | **67** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.2k 🚀 +18/d | **62** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | "Automation executes. Autonomy reasons." — @NVIDIAAP | 🟢 Easy | — | — | 4.8k 🚀 +10/d | **62** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.6k 🚀 +23/d | **59** |
| 🔹 **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。 | 🟡 Some setup | — | — | 12.6k 🚀 +19/d | **57** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 421 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 417 | **54** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 840 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 479 | **52** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Intelligent LLM Routing (omega-pro) — Classifies tasks and routes to the optimal model. Secure Profile (omega-pro) — AES-256 encrypted personal data storage with macOS Keychain integration. | 🟡 Some setup | — | — | 224 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 677 | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 487 | **49** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 438 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 246 | **46** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 Involved | — | — | 475 | **41** |

**Also does this:** [garrytan/gstack](https://github.com/garrytan/gstack), [affaan-m/ECC](https://github.com/affaan-m/ECC), [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [spinabot/brigade](https://github.com/spinabot/brigade), [future-agi/future-agi](https://github.com/future-agi/future-agi), [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase), [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp), [thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills) *(+14 more)*

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

- Stars: **32,328** (+79.0/day over 5d)
- Health score: **79/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-15
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

- Stars: **7,926** (+78.2/day over 5d)
- Health score: **71/100**
- Documentation score: **42/100**
- License: MIT
- Language: Python
- Last push: 2026-09-20
- Works with: Codex

#### [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)

> request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it.

**Core problems it solves**

- **Multi-agent orchestration** — *batched tool calls run concurrently in Hermes,*
- **Parallel execution** — *h category, turns, cost, cache), the phase todo above the prompt, parallel shot ×N, full-row diff bands, and a theme of your own — in the OMH TUI bar…*
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

- Stars: **3,379** (+27.2/day over 5d)
- Health score: **67/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-15
- Works with: Claude Code, Codex

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

- Stars: **7,210** (+18.4/day over 5d)
- Health score: **62/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-10-15
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

- Stars: **4,768** (+10.2/day over 5d)
- Health score: **62/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-10
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Sharing

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 129.3k 🚀 +165/d | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | WSL: on Windows, agents inside WSL distros are wired too, and their sessions counted. Use one provider everywhere: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to. | 🟢 Turnkey | — | ✅ | 13.2k 🚀 +995/d | **88** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth、Grok apply_patch 协议兼容，以及账号池错误分类与状态恢复边界参考其开源… Grok CLI 凭据不加密：access token/… | 🟢 Easy | — | ✅ | 19k 🚀 +43/d | **73** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 30.8k 🚀 +57/d | **70** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 31 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 17.4k 🚀 +43/d | **68** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 9.5k 🚀 +43/d | **68** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.4k 🚀 +38/d | **60** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 545 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 242 | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 412 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 交代一句话，它自己规划、动手、验收，把 PPT / Word / Excel / 网页落到你硬盘上。 10-13 「本机/内网放行」支持通配符：192.168.1.: 放一整个网段，*.local:8080 放一类主机名 | 🟡 Some setup | — | — | 318 🚀 +7/d | **51** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.6k 🚀 +11/d | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 897 | **49** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **129,314** (+165.0/day over 5d)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-15
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

- Stars: **13,161** (+995.4/day over 5d)
- Health score: **88/100**
- Documentation score: **61/100**
- License: MIT
- Language: Go
- Last push: 2026-10-15
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

- Stars: **19,002** (+43.2/day over 5d)
- Health score: **73/100**
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

- Stars: **30,830** (+56.8/day over 5d)
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

- Stars: **17,430** (+42.8/day over 5d)
- Health score: **68/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Skills

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 Some setup | — | — | 74.8k 🚀 +164/d | **89** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Trail-code gives Claude Code, Cursor, Codex and other coding agents a map of your code, and what your team has learned about it. | 🟡 Some setup | — | — | 10k 🚀 +98/d | **77** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 10.1k 🚀 +87/d | **75** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17.2k 🚀 +24/d | **64** |
| 🔹 **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens. | 🟢 Easy · OOTB | ✅ | — | 7.5k | **61** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. | 🟡 Some setup | — | — | 11.1k 🚀 +11/d | **59** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.6k | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 342 | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Run an experimental ARC-AGI-3 harness from the ChatGPT UI. a CI-passed aggregator; single-command releases (`node scripts/release.mjs | 🟡 Some setup | — | — | 701 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 709 | **50** |
| 🔹 **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | A multi-provider gateway for Claude Code and other coding agents. Claude tier routing: Fable / Opus / Sonnet / Haiku | 🟢 Easy | — | — | 624 | **49** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 Easy | — | — | 367 | **47** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | arXiv Review Paper Harness is an agentic harness for writing machine-learning and AI review papers in LaTeX. | 🟢 Easy | — | — | 465 | **45** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [yetone/magpie](https://github.com/yetone/magpie), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel), [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory), [zai-org/ZCode](https://github.com/zai-org/ZCode), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) *(+12 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)

> So I built the filter I&nbsp;needed.

**Core problems it solves**

- **Model / provider routing** — *s the same in longer words.*
- **API gateway / proxy** — *s the same in longer words.*
- **Skills & plugins** — *does not duplicate the full project instructions when it reads both AGENTS.md and GEMINI.md.*
- **GUI / desktop app** — *n terminal dashboard lets you browse your pipeline visually:*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Gemini CLI*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx @santifer/career-ops init`
- Platforms mentioned: Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, config file

**Facts**

- Stars: **74,755** (+164.2/day over 5d)
- Health score: **89/100**
- Documentation score: **74/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **10,043** (~97.5/day lifetime average)
- Health score: **77/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **10,131** (+87.0/day over 5d)
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

- Stars: **17,176** (+24.4/day over 5d)
- Health score: **64/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
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
- Last push: 2026-10-14
- Works with: Claude Code, Codex, OpenCode, Cursor

</details>

## Teams

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. | 🟢 Easy | — | — | 55.6k (+307/d) | **90** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 9.4k 🚀 +204/d | **87** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Website: aimemory.sh | 🟡 Some setup | — | — | 9.3k 🚀 +45/d | **67** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k 🚀 +8/d | **62** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.7k 🚀 +7/d | **57** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 4k 🚀 +6/d | **55** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 320 | **47** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [loopx-project/loopx](https://github.com/loopx-project/loopx), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **55,579** (~307.1/day lifetime average)
- Health score: **90/100**
- Documentation score: **68/100**
- License: MIT
- Language: HTML
- Last push: 2026-10-14
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

- Stars: **9,440** (+203.8/day over 5d)
- Health score: **87/100**
- Documentation score: **78/100**
- License: MIT
- Language: Python
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode

#### [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

> Website: aimemory.sh

**Core problems it solves**

- **Workspace isolation** — *box/queue plus the on-start "you have mail" notice.*
- **Model / provider routing** — *s session summaries and enables semantic search.*
- **API gateway / proxy** — *s session summaries and enables semantic search.*
- **Memory & context** — *> Long-term memory for AI coding agents.*
- **Skills & plugins**
- **Agent runtime** — *> Long-term memory for AI coding agents.*
- **MCP support** — *links ~/.local/bin/ai-memory.*
- **Security & isolation**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 55/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://github.com/akitaonrails/ai-memory/releases/latest/download/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via curl | sh installer, native installer / package; needs docker run, git clone (build from source); configure environment variables, config.json/yaml/toml

**Facts**

- Stars: **9,321** (+44.6/day over 5d)
- Health score: **67/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)

> Linear Chain-of-Thought anchors on whatever it says first.

**Core problems it solves**

- **Multi-agent orchestration** — *vs 6, novelty 8 vs 3, trap detection ~8 vs ~2.*
- **Billing & metering** — *ndpoints at 30s; daemonize the CLI with ticket IDs; race 3 LLM replicas, cache the winner.*
- **Skills & plugins** — *# ADHD — a skill for agents*
- **Agent runtime** — *zy debugging, naming, API surface design, strategy, and any prompt of the shape *"give me a few ways to…".*
- **Team collaboration** — *Open to collaboration with research labs and applied-AI teams working on reasoning, planning, and agentic systems.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 9/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `npx skills add UditAkhourii/adhd`
- Platforms mentioned: Linux
- Turnkey. install via npx one-liner, global npm install; needs npm install/build; one-click setup

**Facts**

- Stars: **4,418** (+8.4/day over 5d)
- Health score: **62/100**
- Documentation score: **58/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex, Gemini CLI, Cursor, Cline / Roo

#### [felinics/Memoh](https://github.com/felinics/Memoh)

> Desktop, browser, network, and long-term memory — always on, even when your laptop is closed.

**Core problems it solves**

- **Multi-agent orchestration** — *wser, network, and long-term memory — always on, even when your laptop is closed.*
- **Workspace isolation**
- **Memory & context**
- **MCP support** — *aude Code and Codex agents inside Memoh workspaces.*
- **Self-hostable** — *ols, and run scheduled tasks.*
- **Team collaboration** — *egram, Discord, Lark, WeChat, Web UI, and more.*
- **GUI / desktop app**
- **Notifications** — *xisting bare-metal install)? Leave internalrpc.shared_secret empty in config.toml: the server then embeds the channel runtime and keeps running as a…*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://memoh.sh | sh`
- Platforms mentioned: Web
- Some setup. install via curl | sh installer, native installer / package; needs docker compose up, git clone (build from source); configure config.json/yaml/toml, sign-in required

**Facts**

- Stars: **2,700** (+7.4/day over 5d)
- Health score: **57/100**
- Documentation score: **53/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-15
- Works with: Claude Code, Codex

</details>

## Providers

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 144.5k 🚀 +456/d | **93** |
| ✅ **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Each hook is approved. Codex stores each approval as a trusted_hash under [hooks.state]. Approving them in an interactive codex session is expected to write these (inferred: the #345 check… Subagents get sharper context… | 🟡 Some setup | — | — | 5.3k 🚀 +68/d | **72** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.4k 🚀 +16/d | **67** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Connect Core (steps 4–7): create a tunnel and a restricted API key at OpenAI, press Connect, then add the app in ChatGPT under Plugins → Add → Add custom MCP server. Share a folder and choose access (steps 2–3): the fol… | 🟢 Easy | — | — | 4.8k 🚀 +63/d | **67** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi is a fast, self-contained terminal AI coding agent. | 🟢 Easy | — | — | 3.3k 🚀 +46/d | **66** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.6k 🚀 +14/d | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 283 | **53** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 431 | **52** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 446 | **51** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 315 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 516 | **43** |

**Also does this:** [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy), [chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory), [nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)

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

- Stars: **144,547** (+455.6/day over 5d)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **5,326** (+67.8/day over 5d)
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

- Stars: **27,383** (+16.2/day over 5d)
- Health score: **67/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

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

- Stars: **4,768** (+63.0/day over 5d)
- Health score: **67/100**
- Documentation score: **33/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Codex

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

- Stars: **3,342** (~46.4/day lifetime average)
- Health score: **66/100**
- Documentation score: **63/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-09-29

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 44.1k 🚀 +91/d | **79** |
| ✅ **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 107.4k 🚀 +22/d | **71** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 4.9k 🚀 +47/d | **71** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点 | 🟡 Some setup | — | — | 2.7k 🚀 +13/d | **60** |
| 🔹 **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file… | 🔴 Involved | — | — | 3.1k (+21/d) | **58** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.3k 🚀 +25/d | **52** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 405 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 797 | **50** |
| 🔹 **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | The system of record for fintech wallets, payouts, marketplaces and billing — with spending limits that keep AI agents in check and an audit trail you can prove. | 🟡 Some setup | — | — | 408 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k | **48** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 425 | **46** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [decolua/9router](https://github.com/decolua/9router), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills), [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **44,081** (+90.8/day over 5d)
- Health score: **79/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

> Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal.

**Core problems it solves**

- **Model / provider routing**
- **Billing & metering** — *pers who need specific model control or paid tier access*
- **Usage analytics**
- **Session persistence**
- **Skills & plugins**
- **MCP support** — *contributions! Gemini CLI is fully open source (Apache 2.0), and we*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx @google/gemini-cli`
- Platforms mentioned: macOS, Linux, Web
- Easy. install via npx one-liner, Homebrew install; needs git clone (build from source), npm install/build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **107,379** (+22.2/day over 5d)
- Health score: **71/100**
- Documentation score: **69/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Gemini CLI
- *Why it is seeded: Gemini's terminal agent, generous free tier.*

#### [aipoch/open-science](https://github.com/aipoch/open-science)

> AI research workbench for reproducible science — open-source, local-first, and model-agnostic.

**Core problems it solves**

- **Remote control** — *greatly appreciate a star on GitHub.*
- **Model / provider routing** — *overview - Node.js quick start and package entry point*
- **Billing & metering** — *### Why does the model connection test fail? A: Check the API Key for missing characters or spaces, verify the Base URL and region, use the provider'…*
- **Skills & plugins** — *s to the skill, not to the availability of every registered host.*
- **MCP support** — *Marketplace contributions are published after review; local imports do not publish skills.*
- **Security & isolation** — *untime owns each data directory.*
- **GUI / desktop app** — *owser share that service.*
- **Cross-agent support** — *Mentions Claude Code, Codex, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install --cask open-science`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **4,877** (~46.9/day lifetime average)
- Health score: **71/100**
- Documentation score: **76/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode

#### [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

> 自选与持仓 · 每日复盘 · 产业资讯 · 产业研究 · 个股深挖 · 回测 · 研报库 · 168 个数据端点

**Core problems it solves**

- **Quota & usage management** — *fig.json 写 provider.profile（如 cli-claude），或者添加时带上环境变量，例如 claude mcp add vibe-research -e VRAPROVIDER=cli-claude -- node …、codex mcp add vibe-research…*
- **Remote control**
- **Multi-agent orchestration** — *calculations.json：派生数字的输入、函数和计算 DAG。*
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

- Stars: **2,707** (+13.0/day over 5d)
- Health score: **60/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-11
- Works with: Claude Code, Codex, Cursor

#### [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)

> Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file storage, RAG, durab…

**Core problems it solves**

- **Multi-agent orchestration** — *— full production-shaped apps: butterSupport, butterbaseCRM.*
- **Billing & metering** — *ers, lease-based quota enforcement, and ops dashboards (those live in a private repo that consumes this one as a submodule).*
- **Memory & context** — *AI-native, open-source backend-as-a-service.*
- **Skills & plugins** — *QuotaEnforcer, and RouterAdapter interfaces in packages/shared.*
- **MCP support** — *AI-native, open-source backend-as-a-service.*
- **Security & isolation** — *endpoints (/auto-api), and migrations.*
- **Self-hostable** — *AI-native, open-source backend-as-a-service.*
- **Notifications** — *, GitHub, Apple, X, …), JWT tuning, post-login hooks, service keys (/auth, /oauth-config, /api-keys).*

**Getting it running**

- Setup: 🔴 **Involved** (friction 67/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -sf http://localhost:4000/health/ready`
- Platforms mentioned: Linux, Web
- Involved setup. install via npx one-liner; needs docker compose up, git clone (build from source); configure API key configuration, OAuth login flow

**Facts**

- Stars: **3,112** (~21.0/day lifetime average)
- Health score: **58/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-13
- Works with: Claude Code

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 11.7k 🚀 +91/d | **76** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.2k 🚀 +15/d | **64** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.4k 🚀 +21/d | **64** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 2.9k 🚀 +67/d | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.4k 🚀 +14/d | **55** |
| 🔹 **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 一个适配 Claude Code / Codex 等 Agent 环境的图文卡片技能,用于从文章、文案、截图、产品笔记、字幕、照片或用户视频生成小红书 / Rednote 图文组图、Live Photo 动态卡与公众号 21:9 + 1:1 封面对。 | 🟢 Easy | — | — | 7.5k 🚀 +17/d | **54** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 284 | **53** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Official agent skills/plugins for Power Platform development by Microsoft. Launch GitHub Copilot CLI or Claude Code with the plugin path: | 🟡 Some setup | — | — | 1k 🚀 +5/d | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 548 | **51** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Control your Pi coding agent from your phone. | 🟢 Easy | — | — | 449 | **50** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot), [loopx-project/loopx](https://github.com/loopx-project/loopx), [simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research), [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go), [yetone/cumora](https://github.com/yetone/cumora), [h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)

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

- Stars: **11,733** (+91.2/day over 5d)
- Health score: **76/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

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

- Stars: **24,153** (+14.8/day over 5d)
- Health score: **64/100**
- Documentation score: **29/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-14
- Works with: Claude Code, Codex
- *Why it is seeded: Drive Claude Code / Codex from a phone with end-to-end encryption.*

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

- Stars: **4,386** (+21.4/day over 5d)
- Health score: **64/100**
- Documentation score: **61/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-09-23
- Works with: Claude Code, Codex, Cursor, Copilot, Cline / Roo

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

- Stars: **2,866** (+67.2/day over 5d)
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

- Stars: **3,441** (+14.0/day over 5d)
- Health score: **55/100**
- Documentation score: **42/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-18

</details>

## Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 213.7k 🚀 +236/d | **90** |
| 🏆 **[bherbruck/solidcraft](https://github.com/bherbruck/solidcraft)** | An open-source parametric 3D CAD application built in pure Rust. Parameters and configurations with unit-aware expressions (2 * width + 5 mm, | 🟢 Turnkey · OOTB | ✅ | ✅ | 2.5k 🚀 +361/d | **84** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 8.9k 🚀 +75/d | **74** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 15k 🚀 +15/d | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.6k 🚀 +10/d | **61** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 465 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). orcarouter: OpenAI-compatible model gateway with namespaced model IDs. | 🔴 Involved | — | — | 1.7k | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 747 | **50** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Project Golem 不是單純聊天機器人，而是一套可運行的 AI 工作系統。 /dashboard/action-gate：Action Gate（高風險操作核准流） | 🟡 Some setup | — | — | 641 | **38** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [openai/codex](https://github.com/openai/codex), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [zai-org/ZCode](https://github.com/zai-org/ZCode), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [slopus/happy](https://github.com/slopus/happy) *(+29 more)*

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

- Stars: **213,653** (+236.4/day over 5d)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

#### [bherbruck/solidcraft](https://github.com/bherbruck/solidcraft)

> An open-source parametric 3D CAD application built in pure Rust.

**Core problems it solves**

- **MCP support** — *, constrain, and build solids with a parametric feature timeline.*
- **GUI / desktop app** — *ll video, recorded with the demo script.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via winget install, native installer / package; GUI application

**Facts**

- Stars: **2,530** (~361.4/day lifetime average)
- Health score: **84/100**
- Documentation score: **59/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-15
- Works with: Claude Code

#### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

> BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into.

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

- Stars: **8,934** (+75.4/day over 5d)
- Health score: **74/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
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

- Stars: **15,018** (+14.8/day over 5d)
- Health score: **64/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-15
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

- Stars: **1,633** (+10.0/day over 5d)
- Health score: **61/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 3.6k 🚀 +50/d | **73** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.2k 🚀 +17/d | **57** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format transformation. | 🟢 Easy | — | — | 986 | **55** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁移。 工作台完整保留：任务看板、Git、文件交付、模型协作、桌宠、15 套皮肤、SSH 与远程访问继续提供；恢复 4.4.0 品牌图标。 | 🟢 Turnkey · OOTB | ✅ | — | 814 🚀 +5/d | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 725 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 435 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 589 | **46** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **3,645** (+50.4/day over 5d)
- Health score: **73/100**
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

- Stars: **4,213** (+16.8/day over 5d)
- Health score: **57/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-09
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

- Stars: **986** (+0.2/day over 5d)
- Health score: **55/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-09
- Works with: Claude Code, OpenCode

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

- Stars: **814** (+4.6/day over 5d)
- Health score: **54/100**
- Documentation score: **43/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-10-06
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

- Stars: **725** (+0.4/day over 5d)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-12
- Works with: Claude Code, Cursor

</details>

## Sessions

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 7.8k 🚀 +44/d | **69** |
| 🔹 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | This one is invisible to anti-bots. | 🟢 Turnkey · OOTB | ✅ | — | 2.8k 🚀 +9/d | **58** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.8k 🚀 +10/d | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Monitor Claude Code, Cursor, and Codex sessions in real time. Run and resume agents: Launch Claude Code or Codex, stream output, send follow-ups, resume previous work, and reattach to background runs. | 🟢 Easy | — | — | 1.1k | **55** |
| 🔹 **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | Park, J.S. et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. UIST 2023. doi:10.1145/3586183.3606763 Liu, N.F. et al. (2024). Lost in the Middle: How Language Models Use Long Contexts. TACL 12, 1… | 🟡 Some setup | — | — | 224 | **53** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew brings task execution, human approvals, persistent memory, and scheduled work into one desktop application. | 🟡 Some setup | — | ✅ | 251 | **49** |
| 👀 **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | Meet Tara, your 24/7 personal assistant powered by Claude Code and OpenAI Codex. | 🔴 Involved | — | — | 517 | **38** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent), [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude), [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck), [greenfield-inc/Pane](https://github.com/greenfield-inc/Pane), [RealZST/HarnessKit](https://github.com/RealZST/HarnessKit), [WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills) *(+11 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [zai-org/ZCode](https://github.com/zai-org/ZCode)

> ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。

**Core problems it solves**

- **Remote control**
- **Model / provider routing**
- **Session persistence**
- **Agent runtime**
- **Self-hostable** — *## 更新 - 2026-10-10：更新至 ZCode v3.15.1 版本。*
- **GUI / desktop app** — *pnpm --filter @zcode/cli...*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via native installer / package; needs pnpm install/build; configure OAuth login flow; GUI application

**Facts**

- Stars: **7,841** (+43.9/day over 7d)
- Health score: **69/100**
- Documentation score: **44/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-10

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

- Stars: **2,753** (+9.4/day over 5d)
- Health score: **58/100**
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

- Stars: **1,760** (+9.8/day over 5d)
- Health score: **56/100**
- Documentation score: **47/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-15
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

- Stars: **1,078** (+4.0/day over 5d)
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
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Droid

</details>

## Voice & Remote Control

*Voice input*

Typing long prompts on a phone is painful.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 160.2k 🚀 +311/d | **98** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. | 🟡 Some setup | — | — | 136.5k 🚀 +137/d | **90** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 5.3k 🚀 +131/d | **84** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | The open-source Grok Bot alternative: your own team of AI bots, in a chat app. Local first. | 🟢 Easy | — | — | 4.9k 🚀 +76/d | **76** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 8.8k 🚀 +28/d | **68** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.7k 🚀 +8/d | **64** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 409 | **54** |

**Also does this:** [getpaseo/paseo](https://github.com/getpaseo/paseo), [slopus/happy](https://github.com/slopus/happy), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

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

- Stars: **160,180** (+310.6/day over 5d)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **136,462** (+136.6/day over 5d)
- Health score: **90/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **5,251** (+131.0/day over 5d)
- Health score: **84/100**
- Documentation score: **62/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

> The open-source Grok Bot alternative: your own team of AI bots, in a chat app.

**Core problems it solves**

- **Mobile access** — *protected by pairing, an existing*
- **Multi-agent orchestration** — *n/ macOS, Windows, and Ubuntu shells with an embedded harness and platform capabilities; Apple speech stays macOS-only, Ubuntu Xorg has opt-in local…*
- **Model / provider routing** — *rs can add their own MCP tool servers with zero code via docs/custom-mcp-servers.md.*
- **API gateway / proxy** — *g — see docs/custom-engines.md.*
- **Skills & plugins** — *skills switched off and routines paused.*
- **MCP support** — *ure bots/channels/tasks, send work, wait for completion, switch models, and interrupt turns.*
- **Security & isolation** — *ks before a potentially billable test message.*
- **Self-hostable**

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g openmausbot`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Easy. install via npx one-liner, global npm install; needs git clone (build from source), pnpm install/build; configure API key configuration, OAuth login flow; explicitly no coding required

**Facts**

- Stars: **4,895** (~76.5/day lifetime average)
- Health score: **76/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Codex, Cursor, Cline / Roo

#### [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)

> Free, open source and performant.

**Core problems it solves**

- **Multi-agent orchestration** — *Everything is visible: you watch avatars move, envelopes fly, and the live terminal stream;*
- **Parallel execution** — *A GOD orchestrator you talk to.*
- **Workspace isolation** — *d avatar state reflects real work.*
- **Model / provider routing** — *led right, and you can add your own.*
- **Usage analytics** — *hareable hires and the Agent Gallery, observability and the circuit*
- **Session persistence** — *a built-in Monaco IDE with git rails, integrations registry + secret broker,*
- **Memory & context** — *al-agent CLIs as fully-capable agents,*
- **Skills & plugins** — *The floor - Every terminal is a real agent.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install        # postinstall rebuilds node-pty against Electron's ABI`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via native installer / package; needs git clone (build from source), npm install/build; configure sign-in required, database dependency; one-click setup

**Facts**

- Stars: **8,769** (+27.8/day over 5d)
- Health score: **68/100**
- Documentation score: **74/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 Some setup | — | — | 6.3k 🚀 +16/d | **65** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.2k | **53** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons,… | 🟡 Some setup | — | — | 729 | **43** |

**Also does this:** [decolua/9router](https://github.com/decolua/9router), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [Justin0504/Aegis](https://github.com/Justin0504/Aegis), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

<details>
<summary><b>Why these tools — 4 detailed breakdowns</b></summary>

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

- Stars: **6,309** (+15.6/day over 5d)
- Health score: **65/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-15
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

- Stars: **2,151** (+0.4/day over 5d)
- Health score: **53/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-16
- Works with: Droid

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

- Stars: **5,886** (+0.4/day over 5d)
- Health score: **50/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

#### [nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)

> A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons, and a rule-based ti…

**Core problems it solves**

- **Automatic failover**
- **Multi-agent orchestration**
- **Parallel execution** — *000 python3 cli.py dashboard.*
- **Usage analytics**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via winget install; needs git clone (build from source); configure environment variables, database dependency

**Facts**

- Stars: **729** (+1.2/day over 5d)
- Health score: **43/100**
- Documentation score: **54/100**
- License: MIT
- Language: Python
- Last push: 2026-04-20
- Works with: Claude Code

</details>

## Sharing

*Quota sharing / splitting*

A subscription's capacity is larger than one person needs; share it safely with others.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is the 1st collaborative AI design agent workspace. 🤖 Agent-native, model-agnostic. | 🟢 Easy | — | — | 101.2k 🚀 +187/d | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 557 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 241 | **42** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

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

- Stars: **101,249** (+187.4/day over 5d)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-15
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

> One proxy.

**Core problems it solves**

- **Quota & usage management**
- **Automatic failover** — *cation providing universal /v1/chat/completions (OpenAI) and /v1/messages (Anthropic) endpoints*
- **Model / provider routing** — *LiteLLM-supported provider once.*
- **API gateway / proxy**
- **Quota sharing / splitting**
- **Usage analytics**
- **Skills & plugins**
- **Security & isolation**

**Getting it running**

- Setup: 🔴 **Involved** (friction 66/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker run -d \`
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via pip install, native installer / package; needs docker compose up, docker run; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **557** (+0.2/day over 5d)
- Health score: **49/100**
- Documentation score: **70/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-09-23
- Works with: Claude Code, Gemini CLI, OpenCode, Cursor

#### [wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

> ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API.

**Core problems it solves**

- **Multi-account switching**
- **Model / provider routing** — *way endpoints for chat, responses, models, embeddings, image, and streaming workloads.*
- **API gateway / proxy**
- **Quota sharing / splitting** — *oarding, and configurable private-account access flows.*
- **Billing & metering** — *a self-hosted AI API gateway and subscription management platform based on Sub2API.*
- **Self-hostable** — *a resets, service interruptions, upstream policy changes, and billing errors are operational risks that must be handled by the deployer.*
- **GUI / desktop app** — *clients that send headers containing underscores, enable underscore headers in the Nginx http block:*
- **Cross-agent support** — *Mentions Codex, OpenCode*

**Getting it running**

- Setup: 🔴 **Involved** (friction 69/100)
- Out of the box: no
- Non-programmer friendly: no
- Involved setup. needs make build; configure API key configuration, config file

**Facts**

- Stars: **241** (+0.0/day over 5d)
- Health score: **42/100**
- Documentation score: **41/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-09-17
- Works with: Codex, OpenCode

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Voice & Remote Control | Desktop UI, Teams |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Sharing | Sessions, Skills |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Providers |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Remote Control & Isolation | Mobile, Sharing |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Desktop UI | Desktop UI, Sessions |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Voice & Remote Control | Analytics, Desktop UI |
| **[openai/codex](https://github.com/openai/codex)** | Sharing | Desktop UI |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Self-hosting & Security | Analytics, Sessions |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Remote Control & Isolation | Self-hosting & Security, Sessions |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Sharing | Sharing, Skills |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Desktop UI, Skills |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Remote Control & Isolation | Self-hosting & Security, Voice & Remote Control |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Voice & Remote Control | Desktop UI, Mobile |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Self-hosting & Security | Billing, Skills |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Billing | Sharing, Sharing |
| **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | Analytics | Self-hosting & Security |
| **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | Skills | Desktop UI |
| **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | Voice & Remote Control | Mobile, Self-hosting & Security |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Remote Control & Isolation | Providers, Sessions |
| **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | Providers | Skills |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Self-hosting & Security | Desktop UI, Desktop UI |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Sharing | Billing, Providers |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Providers | Analytics, Desktop UI |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Billing | Analytics, Providers |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Billing | Self-hosting & Security |
| **[decolua/9router](https://github.com/decolua/9router)** | Sharing | Analytics, Billing |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | Self-hosting & Security | Analytics, Skills |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Sessions | Desktop UI, Skills |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Sharing | Sharing, Skills |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Voice & Remote Control | Desktop UI, Sessions |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Remote Control & Isolation | Desktop UI, Skills |
| **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Remote Control & Isolation | Desktop UI, Skills |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Self-hosting & Security, Skills |
| **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Analytics | Remote Control & Isolation, Skills |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | Providers | Self-hosting & Security, Skills |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Mobile, Teams |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Remote Control & Isolation | Providers, Self-hosting & Security |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Desktop UI, Voice & Remote Control |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Skills | Providers, Self-hosting & Security |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Voice & Remote Control | Analytics, Self-hosting & Security |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Desktop UI |
| **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Teams | Desktop UI, Desktop UI |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Analytics | Desktop UI, Skills |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Remote Control & Isolation | Analytics, Self-hosting & Security |
| **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Sharing | Desktop UI |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Billing | Mobile, Self-hosting & Security |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Desktop UI | Desktop UI |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | Self-hosting & Security | Analytics, Skills |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Remote Control & Isolation | Analytics, Desktop UI |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Analytics | Providers, Skills |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Billing | Analytics, Self-hosting & Security |
| **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | Sessions | Analytics |
| **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Self-hosting & Security | Mobile |
| **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | Remote Control & Isolation | Desktop UI, Sessions |
| **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | Desktop UI | Analytics, Desktop UI |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Analytics, Desktop UI |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Desktop UI | Desktop UI, Sessions |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Teams | Analytics, Self-hosting & Security |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Remote Control & Isolation | Providers, Sessions |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Desktop UI | Desktop UI |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Remote Control & Isolation | Desktop UI, Sessions |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Desktop UI | Desktop UI, Sessions |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | Desktop UI | Desktop UI, Sessions |
| **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Remote Control & Isolation | Desktop UI, Skills |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Mobile, Skills |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Desktop UI | Desktop UI, Skills |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Sessions | Desktop UI, Desktop UI |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Remote Control & Isolation | Analytics, Self-hosting & Security |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Remote Control & Isolation | Mobile, Providers |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Desktop UI | Analytics, Sessions |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Desktop UI, Desktop UI |
| **[erickochen/purple](https://github.com/erickochen/purple)** | Providers | Self-hosting & Security |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | Sharing | Sharing |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Analytics, Desktop UI |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Analytics | Self-hosting & Security, Skills |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Voice & Remote Control | Billing, Teams |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Remote Control & Isolation, Self-hosting & Security |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | Remote Control & Isolation | Desktop UI, Self-hosting & Security |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Mobile | Analytics, Teams |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Providers | Analytics, Desktop UI |
| **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | Sessions | Analytics, Self-hosting & Security |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Remote Control & Isolation | Desktop UI, Self-hosting & Security |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | Analytics | Remote Control & Isolation |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Desktop UI | Desktop UI |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Analytics | Desktop UI, Sessions |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | Skills | Desktop UI, Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Self-hosting & Security | Analytics, Teams |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Self-hosting & Security |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Providers | Analytics |
| **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | Remote Control & Isolation | Desktop UI, Sessions |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Sharing | Analytics, Providers |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Remote Control & Isolation | Sessions, Voice & Remote Control |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Remote Control & Isolation | Analytics, Sessions |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Desktop UI |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Sharing | Desktop UI, Sessions |
| **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | Sharing | Remote Control & Isolation, Self-hosting & Security |
| **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Analytics | Sessions, Skills |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | Remote Control & Isolation | Desktop UI, Desktop UI |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Desktop UI | Desktop UI, Sessions |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Analytics | Desktop UI, Sessions |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Mobile | Desktop UI, Desktop UI |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | Billing | Self-hosting & Security |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Sharing | Analytics, Providers |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Analytics | Providers |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Remote Control & Isolation | Teams, Voice & Remote Control |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | Sessions | Analytics, Self-hosting & Security |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Billing | Providers, Sharing |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Desktop UI, Remote Control & Isolation |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Self-hosting & Security | Skills |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Teams | Remote Control & Isolation |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | Self-hosting & Security | Analytics |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Self-hosting & Security | Desktop UI, Sessions |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Desktop UI, Desktop UI |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Analytics | Desktop UI |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Analytics | Desktop UI |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | Skills | Desktop UI |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Self-hosting & Security | Desktop UI, Desktop UI |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Providers | Analytics, Self-hosting & Security |
| **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | Analytics | Providers |
| **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Providers | Analytics |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Desktop UI | Billing, Skills |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Sharing | Billing, Skills |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Analytics | Self-hosting & Security |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | Desktop UI | Desktop UI, Self-hosting & Security |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | Desktop UI | Desktop UI, Sessions |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | Sessions | Analytics, Desktop UI |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.09x the stars (13,161 vs 144,547) |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 58.11x the stars (19,002 vs 327) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 220.18x the stars (83,890 vs 381) | 🤖 auto (high) |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 8.97x the stars (2,091 vs 233) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.49x the stars (9,440 vs 2,101) | 🤖 auto (high) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 877.01x the stars (279,766 vs 319) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 65.02x the stars (279,766 vs 4,303) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.34x the stars (33,545 vs 923) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.99x the stars (20,939 vs 5,245) | 🤖 auto (high) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 3.02x the stars (854 vs 283) | 🤖 auto (high) |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 56.38x the stars (33,545 vs 595) | 🤖 auto (high) |
| **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 49.99x the stars (33,545 vs 671) | 🤖 auto (high) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 96.67x the stars (33,545 vs 347) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 20.86x the stars (102,352 vs 4,906) | 🤖 auto (high) |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 234.75x the stars (102,352 vs 436) | 🤖 auto (high) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.84x the stars (13,658 vs 392) | 🤖 auto (high) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 11.14x the stars (4,768 vs 428) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 27.20x the stars (9,440 vs 347) | 🤖 auto (high) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 23.85x the stars (20,939 vs 878) | 🤖 auto (high) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 75.71x the stars (19,002 vs 251) | 🤖 auto (high) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.43x the stars (33,545 vs 274) | 🤖 auto (high) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 58.61x the stars (29,482 vs 503) | 🤖 auto (high) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 456.39x the stars (279,766 vs 613) | 🤖 auto (high) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.38x the stars (144,547 vs 8,822) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 25.38x the stars (9,719 vs 383) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 79.25x the stars (29,482 vs 372) | 🤖 auto (high) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 46.46x the stars (279,766 vs 6,022) | 🤖 auto (high) |
| **[spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** | **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | 14.91x the stars (5,309 vs 356) | 🤖 auto (high) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 72.90x the stars (102,352 vs 1,404) | 🤖 auto (high) |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 6.64x the stars (102,352 vs 15,419) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.44x the stars (9,440 vs 2,747) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 8.70x the stars (4,768 vs 548) | 🤖 auto (medium) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 7.36x the stars (9,440 vs 1,282) | 🤖 auto (medium) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.90x the stars (29,482 vs 1,745) | 🤖 auto (medium) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.87x the stars (854 vs 298) | 🤖 auto (high) |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.94x the stars (7,210 vs 725) | 🤖 auto (medium) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 3.69x the stars (2,091 vs 567) | 🤖 auto (medium) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 7.57x the stars (4,768 vs 630) | 🤖 auto (high) |
| **[AndrewDryga/emisar](https://github.com/andrewdryga/emisar)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 87.48x the stars (29,482 vs 337) | 🤖 auto (medium) |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 43.04x the stars (279,766 vs 6,500) | 🤖 auto (medium) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 34.45x the stars (9,440 vs 274) | 🤖 auto (medium) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 3.88x the stars (1,085 vs 280) | 🤖 auto (medium) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 590.22x the stars (279,766 vs 474) | 🤖 auto (medium) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.38x the stars (854 vs 359) | 🤖 auto (high) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 25.39x the stars (33,545 vs 1,321) | 🤖 auto (high) |
| **[AI-QL/tuui](https://github.com/ai-ql/tuui)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 25.48x the stars (29,482 vs 1,157) | 🤖 auto (medium) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 49.79x the stars (279,766 vs 5,619) | 🤖 auto (medium) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.54x the stars (9,440 vs 3,716) | 🤖 auto (medium) |
| **[MoonshotAI/kimi-code](https://github.com/moonshotai/kimi-code)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 4.26x the stars (33,545 vs 7,873) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 1.88x the stars (701 vs 373) | 🤖 auto (medium) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 5.97x the stars (4,768 vs 798) | 🤖 auto (high) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 1.39x the stars (1,052 vs 755) | 🤖 auto (medium) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.26x the stars (1,078 vs 476) | 🤖 auto (high) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.15x the stars (20,939 vs 5,046) | 🤖 auto (medium) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.16x the stars (311 vs 268) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.50x the stars (854 vs 568) | 🤖 auto (high) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.15x the stars (1,048 vs 487) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[yc-software/qm](https://github.com/yc-software/qm)** | remote-control-isolation | 15.4k | 🔻 Superseded | 6.64x the stars (102,352 vs 15,419) |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | providers | 8.8k | 🔻 Superseded | 16.38x the stars (144,547 vs 8,822) |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | remote-control-isolation | 7.9k | 🔻 Superseded | 4.26x the stars (33,545 vs 7,873) |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | self-hosting-security | 6.5k | 🔻 Superseded | 43.04x the stars (279,766 vs 6,500) |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | self-hosting-security | 6k | 🔻 Superseded | 46.46x the stars (279,766 vs 6,022) |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | self-hosting-security | 5.6k | 🔻 Superseded | 49.79x the stars (279,766 vs 5,619) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | remote-control-isolation | 5.2k | 🔻 Superseded | 3.99x the stars (20,939 vs 5,245) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | remote-control-isolation | 5k | 🔻 Superseded | 4.15x the stars (20,939 vs 5,046) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | remote-control-isolation | 4.9k | 🔻 Superseded | 20.86x the stars (102,352 vs 4,906) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | self-hosting-security | 4.3k | 🔻 Superseded | 65.02x the stars (279,766 vs 4,303) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 Superseded | 2.54x the stars (9,440 vs 3,716) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 Superseded | 3.44x the stars (9,440 vs 2,747) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 Superseded | 4.49x the stars (9,440 vs 2,101) |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | self-hosting-security | 1.7k | 🔻 Superseded | 16.90x the stars (29,482 vs 1,745) |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | remote-control-isolation | 1.4k | 🔻 Superseded | 72.90x the stars (102,352 vs 1,404) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | remote-control-isolation | 1.3k | 🔻 Superseded | 25.39x the stars (33,545 vs 1,321) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 7.36x the stars (9,440 vs 1,282) |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | self-hosting-security | 1.2k | 🔻 Superseded | 25.48x the stars (29,482 vs 1,157) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | remote-control-isolation | 923 | 🔻 Superseded | 36.34x the stars (33,545 vs 923) |
| **[hex/claude-council](https://github.com/hex/claude-council)** | remote-control-isolation | 878 | 🔻 Superseded | 23.85x the stars (20,939 vs 878) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | analytics | 798 | 🔻 Superseded | 5.97x the stars (4,768 vs 798) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 Superseded | 1.39x the stars (1,052 vs 755) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | analytics | 725 | 🔻 Superseded | 9.94x the stars (7,210 vs 725) |
| **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | remote-control-isolation | 671 | 🔻 Superseded | 49.99x the stars (33,545 vs 671) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | analytics | 630 | 🔻 Superseded | 7.57x the stars (4,768 vs 630) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | self-hosting-security | 613 | 🔻 Superseded | 456.39x the stars (279,766 vs 613) |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | remote-control-isolation | 595 | 🔻 Superseded | 56.38x the stars (33,545 vs 595) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | desktop-ui | 568 | 🔻 Superseded | 1.50x the stars (854 vs 568) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | remote-control-isolation | 567 | 🔻 Superseded | 3.69x the stars (2,091 vs 567) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | analytics | 548 | 🔻 Superseded | 8.70x the stars (4,768 vs 548) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | self-hosting-security | 503 | 🔻 Superseded | 58.61x the stars (29,482 vs 503) |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 487 | 🔻 Superseded | 2.15x the stars (1,048 vs 487) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions | 476 | 🔻 Superseded | 2.26x the stars (1,078 vs 476) |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | self-hosting-security | 474 | 🔻 Superseded | 590.22x the stars (279,766 vs 474) |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | remote-control-isolation | 436 | 🔻 Superseded | 234.75x the stars (102,352 vs 436) |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | analytics | 428 | 🔻 Superseded | 11.14x the stars (4,768 vs 428) |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice-remote-control | 392 | 🔻 Superseded | 34.84x the stars (13,658 vs 392) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | self-hosting-security | 383 | 🔻 Superseded | 25.38x the stars (9,719 vs 383) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | remote-control-isolation | 381 | 🔻 Superseded | 220.18x the stars (83,890 vs 381) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | skills | 373 | 🔻 Superseded | 1.88x the stars (701 vs 373) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | self-hosting-security | 372 | 🔻 Superseded | 79.25x the stars (29,482 vs 372) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 359 | 🔻 Superseded | 2.38x the stars (854 vs 359) |
| **[spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** | self-hosting-security | 356 | 🔻 Superseded | 14.91x the stars (5,309 vs 356) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | remote-control-isolation | 347 | 🔻 Superseded | 96.67x the stars (33,545 vs 347) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 347 | 🔻 Superseded | 27.20x the stars (9,440 vs 347) |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | self-hosting-security | 337 | 🔻 Superseded | 87.48x the stars (29,482 vs 337) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 Superseded | 58.11x the stars (19,002 vs 327) |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | self-hosting-security | 319 | 🔻 Superseded | 877.01x the stars (279,766 vs 319) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 298 | 🔻 Superseded | 2.87x the stars (854 vs 298) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 283 | 🔻 Superseded | 3.02x the stars (854 vs 283) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | remote-control-isolation | 280 | 🔻 Superseded | 3.88x the stars (1,085 vs 280) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | remote-control-isolation | 274 | 🔻 Superseded | 122.43x the stars (33,545 vs 274) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 274 | 🔻 Superseded | 34.45x the stars (9,440 vs 274) |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | remote-control-isolation | 268 | 🔻 Superseded | 1.16x the stars (311 vs 268) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | sharing | 251 | 🔻 Superseded | 75.71x the stars (19,002 vs 251) |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | remote-control-isolation | 233 | 🔻 Superseded | 8.97x the stars (2,091 vs 233) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-15 09:12 UTC. 216 live tools · 128 candidates rejected by the quality gates.</sub>
