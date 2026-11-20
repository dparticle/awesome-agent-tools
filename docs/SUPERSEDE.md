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
- 62.73x the stars (20,198 vs 322)
- 30.08x the star velocity (38.2/day vs 1.3/day)
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
  "challenger_health": 70,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### CopilotKit/OpenBot → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 23.61x the stars (307,529 vs 13,025)
- 5.95x the star velocity (811.0/day vs 136.4/day)
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

### Deuz-AI/Deuz-SDK → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 98.48x the stars (50,028 vs 508)
- 1164.00x the star velocity (58.2/day vs 0.0/day)
- no harder to set up (32 vs 37 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "mcp-support",
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
  "incumbent_health": 45,
  "challenger_health": 79,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 32
}
```

### GizClaw/flowcraft → pedrohcgs/claude-code-my-workflow

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 4.21x the stars (1,725 vs 410)
- 60.00x the star velocity (3.0/day vs 0.0/day)
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
- 89.59x the stars (34,403 vs 384)
- 464.00x the star velocity (23.2/day vs 0.0/day)
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
- 42.35x the stars (39,424 vs 931)
- 536.00x the star velocity (536.0/day vs 1.0/day)
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
- 5.52x the stars (12,299 vs 2,227)
- 24.80x the star velocity (49.6/day vs 2.0/day)
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
  "challenger_health": 74,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### Othmane-Khadri/YALC-the-GTM-operating-system → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 151.60x the stars (50,028 vs 330)
- 291.00x the star velocity (58.2/day vs 0.2/day)
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
  "incumbent_health": 41,
  "challenger_health": 79,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 32
}
```

### Pimzino/spec-workflow-mcp → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 71.50x the stars (307,529 vs 4,301)
- 16220.00x the star velocity (811.0/day vs 0.0/day)
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
  "incumbent_health": 45,
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
- 36.83x the stars (34,403 vs 934)
- 38.67x the star velocity (23.2/day vs 0.6/day)
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

### Xpropel/Pi-Remote → Gentleman-Programming/gentle-shell

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 8.50x the stars (2,838 vs 334)
- 60.67x the star velocity (36.4/day vs 0.6/day)
- no harder to set up (30 vs 34 friction)

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
  "incumbent_health": 52,
  "challenger_health": 67,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 30
}
```

### athola/claude-night-market → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 143.35x the stars (50,028 vs 349)
- 646.67x the star velocity (58.2/day vs 0.1/day)
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
  "challenger_health": 79,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 32
}
```

### automagik-si/genie → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 97.18x the stars (34,403 vs 354)
- 116.00x the star velocity (23.2/day vs 0.2/day)
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
- 100.65x the stars (30,496 vs 303)
- 488.00x the star velocity (24.4/day vs 0.0/day)
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

### darrenhinde/OpenAgentsControl → garrytan/gstack

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 28.55x the stars (142,186 vs 4,980)
- 142.00x the star velocity (113.6/day vs 0.8/day)
- no harder to set up (39 vs 50 friction)

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
  "incumbent_health": 63,
  "challenger_health": 90,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 39
}
```

### davepoon/buildwithclaude → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 13.24x the stars (50,028 vs 3,778)
- 10.03x the star velocity (58.2/day vs 5.8/day)
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
  "challenger_health": 79,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 32
}
```

### fatwang2/search2ai → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 9.56x the stars (12,299 vs 1,286)
- 992.00x the star velocity (49.6/day vs 0.0/day)
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
  "challenger_health": 74,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 32
}
```

### future-agi/future-agi → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 5.38x the stars (12,299 vs 2,288)
- 22.55x the star velocity (49.6/day vs 2.2/day)
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
  "challenger_health": 74,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### giuseppe-trisciuoglio/developer-kit → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 134.48x the stars (50,028 vs 372)
- 291.00x the star velocity (58.2/day vs 0.2/day)
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
  "challenger_health": 79,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 32
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 28.94x the stars (12,299 vs 425)
- 49.60x the star velocity (49.6/day vs 1.0/day)
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
  "challenger_health": 74,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 32
}
```

### jacobaraujo7/remote_pi → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 49.12x the stars (24,512 vs 499)
- 69.67x the star velocity (83.6/day vs 1.2/day)
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
  "challenger_health": 80,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### jtydhr88/comfyui-custom-node-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 156.34x the stars (50,028 vs 320)
