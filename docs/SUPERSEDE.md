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
- 57.97x the stars (18,955 vs 327)
- 812.00x the star velocity (40.6/day vs 0.0/day)
- no harder to set up (20 vs 41 friction)

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
    "parallel-execution",
    "provider-aggregation",
    "quota-management",
    "security-isolation",
    "usage-analytics"
  ],
  "incumbent_health": 45,
  "challenger_health": 72,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 20
}
```

### BennyKok/omg.dev → omnigent-ai/omnigent

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 19.71x the stars (10,800 vs 548)
- 102.00x the star velocity (20.4/day vs 0.2/day)
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
  "challenger_health": 66,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 25
}
```

### Ibrahim-3d/orchestrator-supaconductor → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 72.03x the stars (27,443 vs 381)
- 352.00x the star velocity (17.6/day vs 0.0/day)
- no harder to set up (27 vs 72 friction)

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
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 47,
  "challenger_health": 69,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 27
}
```

### Othmane-Khadri/YALC-the-GTM-operating-system → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 876.85x the stars (278,839 vs 318)
- 3192.00x the star velocity (638.4/day vs 0.2/day)
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

### Pimzino/spec-workflow-mcp → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 64.80x the stars (278,839 vs 4,303)
- 3192.00x the star velocity (638.4/day vs 0.2/day)
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

### Waishnav/devspace → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 3.98x the stars (20,837 vs 5,238)
- 20.43x the star velocity (122.6/day vs 6.0/day)
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
  "incumbent_health": 58,
  "challenger_health": 86,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 24
}
```

### YYH211/Claude-meta-skill → thedivergentai/Game-Dev-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 3.01x the stars (850 vs 282)
- 68.60x the star velocity (3.4/day vs 0.0/day)
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
  "challenger_health": 58,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 21
}
```

### appautomaton/latex-arxiv-SKILL → nexu-io/open-design

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 217.78x the stars (101,051 vs 464)
- 152.33x the star velocity (182.8/day vs 1.2/day)
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
- 5.60x the stars (27,443 vs 4,903)
- 11.00x the star velocity (17.6/day vs 1.6/day)
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
  "incumbent_health": 63,
  "challenger_health": 69,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 27
}
```

### deepagent-ltd/deepagent-code → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (12/12)
- 233.50x the stars (101,804 vs 436)
- 11080.00x the star velocity (554.0/day vs 0.0/day)
- no harder to set up (45 vs 56 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
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
  "incumbent_health": 48,
  "challenger_health": 89,
  "incumbent_setup_score": 56,
  "challenger_setup_score": 45
}
```

### devaccuracy/ledgerforge → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 390.18x the stars (159,974 vs 410)
- 118.17x the star velocity (310.8/day vs 2.6/day)
- no harder to set up (1 vs 52 friction)

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
  "incumbent_health": 50,
  "challenger_health": 98,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 1
}
```

### future-agi/future-agi → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 4.31x the stars (9,260 vs 2,147)
- 64.94x the star velocity (220.8/day vs 3.4/day)
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
  "challenger_health": 87,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### glebis/claude-skills → XiaomiMiMo/MiMo-Code

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 34.92x the stars (13,653 vs 391)
- 144.00x the star velocity (7.2/day vs 0.0/day)
- no harder to set up (21 vs 30 friction)

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
    "voice-input"
  ],
  "incumbent_health": 51,
  "challenger_health": 64,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 21
}
```

### grpcer/ownmem → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 11.16x the stars (4,756 vs 426)
- 17.00x the star velocity (10.2/day vs 0.6/day)
- no harder to set up (24 vs 25 friction)

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
  "incumbent_health": 56,
  "challenger_health": 62,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 24
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 26.92x the stars (9,260 vs 344)
- 84.92x the star velocity (220.8/day vs 2.6/day)
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
  "incumbent_health": 45,
  "challenger_health": 87,
  "incumbent_setup_score": 75,
  "challenger_setup_score": 32
}
```

