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
- 64.04x the stars (20,620 vs 322)
- 1400.00x the star velocity (70.0/day vs 0.0/day)
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
  "challenger_health": 77,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 32
}
```

### CopilotKit/OpenBot → affaan-m/ECC

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (9/9)
- 22.65x the stars (311,583 vs 13,754)
- 5.03x the star velocity (588.0/day vs 116.8/day)
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
  "incumbent_health": 83,
  "challenger_health": 89,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 57
}
```

### Draculabo/AntigravityManager → jlcodes99/cockpit-tools

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 7.90x the stars (20,620 vs 2,609)
- 7.78x the star velocity (70.0/day vs 9.0/day)
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
  "incumbent_health": 56,
  "challenger_health": 77,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 32
}
```

### Ibrahim-3d/orchestrator-supaconductor → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 89.96x the stars (34,544 vs 384)
- 452.00x the star velocity (22.6/day vs 0.0/day)
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
- 44.97x the stars (42,408 vs 943)
- 275.78x the star velocity (496.4/day vs 1.8/day)
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
  "incumbent_health": 49,
  "challenger_health": 92,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 11
}
```

### SethGammon/Citadel → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 36.75x the stars (34,544 vs 940)
- 56.50x the star velocity (22.6/day vs 0.4/day)
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
- 8.94x the stars (3,023 vs 338)
- 35.75x the star velocity (28.6/day vs 0.8/day)
- no harder to set up (30 vs 40 friction)

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
  "incumbent_health": 51,
  "challenger_health": 65,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 30
}
```

### automagik-si/genie → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 97.86x the stars (34,544 vs 353)
- 452.00x the star velocity (22.6/day vs 0.0/day)
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

### caveman-ai/caveman-code → getpaseo/paseo

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 26.99x the stars (25,906 vs 960)
- 60.44x the star velocity (249.0/day vs 4.1/day)
- no harder to set up (24 vs 27 friction)

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
  "incumbent_health": 55,
  "challenger_health": 87,
  "incumbent_setup_score": 27,
  "challenger_setup_score": 24
}
```

### darrenhinde/OpenAgentsControl → garrytan/gstack

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 28.60x the stars (142,786 vs 4,993)
- 57.12x the star velocity (91.4/day vs 1.6/day)
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
  "incumbent_health": 65,
  "challenger_health": 85,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 39
}
```

### devaccuracy/ledgerforge → aipoch/open-science

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 17.45x the stars (5,583 vs 320)
- 5.33x the star velocity (4.8/day vs 0.9/day)
- no harder to set up (12 vs 52 friction)

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
    "session-persistence",
    "skills-plugins"
  ],
  "incumbent_health": 44,
  "challenger_health": 66,
  "incumbent_setup_score": 52,
  "challenger_setup_score": 12
}
```

### fatwang2/search2ai → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 9.77x the stars (12,580 vs 1,287)
- 246.00x the star velocity (49.2/day vs 0.2/day)
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
  "incumbent_health": 51,
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
- 5.47x the stars (12,580 vs 2,301)
- 16.40x the star velocity (49.2/day vs 3.0/day)
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

### giuseppe-trisciuoglio/developer-kit → abubakarsiddik31/claude-skills-collection

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 3.06x the stars (1,139 vs 372)
- 20.00x the star velocity (1.0/day vs 0.0/day)
- no harder to set up (46 vs 66 friction)

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
  "incumbent_health": 44,
  "challenger_health": 54,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 46
}
```

### harishkotra/agent-office → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 29.26x the stars (12,580 vs 430)
- 123.00x the star velocity (49.2/day vs 0.4/day)
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
- 50.70x the stars (25,906 vs 511)
- 138.33x the star velocity (249.0/day vs 1.8/day)
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
  "incumbent_health": 51,
  "challenger_health": 87,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 24
}
```

### kagisearch/kagimcp → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 21.73x the stars (12,580 vs 579)
- 49.20x the star velocity (49.2/day vs 1.0/day)
- no harder to set up (32 vs 46 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "model-routing",
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
  "incumbent_health": 48,
  "challenger_health": 74,
  "incumbent_setup_score": 46,
  "challenger_setup_score": 32
}
```

### linxidnju/OpenTag → microsoft/TokenEconomizer

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 16.25x the stars (8,155 vs 502)
- 110.00x the star velocity (44.0/day vs 0.4/day)
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
  "challenger_health": 69,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 36
}
```

### mnemon-dev/mnemon → kajisho5/ffmpeg-skill

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 15.69x the stars (11,755 vs 749)
- 142.12x the star velocity (454.8/day vs 3.2/day)
- no harder to set up (50 vs 64 friction)

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
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins",
    "voice-input"
  ],
  "incumbent_health": 52,
  "challenger_health": 90,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 50
}
```

### routatic/proxy → farion1231/cc-switch

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 160.34x the stars (157,619 vs 983)
- 658.00x the star velocity (263.2/day vs 0.4/day)
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
- 55.95x the stars (25,906 vs 463)
- 138.33x the star velocity (249.0/day vs 1.8/day)
- no harder to set up (24 vs 27 friction)

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
  "challenger_health": 87,
  "incumbent_setup_score": 27,
  "challenger_setup_score": 24
}
```

