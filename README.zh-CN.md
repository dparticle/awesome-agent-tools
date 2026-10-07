<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**209 个工具**，分 **15 个分类** · **62 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-07 16:31 UTC**

---

## 怎么读这份清单

所有结论都来自对 **README 正文的分析**，而不是仓库简介。各列含义：

| 列 | 含义 |
| --- | --- |
| **上手难度** | 🟢 开箱即用（有安装包或一行命令）· 🟡 需要配置或依赖 · 🔴 需要自行构建/自建服务 |
| **开箱即用** | 装完就能用：不需要从源码构建、不需要起服务、最多改一点配置 |
| **非程序员友好** | 有图形界面或明确的无代码方案，且不需要自己运维服务。✅ 表示非程序员有现实可行路径 |
| **Star** | 总 star 数，括号内是观测到的日均增长。🚀 表示近期涨得很快 |
| **评分** | 0-100 健康分：流行度、增长势头、维护活跃度、文档质量、上手难度。详见[方法论](docs/METHODOLOGY.md) |

---

## MCP与故障转移

*安全与隔离*

Agent 会执行任意代码并持有凭据，必须控制影响范围。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | SpaceXAI's coding agent harness and TUI. | 🟢 开箱即用 | — | — | 27.2k 🚀 +324/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | AGENTS.md at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode; GitHub Copilot uses .github/copilot-instructions.md instead) Available in release 2.2: guided package setup for Claude Code, Codex, and Kimi Code | 🟡 需配置 | — | — | 274.6k (+1048/d) | **89** |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | name: mcp # extra MCP servers next to agentmemory's, same engine | 🟢 较易 | — | — | 29.2k (+130/d) | **88** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | media="(prefers-color-scheme: dark)" srcset="assets/moli-browser-banner-dark.jpg" media="(prefers-color-scheme: light)" srcset="assets/moli-browser-banner.jpg" src="assets/moli-browser-banner.jpg" alt="Moli Browser — Structure first. Extraction-optimized outputs — the CLI directly produces HTML, Markdown, | 🟢 开箱即用 | ✅ | ✅ | 12k 🚀 +206/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Word, Excel, PowerPoint and PDF files, edited by you and your AI, saved back in the real formats. Yours to run. Native apps for macOS, Windows and Linux; files stay on your | 🟢 较易 | — | — | 8.8k 🚀 +130/d | **85** |
| 🏆 **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | Use the ChatGPT Web models available on your account, including Pro, from Codex’s native model picker—with ChatGPT Web’s separate usage limits, without spending your Work or Codex quota. Run Verify runtime to confirm that Codex Native2 is attached and available. | 🟢 较易 | — | — | 13.6k 🚀 +187/d | **84** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | Loopback by default: computers bind to 127.0.0.1 and require a per-container token, so nothing reaches a logged-in browser by knowing its port. The supervisor binds there too, because it ho… Routines: ask a Bot to do something on a schedule and it does, running as you, in the channel you asked in. A 15-minute floor and a cap of 20 enabled routines keep a sentence from schedulin… | 🟡 需配置 | — | — | 6.2k 🚀 +121/d | **83** |
| 🏆 **[spinabot/brigade](https://github.com/spinabot/brigade)** | Connectors: composio (1,000+ apps), oauth_authorize Reuse a CLI login — already signed into the Claude Code or Codex CLI on | 🟡 需配置 | — | — | 11.3k 🚀 +103/d | **80** |
| 🏆 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | Other AI browser agents get captchas. | 🟢 开箱即用 | ✅ | — | 2.6k 🚀 +377/d | **80** |
| 🏆 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | Lulla et al. 2026 — Building Blocks, Adoption, and Impact (this repo is the community reference they reviewed) | 🟢 开箱即用 | ✅ | — | 11.4k 🚀 +95/d | **79** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | Respect limits and access decisions. Workers, Goal/Loop, Compact & Resume and finish checkpoints organize work; they do not grant extra quota or model access and must not be used to evade r… Unsigned beta: Windows is not publisher-signed; macOS is unsigned and unnotarized. Verify the package against the release checksums. Because of that, macOS asks once after each update for y… | 🟢 较易 | ✅ | — | 4.2k 🚀 +92/d | **75** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite is an MCP and agent-first, open-source platform for building and scaling apps. Appwrite Storage - Store files with compression, encryption, image transformations, and access control. | 🟢 较易 | — | — | 57.6k (+21/d) | **70** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | Data visualization Skill for AI Agents, turning data into polished, interactive HTML charts. 面向 AI Agents 的数据… | 🟢 开箱即用 | ✅ | — | 6k 🚀 +72/d | **69** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | Self-Improving Sovereign Agents — voices: @tom_doerr, @AIDailyGems | 🟢 较易 | — | — | 4.7k (+24/d) | **65** |
| ✅ **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg (zvec-grep), powered by zvec, unifies ripgrep, BM25, and vector search behind one local-first interface. It was carnivorous because it climbed the curtain toward a canary's cage | 🟡 需配置 | — | — | 4k 🚀 +45/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. MCP clients: https://github.com/getsentry/xcodebuildmcp.com/blob/main/app/docs/_content/clients.mdx | 🟢 开箱即用 | ✅ | — | 6.5k (+11/d) | **63** |
| 🔹 **[Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith)** | Keysmith 给本机的 AI 编程工具装指令：先预览，再写入，能验证，能撤走。 | 🟡 需配置 | — | — | 4.7k 🚀 +47/d | **61** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | Decay tied with decay switched off. On hippo's synthetic lifecycle test, full@365 minus decay-off is -0.7 points [-1.4, 0.1] on currentR5, no measurable effect. That test runs 20 sessions,… Sequential Learning Benchmark. benchmarks/sequential-learning/. 50 tasks, 10 buried traps. Measures whether agents learn from past mistakes, not just retrieve text. v0.11.0 informal magnitu… | 🟡 需配置 | — | — | 773 | **56** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | alt="marm-memory - persistent local memory server for AI agents (Model Context Protocol)" Concurrent recall: 10 gathered recalls completed in 151.5ms vs 176.0ms serial (gather/serial = 0.86). Do not read that as parallelism: repeated runs of this same benchmark land anywhere fro… | 🟡 需配置 | — | — | 419 | **54** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | Cross-IDE installers. Claude Code, OpenCode, Codex, GitHub Copilot, Augment Code capture observations; Cursor, Gemini CLI, Antigravity, IBM Bob are query-only (MCP search over memory captur… Web viewer. Read-only UI at http://localhost:37777 for browsing sessions in human-readable form. Token-protected: the worker generates a local bearer token on first start and injects it int… | 🟢 开箱即用 | ✅ | — | 677 | **51** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | PAXM carries decisions, conventions, and working context into later Codex, Claude Code, OpenCode, Pi, Cursor, TRAE, Kimi Code, ZCode, Kiro, Cline, and MCP sessions. Write-provider routes default to a 30-second timeout; optional failures remain | 🟡 需配置 | — | — | 422 🚀 +5/d | **49** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | Enable your AI agents to read, analyze, and modify Figma designs. Get document information, current selection, styles | 🟢 开箱即用 | ✅ | — | 666 | **48** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | A collection of Model Context Protocol (MCP) servers, MCP Clients and Developer Tools by IBM. IBM API Connect MCP Server - IBM APIC MCP server exposes API Connect capabilities to your MCP clients and AI Agent workflows. | 🟡 需配置 | — | — | 410 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 📢 Latest Update: This ai-dev branch will be the forward onging dev branch which contains ai agent changes. 🪪 MCP OAuth: Exposed endpoints have options to use standard OAuth in MCP Spec 2025-06-18, easy to connect. | 🔴 较重 | — | — | 2.7k | **46** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | An MCP server backed by the Kagi API. | 🟡 需配置 | — | — | 535 | **40** |

**也能做这件事：** [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[aipoch/open-science](https://github.com/aipoch/open-science)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[topoteretes/cognee](https://github.com/topoteretes/cognee)、[KunAgent/Kun](https://github.com/KunAgent/Kun)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)

## 隔离与并行

*工作区隔离*

并行 Agent 会互相覆盖文件，除非各自有独立工作副本。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow Outbound images/files enforce maxoutboundimagebytes / maxoutboundfilebytes (20 MiB / 50 MiB defaults) while reading, including files that grow after resolution. Oversize reads are rejected… | 🟡 需配置 | — | — | 83.5k (+161/d) | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | ✅ You have 20 simultaneous Claude Code terminals open and lose track of what everyone is doing ✅ You want agents running autonomously 24/7, but still want to audit work and chime in when needed | 🟡 需配置 | — | — | 98.3k (+449/d) | **89** |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | Persistent file-based planning for AI coding agents and long-running tasks. Host capability tiers: hard block on Claude Code, Codex, and Continue; follow-up injection on Cursor, Pi, Kiro, Hermes Agent, and OpenCode; notify-only elsewhere. | 🟢 较易 | — | — | 27.3k (+99/d) | **85** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 🎁 AionUi × Kimi Partnership : Free premium Kimi "Allegretto" plans ($39/mo · ¥199/mo value) for our contributors! Cron expression — standard 5-field cron with timezone support (e.g. 0 9 * * 1, Asia/Shanghai) | 🟢 开箱即用 | — | — | 33.4k (+78/d) | **81** |
| 🏆 **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 图形化管理：界面化增删改 MCP Server，支持 STDIO / Streamable HTTP / SSE 三种传输方式与项目私有、共享、全局三种作用域。 | 🟢 较易 | — | ✅ | 14.9k (+79/d) | **78** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | Paseo is a desktop, mobile, web, and CLI app for coding agents. Cross-device: iOS, Android, desktop, web, and CLI. Start work at your desk, check in from your phone, script it from the terminal. | 🟢 较易 | — | ✅ | 20k (+56/d) | **73** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | Website · Documentation · 中文 | 🟢 开箱即用 | — | — | 5.3k (+38/d) | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | PR checkout — wt switch pr:123 to jump straight to a PR's branch Dev server per worktree — hash_port template filter gives each worktree a unique port | 🟢 开箱即用 | ✅ | — | 8.9k (+25/d) | **68** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | request into a clear capability, a useful next step, and an honest record of what actually happened — strengthening the workflow you already use, never replacing Hermes or hiding a coding executor behind it. Mixture-of-Models Routing — each delegated lane is routed onto a | 🟢 开箱即用 | ✅ | — | 3.2k (+25/d) | **67** |
| ✅ **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | module outlines: 7 of 12 modules with 3+ nodes in view (cap 12; 3 dropped as too thin to read as a region; 2 dropped as enclosing mostly other modules) — three separate truncations, each wi… PageRank is a bad co-change ranker — 3.8% recall@5 against 40.3% for plain lexical, and fusing | 🟢 较易 | — | — | 2.4k 🚀 +35/d | **66** |
| ✅ **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | Professional context and harness engineering around the coding agents you already use. Recover Claude Code and Codex sessions and search source-linked project knowledge. | 🟢 开箱即用 | — | ✅ | 2.1k (+6/d) | **62** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | Cost-Conscious Composition — prompt-cache TTL (5-min default on API keys; 1-hour automatic on Claude subscriptions), 70/20/10 model routing (Haiku/Sonnet/Opus), /cost + /usage monitoring, A… Worktree base ref (v1.9.0; Anthropic Apr 2026) — worktree.baseRef setting controls fresh (default; remote default-branch) vs head (local HEAD) for new worktrees | 🟢 开箱即用 | — | — | 1.6k (+7/d) | **60** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | Command a team of AI agents from one desktop chat — not one chatbot. Go beyond code — video, slides, and more — the Commander drives open-source tools like HyperFrames and hands off to CLI agents — the coding agents Claude Code, Codex and OpenCode, plus the… | 🟡 需配置 | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | Codex forking requires a codex CLI with codex fork support (verified with codex-cli 0.137.0) Nothing is sent until you explicitly type y at the confirmation prompt. Before the prompt, the CLI shows (1) the public URL the comment will land on, (2) that it posts via the gh CLI using… | 🟡 需配置 | — | — | 1k | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | Developers on any OS: Mac, Windows, and Linux are all first-class citizens, with no "Mac-first with a Windows waitlist" Claude Code on Windows is non-functional when your Windows username contains a period — standard in enterprise Active Directory environments. | 🟢 较易 | — | ✅ | 519 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | Each task gets its own git worktree, its own terminal and its own agent — so a dozen of them can run at the same time without ever touching each other's files. Integrate through your agent. Claude Code, Codex & co. already speak MCP to Linear, Jira, | 🟢 开箱即用 | — | — | 307 | **55** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Self-correcting memory + persistent FTS5-indexed wikis + auto-research loop, all on one SQLite store. playwright &mdash; browser automation (most token-efficient) | 🟡 需配置 | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code (command dao) is a terminal-native AI coding assistant: it reads code, writes code, runs commands, and fixes bugs right in your terminal — streaming its reasoning and tool calls while executing safely behind an approval gate, unti… Cost vs Claude Code — pricing the same token trace of these 7 tasks under each vendor's official rates (and crediting Dao Code's high hit rate to Claude too, in its favor), total cost is st… | 🟡 需配置 | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | The structured skill framework for Claude Code: 131 professional skills for deployment, security, databases, content, marketing, and more. TokenStack™ integration: Context compression proxy for token savings | 🟢 较易 | — | — | 423 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | HeyClaude is a file-backed, human-reviewed directory for Claude agents, MCP servers, skills, hooks, commands, tools, prompts, rules, guides, templates, and statuslines. Claude Haiku 45 Speed Optimizer Agent - Agents - An agent pattern for routing rapid-iteration work to Claude Haiku 4.5 — more than twice Sonnet's speed at one-third the cost ($1/$5 per mill… | 🟢 较易 | — | — | 299 | **49** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | Run every AI coding agent in its own git worktree, in parallel. The desktop app embeds its server on 127.0.0.1 with a per-launch token; nothing is exposed to the network. | 🟢 开箱即用 | — | ✅ | 267 | **47** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | A macOS desktop app for running multiple AI agents in parallel. Run separate agent sessions side-by-side, each in its own workspace with an isolated git worktree | 🟢 较易 | — | ✅ | 216 | **38** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)、[hex/claude-council](https://github.com/hex/claude-council)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)、[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 技能

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | English \| 简体中文 \| 日本語 \| 한국어 \| Русский | 🟡 需配置 | — | — | 44.2k (+311/d) | **89** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. | 🟢 较易 | — | — | 157.3k 🚀 +1344/d | **88** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | monetization-strategy — Brainstorm 3–5 monetization strategies with validation experiments market-segments — Identify 3–5 customer segments with demographics, JTBD, and product fit | 🟢 较易 | — | — | 26.8k (+122/d) | **85** |
| 🏆 **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** | Copy/paste into your CLI prompt: | 🟢 较易 | — | — | 54.8k (+375/d) | **84** |
| 🏆 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. One dominant silhouette built from roughly 4–7 large basic shapes | 🟢 开箱即用 | ✅ | — | 5.8k 🚀 +116/d | **78** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | autoharness is a self-learning skill layer for Claude Code. | 🟢 较易 | — | — | 9.2k 🚀 +77/d | **72** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | Your agent writes code, then forgets everything. | 🟢 开箱即用 | ✅ | — | 7.6k (+34/d) | **71** |
| ✅ **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas | 🟡 需配置 | — | — | 7.3k 🚀 +84/d | **66** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | Skills Manager is a modern desktop application designed to solve the fragmentation of AI assistant skills configurations. ⚡ High Performance: Built with Rust and Tauri 2.0 for a lightweight, blazing-fast experience. | 🟢 开箱即用 | ✅ | ✅ | 1k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | A plugin marketplace and discovery platform for Claude Code. Visual Index: Vexilo · A field guide to Claude Code — Interactive index of 31 agents · 99 commands · 123 skills · 13 rules, organized around the 5-step workflow. (companion repo) | 🟡 需配置 | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | The best source for Power BI AI skills and agentic development resources in one marketplace If it still fails, delete the plugin by hand: remove its folder under %USERPROFILE%\.copilot\installed-plugins\ (or %COPILOT_HOME%\installed-plugins\) and restart Copilot CLI. | 🟢 较易 | — | — | 1k | **57** |
| 🔹 **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | Practical AI agent skills for social media research, powered by ScrapeCreators. | 🟢 较易 | ✅ | — | 3.3k (+27/d) | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. | 🟢 较易 | — | — | 2.8k (+8/d) | **56** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | Turn a real workflow into a tested, installable agent skill—then publish it safely to your team. | 🟢 开箱即用 | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | "A skill forgotten is a power lost." — The Code Architect Godot 4.7 Director's Cut: Full library upgrade to Godot 4.7+ — AreaLight3D, HDR output, Asset Store, built-in virtual joystick, and migration digest for 4.6→4.7 projects. | 🟢 较易 | — | — | 804 | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | Abandoned or unmaintained projects Clean, well-documented code | 🟢 开箱即用 | ✅ | — | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | HashiCorp Agent Skills for Terraform and Packer. | 🟢 较易 | ✅ | — | 885 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) | 🟢 较易 | — | — | 342 | **53** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 33 battle-tested skills + minimal .claude harness for any coding agent (Claude Code, Cursor, Codex, Gemini CLI). A wrapper CLI. No daemon, no server, no runtime state. run.sh is 8 lines. | 🟢 较易 | — | — | 756 🚀 +8/d | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. Claude Code. No subagents are used, so this skill runs in a single context. | 🟢 开箱即用 | — | ✅ | 491 | **52** |
| 🔹 **[zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills)** | 引文管理：DOI → BibTeX，文献元数据提取，引文验证 | 🟡 需配置 | — | — | 4.6k (+32/d) | **51** |
| 🔹 **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | An advanced Distributed Automation Platform for high-concurrency account registration and full-lifecycle inventory management. Docker-aware proxy adaptation: Rewrites 127.0.0.1 / localhost to host.docker.internal inside containers when needed. | 🟡 需配置 | — | — | 1.4k (+7/d) | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. | 🟢 较易 | — | — | 1.1k | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | Unified configuration manager for AI coding assistants. Thank you Kai for the help on GitHub Copilot CLI integration | 🟢 较易 | — | — | 440 | **48** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | scripts/extract_frames.py — ffprobe + ffmpeg -q:v 2 extraction with auto-computed scrollBudget (≈26 px per frame, clamped to [2500, 8000]) Auto-routes the layout per archetype: screen-share footage shows the screen content (top 2/3) with rounded speaker PIP at bottom 1/3; full-frame selfie shows the speaker prominently with ca… | 🟢 较易 | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | A collection of AI agent skills focused on resume optimization, job applications, and career development. 75% of resumes rejected by ATS before humans see them | 🟢 较易 | — | — | 2.6k (+10/d) | **47** |
| 🔹 **[JimLiu/baocut](https://github.com/JimLiu/baocut)** | Give your AI coding agent the power to drive BaoCut — transcribe, add and translate subtitles, review speakers, edit timelines and overlays, and export — all from natural language. Codex — reference the baocut skill in your prompt; it drives the baocut CLI. | 🟢 较易 | — | — | 529 🚀 +6/d | **45** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | GRACE means Graph-RAG Anchored Code Engineering: a contract-first AI engineering methodology built around semantic markup, .grace XML artifacts, knowledge-graph navigation, assertions, scopes, and log-driven verification. Location: $XDGCACHEHOME/grace-cli/analysis, falling back to ~/.cache/grace-cli/analysis. Override the base directory with GRACECACHEDIR. | 🟡 需配置 | — | — | 252 | **44** |
| 👀 **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | A curated collection of Claude Code skills for academic research in economics, finance, and the broader social sciences — organized by the common types of skills a researcher needs across a project's lifecycle. excalidraw-diagram-skill-main, diagram-generator-1.1.1 — Diagram creation | 🟡 需配置 | — | — | 223 | **44** |
| 👀 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | Author: Alireza Rezvani Created: September 16, 2025 Updated: December 17, 2025 (v2.7.0 - Tresor Workflow Framework) Quality: 9.7/10 (Exceptional) Repository: https://github.com/alirezarezvani/claude-code-tresor Overall Quality: 9.7/10 (Exceptional - up from 7.1/10 in v2.5.0) | 🔴 较重 | — | — | 777 | **43** |

*还有 1 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [garrytan/gstack](https://github.com/garrytan/gstack)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[google/artemis](https://github.com/google/artemis)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[spinabot/brigade](https://github.com/spinabot/brigade)、[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)、[nexu-io/html-anything](https://github.com/nexu-io/html-anything)、[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)

## 会话与记忆

*会话持久化*

合上笔记本或断网就会中断长时间运行的会话。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 面向心动、暧昧、追求、冲突、分手与复合的 AI 恋爱军师， 结合情绪支持、关系科学、聊天记录分析和长期记忆，把复杂关系变成可执行的下一步。 | 🟢 较易 | — | — | 7.3k 🚀 +92/d | **74** |
| ✅ **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | Awesome Claude Code Skills — Claude Code Skills / Agents / Plugins 精选合集 | 🟡 需配置 | — | — | 12.4k (+94/d) | **72** |
| ✅ **[pacifio/atlas](https://github.com/pacifio/atlas)** | Switching agents loses the thread. Claude Code cannot read Codex's history, and Codex cannot read Claude Code's. Changing agent mid-task means starting the explanation over. Nothing is locked in. Notes are markdown, canvases are JSON, sessions are JSONL, and the editor is a file on disk. Close Atlas and pick up in vim. The one exception is the checkpoint record… | 🟢 较易 | — | — | 9.3k (+64/d) | **72** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | v1.6.0 — Keyless workflows & pipeline reliability (September 18, 2026): build and search text memory with local models and no cloud LLM key; LLM-dependent improvement stages skip when no LL… Run the prebuilt API with Docker Compose or use the deployment templates. | 🟡 需配置 | — | — | 31.5k (+27/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | sealed_token is a GitHub fine-grained token encrypted against Star History's public key, so only the encrypted value is published here. | 🟢 较易 | ✅ | — | 7.1k (+30/d) | **67** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" /> | 🟡 需配置 | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | A persistent, Git-versioned map of your entire codebase — written by your coding agent, governed by a local MCP server. Fault-injection scenarios — 64 scenarios covering cursor tampering, | 🔴 较重 | — | — | 1.2k 🚀 +21/d | **58** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | Conversations with AI agents reset when context windows close. Agent Action Grammar (AAG): Ultra-compact, deterministic ASCII micro-syntax saving ~78–85% tokens compared to natural language prompt instructions. | 🟡 需配置 | — | — | 757 🚀 +24/d | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | Decomposed retrieval evaluation: ARES (NAACL 2024), RAGChecker (2024) Memory and knowledge-base poisoning: AgentPoison (NeurIPS 2024), PoisonedRAG (USENIX Security 2025) | 🟢 较易 | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | A modular Go toolkit for extensible AI applications, long-term memory, provider backends, and local interactive workflows. Delegation — core/delegation: backend-neutral | 🟢 较易 | — | — | 416 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 如果使用 SQLite，系统会在应用迁移之前自动备份你的数据库文件（如 yourdb.db.20260303143000.bak）。 | 🔴 较重 | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | One project memory system for Claude Code, Codex, CodeBuddy Code, Cursor, Windsurf, Copilot, Gemini CLI, OpenCode, Grok Build, OpenClaw, Hermes Agent, Oh-my-Pi, Pi, Kiro, Antigravity, Trae, DeepSeek Harness, WorkBuddy, and any MCP-capable… memorix background start / memorix serve-http run the HTTP service for a shared endpoint, dashboard, VPS Docker deployment, or multiple clients. | 🔴 较重 | — | — | 835 | **52** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | Plugin-first long-term memory for every agent platform. Corrections that stick. Superseding a record retires the old value from recall and from prompt injection, while git keeps the history. | 🟢 较易 | — | ✅ | 547 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | Compress: Chunks are truncated to signatures + docstrings (or LLM-summarized if Ollama is running). | 🟡 需配置 | — | — | 427 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | Runtime-native integration — runtime-specific SKILL.md, shared guide.md, and supported hooks or extensions Built-in deduplication — remember and import skip exact content repeats and preserve distinct facts; similarity suggestions guide review | 🔴 较重 | — | — | 611 | **51** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | Open Second Brain is a memory layer for AI agents that lives in an Obsidian vault. MCP surface. Tools, tool profiles for hosts with tool limits, and the always-loaded writer server: docs/mcp.md. | 🟢 较易 | — | — | 430 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | Intelligent LLM Routing (omega-pro) — Classifies tasks and routes to the optimal model. Coding → Claude Sonnet. Quick edit → Llama 8b at 1/60th the cost. 1M token context → Gemini Flash. 5… Secure Profile (omega-pro) — AES-256 encrypted personal data storage with macOS Keychain integration. | 🟡 需配置 | — | — | 219 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | LycheeMemory is a compact memory framework for LLM agents. GET /mcp exposes the SSE stream used by some MCP clients | 🟡 需配置 | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | Persistent memory + session search + secret scanning for Pi session-start.persistence-sync and session-start.load | 🔴 较重 | — | — | 473 | **49** |
| 🔹 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | Three skills and two hooks that save, search, and restore your conversation context, so you can pick up exactly where you left off. 2026-03-05: api-auth-refactor, JWT + refresh tokens | 🔴 较重 | — | — | 514 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | A local-first memory layer that captures your conversations, builds a searchable knowledge graph, and automatically injects the right context into every new prompt — no cloud, no subscriptions, no re-explaining yourself. Load the extension in Chrome (it talks to http://localhost:3001) | 🟢 较易 | — | — | 247 | **46** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | Internal API: Agent reads Slack and phone links via authenticated Nitro routes | 🔴 较重 | — | — | 474 | **42** |
| 👀 **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | Manages collaboration — agents communicate directly, persist state to files, follow built-in protocols Sets up everything — planning files, docs/ knowledge base, CLAUDE.md operations guide, agent onboarding | 🟡 需配置 | — | — | 307 | **39** |

**也能做这件事：** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)、[garrytan/gstack](https://github.com/garrytan/gstack)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[spinabot/brigade](https://github.com/spinabot/brigade)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)、[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)、[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)、[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

## 桌面端

*Agent 运行时*

它本身就是那个 Agent——你直接运行和对话的东西——而不是挂在别人 Agent 上的插件。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. | 🟢 开箱即用 | ✅ | ✅ | 212.1k (+405/d) | **90** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. | 🟢 开箱即用 | ✅ | — | 149.7k (+253/d) | **90** |
| 🏆 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md · Windows EN | 🟢 开箱即用 | ✅ | ✅ | 14.9k 🚀 +178/d | **85** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | An agent skill for crafting cinematic product videos: 157 shot recipe cards · 214 styles · 214 motion previews · a production-ready template 🌟 2026-08 · 48 new shot recipe cards — the library grows from 104 to | 🟢 开箱即用 | — | ✅ | 10.6k 🚀 +132/d | **85** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | A coding-agent skill that turns your agent into a security auditor. Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps. | 🟢 较易 | ✅ | — | 25.7k 🚀 +231/d | **83** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill connects your AI agent to Chrome or Microsoft Edge, using the accounts you are already signed into. | 🟢 较易 | — | — | 8.3k 🚀 +77/d | **75** |
| ✅ **[nexu-io/html-anything](https://github.com/nexu-io/html-anything)** | The eight skills that surface at the top of the picker's Featured / 推荐 group — sorted by their recommended: rank in SKILL.md frontmatter (lower = higher). alchaincyf/huashu-md-html — the anti-AI-slop discipline that maps into the hard constraints inside every SKILL.md (CJK-first font stack, 8 px baseline grid, contrast ≥ 4.5, must-use-real-da… | 🔴 较重 | — | — | 9k (+61/d) | **69** |
| ✅ **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | Control your coding agents (Claude Code, Codex, Cursor, Devin, Grok, Hermes, Pi, Antigravity) locally by default, with optional multi-device sync. | 🟢 开箱即用 | ✅ | ✅ | 3.1k 🚀 +39/d | **65** |
| ✅ **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Text-to-lottie is an open-source framework for generating production ready Lottie animations with claude code/codex or any other coding agent supporting skills. | 🟢 开箱即用 | ✅ | — | 5.5k (+44/d) | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | Shares policy through git. Commit .cc-safety-net/ so clones and cloud sessions get the same rules. See Team Setup. Embeds in your own tools. Call checkCommand from Node.js without installing the hook. See Library API. | 🟢 开箱即用 | ✅ | ✅ | 1.6k (+6/d) | **60** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO is a lightweight, CLI-first orchestration layer for AI coding agents. | 🟢 开箱即用 | — | — | 530 | **57** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | A free, open-source app to manage all your AI coding agents — desktop, CLI, or web. Cross-agent deployment — See which agents have the extension and which don't — deploy to any missing agent with one click. HarnessKit handles the format differences between agents (JSON, TO… | 🟢 开箱即用 | — | — | 451 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | A persistent memory system for AI coding agents that enables long-term context retention across sessions using local vector database technology. In later sessions, relevant memories are injected into context (see chatMessage / compaction settings). Browse or edit them in the web UI at http://127.0.0.1:4747. | 🔴 较重 | — | — | 1.7k (+6/d) | **55** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | An open, agent-agnostic standard for capturing a project's durable knowledge as plain Markdown — read and written through one small CLI. | 🟢 开箱即用 | ✅ | ✅ | 564 🚀 +5/d | **55** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | Idea or existing code → verified PRD → features → rules → sequenced RFCs → reviewed, tested code The url-shortener example — fresh-context runs that never saw our list of known problems found 12 of 13 cross-document problems (/workflow-status) and 10 of 10 PRD problems (/verify-prd), p… | 🟢 较易 | — | — | 298 | **52** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Evolve — evolutionary program search with a mandatory budget and zero-call resume. | 🟢 较易 | ✅ | — | 687 (+5/d) | **51** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 让 AI 编码助手直接操控编译器、调试器和通信总线，实现从代码生成到硬件验证的完整闭环。 | 🟢 开箱即用 | — | — | 731 | **50** |
| 🔹 **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | Claudable is a powerful Next.js-based web app builder that combines Claude Code's (Cursor CLI also supported!) advanced AI agent capabilities with Lovable's simple and intuitive app building experience. Features: 256K-1M token context, multiple model sizes (0.5B to 480B), Apache 2.0 license | 🟡 需配置 | — | — | 4.1k (+10/d) | **49** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | Does your coding agent spend 5 minutes just grepping around when you give it a complex task? flow.browser_identity: browser-specific identity API behavior. | 🟡 需配置 | — | — | 436 | **47** |
| 👀 **[wong2/diffx](https://github.com/wong2/diffx)** | A local code review tool designed for the coding agent workflow. Comment status tracker — Sidebar widget showing open, replied, and resolved comment counts with click-to-navigate links | 🟢 开箱即用 | ✅ | ✅ | 208 | **42** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[openai/codex](https://github.com/openai/codex)、[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)、[alibaba/open-code-review](https://github.com/alibaba/open-code-review)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[yetone/magpie](https://github.com/yetone/magpie)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)

## 团队

*团队协作*

多人需要共用一套 Agent 环境，还要有角色与边界。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities. 👔 Senior Project Manager - Scope and task planning | 🟢 开箱即用 | — | — | 158.1k (+440/d) | **98** |
| 🏆 **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | Omnigent is an open-source meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, enforce policies and… the native omnigent claude / omnigent codex / omnigent cursor | 🟢 较易 | — | — | 10.6k 🚀 +90/d | **80** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Desktop client — native apps for Windows / macOS / Linux; FnOS packages for NAS Developer boost — delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance. | 🟢 较易 | — | — | 7.6k 🚀 +84/d | **80** |
| 🏆 **[yc-software/qm](https://github.com/yc-software/qm)** | Shared skills. Skills are scope-owned and shareable by grant, with admin-gated Background work. Crons, watches, and inbound webhooks work while you're away. | 🔴 较重 | — | — | 15.4k 🚀 +223/d | **79** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | Your coding agent already has a memory feature. | 🔴 较重 | — | — | 8.9k (+65/d) | **70** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | Linear Chain-of-Thought anchors on whatever it says first. A measured duel vs. single-shot by Shichinomiya (@shichinomiya_s) — independent blind-scored benchmark (2 problems, LLM-as-judge, A/B positions swapped). ADHD won both, with the biggest gai… | 🟢 开箱即用 | ✅ | ✅ | 4.4k (+32/d) | **68** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | Desktop, browser, network, and long-term memory — always on, even when your laptop is closed. UI — A Vue 3 design system for AI agent management interfaces, including a component library, design tokens, and skills that teach agents how to use them. | 🟡 需配置 | — | — | 2.6k (+10/d) | **57** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | A Claude Code plugin that consults multiple AI coding agents in parallel and shows you their answers side-by-side. kimi-cli (Kimi Code CLI, kimi) shadows the kimi API provider, using the kimi CLI's own configured model unless KIMICLIMODEL is set | 🟡 需配置 | — | — | 843 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | aidevops.sh is an OpenCode plugin and AI DevOps framework for carrying work from intent to a verified outcome. 2,060+ production helpers and supporting modules, excluding tests | 🟡 需配置 | — | — | 406 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | Hots are tater-tots now. v1.1.7 called them hots. The first time a newer veil runs while you are logged in Windows. The first time veil binds a port, Windows Defender Firewall pops up *"Allow this app | 🟢 较易 | — | — | 215 | **54** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | Built by world-class engineers, for vibecoders at flowser.ai — AI Agents with computers for GTM It uses the premium AI model only where it matters. Code-writing uses the top model. Planning, research, review, and checking all use a cheaper, faster model. The result: roughly 60–70% low… | 🟢 较易 | — | — | 1.1k (+9/d) | **49** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | Cost Tracking — token usage and USD cost across 40+ models SHA-256 hash-chained — each trace commits to the previous, tamper-evident | 🟡 需配置 | — | — | 503 | **47** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | Dockside is a self-hosted platform for teams who want a devcontainer for every branch — isolated, browser-accessible, HTTPS-secured, and ready in seconds, on your own infrastructure. AI-ready devcontainers: Claude Code, OpenAI Codex, GitHub Copilot and other AI tools and CLIs run natively inside every devcontainer's integrated IDE. Isolate each AI agent session in its o… | 🔴 较重 | — | — | 322 | **47** |

**也能做这件事：** [loopx-project/loopx](https://github.com/loopx-project/loopx)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 账号

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | Lightweight coding agent that runs in your terminal | 🟢 开箱即用 | — | ✅ | 128.1k (+236/d) | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code on Kimi, Codex on DeepSeek, Gemini CLI on GLM, OpenCode on your ChatGPT plan. Share it on your network. Turn on Share on local network, then create a named gateway key for each client, each with its own daily, weekly or monthly token and cost limit. | 🟢 开箱即用 | — | — | 5.7k 🚀 +405/d | **84** |
| 🏆 **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | Two commands, and every one of them runs any LLM you point it at. 28 state-store registrations handle expiry sweeps (60 s interval) and | 🟡 需配置 | — | — | 17k 🚀 +155/d | **83** |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | glm/glm-4.7 (cheap backup, $0.6/1M) glm/glm-5.1 (Cheap backup, $0.6/1M) | 🔴 较重 | — | — | 30.4k (+111/d) | **81** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | Codex API 服务集成 CLIProxyAPI，Codex Live WebRTC/sideband、Responses WebSocket 状态安全、canonical token accounting v2、Multi-Agent V2 兼容、Grok CLI 账号与 OAuth，以及 Grok apply_patch 协议兼容方向亦参考其开源实现：router-f… | 🟢 较易 | — | — | 18.7k (+71/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | codex-auth is a command-line tool for switching Codex accounts. Local-only: With per-command --skip-api, the tool scans local ~/.codex/sessions//rollout-.jsonl files for usage data and skips team name refresh API calls. This mode is safer, but it can be… | 🟢 较易 | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 支持网页端配置全局 HTTP / HTTPS / SOCKS5 / SOCKS5H 代理 | 🔴 较重 | — | — | 6.5k (+38/d) | **56** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多通道概率分摊，基于成本（40%）、余额（30%）、使用率（30%）加权分配 | 🔴 较重 | — | — | 3.3k (+15/d) | **54** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | codex-multi-auth is a multi-account OAuth manager for the official @openai/codex CLI. Account pool — OAuth login for multiple ChatGPT accounts, stored locally under ~/.codex/multi-auth (files 0600, directories 0700), with per-project pools under projects/ /. | 🟡 需配置 | — | ✅ | 534 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | Juggle every Claude Code account from one terminal: switch in a keypress, track live 5h / 7d usage, auto-switch before a limit stops you, even hand a task to another account from inside Claude. 📊 Monitor live 5h / 7d rate-limit bars, a global token dashboard with API-equivalent cost, plus a live Claude status-incident feed | 🟢 较易 | — | — | 271 | **52** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | A Desktop Application for Managing Multiple OpenAI Codex Accounts Easily switch between accounts, monitor usage, schedule warm-ups, and stay in control of your quota Timed – pick specific times of day (e.g. 08:00, 13:00, 18:00) from | 🟢 较易 | — | ✅ | 881 | **51** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | Automatic Token Refresh: Claude Code manages token refresh internally. CAAM cannot refresh Claude tokens—use /login in Claude Code if tokens expire. --max-retries N — Maximum retry attempts on rate limit (default: 1) | 🟡 需配置 | — | — | 208 | **51** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 特别感谢 gylive/ccodex-sleep-state 带来的生命周期管理与状态展示思路参考。 | 🟡 需配置 | — | — | 214 🚀 +11/d | **48** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[stablyai/orca](https://github.com/stablyai/orca)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[gary23w/nl-veil](https://github.com/gary23w/nl-veil)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

## 模型路由

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | Push you to apply below 4.0/5. It will tell you not to. You can override it, and it will say so. Agent: AI coding CLI with shared skills and modes (AGENTS.md + CLI wrapper) | 🟡 需配置 | — | — | 73.7k (+398/d) | **89** |
| 🏆 **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. More coding-agent integrations: Oh My Pi, Antigravity, IBM Bob / Bob Shell, and Kiro join Codex, Claude Code, OpenCode, GitHub Copilot and Cursor. Connect your agent → | 🟡 需配置 | — | — | 17k 🚀 +160/d | **83** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. cron: "23 7 * * 1" # Mondays at 07:23 UTC | 🟡 需配置 | — | — | 11k 🚀 +129/d | **81** |
| 🏆 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 9.3k 🚀 +106/d | **80** |
| 🏆 **[trailhq/Graft](https://github.com/trailhq/Graft)** | You correct it, and by the next session it has forgotten. Entry-point trace — Trace end-to-end what happens when a client creates a record via the REST API, from route handler to database write. | 🟡 需配置 | — | — | 9.7k 🚀 +101/d | **79** |
| ✅ **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. | 🟡 需配置 | — | — | 7.5k 🚀 +373/d | **75** |
| ✅ **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | Cut Claude Code's input tokens by rendering bulky context as images — the same system prompt, tool docs, and history, in a fraction of the tokens. Grok 4.5 / 4.6 (opt-in): native 14px / 84 cols / maxH 512 (100/100 arith, 97/98 gist). | 🟢 较易 | ✅ | — | 7.5k (+54/d) | **71** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang is a method-native AI work system for running complex work from intent to verified delivery. loushang code: a coding-focused CLI and terminal workbench. | 🟢 较易 | — | — | 1.7k (+13/d) | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. | 🟢 开箱即用 | ✅ | — | 342 | **53** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | Evidence-фильтр (фаза 5.5) — CRAG-классификатор keep/drop по паре (тезис, источник) перед синтезом: наивная подача всего найденного снижает качество (Search-o1 33%→24%), в синтез идут тольк… Evidence filter (5.5) — a CRAG-style relevance classifier runs on every (claim, source) pair before synthesis and keeps only the quotes that actually support that specific claim. Dumping ev… | 🟡 需配置 | — | — | 372 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | Review backends: Codex, Copilot, Cursor, Claude and host review, and why the reviewer must come from another family. | 🔴 较重 | — | — | 706 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code is an AI coding workspace for work that lasts longer than one prompt. On the harder tasks, the average fix-to-pass rate rises from 71.8% to 98.4%. | 🟡 需配置 | — | — | 436 | **50** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | Config UI: starting the gateway also starts a local plugin config page for editing plugins.entries.memos-cloud-openclaw-plugin.config Uses Token auth (Authorization: Token ) | 🟢 较易 | — | — | 367 | **47** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[alibaba/open-code-review](https://github.com/alibaba/open-code-review)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[yetone/magpie](https://github.com/yetone/magpie)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)

## 移动端

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place. Account switcher & usage tracking — See Claude and Codex usage and rate-limit resets, and hot-swap accounts without re-logging in. | 🟢 开箱即用 | ✅ | ✅ | 86.9k (+426/d) | **92** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | Cross-App Automation: Executes testing workflows and everyday tasks on Android from natural language instructions. AndroidWorld Results: 99%+ task completion on Google Research's AndroidWorld benchmark (100+ multi-step tasks). | 🟡 需配置 | — | — | 11.1k 🚀 +205/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | A tiny friend that lives in your Mac's notch — or at the top of your screen on Windows and Linux — and keeps an eye on your AI coding agent sessions. 🤖 Claude Code, Cursor, Codex, Gemini CLI, Antigravity, Copilot CLI, Muse Code, OpenCode, Amp and other agents, live — see every session in your notch: what it reads, edits and runs, step by… | 🟢 较易 | — | — | 3.9k 🚀 +436/d | **83** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | End-to-end encrypted mobile app. Left your desk? The same sessions are Natively multiplayer. Invite a colleague or a friend into the session. | 🟢 较易 | ✅ | ✅ | 24k (+54/d) | **71** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | Run Claude Design on your own local agent — Cursor, Claude Code, Claude Desktop, or any file‑capable coding agent. Best with Opus 4.8. The skill is a long, demanding design brief; the stronger the model, the better the result. Pair it with Claude Opus 4.8 for the best output, and it still works well on… | 🟢 开箱即用 | ✅ | — | 4.3k (+35/d) | **67** |
| ✅ **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 📐 3 个画板尺寸:.poster.xhs 1080×1440(小红书 3:4)、.poster.wide 2100×900(公众号 21:9)、.poster.square 1080×1080(公众号 1:1) | 🟢 较易 | — | — | 7.4k (+56/d) | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | A practical, open-source guide to mastering WorkBuddy through real-world workflows.开源的 WorkBuddy 实战蓝皮书：教程、真实工作流、Skills、MCP、自动化与多智能体实践。 | 🟡 需配置 | — | — | 3.3k 🚀 +37/d | **60** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | A professional dashboard to track and visualize Claude Code, Cursor, and Codex agent sessions, tool usage, conversation history, cost, and subagent orchestration in real time. Tray icon — always-on status surface (macOS menu bar / Windows notification area). Left-click toggles the dashboard window; right-click opens a context menu with Open Dashboard, Open in Bro… | 🟡 需配置 | — | — | 1k | **55** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | An open-source terminal coding agent that connects to xAI’s Grok API — real-time X search, web search, the full Grok model lineup, sub-agents on by default, remote control via Telegram (pair once, drive the agent from your phone while the… Try grok-4.20-non-reasoning for non-reasoning workloads | 🟢 较易 | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | Sonnet 4.6 as the new standard — SWE-bench 79.6%, only 1.2pp below Opus 4.6. Gunshi downgraded Opus → Sonnet 4.6. All Ashigaru default to Sonnet 4.6. One YAML line change, no restarts requi… Agent self-watch + escalation (v3.2) — Each agent monitors its own inbox file with inotifywait (zero-polling, instant wake-up). Fallback: tmux send-keys short nudge (text/Enter sent separat… | 🟡 需配置 | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | Managed sessions keep running when the UI disconnects. Your existing agent subscriptions or API keys. | 🟢 较易 | — | — | 547 🚀 +5/d | **51** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[nexu-io/html-anything](https://github.com/nexu-io/html-anything)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)

## 额度

*额度与用量管理*

看不到剩余额度，任务做到一半就被限流。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | 中文 — ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做规划和 Review。本项目把"思考"交给你已付费的网页版 ChatGPT， Codex 只负责执行。不用 API Key、不搞逆向代理——官方网页 + 只读 MCP 桥接。 Knowing the URL grants nothing: the public MCP endpoint requires OAuth 2.1 | 🔴 较重 | — | — | 7.1k 🚀 +177/d | **78** |
| 🏆 **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | An open-source AI agent for social media — discover trends, create content, publish everywhere, and learn what works across Xiaohongshu, Douyin, Zhihu, Bilibili, and more.🎨一个开源的 AI 社交媒体智能体——发现热点趋势、创作内容、一键发布至各大平台，并学习分析哪些内容真正有效，覆盖小红书、抖音、知乎、哔… | 🟢 开箱即用 | — | — | 3.2k 🚀 +80/d | **78** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 一个真正适合职场人的 PPT Skill。把文档丢给你的 AI Agent，每一页都自带编辑控制台的 PPT Skill——不满意的地方直接在浏览器里改，改完还能一键导出成真实的、可编辑的 PPTX。 | 🟢 开箱即用 | ✅ | — | 9.2k 🚀 +77/d | **77** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 让 AI 在真实项目中规划、执行、验证并交付。 | 🟢 较易 | — | ✅ | 6.3k (+45/d) | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 | 🟡 需配置 | — | — | 4.2k 🚀 +68/d | **64** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | orchestrator：Node 26 串行 853 项：852 通过、1 项 Windows ACL 专项跳过；类型检查通过。历史并发测试的等待超时记录仍保留，不以串行结果抹掉。 | 🟢 较易 | — | — | 2.6k 🚀 +28/d | **64** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | Complete*: MCP Go aims to provide a full implementation of the core MCP specification Simple: Build MCP servers with minimal boilerplate | 🟡 需配置 | — | — | 9.2k (+13/d) | **59** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | Agent skills that make AI agents genuinely good at building mobile apps — studied against the top-grossing apps, finished to a simulator-verified bar. | 🟢 较易 | — | — | 2.4k 🚀 +44/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | ✅ 三画幅封面一次出：同一个 coverLayout 出 4:3（1440×1080）／ 3:4（1080×1440）／ 9:16（1080×1920 抖音，内容压在中央安全区），标题 ≤2 行、钩子行自动马克笔高亮 | 🟡 需配置 | — | — | 282 | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis is a free, open-source macOS menu-bar app that reads the session logs your AI coding tools already write to disk and displays your tokens, costs, and subscription quotas. | 🟢 较易 | — | ✅ | 406 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 10-06 系统沙箱：AI 跑的命令和脚本在 macOS、Windows 上读不到 Key 和账本、改不了应用；设置 → 安全 能关，每条多花 7–16 毫秒 | 🟡 需配置 | — | — | 275 🚀 +5/d | **50** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | aaron-he-zhu/seo-geo-claude-skills（Apache-2.0）——backlink/references/ 下的质量评分矩阵、分析模板与外联模板。 | 🟢 较易 | — | — | 208 | **50** |

**也能做这件事：** [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)、[cita-777/metapi](https://github.com/cita-777/metapi)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | Switch API providers in one click and manage MCP, Skills, and Prompts in one place — no more hand-editing JSON / TOML / YAML config files. Notes — Aggregation doesn't provide failover; Claude Code requires version 2.1.243 or later; Codex needs a restart after the aggregated list changes, while Claude Code doesn't. When you swi… | 🟢 较易 | — | — | 140.7k (+328/d) | **93** |
| ✅ **[HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)** | 同花顺金融数据服务（hithink-finance） 是由同花顺官方提供和维护的 A 股金融数据服务，面向 AI Agent、量化研究者和应用开发者。 | 🟢 较易 | — | — | 4.1k 🚀 +34/d | **64** |
| ✅ **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | 管理多个可命名的官方 Codex 登录与第三方 API，一键复制、切换，并从 cc-switch 导入现有供应商 | 🟢 较易 | — | — | 4.1k 🚀 +43/d | **63** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | Claude Code / Codex 项目导入：只读发现项目和历史会话，预览后导入 Harness 工作区；敏感信息脱敏，历史工具调用不会重新执行。 | 🟢 开箱即用 | ✅ | — | 777 🚀 +14/d | **58** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | purple is a free, open-source terminal SSH manager and SSH config editor in Rust for macOS and Linux that keeps ~/.ssh/config in sync with 18 cloud providers, monitors live SSH tunnels and manages Docker and Podman containers fleet-wide. MCP server for AI agents like Claude Code and Cursor, with a read-only mode and a JSON Lines audit log. | 🟢 较易 | — | ✅ | 722 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 内置完整 RAG：文档加载（可选 Tika 解析 PDF/Word/Excel，或 MinerU 云端解析扫描件/公式/复杂版面为 Markdown）、切块、八大向量库适配（Pinecone / Qdrant / pgvector / Milvus / Redis / Elasticsearch / Chroma / InMemory）、混合检索、重排、引用标注，整条链路在… | 🟢 开箱即用 | — | — | 434 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | The Source-Available Agent Control Plane for Governance, Safety, and Trust. Gateway HTTP/SSE mode via /mcp/message and /mcp/sse (when mcp.enabled=true) | 🔴 较重 | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. Daemon (:8081) - registers the machine and manages agent subprocesses. | 🟡 需配置 | — | — | 697 🚀 +6/d | **49** |

**也能做这件事：** [loopx-project/loopx](https://github.com/loopx-project/loopx)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal. 🎯 Free tier: 60 requests/min and 1,000 requests/day with personal Google | 🟢 较易 | — | — | 107.2k (+200/d) | **91** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | AI API Gateway Platform for Subscription Quota Distribution Public Responses targets: /v1/responses, /responses, and /backend-api/codex/responses, forwarded to the Grok subscription proxy for OAuth accounts or https://api.x.ai/v1/responses for API-k… | 🟡 需配置 | — | — | 43.4k (+148/d) | **85** |
| ✅ **[trycompai/crm](https://github.com/trycompai/crm)** | Comp AI CRM is an open source, CRM designed for AI agents. Under Authorised redirect URIs, add http://localhost:3001/api/auth/callback/google. | 🔴 较重 | — | — | 11.1k 🚀 +166/d | **74** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | AI research workbench for reproducible science — open-source, local-first, and model-agnostic. | 🟢 较易 | — | — | 5.4k 🚀 +57/d | **73** |
| 🔹 **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | Butterbase gives you the building blocks for AI-driven applications without lock-in: a Postgres-backed backend with row-level security, serverless functions, an LLM gateway, realtime subscriptions, key-value store, file storage, RAG, durab… Key-Value store — regional, quota-protected KV with TTL, audit trail, and dashboard expose rules (/v1/:app/kv/). *New in v0.2.0. | 🔴 较重 | — | — | 3.7k (+26/d) | **59** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 这是一个运行了一年的 context infrastructure 系统的完整结构。主要价值是作为 reference implementation，让你看到系统长什么样、数据如何流动、记忆如何积累。 | 🟡 需配置 | — | — | 776 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | An MCP server that enables AI assistants like Claude to interact with Odoo ERP systems. 📊 Server-side aggregation — group, sum, and count without pulling raw rows | 🟡 需配置 | — | — | 398 | **50** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication | 🔴 较重 | — | — | 411 | **46** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[decolua/9router](https://github.com/decolua/9router)、[trailhq/Graft](https://github.com/trailhq/Graft)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[cita-777/metapi](https://github.com/cita-777/metapi)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | Independent user · 7 merged PRs. A LoopX-attributed Engine refactor is continue across Codex, Claude Code, direct-model, and other registered Agent | 🟡 需配置 | — | — | 6.2k (+48/d) | **71** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | AgentOps helps developers build, evaluate, and monitor AI agents. Comprehensive Observability: Track your AI agents' performance, user interactions, and API usage. | 🟢 较易 | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | We've released Piebald, the ultimate agentic AI developer experience. Cline / Roo Code / Zoo Code / Kilo Code (VS Code extension + CLI) | 🟢 开箱即用 | ✅ | — | 222 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | A local dashboard that reads the JSONL transcripts Claude Code writes to ~/.claude/projects/ and turns them into per-prompt cost analytics, tool/file heatmaps, subagent attribution, cache analytics, project comparisons, and a rule-based ti… Settings — switch pricing between API / Pro / Max / Max-20x so cost figures everywhere else reflect your actual plan. | 🟡 需配置 | — | — | 722 | **44** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)

## 语音

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | When I heard Karpathy say this, I wanted to find out how. Remote gbrain MCP — your brain runs on another machine (Tailscale, ngrok, internal LAN) or a teammate's server; paste an MCP URL and bearer token. Optionally pair with a local PGLite for sy… | 🟡 需配置 | — | — | 135.6k (+649/d) | **90** |
| 🏆 **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | Cost tiers. OpenAI prices GPT-5.6 prompts above 272K input at 2x input and 1.5x output Controlled long-task cost: routes between standard and flagship models, edits only the required regions, and supports up to 99% same-session and 95% cross-session cache hit rates. | 🟢 较易 | — | — | 13.6k 🚀 +114/d | **84** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | Tickets with keys (0.5.3): every card gets a key like V53-299, each agent has a Tasks tab with what it did and when, and the Tasks screen filters by date. Local transcription and dictation (0.5.3): dictate into any app (Option on the Mac, | 🟢 较易 | — | — | 8.5k (+66/d) | **75** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[pax-beehive/paxm](https://github.com/pax-beehive/paxm)

## 共享

*配额共享与分发*

订阅容量超过个人所需，想安全地分给他人共用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 🤖 Agent-native, model-agnostic. We don't ship an agent. The claude / codex / cursor-agent / copilot / hermes / kimi already on your PATH are the design engine. Swap with one click. Hand off to engineering. The artifact is real HTML/CSS — drop it into Cursor, Codex, or Claude Code to keep building as code. Or export PPTX / PDF / MP4 straight to marketing. | 🟢 较易 | — | — | 99.8k (+616/d) | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 2.5-Flash: gemini-2.0-flash, gemini-2.5-flash, gemini-2.5-flash-lite Set start command: uvicorn src.proxy_app.main:app --host 0.0.0.0 --port $PORT | 🔴 较重 | — | — | 556 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api is a self-hosted AI API gateway and subscription management platform based on Sub2API. Merged upstream sub2api v0.2.4 (519 commits / 876 files) and unified the frontend and backend versions at 1.0.4. | 🔴 较重 | — | — | 241 | **42** |

**也能做这件事：** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[decolua/9router](https://github.com/decolua/9router)、[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 62% | 0.04x the stars (5,667 vs 140,685) |

<details><summary><b>yetone/magpie 对比 farion1231/cc-switch</b></summary>

Both manage multiple accounts and providers for Claude Code and Codex, and magpie additionally routes other models through the same agent loop.

**未覆盖：** 计费与计量、并行执行、多供应商聚合、会话持久化、技能与插件

</details>

---

## 🪦 淘汰区

永远会有黑马出现。当新工具**完整覆盖**了旧工具的所有能力、热度不输、上手难度也不更高时，旧工具就会被移到这里，而不是悄悄留在推荐列表里。完整规则见 [docs/SUPERSEDE.md](docs/SUPERSEDE.md)。

### 已记录的取代关系

| 被淘汰 | 取代者 | 落败原因 | 来源 |
| --- | --- | --- | --- |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.92x the stars (7,070 vs 713) | 🤖 自动（high） |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/agi-is-going-to-arrive/memory-palace)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 93.30x the stars (29,204 vs 313) | 🤖 自动（high） |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 57.16x the stars (18,691 vs 327) | 🤖 自动（high） |
| **[AndrewDryga/emisar](https://github.com/andrewdryga/emisar)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 13.92x the stars (4,691 vs 337) | 🤖 自动（high） |
| **[Arvincreator/project-golem](https://github.com/arvincreator/project-golem)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 45.70x the stars (29,204 vs 639) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 6.36x the stars (2,417 vs 380) | 🤖 自动（high） |
| **[LerianStudio/ring](https://github.com/lerianstudio/ring)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 11.14x the stars (2,417 vs 217) | 🤖 自动（high） |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[pacifio/atlas](https://github.com/pacifio/atlas)** | 17.99x the stars (9,263 vs 515) | 🤖 自动（high） |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 866.27x the stars (274,608 vs 317) | 🤖 自动（high） |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 63.85x the stars (274,608 vs 4,301) | 🤖 自动（high） |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 61.75x the stars (274,608 vs 4,447) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.17x the stars (33,351 vs 922) | 🤖 自动（high） |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 58.10x the stars (33,351 vs 574) | 🤖 自动（high） |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 96.67x the stars (33,351 vs 345) | 🤖 自动（high） |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 5.92x the stars (29,204 vs 4,930) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 20.09x the stars (98,271 vs 4,891) | 🤖 自动（high） |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 65.63x the stars (29,204 vs 445) | 🤖 自动（high） |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.97x the stars (13,603 vs 389) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 23.62x the stars (7,628 vs 323) | 🤖 自动（high） |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 6.05x the stars (7,628 vs 1,261) | 🤖 自动（high） |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 22.49x the stars (5,667 vs 252) | 🤖 自动（high） |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1144.20x the stars (274,608 vs 240) | 🤖 自动（high） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 24.26x the stars (11,280 vs 465) | 🤖 自动（high） |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 574.96x the stars (158,113 vs 275) | 🤖 自动（high） |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.16x the stars (33,351 vs 273) | 🤖 自动（high） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 58.18x the stars (29,204 vs 502) | 🤖 自动（high） |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 23.13x the stars (8,836 vs 382) | 🤖 自动（high） |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 26.49x the stars (33,351 vs 1,259) | 🤖 自动（high） |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | 8.66x the stars (2,417 vs 279) | 🤖 自动（high） |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 78.29x the stars (29,204 vs 373) | 🤖 自动（high） |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 143.56x the stars (140,685 vs 980) | 🤖 自动（high） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[EverMind-AI/Raven](https://github.com/evermind-ai/raven)** | 9.66x the stars (5,257 vs 544) | 🤖 自动（high） |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 399.14x the stars (274,608 vs 688) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[FrancyJGLisboa/agent-skills-platform](https://github.com/francyjglisboa/agent-skills-platform)** | 8.17x the stars (2,403 vs 294) | 🤖 自动（high） |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[trailhq/Graft](https://github.com/trailhq/graft)** | 21.14x the stars (9,660 vs 457) | 🤖 自动（medium） |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 41.31x the stars (98,271 vs 2,379) | 🤖 自动（medium） |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 17.48x the stars (29,204 vs 1,671) | 🤖 自动（medium） |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[trailhq/Graft](https://github.com/trailhq/graft)** | 15.51x the stars (9,660 vs 623) | 🤖 自动（medium） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.80x the stars (7,628 vs 2,725) | 🤖 自动（high） |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 9.02x the stars (2,083 vs 231) | 🤖 自动（high） |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 6.90x the stars (44,160 vs 6,400) | 🤖 自动（medium） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 452.40x the stars (274,608 vs 607) | 🤖 自动（medium） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.85x the stars (804 vs 282) | 🤖 自动（high） |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 10.33x the stars (4,691 vs 454) | 🤖 自动（medium） |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 579.34x the stars (274,608 vs 474) | 🤖 自动（medium） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.69x the stars (7,628 vs 2,066) | 🤖 自动（high） |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 103.93x the stars (29,204 vs 281) | 🤖 自动（medium） |
| **[AI-QL/tuui](https://github.com/ai-ql/tuui)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 25.28x the stars (29,204 vs 1,155) | 🤖 自动（medium） |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 6.87x the stars (274,608 vs 39,997) | 🤖 自动（medium） |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.70x the stars (33,351 vs 3,833) | 🤖 自动（high） |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.06x the stars (7,628 vs 3,708) | 🤖 自动（medium） |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/fuxi)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 8.72x the stars (29,204 vs 3,351) | 🤖 自动（medium） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 4.90x the stars (29,204 vs 5,955) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.26x the stars (804 vs 355) | 🤖 自动（high） |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 2.86x the stars (14,892 vs 5,208) | 🤖 自动（medium） |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 6.26x the stars (29,204 vs 4,667) | 🤖 自动（medium） |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/gd-agentic-skills)** | 2.63x the stars (804 vs 306) | 🤖 自动（high） |
| **[MoonshotAI/kimi-code](https://github.com/moonshotai/kimi-code)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 4.28x the stars (33,351 vs 7,789) | 🤖 自动（high） |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.33x the stars (1,423 vs 427) | 🤖 自动（medium） |
| **[yetone/cumora](https://github.com/yetone/cumora)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 2.70x the stars (10,643 vs 3,939) | 🤖 自动（high） |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.47x the stars (1,423 vs 969) | 🤖 自动（medium） |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 1.31x the stars (1,423 vs 1,090) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | mcp-failover | 40k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | isolation-parallelism | 7.8k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.4k | 🔻 已被取代 | 已被 alibaba/open-code-review 取代：covers 100% of capabilities (4/4)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | mcp-failover | 6k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | isolation-parallelism | 5.2k | 🔻 已被取代 | 已被 NanmiCoder/cc-haha 取代：covers 100% of capabilities (6/6)。 |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | mcp-failover | 4.9k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (7/7)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-parallelism | 4.9k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | mcp-failover | 4.7k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | mcp-failover | 4.4k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | mcp-failover | 4.3k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[yetone/cumora](https://github.com/yetone/cumora)** | teams | 3.9k | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (9/9)。 |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | isolation-parallelism | 3.8k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | mcp-failover | 3.4k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | isolation-parallelism | 2.4k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | mcp-failover | 1.7k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | isolation-parallelism | 1.3k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | mcp-failover | 1.2k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | mobile | 1.1k | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (11/11)。 |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers | 980 | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (5/5)。 |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile | 969 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-parallelism | 922 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | sessions-memory | 713 | 🔻 已被取代 | 已被 Gentleman-Programming/engram 取代：covers 100% of capabilities (5/5)。 |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | mcp-failover | 688 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | mcp-failover | 639 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 623 | 🔻 已被取代 | 已被 trailhq/Graft 取代：covers 100% of capabilities (4/4)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | mcp-failover | 607 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | isolation-parallelism | 574 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-parallelism | 544 | 🔻 已被取代 | 已被 EverMind-AI/Raven 取代：covers 100% of capabilities (4/4)。 |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | sessions-memory | 515 | 🔻 已被取代 | 已被 pacifio/atlas 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-failover | 502 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | mcp-failover | 474 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | mcp-failover | 465 | 🔻 已被取代 | 已被 spinabot/brigade 取代：covers 100% of capabilities (4/4)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 457 | 🔻 已被取代 | 已被 trailhq/Graft 取代：covers 100% of capabilities (4/4)。 |
| **[oracle/mcp](https://github.com/oracle/mcp)** | mcp-failover | 454 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | mcp-failover | 445 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 427 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (5/5)。 |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice | 389 | 🔻 已被取代 | 已被 XiaomiMiMo/MiMo-Code 取代：covers 100% of capabilities (7/7)。 |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | mcp-failover | 382 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-parallelism | 380 | 🔻 已被取代 | 已被 redhat-et/ripwire 取代：covers 100% of capabilities (5/5)。 |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | mcp-failover | 373 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 355 | 🔻 已被取代 | 已被 thedivergentai/GD-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | isolation-parallelism | 345 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | mcp-failover | 337 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | accounts | 327 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 323 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | mcp-failover | 317 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | mcp-failover | 313 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (9/9)。 |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | skills | 306 | 🔻 已被取代 | 已被 thedivergentai/GD-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills | 294 | 🔻 已被取代 | 已被 FrancyJGLisboa/agent-skills-platform 取代：covers 100% of capabilities (4/4)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 已被取代 | 已被 thedivergentai/GD-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | mcp-failover | 281 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (6/6)。 |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | isolation-parallelism | 279 | 🔻 已被取代 | 已被 redhat-et/ripwire 取代：covers 100% of capabilities (6/6)。 |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 275 | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (6/6)。 |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | isolation-parallelism | 273 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | accounts | 252 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (5/5)。 |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | mcp-failover | 240 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (8/8)。 |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | isolation-parallelism | 231 | 🔻 已被取代 | 已被 maxritter/pilot-shell 取代：covers 100% of capabilities (6/6)。 |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | isolation-parallelism | 217 | 🔻 已被取代 | 已被 redhat-et/ripwire 取代：covers 100% of capabilities (5/5)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-07 16:31 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
