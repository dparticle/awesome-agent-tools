<!-- GENERATED FILE — do not edit by hand. Run `python scripts/agentindex.py build` (or wait for the daily workflow). -->

# The elimination engine

> There is always a dark horse. A curated list that only ever grows becomes a museum — eventually it recommends tools nobody should install.

When a newer tool **strictly covers** an incumbent, the incumbent is retired into the [graveyard](../README.md#-the-graveyard) with the evidence that retired it.

## The rules

An edge `challenger → incumbent` is recorded only when **all** of the following hold. Each rule exists because dropping it produced a false elimination in testing.

| # | Rule | Threshold | Why |
| ---: | --- | --- | --- |
| 1 | Capability coverage | ≥ 100% | The challenger must do everything the incumbent does. 100% means *everything*. |
| 2 | Popularity | ≥ 1.15× the stars | A strictly better tool nobody uses is not yet a replacement. |
| 3 | Momentum | ≥ 1.00× the star velocity | Stops a stagnant tool from killing a rising one. |
| 4 | Setup cost | no more than +12 friction | A better tool that is much harder to install does not actually replace the old one. |
| 5 | Documentation | challenger within 10 doc points | Prevents replacing a well-documented tool with an undocumented one. |
| 6 | Dominance margin | ≥ 0.55 | Blends the margins so marginal calls stay out of the graveyard. |

A tool is never eliminated by a tool that is itself retired, and a chain (C ⊃ B ⊃ A) keeps only the **strongest direct edge** per incumbent, so the report reads as a decision rather than a transitive closure.

## Lifecycle states

| State | Meaning |
| --- | --- |
| 🟢 Active | Listed normally. |
| 🟡 Dormant | No commits for a long time, but not formally replaced. |
| 🔻 Superseded | Strictly covered by a healthier tool; moved to the graveyard. |
| ⛔ Deprecated | Marked so by a human in `config/overrides.json`. |
| 📦 Archived | The owner archived the repository. |

## Supersede vs. challenger

A pair can be reported without anything being retired. That distinction matters, because the obvious headline example in this space does not actually qualify:

**`magpie` is a challenger to `cc-switch`, not its replacement.** They compete for the same job, and magpie additionally routes other models through the same agent loop. But magpie covers roughly 62% of cc-switch's capability set, and at the time of writing has about 4% of its stars. Recording that as a retirement would mean this list asserting something its own methodology contradicts — so the pair appears under **Challengers**, cc-switch stays listed, and the engine keeps watching. If magpie closes the capability gap and the traction gap, the automatic rules will retire cc-switch on their own.

A curated entry in `config/overrides.json` is therefore a **nomination, not a verdict**: the claim is re-checked against the same coverage rule the automatic engine uses, and recorded as a `supersede` (retire) or a `challenger` (watch) accordingly.

## Recorded eliminations

### 0xK3vin/MegaMemory → Gentleman-Programming/engram

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 9.92x the stars (7,070 vs 713)
- 10.35x the star velocity (30.3/day vs 2.9/day)
- no harder to set up (22 vs 28 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "session-persistence"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "session-persistence"
  ],
  "incumbent_health": 43,
  "challenger_health": 67,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 22
}
```

### AGI-is-going-to-arrive/Memory-Palace → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 93.30x the stars (29,204 vs 313)
- 95.87x the star velocity (130.4/day vs 1.4/day)
- no harder to set up (32 vs 47 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "self-hosted",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 44,
  "challenger_health": 88,
  "incumbent_setup_score": 47,
  "challenger_setup_score": 32
}
```

### AlickH/Copool → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 57.16x the stars (18,691 vs 327)
- 45.38x the star velocity (70.8/day vs 1.6/day)
- no harder to set up (26 vs 41 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "billing-metering",
    "gui-desktop",
    "multi-account-switching",
    "quota-management"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "model-routing",
    "multi-account-switching",
    "multi-agent-orchestration",
    "parallel-execution",
    "provider-aggregation",
    "quota-management",
    "security-isolation",
    "usage-analytics"
  ],
  "incumbent_health": 45,
  "challenger_health": 77,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 26
}
```

### AndrewDryga/emisar → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 13.92x the stars (4,691 vs 337)
- 9.96x the star velocity (23.8/day vs 2.4/day)
- no harder to set up (24 vs 25 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "security-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "quota-management",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 52,
  "challenger_health": 65,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 24
}
```

