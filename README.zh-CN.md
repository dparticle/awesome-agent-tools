<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Awesome Agent Tools 中文版

> **用现有工具拼出一个「AGI」。** 单个 AI Agent 的局限太大：额度会用完、人不在电脑旁就停工、新会话记不住项目。本仓库持续搜集并验证那些专门补上这些短板的工具，同时记录哪些工具已经被更强的后来者取代。

**[English](README.md)** · [方法论](docs/METHODOLOGY.md) · [淘汰规则](docs/SUPERSEDE.md) · [能力分类法](docs/TAXONOMY.md) · [机器可读索引](data/index.json)

**108 个工具**，分 **12 个分类** · **38 个已淘汰**（见[淘汰区](#-淘汰区)） · 最近更新 **2026-10-07 14:00 UTC**

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

## 远程与移动端控制

*人不在电脑旁，也能让 Agent 继续干活。*

Agent 跑在工作站上，而你在地铁上、会议里或沙发上。没有这类工具，你一离开工位，会话就停了。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 远程控制、手机端访问、多智能体编排 | 🟡 需配置 | — | — | 98.3k (+451/d) | **89** |
| ✅ **[slopus/happy](https://github.com/slopus/happy)** | 远程控制、手机端访问、多智能体编排 | 🟢 较易 | ✅ | ✅ | 24k (+54/d) | **71** |
| 🔹 **[ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop)** | 自动故障转移、远程控制、手机端访问 | 🟢 开箱即用 | ✅ | — | 777 🚀 +14/d | **58** |

## 额度与多账号运维

*不因某个账号额度耗尽而停工。*

订阅额度有限，且重置时间不由你控制。这类工具把账号池化、监控剩余额度并自动切换，让长任务不会卡在限额上。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[yetone/magpie](https://github.com/yetone/magpie)** | 多账号切换、额度与用量管理、自动故障转移 | 🟢 开箱即用 | — | — | 5.7k 🚀 +436/d | **84** |
| ✅ **[jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools)** | 多账号切换、额度与用量管理、自动故障转移 | 🟢 较易 | — | — | 18.7k (+71/d) | **77** |
| 🔹 **[Loongphy/codex-auth](https://github.com/Loongphy/codex-auth)** | 多账号切换、图形界面与桌面端 | 🟢 较易 | — | ✅ | 2.8k (+12/d) | **58** |
| 🔹 **[uwuclxdy/clauth](https://github.com/uwuclxdy/clauth)** | 多账号切换、额度与用量管理、并行执行 | 🟢 较易 | — | — | 271 | **52** |
| 🔹 **[Dicklesworthstone/coding_agent_account_manager](https://github.com/Dicklesworthstone/coding_agent_account_manager)** | 多账号切换、额度与用量管理、自动故障转移 | 🟡 需配置 | — | — | 208 | **51** |

## 多智能体编排

*单个 Agent 是工人，多个 Agent 才是团队。*

串行干活慢，单个上下文窗口也小。这类工具负责规划、派发、隔离与监管多个 Agent，通常每个 Agent 一个独立工作树。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[stablyai/orca](https://github.com/stablyai/orca)** | 多账号切换、额度与用量管理、远程控制 | 🟢 开箱即用 | ✅ | ✅ | 86.9k (+426/d) | **92** |
| ✅ **[getpaseo/paseo](https://github.com/getpaseo/paseo)** | 远程控制、手机端访问、多智能体编排 | 🟢 较易 | — | ✅ | 20k (+56/d) | **73** |
| 🔹 **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | 远程控制、多智能体编排、并行执行 | 🟡 需配置 | — | — | 2.9k (+12/d) | **54** |
| 🔹 **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 远程控制、手机端访问、多智能体编排 | 🟡 需配置 | — | — | 1.4k (+6/d) | **52** |
| 🔹 **[nekocode/agent-worktree](https://github.com/nekocode/agent-worktree)** | 自动故障转移、多智能体编排、并行执行 | 🟡 需配置 | ✅ | — | 279 | **47** |

## 模型与供应商路由

*让你惯用的 Agent 跑在别家的模型上。*

你喜欢的 Agent 循环并不必然绑定它默认的模型。这类工具让 Claude Code、Codex、Gemini CLI 改跑 DeepSeek、Kimi、Qwen 或本地模型——这也是某个供应商额度用尽后的续命方式。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[decolua/9router](https://github.com/decolua/9router)** | 多账号切换、额度与用量管理、远程控制 | 🔴 较重 | — | — | 30.4k (+111/d) | **81** |
| 🔹 **[routatic/proxy](https://github.com/routatic/proxy)** | 自动故障转移、模型与供应商路由、多供应商聚合 | 🟢 较易 | — | — | 980 (+6/d) | **56** |
| 🔹 **[Mirrowel/LLM-API-Key-Proxy](https://github.com/Mirrowel/LLM-API-Key-Proxy)** | 额度与用量管理、自动故障转移、模型与供应商路由 | 🔴 较重 | — | — | 556 | **49** |
| 🔹 **[hkcanan/katmer-code](https://github.com/hkcanan/katmer-code)** | 多智能体编排、并行执行、模型与供应商路由 | 🟡 需配置 | — | — | 474 | **49** |

## 订阅共享与网关

*把一份订阅变成可计量、可多租户的服务。*

一份订阅的容量常超过个人所需。这类工具把它安全地再分发出去：独立密钥、限流、额度核算与计费，而不是共享一个密码。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api)** | 多账号切换、自动故障转移、手机端访问 | 🟡 需配置 | — | — | 43.4k (+148/d) | **85** |
| 🔹 **[cita-777/metapi](https://github.com/cita-777/metapi)** | 多账号切换、额度与用量管理、自动故障转移 | 🔴 较重 | — | — | 3.3k (+15/d) | **54** |
| 🔹 **[wangyunjeff/sub2api-state-kit](https://github.com/wangyunjeff/sub2api-state-kit)** | 多账号切换、额度与用量管理、模型与供应商路由 | 🟡 需配置 | — | — | 214 🚀 +12/d | **48** |
| 👀 **[wenyi401/ikik-api](https://github.com/wenyi401/ikik-api)** | 多账号切换、模型与供应商路由、API 网关与中转 | 🔴 较重 | — | — | 241 | **42** |

## Agent 运行时与订阅

*你已在付费的那个 Agent 之外的选择。*

有时重点在于模型访问权：一份订阅解锁多个模型，或一个可自由 fork 的开源 Agent。这类是运行时本体，而非插件。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 手机端访问、模型与供应商路由、API 网关与中转 | 🟢 较易 | — | — | 99.8k (+616/d) | **95** |
| 🏆 **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | 模型与供应商路由、计费与计量、用量分析 | 🟢 较易 | — | — | 107.2k (+200/d) | **91** |
| 🏆 **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | 多智能体编排、Agent 运行时、图形界面与桌面端 | 🟢 开箱即用 | ✅ | ✅ | 212.1k (+405/d) | **90** |
| 🏆 **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | 技能与插件、Agent 运行时 | 🟢 开箱即用 | ✅ | — | 149.7k (+253/d) | **90** |
| 🏆 **[openai/codex](https://github.com/openai/codex)** | 多账号切换、自动故障转移、Agent 运行时 | 🟢 开箱即用 | — | ✅ | 128.1k (+236/d) | **89** |
| 🏆 **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 并行执行、模型与供应商路由、API 网关与中转 | 🟢 较易 | — | — | 8.8k 🚀 +130/d | **85** |
| 🏆 **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 远程控制、多智能体编排、并行执行 | 🟢 开箱即用 | — | — | 33.4k (+78/d) | **81** |
| 🔹 **[AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness)** | 自动故障转移、模型与供应商路由、API 网关与中转 | 🟢 较易 | — | — | 1.7k 🚀 +26/d | **59** |
| 🔹 **[jiweiyeah/Skills-Manager](https://github.com/jiweiyeah/Skills-Manager)** | 多供应商聚合、计费与计量、技能与插件 | 🟢 开箱即用 | ✅ | ✅ | 1k | **59** |
| 🔹 **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** | 多智能体编排、并行执行、工作区隔离 | 🟡 需配置 | — | — | 2.2k (+13/d) | **58** |
| 🔹 **[huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)** | 多智能体编排、模型与供应商路由、记忆与上下文 | 🟢 较易 | — | — | 1.3k | **58** |
| 🔹 **[grpcer/ownmem](https://github.com/grpcer/ownmem)** | 记忆与上下文、Agent 运行时、MCP 支持 | 🟢 较易 | ✅ | — | 423 🚀 +8/d | **58** |
| 🔹 **[kerim0x1/bettercode](https://github.com/kerim0x1/bettercode)** | 手机端访问、计费与计量、Agent 运行时 | 🟢 较易 | — | ✅ | 275 🚀 +17/d | **57** |
| 🔹 **[greenfield-inc/Pane](https://github.com/greenfield-inc/Pane)** | 多智能体编排、并行执行、工作区隔离 | 🟢 较易 | — | ✅ | 519 | **56** |
| 🔹 **[hex/claude-council](https://github.com/hex/claude-council)** | 自动故障转移、多智能体编排、并行执行 | 🟡 需配置 | — | — | 843 | **54** |
| 🔹 **[LnYo-Cly/ai4j](https://github.com/LnYo-Cly/ai4j)** | 多智能体编排、工作区隔离、多供应商聚合 | 🟢 开箱即用 | — | — | 434 | **54** |
| 🔹 **[marcusquinn/aidevops](https://github.com/marcusquinn/aidevops)** | 多账号切换、多智能体编排、工作区隔离 | 🟡 需配置 | — | — | 406 | **54** |
| 🔹 **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 多智能体编排、模型与供应商路由、技能与插件 | 🟡 需配置 | — | — | 688 🚀 +6/d | **53** |
| 🔹 **[superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli)** | 远程控制、手机端访问、多智能体编排 | 🟢 较易 | ✅ | — | 3.5k (+8/d) | **52** |
| 🔹 **[AVIDS2/memorix](https://github.com/AVIDS2/memorix)** | 多智能体编排、工作区隔离、模型与供应商路由 | 🔴 较重 | — | — | 835 | **52** |
| 🔹 **[elara-labs/code-context-engine](https://github.com/elara-labs/code-context-engine)** | 自动故障转移、用量分析、会话持久化 | 🟡 需配置 | — | — | 427 | **52** |
| 🔹 **[CatCatUncle/openworkbuddy](https://github.com/CatCatUncle/openworkbuddy)** | 额度与用量管理、远程控制、多智能体编排 | 🟡 需配置 | — | — | 275 🚀 +5/d | **50** |
| 🔹 **[linxidnju/OpenTag](https://github.com/linxidnju/OpenTag)** | Agent 运行时、MCP 支持、安全与隔离 | 🟡 需配置 | — | — | 502 🚀 +5/d | **47** |
| 🔹 **[Othmane-Khadri/YALC-the-GTM-operating-system](https://github.com/Othmane-Khadri/YALC-the-GTM-operating-system)** | 多智能体编排、技能与插件、MCP 支持 | 🔴 较重 | — | — | 317 | **46** |

## 技能、插件与提示词

*把你的工作流教给 Agent。*

基础 Agent 不了解你的技术栈、评审清单或发布流程。这类包把这些知识以可复用的技能、命令、子代理和钩子注入进去。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 多智能体编排、并行执行、工作区隔离 | 🟢 较易 | — | — | 27.3k (+99/d) | **85** |
| 🏆 **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** | 用量分析、技能与插件、通知提醒 | 🟢 较易 | — | — | 26.8k (+122/d) | **85** |
| 🏆 **[NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha)** | 额度与用量管理、自动故障转移、远程控制 | 🟢 较易 | — | ✅ | 14.9k (+79/d) | **78** |
| 🔹 **[davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)** | 多智能体编排、技能与插件、MCP 支持 | 🟡 需配置 | — | — | 3.6k (+8/d) | **58** |
| 🔹 **[data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development)** | 自动故障转移、多智能体编排、技能与插件 | 🟢 较易 | — | — | 1k | **57** |
| 🔹 **[FrancyJGLisboa/agent-skills-platform](https://github.com/FrancyJGLisboa/agent-skills-platform)** | 多智能体编排、记忆与上下文、技能与插件 | 🟢 开箱即用 | — | — | 2.4k (+7/d) | **56** |
| 🔹 **[numman-ali/n-skills](https://github.com/numman-ali/n-skills)** | 多智能体编排、技能与插件、Agent 运行时 | 🟢 开箱即用 | ✅ | — | 1.1k | **55** |
| 🔹 **[wwwzhouhui/skills_collection](https://github.com/wwwzhouhui/skills_collection)** | 额度与用量管理、自动故障转移、手机端访问 | 🟡 需配置 | — | — | 282 | **55** |
| 🔹 **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 手机端访问、多智能体编排、工作区隔离 | 🟡 需配置 | — | — | 1.1k | **53** |
| 🔹 **[claesbackman/AI-research-feedback](https://github.com/claesbackman/AI-research-feedback)** | 多智能体编排、技能与插件 | 🟢 开箱即用 | — | ✅ | 491 | **52** |
| 🔹 **[microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)** | 手机端访问、工作区隔离、技能与插件 | 🟡 需配置 | — | — | 969 | **51** |
| 🔹 **[binance/binance-skills-hub](https://github.com/binance/binance-skills-hub)** | 技能与插件 | 🟢 较易 | — | — | 1.1k | **50** |
| 🔹 **[glebis/claude-skills](https://github.com/glebis/claude-skills)** | 多智能体编排、记忆与上下文、技能与插件 | 🟢 较易 | — | — | 389 | **50** |
| 🔹 **[hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills)** | 多账号切换、多智能体编排、模型与供应商路由 | 🟢 较易 | — | — | 282 | **48** |
| 🔹 **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | 技能与插件、跨 Agent 支持 | 🟢 较易 | — | — | 2.6k (+10/d) | **47** |
| 👀 **[alirezarezvani/claude-code-tresor](https://github.com/alirezarezvani/claude-code-tresor)** | 多账号切换、多智能体编排、技能与插件 | 🔴 较重 | — | — | 777 | **43** |
| 👀 **[jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills)** | 多智能体编排、记忆与上下文、技能与插件 | 🔴 较重 | — | — | 240 | **41** |

## 记忆与上下文

*不必每次开会话都重新解释一遍项目。*

上下文会耗尽、会话会重置，Agent 因此忘掉已经定好的决策。这类工具把项目知识跨会话、跨 Agent 持久化下来。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🏆 **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 自动故障转移、多智能体编排、模型与供应商路由 | 🟢 较易 | — | — | 29.2k (+130/d) | **88** |
| ✅ **[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)** | 工作区隔离、模型与供应商路由、API 网关与中转 | 🔴 较重 | — | — | 8.9k (+65/d) | **70** |
| ✅ **[topoteretes/cognee](https://github.com/topoteretes/cognee)** | 模型与供应商路由、记忆与上下文、MCP 支持 | 🟡 需配置 | — | — | 31.5k (+27/d) | **69** |
| ✅ **[Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram)** | 会话持久化、记忆与上下文、Agent 运行时 | 🟢 较易 | ✅ | — | 7.1k (+30/d) | **67** |
| ✅ **[rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)** | 多智能体编排、并行执行、工作区隔离 | 🟢 开箱即用 | ✅ | — | 3.2k (+25/d) | **67** |
| ✅ **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 额度与用量管理、自动故障转移、多智能体编排 | 🟢 较易 | — | — | 4.7k (+24/d) | **66** |
| ✅ **[memvid/memvid](https://github.com/memvid/memvid)** | 模型与供应商路由、记忆与上下文 | 🟡 需配置 | — | — | 16.6k (+33/d) | **63** |
| 🔹 **[aoci-spec/aoci-code](https://github.com/aoci-spec/aoci-code)** | 自动故障转移、模型与供应商路由、API 网关与中转 | 🔴 较重 | — | — | 1.2k 🚀 +21/d | **58** |
| 🔹 **[felinics/Memoh](https://github.com/felinics/Memoh)** | 多智能体编排、工作区隔离、记忆与上下文 | 🟡 需配置 | — | — | 2.6k (+10/d) | **57** |
| 🔹 **[kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)** | 自动故障转移、远程控制、多智能体编排 | 🟡 需配置 | — | — | 773 | **56** |
| 🔹 **[tigicion/dao-code](https://github.com/tigicion/dao-code)** | 多账号切换、多智能体编排、并行执行 | 🟡 需配置 | — | — | 1.1k (+9/d) | **54** |
| 🔹 **[Lyellr88/marm-memory](https://github.com/Lyellr88/marm-memory)** | 自动故障转移、多智能体编排、模型与供应商路由 | 🟡 需配置 | — | — | 419 | **54** |
| 🔹 **[gary23w/nl-veil](https://github.com/gary23w/nl-veil)** | 多账号切换、自动故障转移、多智能体编排 | 🟢 较易 | — | — | 215 | **54** |
| 🔹 **[Dataojitori/nocturne_memory](https://github.com/Dataojitori/nocturne_memory)** | 远程控制、工作区隔离、会话持久化 | 🔴 较重 | — | — | 1.4k | **52** |
| 🔹 **[JuliusBrussee/cavemem](https://github.com/JuliusBrussee/cavemem)** | 自动故障转移、多智能体编排、记忆与上下文 | 🟢 开箱即用 | ✅ | — | 677 | **51** |
| 🔹 **[omega-memory/omega-memory](https://github.com/omega-memory/omega-memory)** | 多智能体编排、模型与供应商路由、会话持久化 | 🟡 需配置 | — | — | 219 | **51** |
| 🔹 **[LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem)** | 远程控制、模型与供应商路由、API 网关与中转 | 🟡 需配置 | — | — | 1.1k (+6/d) | **50** |
| 🔹 **[deepagent-ltd/deepagent-code](https://github.com/deepagent-ltd/deepagent-code)** | 多智能体编排、工作区隔离、模型与供应商路由 | 🟡 需配置 | — | — | 436 | **50** |
| 🔹 **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 多智能体编排、并行执行、工作区隔离 | 🟢 较易 | — | — | 1.1k (+9/d) | **49** |
| 🔹 **[chandra447/pi-hermes-memory](https://github.com/chandra447/pi-hermes-memory)** | 自动故障转移、模型与供应商路由、会话持久化 | 🔴 较重 | — | — | 473 | **49** |
| 🔹 **[Eshaan-Nair/ArcRift](https://github.com/Eshaan-Nair/ArcRift)** | 自动故障转移、并行执行、记忆与上下文 | 🟢 较易 | — | — | 247 | **46** |
| 🔹 **[harishkotra/agent-office](https://github.com/harishkotra/agent-office)** | 手机端访问、多智能体编排、工作区隔离 | 🔴 较重 | — | — | 323 | **45** |

## 可观测、用量分析与成本

*搞清楚 token 和钱都花到哪去了。*

Agent 在后台花的是真钱。这类工具记录会话、绘制用量曲线、按项目归集成本，并在额度耗尽前提示还剩多少。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🔹 **[hoangsonww/Claude-Code-Agent-Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)** | 自动故障转移、远程控制、手机端访问 | 🟡 需配置 | — | — | 1k | **55** |
| 🔹 **[Piebald-AI/splitrail](https://github.com/Piebald-AI/splitrail)** | 用量分析、Agent 运行时、MCP 支持 | 🟢 开箱即用 | ✅ | — | 222 | **50** |
| 👀 **[nateherkai/token-dashboard](https://github.com/nateherkai/token-dashboard)** | 自动故障转移、多智能体编排、并行执行 | 🟡 需配置 | — | — | 722 | **44** |

## 沙箱与安全

*让它执行代码，但别让它失控。*

Agent 用你的凭据执行任意命令。这类工具用容器、权限确认、密钥脱敏和审计日志把影响范围圈住。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🔹 **[Justin0504/Aegis](https://github.com/Justin0504/Aegis)** | 模型与供应商路由、计费与计量、用量分析 | 🟡 需配置 | — | — | 503 | **47** |

## 互通与 MCP

*给 Agent 一双手，以及一门通用语言。*

Agent 的能力上限取决于它能调用什么。MCP 服务与互通桥接让它接入浏览器、数据库、工单系统，以及别的 Agent。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| ✅ **[homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)** | 技能与插件、MCP 支持、通知提醒 | 🟢 较易 | — | — | 5k (+13/d) | **65** |
| ✅ **[getsentry/MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP)** | Agent 运行时、MCP 支持、跨 Agent 支持 | 🟢 开箱即用 | ✅ | — | 6.5k (+11/d) | **63** |
| 🔹 **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** | 额度与用量管理、并行执行、MCP 支持 | 🟡 需配置 | — | — | 9.2k (+13/d) | **59** |
| 🔹 **[microsoft/mcp](https://github.com/microsoft/mcp)** | 技能与插件、MCP 支持、可自托管 | 🟢 较易 | — | — | 3.7k (+7/d) | **59** |
| 🔹 **[opensumi/core](https://github.com/opensumi/core)** | MCP 支持、图形界面与桌面端 | 🟢 较易 | — | ✅ | 3.7k | **56** |
| 🔹 **[nanbingxyz/5ire](https://github.com/nanbingxyz/5ire)** | 用量分析、记忆与上下文、MCP 支持 | 🟢 较易 | — | ✅ | 5.4k (+5/d) | **55** |
| 🔹 **[oracle/mcp](https://github.com/oracle/mcp)** | 多智能体编排、模型与供应商路由、MCP 支持 | 🟢 开箱即用 | — | — | 454 | **54** |
| 🔹 **[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello)** | 自动故障转移、技能与插件、MCP 支持 | 🟢 较易 | — | — | 445 | **52** |
| 🔹 **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** | 模型与供应商路由、技能与插件、MCP 支持 | 🟡 需配置 | — | — | 373 | **52** |
| 🔹 **[aaronsb/obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin)** | 记忆与上下文、MCP 支持、跨 Agent 支持 | 🟡 需配置 | — | — | 463 | **51** |
| 🔹 **[ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo)** | 自动故障转移、工作区隔离、计费与计量 | 🟡 需配置 | — | — | 398 | **50** |
| 🔹 **[rekog-labs/MCP-Nest](https://github.com/rekog-labs/MCP-Nest)** | MCP 支持 | 🟡 需配置 | — | — | 713 | **49** |
| 🔹 **[JSONbored/awesome-claude](https://github.com/JSONbored/awesome-claude)** | 多账号切换、自动故障转移、远程控制 | 🟢 较易 | — | — | 299 | **49** |
| 🔹 **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | 多智能体编排、并行执行、Agent 运行时 | 🟢 开箱即用 | ✅ | — | 666 | **48** |
| 🔹 **[Pimzino/spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)** | 工作区隔离、API 网关与中转、MCP 支持 | 🔴 较重 | — | — | 4.3k (+10/d) | **47** |
| 🔹 **[AI-QL/tuui](https://github.com/AI-QL/tuui)** | 多智能体编排、MCP 支持、可自托管 | 🟢 较易 | — | ✅ | 1.2k | **47** |
| 🔹 **[metatool-ai/metamcp](https://github.com/metatool-ai/metamcp)** | 多智能体编排、并行执行、API 网关与中转 | 🔴 较重 | — | — | 2.7k | **46** |
| 🔹 **[intuit/quickbooks-online-mcp-server](https://github.com/intuit/quickbooks-online-mcp-server)** | 计费与计量、MCP 支持 | 🔴 较重 | — | — | 411 | **46** |
| 👀 **[r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp)** | MCP 支持 | 🟡 需配置 | — | — | 498 | **41** |

## 工作流与终端体验

*每次会话都能省一点力的小改进。*

状态栏、通知、会话浏览器、提示词管理与评审助手。单看都不起眼，加起来却决定了你是天天用还是躲着用。

| 工具 | 解决什么问题 | 上手难度 | 开箱即用 | 非程序员 | Star | 评分 |
| --- | --- | --- | :---: | :---: | --- | :---: |
| 🔹 **[asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck)** | 多账号切换、自动故障转移、远程控制 | 🟡 需配置 | — | — | 1k | **56** |

---

## 🪦 淘汰区

永远会有黑马出现。当新工具**完整覆盖**了旧工具的所有能力、热度不输、上手难度也不更高时，旧工具就会被移到这里，而不是悄悄留在推荐列表里。完整规则见 [docs/SUPERSEDE.md](docs/SUPERSEDE.md)。

### 已记录的取代关系

| 被淘汰 | 取代者 | 落败原因 | 来源 |
| --- | --- | --- | --- |
| **[0xK3vin/MegaMemory](https://github.com/0xk3vin/megamemory)** | **[Gentleman-Programming/engram](https://github.com/gentleman-programming/engram)** | 9.92x the stars (7,070 vs 713) | 🤖 自动（high） |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/agi-is-going-to-arrive/memory-palace)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 93.30x the stars (29,204 vs 313) | 🤖 自动（high） |
| **[Archive228/loopkit](https://github.com/archive228/loopkit)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 44.12x the stars (33,351 vs 756) | 🤖 自动（high） |
| **[JimLiu/baocut](https://github.com/jimliu/baocut)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 63.05x the stars (33,351 vs 529) | 🤖 自动（high） |
| **[Lampese/codex-switcher](https://github.com/lampese/codex-switcher)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 6.43x the stars (5,667 vs 881) | 🤖 自动（high） |
| **[LerianStudio/ring](https://github.com/lerianstudio/ring)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 125.89x the stars (27,318 vs 217) | 🤖 自动（high） |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/memtensor/memos-cloud-openclaw-plugin)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 79.57x the stars (29,204 vs 367) | 🤖 自动（high） |
| **[RealZST/HarnessKit](https://github.com/realzst/harnesskit)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 73.95x the stars (33,351 vs 451) | 🤖 自动（high） |
| **[anymorph-ai/Claudable](https://github.com/anymorph-ai/claudable)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.23x the stars (33,351 vs 4,052) | 🤖 自动（high） |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-skill)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 218.40x the stars (99,811 vs 457) | 🤖 自动（high） |
| **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 122.50x the stars (27,318 vs 223) | 🤖 自动（high） |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 76.95x the stars (27,318 vs 355) | 🤖 自动（high） |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 8.99x the stars (33,351 vs 3,708) | 🤖 自动（high） |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/codex_accountswitch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 22.49x the stars (5,667 vs 252) | 🤖 自动（high） |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 50.65x the stars (14,892 vs 294) | 🤖 自动（high） |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | **[microsoft/mcp](https://github.com/microsoft/mcp)** | 6.99x the stars (3,741 vs 535) | 🤖 自动（high） |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 21.11x the stars (33,351 vs 1,580) | 🤖 自动（high） |
| **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | **[stablyai/orca](https://github.com/stablyai/orca)** | 9.72x the stars (86,867 vs 8,939) | 🤖 自动（high） |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | **[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)** | 23.13x the stars (8,836 vs 382) | 🤖 自动（high） |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 47.80x the stars (29,204 vs 611) | 🤖 自动（high） |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | **[yetone/magpie](https://github.com/yetone/magpie)** | 10.61x the stars (5,667 vs 534) | 🤖 自动（high） |
| **[neiii/bridle](https://github.com/neiii/bridle)** | **[iOfficeAI/AionUi](https://github.com/iofficeai/aionui)** | 75.80x the stars (33,351 vs 440) | 🤖 自动（high） |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 38.58x the stars (29,204 vs 757) | 🤖 自动（high） |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 16.99x the stars (29,204 vs 1,719) | 🤖 自动（high） |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 61.61x the stars (29,204 vs 474) | 🤖 自动（high） |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 10.72x the stars (29,204 vs 2,725) | 🤖 自动（high） |
| **[LeoYeAI/talewell](https://github.com/leoyeai/talewell)** | **[eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)** | 8.58x the stars (4,691 vs 547) | 🤖 自动（medium） |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | **[OthmanAdi/planning-with-files](https://github.com/othmanadi/planning-with-files)** | 50.22x the stars (27,318 vs 544) | 🤖 自动（medium） |
| **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | **[NanmiCoder/cc-haha](https://github.com/nanmicoder/cc-haha)** | 16.83x the stars (14,892 vs 885) | 🤖 自动（medium） |
| **[YYH211/Claude-meta-skill](https://github.com/yyh211/claude-meta-skill)** | **[abubakarsiddik31/claude-skills-collection](https://github.com/abubakarsiddik31/claude-skills-collection)** | 3.87x the stars (1,090 vs 282) | 🤖 自动（high） |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/ccteam-creator)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 4.64x the stars (1,423 vs 307) | 🤖 自动（high） |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** | 230.14x the stars (98,271 vs 427) | 🤖 自动（medium） |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/ibrahim-3d/orchestrator-supaconductor)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.74x the stars (1,423 vs 380) | 🤖 自动（high） |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.06x the stars (1,423 vs 465) | 🤖 自动（high） |
| **[Socialpranker/deepdive](https://github.com/socialpranker/deepdive)** | **[yohey-w/multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun)** | 3.83x the stars (1,423 vs 372) | 🤖 自动（high） |
| **[IBM/mcp](https://github.com/ibm/mcp)** | **[arinspunk/claude-talk-to-figma-mcp](https://github.com/arinspunk/claude-talk-to-figma-mcp)** | 1.62x the stars (666 vs 410) | 🤖 自动（high） |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 1.35x the stars (99,811 vs 73,682) | 🤖 自动（medium） |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | **[yetone/magpie](https://github.com/yetone/magpie)** | magpie covers cc-switch's core job (multi-account / provider switching for Claude Code and Codex) and additionally routes other models through the same agent loop, so it strictly covers the older tool's feature set. | 👤 人工 |

### 已淘汰工具

| 工具 | 分类 | Star | 状态 | 说明 |
| --- | --- | --- | --- | --- |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | quota-account-ops | 140.7k | 🔻 已被取代 | 依然很流行且在持续维护，但 magpie 覆盖了同样的场景并额外支持跨模型路由。作为上一代参照保留在淘汰区。 |
| **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** | agent-runtimes | 73.7k | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (5/5)。 |
| **[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)** | orchestration | 8.9k | 🔻 已被取代 | 已被 stablyai/orca 取代：covers 100% of capabilities (3/3)。 |
| **[anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable)** | agent-runtimes | 4.1k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[gotalab/cc-sdd](https://github.com/gotalab/cc-sdd)** | agent-runtimes | 3.7k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[zilliztech/memsearch](https://github.com/zilliztech/memsearch)** | memory-context | 2.7k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (7/7)。 |
| **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** | memory-context | 1.7k | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (8/8)。 |
| **[kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net)** | agent-runtimes | 1.6k | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (3/3)。 |
| **[hashicorp/agent-skills](https://github.com/hashicorp/agent-skills)** | skills-plugins | 885 | 🔻 已被取代 | 已被 NanmiCoder/cc-haha 取代：covers 100% of capabilities (3/3)。 |
| **[Lampese/codex-switcher](https://github.com/Lampese/codex-switcher)** | quota-account-ops | 881 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (3/3)。 |
| **[okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory)** | memory-context | 757 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[Archive228/loopkit](https://github.com/Archive228/loopkit)** | agent-runtimes | 756 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (5/5)。 |
| **[0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory)** | memory-context | 713 | 🔻 已被取代 | 已被 Gentleman-Programming/engram 取代：covers 100% of capabilities (5/5)。 |
| **[mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon)** | memory-context | 611 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (6/6)。 |
| **[LeoYeAI/talewell](https://github.com/LeoYeAI/talewell)** | memory-context | 547 | 🔻 已被取代 | 已被 eugeniughelbur/obsidian-second-brain 取代：covers 100% of capabilities (5/5)。 |
| **[rsmdt/the-startup](https://github.com/rsmdt/the-startup)** | skills-plugins | 544 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (4/4)。 |
| **[kagisearch/kagimcp](https://github.com/kagisearch/kagimcp)** | interop-mcp | 535 | 🔻 已被取代 | 已被 microsoft/mcp 取代：covers 100% of capabilities (3/3)。 |
| **[ndycode/codex-multi-auth](https://github.com/ndycode/codex-multi-auth)** | quota-account-ops | 534 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (3/3)。 |
| **[JimLiu/baocut](https://github.com/JimLiu/baocut)** | agent-runtimes | 529 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (3/3)。 |
| **[vercel-labs/personal-agent-template](https://github.com/vercel-labs/personal-agent-template)** | memory-context | 474 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (5/5)。 |
| **[josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate)** | orchestration | 465 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (4/4)。 |
| **[appautomaton/latex-arxiv-SKILL](https://github.com/appautomaton/latex-arxiv-SKILL)** | agent-runtimes | 457 | 🔻 已被取代 | 已被 nexu-io/open-design 取代：covers 100% of capabilities (4/4)。 |
| **[RealZST/HarnessKit](https://github.com/RealZST/HarnessKit)** | agent-runtimes | 451 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (6/6)。 |
| **[neiii/bridle](https://github.com/neiii/bridle)** | agent-runtimes | 440 | 🔻 已被取代 | 已被 iOfficeAI/AionUi 取代：covers 100% of capabilities (3/3)。 |
| **[jacobaraujo7/remote_pi](https://github.com/jacobaraujo7/remote_pi)** | remote-control | 427 | 🔻 已被取代 | 已被 paperclipai/paperclip 取代：covers 100% of capabilities (5/5)。 |
| **[IBM/mcp](https://github.com/IBM/mcp)** | interop-mcp | 410 | 🔻 已被取代 | 已被 arinspunk/claude-talk-to-figma-mcp 取代：covers 100% of capabilities (3/3)。 |
| **[mcpware/cross-code-organizer](https://github.com/mcpware/cross-code-organizer)** | agent-runtimes | 382 | 🔻 已被取代 | 已被 genspark-ai/genoffice 取代：covers 100% of capabilities (6/6)。 |
| **[Ibrahim-3d/orchestrator-supaconductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor)** | orchestration | 380 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (5/5)。 |
| **[Socialpranker/deepdive](https://github.com/Socialpranker/deepdive)** | orchestration | 372 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (4/4)。 |
| **[MemTensor/MemOS-Cloud-OpenClaw-Plugin](https://github.com/MemTensor/MemOS-Cloud-OpenClaw-Plugin)** | memory-context | 367 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (4/4)。 |
| **[giuseppe-trisciuoglio/developer-kit](https://github.com/giuseppe-trisciuoglio/developer-kit)** | skills-plugins | 355 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |
| **[AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace)** | memory-context | 313 | 🔻 已被取代 | 已被 rohitg00/agentmemory 取代：covers 100% of capabilities (9/9)。 |
| **[jessepwj/CCteam-creator](https://github.com/jessepwj/CCteam-creator)** | orchestration | 307 | 🔻 已被取代 | 已被 yohey-w/multi-agent-shogun 取代：covers 100% of capabilities (6/6)。 |
| **[jtydhr88/comfyui-custom-node-skills](https://github.com/jtydhr88/comfyui-custom-node-skills)** | skills-plugins | 294 | 🔻 已被取代 | 已被 NanmiCoder/cc-haha 取代：covers 100% of capabilities (4/4)。 |
| **[YYH211/Claude-meta-skill](https://github.com/YYH211/Claude-meta-skill)** | skills-plugins | 282 | 🔻 已被取代 | 已被 abubakarsiddik31/claude-skills-collection 取代：covers 100% of capabilities (4/4)。 |
| **[isxlan0/Codex_AccountSwitch](https://github.com/isxlan0/Codex_AccountSwitch)** | quota-account-ops | 252 | 🔻 已被取代 | 已被 yetone/magpie 取代：covers 100% of capabilities (5/5)。 |
| **[franklee16/academic-research-skills](https://github.com/franklee16/academic-research-skills)** | skills-plugins | 223 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (3/3)。 |
| **[LerianStudio/ring](https://github.com/LerianStudio/ring)** | skills-plugins | 217 | 🔻 已被取代 | 已被 OthmanAdi/planning-with-files 取代：covers 100% of capabilities (5/5)。 |

---

## 参与贡献

详见 [CONTRIBUTING.md](CONTRIBUTING.md)：

1. **推荐工具** —— 在 [`config/seeds.json`](config/seeds.json) 里加上仓库和分类，下次抓取会用同样的门槛评估它。
2. **质疑结论** —— 如果某个工具被误淘汰、或某项能力识别错了，修改 [`config/overrides.json`](config/overrides.json)，或开 issue 并引用该工具页面上的证据句。

<sub>由 `agentindex` 于 2026-10-07 14:00 UTC 生成，所有数字均为自动重建，不手工编辑。</sub>
