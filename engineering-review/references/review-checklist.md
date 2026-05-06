# Review Checklist

Confirm these before handoff:

- changed behavior is covered by tests
- trust boundaries still validate input
- no hidden state mutation was introduced
- failure paths are observable
- critical runtime paths have targeted logs or an explicit reason why existing observability is sufficient
- side effects have rollback or compensation
- performance impact is acceptable for expected load
- remaining risks are explicit
