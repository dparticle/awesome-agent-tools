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
- 9.90x the stars (7,087 vs 716)
- 10.38x the star velocity (30.4/day vs 2.9/day)
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

### AlickH/Copool → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 57.25x the stars (18,720 vs 327)
- 45.28x the star velocity (70.6/day vs 1.6/day)
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

### Arvincreator/project-golem → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 3.79x the stars (2,422 vs 639)
- 13.57x the star velocity (34.6/day vs 2.5/day)
- no harder to set up (34 vs 45 friction)

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
  "incumbent_health": 39,
  "challenger_health": 66,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 34
}
```

### Ibrahim-3d/orchestrator-supaconductor → HarnessMD/munder-difflin

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 22.58x the stars (8,582 vs 380)
- 40.57x the star velocity (66.5/day vs 1.6/day)
- no harder to set up (32 vs 72 friction)

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
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 48,
  "challenger_health": 75,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 32
}
```

### LerianStudio/ring → XiaomiMiMo/MiMo-Code

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 62.73x the stars (13,612 vs 217)
- 181.57x the star velocity (114.4/day vs 0.6/day)
- no harder to set up (30 vs 40 friction)

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
  "challenger_health": 85,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 30
}
```

### MagicCube/agentara → pacifio/atlas

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 18.14x the stars (9,359 vs 516)
- 26.93x the star velocity (64.1/day vs 2.4/day)
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

### MemTensor/memmy-agent → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 14.10x the stars (29,236 vs 2,074)
- 5.26x the star velocity (129.9/day vs 24.7/day)
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
  "incumbent_health": 60,
  "challenger_health": 88,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### Pimzino/spec-workflow-mcp → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 63.97x the stars (275,209 vs 4,302)
- 103.61x the star velocity (1046.4/day vs 10.1/day)
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

### appautomaton/latex-arxiv-SKILL → nexu-io/open-design

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 218.28x the stars (99,970 vs 458)
- 757.17x the star velocity (613.3/day vs 0.8/day)
- no harder to set up (29 vs 36 friction)

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
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "quota-distribution",
    "self-hosted",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 48,
  "challenger_health": 95,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 29
}
```

### darrenhinde/OpenAgentsControl → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 5.59x the stars (27,330 vs 4,892)
- 8.42x the star velocity (98.3/day vs 11.7/day)
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

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 24.21x the stars (7,918 vs 327)
- 60.01x the star velocity (87.0/day vs 1.4/day)
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

### hkqr/my-free-code → nexu-io/open-design

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 160.21x the stars (99,970 vs 624)
- 40.30x the star velocity (613.3/day vs 15.2/day)
- no harder to set up (29 vs 34 friction)

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
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "quota-distribution",
    "self-hosted",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 52,
  "challenger_health": 95,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 29
}
```

### huytieu/COG-second-brain → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 6.25x the stars (7,918 vs 1,266)
- 24.58x the star velocity (87.0/day vs 3.5/day)
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
- 74.58x the stars (18,720 vs 251)
- 68.58x the star velocity (70.6/day vs 1.0/day)
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
- 46.74x the stars (20,097 vs 430)
- 18.12x the star velocity (56.0/day vs 3.1/day)
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

### jessepwj/CCteam-creator → HarnessMD/munder-difflin

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 27.95x the stars (8,582 vs 307)
- 44.35x the star velocity (66.5/day vs 1.5/day)
- no harder to set up (32 vs 57 friction)

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
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 39,
  "challenger_health": 75,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### kerim0x1/bettercode → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 578.22x the stars (158,431 vs 274)
- 27.38x the star velocity (441.3/day vs 16.1/day)
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

### michaelshimeles/skills → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 21.54x the stars (27,330 vs 1,269)
- 16.72x the star velocity (98.3/day vs 5.9/day)
- no harder to set up (27 vs 28 friction)

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
    "cross-agent-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 85,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 27
}
```

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 143.97x the stars (141,383 vs 982)
- 58.43x the star velocity (329.6/day vs 5.6/day)
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
- 9.57x the stars (5,293 vs 553)
- 28.86x the star velocity (37.8/day vs 1.3/day)
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

### ruvnet/metaharness → redhat-et/ripwire

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 3.51x the stars (2,422 vs 691)
- 5.81x the star velocity (34.6/day vs 6.0/day)
- no harder to set up (34 vs 58 friction)

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
  "incumbent_health": 53,
  "challenger_health": 66,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 34
}
```

### trailhq/Graft → nexu-io/open-design

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 10.23x the stars (99,970 vs 9,770)
- 6.03x the star velocity (613.3/day vs 101.8/day)
- no harder to set up (29 vs 37 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "quota-distribution",
    "self-hosted",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 80,
  "challenger_health": 95,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 29
}
```

### vercel-labs/personal-agent-template → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 580.61x the stars (275,209 vs 474)
- 260.30x the star velocity (1046.4/day vs 4.0/day)
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
  "incumbent_health": 42,
  "challenger_health": 89,
  "incumbent_setup_score": 78,
  "challenger_setup_score": 57
}
```

### zilliztech/memsearch → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 10.72x the stars (29,236 vs 2,728)
- 11.48x the star velocity (129.9/day vs 11.3/day)
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
  "incumbent_health": 57,
  "challenger_health": 88,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### jtydhr88/comfyui-custom-node-skills → FrancyJGLisboa/agent-skills-platform

- **Source:** automatic (high confidence)
- **Dominance:** 0.999

Reasons:

- covers 100% of capabilities (4/4)
- 8.15x the stars (2,403 vs 295)
- 4.96x the star velocity (6.8/day vs 1.4/day)
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

### SethGammon/Citadel → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (6/6)
- 29.64x the stars (27,330 vs 922)
- 21.56x the star velocity (98.3/day vs 4.6/day)
- slightly heavier setup (+2 friction, within tolerance)

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
    "cross-agent-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 55,
  "challenger_health": 85,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### lanes-sh/app → maxritter/pilot-shell

- **Source:** automatic (high confidence)
- **Dominance:** 0.981

Reasons:

- covers 100% of capabilities (7/7)
- 7.63x the stars (2,083 vs 273)
- 4.28x the star velocity (5.9/day vs 1.4/day)
- no harder to set up (12 vs 12 friction)

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
  "incumbent_health": 50,
  "challenger_health": 62,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 12
}
```

