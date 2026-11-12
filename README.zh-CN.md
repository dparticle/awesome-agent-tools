<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**230 个工具**，分 **13 个分类** · **47 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-11-12 12:45 UTC**

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
| （无） | 项目**自带的中文 README**原文，作者自己的措辞 | 41 |
| ‡ | 我们**根据检测到的能力生成**的中文说明（能力名称本身有官方中文名） | 172 |
| † | 项目只写了英文，**保留英文原文，不做机器翻译** | 6 |

带 † 的条目我们**不会**把它翻成中文。翻译会让项目「说出」它从没说过的话，而这个仓库的全部价值就在于结论可核查——一句诚实的英文，比一段流畅的杜撰更有用。带 ‡ 的条目是**我们自己写的**概括，每条结论都能在项目 README 里找到对应证据。

如果你想补齐某个工具的中文说明，欢迎在 [`config/overrides.json`](config/overrides.json) 里加一条 `summary_zh`，它会以最高优先级显示。

---

## 桌面端

*技能与插件*

基础 Agent 不具备你的工作流，需要扩展。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)** | 并发上限：低核机器上 remotion still/render 会报 "Maximum for --concurrency is 2"。 CDN 访问不了：remotion.media 访问不了时（国内常见），headless-shell 自动下载会失败。 | 🟢 较易 | — | — | 18.9k 🚀 +271/d | **86** |
| 🏆 **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)** | 跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 26.9k 🚀 +244/d | **84** |
| 🏆 **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** | 图形界面与桌面端、通知提醒。 ‡ | 🟢 较易 | ✅ | — | 70.8k 🚀 +1218/d | **83** |
| 🏆 **[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 9k 🚀 +95/d | **82** |
| 🏆 **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | MCP 支持、跨 Agent 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 49.6k 🚀 +57/d | **78** |
| ✅ **[Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 8.8k 🚀 +56/d | **76** |
| ✅ **[kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 6.7k 🚀 +100/d | **75** |
| ✅ **[Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill)** | Eleven Claude skills that clone any app. † | 🔴 较重 | — | — | 9k 🚀 +195/d | **71** |
| ✅ **[eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills)** | 样式串味。五份报告共用 57 个类名，其中 13 个同名不同定义（.copy .kpis .badge .chip……），所以给每份样式的每条选择器加作用域前缀 图片路径。各报告的图相对自己那份 json 的目录（images/…、E01-01/f1.png），合成后按输出文件的位置重算 | 🟢 较易 | — | — | 6.5k 🚀 +67/d | **69** |
| ✅ **[AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer)** | Some of us write a lot of papers and grant proposals, and our team started using AI to help with drafts. † | 🟡 需配置 | — | — | 4.6k 🚀 +180/d | **66** |
| ✅ **[danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill)** | A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft m… † | 🟢 较易 | — | — | 6.4k 🚀 +41/d | **64** |
| ✅ **[nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 5k 🚀 +59/d | **64** |
| ✅ **[larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 6.8k 🚀 +16/d | **62** |
| ✅ **[s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)** | ip-as-logo is a compact Agent Skill for generating extremely simple, cute, company-ready IP mascots. † | 🟢 开箱即用 | ✅ | — | 6.5k 🚀 +16/d | **62** |
| 🔹 **[Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 4.4k 🚀 +28/d | **61** |
| 🔹 **[Nanako0129/sepia](https://github.com/Nanako0129/sepia)** | English \| 繁體中文 \| 简体中文 | 🟢 较易 | — | — | 3.8k 🚀 +24/d | **61** |
| 🔹 **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | 跨 Agent 支持、团队协作；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 3.8k | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **57** |
| 🔹 **[WenyuChiou/ai-research-skills](https://github.com/WenyuChiou/ai-research-skills)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 651 🚀 +9/d | **57** |
| 🔹 **[nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 4.3k 🚀 +23/d | **56** |
| 🔹 **[zvec-ai/zvec-grep](https://github.com/zvec-ai/zvec-grep)** | zg（zvec-grep），由 zvec 驱动， 将 ripgrep、BM25 与向量检索统一在一个本地优先的检索入口中。 | 🟡 需配置 | — | — | 4.3k | **56** |
| 🔹 **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/Game-Dev-Agentic-Skills)** | 跨 Agent 支持、MCP 支持、记忆与上下文；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 958 | **56** |
| 🔹 **[mco-org/mco](https://github.com/mco-org/mco)** | MCO 是一个轻量、CLI 优先的 AI Coding Agent 编排层。把同一个任务交给你明确选择的 Agent 和模型，并行执行，比较原始回答，再决定下一步。 | 🟢 开箱即用 | — | — | 554 | **56** |
| 🔹 **[jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 2.9k | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 跨 Agent 支持、计费与计量、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.1k | **55** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 🔌 多工具支持：开箱即用支持 32 款 AI 工具（Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Trae、Cline、Augment、Goose 等），并支持自定义扩展。 🔄 智能同步：自动化的软链接管理，确保您的工具始终使用最新版本的技能，无需手动复制文件。 | 🟢 开箱即用 | ✅ | ✅ | 1.1k | **55** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 并行执行；兼容 Claude Code。 ‡ | 🟢 开箱即用 | — | ✅ | 560 🚀 +6/d | **53** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟢 开箱即用 | — | — | 2.4k | **52** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 1.1k | **52** |
| 🔹 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | 多账号切换、团队协作；兼容 Claude Code、Droid。 ‡ | 🔴 较重 | — | — | 787 | **52** |

*还有 11 个工具见[完整索引](data/index.json)。*

**也能做这件事：** [garrytan/gstack](https://github.com/garrytan/gstack)、[anomalyco/opencode](https://github.com/anomalyco/opencode)、[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)、[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)、[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)、[qybaihe/bla](https://github.com/qybaihe/bla)、[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[langfuse/langfuse](https://github.com/langfuse/langfuse)、[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)

## 隔离与团队

*工作区隔离*

并行 Agent 会互相覆盖文件，除非各自有独立工作副本。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[garrytan/gstack](https://github.com/garrytan/gstack)** | 跨 Agent 支持、Agent 运行时、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 141.3k 🚀 +155/d | **91** |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 跨 Agent 支持、多智能体编排、可自托管；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 113.3k 🚀 +286/d | **89** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Agent 运行时；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 155.4k 🚀 +110/d | **88** |
| 🏆 **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | — | 12.5k 🚀 +120/d | **87** |
| 🏆 **[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)** | Agent 运行时、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | ✅ | 17.9k 🚀 +916/d | **85** |
| 🏆 **[openai/codex-security](https://github.com/openai/codex-security)** | 模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 12.1k 🚀 +153/d | **81** |
| 🏆 **[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)** | Agent 运行时。 ‡ | 🟢 较易 | — | — | 22.7k 🚀 +422/d | **78** |
| ✅ **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | 图形界面与桌面端、MCP 支持、Agent 运行时；兼容 Codex。 ‡ | 🟢 开箱即用 | — | ✅ | 8.2k 🚀 +60/d | **74** |
| ✅ **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | MCP 支持、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 48.6k 🚀 +57/d | **74** |
| ✅ **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 跨 Agent 支持、多智能体编排、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 34.2k 🚀 +31/d | **73** |
| ✅ **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 33.4k 🚀 +42/d | **72** |
| ✅ **[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)** | 多智能体编排、Agent 运行时、自动故障转移；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.3k 🚀 +66/d | **71** |
| ✅ **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 跨 Agent 支持、Agent 运行时、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 28k 🚀 +16/d | **69** |
| ✅ **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 多智能体编排、技能与插件、MCP 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 1.7k | **62** |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | MCP 支持、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 1.3k 🚀 +6/d | **58** |
| 🔹 **[mindmuxai/brain.md](https://github.com/mindmuxai/brain.md)** | Agent 运行时、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 647 🚀 +11/d | **58** |
| 🔹 **[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)** | 两个 AI Agent 做同一个任务：一个写代码，另一个审查。 自带端点 — 导入其他 Agent 的配置（opencode、codex、claude、kimi、pi、omp、gemini、killi）、手动添加密钥，或用 ChatGPT、Command Code、OpenCode Go、Muse Code 订阅登录 | 🟢 较易 | — | ✅ | 388 | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 619 | **56** |
| 🔹 **[styler-ai/ProjectAtlas](https://github.com/styler-ai/ProjectAtlas)** | MCP 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 502 | **56** |
| 🔹 **[automazeio/ccpm](https://github.com/automazeio/ccpm)** | 跨 Agent 支持、自动故障转移、安全与隔离；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 8.4k | **55** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | MCP 支持、跨 Agent 支持、安全与隔离；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 792 | **55** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | MCP 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 452 | **55** |
| 🔹 **[h0x91b/dev-3.0](https://github.com/h0x91b/dev-3.0)** | 跨 Agent 支持、图形界面与桌面端、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 333 | **55** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | Dao Code(命令 dao)是终端原生的 AI 编码助手:在你的终端里读代码、写代码、跑命令、修 bug,边流式展示推理与工具调用,边在审批门下安全执行,直到任务做完。 它面向 DeepSeek V4(1M 上下文),中文优先,灵感来自 Claude Code,但走的是另一条路——不靠贵模型堆体验,而是充分发挥 DeepSeek 的高性价比与极低缓存定价:通过工程化的字节稳定前缀与缓存复用… | 🟡 需配置 | — | — | 787 | **52** |
| 🔹 **[robzilla1738/harness-terminal](https://github.com/robzilla1738/harness-terminal)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 309 | **52** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 跨 Agent 支持、MCP 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 3k | **49** |
| 🔹 **[newsnowlabs/dockside](https://github.com/newsnowlabs/dockside)** | 跨 Agent 支持、远程控制、团队协作；兼容 Claude Code、Codex、Copilot。 ‡ | 🔴 较重 | — | — | 323 | **47** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)、[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)、[felinics/Memoh](https://github.com/felinics/Memoh)、[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)、[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 共享

*可自托管*

不希望代码或密钥经过他人的服务器。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** | 记忆与上下文、技能与插件、MCP 支持；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 58.5k (+184/d) | **90** |
| 🏆 **[affaan-m/ECC](https://github.com/affaan-m/ECC)** | Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ ECC 2.0 alpha 已进入仓库 —— ecc2/ 下的 Rust 控制层现已可在本地构建，并提供 dashboard、start、sessions、status、stop、resume 与 daemon 命令。 | 🟡 需配置 | — | — | 301.7k 🚀 +573/d | **89** |
| 🏆 **[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 7.3k 🚀 +562/d | **85** |
| 🏆 **[nightly-labs/openbot](https://github.com/nightly-labs/openbot)** | 图形界面与桌面端、会话持久化、工作区隔离；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 7.2k 🚀 +209/d | **84** |
| 🏆 **[superdesigndev/treg](https://github.com/superdesigndev/treg)** | MCP 支持、模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟢 较易 | — | — | 7.9k 🚀 +86/d | **80** |
| 🏆 **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 跨 Agent 支持、MCP 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 15.7k 🚀 +81/d | **78** |
| ✅ **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 12.2k 🚀 +69/d | **76** |
| ✅ **[TencentCloud/Octop](https://github.com/TencentCloud/Octop)** | Octop Browser — 基于 CDP 的浏览器自动化，支持持久化配置，用于网页类任务。 Octop Gateway — 多平台 IM 通道桥接，将各类入站消息归一为统一的处理管线。 | 🟢 较易 | — | — | 12k 🚀 +46/d | **73** |
| ✅ **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 30.3k 🚀 +27/d | **70** |
| ✅ **[zai-org/ZCode](https://github.com/zai-org/ZCode)** | 图形界面与桌面端、Agent 运行时、模型与供应商路由。 ‡ | 🟢 较易 | ✅ | ✅ | 8.6k 🚀 +20/d | **65** |
| 🔹 **[spinabot/brigade](https://github.com/spinabot/brigade)** | MCP 支持、记忆与上下文、多智能体编排；兼容 Claude Code、Codex、Copilot、Droid。 ‡ | 🟡 需配置 | — | — | 11.4k | **60** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 桌面、浏览器、网络与长期记忆 — 即使关上笔记本，Agent 也不会停 Twilight AI — 给 Go 用的轻量 AI SDK，风格参考 Vercel AI SDK | 🟡 需配置 | — | — | 2.8k | **56** |
| 🔹 **[vb2250158/RabiRoute](https://github.com/vb2250158/RabiRoute)** | 通知提醒；兼容 Codex。 ‡ | 🟢 较易 | — | — | 493 | **54** |
| 🔹 **[yetone/cumora](https://github.com/yetone/cumora)** | 跨 Agent 支持、图形界面与桌面端、手机端访问；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.2k 🚀 +6/d | **53** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | MCP 支持、技能与插件、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 309 | **52** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | DeepAgent Code（DAC） 将桌面编程工作区和终端智能体连接到同一个执行内核。 面对跨文件、多轮对话、多种工具和多人讨论的工作，你可以保留项目上下文、维护可编辑的计划、委派独立子任务、查看执行过程，并让最终回答回到发起工作的对话中。 | 🟢 较易 | — | — | 428 | **51** |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 安全与隔离、MCP 支持、图形界面与桌面端；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 523 | **50** |
| 🔹 **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | MCP 支持、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟡 需配置 | — | — | 565 | **47** |

**也能做这件事：** [nexu-io/open-design](https://github.com/nexu-io/open-design)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)、[QuantumNous/new-api](https://github.com/QuantumNous/new-api)、[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)、[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)、[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)、[cordum-io/cordum](https://github.com/cordum-io/cordum)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)、[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)

## MCP与安全

*MCP 支持*

Agent 需要通过标准协议访问外部工具与数据。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[lexmount/moli](https://github.com/lexmount/moli)** | Extraction-optimized outputs — the CLI directly produces HTML, Markdown, Unified automation binary — CDP, WebDriver Classic, and WebDriver BiDi † | 🟢 开箱即用 | ✅ | ✅ | 23.5k 🚀 +116/d | **88** |
| 🏆 **[qybaihe/bla](https://github.com/qybaihe/bla)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.4k 🚀 +300/d | **85** |
| 🏆 **[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)** | 跨 Agent 支持、Agent 运行时、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | ✅ | 5.8k 🚀 +194/d | **83** |
| 🏆 **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)** | 技能与插件、跨 Agent 支持、多智能体编排；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 5.2k 🚀 +92/d | **82** |
| 🏆 **[0sec-labs/0](https://github.com/0sec-labs/0)** | Agent 运行时、图形界面与桌面端。 ‡ | 🟢 较易 | ✅ | — | 1.3k 🚀 +144/d | **78** |
| ✅ **[Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)** | Agent 运行时、通知提醒、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 4.6k 🚀 +93/d | **75** |
| ✅ **[Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** | 技能与插件、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Cursor。 ‡ | 🟡 需配置 | — | — | 9.4k 🚀 +97/d | **73** |
| ✅ **[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)** | 在 Codex 原生模型选择器中使用账户可用的 ChatGPT 网页版模型，包括 Pro。 消息通过已登录的 ChatGPT 网页会话发送，并受该账户适用的使用限制约束。 | 🟢 较易 | — | — | 15.7k 🚀 +24/d | **64** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | ✅ | — | 6.6k | **62** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | 通知提醒、并行执行、额度与用量管理。 ‡ | 🟡 需配置 | — | — | 9.2k | **58** |
| 🔹 **[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)** | 跨 Agent 支持、记忆与上下文、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 4.3k | **57** |
| 🔹 **[unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | ✅ | — | 8.5k | **56** |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **56** |
| 🔹 **[1llu50ry/mcp-reverse](https://github.com/1llu50ry/mcp-reverse)** | 跨 Agent 支持、多智能体编排、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 567 | **56** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 模型与供应商路由、跨 Agent 支持、多智能体编排；兼容 Cursor、Cline / Roo。 ‡ | 🟢 开箱即用 | — | — | 478 | **55** |
| 🔹 **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | English \| 简体中文 \| 繁體中文 \| 廣東話 \| 日本語 \| 한국어 \| Español \| Bahasa Indonesia \| Italiano \| Português \| Türkçe \| Tiếng Việt \| ไทย | 🟢 较易 | — | — | 392 | **53** |
| 🔹 **[AndrewDryga/emisar](https://github.com/AndrewDryga/emisar)** | 跨 Agent 支持、Agent 运行时、远程控制；兼容 Codex、Cursor。 ‡ | 🟢 较易 | — | — | 375 🚀 +6/d | **53** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 跨 Agent 支持、多智能体编排、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Copilot。 ‡ | 🟡 需配置 | — | — | 744 | **52** |
| 🔹 **[410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes)** | 跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 542 | **51** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 技能与插件、跨 Agent 支持、通知提醒；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | — | 447 | **51** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | 技能与插件、图形界面与桌面端、模型与供应商路由；兼容 Codex。 ‡ | 🟡 需配置 | — | — | 371 | **50** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | 跨 Agent 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex、Gemini CLI。 ‡ | 🟡 需配置 | — | — | 478 | **46** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 一个 Model Context Protocol (MCP) 服务器，用于结构化的规格驱动开发，配备实时仪表板和 VSCode 扩展。 | 🔴 较重 | — | — | 4.3k | **45** |
| 👀 **[IBM/mcp](https://github.com/IBM/mcp)** | Agent 运行时、多智能体编排。 ‡ | 🟡 需配置 | — | — | 419 | **42** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[nexu-io/open-design](https://github.com/nexu-io/open-design)、[yetone/magpie](https://github.com/yetone/magpie)、[affaan-m/ECC](https://github.com/affaan-m/ECC)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

## 记忆与故障转移

*会话持久化*

合上笔记本或断网就会中断长时间运行的会话。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 面向 AI 智能体的本地优先搜索引擎与 MCP 服务。 一个 Rust 二进制程序即可为代码、文档、日志、JSONL/CSV 和 PDF 建立索引，提供 BM25 全文、向量与混合搜索、代码搜索和智能体记忆，接口兼容 Elasticsearch API。 | 🟢 较易 | — | — | 18.9k 🚀 +80/d | **80** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 跨 Agent 支持、模型与供应商路由、可自托管；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 33.3k 🚀 +29/d | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.9k 🚀 +21/d | **64** |
| ✅ **[shengjidaguai-china/goutoujunshi](https://github.com/shengjidaguai-china/goutoujunshi)** | 多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 9.6k 🚀 +45/d | **62** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | 跨 Agent 支持、技能与插件、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🟢 较易 | — | — | 1.4k 🚀 +15/d | **58** |
| 🔹 **[winstonkoh87/Athena-Public](https://github.com/winstonkoh87/Athena-Public)** | 跨 Agent 支持；兼容 Claude Code、Gemini CLI、Cursor、Copilot。 ‡ | 🟢 较易 | — | — | 622 | **56** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | AOCI-CODE 是一种为 AI Agent 建立软件项目全局认知的索引方法，可提供持久化、可治理的代码仓库认知地图。 | 🔴 较重 | — | — | 1.9k 🚀 +6/d | **55** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 438 | **54** |
| 🔹 **[GizClaw/flowcraft](https://github.com/GizClaw/flowcraft)** | 技能与插件；兼容 Codex、Droid。 ‡ | 🟢 较易 | — | — | 411 | **54** |
| 🔹 **[itechmeat/open-second-brain](https://github.com/itechmeat/open-second-brain)** | 跨 Agent 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 552 🚀 +8/d | **53** |
| 🔹 **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由。 ‡ | 🟡 需配置 | — | — | 17.4k | **52** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 跨 Agent 支持、通知提醒、远程控制；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 1.4k | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 让 Claude Code、Codex、CodeBuddy Code、Cursor、Windsurf、Copilot、Gemini CLI、OpenCode、Grok Build、OpenClaw、Hermes Agent、Oh-my-Pi、Pi、Kiro、Antigravity、Trae、DeepSeek Harness、WorkBuddy 和任何 MCP Agent 共用同一套项目记忆。 | 🔴 较重 | — | — | 928 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | 跨 Agent 支持、自动故障转移、用量分析；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 458 | **52** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 跨 Agent 支持、Agent 运行时、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 932 | **51** |
| 🔹 **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | 跨 Agent 支持、多智能体编排、API 网关与中转；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 717 | **51** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 跨 Agent 支持、自动故障转移、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | — | 679 | **50** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | 技能与插件、自动故障转移、模型与供应商路由。 ‡ | 🔴 较重 | — | — | 529 | **50** |
| 🔹 **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | 多智能体编排、跨 Agent 支持；兼容 Claude Code、Codex、Qwen Code。 ‡ | 🟡 需配置 | — | — | 488 | **49** |
| 🔹 **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | 图形界面与桌面端、通知提醒、可自托管。 ‡ | 🔴 较重 | — | — | 488 | **46** |
| 👀 **[EliaAlberti/cpr-compress-preserve-resume](https://github.com/EliaAlberti/cpr-compress-preserve-resume)** | 技能与插件、自动故障转移、用量分析；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 525 | **43** |

**也能做这件事：** [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)、[paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)、[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)、[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)、[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)、[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[spinabot/brigade](https://github.com/spinabot/brigade)

## 计费

*额度与用量管理*

看不到剩余额度，任务做到一半就被限流。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | Claude Code 跑 Kimi，Codex 跑 DeepSeek，Gemini CLI 跑 GLM，OpenCode 用你的 ChatGPT 订阅。 | 🟢 开箱即用 | — | ✅ | 35.2k 🚀 +737/d | **91** |
| 🏆 **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** | 跨 Agent 支持、通知提醒、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.6k 🚀 +153/d | **84** |
| ✅ **[decolua/9router](https://github.com/decolua/9router)** | 编程永不停歇。使用 RTK + 自动切换到免费/低价 AI 模型，节省 20-40% 的 tokens。 kr/claude-sonnet-4.5 (通过 Kiro 免费使用 Claude 4.5，约 50 积分/月) | 🔴 较重 | — | — | 32.3k 🚀 +48/d | **69** |
| ✅ **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | API 网关与中转、跨 Agent 支持、手机端访问；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4k 🚀 +56/d | **68** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | API 网关与中转、图形界面与桌面端、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 19.9k 🚀 +25/d | **68** |
| ✅ **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | 多智能体编排、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 18.4k 🚀 +29/d | **66** |
| 🔹 **[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)** | MCP 支持、通知提醒、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟡 需配置 | — | — | 3.6k 🚀 +17/d | **60** |
| 🔹 **[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)** | 独立账号平台与中转站：OpenRouter、Kimi 开放平台（国内/国际版）、AnyRouter、AgentRouter、AIHubMix、老张 API、Dahl、FoxCode、肖恩 AI、Cubence、RightCode、Grsai、FreeModel、SharedChat、WONG公益站、Krill AI、EMRank、RelayFor、Daya API、Verce… 账号站点兼容架构… | 🟡 需配置 | — | ✅ | 5.1k | **60** |
| 🔹 **[Appllama/appllama-skills](https://github.com/Appllama/appllama-skills)** | MCP 支持、跨 Agent 支持、手机端访问；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 5.1k 🚀 +36/d | **57** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 图形界面与桌面端；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 2.9k | **56** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | MCP 支持、技能与插件、API 网关与中转；兼容 Claude Code、Codex、Cursor、Cline / Roo。 ‡ | 🟡 需配置 | — | — | 295 | **56** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 通知提醒、跨 Agent 支持、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、Cursor。 ‡ | 🔴 较重 | — | — | 3.3k | **53** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 325 | **53** |
| 🔹 **[basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api)** | 模型与供应商路由、可自托管、会话持久化；兼容 Codex。 ‡ | 🔴 较重 | — | — | 6.9k 🚀 +6/d | **52** |
| 🔹 **[Nanako0129/syrtis](https://github.com/Nanako0129/syrtis)** | Syrtis 是一款免费、基于 MIT 协议的开源 macOS 菜单栏软件，直接读取电脑上 AI 编程工具已有的会话日志，实时显示 token 用量、花费与订阅额度。 它支持超过 25 款工具——包括 Claude Code、Codex、Cursor、OpenCode、Gemini CLI、Copilot、Kiro 与 Antigravity——完全在本地设备完成解析，无 Dock 图标、不收集… | 🟢 较易 | — | ✅ | 517 | **52** |
| 🔹 **[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)** | ChatGPT 付费订阅的网页版额度大量闲置，Codex 却在消耗紧张的 API 额度做 规划和 Review。 本项目把"思考"交给你已付费的网页版 ChatGPT，Codex 只负责 执行。 | 🔴 较重 | — | — | 7.7k 🚀 +5/d | **51** |
| 🔹 **[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)** | 跨 Agent 支持、图形界面与桌面端、API 网关与中转；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 546 | **51** |
| 🔹 **[yan-labs/yan-skills](https://github.com/yan-labs/yan-skills)** | 跨 Agent 支持、API 网关与中转、多智能体编排；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 较易 | — | — | 300 🚀 +5/d | **51** |
| 🔹 **[Licoy/Quosparr](https://github.com/Licoy/Quosparr)** | MCP 支持、模型与供应商路由、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 326 | **50** |

**也能做这件事：** [farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)、[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)

## 移动端

*语音输入*

在手机上敲长提示词很痛苦。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 跨 Agent 支持、多智能体编排、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 167.9k 🚀 +168/d | **98** |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 跨 Agent 支持、工作区隔离、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 123k 🚀 +970/d | **92** |
| 🏆 **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)** | 通知提醒、MCP 支持、图形界面与桌面端；兼容 Codex、OpenCode、Cursor、Cline / Roo。 ‡ | 🟢 较易 | — | — | 21.5k 🚀 +1081/d | **88** |
| 🏆 **[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)** | 图形界面与桌面端、记忆与上下文、API 网关与中转；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 8.9k 🚀 +342/d | **86** |
| 🏆 **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 在你自己的机器上并行运行 agents。无论在手机上还是桌前，都能推进交付。 跨设备： 支持 iOS、Android、桌面端、Web 和 CLI。 | 🟢 较易 | — | ✅ | 23.9k 🚀 +103/d | **83** |
| 🏆 **[wangzan101/Mika](https://github.com/wangzan101/Mika)** | 计费与计量、MCP 支持、模型与供应商路由；兼容 OpenCode。 ‡ | 🟢 较易 | — | ✅ | 8.3k 🚀 +641/d | **81** |
| 🏆 **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** | 从手机、电脑、浏览器继续使用你的 DeepSeek Harness 实例。无论使用哪台设备，都可以回到同一个 Harness 会话。 | 🟡 需配置 | — | — | 2.7k 🚀 +115/d | **79** |
| ✅ **[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)** | 图形界面与桌面端、跨 Agent 支持、通知提醒；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 7.1k 🚀 +24/d | **66** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | MCP 支持、跨 Agent 支持、技能与插件；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 5.3k 🚀 +19/d | **65** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 跨 Agent 支持、图形界面与桌面端、多智能体编排；兼容 Claude Code、Codex、OpenCode。 ‡ | 🟢 较易 | ✅ | ✅ | 24.6k 🚀 +15/d | **64** |
| ✅ **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 图形界面与桌面端、安全与隔离、MCP 支持；兼容 Claude Code。 ‡ | 🟢 较易 | — | ✅ | 15.4k 🚀 +15/d | **64** |
| ✅ **[leepokai/Codync](https://github.com/leepokai/Codync)** | 图形界面与桌面端、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 2.1k 🚀 +21/d | **64** |
| 🔹 **[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids)** | MCP 支持、通知提醒、自动故障转移；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 5.2k | **56** |
| 🔹 **[AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)** | 记忆与上下文、通知提醒。 ‡ | 🟡 需配置 | — | — | 3.8k 🚀 +9/d | **54** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | MCP 支持、技能与插件、跨 Agent 支持；兼容 Claude Code、Copilot。 ‡ | 🟢 较易 | — | — | 1.1k | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 多智能体编排、Agent 运行时、MCP 支持；兼容 Codex。 ‡ | 🟢 较易 | ✅ | — | 3.5k | **51** |
| 🔹 **[LeoYeAI/agent-master-skills](https://github.com/LeoYeAI/agent-master-skills)** | 跨 Agent 支持、自动故障转移、计费与计量；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |
| 🔹 **[BennyKok/omg.dev](https://github.com/BennyKok/omg.dev)** | 跨 Agent 支持、Agent 运行时、通知提醒；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 556 | **50** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 通知提醒、MCP 支持、模型与供应商路由；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 1.4k | **48** |

**也能做这件事：** [makecindy/cindy](https://github.com/makecindy/cindy)、[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)、[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)

## 共享与模型路由

*配额共享与分发*

订阅容量超过个人所需，想安全地分给他人共用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 107.3k 🚀 +184/d | **95** |
| 🏆 **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | 跨 Agent 支持、图形界面与桌面端、技能与插件；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 82.1k 🚀 +259/d | **90** |
| 🏆 **[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)** | 99 种影片风格，交给你的编程 agent。挑一个风格，带上你的故事，agent 用代码把整支片做出来。 | 🟡 需配置 | — | ✅ | 15.1k 🚀 +384/d | **84** |
| ✅ **[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)** | MCP 支持、Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟡 需配置 | — | — | 17.9k 🚀 +24/d | **64** |
| ✅ **[maximhq/bifrost](https://github.com/maximhq/bifrost)** | 图形界面与桌面端、MCP 支持、自动故障转移。 ‡ | 🟡 需配置 | — | — | 9.5k 🚀 +19/d | **63** |
| 🔹 **[MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)** | gpt-instruct 提供面向 Codex 的提示词与可复现评测工具链，重点改善复杂任务的首轮执行、过程连续性、工件验证和可运行回滚。 | 🟡 需配置 | — | — | 11.4k 🚀 +32/d | **61** |
| 🔹 **[zhnt/loushang](https://github.com/zhnt/loushang)** | Loushang 是一个把复杂工作变成可运行流程的智能工作系统。 会话：可恢复、可分叉、可导出、可检查的 coding 对话与执行记录。 | 🟡 需配置 | — | — | 2.1k 🚀 +11/d | **55** |
| 🔹 **[Folkbench/folkbench](https://github.com/Folkbench/folkbench)** | 跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | ✅ | 3.8k | **54** |
| 🔹 **[Swival/swival](https://github.com/Swival/swival)** | Agent 运行时。 ‡ | 🟢 开箱即用 | ✅ | — | 358 | **53** |
| 🔹 **[Xpropel/Pi-Remote](https://github.com/Xpropel/Pi-Remote)** | Pi-Remote 通过 pi 官方扩展 API 接入正在运行的 pi 会话，不修改 pi 源码，不接管终端。 会话始终由本机的 pi 进程持有；浏览器端看到的是同一会话的实时镜像，并可向该会话发送消息与命令，包括切换模型、调整思考级别、压缩上下文、管理会话树等。 | 🟢 较易 | — | — | 328 | **53** |
| 🔹 **[gmickel/flow-next](https://github.com/gmickel/flow-next)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 723 | **50** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 跨 Agent 支持、自动故障转移、图形界面与桌面端；兼容 Claude Code、Gemini CLI、OpenCode、Cursor。 ‡ | 🔴 较重 | — | — | 561 | **49** |

**也能做这件事：** [yetone/magpie](https://github.com/yetone/magpie)、[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)、[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)、[QuantumNous/new-api](https://github.com/QuantumNous/new-api)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)、[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)、[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)、[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)、[tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory)

## 用量分析

*计费与计量*

多人共用容量时，必须精确计量并结算。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)** | 跨 Agent 支持、技能与插件、并行执行；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 66.7k 🚀 +217/d | **91** |
| 🏆 **[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx)** | Agent 运行时、技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 7.1k 🚀 +277/d | **84** |
| 🏆 **[vAPI-Network/vapi-network](https://github.com/vAPI-Network/vapi-network)** | MCP 支持、跨 Agent 支持、自动故障转移；兼容 Claude Code、Codex、Cursor、Droid。 ‡ | 🟡 需配置 | — | — | 4.2k 🚀 +105/d | **78** |
| ✅ **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号管理 - 支持多种上游账号类型（OAuth、API Key） 内置支付系统 - 支持 EasyPay 易支付、支付宝官方、微信官方、Stripe，用户自助充值，无需独立部署支付服务（配置指南） | 🟡 需配置 | — | — | 45.9k 🚀 +62/d | **73** |
| ✅ **[zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills)** | Agent 运行时、跨 Agent 支持；兼容 Claude Code、Codex。 ‡ | 🟢 较易 | — | — | 4.1k 🚀 +49/d | **69** |
| ✅ **[aipoch/open-science](https://github.com/aipoch/open-science)** | 图形界面与桌面端、MCP 支持、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | ✅ | 5.5k 🚀 +7/d | **65** |
| ✅ **[trailhq/Trail-Code](https://github.com/trailhq/Trail-Code)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 11.2k 🚀 +19/d | **62** |
| 🔹 **[trycompai/crm](https://github.com/trycompai/crm)** | MCP 支持。 ‡ | 🔴 较重 | — | — | 12k 🚀 +18/d | **54** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | MCP 支持、跨 Agent 支持、工作区隔离；兼容 Claude Code、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 415 | **51** |
| 🔹 **[grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)** | 记忆与上下文；兼容 OpenCode。 ‡ | 🟡 需配置 | — | — | 839 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 跨 Agent 支持、多智能体编排、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 较易 | — | — | 1.2k | **48** |
| 👀 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | MCP 支持；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 449 | **43** |

**也能做这件事：** [nightly-labs/openbot](https://github.com/nightly-labs/openbot)、[wangzan101/Mika](https://github.com/wangzan101/Mika)、[superdesigndev/treg](https://github.com/superdesigndev/treg)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[makecindy/cindy](https://github.com/makecindy/cindy)、[TencentCloud/Octop](https://github.com/TencentCloud/Octop)、[topoteretes/cognee](https://github.com/topoteretes/cognee)、[decolua/9router](https://github.com/decolua/9router)、[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)、[spinabot/brigade](https://github.com/spinabot/brigade)

## 故障转移

*自动故障转移*

某个账号或供应商不可用时，任务应自动切到下一个而不是中断。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 跨 Agent 支持、Agent 运行时、多账号切换；兼容 Codex、Cursor。 ‡ | 🟢 开箱即用 | — | ✅ | 135k 🚀 +292/d | **89** |
| 🏆 **[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)** | 一个 agent skill，能找到照片的拍摄地点——并展示它的推理过程。 街景核验：match.py 整图排序不理想（盛花期，照片在人行道上拍而街景车走在路中间），于是用 --query-box 0,900,1440,1600 只比树所在的区域，再取 2009 / 2024 两期街景核对石墙、台阶、路灯杆这些不变的地物。 | 🟢 开箱即用 | — | — | 6.9k 🚀 +106/d | **86** |
| 🏆 **[alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion)** | Agent 运行时、技能与插件；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | — | 6.8k 🚀 +184/d | **86** |
| ✅ **[t3dotgg/tstack](https://github.com/t3dotgg/tstack)** | 跨 Agent 支持、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟡 需配置 | — | — | 3.5k 🚀 +185/d | **74** |
| ✅ **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)** | 展开请求看细节：读取已保留的请求头、提交数据、响应正文、耗时与错误，筛选流量或直接查看某个 JSON 字段。 验证并保留证据：配置任务内的请求修改、拦截、模拟响应或同源请求重放，导出 JSON，供后续复查和分享。 | 🟢 较易 | — | — | 10.3k 🚀 +40/d | **68** |
| ✅ **[xai-org/grok-build](https://github.com/xai-org/grok-build)** | 跨 Agent 支持、Agent 运行时、MCP 支持；兼容 Codex、OpenCode。 ‡ | 🟢 开箱即用 | — | — | 27.8k 🚀 +9/d | **63** |
| ✅ **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | 跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 2k 🚀 +13/d | **62** |
| 🔹 **[breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** | Node 22+ LTS（用于钩子脚本 — 通常与 Claude Code / Codex / Gemini CLI 一起已安装） /om-review-brief 通过汇总所有内容生成完整的评估简报：成就记录、决策、事件、能力证据和 1:1 反馈 | 🟡 需配置 | — | — | 5.5k | **58** |
| 🔹 **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | 技能与插件、跨 Agent 支持、Agent 运行时；兼容 Claude Code、OpenCode、Copilot。 ‡ | 🔴 较重 | — | — | 1.9k 🚀 +5/d | **56** |
| 🔹 **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | 模型与供应商路由、技能与插件；兼容 Claude Code。 ‡ | 🟡 需配置 | — | — | 8k 🚀 +10/d | **50** |
| 👀 **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | Memory Palace 为 LLM Agent 提供持久化、可检索、可审计的外部记忆，让每次对话都能在之前的基础上继续，而不是从零开始。 | 🟡 需配置 | — | — | 316 | **44** |

**也能做这件事：** [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)、[farion1231/cc-switch](https://github.com/farion1231/cc-switch)、[garrytan/gstack](https://github.com/garrytan/gstack)、[amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness)、[xerj-org/xerj](https://github.com/xerj-org/xerj)、[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)、[Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell)、[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)、[Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)、[maximhq/bifrost](https://github.com/maximhq/bifrost)

## 桌面端

*图形界面与桌面端*

纯终端工具把不熟悉命令行的人挡在门外。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | The open source coding agent. † | 🟢 开箱即用 | ✅ | ✅ | 226.3k 🚀 +231/d | **90** |
| 🏆 **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** | MCP 支持；兼容 Claude Code。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 15.9k 🚀 +261/d | **88** |
| 🏆 **[openfilm/openfilm](https://github.com/openfilm/openfilm)** | OpenFilm 让你的编程智能体来做视频，也让你亲手修改。 一个真正的剪辑器。 可以移动、缩放、旋转页面里的任何元素，改它的文字、颜色和样式；摆放、裁剪、调整每个片段的 | 🟢 较易 | — | ✅ | 5.9k 🚀 +143/d | **80** |
| 🔹 **[Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)** | 一张图，一种心情。换掉壁纸，原生控件一个不动 —— 侧栏、卡片、项目选择和输入框都是真的。 | 🟢 开箱即用 | ✅ | ✅ | 15.4k 🚀 +8/d | **61** |
| 🔹 **[zeronsh/zeron](https://github.com/zeronsh/zeron)** | 在本地管理你的编码 agent（Claude Code、Codex、Cursor、Devin、Grok、Hermes、Pi、Antigravity），也可以打开多设备同步。 | 🟢 开箱即用 | ✅ | ✅ | 3.5k 🚀 +8/d | **59** |
| 🔹 **[aicodeking/leanrea](https://github.com/aicodeking/leanrea)** | 跨 Agent 支持、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 4.2k 🚀 +34/d | **58** |
| 🔹 **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | 免费、开源的一站式平台，统一管理你所有的 AI 编程 Agent —— 覆盖桌面、CLI、Web 三端。 Agent-first CLI —— 发现专为 Agent 打造的 CLI 工具，这是 Agent 扩展生态的新兴方向。 | 🟢 开箱即用 | — | — | 491 | **56** |
| 🔹 **[zhinkgit/embeddedskills](https://github.com/zhinkgit/embeddedskills)** | 跨 Agent 支持；兼容 Claude Code、Codex、Cursor。 ‡ | 🟢 开箱即用 | — | — | 797 | **53** |
| 🔹 **[rasonyang/ai-native-callcenter](https://github.com/rasonyang/ai-native-callcenter)** | 对接其他产品是一个部署在流程后端地址之后的独立服务，不进入本仓库： 新增语音厂商加的是一个 profile，而不是一个新客户端： | 🟡 需配置 | — | — | 602 🚀 +10/d | **52** |
| 👀 **[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem)** | MCP 支持、技能与插件。 ‡ | 🟡 需配置 | — | — | 642 | **38** |

**也能做这件事：** [stablyai/orca](https://github.com/stablyai/orca)、[openai/codex](https://github.com/openai/codex)、[google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)、[qybaihe/bla](https://github.com/qybaihe/bla)、[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)、[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[getpaseo/paseo](https://github.com/getpaseo/paseo)、[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)、[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)、[xerj-org/xerj](https://github.com/xerj-org/xerj)

## 供应商

*多供应商聚合*

订阅和 API Key 散落各处，希望统一到一个入口。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | MCP 支持、图形界面与桌面端、自动故障转移；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟢 较易 | — | — | 153.9k 🚀 +273/d | **93** |
| ✅ **[ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel)** | 图形界面与桌面端、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | — | — | 4.6k 🚀 +28/d | **69** |
| 🔹 **[HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter)** | 跨 Agent 支持、可自托管、MCP 支持；兼容 Claude Code、Codex、Gemini CLI、OpenCode。 ‡ | 🟡 需配置 | — | — | 4.3k 🚀 +12/d | **58** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 图形界面与桌面端、模型与供应商路由、多智能体编排；兼容 Claude Code、Codex。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 927 | **56** |
| 🔹 **[yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X)** | MCP 支持、图形界面与桌面端、多智能体编排；兼容 Codex。 ‡ | 🟢 较易 | — | — | 4.4k 🚀 +6/d | **55** |
| 🔹 **[erickochen/purple](https://github.com/erickochen/purple)** | MCP 支持、跨 Agent 支持、图形界面与桌面端；兼容 Claude Code、Cursor。 ‡ | 🟢 较易 | — | ✅ | 776 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | Agent 运行时、多智能体编排、MCP 支持。 ‡ | 🟢 开箱即用 | — | — | 440 | **53** |
| 🔹 **[cordum-io/cordum](https://github.com/cordum-io/cordum)** | MCP 支持、API 网关与中转、自动故障转移；兼容 Claude Code。 ‡ | 🔴 较重 | — | — | 509 | **52** |
| 🔹 **[solo-agent/solo](https://github.com/solo-agent/solo)** | 通过频道、讨论串、任务看板和频道团队协调多个智能体。 Server（:8080）- Go API、WebSocket hub、认证和 PostgreSQL 持久化。 | 🟡 需配置 | — | — | 603 | **45** |

**也能做这件事：** [cita-777/metapi](https://github.com/cita-777/metapi)、[sv3nbeast/agent-manager-lite](https://github.com/sv3nbeast/agent-manager-lite)

## 用量分析

*用量分析*

想知道 token 和钱到底花在哪里。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[makecindy/cindy](https://github.com/makecindy/cindy)** | Cindy 是一个开源、开箱即用的 AI Agent。连接你的多台电脑与手机，把熟悉的 Agent、模型和已有订阅放在一起，培养一个懂你工作方式的伙伴。 | 🔴 较重 | — | — | 9.9k 🚀 +98/d | **75** |
| ✅ **[langfuse/langfuse](https://github.com/langfuse/langfuse)** | 跨 Agent 支持、MCP 支持、Agent 运行时；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟢 较易 | — | ✅ | 37.4k (+29/d) | **75** |
| ✅ **[sandbox-quantum/switch](https://github.com/sandbox-quantum/switch)** | MCP 支持、跨 Agent 支持、Agent 运行时；兼容 Claude Code、Codex、OpenCode、Cursor。 ‡ | 🟢 开箱即用 | ✅ | ✅ | 4.4k 🚀 +56/d | **72** |
| ✅ **[QuantumNous/new-api](https://github.com/QuantumNous/new-api)** | API 网关与中转、图形界面与桌面端、模型与供应商路由。 ‡ | 🔴 较重 | — | — | 51.8k 🚀 +59/d | **70** |
| ✅ **[scenario-labs/skills](https://github.com/scenario-labs/skills)** | MCP 支持、跨 Agent 支持、模型与供应商路由；兼容 Claude Code、Codex、Cursor、Copilot。 ‡ | 🟡 需配置 | — | — | 3.7k 🚀 +40/d | **66** |
| 🔹 **[AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)** | 多智能体编排。 ‡ | 🟢 较易 | ✅ | — | 6k | **50** |
| 🔹 **[crshdn/mission-control](https://github.com/crshdn/mission-control)** | 多智能体编排、记忆与上下文、工作区隔离；兼容 Droid。 ‡ | 🔴 较重 | — | — | 2.2k | **50** |

**也能做这件事：** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)、[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)、[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)、[decolua/9router](https://github.com/decolua/9router)、[zai-org/ZCode](https://github.com/zai-org/ZCode)、[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)、[qixing-jk/all-api-hub](https://github.com/qixing-jk/all-api-hub)、[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)、[timwuhaotian/the-pair](https://github.com/timwuhaotian/the-pair)、[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)

---

## ⚔️ 挑战者

挑战者已经覆盖了在位者的部分场景，且增长很快，但**尚未达到淘汰门槛**——要么能力覆盖不全，要么热度差距仍然很大。这些组合最值得关注，下一次真正的淘汰最可能从它们之中产生。

| 在位者 | 挑战者 | 覆盖度 | 热度差距 |
| --- | --- | ---: | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 46% | star 数为 0.23 倍（35,243 vs 153,872） |

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
| **[AlickH/Copool](https://github.com/alickh/copool)** | **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 12.22x the stars (3,959 vs 324) | 🤖 自动（high） |
| **[Autoloops/greplica](https://github.com/autoloops/greplica)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 27.11x the stars (11,981 vs 442) | 🤖 自动（high） |
| **[Draculabo/AntigravityManager](https://github.com/draculabo/antigravitymanager)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 7.99x the stars (19,925 vs 2,493) | 🤖 自动（high） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 89.39x the stars (34,237 vs 383) | 🤖 自动（high） |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 38.06x the stars (35,243 vs 926) | 🤖 自动（high） |
| **[MemTensor/memmy-agent](https://github.com/memtensor/memmy-agent)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.41x the stars (11,981 vs 2,213) | 🤖 自动（high） |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/othmane-khadri/yalc-the-gtm-operating-system)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 151.65x the stars (49,588 vs 327) | 🤖 自动（high） |
| **[SethGammon/Citadel](https://github.com/sethgammon/citadel)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 36.85x the stars (34,237 vs 929) | 🤖 自动（high） |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 135.12x the stars (49,588 vs 367) | 🤖 自动（high） |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 220.36x the stars (107,314 vs 487) | 🤖 自动（high） |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 321.86x the stars (113,294 vs 352) | 🤖 自动（high） |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 99.72x the stars (30,316 vs 304) | 🤖 自动（high） |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/openagentscontrol)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 28.44x the stars (141,334 vs 4,970) | 🤖 自动（high） |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 13.26x the stars (49,588 vs 3,740) | 🤖 自动（high） |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 9.30x the stars (11,981 vs 1,288) | 🤖 自动（high） |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 5.29x the stars (11,981 vs 2,266) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 134.02x the stars (49,588 vs 370) | 🤖 自动（high） |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 28.80x the stars (11,981 vs 416) | 🤖 自动（high） |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 48.83x the stars (23,879 vs 489) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 155.94x the stars (49,588 vs 318) | 🤖 自动（high） |
| **[linxidnju/OpenTag](https://github.com/linxidnju/opentag)** | **[microsoft/TokenEconomizer](https://github.com/microsoft/tokeneconomizer)** | 11.67x the stars (5,833 vs 500) | 🤖 自动（high） |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 481.93x the stars (301,687 vs 626) | 🤖 自动（high） |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 23.16x the stars (34,237 vs 1,478) | 🤖 自动（high） |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 35.20x the stars (19,925 vs 566) | 🤖 自动（high） |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 48.42x the stars (301,687 vs 6,231) | 🤖 自动（high） |
| **[routatic/proxy](https://github.com/routatic/proxy)** | **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 156.85x the stars (153,872 vs 981) | 🤖 自动（high） |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 87.56x the stars (34,237 vs 391) | 🤖 自动（high） |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | **[ardeyouxipianyi/workbuddy2api-hub](https://github.com/ardeyouxipianyi/workbuddy2api-hub)** | 4.10x the stars (3,959 vs 965) | 🤖 自动（high） |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | **[garrytan/gstack](https://github.com/garrytan/gstack)** | 100.52x the stars (141,334 vs 1,406) | 🤖 自动（high） |
| **[yc-software/qm](https://github.com/yc-software/qm)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 7.22x the stars (113,294 vs 15,691) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[TencentCloud/Octop](https://github.com/tencentcloud/octop)** | 4.18x the stars (11,981 vs 2,864) | 🤖 自动（high） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)** | 2.94x the stars (1,704 vs 580) | 🤖 自动（high） |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/amap-ml/longhorizon-harness)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.21x the stars (30,316 vs 1,870) | 🤖 自动（medium） |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 90.65x the stars (49,588 vs 547) | 🤖 自动（medium） |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/seo-promt-master)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 32.62x the stars (18,918 vs 580) | 🤖 自动（medium） |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 4.47x the stars (23,879 vs 5,344) | 🤖 自动（medium） |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 3.32x the stars (1,414 vs 426) | 🤖 自动（medium） |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 6.98x the stars (49,588 vs 7,109) | 🤖 自动（medium） |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | **[xerj-org/xerj](https://github.com/xerj-org/xerj)** | 11.64x the stars (18,918 vs 1,625) | 🤖 自动（high） |
| **[CopilotKit/OpenBot](https://github.com/copilotkit/openbot)** | **[affaan-m/ECC](https://github.com/affaan-m/ecc)** | 26.85x the stars (301,687 vs 11,237) | 🤖 自动（high） |
| **[Deuz-AI/Deuz-SDK](https://github.com/deuz-ai/deuz-sdk)** | **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/claude-code-agent-monitor)** | 2.31x the stars (1,176 vs 508) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 2.57x the stars (1,414 vs 550) | 🤖 自动（medium） |
| **[google/artemis](https://github.com/google/artemis)** | **[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)** | 9.70x the stars (167,864 vs 17,306) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[huytieu/COG-second-brain](https://github.com/huytieu/cog-second-brain)** | 1.63x the stars (1,414 vs 865) | 🤖 自动（high） |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[thedivergentai/Game-Dev-Agentic-Skills](https://github.com/thedivergentai/game-dev-agentic-skills)** | 1.26x the stars (958 vs 759) | 🤖 自动（medium） |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 2.12x the stars (1,089 vs 513) | 🤖 自动（medium） |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | **[sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** | 1.78x the stars (49,588 vs 27,914) | 🤖 自动（medium） |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | desktop-ui | 27.9k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[google/artemis](https://github.com/google/artemis)** | mobile | 17.3k | 🔻 已被取代 | 已被 msitarzewski/agency-agents 取代：covers 100% of capabilities (6/6)。 |
| **[yc-software/qm](https://github.com/yc-software/qm)** | isolation-teams | 15.7k | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (10/10)。 |
| **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** | sharing | 11.2k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (9/9)。 |
| **[internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill)** | desktop-ui | 7.1k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | sharing | 6.2k | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (4/4)。 |
| **[callstack/agent-device](https://github.com/callstack/agent-device)** | mobile | 5.3k | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (9/9)。 |
| **[darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl)** | isolation-teams | 5k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | desktop-ui | 3.7k | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | sharing | 2.9k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager)** | billing | 2.5k | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (8/8)。 |
| **[future-agi/future-agi](https://github.com/future-agi/future-agi)** | sharing | 2.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (6/6)。 |
| **[MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent)** | sharing | 2.2k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (7/7)。 |
| **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | sharing | 1.9k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[oceanbase/powercontext](https://github.com/oceanbase/powercontext)** | memory-failover | 1.6k | 🔻 已被取代 | 已被 xerj-org/xerj 取代：covers 100% of capabilities (4/4)。 |
| **[michaelshimeles/rstack](https://github.com/michaelshimeles/rstack)** | isolation-teams | 1.5k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[wenfxl/openai-cpa](https://github.com/wenfxl/openai-cpa)** | isolation-teams | 1.4k | 🔻 已被取代 | 已被 garrytan/gstack 取代：covers 100% of capabilities (4/4)。 |
| **[fatwang2/search2ai](https://github.com/fatwang2/search2ai)** | sharing | 1.3k | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[routatic/proxy](https://github.com/routatic/proxy)** | providers-2 | 981 | 🔻 已被取代 | 已被 farion1231/cc-switch 取代：covers 100% of capabilities (5/5)。 |
| **[shx2005/codex-account-switcher](https://github.com/shx2005/codex-account-switcher)** | billing | 965 | 🔻 已被取代 | 已被 ardeyouxipianyi/workbuddy2api-hub 取代：covers 100% of capabilities (7/7)。 |
| **[SethGammon/Citadel](https://github.com/SethGammon/Citadel)** | isolation-teams | 929 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | billing | 926 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (4/4)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | memory-failover | 865 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | desktop-ui | 759 | 🔻 已被取代 | 已被 thedivergentai/Game-Dev-Agentic-Skills 取代：covers 100% of capabilities (5/5)。 |
| **[matrixorigin/memoria](https://github.com/matrixorigin/memoria)** | sharing | 626 | 🔻 已被取代 | 已被 affaan-m/ECC 取代：covers 100% of capabilities (6/6)。 |
| **[umutxyp/Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** | memory-failover | 580 | 🔻 已被取代 | 已被 xerj-org/xerj 取代：covers 100% of capabilities (4/4)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | isolation-teams | 580 | 🔻 已被取代 | 已被 pedrohcgs/claude-code-my-workflow 取代：covers 100% of capabilities (4/4)。 |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | billing | 566 | 🔻 已被取代 | 已被 jlcodes99/cockpit-tools 取代：covers 100% of capabilities (6/6)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-failover | 550 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem)** | desktop-ui | 547 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[managedcode/dotnet-skills](https://github.com/managedcode/dotnet-skills)** | desktop-ui | 513 | 🔻 已被取代 | 已被 data-goblin/power-bi-agentic-development 取代：covers 100% of capabilities (6/6)。 |
| **[Deuz-AI/Deuz-SDK](https://github.com/Deuz-AI/Deuz-SDK)** | mcp-security | 508 | 🔻 已被取代 | 已被 hoangsonww/Claude-Code-Agent-Monitor 取代：covers 100% of capabilities (4/4)。 |
| **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | mcp-security | 500 | 🔻 已被取代 | 已被 microsoft/TokenEconomizer 取代：covers 100% of capabilities (4/4)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | mobile | 489 | 🔻 已被取代 | 已被 getpaseo/paseo 取代：covers 100% of capabilities (5/5)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | sharing-model-routing | 487 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[Autoloops/greplica](https://github.com/Autoloops/greplica)** | sharing | 442 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (5/5)。 |
| **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | memory-failover | 426 | 🔻 已被取代 | 已被 huytieu/COG-second-brain 取代：covers 100% of capabilities (4/4)。 |
| **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | sharing | 416 | 🔻 已被取代 | 已被 TencentCloud/Octop 取代：covers 100% of capabilities (8/8)。 |
| **[savannahfeder/agentbox](https://github.com/savannahfeder/agentbox)** | isolation-teams | 391 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | isolation-teams | 383 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | desktop-ui | 370 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | desktop-ui | 367 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[automagik-si/genie](https://github.com/automagik-si/genie)** | isolation-teams | 352 | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (7/7)。 |
| **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | desktop-ui | 327 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (5/5)。 |
| **[AlickH/Copool](https://github.com/AlickH/Copool)** | billing | 324 | 🔻 已被取代 | 已被 ardeyouxipianyi/workbuddy2api-hub 取代：covers 100% of capabilities (4/4)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | desktop-ui | 318 | 🔻 已被取代 | 已被 sickn33/agentic-awesome-skills 取代：covers 100% of capabilities (4/4)。 |
| **[cluster1900/apexo-code](https://github.com/cluster1900/apexo-code)** | sharing | 304 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-11-12 12:45 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