### wenfxl/openai-cpa → garrytan/gstack

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 101.70x the stars (142,786 vs 1,404)
- 1523.33x the star velocity (91.4/day vs 0.1/day)
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
  "incumbent_health": 52,
  "challenger_health": 85,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 39
}
```

### zilliztech/memsearch → TencentCloud/Octop

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 4.26x the stars (12,580 vs 2,950)
- 8.20x the star velocity (49.2/day vs 6.0/day)
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

### rsmdt/the-startup → pedrohcgs/claude-code-my-workflow

- **Source:** automatic (high confidence)
- **Dominance:** 0.997

Reasons:

- covers 100% of capabilities (4/4)
- 2.96x the stars (1,740 vs 588)
- 11.00x the star velocity (2.2/day vs 0.2/day)
- no harder to set up (8 vs 25 friction)

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
  "incumbent_health": 48,
  "challenger_health": 60,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 8
}
```

### findavoulot1973/Blender-AI-MCP-Suite → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (4/4)
- 3.08x the stars (1,527 vs 495)
- 68.00x the star velocity (3.4/day vs 0.0/day)
- slightly heavier setup (+1 friction, within tolerance)

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
  "incumbent_health": 49,
  "challenger_health": 54,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 31
}
```

### hkcanan/katmer-code → rohitg00/pro-workflow

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (6/6)
- 6.19x the stars (2,972 vs 480)
- 5.00x the star velocity (1.0/day vs 0.2/day)
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

### AMAP-ML/LongHorizon-Harness → rohitg00/agentmemory

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (8/8)
- 16.16x the stars (30,621 vs 1,895)
- 11.37x the star velocity (18.2/day vs 1.6/day)
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
  "challenger_health": 69,
  "incumbent_setup_score": 30,
  "challenger_setup_score": 32
}
```

### oceanbase/powercontext → kajisho5/ffmpeg-skill

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (5/5)
- 6.23x the stars (11,755 vs 1,888)
- 21.45x the star velocity (454.8/day vs 21.2/day)
- slightly heavier setup (+2 friction, within tolerance)

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
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins",
    "voice-input"
  ],
  "incumbent_health": 59,
  "challenger_health": 90,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 50
}
```

### vibeeval/vibecosystem → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.981

Reasons:

- covers 100% of capabilities (5/5)
- 2.76x the stars (1,527 vs 554)
- 68.00x the star velocity (3.4/day vs 0.0/day)
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
  "incumbent_health": 51,
  "challenger_health": 54,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 31
}
```

### okf-memory/okf-agent-memory → kajisho5/ffmpeg-skill

- **Source:** automatic (medium confidence)
- **Dominance:** 0.975

Reasons:

- covers 100% of capabilities (5/5)
- 13.42x the stars (11,755 vs 876)
- 454.80x the star velocity (454.8/day vs 1.0/day)
- slightly heavier setup (+5 friction, within tolerance)

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
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins",
    "voice-input"
  ],
  "incumbent_health": 54,
  "challenger_health": 90,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 50
}
```

### MemTensor/memmy-agent → HKUDS/DeepTutor

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (7/7)
- 26.96x the stars (63,686 vs 2,362)
- 16.33x the star velocity (440.8/day vs 27.0/day)
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
    "model-routing",
    "team-collaboration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "model-routing",
    "multi-account-switching",
    "multi-agent-orchestration",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "team-collaboration",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 61,
  "challenger_health": 90,
  "incumbent_setup_score": 42,
  "challenger_setup_score": 48
}
```

### callstack/agent-device → getpaseo/paseo

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (9/9)
- 4.69x the stars (25,906 vs 5,528)
- 24.90x the star velocity (249.0/day vs 10.0/day)
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
  "incumbent_health": 64,
  "challenger_health": 87,
  "incumbent_setup_score": 18,
  "challenger_setup_score": 24
}
```

### grpcer/ownmem → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.970

Reasons:

- covers 100% of capabilities (4/4)
- 3.56x the stars (1,527 vs 429)
- 17.00x the star velocity (3.4/day vs 0.2/day)
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
  "challenger_health": 54,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 31
}
```

### josstei/maestro-orchestrate → hoangsonww/Claude-Code-Agent-Monitor

- **Source:** automatic (high confidence)
- **Dominance:** 0.956

Reasons:

- covers 100% of capabilities (4/4)
- 2.48x the stars (1,218 vs 492)
- 6.67x the star velocity (4.0/day vs 0.6/day)
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
  "challenger_health": 56,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 30
}
```

### LeoYeAI/talewell → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.943

Reasons:

- covers 100% of capabilities (5/5)
- 2.78x the stars (1,527 vs 549)
- 68.00x the star velocity (3.4/day vs 0.0/day)
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
  "challenger_health": 54,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 31
}
```

### johannesjo/parallel-code → paperclipai/paperclip

- **Source:** automatic (medium confidence)
- **Dominance:** 0.940

Reasons:

