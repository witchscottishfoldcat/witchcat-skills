# Regression Rules

After the root cause is confirmed, add the smallest regression coverage that would catch the same failure mode again.

Preferred order:

1. focused unit test when the defect is local logic
2. integration test when the bug crosses boundaries
3. fixture or snapshot update only when behavior is large-format and stable

Do not add a broad test that still misses the original failure mechanism.
