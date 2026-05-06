# TDD Boundaries

Use TDD by default for core logic.

Skip TDD only when the change is clearly one of these:

- config-only
- scaffolding
- migration plumbing
- structural refactor with no behavior change

Borderline case rule:

- if a function makes a decision, transforms data, or enforces a business rule, treat it as core logic
- if a change only wires existing logic together, TDD may be optional