### Arvincreator/project-golem → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 45.70x the stars (29,204 vs 639)
- 50.93x the star velocity (130.4/day vs 2.6/day)
- no harder to set up (32 vs 45 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 39,
  "challenger_health": 88,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### Ibrahim-3d/orchestrator-supaconductor → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 6.36x the stars (2,417 vs 380)
- 21.05x the star velocity (34.5/day vs 1.6/day)
- no harder to set up (34 vs 72 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "multi-agent-orchestration",
    "parallel-execution",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 48,
  "challenger_health": 66,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 34
}
```

### LerianStudio/ring → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 11.14x the stars (2,417 vs 217)
- 53.95x the star velocity (34.5/day vs 0.6/day)
- no harder to set up (34 vs 40 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 48,
  "challenger_health": 66,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 34
}
```

### MagicCube/agentara → pacifio/atlas

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 17.99x the stars (9,263 vs 515)
- 26.66x the star velocity (63.5/day vs 2.4/day)
- no harder to set up (21 vs 84 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "session-persistence"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "multi-agent-orchestration",
    "session-persistence",
    "usage-analytics"
  ],
  "incumbent_health": 38,
  "challenger_health": 72,
  "incumbent_setup_score": 84,
  "challenger_setup_score": 21
}
```

### Othmane-Khadri/YALC-the-GTM-operating-system → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 866.27x the stars (274,608 vs 317)
- 911.41x the star velocity (1048.1/day vs 1.1/day)
- no harder to set up (57 vs 64 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "self-hosted",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 46,
  "challenger_health": 89,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### Pimzino/spec-workflow-mcp → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 63.85x the stars (274,608 vs 4,301)
- 103.77x the star velocity (1048.1/day vs 10.1/day)
- no harder to set up (57 vs 64 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "security-isolation",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 47,
  "challenger_health": 89,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### Ryze-AI-Adgent/open-seo-mcp-skills → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 61.75x the stars (274,608 vs 4,447)
- 8.96x the star velocity (1048.1/day vs 117.0/day)
- no harder to set up (57 vs 57 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 74,
  "challenger_health": 89,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 57
}
```

