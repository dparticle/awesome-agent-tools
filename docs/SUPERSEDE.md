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

### AlickH/Copool → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 60.55x the stars (19,740 vs 326)
- 23.94x the star velocity (32.8/day vs 1.4/day)
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
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 42,
  "challenger_health": 69,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### Autoloops/greplica → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 68.37x the stars (30,152 vs 441)
- 110.00x the star velocity (22.0/day vs 0.2/day)
- no harder to set up (32 vs 37 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "memory-context",
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 41,
  "challenger_health": 69,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 32
}
```

### Ibrahim-3d/orchestrator-supaconductor → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 89.14x the stars (34,050 vs 382)
- 111.00x the star velocity (22.2/day vs 0.2/day)
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
  "challenger_health": 72,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 2
}
```

### MagicCube/agentara → aoci-spec/aoci-code

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 3.59x the stars (1,858 vs 518)
- 25.00x the star velocity (10.0/day vs 0.4/day)
- no harder to set up (73 vs 84 friction)

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
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "session-persistence"
  ],
  "incumbent_health": 38,
  "challenger_health": 55,
  "incumbent_setup_score": 84,
  "challenger_setup_score": 73
}
```

### MemTensor/memmy-agent → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 5.32x the stars (11,693 vs 2,200)
- 9.36x the star velocity (61.8/day vs 6.6/day)
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
  "incumbent_health": 57,
  "challenger_health": 76,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### SethGammon/Citadel → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 36.73x the stars (34,050 vs 927)
- 444.00x the star velocity (22.2/day vs 0.0/day)
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
  "challenger_health": 72,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### Socialpranker/deepdive → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 132.24x the stars (49,193 vs 372)
- 106.33x the star velocity (63.8/day vs 0.6/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 30
}
```

### YYH211/Claude-meta-skill → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 173.21x the stars (49,193 vs 284)
- 1276.00x the star velocity (63.8/day vs 0.0/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 30
}
```

### automagik-dev/genie → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 316.10x the stars (111,268 vs 352)
- 308.14x the star velocity (431.4/day vs 1.4/day)
- no harder to set up (45 vs 50 friction)

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
  "incumbent_health": 55,
  "challenger_health": 89,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 45
}
```

### darrenhinde/OpenAgentsControl → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 22.40x the stars (111,268 vs 4,968)
- 539.25x the star velocity (431.4/day vs 0.8/day)
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
  "incumbent_health": 63,
  "challenger_health": 89,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 45
}
```

### davepoon/buildwithclaude → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 13.21x the stars (49,193 vs 3,725)
- 13.87x the star velocity (63.8/day vs 4.6/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 30
}
```

### fatwang2/search2ai → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 231.19x the stars (297,544 vs 1,287)
- 1950.00x the star velocity (780.0/day vs 0.4/day)
- no harder to set up (57 vs 73 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "mcp-support",
    "model-routing",
    "parallel-execution",
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
  "incumbent_health": 51,
  "challenger_health": 89,
  "incumbent_setup_score": 73,
  "challenger_setup_score": 57
}
```

### future-agi/future-agi → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 13.40x the stars (30,152 vs 2,250)
- 5.79x the star velocity (22.0/day vs 3.8/day)
- no harder to set up (32 vs 45 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "billing-metering",
    "mcp-support",
    "memory-context",
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 59,
  "challenger_health": 69,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### giuseppe-trisciuoglio/developer-kit → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 134.41x the stars (49,193 vs 366)
- 1276.00x the star velocity (63.8/day vs 0.0/day)
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
  "incumbent_health": 43,
  "challenger_health": 81,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 30
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 29.01x the stars (11,693 vs 403)
- 18.18x the star velocity (61.8/day vs 3.4/day)
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
  "challenger_health": 76,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 32
}
```

### internet-court/internet-court-skill → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 6.97x the stars (49,193 vs 7,058)
- 22.79x the star velocity (63.8/day vs 2.8/day)
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
  "incumbent_health": 55,
  "challenger_health": 81,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 30
}
```

### jacobaraujo7/remote_pi → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 48.16x the stars (23,163 vs 481)
- 84.43x the star velocity (118.2/day vs 1.4/day)
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
  "challenger_health": 86,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### jtydhr88/comfyui-custom-node-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 155.67x the stars (49,193 vs 316)
- 79.75x the star velocity (63.8/day vs 0.8/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 30
}
```

### lanes-sh/app → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 122.48x the stars (34,050 vs 278)
- 55.50x the star velocity (22.2/day vs 0.4/day)
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
  "challenger_health": 72,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 2
}
```

### matrixorigin/memoria → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 476.83x the stars (297,544 vs 624)
- 975.00x the star velocity (780.0/day vs 0.8/day)
- no harder to set up (57 vs 63 friction)

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
  "incumbent_health": 51,
  "challenger_health": 89,
  "incumbent_setup_score": 63,
  "challenger_setup_score": 57
}
```

