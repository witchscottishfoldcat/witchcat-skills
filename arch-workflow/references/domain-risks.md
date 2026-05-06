# Domain Risk Prompts

Use these prompts when filling the seven risk dimensions.

## Invariants

- What must never become false?
- What is the catastrophic consequence if it does?

## Atomicity

- Which operations must be all-or-nothing?
- Which boundaries do they cross?
- If failure happens halfway, can the system self-heal?

## Concurrency

- Who races for the same resource?
- What breaks under duplicate or out-of-order execution?

## Side Effects

- Which actions are irreversible?
- If the side effect fires before the main write fails, what compensates?

## Trust Boundaries

- Which inputs are untrusted?
- Where are validation, authz, masking, and rate limits enforced?

## Observability

- What does silent failure look like?
- Which log, metric, or trace would reveal it?

## Performance

- What is on the hot path?
- Which loop, query, or fan-out degrades with scale?