### SethGammon/Citadel → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 36.17x the stars (33,351 vs 922)
- 17.06x the star velocity (78.3/day vs 4.6/day)
- no harder to set up (2 vs 25 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 55,
  "challenger_health": 81,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### YoanWai/agent-manager → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 58.10x the stars (33,351 vs 574)
- 11.46x the star velocity (78.3/day vs 6.8/day)
- no harder to set up (2 vs 13 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "notifications",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 56,
  "challenger_health": 81,
  "incumbent_setup_score": 13,
  "challenger_setup_score": 2
}
```

### automagik-dev/genie → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 96.67x the stars (33,351 vs 345)
- 97.86x the star velocity (78.3/day vs 0.8/day)
- no harder to set up (2 vs 4 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 55,
  "challenger_health": 81,
  "incumbent_setup_score": 4,
  "challenger_setup_score": 2
}
```

### breferrari/obsidian-mind → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 5.92x the stars (29,204 vs 4,930)
- 5.82x the star velocity (130.4/day vs 22.4/day)
- no harder to set up (32 vs 52 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 63,
  "challenger_health": 88,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 32
}
```

### darrenhinde/OpenAgentsControl → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 20.09x the stars (98,271 vs 4,891)
- 38.35x the star velocity (448.7/day vs 11.7/day)
- no harder to set up (45 vs 50 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "memory-context",
    "multi-agent-orchestration",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 65,
  "challenger_health": 89,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 45
}
```

### delorenj/mcp-server-trello → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 65.63x the stars (29,204 vs 445)
- 188.96x the star velocity (130.4/day vs 0.7/day)
- no harder to set up (32 vs 34 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "notifications",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 52,
  "challenger_health": 88,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 32
}
```

### glebis/claude-skills → XiaomiMiMo/MiMo-Code

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 34.97x the stars (13,603 vs 389)
- 102.06x the star velocity (114.3/day vs 1.1/day)
- no harder to set up (30 vs 30 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "multi-agent-orchestration",
    "security-isolation",
    "skills-plugins",
    "voice-input"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 50,
  "challenger_health": 84,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 30
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 23.62x the stars (7,628 vs 323)
- 58.21x the star velocity (83.8/day vs 1.4/day)
- no harder to set up (26 vs 75 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 45,
  "challenger_health": 80,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 26
}
```

### huytieu/COG-second-brain → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 6.05x the stars (7,628 vs 1,261)
- 23.75x the star velocity (83.8/day vs 3.5/day)
- no harder to set up (26 vs 31 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 58,
  "challenger_health": 80,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 26
}
```

### isxlan0/Codex_AccountSwitch → yetone/magpie

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 22.49x the stars (5,667 vs 252)
- 389.22x the star velocity (404.8/day vs 1.0/day)
- no harder to set up (18 vs 46 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "gui-desktop",
    "multi-account-switching",
    "quota-management",
    "usage-analytics"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-account-switching",
    "quota-management",
    "usage-analytics"
  ],
  "incumbent_health": 41,
  "challenger_health": 84,
  "incumbent_setup_score": 46,
  "challenger_setup_score": 18
}
```

### jdrhyne/agent-skills → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 1144.20x the stars (274,608 vs 240)
- 1127.01x the star velocity (1048.1/day vs 0.9/day)
- no harder to set up (57 vs 69 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "self-hosted",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 41,
  "challenger_health": 89,
  "incumbent_setup_score": 69,
  "challenger_setup_score": 57
}
```

### josstei/maestro-orchestrate → spinabot/brigade

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 24.26x the stars (11,280 vs 465)
- 52.86x the star velocity (102.5/day vs 1.9/day)
- no harder to set up (39 vs 51 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "session-persistence"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-account-switching",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 50,
  "challenger_health": 80,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 39
}
```

### kerim0x1/bettercode → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 574.96x the stars (158,113 vs 275)
- 25.62x the star velocity (440.4/day vs 17.2/day)
- no harder to set up (1 vs 24 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mobile-access",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "multi-account-switching",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "team-collaboration",
    "voice-input"
  ],
  "incumbent_health": 57,
  "challenger_health": 98,
  "incumbent_setup_score": 24,
  "challenger_setup_score": 1
}
```

### lanes-sh/app → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 122.16x the stars (33,351 vs 273)
- 56.73x the star velocity (78.3/day vs 1.4/day)
- no harder to set up (2 vs 12 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 50,
  "challenger_health": 81,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 2
}
```

### linxidnju/OpenTag → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 58.18x the stars (29,204 vs 502)
- 26.50x the star velocity (130.4/day vs 4.9/day)
- no harder to set up (32 vs 45 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "security-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 88,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### mcpware/cross-code-organizer → genspark-ai/genoffice

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 23.13x the stars (8,836 vs 382)
- 68.75x the star velocity (129.9/day vs 1.9/day)
- no harder to set up (20 vs 20 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "skills-plugins",
    "usage-analytics"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "usage-analytics"
  ],
  "incumbent_health": 55,
  "challenger_health": 85,
  "incumbent_setup_score": 20,
  "challenger_setup_score": 20
}
```

### michaelshimeles/skills → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 26.49x the stars (33,351 vs 1,259)
- 13.43x the star velocity (78.3/day vs 5.8/day)
- no harder to set up (2 vs 28 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "multi-agent-orchestration",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 81,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 2
}
```

### nekocode/agent-worktree → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 8.66x the stars (2,417 vs 279)
- 30.29x the star velocity (34.5/day vs 1.1/day)
- no harder to set up (34 vs 40 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "gui-desktop",
    "multi-agent-orchestration",
    "parallel-execution",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 47,
  "challenger_health": 66,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 34
}
```

### nwiizo/tfmcp → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 78.29x the stars (29,204 vs 373)
- 200.58x the star velocity (130.4/day vs 0.7/day)
- no harder to set up (32 vs 52 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "security-isolation",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 52,
  "challenger_health": 88,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 32
}
```

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 143.56x the stars (140,685 vs 980)
- 57.94x the star velocity (327.9/day vs 5.7/day)
- no harder to set up (23 vs 33 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "model-routing",
    "provider-aggregation"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-account-switching",
    "parallel-execution",
    "provider-aggregation",
    "session-persistence",
    "skills-plugins",
    "usage-analytics"
  ],
  "incumbent_health": 56,
  "challenger_health": 93,
  "incumbent_setup_score": 33,
  "challenger_setup_score": 23
}
```

### rsmdt/the-startup → EverMind-AI/Raven

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 9.66x the stars (5,257 vs 544)
- 29.32x the star velocity (37.8/day vs 1.3/day)
- no harder to set up (13 vs 25 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "self-hosted",
    "skills-plugins"
  ],
  "incumbent_health": 48,
  "challenger_health": 70,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 13
}
```

