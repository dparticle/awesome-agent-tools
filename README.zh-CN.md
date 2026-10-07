<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**209 个工具**，分 **15 个分类** · **62 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-07 17:48 UTC**

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

**关于「解决什么问题」这一列：** 尽量用中文说明。来源分三档，标记不同，可信度也不同：

| 标记 | 来源 | 数量 |
| --- | --- | ---: |
| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | 25 |
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 171 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 12 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 安全与自托管

*安全与隔离*

Agent 会执行任意代码并持有凭据，必须控制影响范围。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 274.6k (+1048/d) | **89** |
| 🏆 **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.2k 🚀 +324/d | **88** |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 29.2k (+130/d) | **88** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 12k 🚀 +206/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 8.8k 🚀 +130/d | **85** |
| 🏆 **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 13.6k 🚀 +187/d | **84** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | 自动故障转移、手机端访问、模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 6.2k 🚀 +121/d | **83** |
| 🏆 **[spinabot/brigade](https://github.com/spinabot/brigade)** | 记忆与上下文、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.3k 🚀 +103/d | **80** |
| 🏆 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | 跨 Agent 支持、图形界面与桌面端、会话持久化；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟢 开箱即用 | ✅ | — | 2.6k 🚀 +377/d | **80** |
| 🏆 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 11.4k 🚀 +95/d | **79** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | 自动故障转移、图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 4.2k 🚀 +92/d | **75** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | Appwrite 是面向 MCP 与智能体的开源平台，用于构建和扩展应用。 MCP 已包含在内，编程智能体可以直接操作线上的 Appwrite 项目。 | 🟢 较易 | — | — | 57.6k (+21/d) | **70** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6k 🚀 +72/d | **69** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 跨 Agent 支持、技能与插件、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.7k (+24/d) | **65** |
| ✅ **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 4k 🚀 +45/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k (+11/d) | **63** |
| 🔹 **[Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.7k 🚀 +47/d | **61** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 跨 Agent 支持、Agent 运行时、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 773 | **56** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | 跨 Agent 支持、记忆与上下文、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 419 | **54** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、记忆与上下文、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 677 | **51** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 422 🚀 +5/d | **49** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | 跨 Agent 支持、Agent 运行时、并行执行；兼容 Claude Code、Cursor、Copilot、Cline / Roo。 ‡ | 🟢 开箱即用 | ✅ | — | 666 | **48** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时、多智能体编排。 ‡ | 🟡 需配置 | — | — | 410 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | API 网关与中转、图形界面与桌面端、多智能体编排；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 2.7k | **46** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 535 | **40** |

**也能做这件事：** [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[aipoch/open-science](https://github.com/aipoch/open-science)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[topoteretes/cognee](https://github.com/topoteretes/cognee)、[KunAgent/Kun](https://github.com/KunAgent/Kun)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)

## 隔离与并行

*工作区隔离*

并行 Agent 会互相覆盖文件，除非各自有独立工作副本。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | MCP 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 83.5k (+161/d) | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 98.3k (+449/d) | **89** |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.3k (+99/d) | **85** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 33.4k (+78/d) | **81** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、MCP 支持、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 14.9k (+78/d) | **77** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 20k (+56/d) | **73** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | 多智能体编排、跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 5.3k (+38/d) | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 8.9k (+25/d) | **68** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | 中的普通请求，转化为合适的能力、明确的下一步，以及对“已经发生”和“尚未发生”的诚实状态。 | 🟢 开箱即用 | ✅ | — | 3.2k (+25/d) | **67** |
| ✅ **[redhat-et/ripwire](https://github.com/redhat-et/ripwire)** | MCP 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 2.4k 🚀 +35/d | **66** |
| ✅ **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | ✅ | 2.1k (+6/d) | **62** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | — | 1.6k (+7/d) | **60** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | 在一个桌面对话里指挥一支 AI 智能体团队 —— 而不是单个聊天机器人。 不止于代码 —— 视频、幻灯片等 —— 指挥官可驱动 HyperFrames 等开源工具，并把任务交接给 CLI 智能体——编程智能体 Claude Code、Codex、OpenCode，以及个人智能体 OpenClaw、Hermes-Agent——及其他本地智能体，于是一个对话就能产出代码、研究、视频与幻灯片。 | 🟡 需配置 | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | MCP 支持、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1k | **56** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 519 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 307 | **55** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 423 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 299 | **49** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | ✅ | 267 | **47** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | 图形界面与桌面端。 ‡ | 🟢 较易 | — | ✅ | 216 | **38** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)、[hex/claude-council](https://github.com/hex/claude-council)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)、[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 技能

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 44.2k (+311/d) | **89** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 157.3k 🚀 +1344/d | **88** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 跨 Agent 支持、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 26.8k (+122/d) | **85** |
| 🏆 **[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)** | A skill to stop your coding agent from burying the answer. ADHD-friendly output. † | 🟢 较易 | — | — | 54.8k (+375/d) | **84** |
| 🏆 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Agent 运行时；兼容 Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 5.8k 🚀 +116/d | **78** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 9.2k 🚀 +77/d | **72** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 7.6k (+34/d) | **71** |
| ✅ **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Keeps the callable Skill name gc-minimal-zine-poster-v0-3 for backward compatibility. a default 3:5 aged-paper canvas † | 🟡 需配置 | — | — | 7.3k 🚀 +84/d | **66** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | MCP 支持、图形界面与桌面端；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1k | **57** |
| 🔹 **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | ✅ | — | 3.3k (+27/d) | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.8k (+8/d) | **56** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[thedivergentai/GD-Agentic-Skills](https://github.com/thedivergentai/GD-Agentic-Skills)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 804 | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 885 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | Destructive-command blockers (conserve, hookify) † | 🟢 较易 | — | — | 342 | **53** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 756 🚀 +8/d | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. † | 🟢 开箱即用 | — | ✅ | 491 | **52** |
| 🔹 **[zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.6k (+32/d) | **51** |
| 🔹 **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | 安全与隔离；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 1.4k (+7/d) | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. † | 🟢 较易 | — | — | 1.1k | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、OpenCode、Copilot、Goose。 ‡ | 🟢 较易 | — | — | 440 | **48** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Agent 运行时、跨 Agent 支持、MCP 支持；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 2.6k (+10/d) | **47** |
| 🔹 **[JimLiu/baocut](https://github.com/JimLiu/baocut)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 529 🚀 +6/d | **45** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | 记忆与上下文；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 252 | **44** |
| 👀 **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 223 | **44** |
| 👀 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | 多账号切换、团队协作；兼容 Claude Code、Droid。 ‡ | 🔴 较重 | — | — | 777 | **43** |

*还有 1 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [garrytan/gstack](https://github.com/garrytan/gstack)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[google/artemis](https://github.com/google/artemis)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[spinabot/brigade](https://github.com/spinabot/brigade)、[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)、[nexu-io/html-anything](https://github.com/nexu-io/html-anything)、[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)

## 用量分析

*会话持久化*

合上笔记本或断网就会中断长时间运行的会话。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 7.3k 🚀 +92/d | **74** |
| ✅ **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 12.4k (+94/d) | **72** |
| ✅ **[pacifio/atlas](https://github.com/pacifio/atlas)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 9.3k (+63/d) | **72** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 31.5k (+27/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | ✅ | — | 7.1k (+30/d) | **67** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 1.2k 🚀 +21/d | **58** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 757 🚀 +24/d | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | MCP 支持、技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 416 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | MCP 支持、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 835 | **52** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | 确定性召回。 相关度 × 时间衰减 × 重要度，全部在本地计算。检索自己的记忆不需要模型调用、不需要网络、不需要 API key。 内置 prompt 注入。 在 OpenClaw 上，伴生插件会在每一轮对话前注入一份紧凑索引，让 agent 开口时就已经知道它知道什么。 | 🟢 较易 | — | ✅ | 547 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 427 | **52** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | 跨 Agent 支持、多智能体编排、API 网关与中转；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 611 | **51** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 430 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 219 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | MCP 支持、远程控制、API 网关与中转；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | 自动故障转移、模型与供应商路由、技能与插件。 ‡ | 🔴 较重 | — | — | 473 | **49** |
| 🔹 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、自动故障转移；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 514 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 247 | **46** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | MCP 支持、图形界面与桌面端、通知提醒。 ‡ | 🔴 较重 | — | — | 474 | **42** |
| 👀 **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | Skill 文件未变 → 直接用缓存的 prompt 生成 agent，跳过重新读取所有 skill 参考文件（~2500 行 → ~200 行） 先沟通 — 介绍团队机制，了解项目需求，推荐团队配置 | 🟡 需配置 | — | — | 307 | **39** |

**也能做这件事：** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)、[garrytan/gstack](https://github.com/garrytan/gstack)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[spinabot/brigade](https://github.com/spinabot/brigade)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)、[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)、[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)、[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

## 运行时与桌面端

*Agent 运行时*

它本身就是那个 Agent——你直接运行和对话的东西——而不是挂在别人 Agent 上的插件。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | 多智能体编排；兼容 OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 212.1k (+405/d) | **90** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 149.7k (+253/d) | **90** |
| 🏆 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | CDP binds 127.0.0.1 only, but it has no authentication; another process on the same computer may still connect and inspect or control the renderer. Mac: macos/README.md · Windows: windows/README.md ·… † | 🟢 开箱即用 | ✅ | ✅ | 14.9k 🚀 +178/d | **85** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | ✅ | 10.6k 🚀 +132/d | **85** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 多智能体编排、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 25.7k 🚀 +231/d | **83** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 8.3k 🚀 +77/d | **75** |
| ✅ **[nexu-io/html-anything](https://github.com/nexu-io/html-anything)** | 跨 Agent 支持、计费与计量、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 9k (+61/d) | **69** |
| ✅ **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 3.1k 🚀 +39/d | **65** |
| ✅ **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 5.5k (+44/d) | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 1.6k (+6/d) | **60** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 530 | **57** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 451 | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 记忆与上下文、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.7k (+6/d) | **55** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 564 🚀 +5/d | **55** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | 想法或现有代码 → 经过验证的 PRD → 功能 → 规则 → 有序的 RFC → 经过评审和测试的代码 | 🟢 较易 | — | — | 298 | **52** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | MCP 支持。 ‡ | 🟢 较易 | ✅ | — | 687 (+5/d) | **51** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 731 | **50** |
| 🔹 **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Cursor、Qwen Code。 ‡ | 🟡 需配置 | — | — | 4.1k (+10/d) | **49** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | 跨 Agent 支持、记忆与上下文、可自托管；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 436 | **47** |
| 👀 **[wong2/diffx](https://github.com/wong2/diffx)** | A local code review tool designed for the coding agent workflow. Comment status tracker — Sidebar widget showing open, replied, and resolved comment counts with click-to-navigate links † | 🟢 开箱即用 | ✅ | ✅ | 208 | **42** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[openai/codex](https://github.com/openai/codex)、[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)、[alibaba/open-code-review](https://github.com/alibaba/open-code-review)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[yetone/magpie](https://github.com/yetone/magpie)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)

## 团队

*团队协作*

多人需要共用一套 Agent 环境，还要有角色与边界。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 158.1k (+440/d) | **98** |
| 🏆 **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 图形界面与桌面端、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 10.6k 🚀 +90/d | **80** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | 图形界面与桌面端、记忆与上下文、可自托管；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 7.6k 🚀 +84/d | **80** |
| 🏆 **[yc-software/qm](https://github.com/yc-software/qm)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.4k 🚀 +223/d | **79** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 8.9k (+65/d) | **70** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | 跨 Agent 支持、Agent 运行时、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 4.4k (+32/d) | **68** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.6k (+10/d) | **57** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 跨 Agent 支持、自动故障转移、MCP 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 843 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | 工作区隔离、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 406 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | 图形界面与桌面端、记忆与上下文、MCP 支持；兼容 Cursor。 ‡ | 🟢 较易 | — | — | 215 | **54** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.1k (+9/d) | **49** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 安全与隔离、图形界面与桌面端、MCP 支持；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 503 | **47** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、远程控制、工作区隔离；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 322 | **47** |

**也能做这件事：** [loopx-project/loopx](https://github.com/loopx-project/loopx)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 账号

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 128.1k (+236/d) | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | — | 5.7k 🚀 +405/d | **84** |
| 🏆 **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17k 🚀 +155/d | **83** |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 30.4k (+111/d) | **81** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 图形界面与桌面端、跨 Agent 支持、并行执行；兼容 Codex、OpenCode、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 18.7k (+71/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.5k (+38/d) | **56** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k (+15/d) | **54** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | 跨 Agent 支持、API 网关与中转；兼容 Codex、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 534 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 271 | **52** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 881 | **51** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | 跨 Agent 支持、MCP 支持、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 208 | **51** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | API 网关与中转、技能与插件、模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 214 🚀 +11/d | **48** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[stablyai/orca](https://github.com/stablyai/orca)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[gary23w/nl-veil](https://github.com/gary23w/nl-veil)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

## 模型路由

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 73.7k (+398/d) | **89** |
| 🏆 **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17k 🚀 +160/d | **83** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. † | 🟡 需配置 | — | — | 11k 🚀 +129/d | **81** |
| 🏆 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 9.3k 🚀 +106/d | **80** |
| 🏆 **[trailhq/Graft](https://github.com/trailhq/Graft)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 9.7k 🚀 +101/d | **79** |
| ✅ **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 自动故障转移、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 7.5k 🚀 +373/d | **75** |
| ✅ **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 7.5k (+54/d) | **71** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟢 较易 | — | — | 1.7k (+13/d) | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. † | 🟢 开箱即用 | ✅ | — | 342 | **53** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | 多智能体编排、技能与插件、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 372 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 706 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code 是一个面向长期任务的 AI 编程工作区。 你可以让它改一个小地方，在任务运行中随时补充指令，把一场迁移交给带客观完成判据的目标回路，或者召集多位专家共同审阅一项决策——无论哪种，工作都会在多轮对话、进程重启、工具调用、团队成员和不同项目之间保持连贯。 | 🟡 需配置 | — | — | 436 | **50** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | 多智能体编排、记忆与上下文、自动故障转移。 ‡ | 🟢 较易 | — | — | 367 | **47** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[alibaba/open-code-review](https://github.com/alibaba/open-code-review)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[yetone/magpie](https://github.com/yetone/magpie)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)

## 移动端

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 86.9k (+426/d) | **92** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 11.1k 🚀 +205/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 跨 Agent 支持、图形界面与桌面端、安全与隔离；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.9k 🚀 +436/d | **83** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | ✅ | 24k (+54/d) | **71** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | 跨 Agent 支持、技能与插件、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 开箱即用 | ✅ | — | 4.3k (+35/d) | **67** |
| ✅ **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 7.4k (+56/d) | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | 记忆与上下文。 ‡ | 🟡 需配置 | — | — | 3.3k 🚀 +37/d | **60** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 专业的 Dashboard，用于实时追踪和可视化 Claude Code、Cursor 与 Codex Agent 会话、工具使用、对话历史、成本和子 Agent 编排。 基于 Node.js、Express、React 和 SQLite，结合原生 Hook 与按提供方识别的本地 transcript 发现。 | 🟡 需配置 | — | — | 1k | **55** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 547 🚀 +5/d | **51** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[nexu-io/html-anything](https://github.com/nexu-io/html-anything)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)

## 额度

*额度与用量管理*

看不到剩余额度，任务做到一半就被限流。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | MCP 支持、Agent 运行时、技能与插件；兼容 Codex。 ‡ | 🔴 较重 | — | — | 7.1k 🚀 +177/d | **78** |
| 🏆 **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | API 网关与中转、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 3.2k 🚀 +80/d | **78** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 9.2k 🚀 +77/d | **77** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 跨 Agent 支持、图形界面与桌面端、安全与隔离；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | ✅ | 6.3k (+45/d) | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 跨 Agent 支持、Agent 运行时、技能与插件；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.2k 🚀 +68/d | **64** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 2.6k 🚀 +28/d | **64** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | MCP 支持、通知提醒、并行执行。 ‡ | 🟡 需配置 | — | — | 9.2k (+13/d) | **59** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、手机端访问；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 2.4k 🚀 +44/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 282 | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 406 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 计费与计量、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 275 🚀 +5/d | **50** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 计费与计量、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 208 | **50** |

**也能做这件事：** [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)、[cita-777/metapi](https://github.com/cita-777/metapi)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 140.7k (+328/d) | **93** |
| ✅ **[HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API)** | MCP 支持、额度与用量管理、会话持久化；兼容 Cursor。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +34/d | **64** |
| ✅ **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +43/d | **63** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 777 🚀 +14/d | **58** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 722 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 434 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、多智能体编排；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 697 🚀 +6/d | **49** |

**也能做这件事：** [loopx-project/loopx](https://github.com/loopx-project/loopx)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | 技能与插件、模型与供应商路由、会话持久化；兼容 Gemini CLI。 ‡ | 🟢 较易 | — | — | 107.2k (+199/d) | **91** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 43.4k (+148/d) | **85** |
| ✅ **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、可自托管。 ‡ | 🔴 较重 | — | — | 11.1k 🚀 +166/d | **74** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 跨 Agent 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 5.4k 🚀 +57/d | **73** |
| 🔹 **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | 可自托管、记忆与上下文、通知提醒；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 3.7k (+26/d) | **59** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 776 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | 跨 Agent 支持、工作区隔离、自动故障转移；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 398 | **50** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | A comprehensive Model Context Protocol (MCP) server for QuickBooks Online OAuth 2.0 Authentication - Secure token-based authentication † | 🔴 较重 | — | — | 411 | **46** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[decolua/9router](https://github.com/decolua/9router)、[trailhq/Graft](https://github.com/trailhq/Graft)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[cita-777/metapi](https://github.com/cita-777/metapi)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | 跨 Agent 支持、多智能体编排、额度与用量管理；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 6.2k (+48/d) | **71** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排、可自托管。 ‡ | 🟢 较易 | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 222 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | 自动故障转移、多智能体编排、并行执行；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 722 | **44** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)

## 语音

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、技能与插件、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 135.6k (+649/d) | **90** |
| 🏆 **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | 记忆与上下文、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 13.6k 🚀 +114/d | **84** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | 跨 Agent 支持、图形界面与桌面端、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 8.5k (+66/d) | **75** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[pax-beehive/paxm](https://github.com/pax-beehive/paxm)

## 共享

*配额共享与分发*

订阅容量超过个人所需，想安全地分给他人共用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 99.8k (+616/d) | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、模型与供应商路由；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 556 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api 是基于 Sub2API 二次开发的自托管 AI API 网关与订阅管理平台，提供账号池、API Key 管理、多供应商请求转发、用量计费、订阅充值、风控审查和后台运营能力。 | 🔴 较重 | — | — | 241 | **42** |

**也能做这件事：** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[decolua/9router](https://github.com/decolua/9router)、[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 62% | star 数为 0.04 倍（5,667 vs 140,685） |

<details><summary><b>yetone/magpie 对比 farion1231/cc-switch</b></summary>

两者都为 Claude Code 和 Codex 管理多账号与多供应商，而 magpie 还能让其他模型走同一套 Agent 流程。

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
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | security-self-hosting | 40k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | isolation-parallelism | 7.8k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.4k | 🔻 已被取代 | 已被 alibaba/open-code-review 取代：covers 100% of capabilities (4/4)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | security-self-hosting | 6k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | isolation-parallelism | 5.2k | 🔻 已被取代 | 已被 NanmiCoder/cc-haha 取代：covers 100% of capabilities (6/6)。 |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | security-self-hosting | 4.9k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (7/7)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-parallelism | 4.9k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | security-self-hosting | 4.7k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | security-self-hosting | 4.4k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | security-self-hosting | 4.3k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[yetone/cumora](https://github.com/yetone/cumora)** | teams | 3.9k | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (9/9)。 |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | isolation-parallelism | 3.8k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | security-self-hosting | 3.4k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | isolation-parallelism | 2.4k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | security-self-hosting | 1.7k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | isolation-parallelism | 1.3k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | security-self-hosting | 1.2k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | mobile | 1.1k | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (11/11)。 |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers | 980 | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (5/5)。 |
| **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | mobile | 969 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-parallelism | 922 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | analytics | 713 | 🔻 已被取代 | 已被 Gentleman-Programming/engram 取代：covers 100% of capabilities (5/5)。 |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | security-self-hosting | 688 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | security-self-hosting | 639 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 623 | 🔻 已被取代 | 已被 trailhq/Graft 取代：covers 100% of capabilities (4/4)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | security-self-hosting | 607 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | isolation-parallelism | 574 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-parallelism | 544 | 🔻 已被取代 | 已被 EverMind-AI/Raven 取代：covers 100% of capabilities (4/4)。 |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | analytics | 515 | 🔻 已被取代 | 已被 pacifio/atlas 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security-self-hosting | 502 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | security-self-hosting | 474 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | security-self-hosting | 465 | 🔻 已被取代 | 已被 spinabot/brigade 取代：covers 100% of capabilities (4/4)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 457 | 🔻 已被取代 | 已被 trailhq/Graft 取代：covers 100% of capabilities (4/4)。 |
| **[oracle/mcp](https://github.com/oracle/mcp)** | security-self-hosting | 454 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | security-self-hosting | 445 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 427 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (5/5)。 |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice | 389 | 🔻 已被取代 | 已被 XiaomiMiMo/MiMo-Code 取代：covers 100% of capabilities (7/7)。 |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | security-self-hosting | 382 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-parallelism | 380 | 🔻 已被取代 | 已被 redhat-et/ripwire 取代：covers 100% of capabilities (5/5)。 |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | security-self-hosting | 373 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 355 | 🔻 已被取代 | 已被 thedivergentai/GD-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | isolation-parallelism | 345 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | security-self-hosting | 337 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | accounts | 327 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 323 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | security-self-hosting | 317 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | security-self-hosting | 313 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (9/9)。 |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | skills | 306 | 🔻 已被取代 | 已被 thedivergentai/GD-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills | 294 | 🔻 已被取代 | 已被 FrancyJGLisboa/agent-skills-platform 取代：covers 100% of capabilities (4/4)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 已被取代 | 已被 thedivergentai/GD-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | security-self-hosting | 281 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (6/6)。 |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | isolation-parallelism | 279 | 🔻 已被取代 | 已被 redhat-et/ripwire 取代：covers 100% of capabilities (6/6)。 |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 275 | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (6/6)。 |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | isolation-parallelism | 273 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | accounts | 252 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (5/5)。 |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | security-self-hosting | 240 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (8/8)。 |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | isolation-parallelism | 231 | 🔻 已被取代 | 已被 maxritter/pilot-shell 取代：covers 100% of capabilities (6/6)。 |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | isolation-parallelism | 217 | 🔻 已被取代 | 已被 redhat-et/ripwire 取代：covers 100% of capabilities (5/5)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-07 17:48 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
