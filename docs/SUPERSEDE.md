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
- 9.88x the stars (7,101 vs 719)
- 10.36x the star velocity (30.4/day vs 2.9/day)
- no harder to set up (28 vs 28 friction)

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
  "challenger_health": 65,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 28
}
```

### AGI-is-going-to-arrive/Memory-Palace → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 93.47x the stars (29,256 vs 313)
- 95.89x the star velocity (129.4/day vs 1.4/day)
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
- 57.35x the stars (18,752 vs 327)
- 45.48x the star velocity (70.5/day vs 1.6/day)
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
- 13.96x the stars (4,705 vs 337)
- 10.07x the star velocity (23.8/day vs 2.4/day)
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

### BennyKok/omg.dev → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 19.56x the stars (10,698 vs 547)
- 18.73x the star velocity (89.9/day vs 4.8/day)
- no harder to set up (25 vs 31 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mobile-access",
    "notifications",
    "remote-control",
    "self-hosted"
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
  "incumbent_health": 51,
  "challenger_health": 80,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 25
}
```

### Ibrahim-3d/orchestrator-supaconductor → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 6.37x the stars (2,428 vs 381)
- 20.85x the star velocity (34.2/day vs 1.6/day)
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
- 11.19x the stars (2,428 vs 217)
- 54.29x the star velocity (34.2/day vs 0.6/day)
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
  "incumbent_health": 50,
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
- 18.49x the stars (9,540 vs 516)
- 27.38x the star velocity (64.9/day vs 2.4/day)
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
  "challenger_health": 73,
  "incumbent_setup_score": 84,
  "challenger_setup_score": 21
}
```

### Othmane-Khadri/YALC-the-GTM-operating-system → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 869.55x the stars (275,647 vs 317)
- 915.89x the star velocity (1044.1/day vs 1.1/day)
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
- 64.07x the stars (275,647 vs 4,302)
- 103.69x the star velocity (1044.1/day vs 10.1/day)
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
- 59.77x the stars (275,647 vs 4,612)
- 9.06x the star velocity (1044.1/day vs 115.3/day)
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
- 36.18x the stars (33,397 vs 923)
- 17.15x the star velocity (78.0/day vs 4.5/day)
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
- 57.78x the stars (33,397 vs 578)
- 11.47x the star velocity (78.0/day vs 6.8/day)
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

### arinspunk/claude-talk-to-figma-mcp → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 50.07x the stars (33,397 vs 667)
- 64.49x the star velocity (78.0/day vs 1.2/day)
- no harder to set up (2 vs 16 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "parallel-execution"
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
  "incumbent_health": 48,
  "challenger_health": 81,
  "incumbent_setup_score": 16,
  "challenger_setup_score": 2
}
```

### automagik-dev/genie → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 96.52x the stars (33,397 vs 346)
- 97.54x the star velocity (78.0/day vs 0.8/day)
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
- 5.88x the stars (29,256 vs 4,975)
- 5.78x the star velocity (129.4/day vs 22.4/day)
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

### darrenhinde/OpenAgentsControl → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 5.59x the stars (27,355 vs 4,895)
- 8.42x the star velocity (98.0/day vs 11.7/day)
- no harder to set up (27 vs 50 friction)

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
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 65,
  "challenger_health": 85,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 27
}
```

### delorenj/mcp-server-trello → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 65.74x the stars (29,256 vs 445)
- 187.61x the star velocity (129.4/day vs 0.7/day)
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
- 34.83x the stars (13,617 vs 391)
- 101.31x the star velocity (113.5/day vs 1.1/day)
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
  "incumbent_health": 51,
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
- 24.64x the stars (8,156 vs 331)
- 60.72x the star velocity (88.7/day vs 1.5/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 26
}
```

### huytieu/COG-second-brain → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 6.44x the stars (8,156 vs 1,267)
- 25.11x the star velocity (88.7/day vs 3.5/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 26
}
```

### isxlan0/Codex_AccountSwitch → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 74.71x the stars (18,752 vs 251)
- 68.45x the star velocity (70.5/day vs 1.0/day)
- no harder to set up (26 vs 46 friction)

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
  "incumbent_health": 41,
  "challenger_health": 77,
  "incumbent_setup_score": 46,
  "challenger_setup_score": 26
}
```

### jacobaraujo7/remote_pi → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 46.60x the stars (20,224 vs 434)
- 18.12x the star velocity (56.2/day vs 3.1/day)
- no harder to set up (24 vs 36 friction)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "multi-agent-orchestration",
    "parallel-execution",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 50,
  "challenger_health": 74,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### jdrhyne/agent-skills → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 1148.53x the stars (275,647 vs 240)
