<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**215 个工具**，分 **15 个分类** · **57 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-24 08:56 UTC**

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
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 151 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 7 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 桌面端

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 153.2k 🚀 +180/d | **90** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 175k 🚀 +1521/d | **88** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 101.7k 🚀 +535/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 19.8k 🚀 +674/d | **85** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 13.3k 🚀 +166/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 图形界面与桌面端、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 42.7k 🚀 +2277/d | **82** |
| 🏆 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 3.7k 🚀 +335/d | **81** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | MCP 支持、通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 10.7k 🚀 +71/d | **71** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | ✅ | — | 4.6k 🚀 +98/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 8k 🚀 +25/d | **70** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 跨 Agent 支持、通知提醒、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.3k 🚀 +27/d | **68** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4k 🚀 +60/d | **67** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.4k 🚀 +32/d | **64** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 5k 🚀 +45/d | **64** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | English README · 5 分钟快速开始 · 我想重构项目 每一项：worktree → implementer 改 → 独立 verifier 跑测试 → 你 审 PR。 | 🟢 开箱即用 | ✅ | — | 11.6k 🚀 +8/d | **62** |
| 🔹 **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 7k 🚀 +44/d | **61** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. † | 🟢 开箱即用 | ✅ | — | 6.1k 🚀 +16/d | **58** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 3.9k 🚀 +23/d | **58** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 887 | **58** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | MCP 支持、图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.7k 🚀 +4/d | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.9k | **55** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.1k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1k | **55** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 540 | **55** |
| 🔹 **[Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.8k | **53** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | 通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 343 | **53** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Analyze + Generate：先提取视觉系统，再生成不复制原图构图的新作品。 Generate：内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。 | 🟡 需配置 | — | — | 7.4k 🚀 +10/d | **52** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |

*还有 13 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [anomalyco/opencode](https://github.com/anomalyco/opencode)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[garrytan/gstack](https://github.com/garrytan/gstack)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)、[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)

## 安全与自托管

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 47.4k (+197/d) | **87** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 4k 🚀 +111/d | **86** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 面向 AI 智能体的本地优先搜索引擎与 MCP 服务。 一个 Rust 二进制程序即可为代码、文档、日志、JSONL/CSV 和 PDF 建立索引，提供 BM25 全文、向量与混合搜索、代码搜索和智能体记忆，接口兼容 Elasticsearch API。 | 🟡 需配置 | — | — | 14.2k 🚀 +1096/d | **85** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 32.7k 🚀 +38/d | **71** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 29.8k 🚀 +35/d | **71** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | Hermes Agent 的一站式套件。安装一次，然后只需输入 dag-ulw。 Agent 看板与原生 Kanban 协作（agent/operator 参考） | 🟢 开箱即用 | ✅ | — | 3.6k 🚀 +33/d | **69** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.5k 🚀 +14/d | **67** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | 图形界面与桌面端、MCP 支持、API 网关与中转。 ‡ | 🟡 需配置 | — | — | 9.1k 🚀 +28/d | **65** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 8.5k 🚀 +58/d | **64** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.6k 🚀 +27/d | **64** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 1.7k 🚀 +21/d | **57** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | — | 5.1k 🚀 +5/d | **56** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | MCP 支持、技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 414 | **55** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 422 | **54** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 16.6k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 857 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | MCP 支持、跨 Agent 支持、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 437 | **52** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 676 | **51** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 7.8k 🚀 +11/d | **50** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | MCP 支持、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **49** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | MCP 支持、模型与供应商路由、技能与插件。 ‡ | 🔴 较重 | — | — | 500 | **49** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 247 | **45** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、用量分析；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 520 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[garrytan/gstack](https://github.com/garrytan/gstack)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[spinabot/brigade](https://github.com/spinabot/brigade)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)

## 自托管

*可自托管*

不希望代码或密钥经过他人的服务器。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 287.5k 🚀 +793/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 20.4k 🚀 +167/d | **88** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 10.7k 🚀 +139/d | **85** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 使用 ChatGPT 网页版的独立额度，不消耗 Work 或 Codex 额度。 | 🟢 较易 | — | — | 14.9k 🚀 +65/d | **73** |
| ✅ **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.7k 🚀 +71/d | **72** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 57.8k 🚀 +7/d | **67** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k | **62** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | 记忆与上下文、多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.4k | **60** |
| 🔹 **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | Agent 运行时、计费与计量、记忆与上下文。 ‡ | 🟡 需配置 | — | — | 2.2k | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | 通知提醒、并行执行、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.2k 🚀 +8/d | **57** |
| 🔹 **[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)** | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. † | 🟢 开箱即用 | ✅ | — | 2.6k 🚀 +6/d | **57** |
| 🔹 **[graygnatconsole/mcp-audit-tool](https://github.com/graygnatconsole/mcp-audit-tool)** | 跨 Agent 支持、工作区隔离；兼容 Cursor、Copilot、Cline / Roo。 ‡ | 🟢 较易 | — | — | 543 🚀 +21/d | **57** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、多智能体编排；兼容 Cursor、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 465 | **55** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | 跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 495 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **51** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | 多智能体编排、图形界面与桌面端。 ‡ | 🟢 较易 | — | ✅ | 1.2k | **47** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 283 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 图形界面与桌面端、多智能体编排、并行执行；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 2.7k | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时、多智能体编排。 ‡ | 🟡 需配置 | — | — | 415 | **45** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 547 | **40** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[topoteretes/cognee](https://github.com/topoteretes/cognee)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)

## 并行与隔离

*工作区隔离*

并行 Agent 会互相覆盖文件，除非各自有独立工作副本。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 106.7k 🚀 +466/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 21.8k 🚀 +92/d | **81** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | MCP 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 84.4k 🚀 +48/d | **75** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 33.7k 🚀 +22/d | **72** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.6k 🚀 +17/d | **69** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 8.3k 🚀 +44/d | **68** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 9.4k 🚀 +27/d | **68** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **59** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 跨 Agent 支持、通知提醒、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 8.4k (+20/d) | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.2k 🚀 +7/d | **58** |
| 🔹 **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 多智能体编排、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.4k | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 580 | **57** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 580 | **56** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 315 | **55** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 787 | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 2.9k | **52** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 303 | **49** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[0xsline/OpenChatCut](https://github.com/0xsline/OpenChatCut)、[spinabot/brigade](https://github.com/spinabot/brigade)、[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)、[crshdn/mission-control](https://github.com/crshdn/mission-control)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)、[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)、[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)

## 安全

*安全与隔离*

Agent 会执行任意代码并持有凭据，必须控制影响范围。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 6.3k 🚀 +95/d | **77** |
| ✅ **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k 🚀 +82/d | **74** |
| ✅ **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | 可自托管、MCP 支持、自动故障转移。 ‡ | 🟡 需配置 | — | — | 7k 🚀 +73/d | **74** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、可自托管；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 6k 🚀 +48/d | **72** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 跨 Agent 支持、计费与计量、MCP 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 5.4k 🚀 +23/d | **66** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi 为运行服务会处理有限的账户与技术信息；存在的分析均已披露且可关闭。 | 🟢 较易 | — | — | 3.2k 🚀 +40/d | **66** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | MCP 支持、多智能体编排、工作区隔离；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.1k 🚀 +14/d | **65** |
| ✅ **[0xsline/OpenChatCut](https://github.com/0xsline/OpenChatCut)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 2.6k 🚀 +26/d | **63** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 只需向 Claude Code、Codex、OpenCode 或 DeepSeek Harness 给出一次目标，即可让它跨桌面 App 与终端持续工作数十个小时。 | 🟢 较易 | — | — | 1.8k | **59** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 记忆与上下文、跨 Agent 支持、Agent 运行时；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.8k | **55** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 784 | **55** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 通知提醒、工作区隔离、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | ✅ | 345 | **52** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 330 | **52** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、通知提醒、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 309 | **52** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | MCP 支持、用量分析、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 523 | **50** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew 将任务执行、人工审批、持久记忆和定时任务整合到一个桌面应用。 你可以交办任务、添加文件与文件夹材料，查看实时回复、执行步骤、工具调用和结果。 | 🟡 需配置 | — | ✅ | 253 | **47** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[zai-org/ZCode](https://github.com/zai-org/ZCode)、[slopus/happy](https://github.com/slopus/happy)、[yc-software/qm](https://github.com/yc-software/qm)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)

## 共享

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 20.4k 🚀 +768/d | **89** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 130.7k 🚀 +174/d | **89** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 31.3k 🚀 +55/d | **71** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 计费与计量、图形界面与桌面端、跨 Agent 支持；兼容 Codex、OpenCode、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 19.3k 🚀 +39/d | **70** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.8k 🚀 +46/d | **69** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 9.9k 🚀 +41/d | **67** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.8k | **57** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 跨 Agent 支持、计费与计量、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 475 🚀 +33/d | **57** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.5k 🚀 +12/d | **55** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.7k 🚀 +11/d | **55** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 500 🚀 +17/d | **55** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 255 | **52** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、计费与计量；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 300 | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 905 | **49** |
| 🔹 **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | 支持导入当前登录账号、手动粘贴 Token、OAuth 文件快速导入 配额看板与自动刷新（5H / 7D）、低额度提醒与切换提示 | 🟡 需配置 | — | — | 250 | **45** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)、[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)、[cita-777/metapi](https://github.com/cita-777/metapi)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)、[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)

## 团队

*团队协作*

多人需要共用一套 Agent 环境，还要有角色与边界。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 60.5k 🚀 +484/d | **90** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 10.9k 🚀 +171/d | **87** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 13.1k 🚀 +468/d | **84** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 图形界面与桌面端、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 11k 🚀 +25/d | **68** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.5k 🚀 +15/d | **58** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.7k 🚀 +5/d | **56** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code（DAC） 将桌面编程工作区和终端智能体连接到同一个执行内核。 面对跨文件、多轮对话、多种工具和多人讨论的工作，你可以保留项目上下文、维护可编辑的计划、委派独立子任务、查看执行过程，并让最终回答回到发起工作的对话中。 | 🟢 较易 | — | — | 433 | **52** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 计费与计量、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、远程控制、工作区隔离；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 320 | **48** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[loopx-project/loopx](https://github.com/loopx-project/loopx)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 移动端与远程控制

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 104.2k 🚀 +1377/d | **92** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | 跨 App 自动化：根据自然语言指令，在 Android 上执行测试流程和日常任务。 AndroidWorld 结果：在 Google Research AndroidWorld 基准评测（100+ 多步任务）中取得 99%+ 任务完成率。 | 🟡 需配置 | — | — | 14.2k 🚀 +294/d | **82** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | ✅ | 24.3k 🚀 +16/d | **64** |
| 🔹 **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | 在你自己的本地 Agent 上运行 Claude Design —— Cursor、Claude Code、Claude Desktop，或任何能读写文件的编码 Agent。 | 🟢 开箱即用 | ✅ | — | 4.5k 🚀 +14/d | **60** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | 记忆与上下文。 ‡ | 🟡 需配置 | — | — | 3.6k 🚀 +15/d | **57** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 285 | **55** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、额度与用量管理；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 3k 🚀 +23/d | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **51** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟡 需配置 | — | — | 1.1k 🚀 +6/d | **51** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 549 | **51** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 技能与插件、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k | **50** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | Agent 运行时、多智能体编排、可自托管。 ‡ | 🟢 较易 | — | — | 467 | **50** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)、[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)

## 模型路由

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 76.9k 🚀 +264/d | **89** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 一套用代码做片的风格工具箱： 59 种现成风格，也能做出你自己的。 拿来做什么：做什么片、发在哪个平台（竖屏就用 1080×1920 或 1080×1440），有没有品牌色、logo、字体或固定角色； | 🟡 需配置 | — | ✅ | 6.3k 🚀 +564/d | **82** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、可自托管、远程控制。 ‡ | 🟢 较易 | ✅ | ✅ | 8.2k 🚀 +45/d | **70** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 10.6k 🚀 +55/d | **69** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.4k 🚀 +21/d | **64** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. † | 🟡 需配置 | — | — | 11.2k 🚀 +11/d | **59** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟢 较易 | — | — | 1.9k 🚀 +10/d | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. † | 🟢 开箱即用 | ✅ | — | 344 | **53** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 902 | **52** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 5.6k | **51** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 711 | **50** |
| 🔹 **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cline / Roo。 ‡ | 🟢 较易 | — | — | 624 | **49** |
| 🔹 **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | 跨 Agent 支持、技能与插件；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 467 | **45** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[yetone/magpie](https://github.com/yetone/magpie)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)、[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 148.2k 🚀 +400/d | **93** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 44.7k 🚀 +76/d | **76** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 10.7k 🚀 +56/d | **69** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、通知提醒、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 2.8k 🚀 +10/d | **60** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、MCP 支持、可自托管。 ‡ | 🔴 较重 | — | — | 11.6k 🚀 +34/d | **59** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 通知提醒、API 网关与中转、跨 Agent 支持；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 322 🚀 +12/d | **54** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 812 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 406 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **49** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 433 | **43** |

**也能做这件事：** [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[decolua/9router](https://github.com/decolua/9router)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)、[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)、[Licoy/Quosparr](https://github.com/Licoy/Quosparr)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | Agent 运行时；兼容 OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 220.9k 🚀 +757/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | Sketch, constrain, and build solids with a parametric feature timeline. † | 🟢 开箱即用 | ✅ | ✅ | 9.8k 🚀 +702/d | **87** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill 把你的 AI Agent 连接到 Chrome 或 Microsoft Edge，直接使用你已有的登录状态。 | 🟢 较易 | — | — | 9.5k 🚀 +56/d | **70** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 1.8k 🚀 +17/d | **63** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.1k 🚀 +15/d | **62** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 470 | **56** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | — | 516 🚀 +8/d | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 764 | **54** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 457 🚀 +10/d | **53** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | 对接其他产品是一个部署在流程后端地址之后的独立服务，不进入本仓库： 新增语音厂商加的是一个 profile，而不是一个新客户端： | 🟡 需配置 | — | — | 363 🚀 +11/d | **51** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | 技能与插件。 ‡ | 🟡 需配置 | — | — | 642 | **38** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[yetone/magpie](https://github.com/yetone/magpie)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[xerj-org/xerj](https://github.com/xerj-org/xerj)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[google/artemis](https://github.com/google/artemis)、[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)

## 语音

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 163.6k 🚀 +436/d | **98** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、技能与插件、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 137.4k 🚀 +108/d | **88** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 6.3k 🚀 +156/d | **85** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | 通知提醒、MCP 支持、跨 Agent 支持；兼容 Codex、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 5.5k 🚀 +73/d | **76** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | 跨 Agent 支持、通知提醒、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 9k 🚀 +23/d | **67** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | MiMoCode 是一个终端原生的 AI 编程助手。它能读写代码、执行命令、管理 Git，通过持久化记忆系统，在多次会话间保持对你项目的深度理解，并自我进化。 | 🟢 较易 | — | — | 13.7k 🚀 +5/d | **63** |
| 🔹 **[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)** | 面向工作、设计与代码的开源桌面 AI Agent 工作台。 工具商店统一管理本地 MCP、远程 MCP、CLI 和 API 连接器 | 🔴 较重 | — | — | 2.6k | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | 工作区隔离、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 421 | **55** |

**也能做这件事：** [getpaseo/paseo](https://github.com/getpaseo/paseo)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[slopus/happy](https://github.com/slopus/happy)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 4k 🚀 +38/d | **71** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.3k 🚀 +11/d | **56** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、OpenCode。 ‡ | 🟢 较易 | — | — | 986 | **55** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 857 | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 756 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 436 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、多智能体编排；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 511 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 594 | **45** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[loopx-project/loopx](https://github.com/loopx-project/loopx)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch)** | 以本地为核心的研究智能体执行框架和工作空间。 | 🟢 开箱即用 | ✅ | — | 7.5k 🚀 +33/d | **66** |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | 在 Codex、Claude Code、direct-model 等已注册 Agent 会话之间延续工作， 看成果和依据，而不只看活动。 检查交付物、支持与反驳证据、成本，以及下一步决策。 | 🟢 较易 | — | — | 6.4k 🚀 +8/d | **64** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排、可自托管。 ‡ | 🟢 较易 | ✅ | — | 5.9k | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、记忆与上下文、工作区隔离；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |

**也能做这件事：** [decolua/9router](https://github.com/decolua/9router)、[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[Licoy/Quosparr](https://github.com/Licoy/Quosparr)、[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)、[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)

## 共享

*配额共享与分发*

订阅容量超过个人所需，想安全地分给他人共用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 103.7k 🚀 +261/d | **95** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、模型与供应商路由；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 557 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api 是基于 Sub2API 二次开发的自托管 AI API 网关与订阅管理平台，提供账号池、API Key 管理、多供应商请求转发、用量计费、订阅充值、风控审查和后台运营能力。 | 🔴 较重 | — | — | 242 | **39** |

**也能做这件事：** [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[future-agi/future-agi](https://github.com/future-agi/future-agi)、[cordum-io/cordum](https://github.com/cordum-io/cordum)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.14 倍（20,441 vs 148,171） |

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
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/agi-is-going-to-arrive/memory-palace)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 94.44x the stars (29,844 vs 316) | 🤖 自动（high） |
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 59.01x the stars (19,295 vs 327) | 🤖 自动（high） |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 67.98x the stars (29,844 vs 439) | 🤖 自动（high） |
| **[Dodaios/Dodaios](https://github.com/dodaios/dodaios)** | **[HarnessMD/munder-difflin](https://github.com/harnessmd/munder-difflin)** | 36.20x the stars (9,014 vs 249) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.03x the stars (19,295 vs 2,404) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 221.99x the stars (84,357 vs 380) | 🤖 自动（high） |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | 3.34x the stars (1,728 vs 517) | 🤖 自动（high） |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/memtensor/memos-cloud-openclaw-plugin)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 80.88x the stars (29,844 vs 369) | 🤖 自动（high） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.10x the stars (10,898 vs 2,137) | 🤖 自动（high） |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 892.98x the stars (287,539 vs 322) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.40x the stars (33,742 vs 927) | 🤖 自动（high） |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.13x the stars (21,840 vs 5,289) | 🤖 自动（high） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 3.12x the stars (887 vs 284) | 🤖 自动（high） |
| **[YoanWai/agent-manager](https://github.com/yoanwai/agent-manager)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 54.33x the stars (33,742 vs 621) | 🤖 自动（high） |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 97.80x the stars (33,742 vs 345) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 21.63x the stars (106,704 vs 4,933) | 🤖 自动（high） |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 224.29x the stars (287,539 vs 1,282) | 🤖 自动（high） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 11.38x the stars (4,870 vs 428) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.86x the stars (10,898 vs 365) | 🤖 自动（high） |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 1198.08x the stars (287,539 vs 240) | 🤖 自动（high） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[spinabot/brigade](https://github.com/spinabot/brigade)** | 23.42x the stars (11,357 vs 485) | 🤖 自动（high） |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 122.25x the stars (33,742 vs 276) | 🤖 自动（high） |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 27.91x the stars (10,688 vs 383) | 🤖 自动（high） |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 45.56x the stars (29,844 vs 655) | 🤖 自动（high） |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 34.77x the stars (19,295 vs 555) | 🤖 自动（high） |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[aipoch/open-science](https://github.com/aipoch/open-science)** | 14.39x the stars (5,352 vs 372) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 35.70x the stars (29,844 vs 836) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 47.29x the stars (287,539 vs 6,080) | 🤖 自动（high） |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 402.72x the stars (287,539 vs 714) | 🤖 自动（high） |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 62.70x the stars (29,844 vs 476) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.91x the stars (10,898 vs 2,785) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 8.85x the stars (4,870 vs 550) | 🤖 自动（medium） |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.29x the stars (10,898 vs 1,315) | 🤖 自动（medium） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 48.53x the stars (27,614 vs 569) | 🤖 自动（medium） |
| **[yetone/cumora](https://github.com/yetone/cumora)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 2.75x the stars (11,020 vs 4,014) | 🤖 自动（high） |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 10.44x the stars (7,580 vs 726) | 🤖 自动（medium） |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | **[DeusData/codebase-memory-mcp](https://github.com/deusdata/codebase-memory-mcp)** | 8.74x the stars (47,373 vs 5,419) | 🤖 自动（medium） |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 41.65x the stars (287,539 vs 6,904) | 🤖 自动（medium） |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 41.75x the stars (10,898 vs 261) | 🤖 自动（medium） |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 4.12x the stars (1,154 vs 280) | 🤖 自动（medium） |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 2.92x the stars (10,898 vs 3,737) | 🤖 自动（medium） |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 24.43x the stars (33,742 vs 1,381) | 🤖 自动（high） |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 604.07x the stars (287,539 vs 476) | 🤖 自动（medium） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.45x the stars (887 vs 362) | 🤖 自动（high） |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 104.35x the stars (29,844 vs 286) | 🤖 自动（medium） |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.28x the stars (13,714 vs 400) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 3.63x the stars (1,112 vs 306) | 🤖 自动（high） |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 6.13x the stars (29,844 vs 4,870) | 🤖 自动（medium） |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent)** | 5.67x the stars (1,354 vs 239) | 🤖 自动（high） |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 1.38x the stars (148,171 vs 107,574) | 🤖 自动（medium） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.56x the stars (784 vs 503) | 🤖 自动（medium） |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 1.47x the stars (1,112 vs 755) | 🤖 自动（medium） |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.76x the stars (1,112 vs 403) | 🤖 自动（medium） |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.16x the stars (1,065 vs 493) | 🤖 自动（medium） |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.14x the stars (1,112 vs 519) | 🤖 自动（high） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 1.27x the stars (784 vs 615) | 🤖 自动（medium） |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.17x the stars (315 vs 270) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | billing | 107.6k | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (6/6)。 |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | self-hosting | 6.9k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | self-hosting | 6.1k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | security-self-hosting | 5.4k | 🔻 已被取代 | 已被 DeusData/codebase-memory-mcp 取代：covers 100% of capabilities (7/7)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | parallelism-isolation | 5.3k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (6/6)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | parallelism-isolation | 4.9k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (4/4)。 |
| **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | security-self-hosting | 4.9k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (12/12)。 |
| **[yetone/cumora](https://github.com/yetone/cumora)** | teams | 4k | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (9/9)。 |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | teams | 3.7k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.8k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | sharing | 2.4k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (8/8)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.1k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | parallelism-isolation | 1.4k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (9/9)。 |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | self-hosting | 1.3k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | parallelism-isolation | 927 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | security-self-hosting | 836 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 755 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (5/5)。 |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | security-self-hosting | 726 | 🔻 已被取代 | 已被 Gentleman-Programming/engram 取代：covers 100% of capabilities (5/5)。 |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | self-hosting | 714 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | security-self-hosting | 655 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (6/6)。 |
| **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | parallelism-isolation | 621 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | security | 615 | 🔻 已被取代 | 已被 kitfunso/hippo-memory 取代：covers 100% of capabilities (6/6)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | parallelism-isolation | 569 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (4/4)。 |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | sharing | 555 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (5/5)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | security-self-hosting | 550 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | desktop-ui | 519 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | security-self-hosting | 517 | 🔻 已被取代 | 已被 aoci-spec/aoci-code 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | security | 503 | 🔻 已被取代 | 已被 kitfunso/hippo-memory 取代：covers 100% of capabilities (4/4)。 |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 493 | 🔻 已被取代 | 已被 data-goblin/power-bi-agentic-development 取代：covers 100% of capabilities (6/6)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | self-hosting | 485 | 🔻 已被取代 | 已被 spinabot/brigade 取代：covers 100% of capabilities (4/4)。 |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | self-hosting | 476 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | security-self-hosting | 476 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | security-self-hosting | 439 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | security-self-hosting | 428 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 403 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (5/5)。 |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice | 400 | 🔻 已被取代 | 已被 XiaomiMiMo/MiMo-Code 取代：covers 100% of capabilities (8/8)。 |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | self-hosting | 383 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | parallelism-isolation | 380 | 🔻 已被取代 | 已被 bytedance/deer-flow 取代：covers 100% of capabilities (5/5)。 |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | security | 372 | 🔻 已被取代 | 已被 aipoch/open-science 取代：covers 100% of capabilities (5/5)。 |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | security-self-hosting | 369 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 365 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 362 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | parallelism-isolation | 345 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | self-hosting | 322 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | security-self-hosting | 316 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (9/9)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 306 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | security-self-hosting | 286 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (6/6)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 284 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | parallelism-isolation | 280 | 🔻 已被取代 | 已被 asheshgoplani/agent-deck 取代：covers 100% of capabilities (6/6)。 |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | parallelism-isolation | 276 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | parallelism-isolation | 270 | 🔻 已被取代 | 已被 h0x91b/dev-3.0 取代：covers 100% of capabilities (7/7)。 |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 261 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[Dodaios/Dodaios](https://github.com/Dodaios/Dodaios)** | voice | 249 | 🔻 已被取代 | 已被 HarnessMD/munder-difflin 取代：covers 100% of capabilities (9/9)。 |
| **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | self-hosting | 240 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (8/8)。 |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | parallelism-isolation | 239 | 🔻 已被取代 | 已被 first-fluke/oh-my-agent 取代：covers 100% of capabilities (6/6)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-24 08:56 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