### nwiizo/tfmcp → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (5/5)
- 737.83x the stars (275,209 vs 373)
- 1609.88x the star velocity (1046.4/day vs 0.7/day)
- slightly heavier setup (+5 friction, within tolerance)

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
  "incumbent_health": 52,
  "challenger_health": 89,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 57
}
```

### Lling0000/Vibe_coding_guide → maxritter/pilot-shell

- **Source:** automatic (high confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (6/6)
- 9.02x the stars (2,083 vs 231)
- 3.94x the star velocity (5.9/day vs 1.5/day)
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
- 6.94x the stars (44,463 vs 6,408)
- 5.48x the star velocity (310.9/day vs 56.7/day)
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
- 452.65x the stars (275,209 vs 608)
- 364.61x the star velocity (1046.4/day vs 2.9/day)
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
- **Dominance:** 0.966

Reasons:

- covers 100% of capabilities (4/4)
- 2.88x the stars (812 vs 282)
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

### gotalab/cc-sdd → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.965

Reasons:

- covers 100% of capabilities (5/5)
- 7.88x the stars (29,236 vs 3,708)
- 15.69x the star velocity (129.9/day vs 8.3/day)
- slightly heavier setup (+7 friction, within tolerance)

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
  "incumbent_setup_score": 25,
  "challenger_setup_score": 32
}
```

### automagik-dev/genie → maxritter/pilot-shell

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (6/6)
- 6.02x the stars (2,083 vs 346)
- 7.34x the star velocity (5.9/day vs 0.8/day)
- slightly heavier setup (+8 friction, within tolerance)

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
  "incumbent_setup_score": 4,
  "challenger_setup_score": 12
}
```

### WenyuChiou/ai-research-skills → redhat-et/ripwire

- **Source:** automatic (medium confidence)
- **Dominance:** 0.940

Reasons:

- covers 100% of capabilities (5/5)
- 7.89x the stars (2,422 vs 307)
- 18.60x the star velocity (34.6/day vs 1.9/day)
- slightly heavier setup (+12 friction, within tolerance)

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
  "incumbent_health": 54,
  "challenger_health": 66,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 34
}
```

### linxidnju/OpenTag → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.940

Reasons:

- covers 100% of capabilities (4/4)
- 548.23x the stars (275,209 vs 502)
- 214.87x the star velocity (1046.4/day vs 4.9/day)
- slightly heavier setup (+12 friction, within tolerance)

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
  "incumbent_setup_score": 45,
  "challenger_setup_score": 57
}
```

### tigerless-labs/cost-xray → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.908

Reasons:

- covers 100% of capabilities (5/5)
- 8.24x the stars (33,380 vs 4,053)
- 2.39x the star velocity (78.2/day vs 32.7/day)
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
  "incumbent_health": 63,
  "challenger_health": 81,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 2
}
```

### nekocode/agent-worktree → asheshgoplani/agent-deck

- **Source:** automatic (medium confidence)
- **Dominance:** 0.895

Reasons:

- covers 100% of capabilities (6/6)
- 3.72x the stars (1,037 vs 279)
- 2.96x the star velocity (3.4/day vs 1.1/day)
- slightly heavier setup (+8 friction, within tolerance)

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
    "multi-account-switching",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "security-isolation",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 47,
  "challenger_health": 56,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 48
}
```

### giuseppe-trisciuoglio/developer-kit → thedivergentai/GD-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.888

Reasons:

- covers 100% of capabilities (5/5)
- 2.29x the stars (812 vs 355)
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
- **Dominance:** 0.853

Reasons:

- covers 100% of capabilities (6/6)
- 2.86x the stars (14,910 vs 5,209)
- 1.73x the star velocity (78.5/day vs 45.3/day)
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
  "challenger_health": 78,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 29
}
```

### mindmuxai/brain.md → maxritter/pilot-shell

- **Source:** automatic (medium confidence)
- **Dominance:** 0.789

Reasons:

- covers 100% of capabilities (7/7)
- 3.69x the stars (2,083 vs 564)
- 1.16x the star velocity (5.9/day vs 5.0/day)
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

### microsoft/power-platform-skills → yohey-w/multi-agent-shogun

- **Source:** automatic (medium confidence)
- **Dominance:** 0.685

Reasons:

- covers 100% of capabilities (5/5)
- 1.46x the stars (1,423 vs 973)
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

### career-ops-hq/career-ops → nexu-io/open-design

- **Source:** automatic (medium confidence)
- **Dominance:** 0.673

Reasons:

- covers 100% of capabilities (5/5)
- 1.36x the stars (99,970 vs 73,767)
- 1.55x the star velocity (613.3/day vs 396.6/day)
- no harder to set up (29 vs 49 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "model-routing",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "quota-distribution",
    "self-hosted",
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 89,
  "challenger_health": 95,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 29
}
```

### abubakarsiddik31/claude-skills-collection → yohey-w/multi-agent-shogun

- **Source:** automatic (medium confidence)
- **Dominance:** 0.654

Reasons:

- covers 100% of capabilities (11/11)
- 1.30x the stars (1,423 vs 1,091)
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