### ndycode/codex-multi-auth → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 35.12x the stars (19,740 vs 562)
- 164.00x the star velocity (32.8/day vs 0.2/day)
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
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 54,
  "challenger_health": 69,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### nekocode/agent-worktree → Gentleman-Programming/gentle-shell

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 6.05x the stars (1,705 vs 282)
- 193.00x the star velocity (38.6/day vs 0.2/day)
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
    "remote-control",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 49,
  "challenger_health": 65,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 30
}
```

### nwiizo/tfmcp → aipoch/open-science

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 14.74x the stars (5,468 vs 371)
- 252.00x the star velocity (12.6/day vs 0.0/day)
- no harder to set up (35 vs 52 friction)

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
    "notifications",
    "remote-control",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 52,
  "challenger_health": 65,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 35
}
```

### oceanbase/powercontext → xerj-org/xerj

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 12.93x the stars (19,155 vs 1,482)
- 66.40x the star velocity (265.6/day vs 4.0/day)
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
  "incumbent_health": 54,
  "challenger_health": 87,
  "incumbent_setup_score": 63,
  "challenger_setup_score": 33
}
```

### oomol-lab/open-connector → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 48.10x the stars (297,544 vs 6,186)
- 97.50x the star velocity (780.0/day vs 8.0/day)
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
  "incumbent_health": 56,
  "challenger_health": 89,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 57
}
```

### pax-beehive/paxm → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 106.54x the stars (30,152 vs 283)
- 110.00x the star velocity (22.0/day vs 0.2/day)
- no harder to set up (32 vs 40 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
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
  "incumbent_health": 47,
  "challenger_health": 69,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 32
}
```

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 154.98x the stars (152,034 vs 981)
- 5980.00x the star velocity (299.0/day vs 0.0/day)
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

### savannahfeder/agentbox → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 97.01x the stars (34,050 vs 351)
- 6.17x the star velocity (22.2/day vs 3.6/day)
- no harder to set up (2 vs 30 friction)

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
  "incumbent_health": 49,
  "challenger_health": 72,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 2
}
```

### vercel-labs/personal-agent-template → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 614.76x the stars (297,544 vs 484)
- 1300.00x the star velocity (780.0/day vs 0.6/day)
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

### vibeeval/vibecosystem → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 91.27x the stars (49,193 vs 539)
- 27.98x the star velocity (63.8/day vs 2.3/day)
- no harder to set up (30 vs 37 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
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
  "incumbent_health": 53,
  "challenger_health": 81,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 30
}
```

### wenfxl/openai-cpa → milind-soni/OpenMausBot

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 8.94x the stars (12,546 vs 1,404)
- 13588.00x the star velocity (679.4/day vs 0.0/day)
- no harder to set up (28 vs 57 friction)

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
  "incumbent_health": 49,
  "challenger_health": 87,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 28
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 4.14x the stars (11,693 vs 2,821)
- 34.33x the star velocity (61.8/day vs 1.8/day)
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
  "challenger_health": 76,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### huytieu/COG-second-brain → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (9/9)
- 8.72x the stars (11,693 vs 1,341)
- 25.75x the star velocity (61.8/day vs 2.4/day)
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
  "challenger_health": 76,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 32
}
```

### gotalab/cc-sdd → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (5/5)
- 13.10x the stars (49,193 vs 3,756)
- 39.87x the star velocity (63.8/day vs 1.6/day)
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
  "incumbent_health": 58,
  "challenger_health": 81,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 30
}
```

### Draculabo/AntigravityManager → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 0.972

Reasons:

- covers 100% of capabilities (8/8)
- 8.02x the stars (19,740 vs 2,461)
- 4.00x the star velocity (32.8/day vs 8.2/day)
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
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 55,
  "challenger_health": 69,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### callstack/agent-device → getpaseo/paseo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (9/9)
- 4.39x the stars (23,163 vs 5,276)
- 8.69x the star velocity (118.2/day vs 13.6/day)
- slightly heavier setup (+6 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "multi-agent-orchestration",
    "parallel-execution",
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
  "incumbent_health": 65,
  "challenger_health": 86,
  "incumbent_setup_score": 18,
  "challenger_setup_score": 24
}
```

