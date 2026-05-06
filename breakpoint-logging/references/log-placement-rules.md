# Log Placement Rules

Use logs where a human would otherwise drop a breakpoint.

## Good Positions

- request, command, job, or event entry
- before and after a state-changing operation
- before external I/O and after success or failure
- around important branch decisions
- around retries, backoff, timeout, circuit-breaker, and fallback behavior
- at async handoff boundaries
- in exception handlers
- before early return paths that skip expected work

## Usually Avoid

- every iteration of an unbounded loop
- pure getters with no branch or mutation value
- large raw payload dumps
- duplicate entry logs in thin wrapper layers unless they add new context

## Heuristic

If removing a log would not reduce uncertainty during debugging, it probably should not exist.
