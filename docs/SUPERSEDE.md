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

### 1llu50ry/Decompile → ruvnet/ruflo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 141.40x the stars (82,011 vs 580)
- 11.67x the star velocity (153.9/day vs 13.2/day)
- no harder to set up (18 vs 32 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "security-isolation",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 58,
  "challenger_health": 93,
  "incumbent_setup_score": 32,
  "challenger_setup_score": 18
}
```

### AlickH/Copool → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 62.25x the stars (20,106 vs 323)
- 604.00x the star velocity (30.2/day vs 0.0/day)
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

### Draculabo/AntigravityManager → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 7.96x the stars (20,106 vs 2,526)
- 5.21x the star velocity (30.2/day vs 5.8/day)
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

### GizClaw/flowcraft → pedrohcgs/claude-code-my-workflow

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 4.18x the stars (1,717 vs 411)
- 48.00x the star velocity (2.4/day vs 0.0/day)
- no harder to set up (8 vs 28 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "skills-plugins",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 60,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 8
}
```

### Ibrahim-3d/orchestrator-supaconductor → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 89.48x the stars (34,360 vs 384)
- 99.00x the star velocity (19.8/day vs 0.2/day)
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
  "incumbent_health": 45,
  "challenger_health": 70,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 2
}
```

### Lampese/codex-switcher → yetone/magpie

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 41.37x the stars (38,518 vs 931)
- 434.00x the star velocity (520.8/day vs 1.2/day)
- no harder to set up (11 vs 36 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "multi-account-switching",
    "multi-agent-orchestration",
    "quota-management"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "model-routing",
    "multi-account-switching",
    "multi-agent-orchestration",
    "quota-management"
  ],
  "incumbent_health": 51,
  "challenger_health": 91,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 11
}
```

### MemTensor/memmy-agent → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 5.49x the stars (12,211 vs 2,224)
- 19.40x the star velocity (38.8/day vs 2.0/day)
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
  "challenger_health": 71,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### Othmane-Khadri/YALC-the-GTM-operating-system → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 151.31x the stars (49,932 vs 330)
- 99.33x the star velocity (59.6/day vs 0.6/day)
- no harder to set up (32 vs 64 friction)

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
  "challenger_health": 80,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 32
}
```

### SethGammon/Citadel → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 36.95x the stars (34,360 vs 930)
- 396.00x the star velocity (19.8/day vs 0.0/day)
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
  "challenger_health": 70,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### Socialpranker/deepdive → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 133.87x the stars (49,932 vs 373)
- 49.67x the star velocity (59.6/day vs 1.2/day)
- no harder to set up (32 vs 51 friction)

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
  "challenger_health": 80,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 32
}
```

### Tencent/LoopForge → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 30.86x the stars (114,706 vs 3,717)
- 7.20x the star velocity (236.8/day vs 32.9/day)
- no harder to set up (45 vs 55 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "self-hosted",
    "usage-analytics",
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
  "incumbent_setup_score": 55,
  "challenger_setup_score": 45
}
```

### athola/claude-night-market → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 142.66x the stars (49,932 vs 350)
- 1192.00x the star velocity (59.6/day vs 0.0/day)
- no harder to set up (32 vs 42 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
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
  "incumbent_health": 52,
  "challenger_health": 80,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### automagik-si/genie → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 97.06x the stars (34,360 vs 354)
- 49.50x the star velocity (19.8/day vs 0.4/day)
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
  "challenger_health": 70,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 2
}
```

### cluster1900/apexo-code → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 100.48x the stars (30,446 vs 303)
- 444.00x the star velocity (22.2/day vs 0.0/day)
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
  "challenger_health": 69,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 32
}
```

### darrenhinde/OpenAgentsControl → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 5.65x the stars (28,122 vs 4,980)
- 10.62x the star velocity (17.0/day vs 1.6/day)
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
  "incumbent_health": 63,
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
- 13.28x the stars (49,932 vs 3,759)
- 16.56x the star velocity (59.6/day vs 3.6/day)
- no harder to set up (32 vs 50 friction)

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
  "challenger_health": 80,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 32
}
```

