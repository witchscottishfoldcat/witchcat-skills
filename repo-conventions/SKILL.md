---
name: repo-conventions
description: Repository conventions, file naming rules, clean code principles, and output discipline. Use when Codex needs to create or rename files, match an existing repository style, format patches or responses consistently, avoid vague filenames, or enforce rules such as read-before-edit, mirror file names to primary exports, and concise structured output.
---

# Repo Conventions

## Overview

Use this skill whenever file shape, naming, or repository style matters.

For concrete naming help, read `references/naming-rules.md`.

## Read Before Edit

- Read any file before changing it.
- Do not infer structure or invent APIs, paths, or libraries.
- Only modify files that were explicitly read.

## Style Match

Detect the repository's existing naming and layout first. Prefer consistency over introducing a new scheme.

If no local convention is obvious for a new file, fall back to:

- `domain_responsibility_layer.ext`

Examples:

- `order_payment_service.py`
- `user_profile_handler.ts`

## Mirror Rule

The filename should match the primary export when that concept exists.

Examples:

- `invoice_pdf_generator.py` -> `InvoicePdfGenerator`
- `user_profile_page.tsx` -> `UserProfilePage`

## Banned Standalone Names

Do not create vague filenames such as:

- `utils`
- `helpers`
- `manager`
- `misc`
- `common`
- `base`
- `service`
- `handler`

These are only acceptable with a domain prefix, such as `order_utils.py`.

## Naming Violations

If a requested or planned filename breaks the convention:

- state the issue
- offer 2 or 3 compliant alternatives
- ask for a choice before continuing when the decision is ambiguous

Use `references/naming-rules.md` when the repository has mixed conventions or when a new file spans multiple concerns.

## Clean Code Principles

### Constants Over Magic Numbers

- Replace hard-coded values with named constants.
- Use descriptive constant names that explain the value's purpose.
- Keep constants at the top of the file or in a dedicated constants file.

### Meaningful Names

- Variables, functions, and classes should reveal their purpose.
- Names should explain why something exists and how it is used.
- Avoid abbreviations unless they are universally understood.

### Smart Comments

- Do not comment on what the code does — make the code self-documenting.
- Use comments to explain why something is done a certain way.
- Document APIs, complex algorithms, and non-obvious side effects.

### Single Responsibility

- Each function should do exactly one thing.
- Functions should be small and focused.
- If a function needs a comment to explain what it does, it should be split.

### DRY (Don't Repeat Yourself)

- Extract repeated code into reusable functions.
- Share common logic through proper abstraction.
- Maintain single sources of truth.

### Clean Structure

- Keep related code together.
- Organize code in a logical hierarchy.
- Use consistent file and folder naming conventions.

### Encapsulation

- Hide implementation details.
- Expose clear interfaces.
- Move nested conditionals into well-named functions.

### Code Quality Maintenance

- Refactor continuously.
- Fix technical debt early.
- Leave code cleaner than you found it.

### Testing

- Write tests before fixing bugs.
- Keep tests readable and maintainable.
- Test edge cases and error conditions.

### Version Control

- Write clear commit messages.
- Make small, focused commits.
- Use meaningful branch names.

## Output Rules

- keep responses concise
- use code fences with a language tag
- use unified diffs when the user explicitly asks for patch output
- avoid redundant explanation after code blocks

## Change Discipline

- preserve public interfaces where practical
- do not silently broaden scope
- prefer small, reversible changes
- surface assumptions instead of hiding them