- 1134.91x the star velocity (1044.1/day vs 0.9/day)
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

### jessepwj/CCteam-creator → garrytan/gstack

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 441.97x the stars (135,686 vs 307)
- 428.71x the star velocity (643.1/day vs 1.5/day)
- no harder to set up (57 vs 57 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "memory-context",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "session-persistence",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 39,
  "challenger_health": 90,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 57
}
```

### josstei/maestro-orchestrate → spinabot/brigade

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 24.30x the stars (11,300 vs 465)
- 53.02x the star velocity (101.8/day vs 1.9/day)
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
- 578.18x the stars (158,420 vs 274)
- 28.91x the star velocity (440.1/day vs 15.2/day)
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
- 122.33x the stars (33,397 vs 273)
- 57.38x the star velocity (78.0/day vs 1.4/day)
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
- 58.28x the stars (29,256 vs 502)
- 26.80x the star velocity (129.4/day vs 4.8/day)
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
  "incumbent_health": 42,
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
- 23.74x the stars (9,068 vs 382)
- 69.27x the star velocity (129.5/day vs 1.9/day)
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
- 26.19x the stars (33,397 vs 1,275)
- 13.27x the star velocity (78.0/day vs 5.9/day)
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

### microsoft/power-platform-skills → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 101.26x the stars (99,034 vs 978)
- 119.72x the star velocity (450.1/day vs 3.8/day)
- no harder to set up (45 vs 49 friction)

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
  "incumbent_health": 51,
  "challenger_health": 89,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 45
}
```

### nekocode/agent-worktree → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 8.70x the stars (2,428 vs 279)
- 30.27x the star velocity (34.2/day vs 1.1/day)
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
- 78.43x the stars (29,256 vs 373)
- 202.27x the star velocity (129.4/day vs 0.6/day)
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

### oomol-lab/open-connector → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 46.16x the stars (275,647 vs 5,972)
- 17.83x the star velocity (1044.1/day vs 58.5/day)
- no harder to set up (57 vs 72 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "mcp-support",
    "memory-context",
    "model-routing",
    "self-hosted"
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
  "incumbent_health": 66,
  "challenger_health": 89,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 57
}
```

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 144.38x the stars (141,777 vs 982)
- 58.77x the star velocity (329.7/day vs 5.6/day)
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
- 9.56x the stars (5,325 vs 557)
- 28.61x the star velocity (37.8/day vs 1.3/day)
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
- 397.19x the stars (275,647 vs 694)
- 176.07x the star velocity (1044.1/day vs 5.9/day)
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

### tigerless-labs/agent-memory → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 81.38x the stars (275,647 vs 3,387)
- 11.41x the star velocity (1044.1/day vs 91.5/day)
- no harder to set up (57 vs 81 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
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
  "incumbent_health": 70,
  "challenger_health": 89,
  "incumbent_setup_score": 81,
  "challenger_setup_score": 57
}
```

