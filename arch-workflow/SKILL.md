---
name: arch-workflow
description: Architecture planning workflow for ARCH mode and large BUILD tasks. Use when Codex needs to design a cross-module feature, decompose a large change, define module boundaries, create ADR-style decisions, reason about system risks before implementation, or produce a macro plan and micro plan that should be reviewed before coding.
---

# Arch Workflow

## Overview

Use this skill before coding when the task is large, cross-cutting, or rollout-sensitive. In ARCH mode, stop after the micro plan unless the user explicitly asks to continue into implementation.

For reusable planning aids:

- read `references/domain-risks.md` for concrete prompts across all seven risk dimensions
- read `references/adr-template.md` for ADR structure and depth
- read `references/micro-plan-template.md` for task breakdown shape
- run `scripts/render_arch_plan.py` when you want a ready-to-fill architecture skeleton

## Use This Skill For Type L Work

Treat the task as L when one or more of these hold:

- multiple modules or services change together
- data model, migration, or protocol boundaries are involved
- security, financial, or operational risk is material
- observability and rollback design matter as much as the code itself
- requirements imply a new subsystem or a meaningful contract change

## Workflow

### 1. Requirements

Clarify:

- user goal
- stack and versions
- scale, latency, infra, and rollout constraints
- existing system boundaries
- compatibility expectations

### 2. Domain Risks

Answer all seven dimensions:

- Invariants
- Atomicity
- Concurrency
- Side effects
- Trust boundaries
- Observability
- Performance

Keep the analysis concrete. State consequences, not just labels.

### 3. Macro Plan

Produce:

- 3 to 7 modules with one-line ownership boundaries
- build order
- assumptions that would invalidate the plan if false
- one or more ADR entries with decision, context, options, chosen path, tradeoff, and rollback

Do not include filenames, signatures, or implementation detail in the macro plan.

Always pause after the blueprint:

- `Blueprint ready. Does the direction look right?`

Use `references/adr-template.md` when the decision tradeoff is subtle or likely to be revisited.

### 4. Micro Plan

After alignment, break the work into logical units. For each task, specify:

- input
- output
- domain risk addressed
- rollback note
- whether it crosses an atomicity boundary or triggers a side effect

With TDD enabled, split core logic into failing-test and implementation pairs.

Pause after the breakdown:

- `Breakdown ready. Proceed with Phase 1?`

In ARCH mode, stop here.

Use `references/micro-plan-template.md` when the breakdown needs to be crisp and reviewable.

## Assumption Discipline

If a macro-plan assumption is invalidated, return to planning. Do not patch forward on a broken blueprint.

## Status Snapshot

For long workstreams, keep a compact status record with:

- done
- tests
- next
- debt
- rollback point