- covers 100% of capabilities (7/7)
- 106.25x the stars (117,511 vs 1,106)
- 567.00x the star velocity (340.2/day vs 0.6/day)
- slightly heavier setup (+12 friction, within tolerance)

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
  "incumbent_setup_score": 33,
  "challenger_setup_score": 45
}
```

### jtydhr88/comfyui-custom-node-skills → WenyuChiou/ai-research-skills

- **Source:** automatic (high confidence)
- **Dominance:** 0.927

Reasons:

- covers 100% of capabilities (4/4)
- 2.17x the stars (702 vs 323)
- 7.00x the star velocity (2.8/day vs 0.4/day)
- no harder to set up (22 vs 50 friction)

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
    "multi-agent-orchestration",
    "skills-plugins"
  ],
  "incumbent_health": 41,
  "challenger_health": 56,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 22
}
```

### michaelshimeles/rstack → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 0.926

Reasons:

- covers 100% of capabilities (5/5)
- 21.90x the stars (34,544 vs 1,577)
- 2.76x the star velocity (22.6/day vs 8.2/day)
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
  "incumbent_health": 55,
  "challenger_health": 70,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### google/artemis → msitarzewski/agency-agents

- **Source:** automatic (high confidence)
- **Dominance:** 0.914

Reasons:

- covers 100% of capabilities (6/6)
- 9.37x the stars (170,558 vs 18,203)
- 2.51x the star velocity (160.4/day vs 64.0/day)
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
  "incumbent_health": 68,
  "challenger_health": 96,
  "incumbent_setup_score": 56,
  "challenger_setup_score": 1
}
```

### Leonxlnx/earshot → kajisho5/ffmpeg-skill

- **Source:** automatic (medium confidence)
- **Dominance:** 0.901

Reasons:

- covers 100% of capabilities (4/4)
- 1.98x the stars (11,755 vs 5,931)
- 5.44x the star velocity (454.8/day vs 83.6/day)
- slightly heavier setup (+1 friction, within tolerance)

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
    "api-gateway",
    "auto-failover",
    "cross-agent-support",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "skills-plugins",
    "voice-input"
  ],
  "incumbent_health": 73,
  "challenger_health": 90,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 50
}
```

### umutxyp/Seo-Promt-Master → huytieu/COG-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.857

Reasons:

- covers 100% of capabilities (4/4)
- 2.54x the stars (1,527 vs 602)
- 2.43x the star velocity (3.4/day vs 1.4/day)
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
  "incumbent_health": 54,
  "challenger_health": 54,
  "incumbent_setup_score": 28,
  "challenger_setup_score": 31
}
```

### managedcode/dotnet-skills → data-goblin/power-bi-agentic-development

- **Source:** automatic (medium confidence)
- **Dominance:** 0.823

Reasons:

- covers 100% of capabilities (6/6)
- 2.13x the stars (1,116 vs 524)
- 3.67x the star velocity (2.2/day vs 0.6/day)
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
  "incumbent_health": 55,
  "challenger_health": 57,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 34
}
```

### ruvnet/metaharness → huytieu/COG-second-brain

- **Source:** automatic (high confidence)
- **Dominance:** 0.818

Reasons:

- covers 100% of capabilities (6/6)
- 2.00x the stars (1,527 vs 765)
- 2.43x the star velocity (3.4/day vs 1.4/day)
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
  "incumbent_health": 53,
  "challenger_health": 54,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 31
}
```

### BennyKok/omg.dev → greenfield-inc/Pane

- **Source:** automatic (medium confidence)
- **Dominance:** 0.796

Reasons:

- covers 100% of capabilities (8/8)
- 1.22x the stars (685 vs 560)
- 56.00x the star velocity (2.8/day vs 0.0/day)
- no harder to set up (29 vs 31 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mobile-access",
    "multi-agent-orchestration",
    "notifications",
    "remote-control",
    "self-hosted"
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
  "incumbent_health": 50,
  "challenger_health": 56,
  "incumbent_setup_score": 31,
  "challenger_setup_score": 29
}
```

### kaomei/stickman-video-director → milind-soni/OpenMausBot

- **Source:** automatic (medium confidence)
- **Dominance:** 0.787

Reasons:

- covers 100% of capabilities (6/6)
- 3.28x the stars (28,430 vs 8,660)
- 1.41x the star velocity (349.8/day vs 248.6/day)
- slightly heavier setup (+11 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "multi-agent-orchestration",
    "self-hosted"
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
  "incumbent_health": 88,
  "challenger_health": 88,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 34
}
```

### vb2250158/RabiRoute → greenfield-inc/Pane

- **Source:** automatic (medium confidence)
- **Dominance:** 0.769

Reasons:

- covers 100% of capabilities (7/7)
- 1.39x the stars (685 vs 494)
- 14.00x the star velocity (2.8/day vs 0.2/day)
- slightly heavier setup (+11 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "mobile-access",
    "notifications",
    "remote-control",
    "self-hosted"
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
  "incumbent_health": 56,
  "challenger_health": 56,
  "incumbent_setup_score": 18,
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
