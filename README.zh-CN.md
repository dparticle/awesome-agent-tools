<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**222 个工具**，分 **14 个分类** · **51 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-14 09:34 UTC**

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
| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | 47 |
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 161 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 6 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 技能

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 150.7k 🚀 +185/d | **90** |
| 🏆 **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 跨 Agent 支持、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 47.1k 🚀 +456/d | **89** |
| 🏆 **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 95.8k (+406/d) | **88** |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 163.1k 🚀 +793/d | **86** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 11.8k 🚀 +175/d | **83** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 8.9k 🚀 +1774/d | **82** |
| ✅ **[tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness)** | MCP 支持、通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 11.1k 🚀 +72/d | **71** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 7.8k 🚀 +25/d | **69** |
| ✅ **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 3.6k 🚀 +64/d | **68** |
| ✅ **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 跨 Agent 支持、通知提醒、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27k 🚀 +28/d | **68** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 3.4k 🚀 +65/d | **67** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 面向各类 Agent 的 AI 短剧制作 skill 集合：从一本小说到直接交给生成管线的制作素材——拆角色、排大纲、出场景与道具设定、写剧本、切分镜。 每个 skill 都是自包含目录，任何能够读取 SKILL.md 并执行随附脚本的 Agent 都可以使用；Claude Code 和 Codex 只是其中两个运行示例，并非使用前提。 | 🟢 较易 | — | — | 4.5k 🚀 +50/d | **65** |
| ✅ **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | English README · 5 分钟快速开始 · 我想重构项目 每一项：worktree → implementer 改 → 独立 verifier 跑测试 → 你 审 PR。 | 🟢 开箱即用 | ✅ | — | 11.5k 🚀 +17/d | **63** |
| ✅ **[ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | ✅ | — | 3.6k 🚀 +54/d | **62** |
| 🔹 **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.1k 🚀 +21/d | **59** |
| 🔹 **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. † | 🟢 开箱即用 | ✅ | — | 6k 🚀 +22/d | **59** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | 跨 Agent 支持、团队协作；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.7k | **59** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 850 | **58** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | MCP 支持、图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 3.6k 🚀 +5/d | **57** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1k | **57** |
| 🔹 **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Copilot。 ‡ | 🟢 较易 | ✅ | — | 486 | **57** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 383 🚀 +15/d | **57** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.8k | **55** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **54** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | 通知提醒；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 341 | **53** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | 想法或现有代码 → 经过验证的 PRD → 功能 → 规则 → 有序的 RFC → 经过评审和测试的代码 | 🟢 较易 | — | — | 300 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Analyze + Generate：先提取视觉系统，再生成不复制原图构图的新作品。 Generate：内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。 | 🟡 需配置 | — | — | 7.3k 🚀 +8/d | **51** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 895 | **51** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | A collection of Claude Code skills for reviewing and understanding academic research. † | 🟢 开箱即用 | — | ✅ | 499 | **51** |

*还有 8 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [anomalyco/opencode](https://github.com/anomalyco/opencode)、[garrytan/gstack](https://github.com/garrytan/gstack)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)

## 自托管与安全

*可自托管*

不希望代码或密钥经过他人的服务器。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 278.8k 🚀 +638/d | **89** |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 18.2k 🚀 +744/d | **88** |
| ✅ **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | 模型与供应商路由、技能与插件、自动故障转移；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 5.3k 🚀 +75/d | **77** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 使用 ChatGPT 网页版的独立额度，不消耗 Work 或 Codex 额度。 | 🟢 较易 | — | — | 14.2k 🚀 +83/d | **76** |
| ✅ **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k 🚀 +91/d | **75** |
| ✅ **[appwrite/appwrite](https://github.com/appwrite/appwrite)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 57.7k 🚀 +11/d | **68** |
| ✅ **[duty1g/x64dbg-mcp-server](https://github.com/duty1g/x64dbg-mcp-server)** | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. † | 🟢 开箱即用 | ✅ | — | 2.5k 🚀 +48/d | **67** |
| ✅ **[KunAgent/Kun](https://github.com/KunAgent/Kun)** | 图形界面与桌面端、API 网关与中转、通知提醒。 ‡ | 🟢 较易 | — | ✅ | 6.3k (+44/d) | **66** |
| 🔹 **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k | **61** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.1k 🚀 +17/d | **59** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | 通知提醒、并行执行、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.7k 🚀 +8/d | **57** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 只需向 Claude Code、Codex、OpenCode 或 DeepSeek Harness 给出一次目标，即可让它跨桌面 App 与终端持续工作数十个小时。 | 🟢 较易 | — | — | 1.7k 🚀 +6/d | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、多智能体编排；兼容 Cursor、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 460 | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 较易 | — | — | 383 | **54** |
| 🔹 **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | Agent 运行时。 ‡ | 🟢 较易 | ✅ | — | 682 (+5/d) | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | 跨 Agent 支持、Agent 运行时；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 337 | **52** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 446 | **51** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 318 | **49** |
| 🔹 **[schmitech/orbit](https://github.com/schmitech/orbit)** | API 网关与中转、图形界面与桌面端、模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 354 | **48** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | 多智能体编排、图形界面与桌面端。 ‡ | 🟢 较易 | — | ✅ | 1.2k | **47** |
| 🔹 **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 285 | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | API 网关与中转、图形界面与桌面端、多智能体编排；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 2.7k | **46** |
| 🔹 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时、多智能体编排。 ‡ | 🟡 需配置 | — | — | 413 | **45** |
| 👀 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 542 | **40** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[topoteretes/cognee](https://github.com/topoteretes/cognee)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[aipoch/open-science](https://github.com/aipoch/open-science)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

## 语音与远程控制

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 92k 🚀 +743/d | **92** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、技能与插件、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 136.4k 🚀 +133/d | **90** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 101.8k 🚀 +554/d | **89** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 20.8k 🚀 +123/d | **86** |
| 🏆 **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.2k 🚀 +161/d | **84** |
| ✅ **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | MCP 支持、通知提醒、跨 Agent 支持；兼容 Codex、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 4.8k 🚀 +77/d | **76** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | MCP 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 83.8k 🚀 +54/d | **76** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 33.5k 🚀 +23/d | **72** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 跨 Agent 支持、图形界面与桌面端、安全与隔离；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 4.8k 🚀 +47/d | **71** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、可自托管、Agent 运行时。 ‡ | 🟢 较易 | ✅ | ✅ | 7.8k 🚀 +44/d | **69** |
| ✅ **[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)** | 跨 Agent 支持、图形界面与桌面端、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 8.7k 🚀 +27/d | **67** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 图形界面与桌面端、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 10.8k 🚀 +20/d | **66** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、MCP 支持、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15k 🚀 +15/d | **65** |
| ✅ **[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)** | MiMoCode 是一个终端原生的 AI 编程助手。它能读写代码、执行命令、管理 Git，通过持久化记忆系统，在多次会话间保持对你项目的深度理解，并自我进化。 | 🟢 较易 | — | — | 13.7k 🚀 +7/d | **64** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | MCP 支持、记忆与上下文、多智能体编排；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.3k 🚀 +6/d | **61** |
| 🔹 **[Pinvou/pinvou-agent](https://github.com/Pinvou/pinvou-agent)** | 面向工作、设计与代码的开源桌面 AI Agent 工作台。 工具商店统一管理本地 MCP、远程 MCP、CLI 和 API 连接器 | 🔴 较重 | — | — | 2.5k 🚀 +30/d | **60** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 工作区隔离、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k 🚀 +7/d | **57** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | MCP 支持、跨 Agent 支持、安全与隔离；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 776 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 工作区隔离、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 311 | **55** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、通知提醒、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 305 | **54** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 通知提醒、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **51** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、团队协作、工作区隔离；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 320 | **47** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[slopus/happy](https://github.com/slopus/happy)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 团队

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 160k 🚀 +311/d | **98** |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件、并行执行；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 54.9k (+305/d) | **90** |
| 🏆 **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 9.3k 🚀 +221/d | **87** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 9.6k 🚀 +114/d | **84** |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 44k 🚀 +83/d | **78** |
| 🏆 **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 10k 🚀 +98/d | **78** |
| ✅ **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | MCP 支持、技能与插件、模型与供应商路由；兼容 Gemini CLI。 ‡ | 🟢 较易 | — | — | 107.3k 🚀 +14/d | **70** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 29.4k 🚀 +30/d | **70** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 9.2k 🚀 +33/d | **65** |
| ✅ **[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)** | 跨 Agent 支持、Agent 运行时、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 4.4k 🚀 +8/d | **62** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、通知提醒、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 2.7k 🚀 +13/d | **60** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、手机端访问；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4k 🚀 +6/d | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | 工作区隔离、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 408 | **54** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、可自托管。 ‡ | 🔴 较重 | — | — | 11.3k 🚀 +24/d | **52** |
| 🔹 **[cwinvestments/memstack](https://github.com/cwinvestments/memstack)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 426 | **52** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 404 | **51** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 技能与插件、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k | **50** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 792 | **50** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 301 | **49** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、多账号切换；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **48** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.1k | **48** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 424 | **46** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[decolua/9router](https://github.com/decolua/9router)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[spinabot/brigade](https://github.com/spinabot/brigade)、[Justin0504/Aegis](https://github.com/Justin0504/Aegis)、[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)、[cordum-io/cordum](https://github.com/cordum-io/cordum)、[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)

## 运行时与桌面端

*并行执行*

任务串行执行、只能干等；并行能压缩总耗时。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.4k 🚀 +18/d | **69** |
| ✅ **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 9.2k 🚀 +29/d | **69** |
| ✅ **[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)** | 📣 2026-09-30 — Raven 技术报告获评 Hugging Face #1 Paper of the day。 | 🟢 开箱即用 | — | — | 5.4k 🚀 +21/d | **67** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | 中的普通请求，转化为合适的能力、明确的下一步，以及对“已经发生”和“尚未发生”的诚实状态。 | 🟢 开箱即用 | ✅ | — | 3.4k 🚀 +26/d | **67** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | 跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 7.9k 🚀 +34/d | **66** |
| 🔹 **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | ✅ | 2.1k | **61** |
| 🔹 **[MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)** | AI-native 的 MCP 配置 通过 /mcp-config 对话式添加、编辑、认证 MCP 服务器，无需手写 JSON。 编辑器 / IDE 集成（ACP） 用 kimi acp 让 Zed、JetBrains 等任意 Agent Client Protocol 客户端直接驱动会话。 | 🟡 需配置 | — | — | 7.9k 🚀 +11/d | **60** |
| 🔹 **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **59** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 539 | **57** |
| 🔹 **[diffusionstudio/lottie](https://github.com/diffusionstudio/lottie)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 5.6k 🚀 +4/d | **56** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | 在一个桌面对话里指挥一支 AI 智能体团队 —— 而不是单个聊天机器人。 不止于代码 —— 视频、幻灯片等 —— 指挥官可驱动 HyperFrames 等开源工具，并把任务交接给 CLI 智能体——编程智能体 Claude Code、Codex、OpenCode，以及个人智能体 OpenClaw、Hermes-Agent——及其他本地智能体，于是一个对话就能产出代码、研究、视频与幻灯片。 | 🟡 需配置 | — | — | 2.2k | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 536 | **56** |
| 🔹 **[YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)** | 跨 Agent 支持、MCP 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 594 | **55** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 787 (+6/d) | **53** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Cursor、Copilot、Cline / Roo。 ‡ | 🟢 开箱即用 | ✅ | — | 671 | **48** |
| 🔹 **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | 为 AI 编程 agent 设计的 Git worktree 工作流工具。提供隔离的并行开发环境。 Run 引擎："即用即删"工作流 — 创建 worktree、运行 agent、合并、清理。 | 🟡 需配置 | ✅ | — | 280 | **47** |
| 🔹 **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | 跨 Agent 支持、图形界面与桌面端、远程控制；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | ✅ | 268 | **47** |

**也能做这件事：** [garrytan/gstack](https://github.com/garrytan/gstack)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)、[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)

## 用量分析

*记忆与上下文*

每次新会话都从零开始，记不住项目约定。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、模型与供应商路由、可自托管；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 32.2k 🚀 +82/d | **80** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 7.9k 🚀 +84/d | **72** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.2k 🚀 +16/d | **62** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 跨 Agent 支持、技能与插件、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.8k 🚀 +10/d | **62** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 1.5k 🚀 +30/d | **60** |
| 🔹 **[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 12.6k 🚀 +22/d | **58** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | 跨 Agent 支持、技能与插件、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 1.3k | **56** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 420 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | 技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 417 | **54** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 479 🚀 +7/d | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 16.6k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 跨 Agent 支持、通知提醒、远程控制；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 840 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | 跨 Agent 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 224 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、自动故障转移、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 677 | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | 自动故障转移、模型与供应商路由、技能与插件。 ‡ | 🔴 较重 | — | — | 487 | **49** |
| 🔹 **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | 跨 Agent 支持、Agent 运行时、可自托管；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 438 | **46** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 246 | **46** |
| 👀 **[osovv/grace-marketplace](https://github.com/osovv/grace-marketplace)** | 多智能体编排、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 253 | **44** |
| 👀 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | 图形界面与桌面端、通知提醒、可自托管。 ‡ | 🔴 较重 | — | — | 476 | **41** |

**也能做这件事：** [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)、[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)、[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[spinabot/brigade](https://github.com/spinabot/brigade)、[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)、[felinics/Memoh](https://github.com/felinics/Memoh)、[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)、[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)、[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)、[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)

## 共享

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 129.1k 🚀 +160/d | **89** |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 12.3k 🚀 +1012/d | **87** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 计费与计量、图形界面与桌面端、跨 Agent 支持；兼容 Codex、OpenCode、Cursor、Copilot。 ‡ | 🟢 较易 | — | ✅ | 19k 🚀 +41/d | **72** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 30.8k 🚀 +55/d | **70** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.4k 🚀 +45/d | **68** |
| ✅ **[chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 9.5k 🚀 +43/d | **68** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.4k 🚀 +41/d | **61** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.8k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | 跨 Agent 支持、API 网关与中转；兼容 Codex、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 542 | **54** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 241 | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 413 | **51** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 安全与隔离、计费与计量、工作区隔离；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 314 🚀 +7/d | **51** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.6k 🚀 +11/d | **50** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 894 | **49** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | ikik-api 是基于 Sub2API 二次开发的自托管 AI API 网关与订阅管理平台，提供账号池、API Key 管理、多供应商请求转发、用量计费、订阅充值、风控审查和后台运营能力。 | 🔴 较重 | — | — | 241 | **42** |

**也能做这件事：** [Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 模型路由

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 101.1k 🚀 +183/d | **95** |
| ✅ **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 10.1k 🚀 +90/d | **75** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.2k 🚀 +22/d | **64** |
| 🔹 **[teamchong/pxpipe](https://github.com/teamchong/pxpipe)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 7.5k | **61** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | @openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. † | 🟡 需配置 | — | — | 11.1k 🚀 +11/d | **59** |
| 🔹 **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | deepseek harness, openclaw, hermes, claude code, codex, cursor, workbuddy, openCode, pi...都能用! | 🟡 需配置 | — | — | 2.1k | **56** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | — | 342 | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 701 | **52** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 708 | **50** |
| 🔹 **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | 多智能体编排、记忆与上下文、自动故障转移。 ‡ | 🟢 较易 | — | — | 367 | **47** |

**也能做这件事：** [yetone/magpie](https://github.com/yetone/magpie)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[decolua/9router](https://github.com/decolua/9router)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[yetone/cumora](https://github.com/yetone/cumora)、[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)

## 供应商

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、模型与供应商路由；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 144.1k 🚀 +459/d | **93** |
| ✅ **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.8k 🚀 +99/d | **74** |
| ✅ **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Node 22+ LTS（用于钩子脚本 — 通常与 Claude Code / Codex / Gemini CLI 一起已安装） /om-review-brief 通过汇总所有内容生成完整的评估简报：成就记录、决策、事件、能力证据和 1:1 反馈 | 🟡 需配置 | — | — | 5.3k 🚀 +66/d | **72** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.4k 🚀 +14/d | **67** |
| ✅ **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | FuXi 为运行服务会处理有限的账户与技术信息；存在的分析均已披露且可关闭。 | 🟢 较易 | — | — | 3.3k 🚀 +47/d | **66** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 7.6k 🚀 +16/d | **54** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 282 | **53** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | MCP 支持、跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 430 | **52** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、模型与供应商路由、API 网关与中转；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 557 | **49** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 516 | **43** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace 为 LLM Agent 提供持久化、可检索、可审计的外部记忆，让每次对话都能在之前的基础上继续，而不是从零开始。 | 🟡 需配置 | — | — | 313 | **43** |

**也能做这件事：** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)、[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)、[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | 多智能体编排；兼容 OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 213.4k 🚀 +212/d | **90** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 多智能体编排、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 29.4k 🚀 +528/d | **84** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | BrowserSkill 把你的 AI Agent 连接到 Chrome 或 Microsoft Edge，直接使用你已有的登录状态。 | 🟢 较易 | — | — | 8.8k 🚀 +68/d | **73** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15k 🚀 +13/d | **64** |
| 🔹 **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 1.6k 🚀 +8/d | **61** |
| 🔹 **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | 在本地管理你的编码 agent（Claude Code、Codex、Cursor、Devin、Grok、Hermes、Pi、Antigravity），也可以打开多设备同步。 | 🟢 开箱即用 | ✅ | ✅ | 3.2k 🚀 +10/d | **59** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 462 | **56** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | minimax：MiniMax Anthropic Messages 兼容端点。 opencode-claude-auth / Claude Code： 自动捕获使用带有你已认证 anthropic 提供商的 OpenCode。 | 🔴 较重 | — | — | 1.7k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1k | **55** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 744 | **50** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | MCP 支持、多智能体编排。 ‡ | 🟡 需配置 | — | — | 641 | **38** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[anthropics/claude-code](https://github.com/anthropics/claude-code)、[openai/codex](https://github.com/openai/codex)、[alibaba/open-code-review](https://github.com/alibaba/open-code-review)、[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[aipoch/open-science](https://github.com/aipoch/open-science)

## 移动端

*手机端访问*

人不在电脑旁，想用手机继续让 Agent 干活。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[google/artemis](https://github.com/google/artemis)** | 跨 App 自动化：根据自然语言指令，在 Android 上执行测试流程和日常任务。 AndroidWorld 结果：在 Google Research AndroidWorld 基准评测（100+ 多步任务）中取得 99%+ 任务完成率。 | 🟡 需配置 | — | — | 11.7k 🚀 +91/d | **75** |
| ✅ **[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)** | 在你自己的本地 Agent 上运行 Claude Design —— Cursor、Claude Code、Claude Desktop，或任何能读写文件的编码 Agent。 | 🟢 开箱即用 | ✅ | — | 4.4k 🚀 +21/d | **64** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | ✅ | 24.1k 🚀 +13/d | **63** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 2.8k 🚀 +68/d | **62** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | 记忆与上下文。 ‡ | 🟡 需配置 | — | — | 3.4k 🚀 +13/d | **55** |
| 🔹 **[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 7.5k 🚀 +16/d | **54** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 284 | **53** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟡 需配置 | — | — | 1k 🚀 +5/d | **51** |
| 🔹 **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | 远程控制、Agent 运行时、多智能体编排。 ‡ | 🟢 较易 | — | — | 443 | **50** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[stablyai/orca](https://github.com/stablyai/orca)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[loopx-project/loopx](https://github.com/loopx-project/loopx)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)、[yetone/cumora](https://github.com/yetone/cumora)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 3.6k 🚀 +55/d | **74** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.2k 🚀 +18/d | **58** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 812 🚀 +5/d | **56** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、OpenCode。 ‡ | 🟢 较易 | — | — | 985 | **55** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 726 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 435 | **54** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、多智能体编排；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 587 | **46** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[loopx-project/loopx](https://github.com/loopx-project/loopx)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[loopx-project/loopx](https://github.com/loopx-project/loopx)** | 在 Codex、Claude Code、direct-model 等已注册 Agent 会话之间延续工作， Shared Goal Authority 与跨 Host 协作：为显式共享 goal 提供 | 🟡 需配置 | — | — | 6.3k 🚀 +16/d | **65** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、记忆与上下文、模型与供应商路由；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.1k | **53** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 安全与隔离、图形界面与桌面端、MCP 支持；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 542 🚀 +6/d | **53** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 2.9k | **52** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排、可自托管。 ‡ | 🟢 较易 | ✅ | — | 5.9k (+5/d) | **51** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 223 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | 自动故障转移、多智能体编排；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 729 | **43** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)、[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)、[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)、[tigicion/dao-code](https://github.com/tigicion/dao-code)

## 会话

*会话持久化*

合上笔记本或断网就会中断长时间运行的会话。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🔹 **[feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟢 开箱即用 | ✅ | — | 2.8k 🚀 +15/d | **60** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟢 较易 | — | — | 1.8k 🚀 +11/d | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.1k | **55** |
| 🔹 **[jmagly/aiwg](https://github.com/jmagly/aiwg)** | MCP 支持、跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 224 | **53** |
| 🔹 **[YYHDBL/AgentCrew](https://github.com/YYHDBL/AgentCrew)** | AgentCrew 将任务执行、人工审批、持久记忆和定时任务整合到一个桌面应用。 你可以交办任务、添加文件与文件夹材料，查看实时回复、执行步骤、工具调用和结果。 | 🟡 需配置 | — | ✅ | 251 | **49** |
| 👀 **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | 跨 Agent 支持、Agent 运行时、记忆与上下文；兼容 Claude Code、Codex。 ‡ | 🔴 较重 | — | — | 516 | **38** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[anomalyco/opencode](https://github.com/anomalyco/opencode)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[zai-org/ZCode](https://github.com/zai-org/ZCode)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin)、[XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)、[slopus/happy](https://github.com/slopus/happy)、[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.09 倍（12,298 vs 144,070） |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 57.97x the stars (18,955 vs 327) | 🤖 自动（high） |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 19.71x the stars (10,800 vs 548) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 72.03x the stars (27,443 vs 381) | 🤖 自动（high） |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 876.85x the stars (278,839 vs 318) | 🤖 自动（high） |
| **[Pimzino/spec-workflow-mcp](https://github.com/pimzino/spec-workflow-mcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 64.80x the stars (278,839 vs 4,303) | 🤖 自动（high） |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 3.98x the stars (20,837 vs 5,238) | 🤖 自动（high） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 3.01x the stars (850 vs 282) | 🤖 自动（high） |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 217.78x the stars (101,051 vs 464) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 5.60x the stars (27,443 vs 4,903) | 🤖 自动（high） |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 233.50x the stars (101,804 vs 436) | 🤖 自动（high） |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 390.18x the stars (159,974 vs 410) | 🤖 自动（high） |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.31x the stars (9,260 vs 2,147) | 🤖 自动（high） |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | **[XiaomiMiMo/MiMo-Code](https://github.com/xiaomimimo/mimo-code)** | 34.92x the stars (13,653 vs 391) | 🤖 自动（high） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 11.16x the stars (4,756 vs 426) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 26.92x the stars (9,260 vs 344) | 🤖 自动（high） |
| **[hex/claude-council](https://github.com/hex/claude-council)** | **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | 3.85x the stars (3,365 vs 873) | 🤖 自动（high） |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 161.68x the stars (101,051 vs 625) | 🤖 自动（high） |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 75.52x the stars (18,955 vs 251) | 🤖 自动（high） |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 583.85x the stars (159,974 vs 274) | 🤖 自动（high） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 455.62x the stars (278,839 vs 612) | 🤖 自动（high） |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 16.42x the stars (144,070 vs 8,774) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 46.38x the stars (278,839 vs 6,012) | 🤖 自动（high） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[EverMind-AI/Raven](https://github.com/evermind-ai/raven)** | 9.57x the stars (5,429 vs 567) | 🤖 自动（high） |
| **[spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** | **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | 14.82x the stars (5,277 vs 356) | 🤖 自动（high） |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 77.95x the stars (278,839 vs 3,577) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 3.43x the stars (4,821 vs 1,404) | 🤖 自动（high） |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 6.61x the stars (101,804 vs 15,408) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 3.38x the stars (9,260 vs 2,743) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 8.68x the stars (4,756 vs 548) | 🤖 自动（medium） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 29.70x the stars (27,443 vs 924) | 🤖 自动（medium） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.85x the stars (850 vs 298) | 🤖 自动（high） |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 747.56x the stars (278,839 vs 373) | 🤖 自动（medium） |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.92x the stars (7,180 vs 724) | 🤖 自动（medium） |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 6.99x the stars (47,061 vs 6,736) | 🤖 自动（medium） |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 43.14x the stars (278,839 vs 6,464) | 🤖 自动（medium） |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 6.03x the stars (2,088 vs 346) | 🤖 自动（medium） |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 588.27x the stars (278,839 vs 474) | 🤖 自动（medium） |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/ryze-ai-adgent/open-seo-mcp-skills)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 52.57x the stars (278,839 vs 5,304) | 🤖 自动（medium） |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 7.56x the stars (4,756 vs 629) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 2.37x the stars (850 vs 358) | 🤖 自动（high） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 555.46x the stars (278,839 vs 502) | 🤖 自动（medium） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.30x the stars (1,073 vs 467) | 🤖 自动（high） |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 7.62x the stars (2,088 vs 274) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 6.11x the stars (4,756 vs 778) | 🤖 自动（high） |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 3.68x the stars (2,088 vs 567) | 🤖 自动（medium） |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 20.81x the stars (27,443 vs 1,319) | 🤖 自动（high） |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.26x the stars (20,837 vs 4,888) | 🤖 自动（medium） |
| **[Lling0000/Vibe_coding_guide](https://github.com/lling0000/vibe_coding_guide)** | **[maxritter/pilot-shell](https://github.com/maxritter/pilot-shell)** | 8.96x the stars (2,088 vs 233) | 🤖 自动（high） |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 9.45x the stars (29,404 vs 3,112) | 🤖 自动（high） |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 1.88x the stars (701 vs 373) | 🤖 自动（medium） |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 1.36x the stars (101,051 vs 74,449) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | model-routing | 74.4k | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (5/5)。 |
| **[yc-software/qm](https://github.com/yc-software/qm)** | voice-remote-control | 15.4k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (10/10)。 |
| **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | providers | 8.8k | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (7/7)。 |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | skills | 6.7k | 🔻 已被取代 | 已被 alibaba/open-code-review 取代：covers 100% of capabilities (4/4)。 |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | self-hosting-security | 6.5k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (7/7)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | self-hosting-security | 6k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | self-hosting-security | 5.3k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | voice-remote-control | 5.2k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (6/6)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | agent-runtime-desktop-ui | 4.9k | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (4/4)。 |
| **[tigerless-labs/cost-xray](https://github.com/tigerless-labs/cost-xray)** | voice-remote-control | 4.9k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (5/5)。 |
| **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | self-hosting-security | 4.3k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | self-hosting-security | 3.6k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase)** | teams | 3.1k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.7k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams | 2.1k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | voice-remote-control | 1.4k | 🔻 已被取代 | 已被 milind-soni/OpenMausBot 取代：covers 100% of capabilities (4/4)。 |
| **[michaelshimeles/skills](https://github.com/michaelshimeles/skills)** | agent-runtime-desktop-ui | 1.3k | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | agent-runtime-desktop-ui | 924 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (6/6)。 |
| **[hex/claude-council](https://github.com/hex/claude-council)** | agent-runtime-desktop-ui | 873 | 🔻 已被取代 | 已被 rlaope/oh-my-hermes 取代：covers 100% of capabilities (4/4)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | analytics | 778 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | analytics | 724 | 🔻 已被取代 | 已被 Gentleman-Programming/engram 取代：covers 100% of capabilities (5/5)。 |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | analytics | 629 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (6/6)。 |
| **[hkqr/my-free-code](https://github.com/hkqr/my-free-code)** | model-routing | 625 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | self-hosting-security | 612 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | agent-runtime-desktop-ui | 567 | 🔻 已被取代 | 已被 EverMind-AI/Raven 取代：covers 100% of capabilities (4/4)。 |
| **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | agent-runtime-desktop-ui | 567 | 🔻 已被取代 | 已被 maxritter/pilot-shell 取代：covers 100% of capabilities (7/7)。 |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | voice-remote-control | 548 | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (7/7)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | analytics | 548 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | self-hosting-security | 502 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | self-hosting-security | 474 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | sessions | 467 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | model-routing | 464 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | voice-remote-control | 436 | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (12/12)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | analytics | 426 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[devaccuracy/ledgerforge](https://github.com/devaccuracy/ledgerforge)** | teams | 410 | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (4/4)。 |
| **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | voice-remote-control | 391 | 🔻 已被取代 | 已被 XiaomiMiMo/MiMo-Code 取代：covers 100% of capabilities (7/7)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | agent-runtime-desktop-ui | 381 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | model-routing | 373 | 🔻 已被取代 | 已被 ruvnet/metaharness 取代：covers 100% of capabilities (4/4)。 |
| **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | self-hosting-security | 373 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills | 358 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)** | self-hosting-security | 356 | 🔻 已被取代 | 已被 superdesigndev/treg 取代：covers 100% of capabilities (4/4)。 |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | agent-runtime-desktop-ui | 346 | 🔻 已被取代 | 已被 maxritter/pilot-shell 取代：covers 100% of capabilities (6/6)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 344 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | sharing | 327 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | self-hosting-security | 318 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills | 298 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills | 282 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (4/4)。 |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | agent-runtime-desktop-ui | 274 | 🔻 已被取代 | 已被 maxritter/pilot-shell 取代：covers 100% of capabilities (7/7)。 |
| **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | teams | 274 | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (6/6)。 |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | sharing | 251 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (5/5)。 |
| **[Lling0000/Vibe_coding_guide](https://github.com/Lling0000/Vibe_coding_guide)** | agent-runtime-desktop-ui | 233 | 🔻 已被取代 | 已被 maxritter/pilot-shell 取代：covers 100% of capabilities (6/6)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-14 09:34 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