### ruvnet/metaharness → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 399.14x the stars (274,608 vs 688)
- 175.27x the star velocity (1048.1/day vs 6.0/day)
- no harder to set up (57 vs 58 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 89,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 57
}
```

### jtydhr88/comfyui-custom-node-skills → FrancyJGLisboa/agent-skills-platform

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 8.17x the stars (2,403 vs 294)
- 4.99x the star velocity (6.8/day vs 1.4/day)
- no harder to set up (15 vs 50 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "incumbent_health": 41,
  "challenger_health": 56,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 15
}
```

### appautomaton/latex-arxiv-SKILL → trailhq/Graft

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (4/4)
- 21.14x the stars (9,660 vs 457)
- 124.22x the star velocity (100.6/day vs 0.8/day)
- slightly heavier setup (+1 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "model-routing",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "skills-plugins"
  ],
  "incumbent_health": 48,
  "challenger_health": 79,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 37
}
```

### tigerless-labs/agent-memory → paperclipai/paperclip

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (4/4)
- 41.31x the stars (98,271 vs 2,379)
- 6.60x the star velocity (448.7/day vs 68.0/day)
- slightly heavier setup (+2 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 69,
  "challenger_health": 89,
  "incumbent_setup_score": 43,
  "challenger_setup_score": 45
}
```

### AMAP-ML/LongHorizon-Harness → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (8/8)
- 17.48x the stars (29,204 vs 1,671)
- 4.99x the star velocity (130.4/day vs 26.1/day)
- slightly heavier setup (+2 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "security-isolation",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 59,
  "challenger_health": 88,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 32
}
```

### hkqr/my-free-code → trailhq/Graft

- **Source:** automatic (medium confidence)
- **Dominance:** 0.985

Reasons:

- covers 100% of capabilities (4/4)
- 15.51x the stars (9,660 vs 623)
- 6.46x the star velocity (100.6/day vs 15.6/day)
- slightly heavier setup (+3 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "model-routing"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "skills-plugins"
  ],
  "incumbent_health": 52,
  "challenger_health": 79,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 37
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 0.984

Reasons:

- covers 100% of capabilities (7/7)
- 2.80x the stars (7,628 vs 2,725)
- 7.39x the star velocity (83.8/day vs 11.3/day)
- no harder to set up (26 vs 49 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "memory-context",
    "model-routing",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 57,
  "challenger_health": 80,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 26
}
```

### Lling0000/Vibe_coding_guide → maxritter/pilot-shell

- **Source:** automatic (high confidence)
- **Dominance:** 0.971

Reasons:

- covers 100% of capabilities (6/6)
- 9.02x the stars (2,083 vs 231)
- 3.95x the star velocity (5.9/day vs 1.5/day)
- no harder to set up (12 vs 30 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 41,
  "challenger_health": 62,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 12
}
```

### internet-court/internet-court-skill → alibaba/open-code-review

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (4/4)
- 6.90x the stars (44,160 vs 6,400)
- 5.49x the star velocity (311.0/day vs 56.6/day)
- slightly heavier setup (+6 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "incumbent_health": 63,
  "challenger_health": 89,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 37
}
```

### matrixorigin/memoria → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (6/6)
- 452.40x the stars (274,608 vs 607)
- 363.93x the star velocity (1048.1/day vs 2.9/day)
- slightly heavier setup (+6 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "security-isolation",
    "self-hosted",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 89,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 57
}
```

### YYH211/Claude-meta-skill → thedivergentai/GD-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.961

Reasons:

- covers 100% of capabilities (4/4)
- 2.85x the stars (804 vs 282)
- 4.02x the star velocity (3.3/day vs 0.8/day)
- no harder to set up (21 vs 58 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins"
  ],
  "incumbent_health": 42,
  "challenger_health": 56,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 21
}
```

