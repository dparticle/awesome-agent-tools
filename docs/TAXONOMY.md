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
| **Analytics** | 50 | 9 | 0.65 | Voice input, Session persistence, Memory & context, Team collaboration |
| **Desktop UI** | 44 | 61 | 0.75 | Skills & plugins, Multi-agent orchestration, Agent runtime, GUI / desktop app |
| **Memory & MCP** | 37 | 59 | 0.66 | GUI / desktop app, MCP support, API gateway / proxy, Security & isolation |
| **Teams & Isolation** | 28 | 10 | 0.73 | Parallel execution, Workspace isolation, Remote control, Usage analytics |
| **Mobile & Remote Control** | 21 | 3 | 0.73 | Mobile access, Quota sharing / splitting, Remote control, Notifications |
| **Sharing** | 18 | 6 | 0.73 | Quota & usage management, Multi-account switching, Billing & metering, API gateway / proxy |
| **Analytics** | 16 | 18 | 0.80 | Self-hostable, Billing & metering, Security & isolation, Notifications |
| **Billing** | 12 | 7 | 0.80 | Billing & metering, Multi-provider aggregation, API gateway / proxy, Multi-account switching |
| **Notifications** | 12 | 8 | 0.80 | Notifications, Quota & usage management, Parallel execution, MCP support |
| **Failover** | 11 | 57 | 0.84 | Automatic failover, MCP support, GUI / desktop app, Memory & context |
| **Model Routing** | 10 | 44 | 0.91 | Model / provider routing, Agent runtime, GUI / desktop app, Skills & plugins |
| **Providers** | 10 | 0 | 0.77 | Multi-provider aggregation, Team collaboration, Usage analytics, Security & isolation |
| **Analytics** | 8 | 16 | 0.81 | Usage analytics, Security & isolation, Self-hostable, Billing & metering |

*Cohesion* is the mean cosine similarity of a category's members to its centroid: higher means a tighter, more coherent group.

## Multi-category membership

175 of 277 tools belong to more than one category. A tool is cross-listed when it shares at least two of another category's defining capabilities, capped at three categories so the signal stays meaningful. It is described in full only under its primary category — the one whose centroid it is closest to.

## Capabilities

| Capability | Problem it addresses | Patterns | Tools |
| --- | --- | ---: | ---: |
| **Multi-account switching** / 多账号切换 | One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand. | 24 | 29 |
| **Quota & usage management** / 额度与用量管理 | You cannot see how much quota is left, so you get blocked mid-task. | 16 | 27 |
| **Automatic failover** / 自动故障转移 | When one account or provider dies, work should continue on the next one instead of stopping. | 13 | 61 |
| **Remote control** / 远程控制 | Your agent runs on a desktop, but you want to drive it from somewhere else. | 11 | 36 |
| **Mobile access** / 手机端访问 | You are away from the desk and want to keep the agent working from a phone. | 14 | 36 |
| **Multi-agent orchestration** / 多智能体编排 | One agent is not enough; several must be planned, dispatched and supervised together. | 16 | 123 |
| **Parallel execution** / 并行执行 | Tasks run one at a time and you wait; parallelism cuts wall-clock time. | 10 | 45 |
| **Workspace isolation** / 工作区隔离 | Parallel agents overwrite each other's files unless each gets its own checkout. | 12 | 66 |
| **Model / provider routing** / 模型与供应商路由 | You want one agent to run on a different model or provider than its default. | 13 | 99 |
| **Multi-provider aggregation** / 多供应商聚合 | Many subscriptions and API keys are scattered; you want one endpoint for all of them. | 11 | 16 |
| **API gateway / proxy** / API 网关与中转 | Client tools speak one protocol but the upstream speaks another, or you must hide keys. | 14 | 51 |
| **Quota sharing / splitting** / 配额共享与分发 | A subscription's capacity is larger than one person needs; share it safely with others. | 14 | 3 |
| **Billing & metering** / 计费与计量 | When several people share capacity, usage must be measured and charged accurately. | 17 | 41 |
| **Usage analytics** / 用量分析 | You want to know where tokens and money actually went. | 11 | 34 |
| **Session persistence** / 会话持久化 | Closing the laptop or losing connection kills a long-running agent session. | 12 | 43 |
| **Memory & context** / 记忆与上下文 | Every new session starts from zero and forgets your project's conventions. | 12 | 90 |
| **Skills & plugins** / 技能与插件 | The base agent lacks your workflows; you need to extend it. | 11 | 132 |
| **Agent runtime** / Agent 运行时 | This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent. | 12 | 124 |
| **MCP support** / MCP 支持 | The agent needs access to external tools and data through a standard protocol. | 3 | 163 |
| **Security & isolation** / 安全与隔离 | Agents run arbitrary code and hold credentials; blast radius must be contained. | 16 | 59 |
| **Self-hostable** / 可自托管 | You do not want your code or keys flowing through someone else's server. | 14 | 68 |
| **Team collaboration** / 团队协作 | Several people must share one agent setup, with roles and boundaries. | 13 | 33 |
| **GUI / desktop app** / 图形界面与桌面端 | Terminal-only tools shut out people who do not live in a shell. | 12 | 123 |
| **Notifications** / 通知提醒 | A long task finishes or blocks, and nobody notices. | 13 | 73 |
| **Voice input** / 语音输入 | Typing long prompts on a phone is painful. | 6 | 16 |
| **Cross-agent support** / 跨 Agent 支持 | You use more than one agent and refuse to keep separate setups for each. | 22 | 196 |