### fatwang2/search2ai → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 9.48x the stars (12,211 vs 1,288)
- 776.00x the star velocity (38.8/day vs 0.0/day)
- no harder to set up (32 vs 66 friction)

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
  "incumbent_health": 53,
  "challenger_health": 71,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 32
}
```

### future-agi/future-agi → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 5.35x the stars (12,211 vs 2,282)
- 14.92x the star velocity (38.8/day vs 2.6/day)
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
  "challenger_health": 71,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### giuseppe-trisciuoglio/developer-kit → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 134.23x the stars (49,932 vs 372)
- 149.00x the star velocity (59.6/day vs 0.4/day)
- no harder to set up (32 vs 66 friction)

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
  "challenger_health": 80,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 32
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 28.80x the stars (12,211 vs 424)
- 32.33x the star velocity (38.8/day vs 1.2/day)
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
  "challenger_health": 71,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 32
}
```

### jacobaraujo7/remote_pi → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 48.96x the stars (24,335 vs 497)
- 61.83x the star velocity (74.2/day vs 1.2/day)
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
  "challenger_health": 78,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### jtydhr88/comfyui-custom-node-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 156.53x the stars (49,932 vs 319)
- 1192.00x the star velocity (59.6/day vs 0.0/day)
- no harder to set up (32 vs 50 friction)

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
  "incumbent_health": 41,
  "challenger_health": 80,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 32
}
```

### matrixorigin/memoria → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 486.60x the stars (306,070 vs 629)
- 1922.00x the star velocity (768.8/day vs 0.4/day)
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

### oomol-lab/open-connector → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 48.84x the stars (306,070 vs 6,267)
- 147.85x the star velocity (768.8/day vs 5.2/day)
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
  "incumbent_health": 55,
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
- 158.32x the stars (155,469 vs 982)
- 1320.00x the star velocity (264.0/day vs 0.2/day)
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
  "challenger_health": 94,
  "incumbent_setup_score": 33,
  "challenger_setup_score": 23
}
```

### savannahfeder/agentbox → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 56.07x the stars (24,335 vs 434)
- 11.24x the star velocity (74.2/day vs 6.6/day)
- no harder to set up (24 vs 36 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
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
  "incumbent_health": 50,
  "challenger_health": 78,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### tonhowtf/omniget → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 11.67x the stars (169,103 vs 14,494)
- 10.61x the star velocity (214.4/day vs 20.2/day)
- no harder to set up (1 vs 23 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "voice-input"
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
  "incumbent_health": 65,
  "challenger_health": 96,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 1
}
```

### wenfxl/openai-cpa → garrytan/gstack

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 101.05x the stars (141,974 vs 1,405)
- 377.24x the star velocity (109.4/day vs 0.3/day)
- no harder to set up (39 vs 57 friction)

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
  "incumbent_health": 54,
  "challenger_health": 89,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 39
}
```

### yc-software/qm → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (10/10)
- 7.29x the stars (114,706 vs 15,738)
- 26.91x the star velocity (236.8/day vs 8.8/day)
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
  "incumbent_health": 57,
  "challenger_health": 89,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 45
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 4.21x the stars (12,211 vs 2,899)
- 6.26x the star velocity (38.8/day vs 6.2/day)
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
  "incumbent_health": 58,
  "challenger_health": 71,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### AMAP-ML/LongHorizon-Harness → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (8/8)
- 16.22x the stars (30,446 vs 1,877)
- 22.20x the star velocity (22.2/day vs 1.0/day)
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 59,
  "challenger_health": 69,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 32
}
```

### oracle/mcp → ruvnet/ruflo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (5/5)
- 169.44x the stars (82,011 vs 484)
- 128.23x the star velocity (153.9/day vs 1.2/day)
- slightly heavier setup (+2 friction, within tolerance)

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
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "security-isolation",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 55,
  "challenger_health": 93,
  "incumbent_setup_score": 16,
  "challenger_setup_score": 18
}
```

### rsmdt/the-startup → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (4/4)
- 48.24x the stars (28,122 vs 583)
- 28.33x the star velocity (17.0/day vs 0.6/day)
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
  "incumbent_health": 51,
  "challenger_health": 69,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### CopilotKit/OpenBot → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 0.989

