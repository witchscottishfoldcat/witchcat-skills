---
name: engineering-review
description: Engineering review and final quality gate. Use when Codex is asked to review code, summarize findings from a patch, perform a final implementation check before handoff, or evaluate regression risk, observability, performance, security boundaries, and missing tests. This skill prioritizes findings over summaries.
---

# Engineering Review

## Overview

Use this skill for explicit code reviews and as the last gate before handing off non-trivial changes.

For reusable review aids:

- read `references/review-checklist.md` for the final gate
- read `references/severity-rubric.md` to keep findings calibrated
- run `scripts/render_review_report.py` when you want a concise findings-first review scaffold

## Review Order

Prioritize:

1. correctness and regression risk
2. trust boundaries and security
3. invariants, atomicity, and concurrency
4. observability gaps, including missing targeted logs on critical runtime paths
5. performance issues
6. test coverage gaps
7. maintainability issues

## Findings First

When the user asks for a review, lead with findings ordered by severity.

Each finding should include:

- file and line reference when available
- the concrete problem
- the consequence if left unchanged
- the required fix or mitigation

Keep summaries brief and secondary.

Use `references/severity-rubric.md` when severity is ambiguous.

## What To Flag

### Code Quality

Flag these when present:

- cyclomatic complexity at or above 10
- unhandled exceptions
- magic numbers with no rationale
- missing validation at trust boundaries
- hidden state mutation
- critical runtime behavior with no adequate logs around mutations, external calls, or failure paths

Use this format when needed:

- `[QUALITY ISSUE]`
- `Function: <name>`
- `Problem: <what is wrong>`
- `Action: <required fix>`

### Performance

Flag these when present:

- N+1 queries
- O(n^2) behavior on unbounded input
- repeated I/O in loops
- excessive memory allocation

### Architecture Consistency

Check whether the implementation still follows the approved plan. If not:

- explain the divergence
- decide whether to update the plan or revert the implementation

## Final Checklist

Before handoff, verify:

- TDD pairs or equivalent tests pass for the changed behavior
- compensation and rollback exist for side-effecting tasks
- observability exists on critical paths, including targeted logs where debugging would otherwise require breakpoints
- performance impact is acceptable
- open risks and testing gaps are stated explicitly

## If No Findings Exist

Say so explicitly. Then note any residual risk, untested area, or environment gap that still limits confidence.