### grpcer/ownmem → xerj-org/xerj

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (4/4)
- 45.07x the stars (19,155 vs 425)
- 5312.00x the star velocity (265.6/day vs 0.0/day)
- slightly heavier setup (+8 friction, within tolerance)

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
  "incumbent_health": 55,
  "challenger_health": 87,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 33
}
```

### kerim0x1/bettercode → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (6/6)
- 44.80x the stars (11,693 vs 261)
- 1236.00x the star velocity (61.8/day vs 0.0/day)
- slightly heavier setup (+8 friction, within tolerance)

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
  "incumbent_health": 52,
  "challenger_health": 76,
  "incumbent_setup_score": 24,
  "challenger_setup_score": 32
}
```

### cluster1900/apexo-code → bytedance/deer-flow

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (8/8)
- 280.60x the stars (85,021 vs 303)
- 28.77x the star velocity (53.8/day vs 1.9/day)
- slightly heavier setup (+9 friction, within tolerance)

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
  "incumbent_health": 47,
  "challenger_health": 76,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 57
}
```

### michaelshimeles/rstack → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (5/5)
- 23.55x the stars (34,050 vs 1,446)
- 3.47x the star velocity (22.2/day vs 6.4/day)
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
  "incumbent_health": 53,
  "challenger_health": 72,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.945

Reasons:

- covers 100% of capabilities (4/4)
- 2.36x the stars (1,146 vs 486)
- 13.00x the star velocity (2.6/day vs 0.2/day)
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

### Archive228/loopkit → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.945

Reasons:

- covers 100% of capabilities (5/5)
- 64.98x the stars (49,193 vs 757)
- 319.00x the star velocity (63.8/day vs 0.2/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 19,
  "challenger_setup_score": 30
}
```

### CopilotKit/OpenBot → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.907

Reasons:

- covers 100% of capabilities (7/7)
- 29.13x the stars (297,544 vs 10,213)
- 3.27x the star velocity (780.0/day vs 238.8/day)
- slightly heavier setup (+8 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "mcp-support",
    "model-routing",
    "notifications",
    "security-isolation",
    "self-hosted",
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
  "incumbent_health": 84,
  "challenger_health": 89,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 57
}
```

### WenyuChiou/ai-research-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.867

Reasons:

- covers 100% of capabilities (5/5)
- 81.72x the stars (49,193 vs 602)
- 2.36x the star velocity (63.8/day vs 27.0/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 30
}
```

### rsmdt/the-startup → thedivergentai/Game-Dev-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.858

Reasons:

- covers 100% of capabilities (4/4)
- 1.61x the stars (929 vs 577)
- 16.00x the star velocity (3.2/day vs 0.2/day)
- no harder to set up (21 vs 25 friction)

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
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins"
  ],
  "incumbent_health": 51,
  "challenger_health": 56,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 21
}
```

### Waishnav/devspace → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.841

Reasons:

- covers 100% of capabilities (7/7)
- 6.29x the stars (34,050 vs 5,411)
- 1.39x the star velocity (22.2/day vs 16.0/day)
- no harder to set up (2 vs 28 friction)

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
  "incumbent_health": 62,
  "challenger_health": 72,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 2
}
```

### google/artemis → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 0.840

Reasons:

- covers 100% of capabilities (6/6)
- 10.00x the stars (166,661 vs 16,661)
- 1.38x the star velocity (216.6/day vs 157.4/day)
- no harder to set up (1 vs 56 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "mobile-access",
    "multi-agent-orchestration",
    "notifications"
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
  "incumbent_health": 79,
  "challenger_health": 96,
  "incumbent_setup_score": 56,
  "challenger_setup_score": 1
}
```

### sandbox-quantum/switch → genspark-ai/genoffice

- **Source:** automatic (medium confidence)
- **Dominance:** 0.829

Reasons:

- covers 100% of capabilities (6/6)
- 3.02x the stars (11,757 vs 3,894)
- 1.97x the star velocity (68.4/day vs 34.8/day)
- slightly heavier setup (+11 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "self-hosted",
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
  "incumbent_health": 68,
  "challenger_health": 75,
  "incumbent_setup_score": 9,
  "challenger_setup_score": 20
}
```

### yetone/cumora → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 0.819

Reasons:

- covers 100% of capabilities (9/9)
- 2.72x the stars (11,230 vs 4,129)
- 1.39x the star velocity (17.8/day vs 12.8/day)
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

### phuryn/pm-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.759

Reasons:

- covers 100% of capabilities (4/4)
- 1.78x the stars (49,193 vs 27,708)
- 2.11x the star velocity (63.8/day vs 30.2/day)
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
  "challenger_health": 81,
  "incumbent_setup_score": 27,
  "challenger_setup_score": 30
}
```

### sahithvibudhi/vibe-tree → h0x91b/dev-3.0

- **Source:** automatic (medium confidence)
- **Dominance:** 0.677

Reasons:

- covers 100% of capabilities (7/7)
- 1.19x the stars (326 vs 273)
- 2.00x the star velocity (0.4/day vs 0.2/day)
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