### hex/claude-council → rlaope/oh-my-hermes

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 3.85x the stars (3,365 vs 873)
- 6.55x the star velocity (26.2/day vs 4.0/day)
- no harder to set up (13 vs 42 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "multi-agent-orchestration",
    "parallel-execution"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "parallel-execution",
    "worktree-isolation"
  ],
  "incumbent_health": 52,
  "challenger_health": 67,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 13
}
```

### hkqr/my-free-code → nexu-io/open-design

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 161.68x the stars (101,051 vs 625)
- 457.00x the star velocity (182.8/day vs 0.4/day)
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
  "incumbent_health": 49,
  "challenger_health": 95,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 29
}
```

### isxlan0/Codex_AccountSwitch → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 75.52x the stars (18,955 vs 251)
- 812.00x the star velocity (40.6/day vs 0.0/day)
- no harder to set up (20 vs 46 friction)

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
  "challenger_health": 72,
  "incumbent_setup_score": 46,
  "challenger_setup_score": 20
}
```

### kerim0x1/bettercode → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 583.85x the stars (159,974 vs 274)
- 6216.00x the star velocity (310.8/day vs 0.0/day)
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
  "incumbent_health": 53,
  "challenger_health": 98,
  "incumbent_setup_score": 24,
  "challenger_setup_score": 1
}
```

### matrixorigin/memoria → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 455.62x the stars (278,839 vs 612)
- 1596.00x the star velocity (638.4/day vs 0.4/day)
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

### maximhq/bifrost → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 16.42x the stars (144,070 vs 8,774)
- 29.99x the star velocity (458.6/day vs 15.3/day)
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
  "incumbent_health": 62,
  "challenger_health": 93,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 23
}
```

### oomol-lab/open-connector → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 46.38x the stars (278,839 vs 6,012)
- 79.80x the star velocity (638.4/day vs 8.0/day)
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

### rsmdt/the-startup → EverMind-AI/Raven

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 9.57x the stars (5,429 vs 567)
- 10.40x the star velocity (20.8/day vs 2.0/day)
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
  "incumbent_health": 49,
  "challenger_health": 67,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 13
}
```

### spences10/mcp-omnisearch → superdesigndev/treg

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 14.82x the stars (5,277 vs 356)
- 123.61x the star velocity (75.4/day vs 0.6/day)
- no harder to set up (21 vs 31 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "mcp-support",
    "model-routing",
    "security-isolation",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "auto-failover",
    "billing-metering",
    "mcp-support",
    "model-routing",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins"
  ],
  "incumbent_health": 53,
  "challenger_health": 77,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 21
}
```

### tigerless-labs/agent-memory → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 77.95x the stars (278,839 vs 3,577)
- 16.80x the star velocity (638.4/day vs 38.0/day)
- no harder to set up (57 vs 69 friction)

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
  "incumbent_health": 61,
  "challenger_health": 89,
  "incumbent_setup_score": 69,
  "challenger_setup_score": 57
}
```

### wenfxl/openai-cpa → milind-soni/OpenMausBot

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 3.43x the stars (4,821 vs 1,404)
- 1530.40x the star velocity (76.5/day vs 0.0/day)
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
    "voice-input"
  ],
  "incumbent_health": 49,
  "challenger_health": 76,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 28
}
```

### yc-software/qm → paperclipai/paperclip

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (10/10)
- 6.61x the stars (101,804 vs 15,408)
- 72.89x the star velocity (554.0/day vs 7.6/day)
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
  "incumbent_health": 56,
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
- 3.38x the stars (9,260 vs 2,743)
- 78.86x the star velocity (220.8/day vs 2.8/day)
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
  "challenger_health": 87,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 32
}
```

