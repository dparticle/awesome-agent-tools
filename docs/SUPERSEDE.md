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
- 332.17x the stars (288,321 vs 868)
- 231.94x the star velocity (788.6/day vs 3.4/day)
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
- 59.07x the stars (19,316 vs 327)
- 720.00x the star velocity (36.0/day vs 0.0/day)
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
- 68.05x the stars (29,874 vs 439)
- 688.00x the star velocity (34.4/day vs 0.0/day)
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
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 46,
  "challenger_health": 71,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 32
}
```

### BennyKok/omg.dev → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 20.09x the stars (11,029 vs 549)
- 57.00x the star velocity (22.8/day vs 0.4/day)
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
  "challenger_health": 68,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 25
}
```

### Dodaios/Dodaios → HarnessMD/munder-difflin

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 36.14x the stars (9,035 vs 250)
- 11.78x the star velocity (21.2/day vs 1.8/day)
- no harder to set up (32 vs 50 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins",
    "voice-input",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
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
    "usage-analytics",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 55,
  "challenger_health": 66,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 32
}
```

### Draculabo/AntigravityManager → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 8.03x the stars (19,316 vs 2,405)
- 15.00x the star velocity (36.0/day vs 2.4/day)
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
  "challenger_health": 69,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### Ibrahim-3d/orchestrator-supaconductor → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 28.85x the stars (10,963 vs 380)
- 2300.00x the star velocity (115.0/day vs 0.0/day)
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
  "challenger_health": 86,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 32
}
```

### LeoYeAI/talewell → genspark-ai/genoffice

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 19.59x the stars (10,775 vs 550)
- 677.00x the star velocity (135.4/day vs 0.2/day)
- no harder to set up (20 vs 23 friction)

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
    "model-routing",
    "parallel-execution",
    "self-hosted",
    "skills-plugins",
    "usage-analytics"
  ],
  "incumbent_health": 50,
  "challenger_health": 85,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 20
}
```

### Othmane-Khadri/YALC-the-GTM-operating-system → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 892.63x the stars (288,321 vs 323)
- 1314.33x the star velocity (788.6/day vs 0.6/day)
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
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### SethGammon/Citadel → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 36.41x the stars (33,754 vs 927)
- 49.00x the star velocity (19.6/day vs 0.4/day)
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

### Waishnav/devspace → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 4.14x the stars (21,916 vs 5,291)
- 35.08x the star velocity (84.2/day vs 2.4/day)
- no harder to set up (24 vs 28 friction)

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
  "incumbent_health": 56,
  "challenger_health": 79,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 24
}
```

### YYH211/Claude-meta-skill → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 4.64x the stars (1,317 vs 284)
- 52.00x the star velocity (2.6/day vs 0.0/day)
- no harder to set up (31 vs 58 friction)

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
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 42,
  "challenger_health": 57,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 31
}
```

### aoci-spec/aoci-code → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 166.18x the stars (288,321 vs 1,735)
- 39.83x the star velocity (788.6/day vs 19.8/day)
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

- covers 100% of capabilities (6/6)
- 97.84x the stars (33,754 vs 345)
- 392.00x the star velocity (19.6/day vs 0.0/day)
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
  "challenger_health": 71,
  "incumbent_setup_score": 4,
  "challenger_setup_score": 2
}
```

### darrenhinde/OpenAgentsControl → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 21.66x the stars (107,081 vs 4,944)
- 96.59x the star velocity (425.0/day vs 4.4/day)
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

### fatwang2/search2ai → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 224.90x the stars (288,321 vs 1,282)
- 641.14x the star velocity (788.6/day vs 1.2/day)
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

### glebis/claude-skills → XiaomiMiMo/MiMo-Code

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 34.30x the stars (13,720 vs 400)
- 5.60x the star velocity (5.6/day vs 1.0/day)
- no harder to set up (21 vs 36 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
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
    "voice-input"
  ],
  "incumbent_health": 51,
  "challenger_health": 64,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 21
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 29.71x the stars (10,963 vs 369)
- 35.94x the star velocity (115.0/day vs 3.2/day)
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
  "incumbent_health": 46,
  "challenger_health": 86,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 32
}
```

### jacobaraujo7/remote_pi → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 23.62x the stars (11,029 vs 467)
- 38.00x the star velocity (22.8/day vs 0.6/day)
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
  "challenger_health": 68,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 25
}
```

