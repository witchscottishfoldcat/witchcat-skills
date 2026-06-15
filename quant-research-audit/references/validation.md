# Statistical validity & acceptance

Once the data is clean (no look-ahead, units/joins correct), the remaining question is whether the edge is **real and repeatable** or an artifact of fitting. This section is about not fooling yourself.

## Overfitting controls
- **Anchor thresholds to economic priors, not to the backtest.** A cutoff chosen because it maximized in-sample Sharpe is a curve-fit; a cutoff chosen because theory/literature says "industry momentum top-quintile" or "volume-confirmed breakout" is a hypothesis. Prefer the latter and let the data falsify it.
- **Few parameters, simple forms.** Each tunable knob is a degree of freedom to overfit. Round numbers and monotone responses are more likely to generalize than finely-tuned step functions.
- **Soft over hard when factors correlate.** When real data shows your factors move together (e.g. momentum and "overheat" both high in hot names), a single hard cutoff mass-kills good names or lets a cluster through; a soft penalty plus an extreme-only hard gate is more robust.
- **Out-of-sample is sacred.** Reserve data the model never saw during design. Walk-forward (rolling train→test) is the realistic version; a single train/test split is the minimum.

## Multiple testing / selection bias
- If you tried N factor variants, parameter sets, or universes, the best one's backtest is **inflated** by selection — the more you tried, the more the winner is luck. Track how many things you tried; deflate expectations accordingly (and ideally hold out a final test set touched only once).
- "We iterated the threshold until the chart looked good" is in-sample optimization wearing a disguise. So is re-running on new data and re-tuning each time.
- Beware the garden of forking paths: every discretionary choice (winsorization, fill, rebalance day) is an implicit parameter.

## Realistic backtest mechanics
- **Costs and frictions**: commission, slippage (worse for the very breakout/illiquid names momentum strategies love), market impact, borrow cost for shorts, settlement (T+1). A gross-return edge that's smaller than costs is not an edge.
- **No same-bar fills**: decide on information up to bar *t*, fill at *t+1* or with realistic delay (see `look-ahead-pit.md`).
- **Capacity & liquidity**: position sizes must be plausible vs ADV; an edge that only exists at tiny size may not be investable.
- **Regime coverage**: test across ≥2 distinct regimes (trend + chop, risk-on + drawdown). A strategy tuned in one regime often inverts in another — state the regime dependence explicitly.

## What "acceptance" means (the go-live gate)
A new strategy/factor earns deployment by clearing an **out-of-sample bar**, not by compiling or passing unit tests:
- Beats the **closest existing strategy** *and* a **passive benchmark** on risk-adjusted forward return (e.g. IR/Sharpe), out-of-sample, after costs.
- Lower tail / drawdown or lower false-signal rate where that's the thesis (e.g. a breakout-confirmation strategy should show fewer failed breakouts, not just higher average return).
- Adequate sample size and stability across the walk-forward windows — not one lucky period.
- Reproducible: same inputs → same result (cache PIT snapshots; version the params). Park tuned parameters in a versioned config, not hardcoded magic numbers, so they're auditable and A/B-able.

If it doesn't beat both baselines out-of-sample, it's redundant or noise — don't ship it.

## Signal-discrimination sanity check (cheap, catches bugs early)
On a real recent sample, a healthy gate/score produces a **spread**: some pass, some fail, with a sensible distribution of reasons. Two red flags:
- **All-pass / all-fail** → usually a threshold mis-scaled to the score's range, or a feature that's uniformly null/default (trace the join/enrichment — a field everyone fails on is often *not being populated*, not genuinely weak).
- **Degenerate ranking** (everything scores ~the same) → the factor isn't discriminating; check normalization and whether the input variance survived the pipeline.
Use this as a fast pre-backtest smoke before spending compute on a full walk-forward.
