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

### AVIDS2/memorix → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (10/10)
- 330.89x the stars (295,153 vs 892)
- 227.88x the star velocity (774.8/day vs 3.4/day)
- no harder to set up (57 vs 73 friction)

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
    "multi-agent-orchestration",
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 52,
  "challenger_health": 89,
  "incumbent_setup_score": 73,
  "challenger_setup_score": 57
}
```

### AlickH/Copool → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 60.06x the stars (19,639 vs 327)
- 784.00x the star velocity (39.2/day vs 0.0/day)
- no harder to set up (32 vs 41 friction)

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
    "api-gateway",
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-account-switching",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "provider-aggregation",
    "quota-management",
    "security-isolation",
    "voice-input"
  ],
  "incumbent_health": 42,
  "challenger_health": 70,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### BennyKok/omg.dev → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 20.20x the stars (11,169 vs 553)
- 37.50x the star velocity (15.0/day vs 0.4/day)
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
    "auto-failover",
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
  "challenger_health": 67,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 25
}
```

### Dataojitori/nocturne_memory → spinabot/brigade

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 8.05x the stars (11,367 vs 1,412)
- 20.00x the star velocity (1.0/day vs 0.0/day)
- no harder to set up (39 vs 60 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "notifications",
    "remote-control",
    "session-persistence",
    "worktree-isolation"
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
  "incumbent_health": 49,
  "challenger_health": 60,
  "incumbent_setup_score": 60,
  "challenger_setup_score": 39
}
```

### Derpyu520/qq-bridge → milind-soni/OpenMausBot

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 3.18x the stars (10,994 vs 3,460)
- 17.68x the star velocity (1036.0/day vs 58.6/day)
- no harder to set up (28 vs 66 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "mcp-support",
    "model-routing",
    "security-isolation",
    "usage-analytics"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "usage-analytics",
    "voice-input"
  ],
  "incumbent_health": 63,
  "challenger_health": 87,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 28
}
```

### Draculabo/AntigravityManager → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 8.10x the stars (19,639 vs 2,426)
- 13.07x the star velocity (39.2/day vs 3.0/day)
- no harder to set up (32 vs 57 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "model-routing",
    "multi-account-switching",
    "notifications",
    "quota-management"
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
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "provider-aggregation",
    "quota-management",
    "security-isolation",
    "voice-input"
  ],
  "incumbent_health": 54,
  "challenger_health": 70,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### EliaAlberti/cpr-compress-preserve-resume → bytedance/deer-flow

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 162.29x the stars (84,876 vs 523)
- 336.00x the star velocity (67.2/day vs 0.2/day)
- no harder to set up (57 vs 63 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "memory-context",
    "session-persistence",
    "skills-plugins",
    "usage-analytics"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 43,
  "challenger_health": 79,
  "incumbent_setup_score": 63,
  "challenger_setup_score": 57
}
```

### Ibrahim-3d/orchestrator-supaconductor → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 89.22x the stars (33,991 vs 381)
- 143.00x the star velocity (28.6/day vs 0.2/day)
- no harder to set up (2 vs 72 friction)

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
  "incumbent_health": 44,
  "challenger_health": 71,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 2
}
```

### Lyellr88/marm-memory → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (12/12)
- 70.45x the stars (30,084 vs 427)
- 39.00x the star velocity (23.4/day vs 0.6/day)
- no harder to set up (32 vs 48 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "session-persistence"
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 54,
  "challenger_health": 70,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 32
}
```

### MagicCube/agentara → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 572.00x the stars (295,153 vs 516)
- 15496.00x the star velocity (774.8/day vs 0.0/day)
- no harder to set up (57 vs 84 friction)

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
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 38,
  "challenger_health": 89,
  "incumbent_setup_score": 84,
  "challenger_setup_score": 57
}
```

### MemTensor/memmy-agent → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 5.26x the stars (11,476 vs 2,180)
- 8.85x the star velocity (47.8/day vs 5.4/day)
- no harder to set up (32 vs 42 friction)

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
  "incumbent_health": 56,
  "challenger_health": 73,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### SethGammon/Citadel → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 36.59x the stars (33,991 vs 929)