### jdrhyne/agent-skills → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 1201.34x the stars (288,321 vs 240)
- 15772.00x the star velocity (788.6/day vs 0.0/day)
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
  "incumbent_health": 41,
  "challenger_health": 89,
  "incumbent_setup_score": 69,
  "challenger_setup_score": 57
}
```

### lanes-sh/app → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 122.30x the stars (33,754 vs 276)
- 98.00x the star velocity (19.6/day vs 0.2/day)
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
  "incumbent_health": 48,
  "challenger_health": 71,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 2
}
```

### maximhq/bifrost → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 16.34x the stars (148,457 vs 9,088)
- 14.09x the star velocity (366.4/day vs 26.0/day)
- no harder to set up (23 vs 49 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "skills-plugins",
    "usage-analytics"
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
  "incumbent_health": 65,
  "challenger_health": 93,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 23
}
```

### mcpware/cross-code-organizer → genspark-ai/genoffice

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 27.99x the stars (10,775 vs 385)
- 338.50x the star velocity (135.4/day vs 0.4/day)
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
  "challenger_health": 85,
  "incumbent_setup_score": 20,
  "challenger_setup_score": 20
}
```

### mnemon-dev/mnemon → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 437.51x the stars (288,321 vs 659)
- 231.94x the star velocity (788.6/day vs 3.4/day)
- no harder to set up (57 vs 64 friction)

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
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### ndycode/codex-multi-auth → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 34.80x the stars (19,316 vs 555)
- 180.00x the star velocity (36.0/day vs 0.2/day)
- no harder to set up (32 vs 41 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
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
  "incumbent_health": 53,
  "challenger_health": 69,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### nwiizo/tfmcp → aipoch/open-science

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 14.41x the stars (5,359 vs 372)
- 224.00x the star velocity (11.2/day vs 0.0/day)
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
  "challenger_health": 64,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 41
}
```

### okf-memory/okf-agent-memory → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 35.69x the stars (29,874 vs 837)
- 17.20x the star velocity (34.4/day vs 2.0/day)
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
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 55,
  "challenger_health": 71,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### oomol-lab/open-connector → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 47.37x the stars (288,321 vs 6,086)
- 112.66x the star velocity (788.6/day vs 7.0/day)
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

### ruvnet/metaharness → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 402.68x the stars (288,321 vs 716)
- 563.29x the star velocity (788.6/day vs 1.4/day)
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
  "incumbent_setup_score": 58,
  "challenger_setup_score": 57
}
```

### vercel-labs/personal-agent-template → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 605.72x the stars (288,321 vs 476)
- 3943.00x the star velocity (788.6/day vs 0.2/day)
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
  "incumbent_health": 41,
  "challenger_health": 89,
  "incumbent_setup_score": 78,
  "challenger_setup_score": 57
}
```

### yc-software/qm → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (10/10)
- 6.89x the stars (107,081 vs 15,533)
- 27.24x the star velocity (425.0/day vs 15.6/day)
- no harder to set up (45 vs 72 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "model-routing",
    "notifications",
    "security-isolation",
    "session-persistence",
    "skills-plugins",
    "team-collaboration",
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
  "incumbent_health": 58,
  "challenger_health": 89,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 45
}
```

### zilliztech/memsearch → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 10.71x the stars (29,874 vs 2,789)
- 7.17x the star velocity (34.4/day vs 4.8/day)
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 57,
  "challenger_health": 71,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### YoanWai/agent-manager → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.997

Reasons:

- covers 100% of capabilities (5/5)
- 54.09x the stars (33,754 vs 624)
- 4.90x the star velocity (19.6/day vs 4.0/day)
- no harder to set up (2 vs 4 friction)

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
  "incumbent_health": 57,
  "challenger_health": 71,
  "incumbent_setup_score": 4,
  "challenger_setup_score": 2
}
```

### Lling0000/Vibe_coding_guide → TencentCloud/Octop

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (6/6)
- 45.68x the stars (10,963 vs 240)
- 95.83x the star velocity (115.0/day vs 1.2/day)
- slightly heavier setup (+2 friction, within tolerance)

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
  "incumbent_health": 41,
  "challenger_health": 86,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 32
}
```

### rsmdt/the-startup → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (4/4)
- 48.31x the stars (27,634 vs 572)
- 30.00x the star velocity (18.0/day vs 0.6/day)
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
  "incumbent_health": 48,
  "challenger_health": 69,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### giuseppe-trisciuoglio/developer-kit → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.982

Reasons:

- covers 100% of capabilities (5/5)
- 3.63x the stars (1,317 vs 363)
- 4.33x the star velocity (2.6/day vs 0.6/day)
- no harder to set up (31 vs 66 friction)

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
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 44,
  "challenger_health": 57,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 31
}
```

### yetone/cumora → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 0.980

Reasons:

- covers 100% of capabilities (9/9)
- 2.75x the stars (11,029 vs 4,017)
- 6.71x the star velocity (22.8/day vs 3.4/day)
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
  "incumbent_health": 54,
  "challenger_health": 68,
  "incumbent_setup_score": 33,
  "challenger_setup_score": 25
}
```

### ZipengWu365/TOMC → genspark-ai/genoffice

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (8/8)
- 43.80x the stars (10,775 vs 246)
- 9.90x the star velocity (135.4/day vs 13.7/day)
- slightly heavier setup (+5 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "billing-metering",
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
  "incumbent_health": 57,
  "challenger_health": 85,
  "incumbent_setup_score": 15,
  "challenger_setup_score": 20
}
```

### michaelshimeles/skills → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (5/5)
- 24.42x the stars (33,754 vs 1,382)
- 4.08x the star velocity (19.6/day vs 4.8/day)
- no harder to set up (2 vs 22 friction)

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
  "incumbent_health": 56,
  "challenger_health": 71,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 2
}
```

### grpcer/ownmem → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.965

Reasons:

- covers 100% of capabilities (4/4)
- 69.80x the stars (29,874 vs 428)
- 688.00x the star velocity (34.4/day vs 0.0/day)
- slightly heavier setup (+7 friction, within tolerance)

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
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "quota-management",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 55,
  "challenger_health": 71,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 32
}
```

### kajisho5/ffmpeg-skill → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.965

Reasons:

- covers 100% of capabilities (8/8)
- 107.99x the stars (288,321 vs 2,670)
- 15.06x the star velocity (788.6/day vs 52.4/day)
- slightly heavier setup (+7 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
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
  "incumbent_health": 73,
  "challenger_health": 89,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 57
}
```

### nekocode/agent-worktree → asheshgoplani/agent-deck

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (6/6)
- 4.13x the stars (1,157 vs 280)
- 120.00x the star velocity (6.0/day vs 0.0/day)
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
    "quota-management",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 51,
  "challenger_health": 58,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 48
}
```

### Ryze-AI-Adgent/open-seo-mcp-skills → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.956

Reasons:

- covers 100% of capabilities (4/4)
- 40.88x the stars (288,321 vs 7,052)
- 4.65x the star velocity (788.6/day vs 169.6/day)
- slightly heavier setup (+7 friction, within tolerance)

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
  "incumbent_health": 78,
  "challenger_health": 89,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 57
}
```

### Lyellr88/marm-memory → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (12/12)
- 683.23x the stars (288,321 vs 422)
- 15772.00x the star velocity (788.6/day vs 0.0/day)
- slightly heavier setup (+9 friction, within tolerance)

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
  "incumbent_health": 54,
  "challenger_health": 89,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 57
}
```

### hkcanan/katmer-code → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (6/6)
- 606.99x the stars (288,321 vs 475)
- 15772.00x the star velocity (788.6/day vs 0.0/day)
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
  "incumbent_setup_score": 48,
  "challenger_setup_score": 57
}
```