Reasons:

- covers 100% of capabilities (9/9)
- 23.88x the stars (306,070 vs 12,817)
- 4.59x the star velocity (768.8/day vs 167.4/day)
- no harder to set up (57 vs 64 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
    "gui-desktop",
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
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### basketikun/chatgpt2api → decolua/9router

- **Source:** automatic (medium confidence)
- **Dominance:** 0.987

Reasons:

- covers 100% of capabilities (4/4)
- 4.69x the stars (32,598 vs 6,947)
- 4.67x the star velocity (48.6/day vs 10.4/day)
- slightly heavier setup (+1 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "billing-metering",
    "multi-account-switching",
    "quota-management",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "api-gateway",
    "billing-metering",
    "cross-agent-support",
    "model-routing",
    "multi-account-switching",
    "quota-management",
    "remote-control",
    "self-hosted",
    "usage-analytics"
  ],
  "incumbent_health": 54,
  "challenger_health": 70,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 73
}
```

### vibeeval/vibecosystem → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.978

Reasons:

- covers 100% of capabilities (5/5)
- 2.72x the stars (1,501 vs 551)
- 18.75x the star velocity (15.0/day vs 0.8/day)
- no harder to set up (31 vs 37 friction)

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
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 53,
  "challenger_health": 59,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 31
}
```

### umutxyp/Seo-Promt-Master → xerj-org/xerj

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (4/4)
- 32.53x the stars (19,227 vs 591)
- 21.90x the star velocity (43.8/day vs 2.0/day)
- slightly heavier setup (+5 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
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
  "challenger_health": 73,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 33
}
```

### callstack/agent-device → getpaseo/paseo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (9/9)
- 4.47x the stars (24,335 vs 5,440)
- 5.30x the star velocity (74.2/day vs 14.0/day)
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
  "challenger_health": 78,
  "incumbent_setup_score": 18,
  "challenger_setup_score": 24
}
```

### grpcer/ownmem → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (4/4)
- 3.52x the stars (1,501 vs 427)
- 75.00x the star velocity (15.0/day vs 0.2/day)
- slightly heavier setup (+6 friction, within tolerance)

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
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 52,
  "challenger_health": 59,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 31
}
```

### felinics/Memoh → paperclipai/paperclip

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (9/9)
- 40.65x the stars (114,706 vs 2,822)
- 49.33x the star velocity (236.8/day vs 4.8/day)
- slightly heavier setup (+8 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
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
  "incumbent_health": 56,
  "challenger_health": 89,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 45
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.952

Reasons:

- covers 100% of capabilities (4/4)
- 2.43x the stars (1,187 vs 489)
- 6.00x the star velocity (1.2/day vs 0.2/day)
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
  "incumbent_health": 49,
  "challenger_health": 55,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 30
}
```

### WenyuChiou/ai-research-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.950

Reasons:

- covers 100% of capabilities (5/5)
- 73.86x the stars (49,932 vs 676)
- 13.55x the star velocity (59.6/day vs 4.4/day)
- slightly heavier setup (+10 friction, within tolerance)

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
  "incumbent_health": 57,
  "challenger_health": 80,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 32
}
```

### LeoYeAI/talewell → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.938

Reasons:

- covers 100% of capabilities (5/5)
- 2.73x the stars (1,501 vs 550)
- 300.00x the star velocity (15.0/day vs 0.0/day)
- slightly heavier setup (+8 friction, within tolerance)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 59,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 31
}
```

### mark3labs/mcp-go → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 0.927

Reasons:

- covers 100% of capabilities (4/4)
- 2.18x the stars (20,106 vs 9,244)
- 16.78x the star velocity (30.2/day vs 1.8/day)
- no harder to set up (32 vs 48 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "mcp-support",
    "notifications",
    "parallel-execution",
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
  "incumbent_health": 58,
  "challenger_health": 69,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 32
}
```

### sandbox-quantum/switch → genspark-ai/genoffice

- **Source:** automatic (medium confidence)
- **Dominance:** 0.927

Reasons:

- covers 100% of capabilities (6/6)
- 2.77x the stars (12,578 vs 4,546)
- 5.16x the star velocity (58.8/day vs 11.4/day)
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
  "incumbent_health": 64,
  "challenger_health": 74,
  "incumbent_setup_score": 9,
  "challenger_setup_score": 20
}
```

