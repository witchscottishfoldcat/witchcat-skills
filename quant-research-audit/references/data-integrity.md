# Data integrity: units, joins, missingness, vendor traps

These bugs are silent — no exception, plausible-looking numbers — and they invalidate results just as thoroughly as look-ahead. Audit every point where data is merged, scaled, or mapped.

## Units & scale
- Reconcile units at **every** join and aggregation. Common landmines: 万元 vs 千元 vs 元; basis points vs percent vs fraction; shares vs lots vs round-lots; annualized vs periodic; nominal vs adjusted.
- A factor that's "off by 10000x" can still rank monotonically, so ranking-based logic hides the error while any absolute threshold (a 净流入 floor, a turnover cap) silently mis-fires.
- Verify by reconciling one instrument end-to-end against a known source (e.g. a stock's reported figure vs your pipeline's value).

## Joins & taxonomy
- Join on **stable identifiers** (exchange-qualified codes, CUSIP/ISIN, a vendor's index code), never on display names or human-readable industry strings.
- **Two vendors' "industry" are different taxonomies.** A stock's `industry` field from a basic-info table rarely equals a classification provider's scheme. To aggregate constituents into a sector, map every instrument through the *same* membership table you aggregate by, on the *same* code space. String-matching sector names across sources fails subtly (synonyms, levels, revisions).
- When three+ tables must agree (membership ↔ classification ↔ daily series), confirm they share one join key and check the **overlap count** — if only X% of rows join, you have a key/format mismatch, not a data shortage.

## Missingness — never fabricate, never neutral-pass
- Rows that fail to map (an instrument not in the classification, a name with no fundamentals) get **null**, and null must be handled explicitly: exclude, or carry as "unknown" that **cannot pass a gate**. Defaulting missing to a neutral/median value silently lets unqualified names through and is a common way fake breadth enters a portfolio.
- Distinguish "missing because not applicable" from "missing because not yet published" (the latter is also a look-ahead trap — see `look-ahead-pit.md`).

## Aggregation choices that change conclusions
- In-pool vs whole-market: a "sector strength" computed only over your *candidate pool* is a within-pool proxy, not a real market-wide signal. If the intent is top-down sector rotation, aggregate over the full market, not the survivors of your filter.
- Single-snapshot vs windowed: one day's flow/return is noisy; cumulate over a short window for stability when the thesis is about persistence.
- Thin groups: a rank/mean over very few members is noise. Require a minimum group size before trusting a cross-sectional rank.

## Timezone, session, and freshness
- "Today" intraday usually has **no finalized data yet** — vendor endpoints return empty or partial until after close/publish. Code that anchors on "latest date" then reads a single snapshot silently produces all-null features on the current day. **Probe backward to the latest date that actually returns data**, and compute offsets from that resolved anchor.
- Align timezones and trading calendars across sources before joining on date.

## Reusable data-vendor gotchas

### Tushare (reusable across any Tushare project)
- **Row caps / pagination**: many endpoints silently cap a single call (commonly ~3000–6000 rows). Full-market or full-history pulls (e.g. `index_member_all`, large `moneyflow` history) get truncated → join rates collapse (e.g. ~50%) with no error. **Paginate** with `offset`/`limit` until a page returns fewer than the page size, then dedup.
- **Intraday emptiness**: same-day `daily` / `moneyflow` / `sw_daily` are empty until published. Probe backward for the latest populated trade date.
- **Units**: `moneyflow.net_mf_amount` is **万元**; many amount fields are 万元 or 千元 — check the field doc, don't assume 元.
- **PIT membership**: `index_member_all` natively carries `in_date`/`out_date`/`is_new`; the wrapper usually doesn't strip columns, so you can do point-in-time membership by date-window filtering instead of the `is_new=Y` (current-only) flag.
- **Financials**: `fina_indicator` rows are keyed by period (`end_date`); filter by `ann_date ≤ as_of` to avoid using unannounced reports.

### General vendor hygiene (akshare / Wind / JoinQuant / web sources)
- Confirm whether prices are adjusted (前复权/后复权/不复权) and whether adjustment is past-only.
- Re-fetched "historical" data can change (revisions, late corrections); cache the as-of snapshot when reproducibility matters.
- Rate limits and partial failures can yield silently short result sets — assert expected row counts.
