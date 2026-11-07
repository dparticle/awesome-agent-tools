<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**226 个工具**，分 **13 个分类** · **50 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-11-07 11:07 UTC**

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
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 153 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 9 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 移动端

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 167k 🚀 +202/d | **98** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、手机端访问、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 118.1k 🚀 +998/d | **92** |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 140.6k 🚀 +385/d | **91** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 111.9k 🚀 +352/d | **89** |
| 🏆 **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 11.9k 🚀 +406/d | **87** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 23.4k 🚀 +113/d | **85** |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 17.6k 🚀 +300/d | **83** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | 从手机、电脑、浏览器继续使用你的 DeepSeek Harness 实例。无论使用哪台设备，都可以回到同一个 Harness 会话。 | 🟢 较易 | — | — | 2.1k 🚀 +169/d | **80** |
| 🏆 **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | MCP 支持、API 网关与中转、图形界面与桌面端；兼容 Claude Code。 ‡ | 🟢 较易 | ✅ | — | 33.2k (+68/d) | **78** |
| ✅ **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | 图形界面与桌面端、MCP 支持、Agent 运行时。 ‡ | 🟢 开箱即用 | — | ✅ | 7.9k (+65/d) | **75** |
| ✅ **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | MCP 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 85.1k 🚀 +45/d | **75** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | 多智能体编排、通知提醒、Agent 运行时；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2k 🚀 +89/d | **75** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 48.3k 🚀 +57/d | **74** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 34.1k 🚀 +18/d | **71** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 27.9k 🚀 +23/d | **70** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 1.9k 🚀 +54/d | **70** |
| ✅ **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 图形界面与桌面端、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 11.3k 🚀 +20/d | **68** |
| ✅ **[kunchenguid/firstmate](https://github.com/kunchenguid/firstmate)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 8.7k 🚀 +32/d | **66** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7k 🚀 +26/d | **66** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.8k 🚀 +33/d | **66** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、手机端访问；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | ✅ | ✅ | 24.5k 🚀 +16/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、手机端访问、安全与隔离；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.3k 🚀 +14/d | **64** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.2k 🚀 +21/d | **64** |
| ✅ **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、MCP 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **62** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 4.2k 🚀 +28/d | **61** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.3k 🚀 +14/d | **58** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 4.2k 🚀 +21/d | **58** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | MCP 支持、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.2k 🚀 +6/d | **58** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 603 | **56** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 594 | **56** |

*还有 15 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [crshdn/mission-control](https://github.com/crshdn/mission-control)、[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)

## 桌面端

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 186.1k 🚀 +712/d | **87** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 8.5k 🚀 +115/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 25.7k 🚀 +332/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 图形界面与桌面端、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 64.7k 🚀 +1559/d | **83** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | MCP 支持、跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 49.3k 🚀 +56/d | **79** |
| 🏆 **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 8.5k 🚀 +72/d | **79** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 6.2k 🚀 +86/d | **72** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. † | 🔴 较重 | — | — | 8.1k 🚀 +237/d | **71** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 6.2k 🚀 +62/d | **66** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft m… † | 🟢 较易 | — | — | 6.2k 🚀 +44/d | **64** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4.7k 🚀 +57/d | **64** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. † | 🟢 开箱即用 | ✅ | — | 6.5k 🚀 +23/d | **63** |
| ✅ **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 较易 | — | — | 3.7k 🚀 +22/d | **63** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 553 | **57** |
| 🔹 **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Copilot。 ‡ | 🟢 较易 | ✅ | — | 509 | **57** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 939 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.9k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | ✅ | — | 918 | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[lixiaolin94/skills](https://github.com/lixiaolin94/skills)** | 编译目标为 Android 12（API 31）及以上；实际可用的最低版本未测试 电脑上有 adb 和 Python 3.9+（只用标准库） | 🟢 开箱即用 | ✅ | — | 770 | **52** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 并行执行；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | ✅ | 529 | **52** |
| 🔹 **[neiii/bridle](https://github.com/neiii/bridle)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、OpenCode、Copilot、Goose。 ‡ | 🟢 较易 | — | — | 442 | **52** |
| 🔹 **[athola/claude-night-market](https://github.com/athola/claude-night-market)** | 通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 348 | **52** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | 跨 Agent 支持、MCP 支持、计费与计量；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 293 | **52** |
| 🔹 **[LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)** | Analyze + Generate：先提取视觉系统，再生成不复制原图构图的新作品。 Generate：内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。 | 🟡 需配置 | — | — | 7.5k 🚀 +7/d | **51** |
| 🔹 **[nurettincoban/ai-prd-workflow](https://github.com/nurettincoban/ai-prd-workflow)** | 想法或现有代码 → 经过验证的 PRD → 功能 → 规则 → 有序的 RFC → 经过评审和测试的代码 | 🟢 较易 | — | — | 309 | **51** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 跨 Agent 支持、计费与计量、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k | **50** |

*还有 5 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [garrytan/gstack](https://github.com/garrytan/gstack)、[anomalyco/opencode](https://github.com/anomalyco/opencode)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)、[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)、[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

## MCP与安全

*MCP 支持*

Agent 需要通过标准协议访问外部工具与数据。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 22.9k 🚀 +146/d | **89** |
| 🏆 **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Agent 运行时、通知提醒、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 4.1k 🚀 +124/d | **80** |
| 🏆 **[google/artemis](https://github.com/google/artemis)** | 跨 App 自动化：根据自然语言指令，在 Android 上执行测试流程和日常任务。 AndroidWorld 结果：在 Google Research AndroidWorld 基准评测（100+ 多步任务）中取得 99%+ 任务完成率。 | 🟡 需配置 | — | — | 16.9k 🚀 +136/d | **79** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 技能与插件、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 4.7k 🚀 +75/d | **78** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 消息通过已登录的 ChatGPT 网页会话发送，并受该账户适用的使用限制约束。 | 🟢 较易 | — | — | 15.6k 🚀 +31/d | **66** |
| ✅ **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | 技能与插件、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Cursor。 ‡ | 🟡 需配置 | — | — | 8.9k 🚀 +41/d | **62** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.5k | **62** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 只需向 Claude Code、Codex、OpenCode 或 DeepSeek Harness 给出一次目标，即可让它跨桌面 App 与终端持续工作数十个小时。 | 🟢 较易 | — | — | 1.9k 🚀 +8/d | **59** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.3k | **58** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **56** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | 跨 Agent 支持、多智能体编排、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 553 🚀 +5/d | **56** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、多智能体编排；兼容 Cursor、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 474 | **55** |
| 🔹 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Agent 运行时、图形界面与桌面端。 ‡ | 🟢 较易 | ✅ | — | 602 | **54** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | 跨 Agent 支持、Agent 运行时；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 391 🚀 +12/d | **54** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 较易 | — | — | 386 | **54** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | 技能与插件、跨 Agent 支持、手机端访问；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 跨 Agent 支持、多智能体编排、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 739 | **52** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | 技能与插件、图形界面与桌面端、模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 371 | **52** |
| 🔹 **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | 模型与供应商路由、可自托管、并行执行；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 1.3k | **51** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 533 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **51** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | 多智能体编排、图形界面与桌面端、可自托管。 ‡ | 🟢 较易 | — | ✅ | 1.2k | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 图形界面与桌面端、多智能体编排、并行执行；兼容 Cursor。 ‡ | 🔴 较重 | — | — | 2.8k | **46** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | 多智能体编排、跨 Agent 支持、可自托管；兼容 Claude Code、Cursor。 ‡ | 🔴 较重 | — | — | 326 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时、多智能体编排。 ‡ | 🟡 需配置 | — | — | 417 | **42** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[nexu-io/open-design](https://github.com/nexu-io/open-design)、[yetone/magpie](https://github.com/yetone/magpie)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

## 故障转移

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 6.4k 🚀 +170/d | **88** |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 面向 AI 智能体的本地优先搜索引擎与 MCP 服务。 一个 Rust 二进制程序即可为代码、文档、日志、JSONL/CSV 和 PDF 建立索引，提供 BM25 全文、向量与混合搜索、代码搜索和智能体记忆，接口兼容 Elasticsearch API。 | 🟢 较易 | — | — | 18.5k 🚀 +99/d | **84** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | 展开请求看细节：读取已保留的请求头、提交数据、响应正文、耗时与错误，筛选流量或直接查看某个 JSON 字段。 验证并保留证据：配置任务内的请求修改、拦截、模拟响应或同源请求重放，导出 JSON，供后续复查和分享。 | 🟢 较易 | — | — | 10.1k 🚀 +46/d | **69** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 9.3k 🚀 +63/d | **66** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.7k 🚀 +11/d | **63** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.8k 🚀 +19/d | **63** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Node 22+ LTS（用于钩子脚本 — 通常与 Claude Code / Codex / Gemini CLI 一起已安装） /om-review-brief 通过汇总所有内容生成完整的评估简报：成就记录、决策、事件、能力证据和 1:1 反馈 | 🟡 需配置 | — | — | 5.5k 🚀 +7/d | **59** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | — | 5.1k | **55** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 1.9k 🚀 +7/d | **55** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 图形界面与桌面端、技能与插件、跨 Agent 支持；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.8k | **55** |
| 🔹 **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 856 | **55** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | MCP 支持、技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 410 | **55** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 17.4k 🚀 +7/d | **53** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | MCP 支持、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **53** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 434 | **53** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 915 🚀 +5/d | **52** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 512 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | MCP 支持、跨 Agent 支持、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 449 | **52** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 7.9k 🚀 +15/d | **51** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 922 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | 跨 Agent 支持、多智能体编排、API 网关与中转；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 698 | **51** |
| 🔹 **[oleksiijko/pmb](https://github.com/oleksiijko/pmb)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 284 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 676 | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | MCP 支持、技能与插件、模型与供应商路由。 ‡ | 🔴 较重 | — | — | 516 | **49** |
| 🔹 **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | 确定性召回。 相关度 × 时间衰减 × 重要度，全部在本地计算。检索自己的记忆不需要模型调用、不需要网络、不需要 API key。 内置 prompt 注入。 在 OpenClaw 上，伴生插件会在每一轮对话前注入一份紧凑索引，让 agent 开口时就已经知道它知道什么。 | 🟢 较易 | — | ✅ | 549 | **47** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace 为 LLM Agent 提供持久化、可检索、可审计的外部记忆，让每次对话都能在之前的基础上继续，而不是从零开始。 | 🟡 需配置 | — | — | 315 | **44** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、用量分析；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 524 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[garrytan/gstack](https://github.com/garrytan/gstack)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[spinabot/brigade](https://github.com/spinabot/brigade)、[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)

## 团队

*可自托管*

不希望代码或密钥经过他人的服务器。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 298.8k 🚀 +734/d | **89** |
| 🏆 **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | MCP 支持、安全与隔离、自动故障转移。 ‡ | 🟢 较易 | — | — | 10.4k 🚀 +106/d | **83** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 7.4k 🚀 +93/d | **81** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 15.3k 🚀 +82/d | **78** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 11.8k 🚀 +55/d | **75** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 11.9k 🚀 +68/d | **75** |
| ✅ **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | 图形界面与桌面端、工作区隔离、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 6.2k 🚀 +72/d | **73** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 30.2k 🚀 +20/d | **69** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 记忆与上下文、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 33.1k 🚀 +24/d | **68** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、Agent 运行时、模型与供应商路由。 ‡ | 🟢 较易 | ✅ | ✅ | 8.5k 🚀 +21/d | **65** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、模型与供应商路由、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.8k 🚀 +24/d | **64** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | MCP 支持、记忆与上下文、多智能体编排；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.4k | **60** |
| 🔹 **[yc-software/qm](https://github.com/yc-software/qm)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🔴 较重 | — | — | 15.6k 🚀 +8/d | **57** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.8k | **56** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +8/d | **55** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | 通知提醒；兼容 Codex。 ‡ | 🟢 较易 | — | — | 492 | **54** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code（DAC） 将桌面编程工作区和终端智能体连接到同一个执行内核。 面对跨文件、多轮对话、多种工具和多人讨论的工作，你可以保留项目上下文、维护可编辑的计划、委派独立子任务、查看执行过程，并让最终回答回到发起工作的对话中。 | 🟢 较易 | — | — | 428 | **52** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 560 | **47** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[bytedance/deer-flow](https://github.com/bytedance/deer-flow)、[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)、[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)、[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)

## 计费

*额度与用量管理*

看不到剩余额度，任务做到一半就被限流。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 31.6k 🚀 +666/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 跨 Agent 支持、通知提醒、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.8k 🚀 +962/d | **83** |
| ✅ **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、手机端访问；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 4.9k 🚀 +201/d | **74** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | API 网关与中转、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 19.8k 🚀 +32/d | **69** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 32.1k 🚀 +45/d | **67** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 292 | **56** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.9k 🚀 +10/d | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 308 🚀 +5/d | **53** |
| 🔹 **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | 自动故障转移、图形界面与桌面端、安全与隔离；兼容 Codex。 ‡ | 🔴 较重 | — | — | 927 🚀 +22/d | **52** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 545 🚀 +5/d | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 512 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.7k 🚀 +8/d | **51** |
| 🔹 **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 920 | **51** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、模型与供应商路由；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 559 | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 321 | **50** |

**也能做这件事：** [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)、[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)、[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 计费

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件、并行执行；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 65.6k 🚀 +267/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | 技能与插件；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 5.7k 🚀 +715/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 45.6k 🚀 +61/d | **73** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Agent 运行时、跨 Agent 支持、可自托管；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 3.9k 🚀 +47/d | **68** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 图形界面与桌面端、MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | — | — | 5.5k 🚀 +13/d | **65** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 11.1k 🚀 +22/d | **62** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | 模型与供应商路由、MCP 支持、可自托管。 ‡ | 🔴 较重 | — | — | 11.9k 🚀 +16/d | **55** |
| 🔹 **[xiaodou-official/xiaodou-open-platform](https://github.com/xiaodou-official/xiaodou-open-platform)** | 通知提醒、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 327 | **52** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 830 | **50** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 412 | **50** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、多账号切换；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **48** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 446 | **43** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[decolua/9router](https://github.com/decolua/9router)、[spinabot/brigade](https://github.com/spinabot/brigade)、[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

## 共享

*模型与供应商路由*

想让 Agent 跑在非默认的模型或供应商上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 106.4k 🚀 +188/d | **95** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows… † | 🟢 开箱即用 | ✅ | — | 154.9k 🚀 +122/d | **90** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、API 网关与中转、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 80.8k 🚀 +276/d | **90** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 一套用代码做片的风格工具箱： 66 种现成风格，也能做出你自己的。 拿来做什么：做什么片、发在哪个平台（竖屏就用 1080×1920 或 1080×1440），有没有品牌色、logo、字体或固定角色； | 🟡 需配置 | — | ✅ | 13.2k 🚀 +466/d | **84** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. † | 🟢 较易 | — | — | 20.6k 🚀 +1854/d | **80** |
| ✅ **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 3.8k 🚀 +104/d | **75** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 11.2k 🚀 +32/d | **61** |
| 🔹 **[openai/codex-security](https://github.com/openai/codex-security)** | Codex Security helps you find, investigate, and fix vulnerabilities in your code. † | 🟡 需配置 | — | — | 11.3k 🚀 +7/d | **58** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟡 需配置 | — | — | 2k 🚀 +10/d | **54** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | A coding agent for any model. † | 🟢 开箱即用 | ✅ | — | 355 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 718 | **50** |

**也能做这件事：** [zai-org/ZCode](https://github.com/zai-org/ZCode)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)、[yc-software/qm](https://github.com/yc-software/qm)、[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)、[ruvnet/metaharness](https://github.com/ruvnet/metaharness)、[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)、[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)、[hex/claude-council](https://github.com/hex/claude-council)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | 通知提醒、MCP 支持、跨 Agent 支持；兼容 Codex、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 16.1k 🚀 +1028/d | **88** |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy 是一个开源、开箱即用的 AI Agent。连接你的多台电脑与手机，把熟悉的 Agent、模型和已有订阅放在一起，培养一个懂你工作方式的伙伴。 | 🔴 较重 | — | — | 9.4k 🚀 +91/d | **73** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | API 网关与中转、图形界面与桌面端、模型与供应商路由。 ‡ | 🔴 较重 | — | — | 51.5k 🚀 +65/d | **71** |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 4.2k 🚀 +37/d | **68** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | 图形界面与桌面端、MCP 支持、API 网关与中转。 ‡ | 🟡 需配置 | — | — | 9.4k 🚀 +26/d | **65** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | 独立账号平台与中转站：OpenRouter、Kimi 开放平台（国内/国际版）、AnyRouter、AgentRouter、AIHubMix、老张 API、Dahl、FoxCode、肖恩 AI、Cubence、RightCode、Grsai、FreeModel、SharedChat、WONG公益站、Krill AI、EMRank、RelayFor、Daya API、Verce… 账号站点兼容架构… | 🟡 需配置 | — | ✅ | 5k 🚀 +4/d | **61** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排。 ‡ | 🟢 较易 | ✅ | — | 5.9k | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | MCP 支持、图形界面与桌面端、通知提醒；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 523 | **51** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、记忆与上下文、工作区隔离；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[decolua/9router](https://github.com/decolua/9router)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. † | 🟢 开箱即用 | ✅ | ✅ | 225.2k 🚀 +233/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 14.6k 🚀 +313/d | **88** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | 跨 Agent 支持、通知提醒；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 13.3k 🚀 +655/d | **84** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm 让你的编程智能体来做视频，也让你亲手修改。 一个真正的剪辑器。 可以移动、缩放、旋转页面里的任何元素，改它的文字、颜色和样式；摆放、裁剪、调整每个片段的 | 🟢 较易 | — | ✅ | 5.2k 🚀 +152/d | **80** |
| ✅ **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.4k 🚀 +15/d | **62** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 1.9k 🚀 +10/d | **62** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +32/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 485 | **56** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | 对接其他产品是一个部署在流程后端地址之后的独立服务，不进入本仓库： 新增语音厂商加的是一个 profile，而不是一个新客户端： | 🟡 需配置 | — | — | 550 🚀 +7/d | **51** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[openai/codex](https://github.com/openai/codex)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[xerj-org/xerj](https://github.com/xerj-org/xerj)、[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)、[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 152.5k 🚀 +272/d | **93** |
| ✅ **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | 跨 Agent 支持、可自托管、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 4.3k 🚀 +79/d | **72** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 4.5k 🚀 +31/d | **70** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、用量分析、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 910 | **56** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.4k 🚀 +7/d | **54** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 772 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 438 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、自动故障转移；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 510 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 600 | **45** |

**也能做这件事：** [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[automazeio/ccpm](https://github.com/automazeio/ccpm)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

## 账号

*多账号切换*

单个订阅额度会用完，需要在多个账号之间轮换，而不必手动重新登录。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 133.5k 🚀 +141/d | **89** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 18.3k 🚀 +22/d | **64** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.9k | **56** |
| 🔹 **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | 跨 Agent 支持、API 网关与中转、图形界面与桌面端；兼容 Codex、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 565 | **54** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[stablyai/orca](https://github.com/stablyai/orca)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)、[cita-777/metapi](https://github.com/cita-777/metapi)

## 模型路由

*并行执行*

任务串行执行、只能干等；并行能压缩总耗时。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | MCP 支持、通知提醒。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote 通过 pi 官方扩展 API 接入正在运行的 pi 会话，不修改 pi 源码，不接管终端。 会话始终由本机的 pi 进程持有；浏览器端看到的是同一会话的实时镜像，并可向该会话发送消息与命令，包括切换模型、调整思考级别、压缩上下文、管理会话树等。 | 🟢 较易 | — | — | 310 🚀 +31/d | **58** |
| 🔹 **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | 多智能体编排、技能与插件、记忆与上下文；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 577 | **51** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟡 需配置 | — | — | 477 | **46** |

**也能做这件事：** [yetone/magpie](https://github.com/yetone/magpie)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[fatwang2/search2ai](https://github.com/fatwang2/search2ai)、[crshdn/mission-control](https://github.com/crshdn/mission-control)、[Licoy/Quosparr](https://github.com/Licoy/Quosparr)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.21 倍（31,556 vs 152,506） |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 60.73x the stars (19,798 vs 326) | 🤖 自动（high） |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 26.64x the stars (11,750 vs 441) | 🤖 自动（high） |
| **[BennyKok/omg.dev](https://github.com/bennykok/omg.dev)** | **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 20.34x the stars (11,270 vs 554) | 🤖 自动（high） |
| **[Derpyu520/qq-bridge](https://github.com/derpyu520/qq-bridge)** | **[milind-soni/OpenMausBot](https://github.com/milind-soni/openmausbot)** | 4.50x the stars (16,132 vs 3,581) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 223.36x the stars (85,102 vs 381) | 🤖 自动（high） |
| **[MagicCube/agentara](https://github.com/magiccube/agentara)** | **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | 3.61x the stars (1,871 vs 519) | 🤖 自动（high） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.33x the stars (11,750 vs 2,203) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.77x the stars (34,082 vs 927) | 🤖 自动（high） |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.08x the stars (49,303 vs 365) | 🤖 自动（high） |
| **[Waishnav/devspace](https://github.com/waishnav/devspace)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.31x the stars (23,362 vs 5,421) | 🤖 自动（high） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 172.99x the stars (49,303 vs 285) | 🤖 自动（high） |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 221.66x the stars (106,396 vs 480) | 🤖 自动（high） |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 318.70x the stars (111,865 vs 351) | 🤖 自动（high） |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 99.61x the stars (30,182 vs 303) | 🤖 自动（high） |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 41.37x the stars (11,750 vs 284) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.30x the stars (140,558 vs 4,967) | 🤖 自动（high） |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.21x the stars (49,303 vs 3,733) | 🤖 自动（high） |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.21x the stars (11,750 vs 2,254) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.34x the stars (49,303 vs 367) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 29.01x the stars (11,750 vs 405) | 🤖 自动（high） |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 6.98x the stars (49,303 vs 7,067) | 🤖 自动（high） |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.67x the stars (23,362 vs 480) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.53x the stars (49,303 vs 317) | 🤖 自动（high） |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 123.04x the stars (34,082 vs 277) | 🤖 自动（high） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 479.65x the stars (298,821 vs 623) | 🤖 自动（high） |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | **[Gentleman-Programming/gentle-shell](https://github.com/gentleman-programming/gentle-shell)** | 6.97x the stars (1,965 vs 282) | 🤖 自动（high） |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 12.22x the stars (18,520 vs 1,515) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.24x the stars (298,821 vs 6,194) | 🤖 自动（high） |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 106.65x the stars (30,182 vs 283) | 🤖 自动（high） |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 155.78x the stars (152,506 vs 979) | 🤖 自动（high） |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 63.14x the stars (23,362 vs 370) | 🤖 自动（high） |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 617.40x the stars (298,821 vs 484) | 🤖 自动（high） |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 91.47x the stars (49,303 vs 539) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 100.18x the stars (140,558 vs 1,403) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.15x the stars (11,750 vs 2,828) | 🤖 自动（high） |
| **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 8.77x the stars (11,750 vs 1,340) | 🤖 自动（medium） |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.13x the stars (49,303 vs 3,756) | 🤖 自动（medium） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 9.43x the stars (4,705 vs 499) | 🤖 自动（medium） |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | 16.90x the stars (13,301 vs 787) | 🤖 自动（medium） |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 19.19x the stars (27,938 vs 1,456) | 🤖 自动（medium） |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.42x the stars (23,362 vs 5,290) | 🤖 自动（medium） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 43.58x the stars (18,520 vs 425) | 🤖 自动（medium） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.38x the stars (1,156 vs 486) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 8.00x the stars (19,798 vs 2,475) | 🤖 自动（high） |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 65.13x the stars (49,303 vs 757) | 🤖 自动（medium） |
| **[WenyuChiou/ai-research-skills](https://github.com/wenyuchiou/ai-research-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 81.36x the stars (49,303 vs 606) | 🤖 自动（medium） |
| **[Arvincreator/project-golem](https://github.com/arvincreator/project-golem)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 1.80x the stars (1,156 vs 641) | 🤖 自动（high） |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 1.21x the stars (329 vs 273) | 🤖 自动（medium） |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,303 vs 27,746) | 🤖 自动（medium） |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.28x the stars (1,156 vs 508) | 🤖 自动（high） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui | 27.7k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | desktop-ui | 7.1k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | teams | 6.2k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[Waishnav/devspace](https://github.com/Waishnav/devspace)** | mobile | 5.4k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (7/7)。 |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.3k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (9/9)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | mobile | 5k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | desktop-ui | 3.8k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui | 3.7k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[Derpyu520/qq-bridge](https://github.com/Derpyu520/qq-bridge)** | analytics-3 | 3.6k | 🔻 已被取代 | 已被 milind-soni/OpenMausBot 取代：covers 100% of capabilities (4/4)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | teams | 2.8k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (8/8)。 |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | teams | 2.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | teams | 2.2k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | failover | 1.5k | 🔻 已被取代 | 已被 xerj-org/xerj 取代：covers 100% of capabilities (4/4)。 |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | mobile | 1.5k | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | mobile | 1.4k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | teams | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (9/9)。 |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 979 | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (5/5)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | mobile | 927 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | desktop-ui-2 | 787 | 🔻 已被取代 | 已被 google/elephant-goldfish-model 取代：covers 100% of capabilities (4/4)。 |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 757 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | mcp-security | 641 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | teams | 623 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | desktop-ui | 606 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | mobile | 554 | 🔻 已被取代 | 已被 omnigent-ai/omnigent 取代：covers 100% of capabilities (7/7)。 |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | desktop-ui | 539 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[MagicCube/agentara](https://github.com/MagicCube/agentara)** | failover | 519 | 🔻 已被取代 | 已被 aoci-spec/aoci-code 取代：covers 100% of capabilities (5/5)。 |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | mcp-security | 508 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-security | 499 | 🔻 已被取代 | 已被 kajisho5/ffmpeg-skill 取代：covers 100% of capabilities (4/4)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | mcp-security | 486 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | teams | 484 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (5/5)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 480 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (5/5)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | sharing | 480 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | teams | 441 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | failover | 425 | 🔻 已被取代 | 已被 xerj-org/xerj 取代：covers 100% of capabilities (4/4)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | teams | 405 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | mobile | 381 | 🔻 已被取代 | 已被 bytedance/deer-flow 取代：covers 100% of capabilities (5/5)。 |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | mobile | 370 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (6/6)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 367 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui | 365 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[automagik-dev/genie](https://github.com/automagik-dev/genie)** | mobile | 351 | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (7/7)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 326 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (4/4)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 317 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | teams | 303 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | desktop-ui | 285 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[codecoradev/uteke](https://github.com/codecoradev/uteke)** | teams | 284 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[pax-beehive/paxm](https://github.com/pax-beehive/paxm)** | teams | 283 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (7/7)。 |
| **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | mobile | 282 | 🔻 已被取代 | 已被 Gentleman-Programming/gentle-shell 取代：covers 100% of capabilities (6/6)。 |
| **[lanes-sh/app](https://github.com/lanes-sh/app)** | mobile | 277 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (7/7)。 |
| **[sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree)** | mobile | 273 | 🔻 已被取代 | 已被 h0x91b/dev-3.0 取代：covers 100% of capabilities (7/7)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-11-07 11:07 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