- 71.50x the star velocity (28.6/day vs 0.4/day)
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
  "challenger_health": 71,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### Socialpranker/deepdive → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 132.50x the stars (49,024 vs 370)
- 421.17x the star velocity (168.5/day vs 0.4/day)
- no harder to set up (30 vs 51 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "model-routing",
    "multi-agent-orchestration",
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
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 52,
  "challenger_health": 92,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 30
}
```

### Waishnav/devspace → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 4.25x the stars (22,796 vs 5,370)
- 7.66x the star velocity (107.2/day vs 14.0/day)
- no harder to set up (24 vs 28 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "remote-control",
    "worktree-isolation"
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
  "incumbent_health": 61,
  "challenger_health": 84,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 24
}
```

### YYH211/Claude-meta-skill → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 172.62x the stars (49,024 vs 284)
- 3369.40x the star velocity (168.5/day vs 0.0/day)
- no harder to set up (30 vs 58 friction)

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
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 42,
  "challenger_health": 92,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 30
}
```

### YYHDBL/AgentCrew → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 118.44x the stars (30,084 vs 254)
- 468.00x the star velocity (23.4/day vs 0.0/day)
- no harder to set up (32 vs 39 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "notifications",
    "security-isolation",
    "session-persistence"
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 70,
  "incumbent_setup_score": 39,
  "challenger_setup_score": 32
}
```

### aoci-spec/aoci-code → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 160.67x the stars (295,153 vs 1,837)
- 57.82x the star velocity (774.8/day vs 13.4/day)
- no harder to set up (57 vs 64 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "session-persistence"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 57,
  "challenger_health": 89,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### automagik-dev/genie → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 98.52x the stars (33,991 vs 345)
- 572.00x the star velocity (28.6/day vs 0.0/day)
- no harder to set up (2 vs 50 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
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
  "challenger_health": 71,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 2
}
```

### chandra447/pi-hermes-memory → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 576.47x the stars (295,153 vs 512)
- 774.80x the star velocity (774.8/day vs 1.0/day)
- no harder to set up (57 vs 84 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "mcp-support",
    "memory-context",
    "model-routing",
    "session-persistence",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 47,
  "challenger_health": 89,
  "incumbent_setup_score": 84,
  "challenger_setup_score": 57
}
```

### cluster1900/apexo-code → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 99.29x the stars (30,084 vs 303)
- 12.25x the star velocity (23.4/day vs 1.9/day)
- no harder to set up (32 vs 48 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "gui-desktop",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "self-hosted",
    "session-persistence"
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 70,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 32
}
```

### darrenhinde/OpenAgentsControl → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 5.60x the stars (27,824 vs 4,967)
- 6.53x the star velocity (19.6/day vs 3.0/day)
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 65,
  "challenger_health": 69,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 27
}
```

### davepoon/buildwithclaude → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 13.23x the stars (49,024 vs 3,706)
- 44.33x the star velocity (168.5/day vs 3.8/day)
- no harder to set up (30 vs 50 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
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
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 57,
  "challenger_health": 92,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 30
}
```

### giuseppe-trisciuoglio/developer-kit → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 133.95x the stars (49,024 vs 366)
- 842.35x the star velocity (168.5/day vs 0.2/day)
- no harder to set up (30 vs 66 friction)

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
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 44,
  "challenger_health": 92,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 30
}
```

### grpcer/ownmem → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 390.63x the stars (166,016 vs 425)
- 2718.00x the star velocity (271.8/day vs 0.1/day)
- no harder to set up (1 vs 25 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
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
    "mobile-access",
    "multi-account-switching",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "team-collaboration",
    "voice-input"
  ],
  "incumbent_health": 55,
  "challenger_health": 96,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 1
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 29.05x the stars (11,476 vs 395)
- 12.58x the star velocity (47.8/day vs 3.8/day)
- no harder to set up (32 vs 75 friction)

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
  "incumbent_health": 43,
  "challenger_health": 73,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 32
}
```

### hex/claude-council → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 32.77x the stars (30,084 vs 918)
- 16.71x the star velocity (23.4/day vs 1.4/day)
- no harder to set up (32 vs 48 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "session-persistence"
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 51,
  "challenger_health": 70,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 32
}
```

