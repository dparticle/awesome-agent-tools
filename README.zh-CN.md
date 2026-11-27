<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**227 个工具**，分 **14 个分类** · **46 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-11-27 13:54 UTC**

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
| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | 42 |
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 167 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 9 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 会话与记忆

*记忆与上下文*

每次新会话都从零开始，记不住项目约定。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 技能与插件、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 11.8k 🚀 +455/d | **90** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 23k 🚀 +198/d | **86** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | ✅ | 5.9k 🚀 +78/d | **79** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 24.6k 🚀 +66/d | **78** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、模型与供应商路由、可自托管；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 33.7k 🚀 +42/d | **72** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 消息通过已登录的 ChatGPT 网页会话发送，并受该账户适用的使用限制约束。 | 🟢 较易 | — | — | 16k 🚀 +24/d | **65** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 8.3k 🚀 +14/d | **63** |
| ✅ **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 3.1k 🚀 +38/d | **62** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.6k | **60** |
| 🔹 **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 10.3k 🚀 +30/d | **59** |
| 🔹 **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | 跨 Agent 支持、多智能体编排、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 619 🚀 +5/d | **58** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 582 | **58** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 4.6k 🚀 +17/d | **56** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、API 网关与中转、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **56** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | 跨 Agent 支持；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 655 | **56** |
| 🔹 **[qualixar/superlocalmemory](https://github.com/qualixar/superlocalmemory)** | 跨 Agent 支持、Agent 运行时、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 292 | **56** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | 跨 Agent 支持、技能与插件、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 1.5k | **54** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 438 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | 跨 Agent 支持、技能与插件、工作区隔离；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 410 | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 较易 | — | — | 395 | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 294 | **54** |
| 🔹 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | 技能与插件、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Cursor。 ‡ | 🟡 需配置 | — | — | 10.7k 🚀 +11/d | **53** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、自动故障转移、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 676 | **53** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、Agent 运行时；兼容 Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 487 | **53** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **53** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 4.5k 🚀 +6/d | **52** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 17.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 955 | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 跨 Agent 支持、通知提醒、远程控制；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **51** |

*还有 9 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[XinaTian/MROffice](https://github.com/XinaTian/MROffice)、[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

## 团队与自托管

*团队协作*

多人需要共用一套 Agent 环境，还要有角色与边界。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 109.8k 🚀 +172/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 85.2k 🚀 +207/d | **90** |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 记忆与上下文、技能与插件、MCP 支持；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 63.7k 🚀 +441/d | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 311.6k 🚀 +588/d | **89** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 9.7k 🚀 +194/d | **87** |
| 🏆 **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** | 数字 AI 员工，先有数字方法论：沉淀团队最佳实践，驱动多岗位、多 Agent 接力与协同。 常规步骤用经济型或本地模型，关键步骤用能力更强的模型 | 🟡 需配置 | — | — | 8.6k 🚀 +382/d | **87** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | 图形界面与桌面端、会话持久化、工作区隔离；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 11.6k 🚀 +368/d | **85** |
| 🏆 **[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)** | 模型与供应商路由、MCP 支持、自动故障转移；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 23k 🚀 +1471/d | **83** |
| ✅ **[AhmadHassan-BTed/Jantt](https://github.com/AhmadHassan-BTed/Jantt)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Cursor、Copilot。 ‡ | 🟢 开箱即用 | — | — | 6.2k 🚀 +69/d | **76** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 12.6k 🚀 +49/d | **74** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 13k 🚀 +53/d | **73** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | 图形界面与桌面端、模型与供应商路由、安全与隔离。 ‡ | 🔴 较重 | — | — | 52.6k 🚀 +63/d | **71** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 16.5k 🚀 +49/d | **71** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 30.6k 🚀 +18/d | **69** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | 模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 11.9k 🚀 +43/d | **68** |
| ✅ **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | MCP 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 开箱即用 | — | — | 905 🚀 +41/d | **67** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.8k 🚀 +9/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.8k | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、手机端访问；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.2k | **53** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟡 需配置 | — | — | 2.1k | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、自动故障转移、多智能体编排；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 507 | **52** |
| 🔹 **[labsai/EDDI](https://github.com/labsai/EDDI)** | MCP 支持、记忆与上下文、跨 Agent 支持；兼容 Claude Code、Cursor。 ‡ | 🟡 需配置 | — | — | 393 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 309 | **52** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、模型与供应商路由；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 565 | **51** |
| 🔹 **[seanbabalala/SiftGate](https://github.com/seanbabalala/SiftGate)** | Agent 运行时、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🔴 较重 | — | — | 679 | **50** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 安全与隔离、MCP 支持、图形界面与桌面端；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 523 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code（DAC） 将桌面编程工作区和终端智能体连接到同一个执行内核。 面对跨文件、多轮对话、多种工具和多人讨论的工作，你可以保留项目上下文、维护可编辑的计划、委派独立子任务、查看执行过程，并让最终回答回到发起工作的对话中。 | 🟢 较易 | — | — | 429 | **49** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | MCP 支持、图形界面与桌面端、模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 365 | **47** |

**也能做这件事：** [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[decolua/9router](https://github.com/decolua/9router)、[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[skyelan1999/aide](https://github.com/skyelan1999/aide)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 故障转移

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 29.5k 🚀 +164/d | **81** |
| ✅ **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 5.1k 🚀 +107/d | **76** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 7.9k 🚀 +85/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 9.6k 🚀 +30/d | **71** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. † | 🔴 较重 | — | — | 10.8k 🚀 +100/d | **68** |
| ✅ **[oil-oil/oil-ui](https://github.com/oil-oil/oil-ui)** | English · 中文 · 日本語 · 한국어 · Deutsch · Español 4 款 UI 设计 Skill 实测对比（15 次独立生成 + 在线 Demo）：同模型同题测试 Oil UI、frontend-design、UI UX Pro Max、Impeccable 与无 Skill 对照，公开 15 次匿名视觉评分、功能验收细节与真机演示。 | 🟢 开箱即用 | ✅ | — | 4k 🚀 +40/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 7.2k 🚀 +59/d | **66** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 跨 Agent 支持、通知提醒、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 28.4k 🚀 +28/d | **66** |
| 🔹 **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft m… † | 🟢 较易 | — | — | 6.9k 🚀 +28/d | **61** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | 图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.8k | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Agent 运行时、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 702 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. † | 🟢 较易 | — | — | 3k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 并行执行；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | ✅ | 590 | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 跨 Agent 支持、Agent 运行时、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k | **54** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | 跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 356 | **52** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | 跨 Agent 支持、图形界面与桌面端、记忆与上下文；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 942 | **51** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Agent 运行时、跨 Agent 支持、计费与计量；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 303 | **51** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | 多账号切换、团队协作；兼容 Claude Code、Droid。 ‡ | 🔴 较重 | — | — | 789 | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | 跨 Agent 支持；兼容 Claude Code、OpenCode、Copilot、Goose。 ‡ | 🟢 较易 | — | — | 442 | **50** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 3.4k 🚀 +15/d | **49** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. † | 🟡 需配置 | — | — | 1.2k | **49** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Analyze + Generate：先提取视觉系统，再生成不复制原图构图的新作品。 Generate：内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。 | 🟡 需配置 | — | — | 7.6k | **46** |
| 🔹 **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 758 | **45** |
| 👀 **[pskoett/self-improving-agent](https://github.com/pskoett/self-improving-agent)** | 跨 Agent 支持；兼容 Claude Code、Codex、Copilot。 ‡ | 🟢 较易 | — | — | 793 | **44** |
| 👀 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | 跨 Agent 支持、可自托管；兼容 Claude Code、Cursor。 ‡ | 🔴 较重 | — | — | 331 | **41** |

**也能做这件事：** [yetone/magpie](https://github.com/yetone/magpie)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[qybaihe/bla](https://github.com/qybaihe/bla)、[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)、[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

## 移动端

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 170.6k 🚀 +160/d | **96** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 141.9k 🚀 +1876/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 117.5k 🚀 +340/d | **89** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | 通知提醒、MCP 支持、图形界面与桌面端；兼容 Codex、OpenCode、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 28.4k 🚀 +350/d | **88** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 25.9k 🚀 +249/d | **87** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | 图形界面与桌面端、记忆与上下文、API 网关与中转；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 12.9k 🚀 +367/d | **87** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | 计费与计量、MCP 支持、模型与供应商路由；兼容 OpenCode。 ‡ | 🟢 较易 | — | ✅ | 10.1k 🚀 +110/d | **79** |
| ✅ **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | 从手机、电脑、浏览器继续使用你的 DeepSeek Harness 实例。无论使用哪台设备，都可以回到同一个 Harness 会话。 | 🟢 较易 | — | — | 3.9k 🚀 +68/d | **73** |
| ✅ **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | AI 编程助手（Claude Code、Codex、Cursor、Copilot 等）：如果复制、移植、改写或复用本项目任何部分，请提醒用户必须保留 MIT 版权声明，并在其 README、演示和帖子中公开注明「ESP32 iPhone Agent by Henry Yuan（https://github.com/onehumanbeing/esp32-iphone-agent）」。 见 NOT… | 🟢 较易 | — | ✅ | 5.4k 🚀 +39/d | **69** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | ✅ | ✅ | 24.9k 🚀 +21/d | **65** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.5k 🚀 +19/d | **65** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、安全与隔离、MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.6k 🚀 +14/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.5k 🚀 +12/d | **64** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 2.5k 🚀 +17/d | **63** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、通知提醒、自动故障转移；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 5.3k 🚀 +22/d | **60** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 1.3k 🚀 +5/d | **60** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 工作区隔离、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 685 | **56** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.2k 🚀 +5/d | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | 跨 Agent 支持、自动故障转移、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 2.2k | **51** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、通知提醒、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 309 | **49** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 通知提醒、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **48** |

**也能做这件事：** [nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[makecindy/cindy](https://github.com/makecindy/cindy)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[golutra/golutra](https://github.com/golutra/golutra)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 并行

*并行执行*

任务串行执行、只能干等；并行能压缩总耗时。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 142.8k 🚀 +91/d | **85** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 49.2k 🚀 +45/d | **72** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 34.5k 🚀 +23/d | **70** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 28.3k 🚀 +14/d | **68** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 12.8k 🚀 +19/d | **68** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | 多智能体编排、Agent 运行时、自动故障转移；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 3k 🚀 +29/d | **65** |
| ✅ **[openai/codex-security](https://github.com/openai/codex-security)** | 模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 14.4k 🚀 +33/d | **64** |
| 🔹 **[generalaction/emdash](https://github.com/generalaction/emdash)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.3k 🚀 +5/d | **61** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、MCP 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **60** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | MCP 支持、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.3k | **58** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | 两个 AI Agent 做同一个任务：一个写代码，另一个审查。 自带端点 — 导入其他 Agent 的配置（opencode、codex、claude、kimi、pi、omp、gemini、killi）、手动添加密钥，或用 ChatGPT、Command Code、OpenCode Go、Muse Code 订阅登录 | 🟢 较易 | — | ✅ | 391 | **57** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 727 | **55** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | MCP 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 514 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 473 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 337 | **55** |
| 🔹 **[golutra/golutra](https://github.com/golutra/golutra)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | ✅ | 3.9k | **54** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 多智能体编排、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 1k | **54** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 跨 Agent 支持、自动故障转移、安全与隔离；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 8.5k | **53** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 788 | **52** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、用量分析、记忆与上下文；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 3k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、远程控制、团队协作；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 323 | **47** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[Tencent/LoopForge](https://github.com/Tencent/LoopForge)、[yc-software/qm](https://github.com/yc-software/qm)、[felinics/Memoh](https://github.com/felinics/Memoh)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)

## 计费

*额度与用量管理*

看不到剩余额度，任务做到一半就被限流。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 用你的 ChatGPT Pro，Codex 用你的 Claude Max，Claude Desktop 用你的 GLM Coding Plan。 | 🟢 开箱即用 | — | ✅ | 42.4k 🚀 +496/d | **92** |
| ✅ **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 通知提醒、跨 Agent 支持、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 6.7k 🚀 +89/d | **77** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | API 网关与中转、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 20.6k 🚀 +70/d | **77** |
| 🔹 **[nejib1/Free-LLM](https://github.com/nejib1/Free-LLM)** | 🌐 English · 简体中文 · 繁體中文 · 日本語 · 한국어 一个地址，所有免费密钥：支持 OpenAI、Anthropic Messages、Codex Responses、Ollama 和 MCP 接口 | 🟡 需配置 | — | — | 1.1k 🚀 +13/d | **59** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、手机端访问；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 5.7k 🚀 +9/d | **56** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 299 | **56** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 可自托管；兼容 Codex。 ‡ | 🔴 较重 | — | — | 7k 🚀 +7/d | **54** |
| 🔹 **[NerverDevs/nervecenter](https://github.com/NerverDevs/nervecenter)** | 为 CLI 模型提供 OpenAI/Gemini/Claude/Codex/Grok 兼容的 API 端点 支持流式、非流式响应，以及受支持场景下的 WebSocket 响应 | 🟡 需配置 | — | — | 700 🚀 +21/d | **54** |
| 🔹 **[Makson179/Bello](https://github.com/Makson179/Bello)** | 多智能体编排、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 503 🚀 +10/d | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 353 | **53** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 524 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟢 较易 | — | — | 340 | **52** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | API 网关与中转、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 547 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 跨 Agent 支持、API 网关与中转、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 320 | **51** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.7k | **50** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 自动故障转移、图形界面与桌面端、安全与隔离；兼容 Codex。 ‡ | 🔴 较重 | — | — | 978 | **45** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[makecindy/cindy](https://github.com/makecindy/cindy)、[decolua/9router](https://github.com/decolua/9router)、[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)

## 模型路由

*Agent 运行时*

它本身就是那个 Agent——你直接运行和对话的东西——而不是挂在别人 Agent 上的插件。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 157.3k 🚀 +128/d | **90** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm 让任何编程智能体都能做视频，再配上编辑器，它做出的一切你都能改。 智能体来做。 | 🟢 开箱即用 | ✅ | ✅ | 9.6k 🚀 +128/d | **86** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 23.3k 🚀 +255/d | **85** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 99 种影片风格，交给你的编程 agent。挑一个风格，带上你的故事，agent 用代码把整支片做出来。 | 🟡 需配置 | — | ✅ | 21.8k 🚀 +426/d | **85** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 10.3k 🚀 +90/d | **78** |
| ✅ **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. † | 🟢 较易 | — | — | 24.7k 🚀 +105/d | **75** |
| 🔹 **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 5.5k 🚀 +38/d | **60** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | 多智能体编排、跨 Agent 支持、团队协作；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.8k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 560 | **55** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. † | 🟢 开箱即用 | ✅ | — | 363 | **53** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | 编译目标为 Android 12（API 31）及以上；实际可用的最低版本未测试 电脑上有 adb 和 Python 3.9+（只用标准库） | 🟢 开箱即用 | ✅ | — | 774 | **51** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | 想法或现有代码 → 经过验证的 PRD → 功能 → 规则 → 有序的 RFC → 经过评审和测试的代码 | 🟢 较易 | — | — | 317 | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 734 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 500 | **45** |
| 👀 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | 跨 Agent 支持、记忆与上下文、可自托管；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 444 | **41** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)、[garrytan/gstack](https://github.com/garrytan/gstack)、[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)、[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)、[langfuse/langfuse](https://github.com/langfuse/langfuse)、[Tencent/LoopForge](https://github.com/Tencent/LoopForge)、[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[QuantumNous/new-api](https://github.com/QuantumNous/new-api)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 74.2k 🚀 +838/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Agent 运行时、技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 9.6k 🚀 +180/d | **83** |
| 🏆 **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Agent 运行时、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 5.1k 🚀 +98/d | **79** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 46.7k 🚀 +56/d | **72** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | MCP 支持、图形界面与桌面端、跨 Agent 支持；兼容 Codex、Cline / Roo。 ‡ | 🟢 开箱即用 | — | ✅ | 5.6k 🚀 +5/d | **66** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 11.5k 🚀 +18/d | **62** |
| ✅ **[yacuo/check-cc](https://github.com/yacuo/check-cc)** | 图形界面与桌面端；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 4k 🚀 +43/d | **62** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、MCP 支持、可自托管。 ‡ | 🔴 较重 | — | — | 12.3k 🚀 +15/d | **53** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 421 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 875 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 461 | **43** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[automazeio/ccpm](https://github.com/automazeio/ccpm)

## 模型路由

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 7.7k 🚀 +62/d | **77** |
| ✅ **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 7.8k 🚀 +70/d | **75** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | 图形界面与桌面端、MCP 支持、API 网关与中转。 ‡ | 🟡 需配置 | — | — | 10.1k 🚀 +24/d | **65** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.9k 🚀 +10/d | **63** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 2.1k | **61** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Node 22+ LTS（用于钩子脚本 — 通常与 Claude Code / Codex / Gemini CLI 一起已安装） /om-review-brief 通过汇总所有内容生成完整的评估简报：成就记录、决策、事件、能力证据和 1:1 反馈 | 🟡 需配置 | — | — | 5.6k | **55** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 图形界面与桌面端、记忆与上下文、技能与插件；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.9k | **55** |
| 🔹 **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.4k 🚀 +26/d | **54** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 8k 🚀 +5/d | **49** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、记忆与上下文、会话持久化；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 529 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[openai/codex](https://github.com/openai/codex)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[garrytan/gstack](https://github.com/garrytan/gstack)、[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[BaaRai/ARTEX](https://github.com/BaaRai/ARTEX)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)、[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** | LoopForge 是一个可自主部署的团队工作台，让你和编程 Agent 一起交付软件。 在对话里把需求告诉 Main Bot：它会按需打开 Docker 沙箱、检出项目仓库、把任务分派给项目角色，最后提交 PR。 | 🟡 需配置 | — | — | 6.1k 🚀 +97/d | **77** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | ✅ | 37.9k 🚀 +40/d | **77** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy 是一个开源、开箱即用的 AI Agent。连接你的多台电脑与手机，把熟悉的 Agent、模型和已有订阅放在一起，培养一个懂你工作方式的伙伴。 | 🔴 较重 | — | — | 10.7k 🚀 +69/d | **69** |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 4.8k 🚀 +29/d | **67** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 32.9k 🚀 +35/d | **67** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、Agent 运行时、模型与供应商路由。 ‡ | 🟢 较易 | ✅ | ✅ | 8.9k 🚀 +25/d | **66** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | 独立账号平台与中转站：OpenRouter、Kimi 开放平台（国内/国际版）、AnyRouter、AgentRouter、AIHubMix、老张 API、Dahl、FoxCode、肖恩 AI、Cubence、RightCode、Grsai、FreeModel、SharedChat、WONG公益站、Krill AI、EMRank、RelayFor、Daya API、Verce… 账号站点兼容架构… | 🟡 需配置 | — | ✅ | 5.1k | **60** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排。 ‡ | 🟢 较易 | ✅ | — | 6k | **51** |

**也能做这件事：** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)、[QuantumNous/new-api](https://github.com/QuantumNous/new-api)、[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)、[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)、[NerverDevs/nervecenter](https://github.com/NerverDevs/nervecenter)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[Licoy/Quosparr](https://github.com/Licoy/Quosparr)、[cita-777/metapi](https://github.com/cita-777/metapi)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)、[crshdn/mission-control](https://github.com/crshdn/mission-control)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | 多智能体编排；兼容 OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 229.6k 🚀 +210/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. † | 🟢 开箱即用 | ✅ | ✅ | 18.7k 🚀 +196/d | **90** |
| 🏆 **[XinaTian/MROffice](https://github.com/XinaTian/MROffice)** | 跨 Agent 支持、记忆与上下文、可自托管；兼容 Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | ✅ | 4.9k 🚀 +304/d | **80** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.5k 🚀 +7/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 503 | **56** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | 对接其他产品是一个部署在流程后端地址之后的独立服务，不进入本仓库： 新增语音厂商加的是一个 profile，而不是一个新客户端： | 🟡 需配置 | — | — | 837 🚀 +22/d | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 814 | **54** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | 多智能体编排、技能与插件。 ‡ | 🟡 需配置 | — | — | 643 | **38** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[yetone/magpie](https://github.com/yetone/magpie)、[openai/codex](https://github.com/openai/codex)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[openfilm/openfilm](https://github.com/openfilm/openfilm)、[qybaihe/bla](https://github.com/qybaihe/bla)、[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)、[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)、[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 157.6k 🚀 +263/d | **94** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 跨 Agent 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 5k 🚀 +26/d | **67** |
| ✅ **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | 跨 Agent 支持、可自托管、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 4.6k 🚀 +35/d | **63** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、用量分析、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 963 | **56** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 443 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 796 | **53** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 608 | **45** |

**也能做这件事：** [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

## 安全

*安全与隔离*

Agent 会执行任意代码并持有凭据，必须控制影响范围。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 34.2k 🚀 +30/d | **70** |
| ✅ **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 8.2k 🚀 +44/d | **69** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 475 | **53** |
| 🔹 **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | MCP 支持、跨 Agent 支持、可自托管；兼容 Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 631 | **51** |
| 🔹 **[skyelan1999/aide](https://github.com/skyelan1999/aide)** | 可自托管、技能与插件、工作区隔离。 ‡ | 🟡 需配置 | — | — | 326 🚀 +5/d | **50** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[slopus/happy](https://github.com/slopus/happy)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[leepokai/Codync](https://github.com/leepokai/Codync)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[cordum-io/cordum](https://github.com/cordum-io/cordum)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[schmitech/orbit](https://github.com/schmitech/orbit)

## 故障转移

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 136.7k 🚀 +108/d | **87** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7k 🚀 +129/d | **86** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.9k | **55** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | 跨 Agent 支持、API 网关与中转、图形界面与桌面端；兼容 Codex、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 571 | **52** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[stablyai/orca](https://github.com/stablyai/orca)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[cita-777/metapi](https://github.com/cita-777/metapi)、[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.27 倍（42,408 vs 157,619） |

<details><summary><b>yetone/magpie 对比 farion1231/cc-switch</b></summary>

两者都为 Claude Code 和 Codex 管理多账号与多供应商，而 magpie 还能让其他模型走同一套 Agent 流程。

**未覆盖：** 自动故障转移、计费与计量、并行执行、多供应商聚合、会话持久化、技能与插件、用量分析

</details>

---

## 🪦 淘汰区

永远会有黑马出现。当新工具**完整覆盖**了旧工具的所有能力、热度不输、上手难度也不更高时，旧工具就会被移到这里，而不是悄悄留在推荐列表里。完整规则见 [docs/SUPERSEDE.md](docs/SUPERSEDE.md)。

### 已记录的取代关系

| 被淘汰 | 取代者 | 落败原因 | 来源 |
| --- | --- | --- | --- |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 64.04x the stars (20,620 vs 322) | 🤖 自动（high） |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 22.65x the stars (311,583 vs 13,754) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.90x the stars (20,620 vs 2,609) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.96x the stars (34,544 vs 384) | 🤖 自动（high） |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 44.97x the stars (42,408 vs 943) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.75x the stars (34,544 vs 940) | 🤖 自动（high） |
| **[Xpropel/Pi-Remote](https://github.com/xpropel/pi-remote)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 8.94x the stars (3,023 vs 338) | 🤖 自动（high） |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.86x the stars (34,544 vs 353) | 🤖 自动（high） |
| **[caveman-ai/caveman-code](https://github.com/caveman-ai/caveman-code)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 26.99x the stars (25,906 vs 960) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.60x the stars (142,786 vs 4,993) | 🤖 自动（high） |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 17.45x the stars (5,583 vs 320) | 🤖 自动（high） |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 9.77x the stars (12,580 vs 1,287) | 🤖 自动（high） |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.47x the stars (12,580 vs 2,301) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 3.06x the stars (1,139 vs 372) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.26x the stars (12,580 vs 430) | 🤖 自动（high） |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 50.70x the stars (25,906 vs 511) | 🤖 自动（high） |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 21.73x the stars (12,580 vs 579) | 🤖 自动（high） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | 16.25x the stars (8,155 vs 502) | 🤖 自动（high） |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 15.69x the stars (11,755 vs 749) | 🤖 自动（high） |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 160.34x the stars (157,619 vs 983) | 🤖 自动（high） |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 55.95x the stars (25,906 vs 463) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 101.70x the stars (142,786 vs 1,404) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.26x the stars (12,580 vs 2,950) | 🤖 自动（high） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 2.96x the stars (1,740 vs 588) | 🤖 自动（high） |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/blender-ai-mcp-suite)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.08x the stars (1,527 vs 495) | 🤖 自动（medium） |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 6.19x the stars (2,972 vs 480) | 🤖 自动（medium） |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.16x the stars (30,621 vs 1,895) | 🤖 自动（medium） |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 6.23x the stars (11,755 vs 1,888) | 🤖 自动（medium） |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.76x the stars (1,527 vs 554) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 13.42x the stars (11,755 vs 876) | 🤖 自动（medium） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[HKUDS/DeepTutor](https://github.com/hkuds/deeptutor)** | 26.96x the stars (63,686 vs 2,362) | 🤖 自动（medium） |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.69x the stars (25,906 vs 5,528) | 🤖 自动（medium） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.56x the stars (1,527 vs 429) | 🤖 自动（medium） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.48x the stars (1,218 vs 492) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.78x the stars (1,527 vs 549) | 🤖 自动（medium） |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 106.25x the stars (117,511 vs 1,106) | 🤖 自动（medium） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | 2.17x the stars (702 vs 323) | 🤖 自动（high） |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 21.90x the stars (34,544 vs 1,577) | 🤖 自动（high） |
| **[google/artemis](https://github.com/google/artemis)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 9.37x the stars (170,558 vs 18,203) | 🤖 自动（high） |
| **[Leonxlnx/earshot](https://github.com/leonxlnx/earshot)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 1.98x the stars (11,755 vs 5,931) | 🤖 自动（medium） |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.54x the stars (1,527 vs 602) | 🤖 自动（medium） |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.13x the stars (1,116 vs 524) | 🤖 自动（medium） |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.00x the stars (1,527 vs 765) | 🤖 自动（high） |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.22x the stars (685 vs 560) | 🤖 自动（medium） |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 3.28x the stars (28,430 vs 8,660) | 🤖 自动（medium） |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/rabiroute)** | **[greenfield-inc/Pane](https://github.com/greenfield-inc/pane)** | 1.39x the stars (685 vs 494) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[google/artemis](https://github.com/google/artemis)** | mobile | 18.2k | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (6/6)。 |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | teams-self-hosting | 13.8k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (9/9)。 |
| **[kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director)** | mobile | 8.7k | 🔻 已被取代 | 已被 milind-soni/OpenMausBot 取代：covers 100% of capabilities (6/6)。 |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | sessions-memory | 5.9k | 🔻 已被取代 | 已被 kajisho5/ffmpeg-skill 取代：covers 100% of capabilities (4/4)。 |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.5k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (9/9)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | parallelism | 5k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams-self-hosting | 3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.6k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (7/7)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams-self-hosting | 2.4k | 🔻 已被取代 | 已被 HKUDS/DeepTutor 取代：covers 100% of capabilities (7/7)。 |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams-self-hosting | 2.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | teams-self-hosting | 1.9k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | sessions-memory | 1.9k | 🔻 已被取代 | 已被 kajisho5/ffmpeg-skill 取代：covers 100% of capabilities (5/5)。 |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | parallelism | 1.6k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | parallelism | 1.4k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | teams-self-hosting | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | mobile | 1.1k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (7/7)。 |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 983 | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (5/5)。 |
| **[caveman-ai/caveman-code](https://github.com/caveman-ai/caveman-code)** | mobile | 960 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (7/7)。 |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 943 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (4/4)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism | 940 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | sessions-memory | 876 | 🔻 已被取代 | 已被 kajisho5/ffmpeg-skill 取代：covers 100% of capabilities (5/5)。 |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | sessions-memory | 765 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (6/6)。 |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | sessions-memory | 749 | 🔻 已被取代 | 已被 kajisho5/ffmpeg-skill 取代：covers 100% of capabilities (6/6)。 |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | sessions-memory | 602 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism | 588 | 🔻 已被取代 | 已被 pedrohcgs/claude-code-my-workflow 取代：covers 100% of capabilities (4/4)。 |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | teams-self-hosting | 579 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (4/4)。 |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile | 560 | 🔻 已被取代 | 已被 greenfield-inc/Pane 取代：covers 100% of capabilities (8/8)。 |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | sessions-memory | 554 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | sessions-memory | 549 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | failover | 524 | 🔻 已被取代 | 已被 data-goblin/power-bi-agentic-development 取代：covers 100% of capabilities (6/6)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 511 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security | 502 | 🔻 已被取代 | 已被 microsoft/TokenEconomizer 取代：covers 100% of capabilities (4/4)。 |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | sessions-memory | 495 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | mobile | 494 | 🔻 已被取代 | 已被 greenfield-inc/Pane 取代：covers 100% of capabilities (7/7)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions-memory | 492 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | parallelism | 480 | 🔻 已被取代 | 已被 rohitg00/pro-workflow 取代：covers 100% of capabilities (6/6)。 |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 463 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (8/8)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams-self-hosting | 430 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | sessions-memory | 429 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism | 384 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | failover | 372 | 🔻 已被取代 | 已被 abubakarsiddik31/claude-skills-collection 取代：covers 100% of capabilities (5/5)。 |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | parallelism | 353 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | parallelism | 338 | 🔻 已被取代 | 已被 Gentleman-Programming/gentle-shell 取代：covers 100% of capabilities (4/4)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | failover | 323 | 🔻 已被取代 | 已被 WenyuChiou/ai-research-skills 取代：covers 100% of capabilities (4/4)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 322 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | billing-2 | 320 | 🔻 已被取代 | 已被 aipoch/open-science 取代：covers 100% of capabilities (4/4)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-11-27 13:54 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
