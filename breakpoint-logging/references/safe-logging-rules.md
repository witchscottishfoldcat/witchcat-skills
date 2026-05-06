# Safe Logging Rules

Do not log:

- passwords
- API tokens
- session cookies
- access keys
- raw personal data unless already approved and redacted
- full request or response bodies by default

Prefer logging:

- internal ids
- counts
- booleans
- enum-like status values
- bounded snippets that are already masked

If the codebase has masking helpers, use them instead of inventing new redaction logic inline.
