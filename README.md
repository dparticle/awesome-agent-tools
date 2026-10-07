<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools

> **Building an "AGI" out of the tools we already have.** No single agent is enough — one hits its quota, one cannot be reached from your phone, one forgets your project. This is the curated, continuously-verified map of the tools that patch those gaps, and of which ones have been overtaken.

**[中文说明](README.zh-CN.md)** · [Methodology](docs/METHODOLOGY.md) · [Elimination rules](docs/SUPERSEDE.md) · [Capability taxonomy](docs/TAXONOMY.md) · [Machine-readable index](data/index.json)

[![Daily crawl](https://img.shields.io/badge/crawl-daily%20via%20GitHub%20Actions-2ea44f?logo=githubactions&logoColor=white)](.github/workflows/daily.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Tools](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FPLACEHOLDER%2Fmain%2Fdata%2Findex.json&query=%24.counts.tools&label=tools&color=blue)](data/index.json)

**108 tools** across **12 categories** · **38 retired** into the [graveyard](#-the-graveyard) · last rebuilt **2026-10-07 14:00 UTC**

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

- [Remote & Mobile Control](#remote-mobile-control) — 3 tools
- [Quota & Multi-Account Ops](#quota-multi-account-ops) — 5 tools
- [Multi-Agent Orchestration](#multi-agent-orchestration) — 5 tools
- [Model & Provider Routing](#model-provider-routing) — 4 tools
- [Subscription Sharing & Gateways](#subscription-sharing-gateways) — 4 tools
- [Agent Runtimes & Subscriptions](#agent-runtimes-subscriptions) — 24 tools
- [Skills, Plugins & Prompts](#skills,-plugins-prompts) — 17 tools
- [Memory & Context](#memory-context) — 22 tools
- [Observability, Analytics & Cost](#observability,-analytics-cost) — 3 tools
- [Sandboxing & Security](#sandboxing-security) — 1 tools
- [Interop & MCP](#interop-mcp) — 19 tools
- [Workflow & Terminal UX](#workflow-terminal-ux) — 1 tools
- [The Graveyard](#-the-graveyard) — retired tools and why
- [Contributing](#contributing)

---

## Remote & Mobile Control

*Keep the agent working when you are not at the desk.*

Your agent runs on a workstation, but you are on a train, in a meeting, or on the sofa. Without these tools the session simply stops when you walk away.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | Open-source orchestration for teams of AI agents. | 🟡 Some setup | — | — | 98.3k (+451/d) | **89** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | Multi-provider within one session. — Remote control | 🟢 Easy · OOTB | ✅ | ✅ | 24k (+54/d) | **71** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Open-source Windows desktop client and GUI for DeepSeek Harness — zero-setup installer with Codex, plugins, skills, SSH, mobile remote access, and 11… | 🟢 Turnkey · OOTB | ✅ | — | 777 🚀 +14/d | **58** |

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

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

- Stars: **98,271** (~450.8/day lifetime average)
- Health score: **89/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

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

- Stars: **24,042** (~53.9/day lifetime average)
- Health score: **71/100**
- Documentation score: **29/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex
- *Why it is seeded: Drive Claude Code / Codex from a phone with end-to-end encryption.*

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

- Stars: **777** (~14.4/day lifetime average)
- Health score: **58/100**
- Documentation score: **43/100**
- License: BSD-3-Clause
- Language: JavaScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex

</details>

## Quota & Multi-Account Ops

*Never stop because one account hit its limit.*

Subscription quotas are finite and reset on their own schedule. These tools pool accounts, watch the remaining quota, and switch automatically so a long task never dies at the limit.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code on Kimi, Codex on DeepSeek, Gemini CLI on GLM, OpenCode on your ChatGPT plan. | 🟢 Turnkey | — | — | 5.7k 🚀 +436/d | **84** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | English · Portuguese (BR) · 简体中文 — Multi-account switching | 🟢 Easy | — | — | 18.7k (+71/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. | 🟢 Easy | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a… | 🟢 Easy | — | — | 271 | **52** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/codingagentaccount_manager/main/install.sh?$(date +%s)" \| bash | 🟡 Some setup | — | — | 208 | **51** |

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [yetone/magpie](https://github.com/yetone/magpie)

> Claude Code on Kimi, Codex on DeepSeek, Gemini CLI on GLM, OpenCode on your ChatGPT plan.

**Core problems it solves**

- **Multi-account switching**
- **Quota & usage management**
- **Automatic failover**
- **Model / provider routing** — *sonix planner default restores Plan.*
- **API gateway / proxy** — *ncent Cloud · Huawei Cloud MaaS · Volcengine Ark · Mistral · Groq · xAI · OpenRouter · Together · Fireworks · SiliconFlow · NVIDIA NIM · ModelScope ·…*
- **Usage analytics** — *in magpie as they do in their own apps.*
- **Agent runtime**
- **MCP support** — *magpie offers it as a provider.*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 18/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://usemagpie.ai/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via go install, curl | sh installer; configure config file, sign-in required; one-click setup

**Facts**

- Stars: **5,667** (~435.9/day lifetime average)
- Health score: **84/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot
- *Why it is seeded: One place for every agent's model; pools accounts and reroutes models.*

#### [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)

> English · Portuguese (BR) · 简体中文

**Core problems it solves**

- **Multi-account switching** — *surf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Quota & usage management** — *目前支持 Antigravity IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，…*
- **Automatic failover**
- **Multi-agent orchestration** — *测速与已有连接处理的设计也参考其源码，当前运行内核仍为 Mihomo，不代表官方合作关系。*
- **Parallel execution** — *ty IDE、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、CodeBuddy CN、Qoder、Trae、TRAE SOLO、Trae CN、TRAE SOLO CN、Zed 和 ZCode，并支持多账号多实例并行运行。*
- **Model / provider routing**
- **Multi-provider aggregation** — *的指纹浏览器，支持独立浏览器指纹环境、Cookie / 存储隔离、Roxy 原生住宅 IP、团队协作与 API / MCP 自动化能力，适合需要管理 AI 账号矩阵、降低账号关联风险、提升长期使用稳定性的用户。*
- **API gateway / proxy** — *ity 账号切号逻辑参考：Antigravity-Manager*

**Getting it running**

- Setup: 🟢 **Easy** (friction 26/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `brew tap jlcodes99/cockpit-tools https://github.com/jlcodes99/cockpit-tools`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via Homebrew install, native installer / package; needs npm install/build; configure API key configuration, config.json/yaml/toml; GUI application

**Facts**

- Stars: **18,691** (~70.8/day lifetime average)
- Health score: **77/100**
- Documentation score: **61/100**
- Language: Rust
- Last push: 2026-10-01
- Works with: Codex, OpenCode, Cursor, Copilot

#### [Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)

> codex-auth is a command-line tool for switching Codex accounts.

**Core problems it solves**

- **Multi-account switching** — *onfigure live TUI refresh interval*
- **GUI / desktop app** — *napshot from hours ago instead of your latest state.*

**Getting it running**

- Setup: 🟢 **Easy** (friction 21/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Quickest install: `npm install -g @loongphy/codex-auth`
- Easy. install via npx one-liner, global npm install; needs npm install/build; configure environment variables, sign-in required; GUI application

**Facts**

- Stars: **2,782** (~11.6/day lifetime average)
- Health score: **58/100**
- Documentation score: **37/100**
- License: MIT
- Language: Zig
- Last push: 2026-10-06
- Works with: Codex

#### [uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

> Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude.

**Core problems it solves**

- **Multi-account switching** — *r CLAUDE.md, plugins, hooks, skills, MCP servers and tools, leaving a clean session for headless work or blind evals.*
- **Quota & usage management** — *or delegate a headless prompt to another account without leaving the chat.*
- **Parallel execution** — *auth or a single keypress in the TUI.*
- **Model / provider routing** — *ve usage monitor, then wires the two together so a fallback chain moves you off an exhausted account before Claude Code ever blocks.*
- **Usage analytics** — *e and rate limits? The Overview tab shows color-coded 5h (and 7-day) bars per account with reset times; the Usage tab breaks down every rate-limit wi…*
- **Session persistence** — *ns the refresh and auto-switch loop with no TUI and publishes status.json for a menu-bar app to read, or serves that feed, the account switch, the he…*
- **Skills & plugins**
- **MCP support** — *Claude Code multi-account manager & MCP Plugin*

**Getting it running**

- Setup: 🟢 **Easy** (friction 25/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `cargo install clauth`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via cargo install, curl | sh installer; needs cargo build; configure API key configuration, OAuth login flow

**Facts**

- Stars: **271** (~1.7/day lifetime average)
- Health score: **52/100**
- Documentation score: **57/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-07
- Works with: Claude Code, Codex

#### [Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)

> curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/codingagentaccount_manager/main/install.sh?$(date +%s)" | bash

**Core problems it solves**

- **Multi-account switching** — *cost AI coding subscriptions (Claude Max, GPT Pro, Gemini Ultra).*
- **Quota & usage management** — *th nothing cached reads no cached data, not 0%, and is*
- **Automatic failover** — *okens rotated during a failed login are saved before returning to*
- **Multi-agent orchestration**
- **Parallel execution** — *ymlink is created — no broken links for users who don't have a given tool installed.*
- **Model / provider routing** — *so seeding stays an explicit*
- **Billing & metering** — *claims that credentials were renewed.*
- **Usage analytics** — *Tracking — Database-backed tracking of rate limit hits with configurable cooldown windows*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 46/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/coding_agent_account_manager/main/install.sh?…`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via Homebrew install, scoop install; needs git clone (build from source), go build; configure environment variables, API key configuration

**Facts**

- Stars: **208** (~0.7/day lifetime average)
- Health score: **51/100**
- Documentation score: **73/100**
- License: NOASSERTION
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

</details>

## Multi-Agent Orchestration

*One agent is a worker; several are a team.*

Serial work is slow and a single context window is small. These tools plan, dispatch, isolate and supervise several agents at once — often one git worktree per agent.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. | 🟢 Turnkey · OOTB | ✅ | ✅ | 86.9k (+426/d) | **92** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is a desktop, mobile, web, and CLI app for coding agents. | 🟢 Easy | — | ✅ | 20k (+56/d) | **73** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. | 🟡 Some setup | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Command your AI army like a feudal warlord. | 🟡 Some setup | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | A Git worktree workflow tool for AI coding agents. | 🟡 Some setup · OOTB | ✅ | — | 279 | **47** |

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

- Stars: **86,867** (~425.8/day lifetime average)
- Health score: **92/100**
- Documentation score: **52/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo
- *Why it is seeded: Run a fleet of parallel agents, each on your own subscription.*

#### [getpaseo/paseo](https://github.com/getpaseo/paseo)

> Paseo is a desktop, mobile, web, and CLI app for coding agents.

**Core problems it solves**

- **Remote control**
- **Mobile access** — *emon machine and inside connected clients; install only code you trust.*
- **Multi-agent orchestration** — *once, each in its own worktree, on one machine or several.*
- **Parallel execution** — *ull requests, and a browser in one window.*
- **Workspace isolation** — *ktop, mobile, web, and CLI app for coding agents.*
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

- Stars: **19,955** (~55.6/day lifetime average)
- Health score: **73/100**
- Documentation score: **51/100**
- License: NOASSERTION
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Copilot
- *Why it is seeded: Orchestrate several coding agents from desktop and mobile; easier on-ramp than Orca.*

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

- Stars: **2,907** (~11.8/day lifetime average)
- Health score: **54/100**
- Documentation score: **46/100**
- Language: JavaScript
- Last push: 2026-09-29
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)

> Command your AI army like a feudal warlord.

**Core problems it solves**

- **Remote control** — *— you won't need to do it again.*
- **Mobile access** — *Transfer your private key to the phone, or use password authentication*
- **Multi-agent orchestration** — *Zero wait time — give your next order while tasks run in the background*
- **Parallel execution** — *ocumented in detail: docs/philosophy.md*
- **Workspace isolation**
- **Model / provider routing** — *out restarting the entire system.*
- **Billing & metering** — *→ Karo → Ashigaru chain of command prevents conflicts by design: clear ownership, dedicated files per agent, event-driven communication, no polling.*
- **Session persistence** — *ead of direct messaging between agents?*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 46/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://tailscale.com/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Some setup. install via npx one-liner, curl | sh installer; needs git clone (build from source), npm install/build; configure environment variables, API key configuration

**Facts**

- Stars: **1,423** (~5.6/day lifetime average)
- Health score: **52/100**
- Documentation score: **72/100**
- License: MIT
- Language: Shell
- Last push: 2026-08-06
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot

#### [nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)

> A Git worktree workflow tool for AI coding agents.

**Core problems it solves**

- **Automatic failover** — *; dirty worktrees are skipped*
- **Multi-agent orchestration** — *ration: Each feature gets its own working directory*
- **Parallel execution** — *rktree workflow tool for AI coding agents.*
- **Workspace isolation** — *ration is installed automatically.*
- **Agent runtime**
- **GUI / desktop app**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 40/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `npm install -g agent-worktree`
- Platforms mentioned: Windows
- Some setup. install via global npm install; needs pnpm install/build, npm install/build; configure config.json/yaml/toml

**Facts**

- Stars: **279** (~1.1/day lifetime average)
- Health score: **47/100**
- Documentation score: **54/100**
- License: MIT
- Language: Rust
- Last push: 2026-08-25

</details>

## Model & Provider Routing

*Run your favourite agent on somebody else's model.*

The agent loop you like is not tied to the model it ships with. These tools point Claude Code, Codex or Gemini CLI at DeepSeek, Kimi, Qwen or a local model — which is also how you keep working when one vendor's quota is gone.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | Never stop coding. — Multi-account switching | 🔴 Involved | — | — | 30.4k (+111/d) | **81** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | route Claude Code requests through multiple upstream providers (OpenCode Go, OpenCode Zen, and AWS Bedrock) with automatic model selection and format… | 🟢 Easy | — | — | 980 (+6/d) | **56** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | One proxy. — Quota & usage management | 🔴 Involved | — | — | 556 | **49** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic r… | 🟡 Some setup | — | — | 474 | **49** |

<details>
<summary><b>Why these tools — 4 detailed breakdowns</b></summary>

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

- Stars: **30,405** (~110.6/day lifetime average)
- Health score: **81/100**
- Documentation score: **66/100**
- License: MIT
- Language: JavaScript
- Last push: 2026-10-01
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **980** (~5.7/day lifetime average)
- Health score: **56/100**
- Documentation score: **65/100**
- License: AGPL-3.0
- Language: Go
- Last push: 2026-10-02
- Works with: Claude Code, OpenCode

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

- Stars: **556** (~1.1/day lifetime average)
- Health score: **49/100**
- Documentation score: **70/100**
- License: NOASSERTION
- Language: Python
- Last push: 2026-09-23
- Works with: Claude Code, Gemini CLI, OpenCode, Cursor

#### [hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)

> Multi-provider AI chat inside Obsidian — Claude, Gemini, Codex, and Antigravity in one sidebar, with per-tab routing, inline diff editing, academic research skills, and MCP support.

**Core problems it solves**

- **Multi-agent orchestration** — *harts, and actionable findings.*
- **Parallel execution**
- **Model / provider routing** — *s, manifest.json, styles.css into /.obsidian/plugins/katmer-code/*
- **MCP support** — *Context strip shows real input tokens against the model's actual window (1M for Gemini 2.5 / 3.x family, 400K for Codex GPT-5.x, 200K-1M for Claude).*
- **Notifications** — *psible sections and interactive elements*
- **Cross-agent support** — *Mentions Claude Code, Codex, Gemini CLI*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `npm install -g @anthropic-ai/claude-code`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via curl | sh installer, global npm install; needs git clone (build from source), npm install/build; configure config.json/yaml/toml, OAuth login flow; GUI application

**Facts**

- Stars: **474** (~2.4/day lifetime average)
- Health score: **49/100**
- Documentation score: **56/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-15
- Works with: Claude Code, Codex, Gemini CLI

</details>

## Subscription Sharing & Gateways

*Turn one subscription into a metered, multi-tenant service.*

A single subscription often has more capacity than one person uses. These tools redistribute it safely — with per-user keys, rate limits, quota accounting and billing — instead of sharing a password.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution | 🟡 Some setup | — | — | 43.4k (+148/d) | **85** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 中转站的中转站 — 将分散的 AI 中转站聚合为一个统一网关 — Multi-account switching | 🔴 Involved | — | — | 3.3k (+15/d) | **54** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 为 Sub2API 增加 账号级 STATE 票据管理，尝试应对最近 ChatGPT / Codex 账号的模型降质和降并发：请求的模型被路由到其他模型，或 OpenAI 上游限制账号可同时处理的请求数量。 | 🟡 Some setup | — | — | 214 🚀 +12/d | **48** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. | 🔴 Involved | — | — | 241 | **42** |

<details>
<summary><b>Why these tools — 4 detailed breakdowns</b></summary>

#### [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)

> AI API Gateway Platform for Subscription Quota Distribution

**Core problems it solves**

- **Multi-account switching** — *Sub2API: it features a built-in native Roxy AI Agent and high-quality native residential IPs, supports batch automation via simple commands, and sign…*
- **Automatic failover** — *, and more affordable AI API access.*
- **Mobile access** — *oject! AxisNow protects and accelerates websites and APIs, delivering an optimal access experience across mainland China and globally, while extendin…*
- **Multi-agent orchestration** — *targets and bridged to xAI HTTP/SSE Responses upstream*
- **Model / provider routing** — *is makes AI usage more reliable and manageable across individual development, team collaboration, and production environments.*
- **API gateway / proxy** — *es, and legal liabilities shall be borne solely by the party conducting such activity.*
- **Billing & metering** — *r sponsoring this project! PatewayAI is a premium API relay built for heavy AI developers, offering the full Claude and Codex series sourced 100% fro…*
- **Usage analytics**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 57/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash`
- Platforms mentioned: macOS, Windows, Linux, iOS, Android, Web
- Some setup. install via curl | sh installer, global npm install; needs docker compose up, git clone (build from source); configure environment variables, API key configuration; one-click setup

**Facts**

- Stars: **43,392** (~148.1/day lifetime average)
- Health score: **85/100**
- Documentation score: **64/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode
- *Why it is seeded: Turn upstream AI subscriptions into a metered, rate-limited, billable relay.*

#### [cita-777/metapi](https://github.com/cita-777/metapi)

> 中转站的中转站 — 将分散的 AI 中转站聚合为一个统一网关

**Core problems it solves**

- **Multi-account switching** — *Metapi 用户专属福利：通过 专属推广链接 注册即可领取 5 美元等值测试额度 / 首充专属优惠，快速添加上游并开始调用。*
- **Quota & usage management** — *i、Kimi、GLM、DeepSeek 等主流模型。*
- **Automatic failover** — *- 完整的 SSE 流式传输支持，自动格式转换（OpenAI ⇄ Claude）*
- **Multi-provider aggregation**
- **API gateway / proxy** — *中转站的中转站 — 将分散的 AI 中转站聚合为一个统一网关*
- **Billing & metering** — *e、Gemini 兼容上游接入，配合 Metapi 的模型自动发现、成本优选与故障转移，为 Cursor、Claude Code、Codex、Open WebUI 等工具提供稳定模型服务。*
- **Usage analytics**
- **Self-hostable**

**Getting it running**

- Setup: 🔴 **Involved** (friction 81/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker compose up -d`
- Platforms mentioned: Linux, iOS
- Involved setup. needs docker compose up, docker run; configure API key configuration, OAuth login flow

**Facts**

- Stars: **3,304** (~14.9/day lifetime average)
- Health score: **54/100**
- Documentation score: **66/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-06
- Works with: Claude Code, Codex, Gemini CLI, Cursor

#### [wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

> 为 Sub2API 增加 账号级 STATE 票据管理，尝试应对最近 ChatGPT / Codex 账号的模型降质和降并发：请求的模型被路由到其他模型，或 OpenAI 上游限制账号可同时处理的请求数量。

**Core problems it solves**

- **Multi-account switching** — *oxy 的 SID 格式，不用每次手动生成、导入一堆 IP。*
- **Quota & usage management**
- **Model / provider routing**
- **API gateway / proxy** — *1024proxy 的 SID 格式，不用每次手动生成、导入一堆 IP。*
- **Billing & metering** — *过此前置代理」 后，插件列表内账号的固定代理连接会额外经过前置代理：服务器 → Clash 等前置代理 → 账号固定代理 → 上游，最终出口仍是账号固定代理。*
- **Skills & plugins** — *件都是空白配置，不附带作者的账号、代理/IP、API Key、STATE、数据库或签名私钥。*
- **Security & isolation**
- **Self-hostable**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 51/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker compose up -d --build`
- Platforms mentioned: macOS, Linux
- Some setup. needs docker compose up; configure API key configuration, OAuth login flow

**Facts**

- Stars: **214** (~11.9/day lifetime average)
- Health score: **48/100**
- Documentation score: **51/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-09-22
- Works with: Codex

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

- Stars: **241** (~2.3/day lifetime average)
- Health score: **42/100**
- Documentation score: **41/100**
- License: LGPL-3.0
- Language: Go
- Last push: 2026-09-17
- Works with: Codex, OpenCode

</details>

## Agent Runtimes & Subscriptions

*Alternatives to the agent you already pay for.*

Sometimes the model access is the point: a flat subscription that unlocks many models, or an open-source agent you can fork. These are the runtimes themselves, not add-ons.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | OpenDesign is a collaborative design agent workspace. | 🟢 Easy | — | — | 99.8k (+616/d) | **95** |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. | 🟢 Easy | — | — | 107.2k (+200/d) | **91** |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | curl -fsSL https://opencode.ai/install \| bash | 🟢 Turnkey · OOTB | ✅ | ✅ | 212.1k (+405/d) | **90** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, e… | 🟢 Turnkey · OOTB | ✅ | — | 149.7k (+253/d) | **90** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | If you want Codex in your code editor (VS Code, Cursor, Windsurf), install in your IDE. | 🟢 Turnkey | — | ✅ | 128.1k (+236/d) | **89** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. | 🟢 Easy | — | — | 8.8k 🚀 +130/d | **85** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! | 🟢 Turnkey | — | — | 33.4k (+78/d) | **81** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | Give Claude Code, Codex, OpenCode, or DeepSeek Harness a goal once. | 🟢 Easy | — | — | 1.7k 🚀 +26/d | **59** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Y-API provides a unified API for models from DeepSeek, Qwen, GLM, Kimi, OpenAI, and more. | 🟢 Turnkey · OOTB | ✅ | ✅ | 1k | **59** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. | 🟡 Some setup | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | Cognition + Obsidian + Git — A self-evolving second brain powered by AI agents, markdown files, and version control. | 🟢 Easy | — | — | 1.3k | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | Git-native memory for AI coding agents — Memory & context | 🟢 Easy · OOTB | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | Bring your AI conversations, project files, terminals, and live previews together. | 🟢 Easy | — | ✅ | 275 🚀 +17/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Appearance follows your OS — see Appearance. | 🟢 Easy | — | ✅ | 519 | **56** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that consults multiple AI coding agents in parallel and shows you their answers side-by-side. | 🟡 Some setup | — | — | 843 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 面向 JDK 8+ 的 Java AI Agentic 开发套件：统一接入主流大模型服务，内置从工具调用、RAG、MCP、Skill、沙箱到 Agent 编排与长时任务治理的完整能力，支撑快速构建专属的 Agent 与 Harness 应用。 | 🟢 Turnkey | — | — | 434 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. | 🟡 Some setup | — | — | 406 | **54** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | npx metaharness · open the Studio → — Multi-agent orchestration | 🟡 Some setup | — | — | 688 🚀 +6/d | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by d… | 🟢 Easy · OOTB | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent… | 🔴 Involved | — | — | 835 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | One command. — Automatic failover | 🟡 Some setup | — | — | 427 | **52** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 交代一句话，它自己规划、动手、验收，把 PPT / Word / Excel / 网页落到你硬盘上。 | 🟡 Some setup | — | — | 275 🚀 +5/d | **50** |
| 🔹 **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | Tag local AI agents into Slack threads, with local execution, visible progress, approvals, audit trails, and pluggable agent runtimes. | 🟡 Some setup | — | — | 502 🚀 +5/d | **47** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | This repository is YALC 1.0, the first generation and the open-source one. | 🔴 Involved | — | — | 317 | **46** |

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

- Stars: **99,811** (~616.1/day lifetime average)
- Health score: **95/100**
- Documentation score: **92/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code, Codex, OpenCode, Cursor, Copilot, Cline / Roo

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

- Stars: **107,242** (~199.7/day lifetime average)
- Health score: **91/100**
- Documentation score: **69/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Gemini CLI
- *Why it is seeded: Gemini's terminal agent, generous free tier.*

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

- Stars: **212,140** (~404.9/day lifetime average)
- Health score: **90/100**
- Documentation score: **40/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-07
- Works with: OpenCode
- *Why it is seeded: Open-source terminal agent with broad provider support.*

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

- Stars: **149,710** (~253.3/day lifetime average)
- Health score: **90/100**
- Documentation score: **36/100**
- Language: TypeScript
- Last push: 2026-10-07
- Works with: Claude Code
- *Why it is seeded: The reference agentic coding tool.*

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

- Stars: **128,146** (~236.4/day lifetime average)
- Health score: **89/100**
- Documentation score: **37/100**
- License: Apache-2.0
- Language: Rust
- Last push: 2026-10-07
- Works with: Codex, Cursor
- *Why it is seeded: OpenAI's local coding agent.*

</details>

## Skills, Plugins & Prompts

*Teach the agent your workflows.*

A base agent knows nothing about your stack, your review checklist or your deploy process. These packages inject that knowledge as reusable skills, commands, subagents and hooks.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Planning with Files&nbsp;&nbsp;&nbsp; — Multi-agent orchestration | 🟢 Easy | — | — | 27.3k (+99/d) | **85** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | Designed for Claude Code and Cowork. — Usage analytics | 🟢 Easy | — | — | 26.8k (+122/d) | **85** |
| 🏆 **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、… | 🟢 Easy | — | ✅ | 14.9k (+79/d) | **78** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. | 🟡 Some setup | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace | 🟢 Easy | — | — | 1k | **57** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 Turnkey | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Curated by Numman Ali — Multi-agent orchestration | 🟢 Turnkey · OOTB | ✅ | — | 1.1k | **55** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 个人开发的 Claude Code Skills 集合，提供实用的技能工具，助力提升开发效率和内容创作。 | 🟡 Some setup | — | — | 282 | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | A curated collection of official and community-built Claude Skills. | 🟡 Some setup | — | — | 1.1k | **53** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. | 🟢 Turnkey | — | ✅ | 491 | **52** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | Official agent skills/plugins for Power Platform development by Microsoft. | 🟡 Some setup | — | — | 969 | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 Easy | — | — | 1.1k | **50** |
| 🔹 **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | ~100 skills for Claude Code — meeting pipelines, research, image generation, TDD, publishing, personal analytics, and Claude Code ops. | 🟢 Easy | — | — | 389 | **50** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | curl -sSL https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/install.sh \| bash | 🟢 Easy | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. | 🟢 Easy | — | — | 2.6k (+10/d) | **47** |
| 👀 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Rep… | 🔴 Involved | — | — | 777 | **43** |
| 👀 **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | A collection of AI agent skills for Clawdbot, Claude Code, Codex | 🔴 Involved | — | — | 240 | **41** |

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

> Planning with Files&nbsp;&nbsp;&nbsp;

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

- Stars: **27,318** (~98.6/day lifetime average)
- Health score: **85/100**
- Documentation score: **73/100**
- License: MIT
- Language: Shell
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **26,818** (~122.5/day lifetime average)
- Health score: **85/100**
- Documentation score: **56/100**
- License: MIT
- Last push: 2026-09-14
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor

#### [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)

> cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动态 Workflow 编排、模型请求追踪、Computer Use、技能市场、多主题、桌面宠物、H5 远程访问、IM 接入和定时任务，集中在一…

**Core problems it solves**

- **Quota & usage management**
- **Automatic failover** — *图片生成：聊天中直接生成和编辑图片——ChatGPT / Grok 授权登录即可使用，也支持接入任意 OpenAI 兼容的 Images API。*
- **Remote control** — *de Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、Agent Teams 协作工作台、动…*
- **Multi-agent orchestration** — *GitHub Pull Requests License 中文 English Docs 简体中文 · English cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Cla…*
- **Workspace isolation** — *cc-haha 是一个桌面端 Claude Code 工作台：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 / 本地端点）、图片生成、MCP 与 SubAgent 可视化管理、…*
- **Billing & metering**
- **Usage analytics**
- **Session persistence** — */ Agent 定制需求，请联系作者 NanmiCoder。*

**Getting it running**

- Setup: 🟢 **Easy** (friction 29/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: macOS, Windows, Linux
- Easy. configure API key configuration; GUI application

**Facts**

- Stars: **14,892** (~78.8/day lifetime average)
- Health score: **78/100**
- Documentation score: **57/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-05
- Works with: Claude Code, Codex

#### [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)

> A plugin marketplace and discovery platform for Claude Code.

**Core problems it solves**

- **Multi-agent orchestration** — *ations - DevOps, cloud, database optimization*
- **Skills & plugins** — *Plugin Marketplaces from the community*
- **MCP support** — *51 Bundled plugin packages by category*
- **GUI / desktop app** — *he broader Claude Code ecosystem:*
- **Notifications**

**Getting it running**

- Setup: 🟡 **Some setup** (friction 50/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux, Web
- Some setup. needs git clone (build from source); configure database dependency; one-click setup

**Facts**

- Stars: **3,604** (~8.2/day lifetime average)
- Health score: **58/100**
- Documentation score: **63/100**
- License: MIT
- Language: Python
- Last push: 2026-10-06
- Works with: Claude Code

#### [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)

> The best source for Power BI AI skills and agentic development resources in one marketplace

**Core problems it solves**

- **Automatic failover** — *:** glyphs forces an icon set; follow (Follow Claude) decides whether the tree scrolls to what Claude touches; fontHint turns off the one-line instal…*
- **Multi-agent orchestration** — *sts *plugins* that you can install.*
- **Skills & plugins** — *run this in the terminal to get the marketplace:*
- **Agent runtime** — *reports, and the things around them, like workspaces, deployment pipelines, and also processes.*
- **MCP support** — *Agents use the .agent.md extension required by Copilot CLI's documented convention.*
- **Cross-agent support** — *Mentions Claude Code, Copilot*

**Getting it running**

- Setup: 🟢 **Easy** (friction 34/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: macOS, Windows, Linux
- Easy. install via native installer / package; configure config.json/yaml/toml, database migration

**Facts**

- Stars: **1,028** (~3.9/day lifetime average)
- Health score: **57/100**
- Documentation score: **74/100**
- License: GPL-3.0
- Language: C#
- Last push: 2026-10-07
- Works with: Claude Code, Copilot

</details>

## Memory & Context

*Stop re-explaining your project every session.*

Context windows end and sessions reset, so the agent forgets decisions you already made. These tools persist project knowledge across sessions and agents.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | Your coding agent remembers everything. — Automatic failover | 🟢 Easy | — | — | 29.2k (+130/d) | **88** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Your coding agent already has a memory feature. | 🔴 Involved | — | — | 8.9k (+65/d) | **70** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | We rely on free small models that use your CPU. | 🟡 Some setup | — | — | 31.5k (+27/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | sealed_token is a GitHub fine-grained token encrypted against Star History's public key, so only the encrypted value is published here. | 🟢 Easy · OOTB | ✅ | — | 7.1k (+30/d) | **67** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, nev… | 🟢 Turnkey · OOTB | ✅ | — | 3.2k (+25/d) | **67** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | You use Claude every day. — Quota & usage management | 🟢 Easy | — | — | 4.7k (+24/d) | **66** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 Some setup | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. | 🔴 Involved | — | — | 1.2k 🚀 +21/d | **58** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. | 🟡 Some setup | — | — | 2.6k (+10/d) | **57** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Stop re-teaching your agent. — Automatic failover | 🟡 Some setup | — | — | 773 | **56** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — s… | 🟡 Some setup | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | alt="marm-memory - persistent local memory server for AI agents (Model Context Protocol)" | 🟡 Some setup | — | — | 419 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | An AI coding team that remembers your project. | 🟢 Easy | — | — | 215 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | English Version \| 后端测试说明 — Remote control | 🔴 Involved | — | — | 1.4k | **52** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | why agent forget when agent can remember | 🟢 Turnkey · OOTB | ✅ | — | 677 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Cross-model memory for AI agents. — Multi-agent orchestration | 🟡 Some setup | — | — | 219 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | LycheeMemory is a compact memory framework for LLM agents. | 🟡 Some setup | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code is an AI coding workspace for work that lasts longer than one prompt. | 🟡 Some setup | — | — | 436 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM | 🟢 Easy | — | — | 1.1k (+9/d) | **49** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi | 🔴 Involved | — | — | 473 | **49** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into ev… | 🟢 Easy | — | — | 247 | **46** |
| 🔹 **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | Self-growing AI teams in a pixel-art virtual office — powered by local LLMs. | 🔴 Involved | — | — | 323 | **45** |

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

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

- Stars: **29,204** (~130.4/day lifetime average)
- Health score: **88/100**
- Documentation score: **70/100**
- License: Apache-2.0
- Language: TypeScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **8,903** (~64.5/day lifetime average)
- Health score: **70/100**
- Documentation score: **67/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-07
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

- Stars: **31,529** (~27.5/day lifetime average)
- Health score: **69/100**
- Documentation score: **67/100**
- License: Apache-2.0
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Cursor, Cline / Roo

#### [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)

> sealed_token is a GitHub fine-grained token encrypted against Star History's public key, so only the encrypted value is published here.

**Core problems it solves**

- **Session persistence** — *ns, discoveries, accomplished work, next steps, and relevant files.*
- **Memory & context** — *Persistent memory for AI coding agents*
- **Agent runtime** — *Persistent memory for AI coding agents*
- **MCP support** — *ace of a memory in the brain.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 22/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `brew install gentleman-programming/tap/engram`
- Platforms mentioned: Windows, Linux, Web
- Easy. install via Homebrew install; configure database dependency

**Facts**

- Stars: **7,070** (~30.3/day lifetime average)
- Health score: **67/100**
- Documentation score: **54/100**
- License: MIT
- Language: Go
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

#### [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)

> request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it.

**Core problems it solves**

- **Multi-agent orchestration** — *tched tool calls run concurrently in Hermes,*
- **Parallel execution** — *D (live rows with category, turns, cost, cache), the phase todo above the prompt, parallel shot ×N, full-row diff bands, and managed skins — installe…*
- **Workspace isolation**
- **Model / provider routing**
- **Memory & context** — *s such as reconciling a --full install back to core live in*
- **Agent runtime** — *ork run, as it reads in a Slack thread (illustration): one row per lane with its routed category and model, colored by model vendor*
- **Cross-agent support** — *Mentions Claude Code, Codex*

**Getting it running**

- Setup: 🟢 **Turnkey** (friction 13/100)
- Out of the box: **yes**
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/rlaope/oh-my-hermes/main/install.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Turnkey. install via Homebrew install, curl | sh installer; needs npm install/build; configure sign-in required

**Facts**

- Stars: **3,202** (~25.4/day lifetime average)
- Health score: **67/100**
- Documentation score: **65/100**
- License: MIT
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex

</details>

## Observability, Analytics & Cost

*Know where the tokens and the money went.*

Agents spend real money in the background. These tools record sessions, chart usage, attribute cost per project, and surface how much quota is left before it runs out.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | A professional dashboard to track and visualize Claude Code, Cursor, and Codex agent sessions, tool usage, conversation history, cost, and subagent o… | 🟡 Some setup | — | — | 1k | **55** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. | 🟢 Turnkey · OOTB | ✅ | — | 222 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file… | 🟡 Some setup | — | — | 722 | **44** |

<details>
<summary><b>Why these tools — 3 detailed breakdowns</b></summary>

#### [hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)

> A professional dashboard to track and visualize Claude Code, Cursor, and Codex agent sessions, tool usage, conversation history, cost, and subagent orchestration in real time.

**Core problems it solves**

- **Automatic failover** — *terse follow-up never hides the active task.*
- **Remote control** — *, sync manually or on a background poller, and switch the global data scope between local, all sources, or a specific machine, with per-session sourc…*
- **Mobile access** — *tifications arrive even if the browser is closed, as the Service Worker operates in the background.*
- **Multi-agent orchestration** — *g platform for Claude Code, Cursor & Codex agent activity 🚀*
- **Model / provider routing** — *restart The database persists across restarts.*
- **Billing & metering** — *hole session and shows the session total, while a subagent card shows only what that subagent spent, so a subagent card no longer misleadingly reads…*
- **Usage analytics** — *ion flow is based on token usage and model pricing rules.*
- **Session persistence** — *his handles /resume inside a session, Ctrl+C, and other scenarios where a session is orphaned without a clean SessionEnd*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 52/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `docker compose up -d --build`
- Platforms mentioned: macOS, Windows, Linux, iOS, Web
- Some setup. install via npx one-liner, native installer / package; needs docker compose up, git clone (build from source); configure environment variables, config.json/yaml/toml; no-code positioning

**Facts**

- Stars: **1,049** (~4.9/day lifetime average)
- Health score: **55/100**
- Documentation score: **72/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-06
- Works with: Claude Code, Codex, Cursor

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

- Stars: **222** (~0.5/day lifetime average)
- Health score: **50/100**
- Documentation score: **32/100**
- License: MIT
- Language: Rust
- Last push: 2026-10-04
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

- Stars: **722** (~4.2/day lifetime average)
- Health score: **44/100**
- Documentation score: **54/100**
- License: MIT
- Language: Python
- Last push: 2026-04-20
- Works with: Claude Code

</details>

## Sandboxing & Security

*Let it run code without letting it run wild.*

Agents execute arbitrary commands with your credentials. These tools contain the blast radius with containers, permission prompts, secret redaction and audit trails.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Every tool call. — Model / provider routing | 🟡 Some setup | — | — | 503 | **47** |

<details>
<summary><b>Why these tools — 1 detailed breakdowns</b></summary>

#### [Justin0504/Aegis](https://github.com/Justin0504/Aegis)

> Every tool call.

**Core problems it solves**

- **Model / provider routing** — *type, same decision merger, same audit / sink / transparency-log fan-out as built-ins.*
- **Billing & metering**
- **Usage analytics** — *d research assistant, fully integrated with AEGIS.*
- **MCP support** — *, AEGIS provides two proxy modes:*
- **Security & isolation** — *AEGIS is the missing layer: a pre-execution firewall that sits between your agent and its tools, classifies every call in real time, enforces policie…*
- **Self-hostable** — *> Aojie Yuan, Zhiyuan Su, Yue Zhao*
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

- Stars: **503** (~2.3/day lifetime average)
- Health score: **47/100**
- Documentation score: **59/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-06
- Works with: Claude Code

</details>

## Interop & MCP

*Give the agent hands and a common language.*

An agent is only as capable as the tools it can call. MCP servers and interop bridges connect it to browsers, databases, issue trackers and other agents.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| ✅ **[homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** | Using natural language, control smart home devices, query states, execute services and manage your automations. | 🟢 Easy | — | — | 5k (+13/d) | **65** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | 🟢 Turnkey · OOTB | ✅ | — | 6.5k (+11/d) | **63** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Discuss the SDK on Discord — Quota & usage management | 🟡 Some setup | — | — | 9.2k (+13/d) | **59** |
| 🔹 **[microsoft/mcp](https://github.com/microsoft/mcp)** | Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs). | 🟢 Easy | — | — | 3.7k (+7/d) | **59** |
| 🔹 **[opensumi/core](https://github.com/opensumi/core)** | A framework helps you quickly build AI Native IDE products. | 🟢 Easy | — | ✅ | 3.7k | **56** |
| 🔹 **[nanbingxyz/5ire](https://github.com/nanbingxyz/5ire)** | uv (Python package manager) — Usage analytics | 🟢 Easy | — | ✅ | 5.4k (+5/d) | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | Repository containing reference implementations of MCP (Model Context Protocol) servers for managing and interacting with Oracle products. | 🟢 Turnkey | — | — | 454 | **54** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | A Model Context Protocol (MCP) server that gives AI agents full access to your Trello boards — cards, lists, checklists, attachments, comments, custo… | 🟢 Easy | — | — | 445 | **52** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | ⚠️ This project includes production-ready security features but is still under active development. | 🟡 Some setup | — | — | 373 | **52** |
| 🔹 **[aaronsb/obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** | 📦 Available in the Obsidian Community Plugin directory → | 🟡 Some setup | — | — | 463 | **51** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. | 🟡 Some setup | — | — | 398 | **50** |
| 🔹 **[rekog-labs/MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** | A NestJS module to effortlessly expose tools, resources, and prompts for AI, from your NestJS applications using the Model Context Protocol (MCP). | 🟡 Some setup | — | — | 713 | **49** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, template… | 🟢 Easy | — | — | 299 | **49** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Enable your AI agents to read, analyze, and modify Figma designs. | 🟢 Turnkey · OOTB | ✅ | — | 666 | **48** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | I HAVE TAKEN A SMALL BREAK FROM THIS REPO FOR PERSONAL REASONS BUT I WILL BE BACK WITH SOME UPDATES IN THE NEAR FUTURE THANK YOU FOR YOUR UNDERSTANDI… | 🔴 Involved | — | — | 4.3k (+10/d) | **47** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | This repository is essentially an LLM chat desktop application based on MCP. | 🟢 Easy | — | ✅ | 1.2k | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. | 🔴 Involved | — | — | 2.7k | **46** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online | 🔴 Involved | — | — | 411 | **46** |
| 👀 **[r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp)** | Talk to your Strava data using AI. — MCP support | 🟡 Some setup | — | — | 498 | **41** |

<details>
<summary><b>Why these tools — 5 detailed breakdowns</b></summary>

#### [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)

> Using natural language, control smart home devices, query states, execute services and manage your automations.

**Core problems it solves**

- **Skills & plugins** — *atory tool: the catalog always exposes it (it can't be disabled) so tool-only clients never see a silently missing skill surface.*
- **MCP support** — *> Breaking change (v7.3.0): haconfigsetyaml has been moved to beta.*
- **Notifications** — *in the Home Assistant log.*
- **Cross-agent support** — *Mentions Claude Code, Codex, Copilot, Cursor*

**Getting it running**

- Setup: 🟢 **Easy** (friction 22/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -LsSf https://raw.githubusercontent.com/homeassistant-ai/ha-mcp/master/scripts/install-macos.sh | sh`
- Platforms mentioned: macOS, Windows, Linux, Web
- Easy. install via uvx one-liner, curl | sh installer; configure config file, OAuth login flow

**Facts**

- Stars: **4,967** (~12.8/day lifetime average)
- Health score: **65/100**
- Documentation score: **75/100**
- License: MIT
- Language: Python
- Last push: 2026-10-07
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

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

- Stars: **6,464** (~11.2/day lifetime average)
- Health score: **63/100**
- Documentation score: **48/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-10-02
- Works with: Claude Code, Codex, Cursor

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

- Stars: **9,153** (~13.5/day lifetime average)
- Health score: **59/100**
- Documentation score: **58/100**
- License: MIT
- Language: Go
- Last push: 2026-09-23

#### [microsoft/mcp](https://github.com/microsoft/mcp)

> Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to large language models (LLMs).

**Core problems it solves**

- **Skills & plugins** — *om your development environment using tools from the Azure MCP server and extended Azure knowledge skills.*
- **MCP support** — *cations provide context to large language models (LLMs).*
- **Self-hostable**
- **Cross-agent support** — *Mentions Claude Code, Copilot, OpenCode*

**Getting it running**

- Setup: 🟢 **Easy** (friction 36/100)
- Out of the box: no
- Non-programmer friendly: no
- Platforms mentioned: Linux, Web
- Easy. configure database dependency

**Facts**

- Stars: **3,741** (~6.8/day lifetime average)
- Health score: **59/100**
- Documentation score: **60/100**
- License: MIT
- Language: C#
- Last push: 2026-10-07
- Works with: Claude Code, OpenCode, Copilot

#### [opensumi/core](https://github.com/opensumi/core)

> A framework helps you quickly build AI Native IDE products.

**Core problems it solves**

- **MCP support** — *image]: https://flat.badgen.net/github/label-issues/opensumi/core/🤔%20help%20wanted/open*
- **GUI / desktop app** — *s-url] · [Request Feature][github-issues-url] · English · 中文*

**Getting it running**

- Setup: 🟢 **Easy** (friction 32/100)
- Out of the box: no
- Non-programmer friendly: **yes**
- Platforms mentioned: Web
- Easy. needs yarn install/build; GUI application

**Facts**

- Stars: **3,657** (~2.0/day lifetime average)
- Health score: **56/100**
- Documentation score: **51/100**
- License: MIT
- Language: TypeScript
- Last push: 2026-09-29

</details>

## Workflow & Terminal UX

*Small quality-of-life wins, every session.*

Statuslines, notifications, session browsers, prompt managers and review helpers. Individually minor; cumulatively they are the difference between using the agent daily and avoiding it.

| Tool | What it solves | Setup | OOTB | Non-dev | Stars | Score |
| --- | --- | --- | --- | :---: | --- | :---: |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Your AI agent command center — Multi-account switching | 🟡 Some setup | — | — | 1k | **56** |

<details>
<summary><b>Why these tools — 1 detailed breakdowns</b></summary>

#### [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)

> Your AI agent command center

**Core problems it solves**

- **Multi-account switching** — *conductor/group/env chain), so a session can be created straight onto the right login.*
- **Automatic failover** — *ctor's proactive /clear (clearoncompact) only arms on an established window — that variable, or a size the harness reported.*
- **Remote control** — *account, and the session card's*
- **Multi-agent orchestration** — *tion in iTerm2) to bypass it, or use the c / C / V / Y*
- **Parallel execution** — *late to an empty string explicitly disables the segment.*
- **Workspace isolation** — *OpenCode on five more, another agent somewhere in the background? One terminal shows every session — running, waiting, or done — and one keystroke sw…*
- **Model / provider routing** — *makes no network request: it reads the*
- **Usage analytics** — *n five more, another agent somewhere in the background? One terminal shows every session — running, waiting, or done — and one keystroke switches bet…*

**Getting it running**

- Setup: 🟡 **Some setup** (friction 48/100)
- Out of the box: no
- Non-programmer friendly: no
- Quickest install: `curl -fsSL https://raw.githubusercontent.com/asheshgoplani/agent-deck/main/install.sh | bash`
- Platforms mentioned: macOS, Windows, Linux, Web
- Some setup. install via Homebrew install, go install; needs git clone (build from source), npm install/build; configure environment variables, API key configuration; GUI application

**Facts**

- Stars: **1,030** (~3.4/day lifetime average)
- Health score: **56/100**
- Documentation score: **76/100**
- License: MIT
- Language: Go
- Last push: 2026-10-05
- Works with: Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Copilot

</details>

---

## 🪦 The Graveyard

There is always a dark horse. When a newer tool covers **every** capability of an incumbent, matches its traction and is no harder to set up, the incumbent is retired here rather than quietly left in the list. Full rules: [docs/SUPERSEDE.md](docs/SUPERSEDE.md).

### Recorded eliminations

| Retired | Replaced by | Why it lost | Source |
| --- | --- | --- | --- |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.92x the stars (7,070 vs 713) | 🤖 auto (high) |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/agi-is-going-to-arrive/memory-palace)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 93.30x the stars (29,204 vs 313) | 🤖 auto (high) |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 44.12x the stars (33,351 vs 756) | 🤖 auto (high) |
| **[JimLiu/baocut](https://github.com/jimliu/baocut)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 63.05x the stars (33,351 vs 529) | 🤖 auto (high) |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 6.43x the stars (5,667 vs 881) | 🤖 auto (high) |
| **[LerianStudio/ring](https://github.com/lerianstudio/ring)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 125.89x the stars (27,318 vs 217) | 🤖 auto (high) |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/memtensor/memos-cloud-openclaw-plugin)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 79.57x the stars (29,204 vs 367) | 🤖 auto (high) |
| **[RealZST/HarnessKit](https://github.com/realzst/harnesskit)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 73.95x the stars (33,351 vs 451) | 🤖 auto (high) |
| **[anymorph-ai/Claudable](https://github.com/anymorph-ai/claudable)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.23x the stars (33,351 vs 4,052) | 🤖 auto (high) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 218.40x the stars (99,811 vs 457) | 🤖 auto (high) |
| **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 122.50x the stars (27,318 vs 223) | 🤖 auto (high) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 76.95x the stars (27,318 vs 355) | 🤖 auto (high) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.99x the stars (33,351 vs 3,708) | 🤖 auto (high) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 22.49x the stars (5,667 vs 252) | 🤖 auto (high) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 50.65x the stars (14,892 vs 294) | 🤖 auto (high) |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | **[microsoft/mcp](https://github.com/microsoft/mcp)** | 6.99x the stars (3,741 vs 535) | 🤖 auto (high) |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 21.11x the stars (33,351 vs 1,580) | 🤖 auto (high) |
| **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | **[stablyai/orca](https://github.com/stablyai/orca)** | 9.72x the stars (86,867 vs 8,939) | 🤖 auto (high) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 23.13x the stars (8,836 vs 382) | 🤖 auto (high) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 47.80x the stars (29,204 vs 611) | 🤖 auto (high) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 10.61x the stars (5,667 vs 534) | 🤖 auto (high) |
| **[neiii/bridle](https://github.com/neiii/bridle)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 75.80x the stars (33,351 vs 440) | 🤖 auto (high) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 38.58x the stars (29,204 vs 757) | 🤖 auto (high) |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.99x the stars (29,204 vs 1,719) | 🤖 auto (high) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 61.61x the stars (29,204 vs 474) | 🤖 auto (high) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 10.72x the stars (29,204 vs 2,725) | 🤖 auto (high) |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 8.58x the stars (4,691 vs 547) | 🤖 auto (medium) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 50.22x the stars (27,318 vs 544) | 🤖 auto (medium) |
| **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 16.83x the stars (14,892 vs 885) | 🤖 auto (medium) |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 3.87x the stars (1,090 vs 282) | 🤖 auto (high) |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/ccteam-creator)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 4.64x the stars (1,423 vs 307) | 🤖 auto (high) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 230.14x the stars (98,271 vs 427) | 🤖 auto (medium) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.74x the stars (1,423 vs 380) | 🤖 auto (high) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.06x the stars (1,423 vs 465) | 🤖 auto (high) |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.83x the stars (1,423 vs 372) | 🤖 auto (high) |
| **[IBM/mcp](https://github.com/ibm/mcp)** | **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | 1.62x the stars (666 vs 410) | 🤖 auto (high) |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 1.35x the stars (99,811 vs 73,682) | 🤖 auto (medium) |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | magpie covers cc-switch's core job (multi-account / provider switching for Claude Code and Codex) and additionally routes other models through the same agent loop, so it strictly covers the older tool's feature set. | 👤 curated |

### Retired tools

| Tool | Category | Stars | Status | Note |
| --- | --- | --- | --- | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | quota-account-ops | 140.7k | 🔻 Superseded | Still very popular and actively maintained, but magpie covers the same ground plus cross-model routing. Kept in the gra… |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | agent-runtimes | 73.7k | 🔻 Superseded | 1.35x the stars (99,811 vs 73,682) |
| **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | orchestration | 8.9k | 🔻 Superseded | 9.72x the stars (86,867 vs 8,939) |
| **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | agent-runtimes | 4.1k | 🔻 Superseded | 8.23x the stars (33,351 vs 4,052) |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | agent-runtimes | 3.7k | 🔻 Superseded | 8.99x the stars (33,351 vs 3,708) |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | memory-context | 2.7k | 🔻 Superseded | 10.72x the stars (29,204 vs 2,725) |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | memory-context | 1.7k | 🔻 Superseded | 16.99x the stars (29,204 vs 1,719) |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | agent-runtimes | 1.6k | 🔻 Superseded | 21.11x the stars (33,351 vs 1,580) |
| **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | skills-plugins | 885 | 🔻 Superseded | 16.83x the stars (14,892 vs 885) |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | quota-account-ops | 881 | 🔻 Superseded | 6.43x the stars (5,667 vs 881) |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | memory-context | 757 | 🔻 Superseded | 38.58x the stars (29,204 vs 757) |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | agent-runtimes | 756 | 🔻 Superseded | 44.12x the stars (33,351 vs 756) |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | memory-context | 713 | 🔻 Superseded | 9.92x the stars (7,070 vs 713) |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | memory-context | 611 | 🔻 Superseded | 47.80x the stars (29,204 vs 611) |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-context | 547 | 🔻 Superseded | 8.58x the stars (4,691 vs 547) |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | skills-plugins | 544 | 🔻 Superseded | 50.22x the stars (27,318 vs 544) |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | interop-mcp | 535 | 🔻 Superseded | 6.99x the stars (3,741 vs 535) |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | quota-account-ops | 534 | 🔻 Superseded | 10.61x the stars (5,667 vs 534) |
| **[JimLiu/baocut](https://github.com/JimLiu/baocut)** | agent-runtimes | 529 | 🔻 Superseded | 63.05x the stars (33,351 vs 529) |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | memory-context | 474 | 🔻 Superseded | 61.61x the stars (29,204 vs 474) |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | orchestration | 465 | 🔻 Superseded | 3.06x the stars (1,423 vs 465) |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | agent-runtimes | 457 | 🔻 Superseded | 218.40x the stars (99,811 vs 457) |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | agent-runtimes | 451 | 🔻 Superseded | 73.95x the stars (33,351 vs 451) |
| **[neiii/bridle](https://github.com/neiii/bridle)** | agent-runtimes | 440 | 🔻 Superseded | 75.80x the stars (33,351 vs 440) |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | remote-control | 427 | 🔻 Superseded | 230.14x the stars (98,271 vs 427) |
| **[IBM/mcp](https://github.com/IBM/mcp)** | interop-mcp | 410 | 🔻 Superseded | 1.62x the stars (666 vs 410) |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | agent-runtimes | 382 | 🔻 Superseded | 23.13x the stars (8,836 vs 382) |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | orchestration | 380 | 🔻 Superseded | 3.74x the stars (1,423 vs 380) |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | orchestration | 372 | 🔻 Superseded | 3.83x the stars (1,423 vs 372) |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | memory-context | 367 | 🔻 Superseded | 79.57x the stars (29,204 vs 367) |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills-plugins | 355 | 🔻 Superseded | 76.95x the stars (27,318 vs 355) |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | memory-context | 313 | 🔻 Superseded | 93.30x the stars (29,204 vs 313) |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | orchestration | 307 | 🔻 Superseded | 4.64x the stars (1,423 vs 307) |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills-plugins | 294 | 🔻 Superseded | 50.65x the stars (14,892 vs 294) |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills-plugins | 282 | 🔻 Superseded | 3.87x the stars (1,090 vs 282) |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | quota-account-ops | 252 | 🔻 Superseded | 22.49x the stars (5,667 vs 252) |
| **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | skills-plugins | 223 | 🔻 Superseded | 122.50x the stars (27,318 vs 223) |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | skills-plugins | 217 | 🔻 Superseded | 125.89x the stars (27,318 vs 217) |

---

## Contributing

Two ways to help, both described in [CONTRIBUTING.md](CONTRIBUTING.md):

1. **Nominate a tool.** Add it to [`config/seeds.json`](config/seeds.json) with the category you think it belongs to. The next crawl evaluates it against the same gates as everything else.
2. **Challenge a verdict.** If a tool was retired unfairly, or a capability was misdetected, edit [`config/overrides.json`](config/overrides.json) or open an issue quoting the evidence line from the tool's page.

The pipeline runs daily at 04:17 UTC ([workflow](.github/workflows/daily.yml)); every number in this file is regenerated, never hand-edited.

---

<sub>Generated by `agentindex` v1.0.0 on 2026-10-07 14:00 UTC. 108 live tools · 254 candidates rejected by the quality gates.</sub>
