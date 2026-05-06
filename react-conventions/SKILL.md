---
name: react-conventions
description: React and TypeScript frontend conventions for component development. Use when Codex is working with React, Next.js, TypeScript, TSX/JSX files, component props, hooks, state management, CSS-in-JS, or frontend performance optimization. Load this skill automatically for any .tsx/.jsx file or when the tech stack is React-based.
---

# React Conventions

## Overview

Use this skill when the project uses React and TypeScript. It defines component authoring rules, type conventions, styling discipline, and performance patterns. Combine with `repo-conventions` for naming and `build-workflow` for the implementation flow.

## Component Authoring

- Use function components and hooks exclusively. No class components.
- Use early returns to reduce nesting. If you need more than 3 levels of indentation, refactor.
- Each component should do one thing. If it needs a comment to explain what it does, split it.
- Leave no placeholders, TODOs, or missing pieces in implementation.
- Include all required imports. Ensure proper naming of key components.

## TypeScript Rules

- All components and functions must have accurate type definitions.
- Avoid `any`. Use precise types.
- Define component props with `interface`, named `ComponentNameProps`.
- Define state interfaces as `ComponentNameState`.
- Use literal union types over `enum`.
- Prefer type inference where the type is obvious.
- Export all public interfaces for consumer use.
- Use `React.ForwardRefRenderFunction` for ref-forwarding components.

## Props and Events Naming

- Initial value props: `default` + `PropName` (e.g. `defaultValue`)
- Open/close state: `open`, not `visible`
- Show-related: `show` + `PropName` (e.g. `showHeader`)
- Feature toggle: `PropName` + `able` (e.g. `draggable`)
- Disabled state: `disabled`
- Trigger events: `on` + `EventName` (e.g. `onClick`, `onChange`)
- Sub-component events: `on` + `SubComponentName` + `EventName` (e.g. `onHeaderClick`)
- Event handler functions: `handle` prefix (e.g. `handleClick`, `handleKeyDown`)

## Styling

- Use the project's CSS-in-JS solution (e.g. `@ant-design/cssinjs`, styled-components, emotion).
- Use design tokens or theme variables. No hardcoded colors, sizes, or spacing.
- Respect `prefers-reduced-motion` for animations.
- Support dark mode by default.
- Support RTL with CSS logical properties (e.g. `margin-inline-start` instead of `margin-left`).

## Performance

- Use `React.memo`, `useMemo`, and `useCallback` where they prevent real re-renders.
- Do not wrap everything blindly in memo. Measure first.
- Avoid unnecessary state that triggers cascading re-renders.
- Support tree-shaking by keeping exports clean.

## Accessibility

- All interactive elements must be keyboard-accessible.
- Use `aria-label`, `aria-describedby`, and roles where semantic HTML is insufficient.
- Ensure focus states are visible.
- Maintain sufficient color contrast (WCAG 2.1 AA).
- Do not rely solely on color to convey information.

## Component Ref Pattern

Components exposing a ref should follow:

```tsx
interface ComponentRef {
  nativeElement: HTMLElement;
  focus: () => void;
}
```

## API Documentation Format

When documenting component APIs:

| Property | Description | Type | Default |
|---|---|---|---|
| htmlType | ... | string | `button` |
| type | ... | `horizontal` \| `vertical` | `horizontal` |
| disabled | ... | boolean | false |

- String defaults in backticks. Boolean and number defaults as literals.
- No default: use `-`.
- API properties sorted alphabetically.
