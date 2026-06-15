# Look-ahead, point-in-time, survivorship

The single highest-yield audit area. Almost every "too good to be true" backtest dies here. The core question for every input: **was this value actually knowable at the as-of moment, in this exact form?**

## Point-in-time (PIT) membership / universe
- Universe and index membership change over time. Backtesting today's constituents into the past is a **double sin**: survivorship (you only kept the survivors) *and* look-ahead (you "knew" who'd be in the index).
- Correct: membership as-of-date, using join/leave dates. A vendor that exposes `in_date` / `out_date` (or effective/expiry) lets you filter `in_date ≤ as_of AND (out_date is null OR out_date > as_of)`. A "is_current"/"is_new" flag gives you **today's** members — fine for live trading, biased for history.
- Symptom: a strategy that "always held the eventual winners," or whose edge vanishes when you switch to PIT membership.

## Fundamentals, estimates, ratings — announcement lag
- A financial report describes a past period but becomes **knowable only on its announcement/publish date**. Filtering by period end (`end_date`) instead of announcement (`ann_date ≤ as_of`) leaks future earnings.
- Same for analyst estimates, ratings, restatements (use the *original* print, not the restated one), and any "latest available" snapshot — "latest" must mean latest *as of the bar*, not latest in the dataset.
- Index/benchmark divisors, shares outstanding, free-float factors also revise; use the version effective at the bar.

## Feature / signal construction
- **No future bars in a window.** Rolling features must end at-or-before the decision bar. Centered windows, `rolling(...).mean()` that includes the current unfinished bar, `shift(-k)`, or `resample` that peeks forward all leak.
- **Fit on the past only.** Normalization stats, PCA, factor loadings, scalers, model parameters must be fit on data up to the as-of moment, then applied forward. A `StandardScaler.fit(whole_series)` before a backtest is leakage. Walk-forward or expanding-window fitting fixes it.
- **Target leakage.** The label must be strictly in the future of every feature. Double-check any feature derived from the same bar as the label.
- **Corporate actions / adjustment.** Back-adjusted prices bake in *future* splits/dividends into past bars. For point-in-time decisions, use the price/adjustment known at the bar, or confirm the adjustment is past-only.

## Trade timing realism (a softer cousin of look-ahead)
- Decide on bar *t*'s **close-or-earlier** information; execute at *t+1* (or with a realistic delay), not at the same close you used to decide. "Signal at close, fill at that same close" is implicit look-ahead.
- Limit-up/halted/suspended names can't be bought at the touched price — model no-fill, not a free entry.
- Respect settlement (T+1 markets), borrow availability for shorts, and liquidity caps.

## Survivorship beyond membership
- Delisted, merged, and halted instruments must be present in the historical universe with their real (often bad) outcomes. A dataset that silently drops them inflates returns and hides tail risk.
- Backfilled history (a vendor adding a name's pre-inclusion data) is fine for prices but dangerous for "was it investable then" decisions.

## How to verify you've removed look-ahead
- Re-run with strictly PIT inputs and confirm the edge survives (it usually shrinks — that shrinkage is the bias you just removed).
- Shift every feature back one extra bar; if performance collapses, you were standing on the decision bar's future.
- Spot-check a handful of historical dates by hand: reconstruct exactly what was knowable that day and confirm the model saw only that.
- Compare current-membership vs PIT-membership runs; a large gap quantifies the survivorship/look-ahead you removed.
