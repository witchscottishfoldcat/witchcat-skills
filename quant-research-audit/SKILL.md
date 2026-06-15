---
name: quant-research-audit
description: Audit a quantitative trading strategy, factor, signal, or backtest for the silent data and statistics errors that compile, pass tests, and look great — yet invalidate the result. Use whenever a backtest looks suspiciously good, the user asks whether a strategy/factor/backtest is trustworthy or "too good to be true", reviews or productionizes a quant model, builds a new factor or selection strategy, designs an acceptance/go-live gate, or joins market data across sources (any repo, notebook, or vendor — JoinQuant, Tushare, akshare, Wind, custom). This is the quant counterpart to code review: code review checks correctness, this checks whether the research itself is valid. Trigger it even when the code is clearly correct, because the dangerous bugs here are in data provenance and methodology, not syntax.
---

# Quant Research Audit

## Why this exists

In quant work the worst bugs **do not throw, do not fail tests, and produce beautiful results** — they corrupt the *provenance* or *statistics* of the data. A backtest that quietly uses tomorrow's index membership, or sums 万元 into 元, or accepts a strategy because it beat nothing, will look like alpha and lose money live. Generic code review will not catch these because the code is correct; the *research* is wrong.

This skill is repo-agnostic. It is a lens you apply to a strategy / factor / backtest regardless of language, framework, or data vendor. It does not contain any one project's file paths — when you need project specifics, **discover them** (read the data flow) rather than assume them.

## How to apply (trace, don't skim)

The audit is a **data-provenance trace**, not a checklist skim. For every input the model consumes:

1. **Identify the as-of moment** — the instant in simulated time when the decision is made.
2. **Trace each input back to when it was actually knowable.** Membership lists, fundamentals, analyst data, corporate actions, even "latest price" all have a publish/effective time. If an input encodes information from *after* the as-of moment, you have look-ahead.
3. **Check the joins and units** at each merge — different sources use different keys, taxonomies, scales, and timezones.
4. **Question the result's strength** — strong results are a prompt to suspect leakage, not to celebrate. The first hypothesis for "great Sharpe" should be a bug, not skill.

Then judge **acceptance**: does this beat a real baseline out-of-sample, or did it just pass in-sample?

Read the matching reference for depth; each explains the *why* so you can adapt to novel cases:
- `references/look-ahead-pit.md` — point-in-time, look-ahead, survivorship, lag. The highest-yield section.
- `references/data-integrity.md` — units, taxonomy/key joins, missing-vs-fabricated, timezone/session, and reusable data-vendor gotchas (incl. a Tushare section).
- `references/validation.md` — overfitting controls, multiple-testing, and what "acceptance" means.

## The lens (summary — depth in references)

**1. Look-ahead / point-in-time (read `look-ahead-pit.md`)**
- Index/universe membership must be *as-of-date* (with in/out dates), never "current members" — current membership backtested into the past is survivorship + look-ahead at once.
- Fundamentals/estimates must be filtered by **announcement date ≤ as-of**, not by the period they describe (a Q3 report isn't knowable in Q3).
- Any feature built from a window must end at-or-before the as-of bar (no centered windows, no `shift(-1)`, no full-series `fit` then backtest).
- Delisted/halted names must exist in the historical universe (their absence is survivorship).

**2. Data integrity (read `data-integrity.md`)**
- Reconcile **units** at every join (万元 vs 元 vs 千元; bps vs %; shares vs lots).
- Join on **stable codes**, not display names or a vendor's idiosyncratic taxonomy; one source's "industry" string ≠ another's.
- **Missing ≠ neutral and never fabricated** — unmapped/missing rows must be excluded or explicitly handled, not silently defaulted into a pass.
- Mind **timezone and trading session** — "today" intraday often has no published data yet; vendor row caps silently truncate (paginate).

**3. Statistical validity & acceptance (read `validation.md`)**
- Thresholds should follow **economic priors / a literature anchor**, not values tuned to make the backtest look good (that's curve-fitting an in-sample artifact).
- **Acceptance = out-of-sample, walk-forward, beating a real baseline** (the closest existing strategy and a passive benchmark) on risk-adjusted return with realistic costs — not "tests pass" or a high in-sample win rate.
- Account for **multiple testing** — if you tried 50 factor variants, the best one's backtest is inflated.
- Sanity-check signal discrimination: a healthy gate produces a **spread** of outcomes; all-pass or all-fail usually means a threshold or a data-join bug, not a real edge.

## Output of an audit

Report findings **severity-first**, each as: the flaw → why it invalidates the result → the concrete fix → how to verify the fix. Distinguish **invalidating** issues (look-ahead, survivorship, unit error — results cannot be trusted until fixed) from **weakening** ones (mild overfitting, thin samples). Don't bury a look-ahead bug under style nits. If you cannot trace an input to its as-of time from the available code/data, say so explicitly and list it as an unverified risk rather than assuming it's fine.

## Relationship to other skills

Generic code correctness and review belong to `engineering-review` / `build-workflow`; this skill owns the data-provenance and statistical-validity lens they lack. For project-specific wiring (how a given repo registers a strategy, which files to touch), use that repo's own project skill or discover it on the spot — keep this skill free of any single repo's paths so it stays usable everywhere.
