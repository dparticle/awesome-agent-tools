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

**226 tools** across **15 categories** · **44 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-08 11:25 UTC**

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

- [Skills](#skills) — 34 tools
- [Isolation & Parallelism](#isolation-parallelism) — 25 tools
- [Security & Self-hosting](#security-self-hosting) — 27 tools
- [Analytics](#analytics) — 22 tools
- [Self-hosting & Security](#self-hosting-security) — 18 tools
- [Teams](#teams) — 12 tools
- [Accounts](#accounts) — 14 tools
- [Mobile](#mobile) — 13 tools
- [Model Routing](#model-routing) — 12 tools
- [Quota](#quota) — 13 tools
- [Agent Runtime & Desktop UI](#agent-runtime-desktop-ui) — 12 tools
- [Remote Control](#remote-control) — 7 tools
- [Providers](#providers) — 7 tools
- [Analytics](#analytics) — 5 tools
- [Billing](#billing) — 5 tools
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
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natur… | 🟢 Turnkey · OOTB | ✅ | — | 149.8k (+253/d) | **90** |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | English \| 简体中文 \| 日本語 \| 한국어 \| Русский | 🟡 Some setup | — | — | 44.5k (+311/d) | **89** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟡 Some setup | — | — | 158.1k 🚀 +1340/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | An agent skill for crafting cinematic product videos: 157 shot recipe cards · 214 styles · 214 motion previews · a production-ready template | 🟢 Turnkey | — | ✅ | 10.8k 🚀 +135/d | **85** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 Easy | — | — | 26.8k (+122/d) | **85** |
| 🏆 **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** | A skill to stop your coding agent from burying the answer. ADHD-friendly output. | 🟢 Easy | — | — | 55.6k (+378/d) | **84** |
| 🏆 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. | 🟢 Turnkey · OOTB | ✅ | — | 5.8k 🚀 +117/d | **78** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 Easy | — | — | 9.5k 🚀 +79/d | **72** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 Turnkey · OOTB | ✅ | — | 7.6k (+34/d) | **70** |
| ✅ **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 Some setup | — | — | 7.3k 🚀 +83/d | **66** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workfl… | 🟡 Some setup | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1k | **57** |
| 🔹 **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | "A skill forgotten is a power lost." — The Code Architect Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ — AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and migration digest for 4.6→4.7… | 🟢 Easy | — | — | 812 | **57** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 Turnkey | — | — | 529 | **57** |
| 🔹 **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 Easy · OOTB | ✅ | — | 3.3k (+27/d) | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 Easy | — | — | 2.8k (+8/d) | **56** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 Easy · OOTB | ✅ | — | 889 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 Easy | — | — | 342 | **53** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). | 🟢 Easy | — | — | 755 🚀 +8/d | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. | 🟢 Turnkey | — | ✅ | 493 | **52** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code | 🟢 Easy | — | — | 298 | **52** |
| 🔹 **[zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills)** | 审稿意见回复（Rebuttal / Peer-review response） 引文管理：DOI → BibTeX，文献元数据提取，引文验证 | 🟡 Some setup | — | — | 4.6k (+32/d) | **51** |
| 🔹 **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | ~100 skills for Claude Code — meeting pipelines, research, image generation, TDD, publishing, personal analytics, and Claude Code ops. | 🟢 Easy | — | — | 389 | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 Easy | — | — | 1.1k | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 Easy | — | — | 440 | **48** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen cont… | 🟢 Easy | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 2.6k (+10/d) | **47** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | GRACE means Graph-RAG Anchored Code Engineering: a contract-first AI engineering methodology built around semantic markup, .grace XML artifacts, knowledge-graph navigation, assertions, scopes, and log-driven verificatio… | 🟡 Some setup | — | — | 252 | **44** |

**Also does this:** [anomalyco/opencode](https://github.com/anomalyco/opencode), [affaan-m/ECC](https://github.com/affaan-m/ECC), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [yc-software/qm](https://github.com/yc-software/qm), [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt), [pacifio/atlas](https://github.com/pacifio/atlas), [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code), [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) *(+34 more)*

*…and 4 more in [the full index](data/index.json).*

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

- Stars: **149,840** (~253.1/day lifetime average)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-08
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

- Stars: **44,463** (~310.9/day lifetime average)
- Health score: **89/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: Go
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **158,103** (~1339.9/day lifetime average)
- Health score: **86/100**
- Documentation score: **47/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

#### [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)

> An agent skill for crafting cinematic product videos: 157 shot recipe cards · 214 styles · 214 motion previews · a production-ready template

**Core problems it solves**

- **Skills & plugins**
- **Agent runtime** — *communities whose published principles (e.g.*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npx skills add Vincentwei1021/video-shotcraft`
- Platforms mentioned: macOS, Linux, Web
- Turnkey. install via npx one-liner; needs git clone (build from source); one-click setup

**Facts**

- Stars: **10,803** (~135.0/day lifetime average)
- Health score: **85/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex

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

- Stars: **26,834** (~122.0/day lifetime average)
- Health score: **85/100**
- Documentation score: **56/100**
- License: MIT
- Last push: 2026-09-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

</details>

## Isolation & Parallelism

*Parallel execution*

Tasks run one at a time and you wait; parallelism cuts wall-clock time.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. | 🟡 Some setup | — | — | 135.8k (+646/d) | **90** |
| 🏆 **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | English \| 中文 \| 日本語 \| Français \| Русский \| Português We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow | 🟡 Some setup | — | — | 83.5k (+161/d) | **90** |
| 🏆 **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same… | 🟢 Easy | — | — | 13.6k 🚀 +114/d | **85** |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; not… | 🟢 Easy | — | — | 27.3k (+98/d) | **85** |
| 🏆 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 Turnkey · OOTB | ✅ | — | 11.4k (+95/d) | **79** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app… | 🟢 Easy | — | — | 8.6k (+67/d) | **75** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | Disposable worktrees - each task runs in a clean treehouse git worktree, or an Orca-managed worktree when backend=orca, so parallel work on one repo never collides. Strict project boundary - the first mate is read-only… | 🟢 Easy | — | — | 7.7k 🚀 +65/d | **72** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Website · Documentation · 中文 | 🟢 Turnkey | — | — | 5.3k (+38/d) | **70** |
| ✅ **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | Editor & IDE integration (ACP). AI-native MCP configuration. | 🟡 Some setup | — | — | 7.8k (+56/d) | **69** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Basics（基础编辑型）：保留柱状图、折线图、环形图等熟悉轮廓，再用可数刻度、发丝线和编辑排版增加质感，适合结构简单或数据量较少的内容。 Glance（快速判断型）：用粗柱、大数字、色块和清晰排序提前聚合信息，让读者几秒内看懂高低、变化和异常，适合周报、汇报与 dashboard。 | 🟢 Turnkey · OOTB | ✅ | — | 6k 🚀 +71/d | **69** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 Turnkey · OOTB | ✅ | — | 9k (+25/d) | **68** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. | 🟢 Turnkey · OOTB | ✅ | — | 3.2k (+26/d) | **67** |
| ✅ **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. | 🟢 Turnkey | — | ✅ | 2.1k (+6/d) | **62** |
| 🔹 **[Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith)** | Keysmith 给本机的 AI 编程工具装指令：先预览，再写入，能验证，能撤走。 | 🟡 Some setup | — | — | 4.7k 🚀 +46/d | **61** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; A… | 🟢 Turnkey | — | — | 1.6k (+7/d) | **60** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. Go beyond code — video, slides, and more — the Commander drives open-source tools like HyperFrames and hands off to CLI agents — the coding agents Cla… | 🟡 Some setup | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. | 🟡 Some setup | — | — | 1k | **56** |
| 🔹 **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | Claude Code, Codex, OpenCode, Grok, Gemini CLI, Antigravity CLI, Pi, Command Code, Hermes Agent, Muse Code, and Oh My Pi run side by side. | 🟢 Turnkey · OOTB | ✅ | — | 577 🚀 +7/d | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in… | 🟢 Easy | — | ✅ | 519 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. | 🟢 Turnkey | — | — | 307 | **55** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an… | 🟡 Some setup | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | The structured skill framework for Claude Code: 131 professional skills for deployment, security, databases, content, marketing, and more. | 🟢 Easy | — | — | 423 | **52** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Run every AI coding agent in its own git worktree, in parallel. The desktop app embeds its server on 127.0.0.1 with a per-launch token; nothing is exposed to the network. | 🟢 Turnkey | — | ✅ | 267 | **47** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | A macOS desktop app for running multiple AI agents in parallel. Run separate agent sessions side-by-side, each in its own workspace with an isolated git worktree | 🟢 Easy | — | ✅ | 216 | **38** |

**Also does this:** [getpaseo/paseo](https://github.com/getpaseo/paseo), [crshdn/mission-control](https://github.com/crshdn/mission-control), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli), [yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun), [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit), [JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude), [newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [garrytan/gstack](https://github.com/garrytan/gstack)

> When I heard Karpathy say this, I wanted to find out how.

**Core problems it solves**

- **Automatic failover** — *and /diagram always use gstack's bundled browser.*
- **Multi-agent orchestration** — *the cause and re-verify before committing.*
- **Parallel execution** — *etext patterns depending on whether it's a landing page, dashboard, form, or card layout.*
- **Workspace isolation** — *hand, and gstack-uninstall*
- **Model / provider routing** — *deterministic aside repl scripts.*
- **Usage analytics** — *try flows through validated edge functions that enforce schema checks, event type allowlists, and field length limits.*
- **Session persistence** — *Browse my kid's school parent portal and add all the other parents' names, phone numbers, and photos to my Google Contacts." Two ways to get authenti…*
- **Memory & context** — *Come work at YC — ycombinator.com/software*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Some setup. install via native installer / package; needs git clone (build from source), go build; configure API key configuration, config file; one-click setup

**Facts**

- Stars: **135,765** (~646.5/day lifetime average)
- Health score: **90/100**
- Documentation score: **81/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [bytedance/deer-flow](https://github.com/bytedance/deer-flow)

> English | 中文 | 日本語 | Français | Русский | Português

**Core problems it solves**

- **Automatic failover** — *d X-Forwarded-Proto: https) or localhost HTTP.*
- **Multi-agent orchestration** — *llion to our incredible community — you made this happen! 💪🔥*
- **Parallel execution** — *x plus Docker is the recommended deployment target for a persistent server.*
- **Workspace isolation** — *ame matches the payload's type field.*
- **Model / provider routing** — *u configure an optional web search provider, or skip it for now.*
- **API gateway / proxy** — *Optional per-model requestadmission paces requests to help stay within provider request-per-minute limits. It is disabled by default; see the linked…*
- **Usage analytics** — *ent cards show the effective model and, when the provider returns usage metadata, a cumulative token total that updates after each completed sub-agen…*
- **Session persistence** — *es to DeerFlow and get streaming responses*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install --global @minimax-ai/code`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, native installer / package; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **83,504** (~160.9/day lifetime average)
- Health score: **90/100**
- Documentation score: **80/100**
- License: MIT
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Cursor, Droid

#### [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)

> MiMoCode is a terminal-native AI coding assistant.

**Core problems it solves**

- **Multi-agent orchestration** — *emory (MEMORY.md) — persistent project knowledge, rules, and architecture decisions*
- **Parallel execution** — *terminal-native intelligence to desktop workflows.*
- **Workspace isolation**
- **Model / provider routing** — *o/Plus) — OpenAI OAuth login*
- **API gateway / proxy** — *separates the provider ID from the model ID.*
- **Session persistence** — *omatically by the checkpoint-writer subagent*
- **Memory & context** — *e: Where Models and Agents Co-Evolve*
- **Skills & plugins** — *ble/Sol-class), which internalize most of the workflow and work best from one compact contract.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 30/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://mimo.xiaomi.com/install | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, curl | sh installer; needs npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **13,612** (~114.4/day lifetime average)
- Health score: **85/100**
- Documentation score: **63/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-03
- Works with: Claude Code, Codex, OpenCode, Cursor, Cline / Roo

#### [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

> Persistent file-based planning for AI coding agents and long-running tasks.

**Core problems it solves**

- **Multi-agent orchestration** — *plugins for Claude Code, Codex CLI, Pi, Hermes Agent, OpenCode and DeepSeek Harness.*
- **Parallel execution** — *ry mechanism below is a file on disk plus a hook, so it works the same on hour ten as on turn one.*
- **Workspace isolation** — *** One orchestrator owns taskplan.md and the shared summaries; every worker appends to its own ledger or assigned file.*
- **Memory & context**
- **Skills & plugins** — *ackage, wired up for you (skill, extension, status bar):*
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

- Stars: **27,330** (~98.3/day lifetime average)
- Health score: **85/100**
- Documentation score: **73/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)

> npx @cobusgreyling/loop init .

**Core problems it solves**

- **Cross-agent support** — *Mentions Claude Code, Codex, OpenCode*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 16/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npx @cobusgreyling/loop init . --pattern daily-triage --tool claude`
- Turnkey. install via npx one-liner

**Facts**

- Stars: **11,442** (~94.6/day lifetime average)
- Health score: **79/100**
- Documentation score: **36/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode

</details>

## Security & Self-hosting

*Automatic failover*

When one account or provider dies, work should continue on the next one instead of stopping.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 Turnkey | — | — | 27.3k 🚀 +321/d | **88** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi | 🟢 Turnkey · OOTB | ✅ | ✅ | 13.3k 🚀 +230/d | **87** |
| 🏆 **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. | 🟢 Easy | — | — | 13.7k 🚀 +188/d | **84** |
| 🏆 **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | When an AI agent (Claude Code, Codex, Cursor, OpenCode, or another compatible client) encounters an APK, a binary, frontend JS encryption, a CTF challenge, or a pentesting target, this package routes it to the right met… | 🟡 Some setup | — | — | 40.2k (+273/d) | **83** |
| 🏆 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | This one is invisible to anti-bots. | 🟢 Turnkey · OOTB | ✅ | — | 2.7k 🚀 +331/d | **80** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Respect limits and access decisions. Unsigned beta: Windows is not publisher-signed; macOS is unsigned and unnotarized. | 🟢 Easy · OOTB | ✅ | — | 4.2k 🚀 +92/d | **75** |
| ✅ **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | Open-source SEO + GEO skills for Claude on a free SEO MCP server (the Ryze connector) — keyword research, rank tracking, site audits, backlinks, competitor gaps, AI visibility — running on your own Search Console, Analy… | 🟡 Some setup | — | — | 4.6k 🚀 +117/d | **74** |
| ✅ **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | module outlines: 7 of 12 modules with 3+ nodes in view (cap 12; 3 dropped as too thin to read as a region; 2 dropped as enclosing mostly other modules) — three separate truncations, each wi… PageRank is a bad co-change… | 🟢 Easy | — | — | 2.4k 🚀 +35/d | **66** |
| ✅ **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | An agent that closes its session forgets everything it learned in it. | 🔴 Involved | — | — | 2.6k 🚀 +74/d | **66** |
| ✅ **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. | 🟡 Some setup | — | — | 4k 🚀 +44/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k (+11/d) | **63** |
| ✅ **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Subagents get sharper context. context-loader, review-prep, brag-spotter, and friends consult QMD first, then fall back to grep. James Bedford — Vault structure philosophy, separation of AI-generated content | 🟡 Some setup | — | — | 4.9k (+22/d) | **63** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 Easy | — | — | 382 | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 454 | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Dedup - four layers: exact text match -> cosine >= 0.92 auto-merge -> cosine 0.80-0.92 borderline (LLM verify later) -> manual review in the dashboard. Your data, in the open. | 🟢 Easy | — | — | 281 | **54** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custom fields, and workspaces — with built-in rate limiting, type safety, a… | 🟢 Easy | — | — | 445 | **52** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | Open AI agents and connect your client. The runner opens an outbound TLS WebSocket and exposes no inbound listener. | 🟢 Easy | — | — | 337 | **52** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Evolve — evolutionary program search with a mandatory budget and zero-call resume. | 🟢 Easy · OOTB | ✅ | — | 687 (+5/d) | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at… | 🟢 Turnkey · OOTB | ✅ | — | 677 | **51** |
| 🔹 **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | Maestro is a multi-agent development orchestration platform with 39 specialists, an Express path for simple work, a 4-phase standard workflow for medium and complex work, persistent session state, and standalone review/… | 🟡 Some setup | — | — | 465 | **50** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support. | 🟡 Some setup | — | — | 474 | **49** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Enable your AI agents to read, analyze, and modify Figma designs. Get document information, current selection, styles | 🟢 Turnkey · OOTB | ✅ | — | 667 | **48** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | This repository is essentially an LLM chat desktop application based on MCP. Windows: The MCP SDK includes a workaround specifically for Windows systems, as documented in ISSUE 101. | 🟢 Easy | — | ✅ | 1.2k | **47** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. | 🟡 Some setup | — | — | 410 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | This repository is YALC 1.0, the first generation and the open-source one. Rate limiting — DB-backed token bucket on all external sends | 🔴 Involved | — | — | 317 | **46** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace gives LLM agents a persistent, searchable, and auditable memory store, so each conversation can build on the last instead of starting from scratch. | 🟡 Some setup | — | — | 313 | **44** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [garrytan/gstack](https://github.com/garrytan/gstack), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [google/artemis](https://github.com/google/artemis), [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [superdesigndev/treg](https://github.com/superdesigndev/treg), [tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness) *(+39 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **27,273** (~320.9/day lifetime average)
- Health score: **88/100**
- Documentation score: **60/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-09-29
- Works with: Codex, OpenCode

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

- Stars: **13,327** (~229.8/day lifetime average)
- Health score: **87/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-08

#### [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)

> Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota.

**Core problems it solves**

- **Multi-agent orchestration** — *veloper mode and MCP apps.*
- **MCP support** — *thout spending your Work or Codex quota.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 19/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source); configure API key configuration, sign-in required

**Facts**

- Stars: **13,729** (~188.1/day lifetime average)
- Health score: **84/100**
- Documentation score: **45/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Codex

#### [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)

> When an AI agent (Claude Code, Codex, Cursor, OpenCode, or another compatible client) encounters an APK, a binary, frontend JS encryption, a CTF challenge, or a pentesting target, this package routes it to the right methodology, checks ava…

**Core problems it solves**

- **Multi-agent orchestration** — *re / request replay anything-analyzer, Reqable MCP + js-reverse/*
- **Skills & plugins** — *skills/scripts/extract-summaries.ps1 Regenerates INDEX.md from skill frontmatter*
- **MCP support** — *matrix: skills/routing.md · Ops: skills/ops/*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, OpenCode*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Some setup. needs git clone (build from source)

**Facts**

- Stars: **40,183** (~273.4/day lifetime average)
- Health score: **83/100**
- Documentation score: **53/100**
- License: MIT
- Language: PowerShell
- Last push: 2026-09-22
- Works with: Claude Code, Codex, OpenCode, Cursor

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

- Stars: **2,651** (~331.4/day lifetime average)
- Health score: **80/100**
- Documentation score: **33/100**
- License: MIT
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI

</details>

## Analytics

*Session persistence*

Closing the laptop or losing connection kills a long-running agent session.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 Easy | — | — | 7.3k 🚀 +93/d | **74** |
| ✅ **[pacifio/atlas](https://github.com/pacifio/atlas)** | Switching agents loses the thread. Nothing is locked in. | 🟢 Easy | — | — | 9.4k (+64/d) | **73** |
| ✅ **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。 | 🟡 Some setup | — | — | 12.4k (+93/d) | **72** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Do… | 🟡 Some setup | — | — | 31.6k (+28/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | Your AI coding agent forgets everything when the session ends. | 🟢 Easy | — | — | 7.1k (+30/d) | **65** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.3k 🚀 +22/d | **58** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Conversations with AI agents reset when context windows close. Agent Action Grammar (AAG): Ultra-compact, deterministic ASCII micro-syntax saving ~78–85% tokens compared to natural language prompt instructions. | 🟡 Some setup | — | — | 756 🚀 +24/d | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | Decomposed retrieval evaluation: ARES (NAACL 2024), RAGChecker (2024) Memory and knowledge-base poisoning: AgentPoison (NeurIPS 2024), PoisonedRAG (USENIX Security 2025) | 🟢 Easy · OOTB | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Both HTTP and STDIO expose 16 tools: 8 core memory/logging/notebook/compaction tools, 6 bundled code-graph tools, and… | 🟡 Some setup | — | — | 418 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. | 🟢 Easy | — | — | 416 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 设置 API Token（点 Generate 自动生成） | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy,… | 🔴 Involved | — | — | 836 | **52** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Plugin-first long-term memory for every agent platform. Corrections that stick. | 🟢 Easy | — | ✅ | 547 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 Some setup | — | — | 427 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity… | 🔴 Involved | — | — | 612 | **51** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. | 🟢 Easy | — | — | 430 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Intelligent LLM Routing (omega-pro) — Classifies tasks and routes to the optimal model. Secure Profile (omega-pro) — AES-256 encrypted personal data storage with macOS Keychain integration. | 🟡 Some setup | — | — | 220 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | LycheeMemory is a compact memory framework for LLM agents. GET /mcp exposes the SSE stream used by some MCP clients | 🟡 Some setup | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 Involved | — | — | 473 | **49** |
| 🔹 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. | 🔴 Involved | — | — | 514 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. | 🟢 Easy | — | — | 247 | **46** |

**Also does this:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli), [garrytan/gstack](https://github.com/garrytan/gstack), [bytedance/deer-flow](https://github.com/bytedance/deer-flow), [paperclipai/paperclip](https://github.com/paperclipai/paperclip), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [spinabot/brigade](https://github.com/spinabot/brigade), [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin), [hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor), [LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth), [pax-beehive/paxm](https://github.com/pax-beehive/paxm), [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **7,348** (~93.0/day lifetime average)
- Health score: **74/100**
- Documentation score: **42/100**
- License: MIT
- Language: Python
- Last push: 2026-09-20
- Works with: Codex

#### [pacifio/atlas](https://github.com/pacifio/atlas)

> Source control for coding agents.

**Core problems it solves**

- **Multi-agent orchestration** — *cupy the context window for the rest of the session.*
- **Usage analytics**
- **Session persistence** — *gent session produced which commit), which is SQLite in the project's gitignored .atlas/, because it is queried, not read.*
- **Memory & context** — *ts, tool calls, and reasoning.*
- **Agent runtime**
- **GUI / desktop app** — *. Code, notes, and sessions stay on your machine. Sign in and create an organization when you want to sync across a team.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor, Kilo Code*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source); configure sign-in required, database dependency; GUI application

**Facts**

- Stars: **9,359** (~64.1/day lifetime average)
- Health score: **73/100**
- Documentation score: **50/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor

#### [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)

> Ian Xiaohei Illustrations 是一个 Codex Skill，用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。

**Core problems it solves**

- **Memory & context**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Some setup. needs git clone (build from source)

**Facts**

- Stars: **12,411** (~93.3/day lifetime average)
- Health score: **72/100**
- Documentation score: **40/100**
- License: MIT
- Last push: 2026-09-24
- Works with: Claude Code, Codex

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

- Stars: **31,620** (~27.5/day lifetime average)
- Health score: **69/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)

> Your AI coding agent forgets everything when the session ends.

**Core problems it solves**

- **Session persistence** — *ns, discoveries, accomplished work, next steps, and relevant files.*
- **Memory & context** — *ehavior, manual MCP setup, compaction resilience, and troubleshooting: Agent Setup → · Pi users can also find the package at gentle-engram.*
- **Agent runtime**
- **MCP support** — *any MCP-compatible agent · per-agent setup →*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 28/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install gentleman-programming/tap/engram`
- Platforms mentioned: Windows, Linux, Web
- Easy. install via Homebrew install; configure environment variables, database dependency

**Facts**

- Stars: **7,087** (~30.4/day lifetime average)
- Health score: **65/100**
- Documentation score: **57/100**
- License: MIT
- Language: Go
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Self-hosting & Security

*Self-hostable*

You do not want your code or keys flowing through someone else's server.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot uses .github/copilot-instructions.md instead) Available in release 2.2: guided package setup for Claud… | 🟡 Some setup | — | — | 275.2k (+1046/d) | **89** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 8.9k 🚀 +129/d | **85** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. Routines: ask a Bot to do something on a schedule and it does, running as y… | 🟡 Some setup | — | — | 6.2k 🚀 +119/d | **83** |
| 🏆 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 Some setup | — | — | 11.3k 🚀 +103/d | **80** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | The API — everything the CLI does is plain HTTP; interactive OpenAPI docs live at /docs. CLI — a vendor binary (stripe, gh, vercel, ...) run with the credential injected. | 🟢 Easy | — | — | 4.8k 🚀 +57/d | **73** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. | 🟢 Easy | — | — | 57.6k (+21/d) | **70** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi is a fast, self-contained terminal AI coding agent. | 🟢 Easy | — | — | 3.4k 🚀 +52/d | **67** |
| ✅ **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | English \| 简体中文 \| 繁體中文 \| 日本語 \| 한국어 \| Русский \| Français \| Español Deployment options for local Docker or Node.js with SQLite or PostgreSQL state and local or | 🔴 Involved | — | — | 6k 🚀 +59/d | **66** |
| 🔹 **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | ╔═════════════════════════════════════════════════════════════════════════════╗ ║ MARKETING NOTES FOR IMAGE ASSETS ║ ║ All images below live under .github/assets/. | 🟡 Some setup | — | — | 2.1k (+13/d) | **61** |
| 🔹 **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file… | 🔴 Involved | — | — | 3.7k (+26/d) | **59** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.7k 🚀 +26/d | **59** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.7k (+10/d) | **57** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. Sequential Learning Benchmark. | 🟡 Some setup | — | — | 773 | **56** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | PAXM carries decisions, conventions, and working context into later Codex, Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP sessions. | 🟡 Some setup | — | — | 422 🚀 +5/d | **49** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | The self-hosted AI backend for private data and tool-using agents. | 🟡 Some setup | — | — | 353 | **49** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models SHA-256 hash-chained — each trace commits to the previous, tamper-evident | 🟡 Some setup | — | — | 507 | **47** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? | 🟡 Some setup | — | — | 436 | **47** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 Some setup | — | — | 535 | **40** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [yetone/cumora](https://github.com/yetone/cumora), [KunAgent/Kun](https://github.com/KunAgent/Kun), [crshdn/mission-control](https://github.com/crshdn/mission-control), [Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory), [cordum-io/cordum](https://github.com/cordum-io/cordum), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy) *(+5 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [affaan-m/ECC](https://github.com/affaan-m/ECC)

> Use the guided setup or native plugin commands.

**Core problems it solves**

- **Multi-agent orchestration** — *s and evidence live under docs/releases/.*
- **Parallel execution**
- **Workspace isolation**
- **Model / provider routing** — *shims such as /tdd and /eval live in legacy-command-shims/ for explicit opt-in only.*
- **API gateway / proxy** — *eway remaps model names, configure that in Claude Code rather than in ECC.*
- **Memory & context** — *r debugging, before continuing feature work*
- **Skills & plugins** — *tokens use macOS Keychain by default; explicit file fallback must retain owner-only directory/file permissions.*
- **Agent runtime** — *te ECC, change scope, or change its hook profile.*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx ecc-universal@2.2.3 setup`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, bunx one-liner; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **275,209** (~1046.4/day lifetime average)
- Health score: **89/100**
- Documentation score: **73/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)

> Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats.

**Core problems it solves**

- **Parallel execution**
- **Model / provider routing** — *n in with Genspark and skip keys, or bring your own*
- **API gateway / proxy** — *n in with Genspark and skip keys, or bring your own*
- **Billing & metering** — *export as PDF or a native editable Word document.*
- **Usage analytics** — *ub Copilot, OpenCode and Windsurf*
- **Skills & plugins** — *Grok, Mistral, OpenRouter, Requesty, Opper, Cheaper Inference, or any OpenAI-compatible endpoint, local*
- **Agent runtime** — *hing that overflows or overlaps before genoffice create assembles the .pptx and slides render hands back a PNG per slide to look at.*
- **MCP support** — *Brasil) · Deutsch · Français · 简体中文 · 繁體中文 · 한국어 · 日本語 · العربية · Русский · Italiano · Nederlands · Polski · Čeština · Bahasa Indonesia · Bahasa Mel…*

**Getting it running**

- Setup: 🟢 **Easy** (friction 20/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -T report.docx -H "Authorization: Bearer $GENOFFICE_MCP_TOKEN" http://server:3093/files/`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, native installer / package; needs npm install/build; configure API key configuration, sign-in required; one-click setup

**Facts**

- Stars: **8,923** (~129.3/day lifetime average)
- Health score: **85/100**
- Documentation score: **58/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)

> The AI assistant your company can actually own.

**Core problems it solves**

- **Automatic failover** — *somewhere else: a gateway, a proxy.*
- **Mobile access**
- **Model / provider routing** — *verything is on 3001 here, the app included, rather than the 3010 the clone uses.*
- **Session persistence**
- **MCP support** — *rouping customer feedback into themes it can cite.*
- **Security & isolation** — *who gets in**: /admin/people lists everybody who has signed in, promotes and demotes them, and removes access, which ends the session they are using…*
- **Self-hostable** — *untime key, creates or reuses its*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 49/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx --yes copilotkit@latest login`
- Platforms mentioned: macOS, Linux, Web
- Some setup. install via npx one-liner; needs docker run; configure sign-in required, database dependency

**Facts**

- Stars: **6,198** (~119.2/day lifetime average)
- Health score: **83/100**
- Documentation score: **73/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08

#### [spinabot/brigade](https://github.com/spinabot/brigade)

> 🔐 No tokens to juggle.

**Core problems it solves**

- **Multi-account switching**
- **Remote control**
- **Multi-agent orchestration** — *privileged tools are owner-gated*
- **Workspace isolation** — *nnect, walk away, reconnect*
- **Model / provider routing** — *telligence, built on enterprise-grade tech: a crew of*
- **API gateway / proxy** — *o an org chart that governs who can talk to whom.*
- **Billing & metering**
- **Session persistence** — *ns (with IANA timezones and*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 39/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://brigade.spinabot.com/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via curl | sh installer, PowerShell irm | iex installer; needs git clone (build from source), npm install/build; configure API key configuration, config file; GUI application

**Facts**

- Stars: **11,292** (~102.7/day lifetime average)
- Health score: **80/100**
- Documentation score: **62/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-03
- Works with: Claude Code, Codex, Copilot, Droid

#### [superdesigndev/treg](https://github.com/superdesigndev/treg)

> OpenRouter, but for agent tools instead of models.

**Core problems it solves**

- **Automatic failover** — *(secrets won't survive a restart)*
- **Model / provider routing** — *# Treg (OpenRouter for Tools)*
- **Billing & metering** — *e the code to third parties as a competing hosted/managed registry service without written*
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

- Stars: **4,783** (~56.9/day lifetime average)
- Health score: **73/100**
- Documentation score: **71/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code

</details>

## Teams

*Team collaboration*

Several people must share one agent setup, with roles and boundaries.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. | 🟢 Turnkey | — | — | 158.4k (+441/d) | **98** |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine | 🟢 Easy | — | — | 29.2k (+130/d) | **88** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 Easy | — | — | 7.9k 🚀 +87/d | **81** |
| 🏆 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 Involved | — | — | 15.4k 🚀 +219/d | **79** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Your coding agent already has a memory feature. | 🔴 Involved | — | — | 9k (+65/d) | **70** |
| ✅ **[yetone/cumora](https://github.com/yetone/cumora)** | Where agent teams gather. Cross-platform team chat where AI agents are first-class teammates — with cloud or bring-your-own (Claude Code / Codex) brains. | 🟢 Easy | — | — | 3.9k 🚀 +76/d | **69** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. | 🟢 Turnkey · OOTB | ✅ | ✅ | 4.4k (+32/d) | **68** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that consults multiple AI coding agents in parallel and shows you their answers side-by-side. | 🟡 Some setup | — | — | 850 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 406 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Hots are tater-tots now. v1.1.7 called them hots. The first time a newer veil runs while you are logged in Windows. The first time veil binds a port, Windows Defender Firewall pops up *"Allow this app | 🟢 Easy | — | — | 215 | **54** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.1k (+9/d) | **49** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. | 🟢 Easy | — | — | 300 | **49** |

**Also does this:** [nexu-io/open-design](https://github.com/nexu-io/open-design), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [loopx-project/loopx](https://github.com/loopx-project/loopx), [wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection), [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

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

- Stars: **158,431** (~441.3/day lifetime average)
- Health score: **98/100**
- Documentation score: **86/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> Your coding agent remembers everything.

**Core problems it solves**

- **Automatic failover** — *y, paste the block inside { "mcpServers": { ...*
- **Multi-agent orchestration** — *ep / vector / agentmemory adapters score side-by-side, NDJSON output, published scorecards land in docs/benchmarks/.*
- **Model / provider routing** — *inference is on-device afterward.*
- **API gateway / proxy**
- **Billing & metering**
- **Memory & context** — *By default, agentmemory stores iii-engine state outside the repository you start it from: ~/Library/Application Support/agentmemory on macOS, $XDGDAT…*
- **Skills & plugins** — *agentmemory ships 17 skills in the Claude-Code-style /SKILL.md format: 9 invocable action skills (remember, recall, recap, handoff, forget, lesson, c…*
- **Agent runtime** — *Your coding agent remembers everything.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npx -y @agentmemory/agentmemory@latest`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; no code needed

**Facts**

- Stars: **29,236** (~129.9/day lifetime average)
- Health score: **88/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [TencentCloud/Octop](https://github.com/TencentCloud/Octop)

> Octop is an open-source, self-hosted AI assistant.

**Core problems it solves**

- **Automatic failover** — *h OCTOPDEFAULTPASSWORD unset a strong random password is generated; a password you set must be ≥8 characters with letters and digits (weak/common pas…*
- **Mobile access** — *Linux alongside the web dashboard and IM channels.*
- **Multi-agent orchestration** — *A smarter, self-hosted AI assistant — multi-user, multi-agent.*
- **Parallel execution**
- **Workspace isolation** — *dows scripts\install.bat or install.ps1*
- **Model / provider routing** — *ild / quality** hatchling · ruff · mypy · pytest*
- **API gateway / proxy** — *ays back up first (octop backup) before a cross-version upgrade.*
- **Billing & metering** — *Docker Any docker/docker-compose.yml*

**Getting it running**

- Setup: 🟢 **Easy** (friction 26/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via npx one-liner, pip install; needs docker run, make build; configure config.json/yaml/toml, OAuth login flow; one-click setup

**Facts**

- Stars: **7,918** (~87.0/day lifetime average)
- Health score: **81/100**
- Documentation score: **78/100**
- License: MIT
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode

#### [yc-software/qm](https://github.com/yc-software/qm)

> A multiplayer agent harness for work.

**Core problems it solves**

- **Workspace isolation**
- **Model / provider routing** — *- Work in an existing repository: run tests, open PRs, monitor CI, check system logs*
- **Session persistence**
- **Skills & plugins**
- **Agent runtime** — *store, sandbox, memory) sits behind an interface.*
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

- Stars: **15,362** (~219.5/day lifetime average)
- Health score: **79/100**
- Documentation score: **49/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode

#### [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

> Your coding agent already has a memory feature.

**Core problems it solves**

- **Workspace isolation** — *box/queue plus the on-start "you have mail" notice.*
- **Model / provider routing**
- **API gateway / proxy**
- **Memory & context** — *> Long-term memory for AI coding agents.*
- **Agent runtime** — *> Long-term memory for AI coding agents.*
- **MCP support** — *unchd-without-the-app paths:*
- **Security & isolation** — *t one server and what one*
- **Team collaboration** — *here reachable — a homelab box, a LAN host — and*

**Getting it running**

- Setup: 🔴 **Involved** (friction 64/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL "$wrapper_base" -o "$wrapper_tmp/ai-memory-wrapper"`
- Platforms mentioned: macOS, Windows, Linux, Web
- Involved setup. install via native installer / package; needs docker run, git clone (build from source); configure config.json/yaml/toml, OAuth login flow

**Facts**

- Stars: **9,018** (~64.9/day lifetime average)
- Health score: **70/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Accounts

*Multi-account switching*

One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 Turnkey | — | ✅ | 128.3k (+236/d) | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | On your network. Turn on Share on local network and give each client a named gateway key, each with its own daily, weekly or monthly token and cost limit. Docker. Run ghcr.io/yetone/magpie on a server or a NAS and manag… | 🟢 Turnkey | — | ✅ | 6.5k 🚀 +468/d | **86** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://a… | 🟡 Some setup | — | — | 43.5k (+148/d) | **85** |
| 🏆 **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 28 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 Some setup | — | — | 17.1k 🚀 +154/d | **83** |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 Involved | — | — | 30.5k (+110/d) | **81** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth，以及 Grok apply_patch 协议兼容方向，以及账号池错误分类与状态恢复边界… Grok CLI 凭据不加密：access token/… | 🟢 Easy | — | — | 18.7k (+71/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. | 🟢 Easy | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持 gpt-image-2、codex-gpt-image-2、auto、gpt-5、gpt-5-1、gpt-5-2、gpt-5-3、gpt-5-3-mini、gpt-5-mini 模型选择 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 Involved | — | — | 6.6k (+38/d) | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. | 🟡 Some setup | — | ✅ | 535 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. | 🟢 Easy | — | — | 279 | **52** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 多站点多账号：每个站点可添加多个账号，每个账号可持有多个 API Token | 🔴 Involved | — | — | 3.3k (+15/d) | **51** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota | 🟢 Easy | — | ✅ | 882 | **51** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 为 Sub2API 增加 账号级 STATE 票据管理，尝试应对最近 ChatGPT / Codex 账号的模型降质和降并发：请求的模型被路由到其他模型，或 OpenAI 上游限制账号可同时处理的请求数量。 | 🟡 Some setup | — | — | 214 🚀 +11/d | **48** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 241 | **42** |

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

- Stars: **128,342** (~236.4/day lifetime average)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-08
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi.

**Core problems it solves**

- **Multi-account switching**
- **Quota & usage management**
- **Model / provider routing** — *e · Pencil · T3 Code · OpenHanako · AtomCode · Alma · Cindy*
- **API gateway / proxy** — *anfan · Tencent Cloud · Huawei Cloud MaaS · Volcengine Ark · Mistral · Groq · xAI · OpenRouter · Together · Fireworks · SiliconFlow · NVIDIA NIM · Mo…*
- **MCP support** — *ind it, so magpie offers it as a provider.*
- **GUI / desktop app** — *n also have its own short list of models, so its picker shows only what you want there.*
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 12/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://usemagpie.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via go install, curl | sh installer; configure config file, sign-in required; one-click setup

**Facts**

- Stars: **6,548** (~467.7/day lifetime average)
- Health score: **86/100**
- Documentation score: **57/100**
- License: MIT
- Language: Go
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

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

- Stars: **43,477** (~147.9/day lifetime average)
- Health score: **85/100**
- Documentation score: **61/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

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

- Stars: **17,103** (~154.1/day lifetime average)
- Health score: **83/100**
- Documentation score: **53/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
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

- Stars: **30,453** (~110.3/day lifetime average)
- Health score: **81/100**
- Documentation score: **66/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Mobile

*Mobile access*

You are away from the desk and want to keep the agent working from a phone.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 87.6k (+427/d) | **92** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. | 🟡 Some setup | — | — | 11.1k 🚀 +202/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. | 🟢 Easy | — | — | 4.1k 🚀 +414/d | **83** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is an open source agentic development environment for desktop, mobile, web, and CLI. | 🟢 Easy | — | ✅ | 20.1k (+56/d) | **74** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 Easy · OOTB | ✅ | ✅ | 24.1k (+54/d) | **71** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. | 🟢 Turnkey · OOTB | ✅ | — | 4.3k (+35/d) | **67** |
| ✅ **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 一个适配 Claude Code / Codex 等 Agent 环境的图文卡片技能,用于从文章、文案、截图、产品笔记、字幕、照片或用户视频生成小红书 / Rednote 图文组图、Live Photo 动态卡与公众号 21:9 + 1:1 封面对。 | 🟢 Easy | — | — | 7.4k (+56/d) | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 Some setup | — | — | 3.3k 🚀 +37/d | **60** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | A professional dashboard to track and visualize Claude Code, Cursor, and Codex agent sessions, tool usage, conversation history, cost, and subagent orchestration in real time. | 🟡 Some setup | — | — | 1.1k | **55** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from y… | 🟢 Easy · OOTB | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). | 🟡 Some setup | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | An advanced Distributed Automation Platform for high-concurrency account registration and full-lifecycle inventory management. | 🟡 Some setup | — | — | 1.4k (+7/d) | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 Easy | — | — | 547 🚀 +5/d | **51** |

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
- **Parallel execution**
- **Workspace isolation** — *agent finishes and send follow-ups from anywhere.*
- **Usage analytics**

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `brew install --cask stablyai/orca/orca`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android
- Turnkey. install via Homebrew install, native installer / package; GUI application

**Facts**

- Stars: **87,556** (~427.1/day lifetime average)
- Health score: **92/100**
- Documentation score: **51/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

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

- Stars: **11,137** (~202.5/day lifetime average)
- Health score: **83/100**
- Documentation score: **68/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)

> A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions.

**Core problems it solves**

- **Automatic failover** — *e permission requests show up with Allow / Deny / Always; AskUserQuestion prompts show the choices right in the notch (single or multi-select, up to…*
- **Remote control**
- **Mobile access** — *your macOS Keychain, Windows Credential Manager or Linux Secret Service (GNOME Keyring, KWallet).*
- **Model / provider routing** — *p to the right terminal — open the exact terminal window of a session (macOS).*
- **Agent runtime**
- **Security & isolation** — *See what Claude is editing, live in the notch: each file modification shows the file name and +N −M counts in the ticker, tap to read the full diff*
- **GUI / desktop app** — *ting from 0.1.0? macOS may ask you, once for each key you saved, to let Coucou use it: enter your Mac password and click Always Allow.*
- **Notifications** — *your iPhone's Lock Screen and Dynamic Island with the agent's state, then comes back to the notch when you unlock.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 23/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew install xcodegen`
- Platforms mentioned: macOS, Windows, Linux, iOS
- Easy. install via Homebrew install, native installer / package; needs git clone (build from source), npm install/build; configure API key configuration, database dependency; one-click setup

**Facts**

- Stars: **4,138** (~413.8/day lifetime average)
- Health score: **83/100**
- Documentation score: **60/100**
- License: MIT
- Language: Swift
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **20,097** (~56.0/day lifetime average)
- Health score: **74/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

#### [slopus/happy](https://github.com/slopus/happy)

> Multi-provider within one session.

**Core problems it solves**

- **Remote control** — *lopus/slopus.github.io The website and docs at happy.engineering*
- **Mobile access** — *Happy adds a harness, not another bill.*
- **Multi-agent orchestration**
- **Model / provider routing** — *.com/user-attachments/assets/b3580704-f9e0-441e-80be-3f83f6a08ab5*
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

- Stars: **24,053** (~53.8/day lifetime average)
- Health score: **71/100**
- Documentation score: **29/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex
- *Why it is seeded: Drive Claude Code / Codex from a phone with end-to-end encryption.*

</details>

## Model Routing

*Model / provider routing*

You want one agent to run on a different model or provider than its default.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 🤖 Agent-native, model-agnostic. Hand off to engineering. | 🟢 Easy | — | — | 100k (+613/d) | **95** |
| 🏆 **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. | 🟡 Some setup | — | — | 17k 🚀 +159/d | **83** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. | 🟡 Some setup | — | — | 11k 🚀 +128/d | **81** |
| 🏆 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 Some setup | — | — | 9.3k 🚀 +105/d | **80** |
| ✅ **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 Some setup | — | — | 7.5k 🚀 +357/d | **75** |
| ✅ **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens. | 🟢 Easy · OOTB | ✅ | — | 7.5k (+54/d) | **71** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. | 🟢 Easy | — | — | 1.7k (+13/d) | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 Turnkey · OOTB | ✅ | — | 343 | **53** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CR… | 🟡 Some setup | — | — | 371 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 Involved | — | — | 707 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code is an AI coding workspace for work that lasts longer than one prompt. | 🟡 Some setup | — | — | 436 | **50** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 Easy | — | — | 367 | **47** |

**Also does this:** [yetone/magpie](https://github.com/yetone/magpie), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [decolua/9router](https://github.com/decolua/9router), [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven), [yetone/cumora](https://github.com/yetone/cumora), [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness), [aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code), [LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem), [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy) *(+4 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [nexu-io/open-design](https://github.com/nexu-io/open-design)

> OpenDesign is a collaborative design agent workspace.

**Core problems it solves**

- **Mobile access** — *read your DESIGN.md and render in a sandboxed iframe.*
- **Model / provider routing** — *No CLI installed? The BYOK proxy at POST /api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream gives you the same loop (no process spaw…*
- **API gateway / proxy** — *udio}/stream gives you the same loop (no process spawn) — paste baseUrl + apiKey + model, with presets for OpenAI, Atlas Cloud, Anthropic, Azure Open…*
- **Quota sharing / splitting** — *## What is OpenDesign OpenDesign is a collaborative design agent workspace.*
- **Billing & metering** — *0+ functional skills · rendering templates · 277 plugins*
- **Session persistence** — *ive runtime adapters for agents that OD launches directly.*
- **Skills & plugins** — *eedback, and let your agent refine it in the same project.*
- **Agent runtime** — *ais · 简体中文 · 繁體中文 · 한국어 · 日本語 · العربية · Русский · Українська · Türkçe · ภาษาไทย*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://open-design.ai/install.sh | sh -s <agent>`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Easy. install via npx one-liner, curl | sh installer; needs docker compose up, git clone (build from source); configure database dependency, database migration; one-click setup

**Facts**

- Stars: **99,970** (~613.3/day lifetime average)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **17,024** (~159.1/day lifetime average)
- Health score: **83/100**
- Documentation score: **64/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [openai/codex-security](https://github.com/openai/codex-security)

> @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code.

**Core problems it solves**

- **Model / provider routing**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 37/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install @openai/codex-security`
- Some setup. install via npx one-liner; needs npm install/build; configure API key configuration, sign-in required

**Facts**

- Stars: **11,020** (~128.1/day lifetime average)
- Health score: **81/100**
- Documentation score: **40/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Codex

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

- Stars: **9,348** (~105.0/day lifetime average)
- Health score: **80/100**
- Documentation score: **59/100**
- License: MIT
- Language: Python
- Last push: 2026-10-04
- Works with: Codex

#### [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)

> Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

**Core problems it solves**

- **Automatic failover**
- **Model / provider routing**
- **Skills & plugins**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install fast-jev-compaction`
- Platforms mentioned: macOS
- Some setup. needs npm install/build; configure API key configuration, .env file

**Facts**

- Stars: **7,500** (~357.1/day lifetime average)
- Health score: **75/100**
- Documentation score: **30/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-18
- Works with: Claude Code

</details>

## Quota

*Quota & usage management*

You cannot see how much quota is left, so you get blocked mid-task.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。 | 🔴 Involved | — | — | 7.1k 🚀 +178/d | **78** |
| 🏆 **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些… | 🟢 Turnkey | — | — | 3.3k 🚀 +79/d | **78** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。 把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 Turnkey · OOTB | ✅ | — | 9.2k 🚀 +77/d | **77** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 人保留最终决策。 Agent 可以起草提案卡片——固定约定、请求执行、添加成员——但只有你能采纳或忽略。 执行隔离且有证据。 每个执行任务在独立 Git worktree 中运行，交付固定为不可变版本再交 Reviewer 评审；声明的验证检查、Diff、日志与集成面板都留在房间内。 | 🟢 Easy | — | ✅ | 6.3k (+45/d) | **67** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Self-Improving Sovereign Agents — voices: @tom_doerr, @AIDailyGems | 🟢 Easy | — | — | 4.7k (+24/d) | **65** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | AI 短剧制作的 skill 集合：从一本小说到直接喂生成管线的制作素材——拆角色、排大纲、出场景与道具设定、写剧本、切分镜。 给 AI 编码 agent 用，Claude Code 和 codex 都能跑。 | 🟡 Some setup | — | — | 4.2k 🚀 +67/d | **64** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | orchestrator：Node 26 串行 853 项：852 通过、1 项 Windows ACL 专项跳过；类型检查通过。 desktop：84/84，类型检查与生产构建通过；Python（计算库、回测、数据脚本）：754/754。 | 🟢 Easy | — | — | 2.6k 🚀 +28/d | **64** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 Some setup | — | — | 9.2k (+13/d) | **60** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 Easy | — | — | 2.5k 🚀 +44/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 282 | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 Easy | — | ✅ | 409 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 交代一句话，它自己规划、动手、验收，把 PPT / Word / Excel / 网页落到你硬盘上。 10-06 系统沙箱：AI 跑的命令和脚本在 macOS、Windows 上读不到 Key 和账本、改不了应用；设置 → 安全 能关，每条多花 7–16 毫秒 | 🟡 Some setup | — | — | 277 🚀 +5/d | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 Involved | — | — | 556 | **49** |

**Also does this:** [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)

> 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。不用 API Key、不搞逆向代理——官方网页 + 只读 MCP 桥接。

**Core problems it solves**

- **Quota & usage management** — *ouble? First ask Codex to “Update Codex with ChatGPT” and try again.*
- **Skills & plugins**
- **Agent runtime** — *One-paste install · 一段话安装*
- **MCP support** — *e latest version resolves most known issues.*

**Getting it running**

- Setup: 🔴 **Involved** (friction 63/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Windows, Web
- Involved setup. needs pnpm install/build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **7,127** (~178.2/day lifetime average)
- Health score: **78/100**
- Documentation score: **50/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-01
- Works with: Codex

#### [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)

> An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔…

**Core problems it solves**

- **Quota & usage management** — *平台适配的成品直接到对应平台，再通过**归因**分析表现并把有效经验沉淀回账号画像。*
- **Multi-provider aggregation**
- **API gateway / proxy** — *装 OpenClaw，并创建独立的 easel profile，不覆盖用户已有的 ~/.openclaw/。*
- **Memory & context**
- **Skills & plugins** — *布与归因** 发布质量门禁、敏感与版权风险检查、平台搜索优化、发布 Checklist、多平台格式适配；小红书、抖音、快手、知乎、B 站、微信视频号、微信公众号登录与发布；内容日历回写、账号数据、评论洞察、内容复盘、ROI 与画像记忆*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 15/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via pip install, native installer / package; needs git clone (build from source); configure API key configuration; Chinese: beginner/one-click framing

**Facts**

- Stars: **3,256** (~79.4/day lifetime average)
- Health score: **78/100**
- Documentation score: **79/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex

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

- Stars: **9,245** (~77.0/day lifetime average)
- Health score: **77/100**
- Documentation score: **57/100**
- License: AGPL-3.0
- Language: JavaScript
- Last push: 2026-09-12
- Works with: Claude Code, Codex, Cursor

#### [KunAgent/Kun](https://github.com/KunAgent/Kun)

> 让 AI 在真实项目中规划、执行、验证并交付。

**Core problems it solves**

- **Quota & usage management** — *，提示、附件和任务上下文会发送给所选 Provider；使用前请确认该服务的数据政策。*
- **Workspace isolation** — *建一个房间，为成员选择 Agent 档案、模型和授权的本地仓库，然后用 IM 式的私聊或群聊推进工作。*
- **MCP support** — *arkdown，预览、引用和分析 PDF / Office 文档，分析电子表格，并从大纲创建演示文稿；Office 文件保持只读。*
- **Security & isolation** — *esign 画布；Work 面向写作、资料整理、文档分析和演示产出；Rooms 把多个 Agent 放进同一个协作空间，用私聊和群聊完成讨论、分工、执行与评审。*
- **Self-hostable**
- **GUI / desktop app** — *是把 AI 从“回答问题”推进到“完成工作”的本地优先工作台。*
- **Cross-agent support** — *Mentions Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 27/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via native installer / package; needs git clone (build from source), npm install/build; GUI application

**Facts**

- Stars: **6,319** (~45.5/day lifetime average)
- Health score: **67/100**
- Documentation score: **41/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Codex, Cursor

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

- Stars: **4,697** (~23.8/day lifetime average)
- Health score: **65/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

## Agent Runtime & Desktop UI

*GUI / desktop app*

Terminal-only tools shut out people who do not live in a shell.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 Turnkey · OOTB | ✅ | ✅ | 212.3k (+404/d) | **90** |
| 🏆 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 Turnkey · OOTB | ✅ | ✅ | 14.9k 🚀 +178/d | **85** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 Easy · OOTB | ✅ | — | 26.4k 🚀 +238/d | **84** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 Easy | — | — | 8.4k 🚀 +78/d | **75** |
| ✅ **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 Turnkey · OOTB | ✅ | ✅ | 3.1k 🚀 +40/d | **65** |
| ✅ **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 Turnkey · OOTB | ✅ | — | 5.5k (+44/d) | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1.6k (+6/d) | **60** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **59** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. | 🟢 Turnkey | — | — | 453 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | A persistent memory system for AI coding agents that enables long-term context retention across sessions using local vector database technology. | 🔴 Involved | — | — | 1.7k (+6/d) | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 Turnkey | — | — | 733 | **50** |
| 🔹 **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | Claudable is a powerful Next.js-based web app builder that combines Claude Code's (Cursor CLI also supported!) advanced AI agent capabilities with Lovable's simple and intuitive app building experience. | 🟡 Some setup | — | — | 4.1k (+10/d) | **49** |

**Also does this:** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents), [stablyai/orca](https://github.com/stablyai/orca), [affaan-m/ECC](https://github.com/affaan-m/ECC), [openai/codex](https://github.com/openai/codex), [alibaba/open-code-review](https://github.com/alibaba/open-code-review), [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files), [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex), [zai-org/ZCode](https://github.com/zai-org/ZCode), [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou), [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi), [TencentCloud/Octop](https://github.com/TencentCloud/Octop), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) *(+44 more)*

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

- Stars: **212,311** (~404.4/day lifetime average)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

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

- Stars: **14,934** (~177.8/day lifetime average)
- Health score: **85/100**
- Documentation score: **35/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-05
- Works with: Codex

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

- Stars: **26,409** (~237.9/day lifetime average)
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

- Stars: **8,416** (~77.9/day lifetime average)
- Health score: **75/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Cursor

#### [zeronsh/zeron](https://github.com/zeronsh/zeron)

> Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync.

**Core problems it solves**

- **Agent runtime**
- **GUI / desktop app** — *Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. En…*
- **Cross-agent support** — *Mentions Claude Code, Codex, Cursor*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Quickest install: `curl -fsSL https://zeron.sh/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via curl | sh installer, download a release binary; configure sign-in required; GUI application

**Facts**

- Stars: **3,121** (~39.5/day lifetime average)
- Health score: **65/100**
- Documentation score: **35/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Cursor

</details>

## Remote Control

*Remote control*

Your agent runs on a desktop, but you want to drive it from somewhere else.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 Some setup | — | — | 98.7k (+451/d) | **89** |
| 🏆 **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。 | 🟢 Easy · OOTB | ✅ | ✅ | 7.5k 🚀 +443/d | **83** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.4k (+78/d) | **81** |
| 🏆 **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting,… | 🟢 Easy | — | — | 10.7k 🚀 +90/d | **80** |
| 🏆 **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 模型自选：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。 | 🟢 Easy | — | ✅ | 14.9k (+78/d) | **78** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 Easy | — | — | 5.5k 🚀 +57/d | **73** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. | 🔴 Involved | — | — | 322 | **47** |

**Also does this:** [stablyai/orca](https://github.com/stablyai/orca), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki), [spinabot/brigade](https://github.com/spinabot/brigade), [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector), [felinics/Memoh](https://github.com/felinics/Memoh), [BennyKok/omg.dev](https://github.com/BennyKok/omg.dev), [CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **98,662** (~450.5/day lifetime average)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [zai-org/ZCode](https://github.com/zai-org/ZCode)

> ZCode 是 AI 编程工作台，提供桌面应用、浏览器界面和终端 Agent。本仓库包含客户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。

**Core problems it solves**

- **Remote control**
- **Model / provider routing**
- **Session persistence**
- **Agent runtime**
- **Self-hostable** — *户端、后端服务、共享 UI，以及 Agent CLI 与运行时源码。*
- **GUI / desktop app** — *pnpm --filter @zcode/cli...*

**Getting it running**

- Setup: 🟢 **Easy** (friction 24/100)
- Out of the box: **yes**
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via native installer / package; needs pnpm install/build; configure OAuth login flow; GUI application

**Facts**

- Stars: **7,534** (~443.2/day lifetime average)
- Health score: **83/100**
- Documentation score: **43/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-09-29

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

- Stars: **33,380** (~78.2/day lifetime average)
- Health score: **81/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-09-09
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)

> Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, enforce policies and…

**Core problems it solves**

- **Remote control** — *ode, point at OpenRouter's Anthropic-compatible endpoint*
- **Mobile access**
- **Multi-agent orchestration** — *agents ship with the repo, and they make good first sessions:*
- **Workspace isolation**
- **Model / provider routing** — *switch models in the middle of a session with the /model command.*
- **API gateway / proxy** — *A first-party vendor key for Anthropic, OpenAI, and similar providers*
- **Agent runtime** — *quires agy 1.1.13 or newer.*
- **MCP support** — *ies, searches the live web and reads*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, curl | sh installer; needs docker compose up, npm install/build; configure environment variables, API key configuration; no-code positioning

**Facts**

- Stars: **10,674** (~90.5/day lifetime average)
- Health score: **80/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)

> cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动态 Workflow 编排、模型请求追踪、Computer Use、技能市场、多主题、桌面宠物、H5 远程访问、IM 接入和定时任务，集中在一…

**Core problems it solves**

- **Automatic failover** — *图片生成：聊天中直接生成和编辑图片——ChatGPT / Grok 授权登录即可使用，也支持接入任意 OpenAI 兼容的 Images API。*
- **Remote control** — *de Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动…*
- **Multi-agent orchestration** — *GitHub Pull Requests License 中文 English Docs 简体中文 · English cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Cla…*
- **Workspace isolation** — *cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、…*
- **Billing & metering** — *过程中有问题、想反馈 Bug，或者想看看别人怎么用，欢迎扫码加入 cc-haha 企业微信用户群。*
- **Usage analytics**
- **Session persistence** — */ Agent 定制需求，请联系作者 NanmiCoder。*
- **Memory & context** — *端功能 功能总览 · Computer Use · 桌面宠物 · 手机 H5 与 IM 接力*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Easy. configure API key configuration; GUI application

**Facts**

- Stars: **14,910** (~78.5/day lifetime average)
- Health score: **78/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Claude Code

</details>

## Providers

*Multi-provider aggregation*

Many subscriptions and API keys are scattered; you want one endpoint for all of them.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. | 🟢 Easy | — | — | 141.4k (+330/d) | **93** |
| ✅ **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Codex 可视化提示词注入 · Provider · 会话 · Skills / MCP 管理工具 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 Easy | — | — | 4.1k 🚀 +43/d | **63** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | DSH 0.1.6 破坏性更新适配：精确锁定 @deepseek-ai/dsh@0.1.6-alpha.1，完成 Agent、Session、PTC、Workflow、Sandbox 与 Agent Team 新契约迁移。 工作台完整保留：任务看板、Git、文件交付、模型协作、桌宠、15 套皮肤、SSH 与远程访问继续提供；恢复 4.4.0 品牌图标。 | 🟢 Turnkey · OOTB | ✅ | — | 783 🚀 +14/d | **58** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman cont… | 🟢 Easy | — | ✅ | 723 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 434 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 Involved | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. | 🟡 Some setup | — | — | 696 🚀 +6/d | **49** |

**Also does this:** [loopx-project/loopx](https://github.com/loopx-project/loopx), [cita-777/metapi](https://github.com/cita-777/metapi)

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

- Stars: **141,383** (~329.6/day lifetime average)
- Health score: **93/100**
- Documentation score: **73/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-08
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot
- *Why it is seeded: The incumbent all-in-one provider/account switcher for Claude Code, Codex and friends.*

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

- Stars: **4,103** (~42.7/day lifetime average)
- Health score: **63/100**
- Documentation score: **38/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-06
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

- Stars: **783** (~14.2/day lifetime average)
- Health score: **58/100**
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

- Stars: **723** (~3.1/day lifetime average)
- Health score: **54/100**
- Documentation score: **46/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-02
- Works with: Claude Code, Cursor

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

- Stars: **434** (~0.6/day lifetime average)
- Health score: **54/100**
- Documentation score: **56/100**
- License: Apache-2.0
- Language: HTML
- Last push: 2026-10-02

</details>

## Analytics

*Usage analytics*

You want to know where tokens and money actually went.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 Some setup | — | — | 6.2k (+48/d) | **71** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Research → Ideation → Swipe → Build → Test → Review → Pull Request — fully automated. | 🔴 Involved | — | — | 2.1k (+9/d) | **54** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 Easy · OOTB | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. Cline / Roo Code / Zoo Code / Kilo Code (VS Code extension + CLI) | 🟢 Turnkey · OOTB | ✅ | — | 223 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons,… | 🟡 Some setup | — | — | 723 | **44** |

**Also does this:** [decolua/9router](https://github.com/decolua/9router), [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X), [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

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

- Stars: **6,201** (~48.1/day lifetime average)
- Health score: **71/100**
- Documentation score: **84/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-08
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

- Stars: **2,147** (~8.6/day lifetime average)
- Health score: **54/100**
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

- Stars: **5,887** (~5.1/day lifetime average)
- Health score: **51/100**
- Documentation score: **53/100**
- License: MIT
- Language: Python
- Last push: 2026-06-25

#### [Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)

> We've released Piebald, the ultimate agentic AI developer experience.

**Core problems it solves**

- **Usage analytics**
- **Agent runtime** — *e / Zoo Code / Kilo Code (VS Code extension + CLI)*
- **MCP support** — *epository to show your support!** ⭐*
- **GUI / desktop app**
- **Cross-agent support** — *Mentions Claude Code, Cline, Codex, Copilot*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 0/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `winget install --id LLVM.LLVM`
- Platforms mentioned: macOS, Windows, Linux
- Turnkey. install via winget install, download a release binary

**Facts**

- Stars: **223** (~0.5/day lifetime average)
- Health score: **50/100**
- Documentation score: **32/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Copilot, Cline / Roo

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

- Stars: **723** (~4.2/day lifetime average)
- Health score: **44/100**
- Documentation score: **54/100**
- License: MIT
- Language: Python
- Last push: 2026-04-20
- Works with: Claude Code

</details>

## Billing

*Billing & metering*

When several people share capacity, usage must be measured and charged accurately.

| Tool | What it does | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 107.3k (+199/d) | **91** |
| ✅ **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 Involved | — | — | 11.1k 🚀 +164/d | **74** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 Some setup | — | — | 776 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 399 | **50** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 Involved | — | — | 413 | **46** |

**Also does this:** [farion1231/cc-switch](https://github.com/farion1231/cc-switch), [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api), [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice), [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha), [aipoch/open-science](https://github.com/aipoch/open-science), [superdesigndev/treg](https://github.com/superdesigndev/treg), [future-agi/future-agi](https://github.com/future-agi/future-agi), [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase), [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop), [mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer), [marcusquinn/aidevops](https://github.com/marcusquinn/aidevops), [elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine) *(+7 more)*

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **107,252** (~199.3/day lifetime average)
- Health score: **91/100**
- Documentation score: **69/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-08
- Works with: Gemini CLI
- *Why it is seeded: Gemini's terminal agent, generous free tier.*

#### [trycompai/crm](https://github.com/trycompai/crm)

> Comp AI CRM is an open source, CRM designed for AI agents.

**Core problems it solves**

- **Model / provider routing** — *ur own identity provider on*
- **Billing & metering**
- **Self-hostable**

**Getting it running**

- Setup: 🔴 **Involved** (friction 90/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker compose up -d          # Postgres on :5432`
- Platforms mentioned: Linux, Web
- Involved setup. needs docker compose up, git clone (build from source); configure environment variables, OAuth login flow

**Facts**

- Stars: **11,138** (~163.8/day lifetime average)
- Health score: **74/100**
- Documentation score: **48/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-11

#### [grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)

> 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。

**Core problems it solves**

- **Billing & metering**
- **Memory & context**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 44/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux, Web
- Some setup. needs git clone (build from source); Chinese: beginner/one-click framing

**Facts**

- Stars: **776** (~3.8/day lifetime average)
- Health score: **50/100**
- Documentation score: **42/100**
- Language: Python
- Last push: 2026-10-08
- Works with: OpenCode

#### [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)

> An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems.

**Core problems it solves**

- **Automatic failover** — *totals/counts/groupings" rather than "list of records" — it pushes the work down to PostgreSQL instead of pulling raw rows.*
- **Workspace isolation** — *hows "READ-ONLY" indicators in responses*
- **Billing & metering** — *any standard Odoo installation.*
- **MCP support** — *ccess with any Odoo instance (no module required)*
- **Cross-agent support** — *Mentions Claude Code, Copilot, Cursor*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 46/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via npx one-liner, uvx one-liner; needs docker run, git clone (build from source); configure environment variables, API key configuration

**Facts**

- Stars: **399** (~0.7/day lifetime average)
- Health score: **50/100**
- Documentation score: **58/100**
- License: MPL-2.0
- Language: Python
- Last push: 2026-10-08
- Works with: Claude Code, Cursor, Copilot

#### [intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)

> A comprehensive Model Context Protocol (MCP) server for QuickBooks Online

**Core problems it solves**

- **Billing & metering** — *te CRUD operations are available for all entity types:*
- **MCP support** — *# QuickBooks Online MCP Server*

**Getting it running**

- Setup: 🔴 **Involved** (friction 78/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install`
- Platforms mentioned: Linux, Web
- Involved setup. needs git clone (build from source), npm install/build; configure environment variables, OAuth login flow

**Facts**

- Stars: **413** (~1.1/day lifetime average)
- Health score: **46/100**
- Documentation score: **63/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-09-15
- Works with: Claude Code

</details>

---

## Cross-listed tools

These tools solve problems in more than one area, so they appear under several headings. Each is described in full only under its primary category.

| Tool | Primary | Also listed under |
| --- | --- | --- |
| **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Teams | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | Model Routing | Self-hosting & Security, Teams |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Providers | Billing, Security & Self-hosting |
| **[stablyai/orca](https://github.com/stablyai/orca)** | Mobile | Agent Runtime & Desktop UI, Remote Control |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Billing | Analytics |
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Agent Runtime & Desktop UI | Skills |
| **[garrytan/gstack](https://github.com/garrytan/gstack)** | Isolation & Parallelism | Analytics, Security & Self-hosting |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | Isolation & Parallelism | Analytics, Security & Self-hosting |
| **[openai/codex](https://github.com/openai/codex)** | Accounts | Agent Runtime & Desktop UI |
| **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Self-hosting & Security | Agent Runtime & Desktop UI, Skills |
| **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Remote Control | Analytics, Skills |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Teams | Security & Self-hosting, Self-hosting & Security |
| **[yetone/magpie](https://github.com/yetone/magpie)** | Accounts | Model Routing |
| **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | Accounts | Billing, Model Routing |
| **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Isolation & Parallelism | Analytics, Self-hosting & Security |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Self-hosting & Security | Billing, Model Routing |
| **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | Agent Runtime & Desktop UI | Skills |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | Security & Self-hosting | Skills |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Accounts | Agent Runtime & Desktop UI, Model Routing |
| **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | Model Routing | Remote Control, Self-hosting & Security |
| **[google/artemis](https://github.com/google/artemis)** | Mobile | Security & Self-hosting |
| **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | Remote Control | Agent Runtime & Desktop UI |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Self-hosting & Security | Security & Self-hosting |
| **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | Mobile | Agent Runtime & Desktop UI |
| **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Teams | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | Remote Control | Agent Runtime & Desktop UI, Skills |
| **[decolua/9router](https://github.com/decolua/9router)** | Accounts | Analytics, Model Routing |
| **[spinabot/brigade](https://github.com/spinabot/brigade)** | Self-hosting & Security | Analytics, Remote Control |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Remote Control | Agent Runtime & Desktop UI, Teams |
| **[yc-software/qm](https://github.com/yc-software/qm)** | Teams | Agent Runtime & Desktop UI, Skills |
| **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | Quota | Skills |
| **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Skills | Agent Runtime & Desktop UI |
| **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | Remote Control | Billing, Security & Self-hosting |
| **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Accounts | Agent Runtime & Desktop UI, Quota |
| **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Analytics |
| **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Mobile | Agent Runtime & Desktop UI, Isolation & Parallelism |
| **[pacifio/atlas](https://github.com/pacifio/atlas)** | Analytics | Agent Runtime & Desktop UI, Skills |
| **[aipoch/open-science](https://github.com/aipoch/open-science)** | Remote Control | Billing |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | Self-hosting & Security | Billing, Security & Self-hosting |
| **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | Skills | Security & Self-hosting |
| **[slopus/happy](https://github.com/slopus/happy)** | Mobile | Agent Runtime & Desktop UI |
| **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Analytics | Providers, Teams |
| **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Isolation & Parallelism | Model Routing, Self-hosting & Security |
| **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Teams | Model Routing, Self-hosting & Security |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[yetone/cumora](https://github.com/yetone/cumora)** | Teams | Model Routing, Self-hosting & Security |
| **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Teams | Agent Runtime & Desktop UI, Skills |
| **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | Quota | Self-hosting & Security |
| **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Mobile | Skills |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | Self-hosting & Security | Security & Self-hosting |
| **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | Self-hosting & Security | Remote Control |
| **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | Security & Self-hosting | Agent Runtime & Desktop UI, Skills |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Quota | Security & Self-hosting, Skills |
| **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | Quota | Skills |
| **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | Quota | Security & Self-hosting |
| **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | Providers | Analytics, Security & Self-hosting |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Security & Self-hosting | Agent Runtime & Desktop UI, Skills |
| **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | Self-hosting & Security | Billing |
| **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Isolation & Parallelism | Security & Self-hosting, Skills |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Self-hosting & Security | Billing, Security & Self-hosting |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Self-hosting & Security | Model Routing, Security & Self-hosting |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | Analytics | Model Routing, Security & Self-hosting |
| **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Providers | Agent Runtime & Desktop UI, Billing |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Analytics | Security & Self-hosting, Skills |
| **[felinics/Memoh](https://github.com/felinics/Memoh)** | Self-hosting & Security | Remote Control, Security & Self-hosting |
| **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[mco-org/mco](https://github.com/mco-org/mco)** | Skills | Agent Runtime & Desktop UI |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | Agent Runtime & Desktop UI | Security & Self-hosting, Skills |
| **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Skills | Security & Self-hosting |
| **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Self-hosting & Security | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | Agent Runtime & Desktop UI | Skills |
| **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | Mobile | Analytics, Security & Self-hosting |
| **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | Security & Self-hosting | Billing, Skills |
| **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | Quota | Security & Self-hosting, Teams |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Isolation & Parallelism | Security & Self-hosting, Skills |
| **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | Analytics | Isolation & Parallelism, Self-hosting & Security |
| **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Isolation & Parallelism | Agent Runtime & Desktop UI, Skills |
| **[hex/claude-council](https://github.com/hex/claude-council)** | Teams | Security & Self-hosting, Skills |
| **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Providers | Analytics, Skills |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | Analytics | Security & Self-hosting, Self-hosting & Security |
| **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | Teams | Billing, Isolation & Parallelism |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | Security & Self-hosting | Agent Runtime & Desktop UI |
| **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Teams | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | Mobile | Isolation & Parallelism, Security & Self-hosting |
| **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Mobile | Isolation & Parallelism, Skills |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | Analytics | Agent Runtime & Desktop UI, Skills |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Analytics | Skills |
| **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | Providers | Security & Self-hosting, Self-hosting & Security |
| **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Analytics | Billing, Security & Self-hosting |
| **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | Isolation & Parallelism | Billing, Skills |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Model Routing | Skills |
| **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Accounts | Analytics, Analytics |
| **[cita-777/metapi](https://github.com/cita-777/metapi)** | Accounts | Billing, Providers |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | Mobile | Skills |
| **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Security & Self-hosting | Agent Runtime & Desktop UI |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Analytics | Security & Self-hosting, Skills |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Mobile | Agent Runtime & Desktop UI, Remote Control |
| **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Quota | Agent Runtime & Desktop UI |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | Skills | Agent Runtime & Desktop UI |
| **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Analytics | Security & Self-hosting, Skills |
| **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | Analytics | Billing, Model Routing |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | Agent Runtime & Desktop UI | Skills |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | Model Routing | Agent Runtime & Desktop UI, Skills |
| **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | Billing | Security & Self-hosting |
| **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | Quota | Remote Control, Self-hosting & Security |
| **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | Analytics | Agent Runtime & Desktop UI, Billing |
| **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | Agent Runtime & Desktop UI | Security & Self-hosting, Skills |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Teams | Isolation & Parallelism, Skills |
| **[solo-agent/solo](https://github.com/solo-agent/solo)** | Providers | Agent Runtime & Desktop UI, Skills |
| **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | Quota | Model Routing, Self-hosting & Security |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | Self-hosting & Security | Analytics |
| **[schmitech/orbit](https://github.com/schmitech/orbit)** | Self-hosting & Security | Billing, Model Routing |
| **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | Teams | Isolation & Parallelism, Self-hosting & Security |
| **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Security & Self-hosting | Agent Runtime & Desktop UI, Skills |
| **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Skills | Analytics, Billing |
| **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | Accounts | Model Routing, Self-hosting & Security |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | Security & Self-hosting | Agent Runtime & Desktop UI |
| **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Self-hosting & Security | Billing, Teams |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Self-hosting & Security | Skills |
| **[IBM/mcp](https://github.com/IBM/mcp)** | Security & Self-hosting | Agent Runtime & Desktop UI, Skills |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Model Routing | Security & Self-hosting |
| **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Remote Control | Isolation & Parallelism |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Isolation & Parallelism | Agent Runtime & Desktop UI |
| **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | Security & Self-hosting | Agent Runtime & Desktop UI |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | Security & Self-hosting | Skills |
| **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Analytics | Agent Runtime & Desktop UI, Security & Self-hosting |
| **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | Analytics | Security & Self-hosting |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Security & Self-hosting | Model Routing, Self-hosting & Security |
| **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | Accounts | Model Routing, Self-hosting & Security |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | Skills | Agent Runtime & Desktop UI, Security & Self-hosting |

---

## ⚔️ Challengers

A challenger covers an incumbent's ground and is rising, but has **not** yet met the bar for retirement — either it misses some of the incumbent's capabilities, or its traction is still far behind. These are the pairs to watch: they are where the next elimination is most likely to come from.

| Incumbent | Challenger | Coverage | Traction gap |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | 0.05x the stars (6,548 vs 141,383) |

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
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.90x the stars (7,087 vs 716) | 🤖 auto (high) |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 57.25x the stars (18,720 vs 327) | 🤖 auto (high) |
| **[Arvincreator/project-golem](https://github.com/arvincreator/project-golem)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 3.79x the stars (2,422 vs 639) | 🤖 auto (high) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[HarnessMD/munder-difflin](https://github.com/harnessmd/munder-difflin)** | 22.58x the stars (8,582 vs 380) | 🤖 auto (high) |
| **[LerianStudio/ring](https://github.com/lerianstudio/ring)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 62.73x the stars (13,612 vs 217) | 🤖 auto (high) |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[pacifio/atlas](https://github.com/pacifio/atlas)** | 18.14x the stars (9,359 vs 516) | 🤖 auto (high) |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 14.10x the stars (29,236 vs 2,074) | 🤖 auto (high) |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 63.97x the stars (275,209 vs 4,302) | 🤖 auto (high) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 218.28x the stars (99,970 vs 458) | 🤖 auto (high) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.59x the stars (27,330 vs 4,892) | 🤖 auto (high) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 24.21x the stars (7,918 vs 327) | 🤖 auto (high) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 160.21x the stars (99,970 vs 624) | 🤖 auto (high) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 6.25x the stars (7,918 vs 1,266) | 🤖 auto (high) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 74.58x the stars (18,720 vs 251) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 46.74x the stars (20,097 vs 430) | 🤖 auto (high) |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/ccteam-creator)** | **[HarnessMD/munder-difflin](https://github.com/harnessmd/munder-difflin)** | 27.95x the stars (8,582 vs 307) | 🤖 auto (high) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 578.22x the stars (158,431 vs 274) | 🤖 auto (high) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 21.54x the stars (27,330 vs 1,269) | 🤖 auto (high) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 143.97x the stars (141,383 vs 982) | 🤖 auto (high) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[EverMind-AI/Raven](https://github.com/evermind-ai/raven)** | 9.57x the stars (5,293 vs 553) | 🤖 auto (high) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 3.51x the stars (2,422 vs 691) | 🤖 auto (high) |
| **[trailhq/Graft](https://github.com/trailhq/graft)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 10.23x the stars (99,970 vs 9,770) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 580.61x the stars (275,209 vs 474) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 10.72x the stars (29,236 vs 2,728) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[FrancyJGLisboa/agent-skills-platform](https://github.com/francyjglisboa/agent-skills-platform)** | 8.15x the stars (2,403 vs 295) | 🤖 auto (high) |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 29.64x the stars (27,330 vs 922) | 🤖 auto (medium) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 7.63x the stars (2,083 vs 273) | 🤖 auto (high) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 737.83x the stars (275,209 vs 373) | 🤖 auto (medium) |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 9.02x the stars (2,083 vs 231) | 🤖 auto (high) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 6.94x the stars (44,463 vs 6,408) | 🤖 auto (medium) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 452.65x the stars (275,209 vs 608) | 🤖 auto (medium) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.88x the stars (812 vs 282) | 🤖 auto (high) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 7.88x the stars (29,236 vs 3,708) | 🤖 auto (medium) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 6.02x the stars (2,083 vs 346) | 🤖 auto (medium) |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 7.89x the stars (2,422 vs 307) | 🤖 auto (medium) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 548.23x the stars (275,209 vs 502) | 🤖 auto (medium) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.24x the stars (33,380 vs 4,053) | 🤖 auto (high) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 3.72x the stars (1,037 vs 279) | 🤖 auto (medium) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.29x the stars (812 vs 355) | 🤖 auto (high) |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 2.86x the stars (14,910 vs 5,209) | 🤖 auto (medium) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 3.69x the stars (2,083 vs 564) | 🤖 auto (medium) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.46x the stars (1,423 vs 973) | 🤖 auto (medium) |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 1.36x the stars (99,970 vs 73,767) | 🤖 auto (medium) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.30x the stars (1,423 vs 1,091) | 🤖 auto (medium) |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | model-routing | 73.8k | 🔻 Superseded | 1.36x the stars (99,970 vs 73,767) |
| **[trailhq/Graft](https://github.com/trailhq/Graft)** | model-routing | 9.8k | 🔻 Superseded | 10.23x the stars (99,970 vs 9,770) |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.4k | 🔻 Superseded | 6.94x the stars (44,463 vs 6,408) |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | remote-control | 5.2k | 🔻 Superseded | 2.86x the stars (14,910 vs 5,209) |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-parallelism | 4.9k | 🔻 Superseded | 5.59x the stars (27,330 vs 4,892) |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | self-hosting-security | 4.3k | 🔻 Superseded | 63.97x the stars (275,209 vs 4,302) |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | remote-control | 4.1k | 🔻 Superseded | 8.24x the stars (33,380 vs 4,053) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 Superseded | 7.88x the stars (29,236 vs 3,708) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 Superseded | 10.72x the stars (29,236 vs 2,728) |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 Superseded | 14.10x the stars (29,236 vs 2,074) |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | isolation-parallelism | 1.3k | 🔻 Superseded | 21.54x the stars (27,330 vs 1,269) |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 Superseded | 6.25x the stars (7,918 vs 1,266) |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | mobile | 1.1k | 🔻 Superseded | 1.30x the stars (1,423 vs 1,091) |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers | 982 | 🔻 Superseded | 143.97x the stars (141,383 vs 982) |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile | 973 | 🔻 Superseded | 1.46x the stars (1,423 vs 973) |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-parallelism | 922 | 🔻 Superseded | 29.64x the stars (27,330 vs 922) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | analytics | 716 | 🔻 Superseded | 9.90x the stars (7,087 vs 716) |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | security-self-hosting | 691 | 🔻 Superseded | 3.51x the stars (2,422 vs 691) |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | security-self-hosting | 639 | 🔻 Superseded | 3.79x the stars (2,422 vs 639) |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 624 | 🔻 Superseded | 160.21x the stars (99,970 vs 624) |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | self-hosting-security | 608 | 🔻 Superseded | 452.65x the stars (275,209 vs 608) |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | isolation-parallelism | 564 | 🔻 Superseded | 3.69x the stars (2,083 vs 564) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-parallelism | 553 | 🔻 Superseded | 9.57x the stars (5,293 vs 553) |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | analytics | 516 | 🔻 Superseded | 18.14x the stars (9,359 vs 516) |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | self-hosting-security | 502 | 🔻 Superseded | 548.23x the stars (275,209 vs 502) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | self-hosting-security | 474 | 🔻 Superseded | 580.61x the stars (275,209 vs 474) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 458 | 🔻 Superseded | 218.28x the stars (99,970 vs 458) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 430 | 🔻 Superseded | 46.74x the stars (20,097 vs 430) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-parallelism | 380 | 🔻 Superseded | 22.58x the stars (8,582 vs 380) |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | self-hosting-security | 373 | 🔻 Superseded | 737.83x the stars (275,209 vs 373) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 355 | 🔻 Superseded | 2.29x the stars (812 vs 355) |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | isolation-parallelism | 346 | 🔻 Superseded | 6.02x the stars (2,083 vs 346) |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | accounts | 327 | 🔻 Superseded | 57.25x the stars (18,720 vs 327) |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 327 | 🔻 Superseded | 24.21x the stars (7,918 vs 327) |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | isolation-parallelism | 307 | 🔻 Superseded | 27.95x the stars (8,582 vs 307) |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | security-self-hosting | 307 | 🔻 Superseded | 7.89x the stars (2,422 vs 307) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills | 295 | 🔻 Superseded | 8.15x the stars (2,403 vs 295) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 Superseded | 2.88x the stars (812 vs 282) |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | isolation-parallelism | 279 | 🔻 Superseded | 3.72x the stars (1,037 vs 279) |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 274 | 🔻 Superseded | 578.22x the stars (158,431 vs 274) |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | isolation-parallelism | 273 | 🔻 Superseded | 7.63x the stars (2,083 vs 273) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | accounts | 251 | 🔻 Superseded | 74.58x the stars (18,720 vs 251) |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | isolation-parallelism | 231 | 🔻 Superseded | 9.02x the stars (2,083 vs 231) |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | isolation-parallelism | 217 | 🔻 Superseded | 62.73x the stars (13,612 vs 217) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-08 11:25 UTC. 226 live tools · 130 candidates rejected by the quality gates.</sub>