### LeoYeAI/talewell → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (5/5)
- 8.68x the stars (4,756 vs 548)
- 51.00x the star velocity (10.2/day vs 0.2/day)
- slightly heavier setup (+1 friction, within tolerance)

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
  "incumbent_health": 50,
  "challenger_health": 62,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 24
}
```

### SethGammon/Citadel → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (6/6)
- 29.70x the stars (27,443 vs 924)
- 88.00x the star velocity (17.6/day vs 0.2/day)
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
  "challenger_health": 69,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### jtydhr88/comfyui-custom-node-skills → thedivergentai/Game-Dev-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.989

Reasons:

- covers 100% of capabilities (4/4)
- 2.85x the stars (850 vs 298)
- 5.72x the star velocity (3.4/day vs 0.6/day)
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
  "incumbent_health": 41,
  "challenger_health": 58,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 21
}
```

### nwiizo/tfmcp → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (5/5)
- 747.56x the stars (278,839 vs 373)
- 12768.00x the star velocity (638.4/day vs 0.0/day)
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
  "incumbent_setup_score": 52,
  "challenger_setup_score": 57
}
```

### 0xK3vin/MegaMemory → Gentleman-Programming/engram

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (5/5)
- 9.92x the stars (7,180 vs 724)
- 15.80x the star velocity (15.8/day vs 1.0/day)
- slightly heavier setup (+6 friction, within tolerance)

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
  "challenger_health": 62,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 34
}
```

### internet-court/internet-court-skill → alibaba/open-code-review

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (4/4)
- 6.99x the stars (47,061 vs 6,736)
- 10.40x the star velocity (455.6/day vs 43.8/day)
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
  "incumbent_health": 60,
  "challenger_health": 89,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 37
}
```

### CopilotKit/OpenBot → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (7/7)
- 43.14x the stars (278,839 vs 6,464)
- 14.92x the star velocity (638.4/day vs 42.8/day)
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
  "incumbent_health": 68,
  "challenger_health": 89,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 57
}
```

### automagik-dev/genie → maxritter/pilot-shell

- **Source:** automatic (medium confidence)
- **Dominance:** 0.960

Reasons:

- covers 100% of capabilities (6/6)
- 6.03x the stars (2,088 vs 346)
- 12.00x the star velocity (0.6/day vs 0.0/day)
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
  "challenger_health": 61,
  "incumbent_setup_score": 4,
  "challenger_setup_score": 12
}
```

### hkcanan/katmer-code → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (6/6)
- 588.27x the stars (278,839 vs 474)
- 12768.00x the star velocity (638.4/day vs 0.0/day)
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
  "incumbent_health": 49,
  "challenger_health": 89,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 57
}
```

### Ryze-AI-Adgent/open-seo-mcp-skills → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (4/4)
- 52.57x the stars (278,839 vs 5,304)
- 4.61x the star velocity (638.4/day vs 138.4/day)
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

### mnemon-dev/mnemon → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.952

Reasons:

- covers 100% of capabilities (6/6)
- 7.56x the stars (4,756 vs 629)
- 3.40x the star velocity (10.2/day vs 3.0/day)
- no harder to set up (24 vs 64 friction)

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
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "quota-management",
    "security-isolation",
    "skills-plugins"
  ],
  "incumbent_health": 51,
  "challenger_health": 62,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 24
}
```

### giuseppe-trisciuoglio/developer-kit → thedivergentai/Game-Dev-Agentic-Skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.947

Reasons:

- covers 100% of capabilities (5/5)
- 2.37x the stars (850 vs 358)
- 8.57x the star velocity (3.4/day vs 0.4/day)
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
  "incumbent_health": 44,
  "challenger_health": 58,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 21
}
```

### linxidnju/OpenTag → affaan-m/ECC

- **Source:** automatic (medium confidence)
- **Dominance:** 0.940

Reasons:

- covers 100% of capabilities (4/4)
- 555.46x the stars (278,839 vs 502)
- 12768.00x the star velocity (638.4/day vs 0.0/day)
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
  "incumbent_setup_score": 45,
  "challenger_setup_score": 57
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.939

