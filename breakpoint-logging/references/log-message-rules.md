# Log Message Rules

Prefer messages that answer one question clearly.

## Include

- stable identifier or correlation id when available
- branch or mode name when a decision is important
- small state summary before and after mutation
- external target, attempt count, latency, and outcome for network or storage calls

## Prefer

- structured fields over free-form strings
- counts and ids over whole objects
- bounded summaries over full payloads

## Example Shapes

- `starting order sync`
- `order validation failed`
- `payment status transition`
- `retrying webhook delivery`
- `skipping cache write due to stale version`
