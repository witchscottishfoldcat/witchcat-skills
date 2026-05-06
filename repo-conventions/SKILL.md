---
name: repo-conventions
description: Repository conventions, file naming rules, and output discipline. Use when Codex needs to create or rename files, match an existing repository style, format patches or responses consistently, avoid vague filenames, or enforce rules such as read-before-edit, mirror file names to primary exports, and concise structured output.
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
