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

### Archive228/loopkit → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 44.12x the stars (33,351 vs 756)
- 10.25x the star velocity (78.3/day vs 7.6/day)
- no harder to set up (2 vs 19 friction)

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
  "challenger_health": 81,
  "incumbent_setup_score": 19,
  "challenger_setup_score": 2
}
```

### JimLiu/baocut → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 63.05x the stars (33,351 vs 529)
- 12.73x the star velocity (78.3/day vs 6.2/day)
- no harder to set up (2 vs 25 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
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
  "incumbent_health": 45,
  "challenger_health": 81,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### Lampese/codex-switcher → yetone/magpie

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 6.43x the stars (5,667 vs 881)
- 131.70x the star velocity (435.9/day vs 3.3/day)
- no harder to set up (18 vs 36 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "gui-desktop",
    "multi-account-switching",
    "quota-management"
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
  "incumbent_health": 51,
  "challenger_health": 84,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 18
}
```

### LerianStudio/ring → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 125.89x the stars (27,318 vs 217)
- 154.09x the star velocity (98.6/day vs 0.6/day)
- no harder to set up (27 vs 40 friction)

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
    "cross-agent-support",
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 48,
  "challenger_health": 85,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 27
}
```

### MemTensor/MemOS-Cloud-OpenClaw-Plugin → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 79.57x the stars (29,204 vs 367)
- 87.50x the star velocity (130.4/day vs 1.5/day)
- no harder to set up (32 vs 34 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "auto-failover",
    "memory-context",
    "model-routing",
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
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 47,
  "challenger_health": 88,
  "incumbent_setup_score": 34,
  "challenger_setup_score": 32
}
```

### RealZST/HarnessKit → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 73.95x the stars (33,351 vs 451)
- 33.46x the star velocity (78.3/day vs 2.3/day)
- no harder to set up (2 vs 2 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "multi-agent-orchestration",
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
  "challenger_health": 81,
  "incumbent_setup_score": 2,
  "challenger_setup_score": 2
}
```

### anymorph-ai/Claudable → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 8.23x the stars (33,351 vs 4,052)
- 7.98x the star velocity (78.3/day vs 9.8/day)
- no harder to set up (2 vs 44 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
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
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "remote-control",
    "skills-plugins",
    "team-collaboration",
    "worktree-isolation"
  ],
  "incumbent_health": 49,
  "challenger_health": 81,
  "incumbent_setup_score": 44,
  "challenger_setup_score": 2
}
```

### appautomaton/latex-arxiv-SKILL → nexu-io/open-design

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 218.40x the stars (99,811 vs 457)
- 760.64x the star velocity (616.1/day vs 0.8/day)
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

### franklee16/academic-research-skills → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 122.50x the stars (27,318 vs 223)
- 75.86x the star velocity (98.6/day vs 1.3/day)
- no harder to set up (27 vs 37 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "multi-agent-orchestration",
    "skills-plugins"
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
  "incumbent_health": 44,
  "challenger_health": 85,
  "incumbent_setup_score": 37,
  "challenger_setup_score": 27
}
```

### giuseppe-trisciuoglio/developer-kit → OthmanAdi/planning-with-files

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 76.95x the stars (27,318 vs 355)
- 97.64x the star velocity (98.6/day vs 1.0/day)
- no harder to set up (27 vs 66 friction)

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
    "memory-context",
    "multi-agent-orchestration",
    "parallel-execution",
    "security-isolation",
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 46,
  "challenger_health": 85,
  "incumbent_setup_score": 66,
  "challenger_setup_score": 27
}
```

### gotalab/cc-sdd → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 8.99x the stars (33,351 vs 3,708)
- 9.43x the star velocity (78.3/day vs 8.3/day)
- no harder to set up (2 vs 25 friction)

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
  "incumbent_health": 59,
  "challenger_health": 81,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 2
}
```

### isxlan0/Codex_AccountSwitch → yetone/magpie

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 22.49x the stars (5,667 vs 252)
- 419.15x the star velocity (435.9/day vs 1.0/day)
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

### jtydhr88/comfyui-custom-node-skills → NanmiCoder/cc-haha

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (4/4)
- 50.65x the stars (14,892 vs 294)
- 57.51x the star velocity (78.8/day vs 1.4/day)
- no harder to set up (29 vs 50 friction)

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
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "quota-management",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 41,
  "challenger_health": 78,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 29
}
```

