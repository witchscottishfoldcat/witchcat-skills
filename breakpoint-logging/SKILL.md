---
name: breakpoint-logging
description: Add targeted diagnostic logs at the places where a human debugger would normally set breakpoints. Use when Codex is asked to instrument code for debugging, trace control flow, inspect state transitions, replace temporary breakpoints with logs, add observability around branches or external calls, or prepare code for debugging in environments where interactive debugging is inconvenient or impossible. This skill should also be treated as a default companion when code changes critical runtime behavior and existing observability is not clearly sufficient.
---

# Breakpoint Logging

## Overview

Use this skill to add logs with breakpoint intent, not blanket noise. Prefer the repository's existing logger, log format, and log levels. Combine this skill with `debug-workflow` when the bug still needs root-cause validation and with `repo-conventions` when the codebase has strict logging patterns.

This is no longer only an explicit-on-demand skill. Treat it as the default companion for BUILD and DEBUG work that changes critical runtime paths unless the codebase already has adequate tracing at those points.

## What This Skill Owns

This skill helps choose where logs belong, what each log should say, and how to keep the signal high.

It does not replace full debugging. If the task is to diagnose the actual cause, use `debug-workflow` first or alongside this skill.

## Placement Rules

Add logs where a debugger breakpoint would reveal important control flow or state:

- function or handler entry when the path is uncertain
- before and after state mutation
- at branch decisions whose outcome matters
- before external calls and after their result or failure
- inside retry, timeout, or fallback paths
- at exception capture points
- at async or queue boundaries where causality is lost
- immediately before early returns that can suppress expected behavior

Do not log every line. The goal is to reconstruct the important path with minimal noise.

For a fuller checklist, read `references/log-placement-rules.md`.

## Message Rules

Each log line should make one debugging question easier to answer:

- Did execution reach this point?
- Which branch was chosen?
- What stable identifiers explain the current state?
- What changed?
- Did the external dependency succeed, fail, or time out?

Prefer structured fields over concatenated prose when the codebase supports structured logging.

For message design, read `references/log-message-rules.md`.

## Safety Rules

- never log passwords, tokens, secrets, raw credentials, session cookies, or private keys
- avoid logging full bodies that may contain PII unless the repo already has an approved redaction path
- prefer ids, counts, status, and bounded summaries over raw payload dumps
- respect existing masking and redaction helpers
- use debug-level logs for temporary tracing when possible
- avoid hot-loop spam; aggregate, sample, or log loop boundaries instead

For safe fields and redaction guidance, read `references/safe-logging-rules.md`.

## Workflow

1. Read the relevant files and identify the debugging question.
2. Mark the smallest set of breakpoint-like positions that would answer that question.
3. Reuse the repository's existing logger, levels, and field naming.
4. Add logs around state transitions, branches, external boundaries, and failures.
5. Avoid noisy logs in hot paths unless sampling or aggregation keeps cost bounded.
6. If the user wants temporary instrumentation, say so in comments or naming only when the codebase already has such a convention.

Default expectation:

- if you change critical runtime behavior, make an explicit log decision
- either add targeted logs at breakpoint-like positions
- or state clearly why the existing observability is already enough

When you want a clean scaffold before instrumenting, run `scripts/render_log_plan.py`.

## Output Expectations

When reporting the work, explain:

- which execution questions the logs answer
- where logs were inserted
- any deliberate omissions to avoid noise or risk