- 291.00x the star velocity (58.2/day vs 0.2/day)
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
  "challenger_health": 79,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 32
}
```

### linxidnju/OpenTag → microsoft/TokenEconomizer

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 15.64x the stars (7,819 vs 500)
- 6684.00x the star velocity (334.2/day vs 0.0/day)
- no harder to set up (36 vs 45 friction)

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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "session-persistence"
  ],
  "incumbent_health": 41,
  "challenger_health": 84,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 36
}
```

### michaelshimeles/rstack → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 22.49x the stars (34,403 vs 1,530)
- 8.92x the star velocity (23.2/day vs 2.6/day)
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
  "incumbent_health": 52,
  "challenger_health": 70,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### oomol-lab/open-connector → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 49.01x the stars (307,529 vs 6,275)
- 135.17x the star velocity (811.0/day vs 6.0/day)
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

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 159.01x the stars (155,990 vs 981)
- 5760.00x the star velocity (288.0/day vs 0.0/day)
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
- 54.71x the stars (24,512 vs 448)
- 13.93x the star velocity (83.6/day vs 6.0/day)
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
  "challenger_health": 80,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### tonhowtf/omniget → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 11.68x the stars (169,449 vs 14,509)
- 16.03x the star velocity (202.0/day vs 12.6/day)
- no harder to set up (1 vs 14 friction)

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
  "incumbent_health": 66,
  "challenger_health": 96,
  "incumbent_setup_score": 14,
  "challenger_setup_score": 1
}
```

### wenfxl/openai-cpa → sickn33/agentic-awesome-skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 35.61x the stars (50,028 vs 1,405)
- 264.55x the star velocity (58.2/day vs 0.2/day)
- no harder to set up (32 vs 57 friction)

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
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics"
  ],
  "incumbent_health": 54,
  "challenger_health": 79,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 4.22x the stars (12,299 vs 2,913)
- 7.75x the star velocity (49.6/day vs 6.4/day)
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
  "challenger_health": 74,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### hkcanan/katmer-code → rohitg00/pro-workflow

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (6/6)
- 6.19x the stars (2,966 vs 479)
- 9.00x the star velocity (1.8/day vs 0.2/day)
- slightly heavier setup (+1 friction, within tolerance)

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
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "security-isolation",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 46,
  "challenger_health": 49,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 49
}
```

### Draculabo/AntigravityManager → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 0.994

Reasons:

- covers 100% of capabilities (7/7)
- 7.94x the stars (20,198 vs 2,545)
- 4.78x the star velocity (38.2/day vs 8.0/day)
- no harder to set up (32 vs 57 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "auto-failover",
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
  "challenger_health": 70,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### AMAP-ML/LongHorizon-Harness → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (8/8)
- 16.20x the stars (30,496 vs 1,882)
- 13.56x the star velocity (24.4/day vs 1.8/day)
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
  "incumbent_health": 57,
  "challenger_health": 70,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 32
}
```

### rsmdt/the-startup → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (4/4)
- 48.05x the stars (28,155 vs 586)
- 22.00x the star velocity (17.6/day vs 0.8/day)
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
  "challenger_health": 67,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### vibeeval/vibecosystem → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.978

Reasons:

- covers 100% of capabilities (5/5)
- 2.72x the stars (1,506 vs 553)
- 8.25x the star velocity (6.6/day vs 0.8/day)
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
  "incumbent_health": 52,
  "challenger_health": 57,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 31
}
```

### callstack/agent-device → getpaseo/paseo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (9/9)
- 4.48x the stars (24,512 vs 5,469)
- 5.97x the star velocity (83.6/day vs 14.0/day)
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
  "challenger_health": 80,
  "incumbent_setup_score": 18,
  "challenger_setup_score": 24
}
```

### grpcer/ownmem → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (4/4)
- 3.52x the stars (1,506 vs 428)
- 16.50x the star velocity (6.6/day vs 0.4/day)
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
  "challenger_health": 57,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 31
}
```

### onehumanbeing/esp32-iphone-agent → paperclipai/paperclip

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (5/5)
- 22.44x the stars (115,360 vs 5,141)
- 8.22x the star velocity (266.2/day vs 32.4/day)
- slightly heavier setup (+9 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "mobile-access",
    "self-hosted"
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
  "incumbent_health": 67,
  "challenger_health": 89,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 45
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.953

Reasons:

- covers 100% of capabilities (4/4)
- 2.44x the stars (1,195 vs 489)
- 44.00x the star velocity (2.2/day vs 0.0/day)
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
- 73.46x the stars (50,028 vs 681)
- 18.19x the star velocity (58.2/day vs 3.2/day)
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
  "incumbent_health": 56,
  "challenger_health": 79,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 32
}
```

### basketikun/chatgpt2api → decolua/9router

- **Source:** automatic (medium confidence)
- **Dominance:** 0.942

Reasons:

- covers 100% of capabilities (4/4)
- 4.69x the stars (32,661 vs 6,967)
- 3.26x the star velocity (40.4/day vs 12.4/day)
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
  "incumbent_health": 55,
  "challenger_health": 68,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 73
}
```