### kagisearch/kagimcp → microsoft/mcp

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 6.99x the stars (3,741 vs 535)
- 8.46x the star velocity (6.8/day vs 0.8/day)
- no harder to set up (36 vs 40 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "self-hosted"
  ],
  "challenger_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "self-hosted",
    "skills-plugins"
  ],
  "incumbent_health": 40,
  "challenger_health": 59,
  "incumbent_setup_score": 40,
  "challenger_setup_score": 36
}
```

### kenryu42/cc-safety-net → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 21.11x the stars (33,351 vs 1,580)
- 14.13x the star velocity (78.3/day vs 5.5/day)
- no harder to set up (2 vs 15 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop"
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
  "incumbent_health": 60,
  "challenger_health": 81,
  "incumbent_setup_score": 15,
  "challenger_setup_score": 2
}
```

### max-sixty/worktrunk → stablyai/orca

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 9.72x the stars (86,867 vs 8,939)
- 16.86x the star velocity (425.8/day vs 25.2/day)
- no harder to set up (50 vs 50 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "parallel-execution",
    "worktree-isolation"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "mobile-access",
    "multi-account-switching",
    "multi-agent-orchestration",
    "notifications",
    "parallel-execution",
    "quota-management",
    "remote-control",
    "self-hosted",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 68,
  "challenger_health": 92,
  "incumbent_setup_score": 50,
  "challenger_setup_score": 50
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

### mnemon-dev/mnemon → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (6/6)
- 47.80x the stars (29,204 vs 611)
- 48.83x the star velocity (130.4/day vs 2.7/day)
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
  "incumbent_health": 51,
  "challenger_health": 88,
  "incumbent_setup_score": 64,
  "challenger_setup_score": 32
}
```

### ndycode/codex-multi-auth → yetone/magpie

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 10.61x the stars (5,667 vs 534)
- 184.71x the star velocity (435.9/day vs 2.4/day)
- no harder to set up (18 vs 41 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "api-gateway",
    "cross-agent-support",
    "multi-account-switching"
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
  "incumbent_health": 54,
  "challenger_health": 84,
  "incumbent_setup_score": 41,
  "challenger_setup_score": 18
}
```

### neiii/bridle → iOfficeAI/AionUi

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (3/3)
- 75.80x the stars (33,351 vs 440)
- 50.51x the star velocity (78.3/day vs 1.6/day)
- no harder to set up (2 vs 22 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
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
  "incumbent_health": 48,
  "challenger_health": 81,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 2
}
```

### okf-memory/okf-agent-memory → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 38.58x the stars (29,204 vs 757)
- 5.34x the star velocity (130.4/day vs 24.4/day)
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
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 58,
  "challenger_health": 88,
  "incumbent_setup_score": 45,
  "challenger_setup_score": 32
}
```

### tickernelz/opencode-mem → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (8/8)
- 16.99x the stars (29,204 vs 1,719)
- 20.47x the star velocity (130.4/day vs 6.4/day)
- no harder to set up (32 vs 60 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "gui-desktop",
    "memory-context",
    "model-routing",
    "multi-agent-orchestration",
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
    "model-routing",
    "multi-agent-orchestration",
    "notifications",
    "security-isolation",
    "self-hosted",
    "skills-plugins",
    "team-collaboration"
  ],
  "incumbent_health": 55,
  "challenger_health": 88,
  "incumbent_setup_score": 60,
  "challenger_setup_score": 32
}
```

### vercel-labs/personal-agent-template → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (5/5)
- 61.61x the stars (29,204 vs 474)
- 32.19x the star velocity (130.4/day vs 4.0/day)
- no harder to set up (32 vs 78 friction)

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
  "incumbent_setup_score": 78,
  "challenger_setup_score": 32
}
```