### internet-court/internet-court-skill → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 6.95x the stars (49,024 vs 7,051)
- 40.11x the star velocity (168.5/day vs 4.2/day)
- no harder to set up (30 vs 31 friction)

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
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 57,
  "challenger_health": 92,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 30
}
```

### jacobaraujo7/remote_pi → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 23.51x the stars (11,169 vs 475)
- 18.75x the star velocity (15.0/day vs 0.8/day)
- no harder to set up (25 vs 36 friction)

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
    "api-gateway",
    "auto-failover",
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
  "incumbent_health": 50,
  "challenger_health": 67,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 25
}
```

### jtydhr88/comfyui-custom-node-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 156.13x the stars (49,024 vs 314)
- 168.47x the star velocity (168.5/day vs 1.0/day)
- no harder to set up (30 vs 50 friction)

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
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 44,
  "challenger_health": 92,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 30
}
```

### lanes-sh/app → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 122.71x the stars (33,991 vs 277)
- 143.00x the star velocity (28.6/day vs 0.2/day)
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
  "challenger_health": 71,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 2
}
```

### mcpware/cross-code-organizer → genspark-ai/genoffice

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 29.89x the stars (11,537 vs 386)
- 375.00x the star velocity (75.0/day vs 0.2/day)
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
    "memory-context",
    "model-routing",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "usage-analytics"
  ],
  "incumbent_health": 54,
  "challenger_health": 77,
  "incumbent_setup_score": 20,
  "challenger_setup_score": 20
}
```

### microsoft/power-platform-skills → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 99.82x the stars (110,104 vs 1,103)
- 56.11x the star velocity (392.8/day vs 7.0/day)
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
  "incumbent_health": 52,
  "challenger_health": 89,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 45
}
```

### mnemon-dev/mnemon → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 16.85x the stars (11,476 vs 681)
- 17.07x the star velocity (47.8/day vs 2.8/day)
- no harder to set up (32 vs 64 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
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
  "incumbent_health": 51,
  "challenger_health": 73,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 32
}
```

### ndycode/codex-multi-auth → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 35.01x the stars (19,639 vs 561)
- 39.20x the star velocity (39.2/day vs 1.0/day)
- no harder to set up (32 vs 41 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "multi-account-switching",
    "voice-input"
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
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "provider-aggregation",
    "quota-management",
    "security-isolation",
    "voice-input"
  ],
  "incumbent_health": 54,
  "challenger_health": 70,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### nekocode/agent-worktree → Gentleman-Programming/gentle-shell

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 5.42x the stars (1,522 vs 281)
- 224.00x the star velocity (11.2/day vs 0.0/day)
- no harder to set up (30 vs 40 friction)

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
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 49,
  "challenger_health": 60,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 30
}
```

### nwiizo/tfmcp → aipoch/open-science

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 14.61x the stars (5,420 vs 371)
- 11.61x the star velocity (7.2/day vs 0.6/day)
- no harder to set up (41 vs 52 friction)

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
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "remote-control",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 52,
  "challenger_health": 63,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 41
}
```

### oceanbase/powercontext → xerj-org/xerj

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 12.62x the stars (18,755 vs 1,486)
- 15.66x the star velocity (303.8/day vs 19.4/day)
- no harder to set up (33 vs 63 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context"
  ],
  "incumbent_health": 57,
  "challenger_health": 87,
  "incumbent_setup_score": 63,
  "challenger_setup_score": 33
}
```

### okf-memory/okf-agent-memory → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 13.52x the stars (11,476 vs 849)
- 39.83x the star velocity (47.8/day vs 1.2/day)
- no harder to set up (32 vs 45 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
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
  "incumbent_health": 54,
  "challenger_health": 73,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 153.92x the stars (151,146 vs 982)
- 6084.00x the star velocity (304.2/day vs 0.0/day)
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
  "incumbent_health": 55,
  "challenger_health": 93,
  "incumbent_setup_score": 33,
  "challenger_setup_score": 23
}
```

### savannahfeder/agentbox → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 67.05x the stars (22,796 vs 340)
- 11.04x the star velocity (107.2/day vs 9.7/day)
- no harder to set up (24 vs 30 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "parallel-execution",
    "worktree-isolation"
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
  "challenger_health": 84,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 24
}
```