### LeoYeAI/talewell → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.939

Reasons:

- covers 100% of capabilities (5/5)
- 2.74x the stars (1,506 vs 550)
- 132.00x the star velocity (6.6/day vs 0.0/day)
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
  "challenger_health": 57,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 31
}
```

### mark3labs/mcp-go → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 0.928

Reasons:

- covers 100% of capabilities (4/4)
- 2.18x the stars (20,198 vs 9,245)
- 27.29x the star velocity (38.2/day vs 1.4/day)
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
  "challenger_health": 70,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 32
}
```

### umutxyp/Seo-Promt-Master → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.908

Reasons:

- covers 100% of capabilities (4/4)
- 2.54x the stars (1,506 vs 594)
- 3.67x the star velocity (6.6/day vs 1.8/day)
- slightly heavier setup (+3 friction, within tolerance)

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
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 53,
  "challenger_health": 57,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 31
}
```

### ruvnet/metaharness → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.908

Reasons:

- covers 100% of capabilities (6/6)
- 2.00x the stars (1,506 vs 753)
- 6.60x the star velocity (6.6/day vs 1.0/day)
- no harder to set up (31 vs 58 friction)

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
  "incumbent_setup_score": 58,
  "challenger_setup_score": 31
}
```

### okf-memory/okf-agent-memory → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.874

Reasons:

- covers 100% of capabilities (5/5)
- 1.73x the stars (1,506 vs 872)
- 5.50x the star velocity (6.6/day vs 1.2/day)
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
  "incumbent_health": 55,
  "challenger_health": 57,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 31
}
```

### devaccuracy/ledgerforge → aipoch/open-science

- **Source:** automatic (high confidence)
- **Dominance:** 0.843

Reasons:

- covers 100% of capabilities (4/4)
- 16.93x the stars (5,553 vs 328)
- 1.41x the star velocity (4.8/day vs 3.4/day)
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
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "notifications",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 45,
  "challenger_health": 65,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 21
}
```

### oceanbase/powercontext → aoci-spec/aoci-code

- **Source:** automatic (medium confidence)
- **Dominance:** 0.831

Reasons:

- covers 100% of capabilities (4/4)
- 1.56x the stars (2,743 vs 1,756)
- 8.57x the star velocity (164.6/day vs 19.2/day)
- slightly heavier setup (+4 friction, within tolerance)

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
    "auto-failover",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "session-persistence"
  ],
  "incumbent_health": 56,
  "challenger_health": 78,
  "incumbent_setup_score": 69,
  "challenger_setup_score": 73
}
```

### sandbox-quantum/switch → genspark-ai/genoffice

- **Source:** automatic (medium confidence)
- **Dominance:** 0.827

Reasons:

- covers 100% of capabilities (6/6)
- 2.72x the stars (12,677 vs 4,661)
- 2.31x the star velocity (59.6/day vs 25.8/day)
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
  "incumbent_health": 67,
  "challenger_health": 74,
  "incumbent_setup_score": 9,
  "challenger_setup_score": 20
}
```

### Archive228/loopkit → numman-ali/n-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.797

Reasons:

- covers 100% of capabilities (5/5)
- 1.39x the stars (1,052 vs 759)
- 4.00x the star velocity (0.2/day vs 0.0/day)
- no harder to set up (16 vs 19 friction)

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
    "mcp-support",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "incumbent_health": 45,
  "challenger_health": 52,
  "incumbent_setup_score": 19,
  "challenger_setup_score": 16
}
```

### managedcode/dotnet-skills → data-goblin/power-bi-agentic-development

- **Source:** automatic (medium confidence)
- **Dominance:** 0.725

Reasons:

- covers 100% of capabilities (6/6)
- 2.12x the stars (1,101 vs 519)
- 1.67x the star velocity (1.0/day vs 0.6/day)
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
  "challenger_health": 56,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 34
}
```

### phuryn/pm-skills → sickn33/agentic-awesome-skills

- **Source:** automatic (medium confidence)
- **Dominance:** 0.705

Reasons:

- covers 100% of capabilities (4/4)
- 1.77x the stars (50,028 vs 28,193)
- 1.48x the star velocity (58.2/day vs 39.2/day)
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
  "challenger_health": 79,
  "incumbent_setup_score": 27,
  "challenger_setup_score": 32
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