### wenfxl/openai-cpa → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 70.54x the stars (99,034 vs 1,404)
- 64.12x the star velocity (450.1/day vs 7.0/day)
- no harder to set up (45 vs 57 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins"
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
  "incumbent_health": 51,
  "challenger_health": 89,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 45
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 0.999

Reasons:

- covers 100% of capabilities (7/7)
- 2.99x the stars (8,156 vs 2,729)
- 7.86x the star velocity (88.7/day vs 11.3/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 26
}
```

### AMAP-ML/LongHorizon-Harness → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (8/8)
- 17.15x the stars (29,256 vs 1,706)
- 5.01x the star velocity (129.4/day vs 25.9/day)
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

### Lling0000/Vibe_coding_guide → maxritter/pilot-shell

- **Source:** automatic (high confidence)
- **Dominance:** 0.971

Reasons:

- covers 100% of capabilities (6/6)
- 9.03x the stars (2,085 vs 231)
- 3.96x the star velocity (5.9/day vs 1.5/day)
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
- 6.87x the stars (44,783 vs 6,517)
- 5.44x the star velocity (311.0/day vs 57.2/day)
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
- 451.88x the stars (275,647 vs 610)
- 365.08x the star velocity (1044.1/day vs 2.9/day)
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
- **Dominance:** 0.967

Reasons:

- covers 100% of capabilities (4/4)
- 2.90x the stars (817 vs 282)
- 4.10x the star velocity (3.4/day vs 0.8/day)
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
  "challenger_health": 57,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 21
}
```

### oracle/mcp → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (5/5)
- 10.30x the stars (4,705 vs 457)
- 22.85x the star velocity (23.8/day vs 1.0/day)
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

### MemTensor/memmy-agent → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (7/7)
- 3.92x the stars (8,156 vs 2,082)
- 3.62x the star velocity (88.7/day vs 24.5/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 26
}
```

### hkcanan/katmer-code → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (6/6)
- 581.53x the stars (275,647 vs 474)
- 440.56x the star velocity (1044.1/day vs 2.4/day)
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

### oleksiijko/pmb → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.950

Reasons:

- covers 100% of capabilities (6/6)
- 104.11x the stars (29,256 vs 281)
- 63.15x the star velocity (129.4/day vs 2.0/day)
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
- 25.33x the stars (29,256 vs 1,155)
- 62.24x the star velocity (129.4/day vs 2.1/day)
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
- **Dominance:** 0.937

Reasons:

- covers 100% of capabilities (4/4)
- 6.83x the stars (275,647 vs 40,367)
- 3.83x the star velocity (1044.1/day vs 272.8/day)
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

### gotalab/cc-sdd → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.924

Reasons:

- covers 100% of capabilities (5/5)
- 2.20x the stars (8,156 vs 3,708)
- 10.73x the star velocity (88.7/day vs 8.3/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 26
}
```

### fuxicodex/Fuxi → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.911

Reasons:

- covers 100% of capabilities (5/5)
- 8.73x the stars (29,256 vs 3,350)
- 2.55x the star velocity (129.4/day vs 50.8/day)
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

### giuseppe-trisciuoglio/developer-kit → thedivergentai/GD-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.888

Reasons:

- covers 100% of capabilities (5/5)
- 2.29x the stars (817 vs 356)
- 3.33x the star velocity (3.4/day vs 1.0/day)
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
  "challenger_health": 57,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 21
}
```

### Waishnav/devspace → NanmiCoder/cc-haha

- **Source:** automatic (medium confidence)
- **Dominance:** 0.854

Reasons:

- covers 100% of capabilities (6/6)
- 2.87x the stars (14,930 vs 5,208)
- 1.74x the star velocity (78.2/day vs 44.9/day)
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

### WenyuChiou/ai-research-skills → thedivergentai/GD-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.847

Reasons:

- covers 100% of capabilities (5/5)
- 2.66x the stars (817 vs 307)
- 1.82x the star velocity (3.4/day vs 1.9/day)
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
  "challenger_health": 57,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 21
}
```

### superdesigndev/treg → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.846

Reasons:

- covers 100% of capabilities (8/8)
- 5.97x the stars (29,256 vs 4,900)
- 2.25x the star velocity (129.4/day vs 57.6/day)
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
  "incumbent_health": 73,
  "challenger_health": 88,
  "incumbent_setup_score": 21,
  "challenger_setup_score": 32
}
```

### MoonshotAI/kimi-code → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.842

Reasons:

- covers 100% of capabilities (7/7)
- 4.28x the stars (33,397 vs 7,811)
- 1.40x the star velocity (78.0/day vs 55.8/day)
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

### tigerless-labs/cost-xray → getpaseo/paseo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.790

Reasons:

- covers 100% of capabilities (5/5)
- 4.31x the stars (20,224 vs 4,691)
- 1.50x the star velocity (56.2/day vs 37.5/day)
- slightly heavier setup (+12 friction, within tolerance)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "multi-agent-orchestration",
    "parallel-execution",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 65,
  "challenger_health": 74,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 24
}
```

### mindmuxai/brain.md → maxritter/pilot-shell

- **Source:** automatic (medium confidence)
- **Dominance:** 0.789

Reasons:

- covers 100% of capabilities (7/7)
- 3.68x the stars (2,085 vs 566)
- 1.17x the star velocity (5.9/day vs 5.0/day)
- slightly heavier setup (+6 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "skills-plugins",
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
  "incumbent_health": 55,
  "challenger_health": 62,
  "incumbent_setup_score": 6,
  "challenger_setup_score": 12
}
```

### op7418/guizang-social-card-skill → omnigent-ai/omnigent

- **Source:** automatic (medium confidence)
- **Dominance:** 0.693

Reasons:

- covers 100% of capabilities (4/4)
- 1.44x the stars (10,698 vs 7,425)
- 1.62x the star velocity (89.9/day vs 55.4/day)
- no harder to set up (25 vs 25 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mobile-access",
    "notifications"
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
  "incumbent_health": 62,
  "challenger_health": 80,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 25
}
```

### abubakarsiddik31/claude-skills-collection → yohey-w/multi-agent-shogun

- **Source:** automatic (medium confidence)
- **Dominance:** 0.653

Reasons:

- covers 100% of capabilities (11/11)
- 1.30x the stars (1,424 vs 1,092)
- 1.80x the star velocity (5.5/day vs 3.1/day)
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