Reasons:

- covers 100% of capabilities (4/4)
- 2.30x the stars (1,073 vs 467)
- 9.50x the star velocity (3.8/day vs 0.4/day)
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
  "incumbent_health": 50,
  "challenger_health": 55,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 30
}
```

### lanes-sh/app → maxritter/pilot-shell

- **Source:** automatic (high confidence)
- **Dominance:** 0.937

Reasons:

- covers 100% of capabilities (7/7)
- 7.62x the stars (2,088 vs 274)
- 3.00x the star velocity (0.6/day vs 0.2/day)
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
  "challenger_health": 61,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 12
}
```

### okf-memory/okf-agent-memory → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.916

Reasons:

- covers 100% of capabilities (5/5)
- 6.11x the stars (4,756 vs 778)
- 2.55x the star velocity (10.2/day vs 4.0/day)
- no harder to set up (24 vs 45 friction)

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
  "challenger_health": 62,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 24
}
```

### mindmuxai/brain.md → maxritter/pilot-shell

- **Source:** automatic (medium confidence)
- **Dominance:** 0.907

Reasons:

- covers 100% of capabilities (7/7)
- 3.68x the stars (2,088 vs 567)
- 3.00x the star velocity (0.6/day vs 0.2/day)
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
  "incumbent_health": 51,
  "challenger_health": 61,
  "incumbent_setup_score": 6,
  "challenger_setup_score": 12
}
```

### michaelshimeles/skills → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 0.886

Reasons:

- covers 100% of capabilities (5/5)
- 20.81x the stars (27,443 vs 1,319)
- 2.00x the star velocity (17.6/day vs 8.8/day)
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
  "incumbent_health": 52,
  "challenger_health": 69,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 27
}
```

### tigerless-labs/cost-xray → getpaseo/paseo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.881

Reasons:

- covers 100% of capabilities (5/5)
- 4.26x the stars (20,837 vs 4,888)
- 3.11x the star velocity (122.6/day vs 39.4/day)
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
  "challenger_health": 86,
  "incumbent_setup_score": 12,
  "challenger_setup_score": 24
}
```

### Lling0000/Vibe_coding_guide → maxritter/pilot-shell

- **Source:** automatic (high confidence)
- **Dominance:** 0.850

Reasons:

- covers 100% of capabilities (6/6)
- 8.96x the stars (2,088 vs 233)
- 1.50x the star velocity (0.6/day vs 0.4/day)
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
  "incumbent_health": 40,
  "challenger_health": 61,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 12
}
```

### butterbase-ai/butterbase → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 0.842

Reasons:

- covers 100% of capabilities (8/8)
- 9.45x the stars (29,404 vs 3,112)
- 1.40x the star velocity (29.6/day vs 21.2/day)
- no harder to set up (32 vs 67 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "billing-metering",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
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
    "quota-management",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 58,
  "challenger_health": 70,
  "incumbent_setup_score": 67,
  "challenger_setup_score": 32
}
```

### Socialpranker/deepdive → ruvnet/metaharness

- **Source:** automatic (medium confidence)
- **Dominance:** 0.814

Reasons:

- covers 100% of capabilities (4/4)
- 1.88x the stars (701 vs 373)
- 3.50x the star velocity (1.4/day vs 0.4/day)
- slightly heavier setup (+7 friction, within tolerance)

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
    "mcp-support",
    "model-routing",
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "incumbent_health": 52,
  "challenger_health": 52,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 58
}
```

### career-ops-hq/career-ops → nexu-io/open-design

- **Source:** automatic (medium confidence)
- **Dominance:** 0.677

Reasons:

- covers 100% of capabilities (5/5)
- 1.36x the stars (101,051 vs 74,449)
- 1.58x the star velocity (182.8/day vs 115.4/day)
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
  "incumbent_health": 88,
  "challenger_health": 95,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 29
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