### oracle/mcp → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (5/5)
- 10.33x the stars (4,691 vs 454)
- 22.89x the star velocity (23.8/day vs 1.0/day)
- slightly heavier setup (+8 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "security-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "quota-management",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 54,
  "challenger_health": 65,
  "incumbent_setup_score": 16,
  "challenger_setup_score": 24
}
```

### hkcanan/katmer-code → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (6/6)
- 579.34x the stars (274,608 vs 474)
- 440.39x the star velocity (1048.1/day vs 2.4/day)
- slightly heavier setup (+9 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 49,
  "challenger_health": 89,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 57
}
```

### MemTensor/memmy-agent → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 0.951

Reasons:

- covers 100% of capabilities (7/7)
- 3.69x the stars (7,628 vs 2,066)
- 3.37x the star velocity (83.8/day vs 24.9/day)
- no harder to set up (26 vs 42 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 60,
  "challenger_health": 80,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 26
}
```

### oleksiijko/pmb → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.950

Reasons:

- covers 100% of capabilities (6/6)
- 103.93x the stars (29,204 vs 281)
- 62.68x the star velocity (130.4/day vs 2.1/day)
- slightly heavier setup (+10 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 54,
  "challenger_health": 88,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 32
}
```

### AI-QL/tuui → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.945

Reasons:

- covers 100% of capabilities (4/4)
- 25.28x the stars (29,204 vs 1,155)
- 62.68x the star velocity (130.4/day vs 2.1/day)
- slightly heavier setup (+11 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 88,
  "incumbent_setup_score": 21,
  "challenger_setup_score": 32
}
```

### zhaoxuya520/reverse-skill → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.938

Reasons:

- covers 100% of capabilities (4/4)
- 6.87x the stars (274,608 vs 39,997)
- 3.85x the star velocity (1048.1/day vs 272.1/day)
- slightly heavier setup (+6 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 83,
  "challenger_health": 89,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 57
}
```

### tigerless-labs/cost-xray → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.914

Reasons:

- covers 100% of capabilities (5/5)
- 8.70x the stars (33,351 vs 3,833)
- 2.51x the star velocity (78.3/day vs 31.2/day)
- no harder to set up (2 vs 12 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "remote-control"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 65,
  "challenger_health": 81,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 2
}
```

### gotalab/cc-sdd → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.909

Reasons:

- covers 100% of capabilities (5/5)
- 2.06x the stars (7,628 vs 3,708)
- 10.10x the star velocity (83.8/day vs 8.3/day)
- slightly heavier setup (+1 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 59,
  "challenger_health": 80,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 26
}
```

### fuxicodex/Fuxi → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.908

Reasons:

- covers 100% of capabilities (5/5)
- 8.72x the stars (29,204 vs 3,351)
- 2.49x the star velocity (130.4/day vs 52.4/day)
- slightly heavier setup (+1 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "mcp-support",
    "model-routing",
    "security-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 67,
  "challenger_health": 88,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 32
}
```

### oomol-lab/open-connector → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 0.897

Reasons:

- covers 100% of capabilities (4/4)
- 4.90x the stars (29,204 vs 5,955)
- 2.19x the star velocity (130.4/day vs 59.5/day)
- no harder to set up (32 vs 72 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "mcp-support",
    "model-routing",
    "self-hosted",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 66,
  "challenger_health": 88,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 32
}
```

### giuseppe-trisciuoglio/developer-kit → thedivergentai/GD-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.885

Reasons:

- covers 100% of capabilities (5/5)
- 2.26x the stars (804 vs 355)
- 3.31x the star velocity (3.3/day vs 1.0/day)
- no harder to set up (21 vs 66 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "memory-context",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins"
  ],
  "incumbent_health": 46,
  "challenger_health": 56,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 21
}
```

### Waishnav/devspace → NanmiCoder/cc-haha

- **Source:** automatic (medium confidence)
- **Dominance:** 0.852

Reasons:

- covers 100% of capabilities (6/6)
- 2.86x the stars (14,892 vs 5,208)
- 1.73x the star velocity (78.4/day vs 45.3/day)
- slightly heavier setup (+1 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "remote-control",
    "self-hosted",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "auto-failover",
    "billing-metering",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 66,
  "challenger_health": 77,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 29
}
```