### devaccuracy/ledgerforge → aipoch/open-science

- **Source:** automatic (high confidence)
- **Dominance:** 0.915

Reasons:

- covers 100% of capabilities (4/4)
- 16.50x the stars (5,545 vs 336)
- 2.51x the star velocity (4.4/day vs 1.8/day)
- no harder to set up (21 vs 52 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "billing-metering",
    "mcp-support",
    "notifications",
    "security-isolation"
  ],
  "challenger_capabilities": [
    "billing-metering",
    "gui-desktop",
    "mcp-support",
    "notifications",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 45,
  "challenger_health": 64,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 21
}
```

### oceanbase/powercontext → xerj-org/xerj

- **Source:** automatic (high confidence)
- **Dominance:** 0.909

Reasons:

- covers 100% of capabilities (4/4)
- 11.11x the stars (19,227 vs 1,731)
- 2.41x the star velocity (43.8/day vs 18.2/day)
- no harder to set up (33 vs 69 friction)

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
  "incumbent_health": 56,
  "challenger_health": 73,
  "incumbent_setup_score": 69,
  "challenger_setup_score": 33
}
```

### Xpropel/Pi-Remote → greenfield-inc/Pane

- **Source:** automatic (high confidence)
- **Dominance:** 0.906

Reasons:

- covers 100% of capabilities (4/4)
- 1.98x the stars (661 vs 333)
- 7.40x the star velocity (7.4/day vs 1.0/day)
- no harder to set up (29 vs 34 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "gui-desktop",
    "model-routing",
    "parallel-execution"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "self-hosted",
    "session-persistence",
    "voice-input",
    "worktree-isolation"
  ],
  "incumbent_health": 52,
  "challenger_health": 57,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 29
}
```

### michaelshimeles/rstack → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.901

Reasons:

- covers 100% of capabilities (5/5)
- 22.53x the stars (34,360 vs 1,525)
- 2.25x the star velocity (19.8/day vs 8.8/day)
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
  "challenger_health": 70,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### arjun988/blender-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.881

Reasons:

- covers 100% of capabilities (4/4)
- 11.85x the stars (49,932 vs 4,215)
- 1.92x the star velocity (59.6/day vs 31.0/day)
- no harder to set up (32 vs 51 friction)

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
  "incumbent_health": 61,
  "challenger_health": 80,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 32
}
```

### okf-memory/okf-agent-memory → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.875

Reasons:

- covers 100% of capabilities (5/5)
- 1.73x the stars (1,501 vs 868)
- 37.50x the star velocity (15.0/day vs 0.4/day)
- no harder to set up (31 vs 45 friction)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 54,
  "challenger_health": 59,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 31
}
```

### findavoulot1973/Blender-AI-MCP-Suite → ruvnet/ruflo

- **Source:** automatic (high confidence)
- **Dominance:** 0.854

Reasons:

- covers 100% of capabilities (4/4)
- 164.68x the stars (82,011 vs 498)
- 1.54x the star velocity (153.9/day vs 99.6/day)
- no harder to set up (18 vs 30 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration"
  ],
  "challenger_capabilities": [
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "security-isolation",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 71,
  "challenger_health": 93,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 18
}
```

### phuryn/pm-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.722

Reasons:

- covers 100% of capabilities (4/4)
- 1.78x the stars (49,932 vs 28,129)
- 1.70x the star velocity (59.6/day vs 35.0/day)
- slightly heavier setup (+5 friction, within tolerance)

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
  "challenger_health": 80,
  "incumbent_setup_score": 27,
  "challenger_setup_score": 32
}
```

### managedcode/dotnet-skills → data-goblin/power-bi-agentic-development

- **Source:** automatic (medium confidence)
- **Dominance:** 0.711

Reasons:

- covers 100% of capabilities (6/6)
- 2.12x the stars (1,098 vs 518)
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
