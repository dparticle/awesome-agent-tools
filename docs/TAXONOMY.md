<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Category taxonomy

**Categories in this list are discovered, not declared.** No file lists them. Every run clusters the indexed tools by how prominently their READMEs document each capability, and the resulting groups become the sections you see. Adding a tool can therefore change the taxonomy, and a section that stops being distinct disappears on its own.

## How a category is derived

1. Each capability is weighted by **inverse document frequency**, so a capability that nearly every tool claims contributes almost nothing.
2. Each tool becomes a normalised vector of `idf × log(1 + mentions)` — what it *emphasises*, not merely what it mentions.
3. Tools are clustered by cosine similarity using agglomerative average linkage, stopping at a similarity threshold.
4. A cluster is named from the capabilities where it has the highest **lift** against the corpus, so the title reflects what makes the group distinct.

Capabilities claimed by more than 60% of tools are excluded from clustering: they describe the whole ecosystem, and including them collapsed every tool into a single section during development.

## Categories

| Category | Tools | Also in | Cohesion | Defining capabilities |
| --- | ---: | ---: | ---: | --- |
| **Skills** | 38 | 67 | 0.74 | Skills & plugins, Multi-agent orchestration, Agent runtime, Notifications |
| **Isolation & Parallelism** | 37 | 8 | 0.69 | Parallel execution, Voice input, Workspace isolation, Multi-agent orchestration |
| **Security & Self-hosting** | 30 | 57 | 0.72 | Automatic failover, MCP support, Multi-agent orchestration, GUI / desktop app |
| **Analytics** | 24 | 13 | 0.77 | Session persistence, Memory & context, Usage analytics, MCP support |
| **Self-hosting & Security** | 23 | 17 | 0.70 | Self-hostable, Security & isolation, API gateway / proxy, Billing & metering |
| **Teams** | 18 | 5 | 0.75 | Team collaboration, Billing & metering, Mobile access, Voice input |
| **Accounts** | 16 | 0 | 0.77 | Multi-account switching, Quota & usage management, Quota sharing / splitting, Billing & metering |
| **Mobile** | 16 | 0 | 0.76 | Mobile access, Remote control, Voice input, Notifications |
| **Model Routing** | 16 | 17 | 0.73 | Model / provider routing, API gateway / proxy, Quota sharing / splitting, Agent runtime |
| **Quota** | 13 | 1 | 0.77 | Quota & usage management, Multi-provider aggregation, Quota sharing / splitting, API gateway / proxy |
| **Agent Runtime & Desktop UI** | 12 | 75 | 0.86 | GUI / desktop app, Agent runtime, Multi-agent orchestration, Skills & plugins |
| **Remote Control** | 9 | 9 | 0.78 | Remote control, Team collaboration, Self-hostable, Workspace isolation |
| **Providers** | 8 | 2 | 0.78 | Multi-provider aggregation, Team collaboration, Usage analytics, Security & isolation |
| **Analytics** | 5 | 4 | 0.83 | Usage analytics, Quota & usage management, Team collaboration, Mobile access |
| **Billing** | 5 | 20 | 0.87 | Billing & metering, MCP support, Usage analytics, Session persistence |

*Cohesion* is the mean cosine similarity of a category's members to its centroid: higher means a tighter, more coherent group.

## Multi-category membership

175 of 270 tools belong to more than one category. A tool is cross-listed when it shares at least two of another category's defining capabilities, capped at three categories so the signal stays meaningful. It is described in full only under its primary category — the one whose centroid it is closest to.

## Capabilities

| Capability | Problem it addresses | Patterns | Tools |
| --- | --- | ---: | ---: |
| **Multi-account switching** / 多账号切换 | One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand. | 24 | 28 |
| **Quota & usage management** / 额度与用量管理 | You cannot see how much quota is left, so you get blocked mid-task. | 16 | 26 |
| **Automatic failover** / 自动故障转移 | When one account or provider dies, work should continue on the next one instead of stopping. | 13 | 52 |
| **Remote control** / 远程控制 | Your agent runs on a desktop, but you want to drive it from somewhere else. | 11 | 31 |
| **Mobile access** / 手机端访问 | You are away from the desk and want to keep the agent working from a phone. | 14 | 31 |
| **Multi-agent orchestration** / 多智能体编排 | One agent is not enough; several must be planned, dispatched and supervised together. | 16 | 134 |
| **Parallel execution** / 并行执行 | Tasks run one at a time and you wait; parallelism cuts wall-clock time. | 10 | 53 |
| **Workspace isolation** / 工作区隔离 | Parallel agents overwrite each other's files unless each gets its own checkout. | 12 | 69 |
| **Model / provider routing** / 模型与供应商路由 | You want one agent to run on a different model or provider than its default. | 13 | 99 |
| **Multi-provider aggregation** / 多供应商聚合 | Many subscriptions and API keys are scattered; you want one endpoint for all of them. | 11 | 13 |
| **API gateway / proxy** / API 网关与中转 | Client tools speak one protocol but the upstream speaks another, or you must hide keys. | 14 | 51 |
| **Quota sharing / splitting** / 配额共享与分发 | A subscription's capacity is larger than one person needs; share it safely with others. | 14 | 4 |
| **Billing & metering** / 计费与计量 | When several people share capacity, usage must be measured and charged accurately. | 17 | 41 |
| **Usage analytics** / 用量分析 | You want to know where tokens and money actually went. | 11 | 39 |
| **Session persistence** / 会话持久化 | Closing the laptop or losing connection kills a long-running agent session. | 12 | 47 |
| **Memory & context** / 记忆与上下文 | Every new session starts from zero and forgets your project's conventions. | 12 | 94 |
| **Skills & plugins** / 技能与插件 | The base agent lacks your workflows; you need to extend it. | 11 | 132 |
| **Agent runtime** / Agent 运行时 | This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent. | 12 | 124 |
| **MCP support** / MCP 支持 | The agent needs access to external tools and data through a standard protocol. | 3 | 153 |
| **Security & isolation** / 安全与隔离 | Agents run arbitrary code and hold credentials; blast radius must be contained. | 16 | 56 |
| **Self-hostable** / 可自托管 | You do not want your code or keys flowing through someone else's server. | 14 | 64 |
| **Team collaboration** / 团队协作 | Several people must share one agent setup, with roles and boundaries. | 13 | 33 |
| **GUI / desktop app** / 图形界面与桌面端 | Terminal-only tools shut out people who do not live in a shell. | 12 | 112 |
| **Notifications** / 通知提醒 | A long task finishes or blocks, and nobody notices. | 13 | 61 |
| **Voice input** / 语音输入 | Typing long prompts on a phone is painful. | 6 | 12 |
| **Cross-agent support** / 跨 Agent 支持 | You use more than one agent and refuse to keep separate setups for each. | 22 | 189 |