### zilliztech/memsearch → rohitg00/agentmemory

- **Source:** automatic (high confidence)
- **Dominance:** 1.000

Reasons:

- covers 100% of capabilities (7/7)
- 10.72x the stars (29,204 vs 2,725)
- 11.49x the star velocity (130.4/day vs 11.3/day)
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

### LeoYeAI/talewell → eugeniughelbur/obsidian-second-brain

- **Source:** automatic (medium confidence)
- **Dominance:** 0.995

Reasons:

- covers 100% of capabilities (5/5)
- 8.58x the stars (4,691 vs 547)
- 8.41x the star velocity (23.8/day vs 2.8/day)
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
  "incumbent_health": 52,
  "challenger_health": 66,
  "incumbent_setup_score": 23,
  "challenger_setup_score": 24
}
```

### rsmdt/the-startup → OthmanAdi/planning-with-files

- **Source:** automatic (medium confidence)
- **Dominance:** 0.990

Reasons:

- covers 100% of capabilities (4/4)
- 50.22x the stars (27,318 vs 544)
- 76.45x the star velocity (98.6/day vs 1.3/day)
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
    "skills-plugins",
    "worktree-isolation"
  ],
  "incumbent_health": 48,
  "challenger_health": 85,
  "incumbent_setup_score": 25,
  "challenger_setup_score": 27
}
```

### hashicorp/agent-skills → NanmiCoder/cc-haha

- **Source:** automatic (medium confidence)
- **Dominance:** 0.965

Reasons:

- covers 100% of capabilities (3/3)
- 16.83x the stars (14,892 vs 885)
- 29.62x the star velocity (78.8/day vs 2.7/day)
- slightly heavier setup (+7 friction, within tolerance)

Evidence:

```json
{
  "incumbent_capabilities": [
    "cross-agent-support",
    "mcp-support",
    "skills-plugins"
  ],
  "challenger_capabilities": [
    "auto-failover",
    "billing-metering",
    "cross-agent-support",
    "gui-desktop",
    "mcp-support",
    "memory-context",
    "multi-agent-orchestration",
    "quota-management",
    "remote-control",
    "security-isolation",
    "self-hosted",
    "session-persistence",
    "skills-plugins",
    "usage-analytics",
    "worktree-isolation"
  ],
  "incumbent_health": 53,
  "challenger_health": 78,
  "incumbent_setup_score": 22,
  "challenger_setup_score": 29
}
```

### YYH211/Claude-meta-skill → abubakarsiddik31/claude-skills-collection

- **Source:** automatic (high confidence)
- **Dominance:** 0.963

Reasons:

- covers 100% of capabilities (4/4)
- 3.87x the stars (1,090 vs 282)
- 3.72x the star velocity (3.1/day vs 0.8/day)
- no harder to set up (46 vs 58 friction)

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
  "incumbent_health": 42,
  "challenger_health": 53,
  "incumbent_setup_score": 58,
  "challenger_setup_score": 46
}
```

### jessepwj/CCteam-creator → yohey-w/multi-agent-shogun

- **Source:** automatic (high confidence)
- **Dominance:** 0.963

Reasons:

- covers 100% of capabilities (6/6)
- 4.64x the stars (1,423 vs 307)
- 3.72x the star velocity (5.6/day vs 1.5/day)
- no harder to set up (46 vs 57 friction)

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
  "incumbent_health": 39,
  "challenger_health": 52,
  "incumbent_setup_score": 57,
  "challenger_setup_score": 46
}
```

### jacobaraujo7/remote_pi → paperclipai/paperclip

- **Source:** automatic (medium confidence)
- **Dominance:** 0.955

Reasons:

- covers 100% of capabilities (5/5)
- 230.14x the stars (98,271 vs 427)
- 145.88x the star velocity (450.8/day vs 3.1/day)
- slightly heavier setup (+9 friction, within tolerance)

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
  "incumbent_health": 50,
  "challenger_health": 89,
  "incumbent_setup_score": 36,
  "challenger_setup_score": 45
}
```

### Ibrahim-3d/orchestrator-supaconductor → yohey-w/multi-agent-shogun

- **Source:** automatic (high confidence)
- **Dominance:** 0.951

Reasons:

- covers 100% of capabilities (5/5)
- 3.74x the stars (1,423 vs 380)
- 3.38x the star velocity (5.6/day vs 1.6/day)
- no harder to set up (46 vs 72 friction)

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
  "incumbent_health": 48,
  "challenger_health": 52,
  "incumbent_setup_score": 72,
  "challenger_setup_score": 46
}
```

### josstei/maestro-orchestrate → yohey-w/multi-agent-shogun

- **Source:** automatic (high confidence)
- **Dominance:** 0.931

Reasons:

- covers 100% of capabilities (4/4)
- 3.06x the stars (1,423 vs 465)
- 2.88x the star velocity (5.6/day vs 1.9/day)
- no harder to set up (46 vs 51 friction)

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
  "incumbent_setup_score": 51,
  "challenger_setup_score": 46
}
```

### Socialpranker/deepdive → yohey-w/multi-agent-shogun

- **Source:** automatic (high confidence)
- **Dominance:** 0.891

Reasons:

- covers 100% of capabilities (4/4)
- 3.83x the stars (1,423 vs 372)
- 2.08x the star velocity (5.6/day vs 2.7/day)
- no harder to set up (46 vs 51 friction)

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
  "incumbent_health": 52,
  "challenger_health": 52,
  "incumbent_setup_score": 51,
  "challenger_setup_score": 46
}
```

### IBM/mcp → arinspunk/claude-talk-to-figma-mcp

- **Source:** automatic (high confidence)
- **Dominance:** 0.722

Reasons:

- covers 100% of capabilities (3/3)
- 1.62x the stars (666 vs 410)
- 1.64x the star velocity (1.2/day vs 0.7/day)
- no harder to set up (16 vs 48 friction)

Evidence:

```json
{
  "incumbent_capabilities": [
    "agent-runtime",
    "mcp-support",
    "multi-agent-orchestration"
  ],
  "challenger_capabilities": [
    "agent-runtime",
    "cross-agent-support",
    "mcp-support",
    "multi-agent-orchestration",
    "parallel-execution"
  ],
  "incumbent_health": 47,
  "challenger_health": 48,
  "incumbent_setup_score": 48,
  "challenger_setup_score": 16
}
```

### career-ops-hq/career-ops → nexu-io/open-design

- **Source:** automatic (medium confidence)
- **Dominance:** 0.673

Reasons:

- covers 100% of capabilities (5/5)
- 1.35x the stars (99,811 vs 73,682)
- 1.55x the star velocity (616.1/day vs 398.3/day)
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
  "incumbent_health": 90,
  "challenger_health": 95,
  "incumbent_setup_score": 49,
  "challenger_setup_score": 29
}
```

### farion1231/cc-switch → yetone/magpie

- **Source:** human curation
- **Dominance:** 0.000

Reasons:

- magpie covers cc-switch's core job (multi-account / provider switching for Claude Code and Codex) and additionally routes other models through the same agent loop, so it strictly covers the older tool's feature set.

Evidence:

```json
{
  "manual": true,
  "note": "magpie covers cc-switch's core job (multi-account / provider switching for Claude Code and Codex) and additionally routes other models through the same agent loop, so it strictly covers the older tool's feature set."
}
```

## The canonical example

**`magpie` retires `cc-switch`.** Both manage multiple accounts and providers for Claude Code and Codex. `cc-switch` is enormously popular and still actively maintained — but `magpie` covers the same ground *and* routes other models through the same agent loop, so it strictly covers the older tool's feature set. The elimination is recorded as **manual**, because a human read both READMEs and made the call; the automatic rules then keep it consistent on later runs.

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
