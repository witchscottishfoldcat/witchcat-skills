# M-Task Risk Scan

Use this when the task is medium-sized and you want a compact risk pass.

## Prompt

Answer only the dimensions that materially affect the change:

- Invariants: what must not break, and what user or system failure follows if it does
- Atomicity: what has to succeed or fail together
- Concurrency: who can race on the same state
- Side effects: what cannot be undone cleanly
- Trust boundaries: which input is untrusted and what validates it
- Observability: what could fail silently
- Performance: what path could degrade under scale

## Output Shape

```text
[DOMAIN RISKS]
Invariants       : ...
Atomicity        : ...
Concurrency      : ...
Side Effects     : ...
Trust Boundaries : ...
Observability    : ...
Performance      : ...
Top Risks        : ...
```
