<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**220 个工具**，分 **14 个分类** · **51 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-27 09:54 UTC**

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
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 155 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 6 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 记忆与MCP

*记忆与上下文*

每次新会话都从零开始，记不住项目约定。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 290.2k 🚀 +844/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 21k 🚀 +204/d | **88** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 面向 AI 智能体的本地优先搜索引擎与 MCP 服务。 一个 Rust 二进制程序即可为代码、文档、日志、JSONL/CSV 和 PDF 建立索引，提供 BM25 全文、向量与混合搜索、代码搜索和智能体记忆，接口兼容 Elasticsearch API。 | 🟢 较易 | — | — | 17k 🚀 +801/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 11k 🚀 +120/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 13.9k 🚀 +217/d | **82** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 使用 ChatGPT 网页版的独立额度，不消耗 Work 或 Codex 额度。 | 🟢 较易 | — | — | 15.1k 🚀 +58/d | **72** |
| ✅ **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、API 网关与中转、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.7k 🚀 +61/d | **70** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 32.8k 🚀 +30/d | **69** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 57.8k 🚀 +6/d | **67** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 8.7k 🚀 +64/d | **66** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | English README · 5 分钟快速开始 · 我想重构项目 每一项：worktree → implementer 改 → 独立 verifier 跑测试 → 你 审 PR。 | 🟢 开箱即用 | ✅ | — | 11.6k 🚀 +8/d | **62** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k | **62** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k 🚀 +18/d | **61** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | 多智能体编排、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.4k | **60** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 4k 🚀 +28/d | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | 通知提醒、并行执行、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | 跨 Agent 支持、安全与隔离；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k | **57** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.2k 🚀 +10/d | **57** |
| 🔹 **[1llu50ry/mcp-gamehacking](https://github.com/1llu50ry/mcp-gamehacking)** | 跨 Agent 支持、多智能体编排、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 385 🚀 +18/d | **57** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.1k | **55** |
| 🔹 **[graygnatconsole/mcp-audit-tool](https://github.com/graygnatconsole/mcp-audit-tool)** | 跨 Agent 支持、工作区隔离；兼容 Cursor、Copilot、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 544 | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、多智能体编排；兼容 Cursor、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 468 | **55** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 16.7k 🚀 +13/d | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | 技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 414 | **54** |
| 🔹 **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | 多智能体编排、跨 Agent 支持、会话持久化；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 224 | **53** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | 跨 Agent 支持、自动故障转移、会话持久化；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 440 | **52** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | 跨 Agent 支持、Agent 运行时、安全与隔离；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 330 | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 497 | **51** |
| 🔹 **[GMaN1911/claude-cognitive](https://github.com/GMaN1911/claude-cognitive)** | 跨 Agent 支持；兼容 Claude Code、Gemini CLI、Cursor、Aider。 ‡ | 🟡 需配置 | — | — | 451 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **51** |

*还有 8 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[garrytan/gstack](https://github.com/garrytan/gstack)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

## 桌面端

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 153.5k 🚀 +139/d | **90** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 177.6k 🚀 +1040/d | **87** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 103.3k 🚀 +492/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 21.2k 🚀 +487/d | **83** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 图形界面与桌面端、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 49.1k 🚀 +2274/d | **82** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 7.3k 🚀 +91/d | **80** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 5.5k 🚀 +103/d | **76** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | ✅ | — | 4.9k 🚀 +84/d | **69** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | MCP 支持、通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 10.8k 🚀 +51/d | **67** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 跨 Agent 支持、通知提醒、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.4k 🚀 +25/d | **66** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +50/d | **65** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 7k 🚀 +25/d | **61** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. † | 🟢 开箱即用 | ✅ | — | 6.2k 🚀 +24/d | **59** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | 跨 Agent 支持、团队协作；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.7k | **59** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | MCP 支持、图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.7k | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 898 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 541 | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 并行执行；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | ✅ | 510 | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | 通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 343 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、OpenCode、Copilot、Goose。 ‡ | 🟢 较易 | — | — | 440 | **52** |
| 🔹 **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | 跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 368 | **52** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | 跨 Agent 支持、MCP 支持、计费与计量；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 292 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Analyze + Generate：先提取视觉系统，再生成不复制原图构图的新作品。 Generate：内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。 | 🟡 需配置 | — | — | 7.4k 🚀 +5/d | **51** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 910 | **51** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | 想法或现有代码 → 经过验证的 PRD → 功能 → 规则 → 有序的 RFC → 经过评审和测试的代码 | 🟢 较易 | — | — | 305 | **51** |

*还有 9 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [anomalyco/opencode](https://github.com/anomalyco/opencode)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[garrytan/gstack](https://github.com/garrytan/gstack)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)、[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)、[leepokai/Codync](https://github.com/leepokai/Codync)

## 移动端与远程控制

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 107.5k 🚀 +1105/d | **92** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 107.8k 🚀 +385/d | **89** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 137.9k 🚀 +124/d | **88** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 22.2k 🚀 +103/d | **83** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 6.6k 🚀 +88/d | **79** |
| ✅ **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | 可自托管、MCP 支持、安全与隔离。 ‡ | 🟡 需配置 | — | — | 7.3k 🚀 +75/d | **74** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | 通知提醒、MCP 支持、跨 Agent 支持；兼容 Codex、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 5.7k 🚀 +65/d | **74** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | MCP 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 84.5k 🚀 +39/d | **73** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 33.8k 🚀 +24/d | **72** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | 跨 Agent 支持、通知提醒、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 9.1k 🚀 +28/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、可自托管、Agent 运行时。 ‡ | 🟢 较易 | ✅ | ✅ | 8.3k 🚀 +39/d | **68** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 图形界面与桌面端、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 11.1k 🚀 +18/d | **67** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、MCP 支持、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.2k 🚀 +16/d | **65** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | MiMoCode 是一个终端原生的 AI 编程助手。它能读写代码、执行命令、管理 Git，通过持久化记忆系统，在多次会话间保持对你项目的深度理解，并自我进化。 | 🟢 较易 | — | — | 13.7k 🚀 +8/d | **63** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 图形界面与桌面端、跨 Agent 支持、安全与隔离；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 5.4k 🚀 +9/d | **63** |
| 🔹 **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | MCP 支持、图形界面与桌面端、安全与隔离。 ‡ | 🔴 较重 | — | — | 3k 🚀 +48/d | **59** |
| 🔹 **[leepokai/Codync](https://github.com/leepokai/Codync)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 939 | **58** |
| 🔹 **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 多智能体编排、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.4k | **57** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 工作区隔离、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.2k 🚀 +6/d | **57** |
| 🔹 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | 从手机、电脑、浏览器继续使用你的 DeepSeek Harness 实例。 当前开发适配基线为 dsh-v0.2.1-rc.1，验证范围见兼容性说明。 | 🟢 较易 | — | — | 888 🚀 +12/d | **56** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | MCP 支持、跨 Agent 支持、安全与隔离；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 785 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 工作区隔离、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 320 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | 工作区隔离、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 423 | **54** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 788 | **53** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、通知提醒、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 309 | **52** |
| 🔹 **[autohandai/code-cli](https://github.com/autohandai/code-cli)** | 技能与插件、跨 Agent 支持、安全与隔离；兼容 Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 211 | **52** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 2.9k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 通知提醒、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **51** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 304 | **49** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[slopus/happy](https://github.com/slopus/happy)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)

## 共享

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 23.2k 🚀 +798/d | **89** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 131.1k 🚀 +142/d | **89** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 31.5k 🚀 +59/d | **72** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 10.1k 🚀 +51/d | **69** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 计费与计量、图形界面与桌面端、跨 Agent 支持；兼容 Codex、OpenCode、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 19.4k 🚀 +35/d | **69** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 18k 🚀 +39/d | **67** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.8k | **56** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.6k 🚀 +15/d | **55** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.8k 🚀 +12/d | **55** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 跨 Agent 支持、计费与计量、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 549 🚀 +19/d | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 505 | **52** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 264 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、计费与计量；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 308 | **50** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | 跨 Agent 支持、MCP 支持、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 210 | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 908 | **49** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 计费与计量、自动故障转移、图形界面与桌面端；兼容 Codex。 ‡ | 🔴 较重 | — | — | 332 🚀 +14/d | **49** |
| 🔹 **[youssefvdel/qwengate](https://github.com/youssefvdel/qwengate)** | 跨 Agent 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、OpenCode、Cursor、Qwen Code。 ‡ | 🟢 较易 | — | — | 205 | **46** |
| 🔹 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | 支持导入当前登录账号、手动粘贴 Token、OAuth 文件快速导入 配额看板与自动刷新（5H / 7D）、低额度提醒与切换提示 | 🟡 需配置 | — | — | 250 | **45** |
| 👀 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 计费与计量、技能与插件、模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 219 | **43** |

**也能做这件事：** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[spinabot/brigade](https://github.com/spinabot/brigade)、[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[cita-777/metapi](https://github.com/cita-777/metapi)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)、[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

## 隔离

*工作区隔离*

并行 Agent 会互相覆盖文件，除非各自有独立工作副本。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.7k 🚀 +23/d | **70** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 9.5k 🚀 +28/d | **69** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | 跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 8.3k 🚀 +34/d | **66** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **59** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 583 | **57** |
| 🔹 **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | 跨 Agent 支持、MCP 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 625 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | MCP 支持、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 460 | **55** |
| 🔹 **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | 技能与插件、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 345 | **55** |
| 🔹 **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | 为 AI 编程 agent 设计的 Git worktree 工作流工具。提供隔离的并行开发环境。 Run 引擎："即用即删"工作流 — 创建 worktree、运行 agent、合并、清理。 | 🟡 需配置 | ✅ | — | 281 | **51** |
| 🔹 **[lanes-sh/app](https://github.com/lanes-sh/app)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 276 | **48** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |
| 👀 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | 跨 Agent 支持、图形界面与桌面端、远程控制；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | ✅ | 272 | **43** |
| 👀 **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | 把 AI Coding 从 prompt 实验，升级为可审查、可验证、可交付的工程工作流。 读第 1-2 章，理解“写字符”到“管理 Agent 注意力”的角色变化。 | 🟢 较易 | — | — | 242 | **41** |
| 👀 **[owengretzinger/constellagent](https://github.com/owengretzinger/constellagent)** | 图形界面与桌面端。 ‡ | 🟢 较易 | — | ✅ | 217 | **38** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[yc-software/qm](https://github.com/yc-software/qm)、[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[automazeio/ccpm](https://github.com/automazeio/ccpm)

## 模型路由

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 77.7k 🚀 +252/d | **89** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 一套用代码做片的风格工具箱： 59 种现成风格，也能做出你自己的。 拿来做什么：做什么片、发在哪个平台（竖屏就用 1080×1920 或 1080×1440），有没有品牌色、logo、字体或固定角色； | 🟡 需配置 | — | ✅ | 8.4k 🚀 +651/d | **82** |
| 🏆 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 3.8k 🚀 +150/d | **78** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 10.8k 🚀 +50/d | **68** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.5k 🚀 +32/d | **66** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、跨 Agent 支持、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 10.8k 🚀 +37/d | **65** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. † | 🟡 需配置 | — | — | 11.2k 🚀 +10/d | **59** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟢 较易 | — | — | 1.9k 🚀 +10/d | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. † | 🟢 开箱即用 | ✅ | — | 344 | **53** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 5.6k | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 713 | **50** |
| 🔹 **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cline / Roo。 ‡ | 🟢 较易 | — | — | 629 | **49** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | 跨 Agent 支持、技能与插件；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 470 | **45** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[yetone/magpie](https://github.com/yetone/magpie)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[zai-org/ZCode](https://github.com/zai-org/ZCode)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)

## 团队

*团队协作*

多人需要共用一套 Agent 环境，还要有角色与边界。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 164.4k 🚀 +267/d | **98** |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 61.6k 🚀 +358/d | **90** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 11.2k 🚀 +103/d | **84** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 13.9k 🚀 +265/d | **84** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.5k 🚀 +10/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.8k 🚀 +6/d | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4k | **54** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 跨 Agent 支持、通知提醒、工作区隔离；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 8.4k | **54** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、远程控制、工作区隔离；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 320 | **48** |

**也能做这件事：** [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[jmagly/aiwg](https://github.com/jmagly/aiwg)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | MCP 支持、技能与插件、模型与供应商路由；兼容 Gemini CLI。 ‡ | 🟢 较易 | — | — | 108.6k 🚀 +213/d | **91** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、可自托管；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 6.3k 🚀 +74/d | **77** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 44.9k 🚀 +70/d | **75** |
| ✅ **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、通知提醒、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 3k 🚀 +45/d | **67** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、MCP 支持、可自托管。 ‡ | 🔴 较重 | — | — | 11.7k 🚀 +25/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 286 | **55** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 通知提醒、API 网关与中转、跨 Agent 支持；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 323 | **52** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 407 | **50** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 跨 Agent 支持、API 网关与中转、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 227 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **48** |
| 🔹 **[nextlevelbuilder/skillx](https://github.com/nextlevelbuilder/skillx)** | 技能与插件、图形界面与桌面端、MCP 支持。 ‡ | 🟡 需配置 | — | — | 192 | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 434 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[decolua/9router](https://github.com/decolua/9router)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[Licoy/Quosparr](https://github.com/Licoy/Quosparr)、[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)、[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)、[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

## 故障转移

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 149.2k 🚀 +344/d | **93** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 4.3k 🚀 +106/d | **85** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.6k 🚀 +15/d | **67** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi 为运行服务会处理有限的账户与技术信息；存在的分析均已披露且可关闭。 | 🟢 较易 | — | — | 3.2k 🚀 +38/d | **66** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 1.8k 🚀 +14/d | **62** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 只需向 Claude Code、Codex、OpenCode 或 DeepSeek Harness 给出一次目标，即可让它跨桌面 App 与终端持续工作数十个小时。 | 🟢 较易 | — | — | 1.8k | **59** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | — | 5.1k 🚀 +6/d | **56** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 7.8k 🚀 +9/d | **50** |
| 🔹 **[api7/aisix](https://github.com/api7/aisix)** | MCP 支持、可自托管、团队协作。 ‡ | 🟡 需配置 | — | — | 207 | **49** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace 为 LLM Agent 提供持久化、可检索、可审计的外部记忆，让每次对话都能在之前的基础上继续，而不是从零开始。 | 🟡 需配置 | — | — | 314 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、记忆与上下文、会话持久化；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 520 | **43** |

**也能做这件事：** [affaan-m/ECC](https://github.com/affaan-m/ECC)、[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Agent 运行时；兼容 OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 222.1k 🚀 +447/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. † | 🟢 开箱即用 | ✅ | ✅ | 10.9k 🚀 +374/d | **88** |
| ✅ **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.1k 🚀 +314/d | **76** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill 把你的 AI Agent 连接到 Chrome 或 Microsoft Edge，直接使用你已有的登录状态。 | 🟢 较易 | — | — | 9.7k 🚀 +56/d | **71** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.2k 🚀 +16/d | **63** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 475 | **56** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | — | 522 🚀 +8/d | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 767 | **54** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 487 🚀 +9/d | **53** |
| 👀 **[wong2/diffx](https://github.com/wong2/diffx)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 217 | **42** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | 技能与插件。 ‡ | 🟡 需配置 | — | — | 642 | **38** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[yetone/magpie](https://github.com/yetone/magpie)、[xerj-org/xerj](https://github.com/xerj-org/xerj)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[google/artemis](https://github.com/google/artemis)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)、[makecindy/cindy](https://github.com/makecindy/cindy)

## 移动端

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | 跨 App 自动化：根据自然语言指令，在 Android 上执行测试流程和日常任务。 AndroidWorld 结果：在 Google Research AndroidWorld 基准评测（100+ 多步任务）中取得 99%+ 任务完成率。 | 🟡 需配置 | — | — | 15.1k 🚀 +278/d | **82** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 3.3k 🚀 +85/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | ✅ | 24.3k 🚀 +16/d | **64** |
| 🔹 **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | 在你自己的本地 Agent 上运行 Claude Design —— Cursor、Claude Code、Claude Desktop，或任何能读写文件的编码 Agent。 | 🟢 开箱即用 | ✅ | — | 4.5k 🚀 +12/d | **60** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | 记忆与上下文、通知提醒。 ‡ | 🟡 需配置 | — | — | 3.6k 🚀 +9/d | **54** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟡 需配置 | — | — | 1.1k | **51** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | 远程控制、Agent 运行时、多智能体编排。 ‡ | 🟢 较易 | — | — | 470 | **50** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[makecindy/cindy](https://github.com/makecindy/cindy)、[loopx-project/loopx](https://github.com/loopx-project/loopx)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)、[yetone/cumora](https://github.com/yetone/cumora)、[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 4.1k 🚀 +29/d | **69** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 871 | **56** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.3k 🚀 +6/d | **55** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、OpenCode。 ‡ | 🟢 较易 | — | — | 983 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 760 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 434 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、多智能体编排；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 511 | **52** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[loopx-project/loopx](https://github.com/loopx-project/loopx)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | 她本身（Source）——审计、fork、二次开发，把通用改进以 Apache-2.0 贡献回来。 移动端未注入 TapDB 配置（clientId / clientToken）时不会初始化 SDK。 | 🔴 较重 | — | — | 7k 🚀 +73/d | **69** |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | 以本地为核心的研究智能体执行框架和工作空间。 | 🟢 开箱即用 | ✅ | — | 7.6k 🚀 +29/d | **65** |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | 2026-08-02 · ⏱️ 200+ 小时长程轨迹在 X 公开分享 — 早期 owner-run 案例跨越 200+ 小时自然时长，展示执行、等待、人工决策与恢复的衔接，并在 X 获得广泛传播。 2026-09-06 · 🎉 LoopX 1.0 — 个人 Agent 工作区：跨会话跟进 Agent 工作、处理待决事项、核对交付结果。 | 🟢 较易 | — | — | 6.4k 🚀 +10/d | **65** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排、可自托管。 ‡ | 🟢 较易 | ✅ | — | 5.9k | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 安全与隔离、图形界面与桌面端、MCP 支持；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 524 | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 226 | **51** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

## 安全与自托管

*配额共享与分发*

订阅容量超过个人所需，想安全地分给他人共用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 104.3k 🚀 +212/d | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、模型与供应商路由；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 557 | **46** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api 是基于 Sub2API 二次开发的自托管 AI API 网关与订阅管理平台，提供账号池、API Key 管理、多供应商请求转发、用量计费、订阅充值、风控审查和后台运营能力。 | 🔴 较重 | — | — | 242 | **39** |

**也能做这件事：** [decolua/9router](https://github.com/decolua/9router)、[spinabot/brigade](https://github.com/spinabot/brigade)、[cordum-io/cordum](https://github.com/cordum-io/cordum)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)、[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)、[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.16 倍（23,215 vs 149,223） |

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
| **[AVIDS2/memorix](https://github.com/avids2/memorix)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 332.83x the stars (290,229 vs 872) | 🤖 自动（high） |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 59.33x the stars (19,400 vs 327) | 🤖 自动（high） |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 20.09x the stars (11,072 vs 551) | 🤖 自动（high） |
| **[Digital-Process-Tools/claude-remember](https://github.com/digital-process-tools/claude-remember)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 135.76x the stars (27,695 vs 204) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.05x the stars (19,400 vs 2,409) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 72.88x the stars (27,695 vs 380) | 🤖 自动（high） |
| **[Karanjot786/agent-skills-cli](https://github.com/karanjot786/agent-skills-cli)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 4.61x the stars (898 vs 195) | 🤖 自动（high） |
| **[KbWen/agentic-os](https://github.com/kbwen/agentic-os)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 125.89x the stars (27,695 vs 220) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 20.05x the stars (11,029 vs 550) | 🤖 自动（high） |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 562.46x the stars (290,229 vs 516) | 🤖 自动（high） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.20x the stars (11,165 vs 2,148) | 🤖 自动（high） |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 898.54x the stars (290,229 vs 323) | 🤖 自动（high） |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.19x the stars (22,186 vs 5,297) | 🤖 自动（high） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 3.90x the stars (1,107 vs 284) | 🤖 自动（high） |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 165.09x the stars (290,229 vs 1,758) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.59x the stars (27,695 vs 4,951) | 🤖 自动（high） |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.34x the stars (13,737 vs 400) | 🤖 自动（high） |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1209.29x the stars (290,229 vs 240) | 🤖 自动（high） |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 629.81x the stars (164,380 vs 261) | 🤖 自动（high） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 44.11x the stars (22,186 vs 503) | 🤖 自动（high） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 470.39x the stars (290,229 vs 617) | 🤖 自动（high） |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.33x the stars (149,223 vs 9,137) | 🤖 自动（high） |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 28.65x the stars (11,029 vs 385) | 🤖 自动（high） |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 34.89x the stars (19,400 vs 556) | 🤖 自动（high） |
| **[ndycode/oc-codex-multi-auth](https://github.com/ndycode/oc-codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 93.72x the stars (19,400 vs 207) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.57x the stars (290,229 vs 6,101) | 🤖 自动（high） |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 405.91x the stars (290,229 vs 715) | 🤖 自动（high） |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 605.91x the stars (290,229 vs 479) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 4.08x the stars (5,723 vs 1,403) | 🤖 自动（high） |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.44x the stars (11,165 vs 1,323) | 🤖 自动（medium） |
| **[sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 54.33x the stars (11,029 vs 203) | 🤖 自动（medium） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.91x the stars (898 vs 309) | 🤖 自动（high） |
| **[ZipengWu365/TOMC](https://github.com/zipengwu365/tomc)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 41.62x the stars (11,029 vs 265) | 🤖 自动（medium） |
| **[YYHDBL/AgentCrew](https://github.com/yyhdbl/agentcrew)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 426.10x the stars (107,804 vs 253) | 🤖 自动（medium） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 599.65x the stars (290,229 vs 484) | 🤖 自动（medium） |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 94.08x the stars (290,229 vs 3,085) | 🤖 自动（medium） |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 19.95x the stars (27,695 vs 1,388) | 🤖 自动（medium） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 39.64x the stars (16,964 vs 428) | 🤖 自动（medium） |
| **[Lyellr88/marm-memory](https://github.com/lyellr88/marm-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 684.50x the stars (290,229 vs 424) | 🤖 自动（medium） |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 318.23x the stars (290,229 vs 912) | 🤖 自动（medium） |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 611.01x the stars (290,229 vs 475) | 🤖 自动（medium） |
| **[garagon/nanostack](https://github.com/garagon/nanostack)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 520.79x the stars (107,804 vs 207) | 🤖 自动（medium） |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 38.60x the stars (290,229 vs 7,519) | 🤖 自动（medium） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.46x the stars (898 vs 365) | 🤖 自动（high） |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 2.13x the stars (1,107 vs 519) | 🤖 自动（medium） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.56x the stars (898 vs 575) | 🤖 自动（high） |
| **[Dataojitori/nocturne_memory](https://github.com/dataojitori/nocturne_memory)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 8.05x the stars (11,360 vs 1,411) | 🤖 自动（high） |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.51x the stars (22,186 vs 6,322) | 🤖 自动（medium） |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.20x the stars (898 vs 408) | 🤖 自动（high） |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.17x the stars (1,072 vs 495) | 🤖 自动（medium） |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.19x the stars (898 vs 755) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | failover | 9.1k | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (7/7)。 |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | memory-mcp | 7.5k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | mobile-remote-control | 6.3k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (5/5)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | memory-mcp | 6.1k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | mobile-remote-control | 5.3k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (7/7)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation | 5k | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (4/4)。 |
| **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | memory-mcp | 3.1k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (8/8)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (8/8)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | memory-mcp | 1.8k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (9/9)。 |
| **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | memory-mcp | 1.4k | 🔻 已被取代 | 已被 spinabot/brigade 取代：covers 100% of capabilities (7/7)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile-remote-control | 1.4k | 🔻 已被取代 | 已被 milind-soni/OpenMausBot 取代：covers 100% of capabilities (4/4)。 |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation | 1.4k | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (9/9)。 |
| **[hex/claude-council](https://github.com/hex/claude-council)** | memory-mcp | 912 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (7/7)。 |
| **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | memory-mcp | 872 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (10/10)。 |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | memory-mcp | 715 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | memory-mcp | 617 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | desktop-ui | 575 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 556 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (5/5)。 |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile-remote-control | 551 | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (7/7)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-mcp | 550 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (5/5)。 |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | desktop-ui | 519 | 🔻 已被取代 | 已被 abubakarsiddik31/claude-skills-collection 取代：covers 100% of capabilities (4/4)。 |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | memory-mcp | 516 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mobile-remote-control | 503 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (4/4)。 |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 495 | 🔻 已被取代 | 已被 data-goblin/power-bi-agentic-development 取代：covers 100% of capabilities (6/6)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | memory-mcp | 484 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | memory-mcp | 479 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | memory-mcp | 475 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | memory-mcp | 428 | 🔻 已被取代 | 已被 xerj-org/xerj 取代：covers 100% of capabilities (4/4)。 |
| **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | memory-mcp | 424 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (12/12)。 |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 408 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | mobile-remote-control | 400 | 🔻 已被取代 | 已被 XiaomiMiMo/MiMo-Code 取代：covers 100% of capabilities (8/8)。 |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | memory-mcp | 385 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation | 380 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 365 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | memory-mcp | 323 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 309 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 已被取代 | 已被 abubakarsiddik31/claude-skills-collection 取代：covers 100% of capabilities (4/4)。 |
| **[ZipengWu365/TOMC](https://github.com/ZipengWu365/TOMC)** | memory-mcp | 265 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (8/8)。 |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 261 | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (6/6)。 |
| **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | mobile-remote-control | 253 | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (6/6)。 |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | memory-mcp | 240 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (8/8)。 |
| **[KbWen/agentic-os](https://github.com/KbWen/agentic-os)** | isolation | 220 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (6/6)。 |
| **[ndycode/oc-codex-multi-auth](https://github.com/ndycode/oc-codex-multi-auth)** | sharing | 207 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (5/5)。 |
| **[garagon/nanostack](https://github.com/garagon/nanostack)** | mobile-remote-control | 207 | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (10/10)。 |
| **[Digital-Process-Tools/claude-remember](https://github.com/Digital-Process-Tools/claude-remember)** | isolation | 204 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills)** | memory-mcp | 203 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[Karanjot786/agent-skills-cli](https://github.com/Karanjot786/agent-skills-cli)** | desktop-ui | 195 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-27 09:54 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
