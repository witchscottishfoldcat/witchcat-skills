# Debug Trace Checklist

Trace enough state to eliminate competing causes.

## Capture

- exact request or event input
- feature flags and config affecting the path
- database rows or records that matter
- cache keys and freshness
- retries, timeouts, or backoff state
- thread, worker, or job context
- external dependency response shape

## Ask

- what state changed immediately before failure
- where causality becomes unclear
- whether the bug is data-dependent, timing-dependent, or environment-dependent
- whether the symptom is a primary failure or a downstream effect
