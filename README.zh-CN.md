<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**220 个工具**，分 **13 个分类** · **54 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-26 10:10 UTC**

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
| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | 44 |
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 161 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 5 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 安全与自托管

*可自托管*

不希望代码或密钥经过他人的服务器。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 289.2k 🚀 +804/d | **89** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 面向 AI 智能体的本地优先搜索引擎与 MCP 服务。 一个 Rust 二进制程序即可为代码、文档、日志、JSONL/CSV 和 PDF 建立索引，提供 BM25 全文、向量与混合搜索、代码搜索和智能体记忆，接口兼容 Elasticsearch API。 | 🟢 较易 | — | — | 15.7k 🚀 +629/d | **86** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 11.1k 🚀 +109/d | **85** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 10.9k 🚀 +130/d | **85** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 13.6k 🚀 +330/d | **84** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 13.7k 🚀 +196/d | **82** |
| 🏆 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 3.7k 🚀 +288/d | **81** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 29.9k 🚀 +32/d | **71** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 32.8k 🚀 +30/d | **69** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 57.8k | **66** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 8.6k 🚀 +58/d | **64** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | MiMoCode 是一个终端原生的 AI 编程助手。它能读写代码、执行命令、管理 Git，通过持久化记忆系统，在多次会话间保持对你项目的深度理解，并自我进化。 | 🟢 较易 | — | — | 13.7k 🚀 +6/d | **63** |
| ✅ **[tianma-if/edgeever](https://github.com/tianma-if/edgeever)** | EdgeEver 是一款现代化的开源笔记与个人知识库工作区。 它保留经典高效的三栏工作区体验（目录树 · 笔记列表 · 编辑写作），同时具备完全开放的数据架构与原生 AI Agent 联动能力，让个人知识沉淀更轻量、更自由。 | 🟢 较易 | — | — | 2.9k (+24/d) | **63** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.4k 🚀 +20/d | **62** |
| 🔹 **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | English README · 5 分钟快速开始 · 我想重构项目 每一项：worktree → implementer 改 → 独立 verifier 跑测试 → 你 审 PR。 | 🟢 开箱即用 | ✅ | — | 11.6k 🚀 +6/d | **61** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | MCP 支持、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.4k | **60** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 4k 🚀 +30/d | **60** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.7k 🚀 +5/d | **56** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | MCP 支持、技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 414 | **55** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 16.6k | **52** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code（DAC） 将桌面编程工作区和终端智能体连接到同一个执行内核。 面对跨文件、多轮对话、多种工具和多人讨论的工作，你可以保留项目上下文、维护可编辑的计划、委派独立子任务、查看执行过程，并让最终回答回到发起工作的对话中。 | 🟢 较易 | — | — | 433 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 497 | **51** |
| 🔹 **[GMaN1911/claude-cognitive](https://github.com/GMaN1911/claude-cognitive)** | 跨 Agent 支持；兼容 Claude Code、Gemini CLI、Cursor、Aider。 ‡ | 🟡 需配置 | — | — | 451 | **51** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 548 | **49** |

**也能做这件事：** [bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[yetone/cumora](https://github.com/yetone/cumora)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)、[cordum-io/cordum](https://github.com/cordum-io/cordum)、[crshdn/mission-control](https://github.com/crshdn/mission-control)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 桌面端

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 153.4k 🚀 +139/d | **90** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 176.5k 🚀 +1204/d | **87** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 102.7k 🚀 +521/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 20.8k 🚀 +576/d | **85** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 图形界面与桌面端、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 47.7k 🚀 +2557/d | **82** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 7.2k 🚀 +91/d | **80** |
| 🏆 **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | MCP 支持、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 2.8k 🚀 +258/d | **78** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill 把你的 AI Agent 连接到 Chrome 或 Microsoft Edge，直接使用你已有的登录状态。 | 🟢 较易 | — | — | 9.6k 🚀 +56/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 8k 🚀 +26/d | **70** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 5.2k 🚀 +64/d | **68** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | ✅ | — | 4.8k 🚀 +84/d | **68** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | MCP 支持、通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 10.8k 🚀 +50/d | **67** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +55/d | **66** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 跨 Agent 支持、通知提醒、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.4k 🚀 +25/d | **66** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 7k 🚀 +46/d | **61** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. † | 🟢 开箱即用 | ✅ | — | 6.2k 🚀 +21/d | **59** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | 跨 Agent 支持、团队协作；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.7k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | MCP 支持、图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.7k | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 893 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 540 | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 并行执行；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | ✅ | 507 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | 通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 343 | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、OpenCode、Copilot、Goose。 ‡ | 🟢 较易 | — | — | 440 | **52** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | 跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 368 | **52** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | 跨 Agent 支持、MCP 支持、计费与计量；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 291 | **52** |

*还有 10 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[anomalyco/opencode](https://github.com/anomalyco/opencode)、[garrytan/gstack](https://github.com/garrytan/gstack)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

## 并行与隔离

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 164.1k 🚀 +287/d | **98** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、技能与插件、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 137.8k 🚀 +129/d | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 107.5k 🚀 +411/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 22.1k 🚀 +101/d | **83** |
| 🏆 **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 47.5k 🚀 +87/d | **80** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | MCP 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 84.4k 🚀 +41/d | **74** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 33.8k 🚀 +22/d | **72** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.7k 🚀 +20/d | **69** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 9.5k 🚀 +27/d | **68** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | 跨 Agent 支持、通知提醒、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 9.1k 🚀 +26/d | **67** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 8.3k 🚀 +38/d | **67** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **59** |
| 🔹 **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | 多智能体编排、Agent 运行时、通知提醒；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 1.4k (+9/d) | **59** |
| 🔹 **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 多智能体编排、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.4k | **57** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.2k 🚀 +6/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 581 | **57** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 581 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | MCP 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 459 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 320 | **55** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 跨 Agent 支持、通知提醒、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 8.4k | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 422 | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 788 | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 2.9k | **52** |
| 🔹 **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | 跨 Agent 支持、技能与插件、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Droid。 ‡ | 🟢 较易 | — | — | 400 | **51** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 304 | **49** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)、[crshdn/mission-control](https://github.com/crshdn/mission-control)、[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 桌面端

*MCP 支持*

Agent 需要通过标准协议访问外部工具与数据。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Agent 运行时；兼容 OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 221.7k 🚀 +451/d | **90** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 20.8k 🚀 +167/d | **88** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. † | 🟢 开箱即用 | ✅ | ✅ | 10.6k 🚀 +418/d | **87** |
| 🏆 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | 技能与插件、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Cursor。 ‡ | 🟡 需配置 | — | — | 7.3k 🚀 +206/d | **79** |
| ✅ **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、API 网关与中转、记忆与上下文；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.7k 🚀 +94/d | **77** |
| ✅ **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 跨 Agent 支持、技能与插件、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 3k 🚀 +57/d | **74** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 使用 ChatGPT 网页版的独立额度，不消耗 Work 或 Codex 额度。 | 🟢 较易 | — | — | 15k 🚀 +59/d | **72** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.2k 🚀 +17/d | **63** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k | **62** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.2k 🚀 +11/d | **58** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | 通知提醒、并行执行、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[graygnatconsole/mcp-audit-tool](https://github.com/graygnatconsole/mcp-audit-tool)** | 跨 Agent 支持、工作区隔离；兼容 Cursor、Copilot、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 543 🚀 +8/d | **57** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 473 | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.1k | **55** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | — | 520 🚀 +8/d | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、安全与隔离；兼容 Cursor、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 468 | **55** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | 跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 407 | **55** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 较易 | — | — | 385 | **54** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 479 🚀 +9/d | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 跨 Agent 支持、模型与供应商路由、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 716 | **52** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | 对接其他产品是一个部署在流程后端地址之后的独立服务，不进入本仓库： 新增语音厂商加的是一个 profile，而不是一个新客户端： | 🟡 需配置 | — | — | 400 🚀 +14/d | **52** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | 可自托管。 ‡ | 🟢 较易 | — | ✅ | 1.2k | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | API 网关与中转、并行执行；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 2.7k | **46** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | 跨 Agent 支持、模型与供应商路由、通知提醒；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟡 需配置 | — | — | 475 | **46** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | 跨 Agent 支持、可自托管、技能与插件；兼容 Claude Code、Cursor。 ‡ | 🔴 较重 | — | — | 323 | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时。 ‡ | 🟡 需配置 | — | — | 416 | **45** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[nexu-io/open-design](https://github.com/nexu-io/open-design)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[yetone/magpie](https://github.com/yetone/magpie)、[xerj-org/xerj](https://github.com/xerj-org/xerj)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

## 移动端与远程控制

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 106.4k 🚀 +1210/d | **92** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、语音输入、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 6.5k 🚀 +168/d | **85** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | 跨 App 自动化：根据自然语言指令，在 Android 上执行测试流程和日常任务。 AndroidWorld 结果：在 Google Research AndroidWorld 基准评测（100+ 多步任务）中取得 99%+ 任务完成率。 | 🟡 需配置 | — | — | 14.9k 🚀 +308/d | **82** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Codex、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 5.6k 🚀 +63/d | **74** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 3k 🚀 +44/d | **67** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | ✅ | 24.3k 🚀 +16/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.9k 🚀 +17/d | **64** |
| 🔹 **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | 在你自己的本地 Agent 上运行 Claude Design —— Cursor、Claude Code、Claude Desktop，或任何能读写文件的编码 Agent。 | 🟢 开箱即用 | ✅ | — | 4.5k 🚀 +13/d | **60** |
| 🔹 **[leepokai/Codync](https://github.com/leepokai/Codync)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 892 | **58** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | 记忆与上下文。 ‡ | 🟡 需配置 | — | — | 3.6k 🚀 +11/d | **56** |
| 🔹 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | 远程模式支持官方插件页的列表、配置和启用/停用（需更新 Host Remote 插件）。Remote 自身仍只能在 Host 本地配置和启停；不开放远程安装、卸载。 | 🟢 较易 | — | — | 862 🚀 +12/d | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4k 🚀 +5/d | **55** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 285 | **55** |
| 🔹 **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | ✅ | 261 🚀 +7/d | **55** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、额度与用量管理；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 3k 🚀 +30/d | **54** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **51** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟡 需配置 | — | — | 1.1k 🚀 +5/d | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 550 | **51** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Agent 运行时、多智能体编排、可自托管。 ‡ | 🟢 较易 | — | — | 468 | **50** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)、[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

## 共享

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 22.1k 🚀 +733/d | **89** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 131k 🚀 +143/d | **89** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 31.4k 🚀 +57/d | **71** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 10k 🚀 +51/d | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | API 网关与中转、图形界面与桌面端、跨 Agent 支持；兼容 Codex、OpenCode、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 19.4k 🚀 +38/d | **69** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.9k 🚀 +39/d | **67** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.8k | **56** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 550 🚀 +23/d | **56** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.6k 🚀 +15/d | **55** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.7k 🚀 +13/d | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 503 | **52** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 259 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 304 | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 906 | **49** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 自动故障转移、图形界面与桌面端、安全与隔离；兼容 Codex。 ‡ | 🔴 较重 | — | — | 269 🚀 +12/d | **48** |
| 🔹 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | 支持导入当前登录账号、手动粘贴 Token、OAuth 文件快速导入 配额看板与自动刷新（5H / 7D）、低额度提醒与切换提示 | 🟡 需配置 | — | — | 250 | **45** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)、[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)、[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 安全

*安全与隔离*

Agent 会执行任意代码并持有凭据，必须控制影响范围。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | 可自托管、MCP 支持、自动故障转移。 ‡ | 🟡 需配置 | — | — | 7.2k 🚀 +71/d | **74** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、可自托管；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 6.1k 🚀 +31/d | **68** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi 为运行服务会处理有限的账户与技术信息；存在的分析均已披露且可关闭。 | 🟢 较易 | — | — | 3.2k 🚀 +39/d | **66** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、MCP 支持、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.2k 🚀 +16/d | **65** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 图形界面与桌面端、跨 Agent 支持、计费与计量；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 5.4k 🚀 +10/d | **63** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.5k 🚀 +13/d | **57** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k | **57** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 图形界面与桌面端、记忆与上下文、跨 Agent 支持；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.8k | **55** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 785 | **55** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 图形界面与桌面端、工作区隔离、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | ✅ | 351 | **52** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 330 | **52** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 309 | **52** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 图形界面与桌面端、MCP 支持、用量分析；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 524 | **51** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew 将任务执行、人工审批、持久记忆和定时任务整合到一个桌面应用。 你可以交办任务、添加文件与文件夹材料，查看实时回复、执行步骤、工具调用和结果。 | 🟡 需配置 | — | ✅ | 253 | **47** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |

**也能做这件事：** [garrytan/gstack](https://github.com/garrytan/gstack)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[slopus/happy](https://github.com/slopus/happy)、[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)、[leepokai/Codync](https://github.com/leepokai/Codync)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)

## 故障转移

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、模型与供应商路由、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 148.8k 🚀 +357/d | **93** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 4.2k 🚀 +108/d | **85** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.5k 🚀 +13/d | **67** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 1.8k 🚀 +15/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Node 22+ LTS（用于钩子脚本 — 通常与 Claude Code / Codex / Gemini CLI 一起已安装） /om-review-brief 通过汇总所有内容生成完整的评估简报：成就记录、决策、事件、能力证据和 1:1 反馈 | 🟡 需配置 | — | — | 5.4k 🚀 +6/d | **59** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 只需向 Claude Code、Codex、OpenCode 或 DeepSeek Harness 给出一次目标，即可让它跨桌面 App 与终端持续工作数十个小时。 | 🟢 较易 | — | — | 1.8k | **59** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | — | — | 5.1k 🚀 +6/d | **56** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | MCP 支持、跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 440 | **52** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 676 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **51** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 286 | **51** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 7.8k 🚀 +9/d | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、模型与供应商路由、API 网关与中转；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 557 | **46** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace 为 LLM Agent 提供持久化、可检索、可审计的外部记忆，让每次对话都能在之前的基础上继续，而不是从零开始。 | 🟡 需配置 | — | — | 315 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、记忆与上下文、会话持久化；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 520 | **43** |

**也能做这件事：** [openai/codex](https://github.com/openai/codex)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)、[makecindy/cindy](https://github.com/makecindy/cindy)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)

## 模型路由

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 104k 🚀 +223/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 77.4k 🚀 +250/d | **89** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 一套用代码做片的风格工具箱： 59 种现成风格，也能做出你自己的。 拿来做什么：做什么片、发在哪个平台（竖屏就用 1080×1920 或 1080×1440），有没有品牌色、logo、字体或固定角色； | 🟡 需配置 | — | ✅ | 7.8k 🚀 +634/d | **82** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 10.7k 🚀 +54/d | **68** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.4k 🚀 +28/d | **65** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. † | 🟡 需配置 | — | — | 11.2k 🚀 +12/d | **59** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟢 较易 | — | — | 1.9k 🚀 +9/d | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | — | 344 | **53** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 跨 Agent 支持、Agent 运行时、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 908 | **52** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 5.6k | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 713 | **50** |

**也能做这件事：** [yetone/magpie](https://github.com/yetone/magpie)、[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)、[decolua/9router](https://github.com/decolua/9router)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | MCP 支持、技能与插件、模型与供应商路由；兼容 Gemini CLI。 ‡ | 🟢 较易 | — | — | 108.4k 🚀 +183/d | **91** |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件、并行执行；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 61.2k 🚀 +394/d | **90** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 44.9k 🚀 +72/d | **75** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 10.8k 🚀 +41/d | **66** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、MCP 支持、可自托管。 ‡ | 🔴 较重 | — | — | 11.7k 🚀 +24/d | **57** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 通知提醒、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 323 🚀 +12/d | **54** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 814 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 407 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、多账号切换；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **49** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 434 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[decolua/9router](https://github.com/decolua/9router)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[spinabot/brigade](https://github.com/spinabot/brigade)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 4.1k 🚀 +32/d | **69** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.3k 🚀 +8/d | **56** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、用量分析、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 866 | **56** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、OpenCode。 ‡ | 🟢 较易 | — | — | 984 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 759 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 434 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、多智能体编排；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 511 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 594 | **45** |

**也能做这件事：** [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[yc-software/qm](https://github.com/yc-software/qm)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | 以本地为核心的研究智能体执行框架和工作空间。 | 🟢 开箱即用 | ✅ | — | 7.6k 🚀 +32/d | **65** |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | 2026-08-02 · ⏱️ 200+ 小时长程轨迹在 X 公开分享 — 早期 owner-run 案例跨越 200+ 小时自然时长，展示执行、等待、人工决策与恢复的衔接，并在 X 获得广泛传播。 2026-09-06 · 🎉 LoopX 1.0 — 个人 Agent 工作区：跨会话跟进 Agent 工作、处理待决事项、核对交付结果。 | 🟢 较易 | — | — | 6.4k 🚀 +10/d | **65** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | 她本身（Source）——审计、fork、二次开发，把通用改进以 Apache-2.0 贡献回来。 她够得到的系统（MCP）——把内部工具和业务系统接进来。 | 🔴 较重 | — | — | 5.6k 🚀 +59/d | **65** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排、可自托管。 ‡ | 🟢 较易 | ✅ | — | 5.9k | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、记忆与上下文、工作区隔离；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |

**也能做这件事：** [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[tianma-if/edgeever](https://github.com/tianma-if/edgeever)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)、[yetone/cumora](https://github.com/yetone/cumora)、[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)

## 远程控制

*远程控制*

Agent 跑在电脑上，但你想在别处操控它。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 6.3k 🚀 +103/d | **78** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 图形界面与桌面端、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 11.1k 🚀 +23/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、Agent 运行时、模型与供应商路由。 ‡ | 🟢 较易 | ✅ | ✅ | 8.3k 🚀 +40/d | **68** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 320 | **48** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[spinabot/brigade](https://github.com/spinabot/brigade)、[felinics/Memoh](https://github.com/felinics/Memoh)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)、[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.15 倍（22,131 vs 148,832） |

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
| **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.86x the stars (11,107 vs 372) | 🤖 自动（high） |
| **[AVIDS2/memorix](https://github.com/avids2/memorix)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 331.61x the stars (289,160 vs 872) | 🤖 自动（high） |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 59.22x the stars (19,365 vs 327) | 🤖 自动（high） |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 25.30x the stars (11,107 vs 439) | 🤖 自动（high） |
| **[Dodaios/Dodaios](https://github.com/dodaios/dodaios)** | **[HarnessMD/munder-difflin](https://github.com/harnessmd/munder-difflin)** | 35.45x the stars (9,074 vs 256) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.05x the stars (19,365 vs 2,406) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[HarnessMD/munder-difflin](https://github.com/harnessmd/munder-difflin)** | 23.88x the stars (9,074 vs 380) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 19.80x the stars (10,890 vs 550) | 🤖 自动（high） |
| **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 70.51x the stars (29,897 vs 424) | 🤖 自动（high） |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 560.39x the stars (289,160 vs 516) | 🤖 自动（high） |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/memtensor/memos-cloud-openclaw-plugin)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 81.02x the stars (29,897 vs 369) | 🤖 自动（high） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.18x the stars (11,107 vs 2,143) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.40x the stars (33,779 vs 928) | 🤖 自动（high） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 3.14x the stars (893 vs 284) | 🤖 自动（high） |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 54.13x the stars (33,779 vs 624) | 🤖 自动（high） |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 165.33x the stars (289,160 vs 1,749) | 🤖 自动（high） |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 221.84x the stars (104,043 vs 469) | 🤖 自动（high） |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.91x the stars (33,779 vs 345) | 🤖 自动（high） |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 576.02x the stars (289,160 vs 502) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 21.71x the stars (107,454 vs 4,949) | 🤖 自动（high） |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.66x the stars (11,107 vs 1,282) | 🤖 自动（high） |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.04x the stars (11,107 vs 2,202) | 🤖 自动（high） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[tianma-if/edgeever](https://github.com/tianma-if/edgeever)** | 6.71x the stars (2,878 vs 429) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 30.02x the stars (11,107 vs 370) | 🤖 自动（high） |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 165.94x the stars (104,043 vs 627) | 🤖 自动（high） |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.39x the stars (33,779 vs 276) | 🤖 自动（high） |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.34x the stars (148,832 vs 9,107) | 🤖 自动（high） |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 16.80x the stars (11,107 vs 661) | 🤖 自动（high） |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 34.83x the stars (19,365 vs 556) | 🤖 自动（high） |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 5.11x the stars (1,431 vs 280) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 13.24x the stars (11,107 vs 839) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.47x the stars (289,160 vs 6,092) | 🤖 自动（high） |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 105.64x the stars (29,897 vs 283) | 🤖 自动（high） |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 607.48x the stars (289,160 vs 476) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.97x the stars (11,107 vs 2,795) | 🤖 自动（high） |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.42x the stars (11,107 vs 1,319) | 🤖 自动（medium） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.10x the stars (27,655 vs 575) | 🤖 自动（medium） |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 41.12x the stars (29,897 vs 727) | 🤖 自动（medium） |
| **[ZipengWu365/TOMC](https://github.com/zipengwu365/tomc)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 40.94x the stars (10,890 vs 266) | 🤖 自动（medium） |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 24.41x the stars (33,779 vs 1,384) | 🤖 自动（high） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.31x the stars (1,118 vs 484) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.45x the stars (893 vs 364) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.89x the stars (893 vs 309) | 🤖 自动（high） |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 2.09x the stars (11,056 vs 5,295) | 🤖 自动（high） |
| **[Arvincreator/project-golem](https://github.com/arvincreator/project-golem)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 1.74x the stars (1,118 vs 642) | 🤖 自动（high） |
| **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 3.93x the stars (29,897 vs 7,616) | 🤖 自动（high） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.56x the stars (785 vs 503) | 🤖 自动（medium） |
| **[Dataojitori/nocturne_memory](https://github.com/dataojitori/nocturne_memory)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 8.06x the stars (11,357 vs 1,409) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 1.27x the stars (1,786 vs 1,404) | 🤖 自动（medium） |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.19x the stars (320 vs 270) | 🤖 自动（medium） |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.18x the stars (893 vs 755) | 🤖 自动（medium） |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.16x the stars (1,068 vs 495) | 🤖 自动（medium） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.27x the stars (785 vs 616) | 🤖 自动（medium） |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 1.46x the stars (1,118 vs 766) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | failover | 9.1k | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (7/7)。 |
| **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | security-self-hosting | 7.6k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | security-self-hosting | 6.1k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | remote-control | 5.3k | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (6/6)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | parallelism-isolation | 4.9k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | security-self-hosting | 2.8k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (8/8)。 |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | security-self-hosting | 2.2k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | security-self-hosting | 2.1k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | security-self-hosting | 1.7k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (9/9)。 |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | security-self-hosting | 1.4k | 🔻 已被取代 | 已被 spinabot/brigade 取代：covers 100% of capabilities (7/7)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | security | 1.4k | 🔻 已被取代 | 已被 tickernelz/opencode-mem 取代：covers 100% of capabilities (4/4)。 |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | parallelism-isolation | 1.4k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | security-self-hosting | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (9/9)。 |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | security-self-hosting | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism-isolation | 928 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | security-self-hosting | 872 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (10/10)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | security-self-hosting | 839 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | desktop-ui-2 | 766 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | security-self-hosting | 727 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | security-self-hosting | 661 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | desktop-ui-2 | 642 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 627 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | parallelism-isolation | 624 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | security | 616 | 🔻 已被取代 | 已被 kitfunso/hippo-memory 取代：covers 100% of capabilities (6/6)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism-isolation | 575 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (4/4)。 |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 556 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (5/5)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | security-self-hosting | 550 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (5/5)。 |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | security-self-hosting | 516 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security | 503 | 🔻 已被取代 | 已被 kitfunso/hippo-memory 取代：covers 100% of capabilities (4/4)。 |
| **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | security-self-hosting | 502 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 495 | 🔻 已被取代 | 已被 data-goblin/power-bi-agentic-development 取代：covers 100% of capabilities (6/6)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | desktop-ui-2 | 484 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | security-self-hosting | 476 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 469 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | security-self-hosting | 439 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | security-self-hosting | 429 | 🔻 已被取代 | 已被 tianma-if/edgeever 取代：covers 100% of capabilities (4/4)。 |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | security-self-hosting | 424 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (12/12)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism-isolation | 380 | 🔻 已被取代 | 已被 HarnessMD/munder-difflin 取代：covers 100% of capabilities (5/5)。 |
| **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | security-self-hosting | 372 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | security-self-hosting | 370 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | security-self-hosting | 369 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 364 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | parallelism-isolation | 345 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 309 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | security-self-hosting | 283 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (7/7)。 |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | parallelism-isolation | 280 | 🔻 已被取代 | 已被 Gentleman-Programming/gentle-shell 取代：covers 100% of capabilities (6/6)。 |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | parallelism-isolation | 276 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | parallelism-isolation | 270 | 🔻 已被取代 | 已被 h0x91b/dev-3.0 取代：covers 100% of capabilities (7/7)。 |
| **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | security-self-hosting | 266 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (8/8)。 |
| **[Dodaios/Dodaios](https://github.com/Dodaios/Dodaios)** | parallelism-isolation | 256 | 🔻 已被取代 | 已被 HarnessMD/munder-difflin 取代：covers 100% of capabilities (9/9)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-26 10:10 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
