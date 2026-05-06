---
name: build-workflow
description: Feature development and implementation workflow for BUILD mode. Use when Codex needs to add a feature, change behavior, refactor with user-visible impact, implement an endpoint, update business logic, or make a medium-sized code change that should follow requirements clarification, risk analysis, micro planning, TDD-first execution, and a final review.
---

# Build Workflow

## Overview

Use this skill to keep BUILD work proportional and disciplined. If the task expands into architecture work, load `arch-workflow` first. If naming or file-shape decisions matter, also load `repo-conventions`. Before handing off, run `engineering-review`.

Targeted logging is a default expectation for critical runtime changes. When code affects state mutation, external calls, important branches, retries, exception paths, or async boundaries, also apply `breakpoint-logging` unless the codebase already has sufficient observability there.

For reusable output scaffolds:

- read `references/m-task-risk-scan.md` for a concise M-task risk sweep
- read `references/micro-plan-template.md` for micro-plan shape
- run `scripts/render_build_plan.py` when you want a ready-to-fill plan skeleton

## Classify First

- Type S: explanation, API usage, or a no-code answer. Respond directly and skip this workflow.
- Type M: small or medium implementation, local bug fix, or contained refactor. Use the full workflow below.
- Type L: cross-module, architecture-sensitive, or rollout-sensitive change. Stop and switch to `arch-workflow` before implementation.

Do not force architecture ceremony onto clearly M-sized tasks.

## Workflow

### 1. Requirements

Clarify:

- user goal
- stack and relevant versions
- constraints such as latency, scale, infra, or compatibility
- existing code style and boundaries

Ask only if the missing information is truly blocking or risky.

### 2. Domain Risks

For M tasks, scan these dimensions and answer only what matters:

- Invariants: what must not break, and what happens if it does
- Atomicity: which changes must succeed or fail together
- Concurrency: who can race on the same resource
- Side effects: emails, payments, external calls, writes with no easy rollback
- Trust boundaries: untrusted input, authz, masking, validation
- Observability: what could fail silently without logs, metrics, or traces
- Performance: hot paths, repeated I/O, unbounded loops, memory growth

Keep the output short, but make the real risks explicit.

If observability is part of the risk, treat breakpoint-style logging as a default mitigation candidate rather than an optional enhancement.

### 3. Micro Plan

Break the work into logical units with:

- input
- output
- risk addressed
- rollback note

When TDD is on, split core logic into a failing-test task followed by an implementation task.

Pause before implementation when the environment or user preference requires confirmation.

Use `references/micro-plan-template.md` when a clean output skeleton will save time or reduce drift.

### 4. Implementation

Execute one logical unit at a time.

Rules:

- preserve public interfaces unless the user asked for a break
- keep state changes explicit
- for critical runtime paths, either add targeted logs or explicitly justify why existing observability is already sufficient
- add concise comments only where the logic is non-obvious
- do not silently increase complexity
- stop immediately on a security red flag

By default, check these locations for logs:

- before and after meaningful state mutation
- around external I/O boundaries
- at important branch decisions
- at retries, timeouts, fallbacks, and exception paths
- at async handoff boundaries

Use concise execution logs such as:

- `[DONE] Task 1.1 - failing test added`
- `[DONE] Task 1.2 - implementation completed`

### 5. Review

Before finishing, verify:

- tests relevant to the change pass
- invariants still hold
- observability is sufficient on critical paths, including targeted logs where runtime tracing would otherwise require breakpoints
- performance impact is acceptable
- the implementation still matches the plan

If the plan no longer fits, update the plan or revert the divergence. Do not hand off a drifted design without explanation.

## TDD Rule

TDD is on by default for core logic.

Exemptions:

- config-only changes
- scaffolding
- migrations
- structural-only refactors with no behavior change

For borderline cases, read `references/tdd-boundaries.md`.

## Security Block

If you detect a risky pattern, stop and emit:

- `[SECURITY BLOCK]`
- `Detected: <risk type>`
- `Unsafe: <pattern>`
- `Safe: <safer alternative>`
