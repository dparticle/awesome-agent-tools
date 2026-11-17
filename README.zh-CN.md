<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**226 个工具**，分 **16 个分类** · **50 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-11-17 13:27 UTC**

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
| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | 49 |
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 167 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 9 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 桌面端

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 20.9k 🚀 +401/d | **86** |
| 🏆 **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 9.3k 🚀 +98/d | **85** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 27.8k 🚀 +185/d | **84** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 跨 Agent 支持、Agent 运行时、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 49.9k 🚀 +54/d | **78** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 7.1k 🚀 +88/d | **73** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. † | 🔴 较重 | — | — | 9.7k 🚀 +123/d | **71** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | 展开请求看细节：读取已保留的请求头、提交数据、响应正文、耗时与错误，筛选流量或直接查看某个 JSON 字段。 验证并保留证据：配置任务内的请求修改、拦截、模拟响应或同源请求重放，导出 JSON，供后续复查和分享。 | 🟢 较易 | — | — | 10.5k 🚀 +31/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 6.8k 🚀 +46/d | **65** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft m… † | 🟢 较易 | — | — | 6.6k 🚀 +36/d | **63** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.9k 🚀 +15/d | **62** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | Agent 运行时；兼容 Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.6k 🚀 +13/d | **60** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 4.5k 🚀 +20/d | **60** |
| 🔹 **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 较易 | — | — | 3.9k 🚀 +12/d | **59** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.4k 🚀 +10/d | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | Agent 运行时、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | Intent Solutions is a Claude Partner Network Select Services Partner. By job to be done — tonsofskills.com/cowork, curated bundles as one-click downloads. † | 🟢 较易 | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 4.4k 🚀 +13/d | **54** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 跨 Agent 支持、Agent 运行时、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k | **54** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | 跨 Agent 支持、图形界面与桌面端、记忆与上下文；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | 多账号切换、团队协作；兼容 Claude Code、Droid。 ‡ | 🔴 较重 | — | — | 788 | **52** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | Binance Skills Hub is an open skills marketplace that gives AI agents native access to crypto: both centralized and decentralized. † | 🟡 需配置 | — | — | 1.2k 🚀 +7/d | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 931 | **51** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | Agent 运行时、跨 Agent 支持、计费与计量；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 299 | **51** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 3.2k 🚀 +18/d | **50** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | 跨 Agent 支持；兼容 Claude Code、OpenCode、Copilot、Goose。 ‡ | 🟢 较易 | — | — | 444 | **50** |
| 🔹 **[GMaN1911/claude-cognitive](https://github.com/GMaN1911/claude-cognitive)** | 跨 Agent 支持；兼容 Claude Code、Gemini CLI、Cursor、Aider。 ‡ | 🟡 需配置 | — | — | 451 | **49** |
| 🔹 **[pskoett/self-improving-agent](https://github.com/pskoett/self-improving-agent)** | 跨 Agent 支持；兼容 Claude Code、Codex、Copilot。 ‡ | 🟢 较易 | — | — | 792 | **47** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Analyze + Generate：先提取视觉系统，再生成不复制原图构图的新作品。 Generate：内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。 | 🟡 需配置 | — | — | 7.5k 🚀 +6/d | **46** |

*还有 1 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [ruvnet/ruflo](https://github.com/ruvnet/ruflo)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[qybaihe/bla](https://github.com/qybaihe/bla)、[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)、[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)、[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)、[langfuse/langfuse](https://github.com/langfuse/langfuse)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)

## 团队与自托管

*团队协作*

多人需要共用一套 Agent 环境，还要有角色与边界。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 305k 🚀 +670/d | **89** |
| 🏆 **[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 10k 🚀 +547/d | **86** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | 图形界面与桌面端、会话持久化、工作区隔离；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 8.4k 🚀 +248/d | **84** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 8.2k 🚀 +66/d | **76** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | ✅ | 37.5k 🚀 +38/d | **76** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 16k 🚀 +66/d | **75** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 12.5k 🚀 +54/d | **73** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 12.2k 🚀 +36/d | **71** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | API 网关与中转、图形界面与桌面端、模型与供应商路由。 ‡ | 🔴 较重 | — | — | 52.1k 🚀 +53/d | **69** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 30.4k 🚀 +21/d | **69** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、Agent 运行时、模型与供应商路由。 ‡ | 🟢 较易 | ✅ | ✅ | 8.7k 🚀 +20/d | **65** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、模型与供应商路由、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 18k 🚀 +15/d | **62** |
| 🔹 **[vstorm-co/agenticos](https://github.com/vstorm-co/agenticos)** | MCP 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 开箱即用 | — | — | 390 | **58** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.7k 🚀 +6/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.8k | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.2k 🚀 +5/d | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、自动故障转移；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 510 | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 310 | **52** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | MCP 支持、图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 524 | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code（DAC） 将桌面编程工作区和终端智能体连接到同一个执行内核。 面对跨文件、多轮对话、多种工具和多人讨论的工作，你可以保留项目上下文、维护可编辑的计划、委派独立子任务、查看执行过程，并让最终回答回到发起工作的对话中。 | 🟢 较易 | — | — | 429 | **49** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 570 | **47** |

**也能做这件事：** [ruvnet/ruflo](https://github.com/ruvnet/ruflo)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[crshdn/mission-control](https://github.com/crshdn/mission-control)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)、[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 会话与记忆

*会话持久化*

合上笔记本或断网就会中断长时间运行的会话。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 面向 AI 智能体的本地优先搜索引擎与 MCP 服务。 一个 Rust 二进制程序即可为代码、文档、日志、JSONL/CSV 和 PDF 建立索引，提供 BM25 全文、向量与混合搜索、代码搜索和智能体记忆，接口兼容 Elasticsearch API。 | 🟢 较易 | — | — | 19.2k 🚀 +53/d | **75** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 8.2k 🚀 +54/d | **71** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、模型与供应商路由、可自托管；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 33.4k 🚀 +19/d | **67** |
| 🔹 **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 9.8k 🚀 +39/d | **61** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | 跨 Agent 支持、技能与插件、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 1.5k 🚀 +17/d | **59** |
| 🔹 **[ai-driven-dev/framework](https://github.com/ai-driven-dev/framework)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 562 | **57** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | 跨 Agent 支持；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 624 | **56** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟡 需配置 | — | — | 2.1k 🚀 +10/d | **55** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 1.9k 🚀 +6/d | **55** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **55** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 438 | **54** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 17.4k 🚀 +6/d | **53** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 跨 Agent 支持、通知提醒、远程控制；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 941 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | 跨 Agent 支持、自动故障转移、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 462 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 945 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | 跨 Agent 支持、多智能体编排、API 网关与中转；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 720 | **51** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | 技能与插件、自动故障转移、模型与供应商路由。 ‡ | 🔴 较重 | — | — | 535 | **49** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、自动故障转移、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 678 | **46** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | 图形界面与桌面端、通知提醒、可自托管。 ‡ | 🔴 较重 | — | — | 494 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、自动故障转移、用量分析；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 525 | **43** |

**也能做这件事：** [affaan-m/ECC](https://github.com/affaan-m/ECC)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)、[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)、[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)

## 移动端

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 127.4k 🚀 +879/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、可自托管；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 114.5k 🚀 +237/d | **89** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 141.9k 🚀 +107/d | **88** |
| 🏆 **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 7.4k 🚀 +314/d | **84** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 24.2k 🚀 +71/d | **77** |
| ✅ **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | 从手机、电脑、浏览器继续使用你的 DeepSeek Harness 实例。无论使用哪台设备，都可以回到同一个 Harness 会话。 | 🟢 较易 | — | — | 3.1k 🚀 +90/d | **77** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | 多智能体编排、Agent 运行时、自动故障转移；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.7k 🚀 +88/d | **77** |
| ✅ **[google/artemis](https://github.com/google/artemis)** | 跨 App 自动化：根据自然语言指令，在 Android 上执行测试流程和日常任务。 AndroidWorld 结果：在 Google Research AndroidWorld 基准评测（100+ 多步任务）中取得 99%+ 任务完成率。 | 🟡 需配置 | — | — | 17.6k 🚀 +62/d | **68** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 2.2k 🚀 +30/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | ✅ | ✅ | 24.7k 🚀 +14/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、安全与隔离、MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.5k 🚀 +12/d | **63** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 1.3k | **60** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、自动故障转移、图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 5.2k 🚀 +7/d | **57** |
| 🔹 **[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)** | 工作区隔离、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟢 较易 | — | ✅ | 1.1k | **56** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Codex、Copilot。 ‡ | 🟢 开箱即用 | — | ✅ | 493 | **56** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.2k | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 559 | **51** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 309 | **49** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **47** |

**也能做这件事：** [nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[makecindy/cindy](https://github.com/makecindy/cindy)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)、[yetone/cumora](https://github.com/yetone/cumora)

## MCP与安全

*API 网关与中转*

客户端与上游协议不一致，或需要隐藏密钥、统一出口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 面向 Claude Code 与 Codex 的智能体元基座（meta-harness）。 | 🟢 开箱即用 | — | — | 81.9k (+154/d) | **93** |
| 🏆 **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | 技能与插件、多智能体编排、远程控制；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 33.9k 🚀 +102/d | **84** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 23.9k 🚀 +86/d | **82** |
| 🏆 **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | 技能与插件、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Cursor。 ‡ | 🟡 需配置 | — | — | 10.4k 🚀 +196/d | **78** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 消息通过已登录的 ChatGPT 网页会话发送，并受该账户适用的使用限制约束。 | 🟢 较易 | — | — | 15.8k 🚀 +15/d | **63** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | 跨 Agent 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 11.3k 🚀 +18/d | **62** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.6k | **62** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 只需向 Claude Code、Codex、OpenCode 或 DeepSeek Harness 给出一次目标，即可让它跨桌面 App 与终端持续工作数十个小时。 | 🟢 较易 | — | — | 1.9k | **59** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.3k | **57** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k | **56** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 较易 | — | — | 394 | **54** |
| 🔹 **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | 模型与供应商路由、可自托管、并行执行；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 1.3k | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 跨 Agent 支持、多智能体编排、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 753 | **53** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | 跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 600 🚀 +10/d | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | 跨 Agent 支持、Agent 运行时、远程控制；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 401 🚀 +5/d | **53** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **49** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Agent 运行时、通知提醒、技能与插件。 ‡ | 🟡 需配置 | — | — | 508 | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时、多智能体编排。 ‡ | 🟡 需配置 | — | — | 421 | **42** |
| 👀 **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | 在 Slack thread 里发起任务，在你自己的机器/环境里执行，过程可见、权限可控、结果可审计。 | 🟡 需配置 | — | — | 500 | **41** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[yetone/magpie](https://github.com/yetone/magpie)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[QuantumNous/new-api](https://github.com/QuantumNous/new-api)

## 计费

*额度与用量管理*

看不到剩余额度，任务做到一半就被限流。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 38k 🚀 +547/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 跨 Agent 支持、通知提醒、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.8k 🚀 +232/d | **84** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 32.5k 🚀 +49/d | **70** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | API 网关与中转、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 20.1k 🚀 +29/d | **68** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、通知提醒、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 3.8k 🚀 +31/d | **65** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 297 | **56** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、手机端访问；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 5.2k 🚀 +19/d | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 336 | **53** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 523 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟢 较易 | — | — | 330 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.7k 🚀 +4/d | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 547 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 跨 Agent 支持、API 网关与中转、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 311 | **51** |
| 🔹 **[Makson179/Bello](https://github.com/Makson179/Bello)** | 多智能体编排、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 364 | **50** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 自动故障转移、图形界面与桌面端、安全与隔离；兼容 Codex。 ‡ | 🔴 较重 | — | — | 971 | **48** |

**也能做这件事：** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[Folkbench/folkbench](https://github.com/Folkbench/folkbench)、[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 隔离与团队

*工作区隔离*

并行 Agent 会互相覆盖文件，除非各自有独立工作副本。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | 模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 13.9k 🚀 +358/d | **81** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 48.8k 🚀 +41/d | **71** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 12.6k 🚀 +25/d | **69** |
| ✅ **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | 图形界面与桌面端、MCP 支持、Agent 运行时；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 8.3k 🚀 +26/d | **67** |
| ✅ **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | 跨 Agent 支持、记忆与上下文、多智能体编排；兼容 Claude Code、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 5k | **63** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、MCP 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **60** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 719 🚀 +14/d | **59** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 659 🚀 +8/d | **57** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | 两个 AI Agent 做同一个任务：一个写代码，另一个审查。 自带端点 — 导入其他 Agent 的配置（opencode、codex、claude、kimi、pi、omp、gemini、killi）、手动添加密钥，或用 ChatGPT、Command Code、OpenCode Go、Muse Code 订阅登录 | 🟢 较易 | — | ✅ | 390 | **57** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 334 | **55** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 787 | **52** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排、可自托管。 ‡ | 🟢 较易 | ✅ | — | 6k | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、记忆与上下文、模型与供应商路由；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 3k | **49** |

**也能做这件事：** [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[johannesjo/parallel-code](https://github.com/johannesjo/parallel-code)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Agent 运行时、技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 7.9k 🚀 +162/d | **84** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 4.9k 🚀 +144/d | **82** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | 手机端访问、MCP 支持、模型与供应商路由；兼容 OpenCode。 ‡ | 🟢 较易 | — | ✅ | 8.9k 🚀 +120/d | **81** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 46.2k 🚀 +51/d | **71** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Agent 运行时、跨 Agent 支持、可自托管；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4.4k 🚀 +49/d | **69** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy 是一个开源、开箱即用的 AI Agent。连接你的多台电脑与手机，把熟悉的 Agent、模型和已有订阅放在一起，培养一个懂你工作方式的伙伴。 | 🔴 较重 | — | — | 10.3k 🚀 +64/d | **68** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 图形界面与桌面端、MCP 支持、通知提醒；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 5.5k | **64** |
| ✅ **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 3.9k 🚀 +36/d | **62** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | 独立账号平台与中转站：OpenRouter、Kimi 开放平台（国内/国际版）、AnyRouter、AgentRouter、AIHubMix、老张 API、Dahl、FoxCode、肖恩 AI、Cubence、RightCode、Grsai、FreeModel、SharedChat、WONG公益站、Krill AI、EMRank、RelayFor、Daya API、Verce… 账号站点兼容架构… | 🟡 需配置 | — | ✅ | 5.1k | **60** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、MCP 支持、可自托管。 ‡ | 🔴 较重 | — | — | 12.1k 🚀 +32/d | **57** |
| 🔹 **[yacuo/check-cc](https://github.com/yacuo/check-cc)** | 图形界面与桌面端；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.5k (+27/d) | **56** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **53** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 417 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 847 | **50** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 453 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[decolua/9router](https://github.com/decolua/9router)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[Licoy/Quosparr](https://github.com/Licoy/Quosparr)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

## 故障转移

*Agent 运行时*

它本身就是那个 Agent——你直接运行和对话的东西——而不是挂在别人 Agent 上的插件。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 156k 🚀 +117/d | **89** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 6k 🚀 +123/d | **86** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 20.6k 🚀 +549/d | **85** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 99 种影片风格，交给你的编程 agent。挑一个风格，带上你的故事，agent 用代码把整支片做出来。 | 🟡 需配置 | — | ✅ | 17.6k 🚀 +491/d | **85** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. † | 🟢 较易 | — | — | 23.6k 🚀 +191/d | **78** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 9.4k 🚀 +79/d | **78** |
| 🔹 **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 5.2k 🚀 +41/d | **61** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 11.5k 🚀 +26/d | **60** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | 多智能体编排、跨 Agent 支持、团队协作；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.8k | **58** |
| 🔹 **[chipfighter/context-attachment-manager](https://github.com/chipfighter/context-attachment-manager)** | Agent 每发一条消息，通常会把之前所有的图再发一遍，图一多，对话就越来越慢，最后可能发不出去。 这个插件给每张图编号（IMG-001、IMG-002……），之前的图改成发一段简短的占位： | 🟢 较易 | — | — | 805 🚀 +15/d | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 557 | **55** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. † | 🟢 开箱即用 | ✅ | — | 359 | **53** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | 想法或现有代码 → 经过验证的 PRD → 功能 → 规则 → 有序的 RFC → 经过评审和测试的代码 | 🟢 较易 | — | — | 311 | **53** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | 编译目标为 Android 12（API 31）及以上；实际可用的最低版本未测试 电脑上有 adb 和 Python 3.9+（只用标准库） | 🟢 开箱即用 | ✅ | — | 774 | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 726 | **50** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 487 | **45** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)、[garrytan/gstack](https://github.com/garrytan/gstack)、[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)、[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)、[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)、[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)、[langfuse/langfuse](https://github.com/langfuse/langfuse)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)

## 并行

*并行执行*

任务串行执行、只能干等；并行能压缩总耗时。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 67.8k 🚀 +228/d | **91** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、技能与插件、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 34.3k 🚀 +20/d | **70** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 28.1k 🚀 +17/d | **69** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | MCP 支持、通知提醒、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | ✅ | 564 | **54** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 跨 Agent 支持、工作区隔离、通知提醒；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 8.5k | **53** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、技能与插件、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 974 | **53** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote 通过 pi 官方扩展 API 接入正在运行的 pi 会话，不修改 pi 源码，不接管终端。 会话始终由本机的 pi 进程持有；浏览器端看到的是同一会话的实时镜像，并可向该会话发送消息与命令，包括切换模型、调整思考级别、压缩上下文、管理会话树等。 | 🟢 较易 | — | — | 333 | **52** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 计费与计量、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、远程控制、工作区隔离；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 324 | **47** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟡 需配置 | — | — | 478 | **46** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)、[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)、[felinics/Memoh](https://github.com/felinics/Memoh)、[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)、[cordum-io/cordum](https://github.com/cordum-io/cordum)、[crshdn/mission-control](https://github.com/crshdn/mission-control)、[solo-agent/solo](https://github.com/solo-agent/solo)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. † | 🟢 开箱即用 | ✅ | ✅ | 227.5k 🚀 +232/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 16.8k 🚀 +174/d | **89** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm 让你的编程智能体来做视频，也让你亲手修改。 一个真正的剪辑器。 可以移动、缩放、旋转页面里的任何元素，改它的文字、颜色和样式；摆放、裁剪、调整每个片段的 | 🟢 较易 | — | ✅ | 8k 🚀 +433/d | **81** |
| ✅ **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | 在本地管理你的编码 agent（Claude Code、Codex、Cursor、Devin、Grok、Hermes、Pi、Antigravity），也可以打开多设备同步。 | 🟢 开箱即用 | ✅ | ✅ | 3.7k 🚀 +42/d | **66** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.4k 🚀 +5/d | **58** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.3k 🚀 +21/d | **56** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 497 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 801 | **53** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | 对接其他产品是一个部署在流程后端地址之后的独立服务，不进入本仓库： 新增语音厂商加的是一个 profile，而不是一个新客户端： | 🟡 需配置 | — | — | 669 🚀 +13/d | **53** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | MCP 支持、技能与插件。 ‡ | 🟡 需配置 | — | — | 643 | **38** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[yetone/magpie](https://github.com/yetone/magpie)、[openai/codex](https://github.com/openai/codex)、[qybaihe/bla](https://github.com/qybaihe/bla)、[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)、[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[xerj-org/xerj](https://github.com/xerj-org/xerj)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)

## 故障转移

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 7.2k 🚀 +58/d | **76** |
| ✅ **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | 技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 7.1k 🚀 +61/d | **75** |
| ✅ **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.1k 🚀 +117/d | **73** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | 图形界面与桌面端、MCP 支持、API 网关与中转。 ‡ | 🟡 需配置 | — | — | 9.7k 🚀 +29/d | **65** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.8k 🚀 +8/d | **63** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 2.1k 🚀 +11/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Node 22+ LTS（用于钩子脚本 — 通常与 Claude Code / Codex / Gemini CLI 一起已安装） /om-review-brief 通过汇总所有内容生成完整的评估简报：成就记录、决策、事件、能力证据和 1:1 反馈 | 🟡 需配置 | — | — | 5.5k | **58** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 图形界面与桌面端、记忆与上下文、技能与插件；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.9k | **55** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 8k 🚀 +7/d | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace 为 LLM Agent 提供持久化、可检索、可审计的外部记忆，让每次对话都能在之前的基础上继续，而不是从零开始。 | 🟡 需配置 | — | — | 316 | **44** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[openai/codex](https://github.com/openai/codex)、[garrytan/gstack](https://github.com/garrytan/gstack)、[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 155.2k 🚀 +256/d | **94** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 跨 Agent 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 4.7k 🚀 +24/d | **68** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.5k 🚀 +22/d | **59** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | 跨 Agent 支持、可自托管、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 4.4k 🚀 +8/d | **57** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 936 | **56** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 777 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 441 | **50** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 605 | **45** |

**也能做这件事：** [sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

## 共享

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 168.9k 🚀 +214/d | **96** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 7.5k 🚀 +474/d | **89** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | 通知提醒、MCP 支持、图形界面与桌面端；兼容 Codex、OpenCode、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 24.6k 🚀 +607/d | **88** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | 图形界面与桌面端、记忆与上下文、API 网关与中转；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 9.8k 🚀 +188/d | **87** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.3k 🚀 +28/d | **66** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | 工作区隔离、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 463 | **55** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | 跨 Agent 支持、自动故障转移、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 2.2k | **51** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[leepokai/Codync](https://github.com/leepokai/Codync)、[slopus/happy](https://github.com/slopus/happy)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)

## 共享

*配额共享与分发*

订阅容量超过个人所需，想安全地分给他人共用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 108k 🚀 +147/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 83.2k 🚀 +221/d | **90** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.4k 🚀 +13/d | **64** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、模型与供应商路由；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 563 | **49** |

**也能做这件事：** [nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[yetone/cumora](https://github.com/yetone/cumora)

## 账号

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 135.6k 🚀 +126/d | **89** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.9k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | 跨 Agent 支持、API 网关与中转、图形界面与桌面端；兼容 Codex、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 566 | **54** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[cita-777/metapi](https://github.com/cita-777/metapi)、[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.24 倍（37,977 vs 155,150） |

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
| **[1llu50ry/Decompile](https://github.com/1llu50ry/decompile)** | **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 141.74x the stars (81,925 vs 578) | 🤖 自动（high） |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 62.14x the stars (20,070 vs 323) | 🤖 自动（high） |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 27.45x the stars (12,160 vs 443) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.97x the stars (20,070 vs 2,519) | 🤖 自动（high） |
| **[GizClaw/flowcraft](https://github.com/gizclaw/flowcraft)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 4.17x the stars (1,715 vs 411) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.42x the stars (34,338 vs 384) | 🤖 自动（high） |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 40.84x the stars (37,977 vs 930) | 🤖 自动（high） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.48x the stars (12,160 vs 2,219) | 🤖 自动（high） |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 151.55x the stars (49,860 vs 329) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.88x the stars (34,338 vs 931) | 🤖 自动（high） |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 133.67x the stars (49,860 vs 373) | 🤖 自动（high） |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 142.46x the stars (49,860 vs 350) | 🤖 自动（high） |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[JetBrains/thinkrail](https://github.com/jetbrains/thinkrail)** | 23.58x the stars (8,322 vs 353) | 🤖 自动（high） |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 100.40x the stars (30,422 vs 303) | 🤖 自动（high） |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.28x the stars (49,860 vs 3,755) | 🤖 自动（high） |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.33x the stars (12,160 vs 2,282) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.03x the stars (49,860 vs 372) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.75x the stars (12,160 vs 423) | 🤖 自动（high） |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 49.15x the stars (24,233 vs 493) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 156.30x the stars (49,860 vs 319) | 🤖 自动（high） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 484.96x the stars (305,037 vs 629) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.74x the stars (305,037 vs 6,258) | 🤖 自动（high） |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 157.99x the stars (155,150 vs 982) | 🤖 自动（high） |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 56.49x the stars (24,233 vs 429) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 100.98x the stars (141,870 vs 1,405) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.20x the stars (12,160 vs 2,893) | 🤖 自动（high） |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | **[decolua/9router](https://github.com/decolua/9router)** | 4.70x the stars (32,544 vs 6,927) | 🤖 自动（medium） |
| **[oracle/mcp](https://github.com/oracle/mcp)** | **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 169.62x the stars (81,925 vs 483) | 🤖 自动（medium） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.29x the stars (28,106 vs 582) | 🤖 自动（medium） |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.72x the stars (1,497 vs 550) | 🤖 自动（high） |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 11.67x the stars (168,934 vs 14,480) | 🤖 自动（high） |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/projectatlas)** | **[JetBrains/thinkrail](https://github.com/jetbrains/thinkrail)** | 16.35x the stars (8,322 vs 509) | 🤖 自动（medium） |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 32.62x the stars (19,181 vs 588) | 🤖 自动（medium） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.51x the stars (1,497 vs 426) | 🤖 自动（medium） |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.47x the stars (24,233 vs 5,421) | 🤖 自动（medium） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.43x the stars (1,186 vs 489) | 🤖 自动（high） |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 74.31x the stars (49,860 vs 671) | 🤖 自动（medium） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.72x the stars (1,497 vs 550) | 🤖 自动（medium） |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[JetBrains/thinkrail](https://github.com/jetbrains/thinkrail)** | 5.46x the stars (8,322 vs 1,524) | 🤖 自动（high） |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 4.76x the stars (8,207 vs 1,724) | 🤖 自动（high） |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 17.82x the stars (5,541 vs 311) | 🤖 自动（high） |
| **[Leonxlnx/earshot](https://github.com/leonxlnx/earshot)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 22.61x the stars (114,478 vs 5,063) | 🤖 自动（high） |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 24.06x the stars (305,037 vs 12,678) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.73x the stars (1,497 vs 867) | 🤖 自动（high） |
| **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 12.32x the stars (49,860 vs 4,046) | 🤖 自动（high） |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 2.75x the stars (12,490 vs 4,544) | 🤖 自动（medium） |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/blender-ai-mcp-suite)** | **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 164.51x the stars (81,925 vs 498) | 🤖 自动（high） |
| **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 22.67x the stars (114,478 vs 5,049) | 🤖 自动（medium） |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,860 vs 28,090) | 🤖 自动（medium） |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,096 vs 518) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui-2 | 28.1k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[tonhowtf/omniget](https://github.com/tonhowtf/omniget)** | sharing | 14.5k | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (5/5)。 |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | teams-self-hosting | 12.7k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (9/9)。 |
| **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | billing | 6.9k | 🔻 已被取代 | 已被 decolua/9router 取代：covers 100% of capabilities (4/4)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | teams-self-hosting | 6.3k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.4k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (9/9)。 |
| **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | mobile | 5.1k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)** | mobile | 5k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (5/5)。 |
| **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | teams-self-hosting | 4.5k | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[arjun988/blender-skills](https://github.com/arjun988/blender-skills)** | desktop-ui-2 | 4k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui-2 | 3.8k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams-self-hosting | 2.9k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (8/8)。 |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams-self-hosting | 2.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams-self-hosting | 2.2k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | sessions-memory | 1.7k | 🔻 已被取代 | 已被 Gentleman-Programming/engram 取代：covers 100% of capabilities (4/4)。 |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation-teams | 1.5k | 🔻 已被取代 | 已被 JetBrains/thinkrail 取代：covers 100% of capabilities (5/5)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile | 1.4k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 982 | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism | 931 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 930 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (4/4)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | sessions-memory | 867 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui-2 | 671 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | teams-self-hosting | 629 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | sessions-memory | 588 | 🔻 已被取代 | 已被 xerj-org/xerj 取代：covers 100% of capabilities (4/4)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism | 582 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (4/4)。 |
| **[1llu50ry/Decompile](https://github.com/1llu50ry/Decompile)** | mcp-security | 578 | 🔻 已被取代 | 已被 ruvnet/ruflo 取代：covers 100% of capabilities (7/7)。 |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | sessions-memory | 550 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | sessions-memory | 550 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui-2 | 518 | 🔻 已被取代 | 已被 data-goblin/power-bi-agentic-development 取代：covers 100% of capabilities (6/6)。 |
| **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | isolation-teams | 509 | 🔻 已被取代 | 已被 JetBrains/thinkrail 取代：covers 100% of capabilities (6/6)。 |
| **[findavoulot1973/Blender-AI-MCP-Suite](https://github.com/findavoulot1973/Blender-AI-MCP-Suite)** | mcp-security | 498 | 🔻 已被取代 | 已被 ruvnet/ruflo 取代：covers 100% of capabilities (4/4)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 493 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (5/5)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions-memory | 489 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[oracle/mcp](https://github.com/oracle/mcp)** | mcp-security | 483 | 🔻 已被取代 | 已被 ruvnet/ruflo 取代：covers 100% of capabilities (5/5)。 |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | teams-self-hosting | 443 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 429 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (8/8)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | sessions-memory | 426 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams-self-hosting | 423 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | isolation-teams | 411 | 🔻 已被取代 | 已被 pedrohcgs/claude-code-my-workflow 取代：covers 100% of capabilities (5/5)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism | 384 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui-2 | 373 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui-2 | 372 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | isolation-teams | 353 | 🔻 已被取代 | 已被 JetBrains/thinkrail 取代：covers 100% of capabilities (7/7)。 |
| **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | desktop-ui-2 | 350 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | desktop-ui-2 | 329 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 323 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui-2 | 319 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | billing-2 | 311 | 🔻 已被取代 | 已被 aipoch/open-science 取代：covers 100% of capabilities (4/4)。 |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams-self-hosting | 303 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-11-17 13:27 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
