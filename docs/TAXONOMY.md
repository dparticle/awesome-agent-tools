<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# Capability taxonomy

Categories group tools by **the problem they solve**. Capabilities are the finer grained, machine-detected features used for scoring and for the elimination engine. Both are matched against the README body, with the triggering sentence kept as evidence.

## Categories

### `remote-control` — Remote & Mobile Control / 远程与移动端控制

Your agent runs on a workstation, but you are on a train, in a meeting, or on the sofa. Without these tools the session simply stops when you walk away.

- Required capabilities: `any`
- Tools currently listed: **4**

Discovery queries:


### `quota-account-ops` — Quota & Multi-Account Ops / 额度与多账号运维

Subscription quotas are finite and reset on their own schedule. These tools pool accounts, watch the remaining quota, and switch automatically so a long task never dies at the limit.

- Required capabilities: `any`
- Tools currently listed: **9**

Discovery queries:


### `orchestration` — Multi-Agent Orchestration / 多智能体编排

Serial work is slow and a single context window is small. These tools plan, dispatch, isolate and supervise several agents at once — often one git worktree per agent.

- Required capabilities: `any`
- Tools currently listed: **10**

Discovery queries:


### `model-routing` — Model & Provider Routing / 模型与供应商路由

The agent loop you like is not tied to the model it ships with. These tools point Claude Code, Codex or Gemini CLI at DeepSeek, Kimi, Qwen or a local model — which is also how you keep working when one vendor's quota is gone.

- Required capabilities: `any`
- Tools currently listed: **4**

Discovery queries:


### `sharing-gateway` — Subscription Sharing & Gateways / 订阅共享与网关

A single subscription often has more capacity than one person uses. These tools redistribute it safely — with per-user keys, rate limits, quota accounting and billing — instead of sharing a password.

- Required capabilities: `any`
- Tools currently listed: **4**

Discovery queries:


### `agent-runtimes` — Agent Runtimes & Subscriptions / Agent 运行时与订阅

Sometimes the model access is the point: a flat subscription that unlocks many models, or an open-source agent you can fork. These are the runtimes themselves, not add-ons.

- Required capabilities: `any`
- Tools currently listed: **34**

Discovery queries:


### `skills-plugins` — Skills, Plugins & Prompts / 技能、插件与提示词

A base agent knows nothing about your stack, your review checklist or your deploy process. These packages inject that knowledge as reusable skills, commands, subagents and hooks.

- Required capabilities: `any`
- Tools currently listed: **24**

Discovery queries:


### `memory-context` — Memory & Context / 记忆与上下文

Context windows end and sessions reset, so the agent forgets decisions you already made. These tools persist project knowledge across sessions and agents.

- Required capabilities: `any`
- Tools currently listed: **31**

Discovery queries:


### `observability` — Observability, Analytics & Cost / 可观测、用量分析与成本

Agents spend real money in the background. These tools record sessions, chart usage, attribute cost per project, and surface how much quota is left before it runs out.

- Required capabilities: `any`
- Tools currently listed: **3**

Discovery queries:


### `security-sandbox` — Sandboxing & Security / 沙箱与安全

Agents execute arbitrary commands with your credentials. These tools contain the blast radius with containers, permission prompts, secret redaction and audit trails.

- Required capabilities: `any`
- Tools currently listed: **1**

Discovery queries:


### `interop-mcp` — Interop & MCP / 互通与 MCP

An agent is only as capable as the tools it can call. MCP servers and interop bridges connect it to browsers, databases, issue trackers and other agents.

- Required capabilities: `any`
- Tools currently listed: **21**

Discovery queries:


### `workflow-ux` — Workflow & Terminal UX / 工作流与终端体验

Statuslines, notifications, session browsers, prompt managers and review helpers. Individually minor; cumulatively they are the difference between using the agent daily and avoiding it.

- Required capabilities: `any`
- Tools currently listed: **1**

Discovery queries:


## Capabilities

| Capability | Problem it addresses | Patterns | Tools |
| --- | --- | ---: | ---: |
| **Multi-account switching** / 多账号切换 | One subscription's quota runs out; you need to rotate between several accounts without re-logging-in by hand. | 24 | 23 |
| **Quota & usage management** / 额度与用量管理 | You cannot see how much quota is left, so you get blocked mid-task. | 16 | 16 |
| **Automatic failover** / 自动故障转移 | When one account or provider dies, work should continue on the next one instead of stopping. | 13 | 34 |
| **Remote control** / 远程控制 | Your agent runs on a desktop, but you want to drive it from somewhere else. | 11 | 19 |
| **Mobile access** / 手机端访问 | You are away from the desk and want to keep the agent working from a phone. | 14 | 17 |
| **Multi-agent orchestration** / 多智能体编排 | One agent is not enough; several must be planned, dispatched and supervised together. | 16 | 79 |
| **Parallel execution** / 并行执行 | Tasks run one at a time and you wait; parallelism cuts wall-clock time. | 10 | 32 |
| **Workspace isolation** / 工作区隔离 | Parallel agents overwrite each other's files unless each gets its own checkout. | 12 | 37 |
| **Model / provider routing** / 模型与供应商路由 | You want one agent to run on a different model or provider than its default. | 13 | 59 |
| **Multi-provider aggregation** / 多供应商聚合 | Many subscriptions and API keys are scattered; you want one endpoint for all of them. | 11 | 9 |
| **API gateway / proxy** / API 网关与中转 | Client tools speak one protocol but the upstream speaks another, or you must hide keys. | 14 | 33 |
| **Quota sharing / splitting** / 配额共享与分发 | A subscription's capacity is larger than one person needs; share it safely with others. | 14 | 4 |
| **Billing & metering** / 计费与计量 | When several people share capacity, usage must be measured and charged accurately. | 17 | 30 |
| **Usage analytics** / 用量分析 | You want to know where tokens and money actually went. | 11 | 30 |
| **Session persistence** / 会话持久化 | Closing the laptop or losing connection kills a long-running agent session. | 12 | 29 |
| **Memory & context** / 记忆与上下文 | Every new session starts from zero and forgets your project's conventions. | 12 | 58 |
| **Skills & plugins** / 技能与插件 | The base agent lacks your workflows; you need to extend it. | 11 | 76 |
| **Agent runtime** / Agent 运行时 | This IS the agent — the thing you run and talk to — rather than an add-on bolted onto somebody else's agent. | 12 | 69 |
| **MCP support** / MCP 支持 | The agent needs access to external tools and data through a standard protocol. | 3 | 95 |
| **Security & isolation** / 安全与隔离 | Agents run arbitrary code and hold credentials; blast radius must be contained. | 16 | 35 |
| **Self-hostable** / 可自托管 | You do not want your code or keys flowing through someone else's server. | 14 | 33 |
| **Team collaboration** / 团队协作 | Several people must share one agent setup, with roles and boundaries. | 13 | 21 |
| **GUI / desktop app** / 图形界面与桌面端 | Terminal-only tools shut out people who do not live in a shell. | 12 | 66 |
| **Notifications** / 通知提醒 | A long task finishes or blocks, and nobody notices. | 13 | 34 |
| **Voice input** / 语音输入 | Typing long prompts on a phone is painful. | 6 | 7 |
| **Cross-agent support** / 跨 Agent 支持 | You use more than one agent and refuse to keep separate setups for each. | 22 | 109 |