### AI-QL/tuui → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.945

Reasons:

- covers 100% of capabilities (4/4)
- 25.78x the stars (29,874 vs 1,159)
- 688.00x the star velocity (34.4/day vs 0.0/day)
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 71,
  "incumbent_setup_score": 21,
  "challenger_setup_score": 32
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.940

Reasons:

- covers 100% of capabilities (4/4)
- 2.30x the stars (1,114 vs 484)
- 6.82x the star velocity (3.0/day vs 0.4/day)
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

### jtydhr88/comfyui-custom-node-skills → thedivergentai/Game-Dev-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.935

Reasons:

- covers 100% of capabilities (4/4)
- 2.90x the stars (889 vs 307)
- 3.17x the star velocity (3.8/day vs 1.2/day)
- no harder to set up (21 vs 50 friction)

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
    "multi-agent-orchestration",
    "parallel-execution",
    "skills-plugins"
  ],
  "incumbent_health": 44,
  "challenger_health": 56,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 21
}
```

### Archive228/loopkit → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.817

Reasons:

- covers 100% of capabilities (5/5)
- 1.74x the stars (1,317 vs 755)
- 52.00x the star velocity (2.6/day vs 0.0/day)
- slightly heavier setup (+12 friction, within tolerance)

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
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 45,
  "challenger_health": 57,
  "incumbent_setup_score": 19,
  "challenger_setup_score": 31
}
```

### Socialpranker/deepdive → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.812

Reasons:

- covers 100% of capabilities (4/4)
- 3.58x the stars (1,317 vs 368)
- 1.10x the star velocity (2.6/day vs 2.4/day)
- no harder to set up (31 vs 51 friction)

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
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 52,
  "challenger_health": 57,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 31
}
```

### linxidnju/OpenTag → kitfunso/hippo-memory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.801

Reasons:

- covers 100% of capabilities (4/4)
- 1.56x the stars (784 vs 503)
- 8.00x the star velocity (0.4/day vs 0.0/day)
- slightly heavier setup (+10 friction, within tolerance)

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
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "worktree-isolation"
  ],
  "incumbent_health": 41,
  "challenger_health": 55,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 55
}
```

### wenfxl/openai-cpa → tickernelz/opencode-mem

- **Source:** automatic (medium confidence)
- **Dominance:** 0.790

Reasons:

- covers 100% of capabilities (4/4)
- 1.27x the stars (1,785 vs 1,404)
- 14.00x the star velocity (2.8/day vs 0.2/day)
- slightly heavier setup (+3 friction, within tolerance)

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
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 49,
  "challenger_health": 55,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 60
}
```

### WenyuChiou/ai-research-skills → thedivergentai/Game-Dev-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.758

Reasons:

- covers 100% of capabilities (5/5)
- 2.19x the stars (889 vs 406)
- 1.27x the star velocity (3.8/day vs 3.0/day)
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
  "incumbent_health": 55,
  "challenger_health": 56,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 21
}
```

### managedcode/dotnet-skills → data-goblin/power-bi-agentic-development

- **Source:** automatic (medium confidence)
- **Dominance:** 0.715

Reasons:

- covers 100% of capabilities (6/6)
- 2.16x the stars (1,066 vs 494)
- 1.50x the star velocity (1.2/day vs 0.8/day)
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

### sahithvibudhi/vibe-tree → h0x91b/dev-3.0

- **Source:** automatic (medium confidence)
- **Dominance:** 0.700

Reasons:

- covers 100% of capabilities (7/7)
- 1.17x the stars (317 vs 270)
- 2.50x the star velocity (1.0/day vs 0.4/day)
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

### matrixorigin/memoria → kitfunso/hippo-memory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.691

Reasons:

- covers 100% of capabilities (6/6)
- 1.27x the stars (784 vs 615)
- 2.00x the star velocity (0.4/day vs 0.2/day)
- no harder to set up (55 vs 63 friction)

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
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "worktree-isolation"
  ],
  "incumbent_health": 51,
  "challenger_health": 55,
  "incumbent_setup_score": 63,
  "challenger_setup_score": 55
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