### tickernelz/opencode-mem → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (11/11)
- 162.89x the stars (295,153 vs 1,812)
- 193.70x the star velocity (774.8/day vs 4.0/day)
- no harder to set up (57 vs 60 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "security-isolation",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 55,
  "challenger_health": 89,
  "incumbent_setup_score": 60,
  "challenger_setup_score": 57
}
```

### vercel-labs/personal-agent-template → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 611.08x the stars (295,153 vs 483)
- 968.50x the star velocity (774.8/day vs 0.8/day)
- no harder to set up (57 vs 78 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "notifications",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 46,
  "challenger_health": 89,
  "incumbent_setup_score": 78,
  "challenger_setup_score": 57
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 4.08x the stars (11,476 vs 2,814)
- 19.92x the star velocity (47.8/day vs 2.4/day)
- no harder to set up (32 vs 49 friction)

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
  "challenger_health": 73,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### huytieu/COG-second-brain → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (9/9)
- 8.62x the stars (11,476 vs 1,332)
- 26.56x the star velocity (47.8/day vs 1.8/day)
- slightly heavier setup (+1 friction, within tolerance)

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
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
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
  "incumbent_health": 56,
  "challenger_health": 73,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 32
}
```

### rsmdt/the-startup → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (4/4)
- 48.22x the stars (27,824 vs 577)
- 49.00x the star velocity (19.6/day vs 0.4/day)
- slightly heavier setup (+2 friction, within tolerance)

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
    "agent-runtime",
    "cross-agent-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 69,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### gotalab/cc-sdd → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (5/5)
- 13.08x the stars (49,024 vs 3,748)
- 421.17x the star velocity (168.5/day vs 0.4/day)
- slightly heavier setup (+5 friction, within tolerance)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 57,
  "challenger_health": 92,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 30
}
```

### linxidnju/OpenTag → kajisho5/ffmpeg-skill

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (4/4)
- 8.61x the stars (4,329 vs 503)
- 4800.00x the star velocity (240.0/day vs 0.0/day)
- slightly heavier setup (+5 friction, within tolerance)

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
    "multi-agent-orchestration",
    "security-isolation",
    "skills-plugins",
    "voice-input"
  ],
  "incumbent_health": 41,
  "challenger_health": 87,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 50
}
```

### michaelshimeles/rstack → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.965

Reasons:

- covers 100% of capabilities (5/5)
- 23.77x the stars (33,991 vs 1,430)
- 3.76x the star velocity (28.6/day vs 7.6/day)
- no harder to set up (2 vs 25 friction)

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
  "incumbent_health": 54,
  "challenger_health": 71,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### WenyuChiou/ai-research-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (5/5)
- 90.28x the stars (49,024 vs 543)
- 6.29x the star velocity (168.5/day vs 26.8/day)
- slightly heavier setup (+8 friction, within tolerance)

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
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 61,
  "challenger_health": 92,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 30
}
```

### LeoYeAI/talewell → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (5/5)
- 20.87x the stars (11,476 vs 550)
- 956.00x the star velocity (47.8/day vs 0.0/day)
- slightly heavier setup (+9 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
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
  "incumbent_health": 47,
  "challenger_health": 73,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 32
}
```

### Archive228/loopkit → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.945

Reasons:

- covers 100% of capabilities (5/5)
- 64.85x the stars (49,024 vs 756)
- 842.35x the star velocity (168.5/day vs 0.2/day)
- slightly heavier setup (+11 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
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
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 46,
  "challenger_health": 92,
  "incumbent_setup_score": 19,
  "challenger_setup_score": 30
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.944

Reasons:

- covers 100% of capabilities (4/4)
- 2.34x the stars (1,137 vs 485)
- 48.00x the star velocity (2.4/day vs 0.0/day)
- no harder to set up (30 vs 51 friction)

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
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 51,
  "challenger_health": 55,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 30
}
```

### garrytan/gstack → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 0.922

Reasons:

- covers 100% of capabilities (11/11)
- 2.13x the stars (295,153 vs 138,631)
- 6.15x the star velocity (774.8/day vs 126.0/day)
- no harder to set up (57 vs 65 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
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
    "session-persistence",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 88,
  "challenger_health": 89,
  "incumbent_setup_score": 65,
  "challenger_setup_score": 57
}
```

### Arvincreator/project-golem → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.880

Reasons:

- covers 100% of capabilities (4/4)
- 1.77x the stars (1,137 vs 641)
- 48.00x the star velocity (2.4/day vs 0.0/day)
- no harder to set up (30 vs 45 friction)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 38,
  "challenger_health": 55,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 30
}
```

### phuryn/pm-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.866

Reasons:

- covers 100% of capabilities (4/4)
- 1.78x the stars (49,024 vs 27,619)
- 5.62x the star velocity (168.5/day vs 30.0/day)
- slightly heavier setup (+3 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "notifications",
    "skills-plugins",
    "usage-analytics"
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
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 68,
  "challenger_health": 92,
  "incumbent_setup_score": 27,
  "challenger_setup_score": 30
}
```

### Gentleman-Programming/engram → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 0.852

Reasons:

- covers 100% of capabilities (5/5)
- 3.89x the stars (30,084 vs 7,739)
- 1.52x the star velocity (23.4/day vs 15.4/day)
- no harder to set up (32 vs 34 friction)

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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 62,
  "challenger_health": 70,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 32
}
```

### codecoradev/uteke → felinics/Memoh

- **Source:** automatic (high confidence)
- **Dominance:** 0.846

Reasons:

- covers 100% of capabilities (5/5)
- 9.86x the stars (2,772 vs 281)
- 1.45x the star velocity (2.6/day vs 1.8/day)
- no harder to set up (37 vs 37 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "notifications",
    "self-hosted",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 52,
  "challenger_health": 56,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 37
}
```

### yetone/cumora → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 0.800

Reasons:

- covers 100% of capabilities (9/9)
- 2.73x the stars (11,169 vs 4,096)
- 1.19x the star velocity (15.0/day vs 12.6/day)
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
    "auto-failover",
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
  "incumbent_health": 56,
  "challenger_health": 67,
  "incumbent_setup_score": 33,
  "challenger_setup_score": 25
}
```

### sahithvibudhi/vibe-tree → h0x91b/dev-3.0

- **Source:** automatic (medium confidence)
- **Dominance:** 0.789

Reasons:

- covers 100% of capabilities (7/7)
- 1.19x the stars (323 vs 272)
- 12.00x the star velocity (0.6/day vs 0.0/day)
- no harder to set up (12 vs 14 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "parallel-execution",
    "remote-control",
    "session-persistence",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "quota-management",
    "remote-control",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 43,
  "challenger_health": 55,
  "incumbent_setup_score": 14,
  "challenger_setup_score": 12
}
```

### managedcode/dotnet-skills → data-goblin/power-bi-agentic-development

- **Source:** automatic (medium confidence)
- **Dominance:** 0.771

Reasons:

- covers 100% of capabilities (6/6)
- 2.16x the stars (1,080 vs 499)
- 2.33x the star velocity (1.4/day vs 0.6/day)
- slightly heavier setup (+12 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "incumbent_health": 56,
  "challenger_health": 57,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 34
}
```

### zhinkgit/embeddedskills → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (medium confidence)
- **Dominance:** 0.626

Reasons:

- covers 100% of capabilities (4/4)
- 1.46x the stars (1,137 vs 780)
- 1.50x the star velocity (2.4/day vs 1.6/day)
- slightly heavier setup (+12 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "multi-agent-orchestration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 53,
  "challenger_health": 55,
  "incumbent_setup_score": 18,
  "challenger_setup_score": 30
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