### superdesigndev/treg → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.851

Reasons:

- covers 100% of capabilities (8/8)
- 6.26x the stars (29,204 vs 4,667)
- 2.35x the star velocity (130.4/day vs 55.6/day)
- slightly heavier setup (+11 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "billing-metering",
    "mcp-support",
    "model-routing",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 72,
  "challenger_health": 88,
  "incumbent_setup_score": 21,
  "challenger_setup_score": 32
}
```

### WenyuChiou/ai-research-skills → thedivergentai/GD-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.843

Reasons:

- covers 100% of capabilities (5/5)
- 2.63x the stars (804 vs 306)
- 1.81x the star velocity (3.3/day vs 1.9/day)
- no harder to set up (21 vs 22 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins"
  ],
  "incumbent_health": 54,
  "challenger_health": 56,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 21
}
```

### MoonshotAI/kimi-code → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.841

Reasons:

- covers 100% of capabilities (7/7)
- 4.28x the stars (33,351 vs 7,789)
- 1.39x the star velocity (78.3/day vs 56.4/day)
- no harder to set up (2 vs 43 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 69,
  "challenger_health": 81,
  "incumbent_setup_score": 43,
  "challenger_setup_score": 2
}
```

### jacobaraujo7/remote_pi → yohey-w/multi-agent-shogun

- **Source:** automatic (medium confidence)
- **Dominance:** 0.823

Reasons:

- covers 100% of capabilities (5/5)
- 3.33x the stars (1,423 vs 427)
- 1.81x the star velocity (5.6/day vs 3.1/day)
- slightly heavier setup (+10 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "mobile-access",
    "multi-agent-orchestration",
    "remote-control",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 50,
  "challenger_health": 52,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 46
}
```

### yetone/cumora → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 0.795

Reasons:

- covers 100% of capabilities (9/9)
- 2.70x the stars (10,643 vs 3,939)
- 1.17x the star velocity (90.2/day vs 77.2/day)
- no harder to set up (25 vs 33 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "self-hosted",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "self-hosted",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 69,
  "challenger_health": 80,
  "incumbent_setup_score": 33,
  "challenger_setup_score": 25
}
```

### microsoft/power-platform-skills → yohey-w/multi-agent-shogun

- **Source:** automatic (medium confidence)
- **Dominance:** 0.686

Reasons:

- covers 100% of capabilities (5/5)
- 1.47x the stars (1,423 vs 969)
- 1.48x the star velocity (5.6/day vs 3.8/day)
- no harder to set up (46 vs 49 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "mobile-access",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 51,
  "challenger_health": 52,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 46
}
```

### abubakarsiddik31/claude-skills-collection → yohey-w/multi-agent-shogun

- **Source:** automatic (medium confidence)
- **Dominance:** 0.655

Reasons:

- covers 100% of capabilities (11/11)
- 1.31x the stars (1,423 vs 1,090)
- 1.81x the star velocity (5.6/day vs 3.1/day)
- no harder to set up (46 vs 46 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "multi-agent-orchestration",
    "notifications",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 52,
  "incumbent_setup_score": 46,
  "challenger_setup_score": 46
}
```

## The canonical example

**`magpie` vs `cc-switch` — reported as a challenger, not an elimination.** They solve the same problem, and magpie goes further by routing other models through the same agent loop. It is tempting to declare the older tool replaced. The rules refuse: magpie covers ~62% of cc-switch's capabilities and has ~4% of its stars. The pair is therefore surfaced under **Challengers**, which is where a reader deciding what to install actually benefits from seeing it — and nothing is retired on the strength of a claim the data does not support.

## Challenging a verdict

Add or edit an entry in [`config/overrides.json`](../config/overrides.json):

```json
{
  "supersede": [
    {
      "incumbent": "owner/old",
      "challenger": "owner/new",
      "note": "why the new tool strictly covers the old one"
    }
  ]
}
```

A manual edge always wins over an automatic one for the same incumbent, because a human has read both READMEs.
