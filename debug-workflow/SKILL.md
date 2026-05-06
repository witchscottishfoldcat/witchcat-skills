---
name: debug-workflow
description: Root-cause debugging workflow for DEBUG mode. Use when Codex needs to diagnose a bug, production failure, flaky test, regression, data mismatch, performance anomaly, or concurrency issue and must reproduce the problem, trace state transitions, validate the true cause, apply a minimal fix, and add regression coverage instead of guessing.
---

# Debug Workflow

## Overview

Use this skill when the task is diagnosis first and code change second. Do not propose a fix until reproduction and validation have eliminated competing causes.

For reusable checklists:

- read `references/debug-trace-checklist.md` before tracing a stateful bug
- read `references/regression-rules.md` when deciding what regression coverage is enough
- run `scripts/render_debug_report.py` when you want a ready-to-fill debug report skeleton

## Requirements

Capture:

- exact failure symptom
- exact repro path or best-known trigger
- affected environment, branch, dataset, and recent changes
- expected behavior versus actual behavior

If the report is vague, tighten it before editing code.

## Risk Scan

In DEBUG mode, focus on these dimensions first:

- Invariants: what must never break
- Concurrency: races, duplicate writes, lock contention, timing issues
- Trust boundaries: malformed or hostile input, authz gaps, missing validation

Bring in the other dimensions only if the trace shows they matter.

## Debug Loop

Use this structure:

`[DEBUG]`

1. Reproduce: exact steps to trigger the issue
2. Trace: state transitions leading to failure
3. Hypothesis: suspected root cause
4. Validate: how the hypothesis was confirmed and competing causes were ruled out
5. Fix: minimal change that addresses the confirmed cause
6. Regression: test added to prevent recurrence

## Trace Expectations

When relevant, include state snapshots for:

- request parameters
- database state
- cache state
- background job or thread context
- feature flags, time boundaries, and retries

If the system is distributed, note which boundary loses causality.

Use `references/debug-trace-checklist.md` when the state graph is large or crosses process boundaries.

## Validation Rules

- Reproduction must be stable enough to distinguish signal from noise.
- A hypothesis is not validated until it predicts the observed failure and the fix removes that failure.
- If multiple causes remain plausible, keep tracing. Do not patch the first suspicious line.

## Fix Rules

- prefer the smallest fix that addresses the true cause
- preserve backward compatibility unless the bug is caused by a broken contract
- add logging or metrics if the failure could recur silently, and prefer `breakpoint-logging` style targeted logs on the critical path
- add a regression test unless the bug is purely environmental and cannot be sensibly encoded

## If Reproduction Fails

State:

- what was tried
- what evidence exists
- what data is missing
- what instrumentation should be added next
