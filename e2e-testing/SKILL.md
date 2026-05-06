---
name: e2e-testing
description: End-to-end testing conventions using Playwright. Use when Codex needs to write, debug, or review E2E tests, set up Playwright configuration, design page objects, handle network mocking, or fix flaky tests. Load this skill when working with .spec.ts files, e2e/ directories, or playwright.config files.
---

# E2E Testing

## Overview

Use this skill for Playwright E2E testing. It defines selector strategy, waiting discipline, test architecture, network mocking, and CI integration. Combine with `debug-workflow` when diagnosing flaky tests.

## Selector Priority

Use selectors in this strict order:

1. **`page.getByRole()`** — highest priority. Simulates how users and assistive technology interact. Stable across style changes.
2. **`page.getByText()`** — for non-interactive text verification.
3. **`page.getByTestId()`** — for elements with no semantic role. Requires `data-testid` attribute in source.
4. **`page.getByLabel()` / `page.getByPlaceholder()`** — for form elements.

**Forbidden selectors:**
- XPath (breaks on any DOM restructuring)
- CSS class selectors (breaks on style refactors)
- `page.locator('.btn-primary.active')`

## Waiting Discipline

**Absolute ban: `page.waitForTimeout()`**

Hard waits are the leading cause of flaky tests. They are either too short on slow CI or wastefully long on fast machines.

**Use web-first assertions instead:**

```typescript
// Wrong — non-retrying
const isVisible = await page.isVisible('.success');
expect(isVisible).toBe(true);

// Right — auto-retrying until timeout
await expect(page.getByText('Success')).toBeVisible();
```

For complex async state:
- Wait for network: `await page.waitForResponse(r => r.url().includes('/api') && r.status() === 200)`
- Wait with explicit timeout: `await expect(locator).toBeVisible({ timeout: 10000 })`

## Test Architecture

### Directory Structure

```
tests/
├── e2e/
│   ├── auth.setup.ts          # Global auth (generates storageState)
│   ├── checkout/              # Business module
│   │   └── payment-flow.spec.ts
│   └── dashboard/
│       └── analytics.spec.ts
├── fixtures/                  # Custom test fixtures (DI)
├── pages/                     # Page Object Models
│   └── components/            # Reusable component objects
├── test-data/                 # Static test data
└── playwright.config.ts
```

### Naming Rules

- Files: `kebab-case.spec.ts` (e.g. `user-login.spec.ts`)
- Page Object classes: `PascalCase` (e.g. `LoginPage`)
- Test titles: express business value, not implementation detail
  - Bad: `test('click button and check div')`
  - Good: `test('should display confirmation after successful payment')`

### Auth State Reuse

Do not UI-login in every test. Use `storageState`:

1. One `auth.setup.ts` project performs login once.
2. Save cookies/localStorage to `playwright/.auth/user.json`.
3. Configure `storageState` in `playwright.config.ts`.

### Data Isolation

Each test must have independent data. Use fixtures or API calls to set up and tear down data per test.

## Network Layer

### Mock External Dependencies

For unstable third-party services, abort or mock:

```typescript
await page.route('**/*analytics.com*', (route) => route.abort());
```

### Mock API Responses

Do not depend on real backend data. Manufacture deterministic data:

```typescript
await page.route('**/api/users/1', (route) =>
  route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify({ name: 'Test User', role: 'admin' }),
  }),
);
```

## ESLint Enforcement

Configure `eslint-plugin-playwright` with these rules as errors:

- `playwright/no-wait-for-timeout` — ban hard waits
- `playwright/no-page-pause` — prevent debug code in commits
- `playwright/missing-playwright-await` — prevent missing await (silent false positives)
- `playwright/no-element-handle` — encourage locators over element handles

## CI Configuration

In `playwright.config.ts`:

- **Trace**: `trace: 'on-first-retry'` — records DOM snapshots, network, console for failed tests
- **Screenshot**: `screenshot: 'only-on-failure'`
- **Video**: `video: 'retain-on-failure'`
- **Retries**: `retries: 2` — marks flaky tests without blocking the pipeline
- **Sharding**: `npx playwright test --shard=1/5` — distribute across machines

## Flaky-Free Checklist

Before submitting:

- [ ] No `waitForTimeout` anywhere
- [ ] All `expect`, `click`, `fill` preceded by `await`
- [ ] Using `getByRole` or `getByText`, not XPath
- [ ] Tests independent — no shared state between tests
- [ ] Using retrying assertions (`await expect().toBeVisible()`), not boolean checks
