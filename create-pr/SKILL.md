---
name: create-pr
description: Push the current branch and create or update a Pull Request using GitHub CLI (gh) or GitLab CLI (glab). Use when the user says create PR, submit PR, open PR, merge request, create pull request, 提 PR, 建 PR, 提交合并请求, or when the implementation is complete and ready for review. Auto-detect GitHub or GitLab from the remote URL.
---

# Create PR

## Overview

Use this skill when code changes are complete and the user wants to submit them for review. It handles branch status checking, pushing, and PR/MR creation on GitHub or GitLab.

## Platform Detection

Detect the platform from `git remote get-url origin`:

- Contains `github.com` -> use `gh`
- Contains `gitlab.com` or a self-hosted GitLab URL -> use `glab`
- If unsure, ask the user

## Workflow

### 1. Pre-flight Check

```bash
git status -sb
git log -3 --oneline
git branch --show-current
```

Verify:

- Working tree is clean (no uncommitted changes). If dirty, commit or stash first.
- Current branch is not `main` or `master`. If it is, ask the user to create a feature branch.
- Commits exist ahead of origin.

### 2. Push

If the branch is ahead of origin:

```bash
git push -u origin <branch-name>
```

If the branch already tracks origin:

```bash
git push origin
```

### 3. Create PR

#### GitHub

```bash
gh pr create --base <target-branch> --title "<title>" --body "<description>"
```

#### GitLab

```bash
glab mr create --target-branch <target-branch> --title "<title>" --description "<description>"
```

- `--base` / `--target-branch`: defaults to the repository's default branch (usually `main` or `master`). Override if the user specifies a different target.
- If a PR/MR already exists for this branch, the CLI will detect it and offer to update instead of creating a duplicate.

### 4. Title and Description

#### Title

- Derive from the most recent commit message or from the overall change summary.
- Follow the project's existing commit/PR title convention if detectable.
- Keep it concise: one line, under 72 characters.

#### Description Template

If the user does not specify a description, use this minimal template:

```markdown
## Changes

- (bullet list of key changes)

## Testing

- (how the changes were tested)

## Checklist

- [ ] Tests pass
- [ ] No breaking changes (or documented if present)
```

For larger changes, expand with:

```markdown
## Motivation

(Why this change was needed)

## Changes

- (key changes)

## Breaking Changes

(If any, list them with migration instructions)

## Testing

- (test approach and results)

## Screenshots / Demo

(If applicable)
```

### 5. Post-creation

After the PR is created:

- Output the PR URL.
- If CI checks are visible, note their status.
- Remind the user to request reviewers if applicable.

## Commit Message Convention

Do not hardcode a specific format. Detect and follow the project's existing convention:

- Look at recent commit messages: `git log -10 --oneline`
- If the project uses conventional commits (`feat:`, `fix:`, `chore:`), follow that pattern.
- If the project uses scope-based (`Component: description`), follow that pattern.
- If no pattern is obvious, use a clear descriptive message in the user's language.

## Edge Cases

### Draft PR

If the user says "draft PR" or "WIP PR":

- GitHub: add `--draft` flag
- GitLab: add `--draft` or prefix title with `Draft:`

### Existing PR Update

If a PR already exists and the user pushes new commits:

```bash
git push origin <branch-name>
```

The existing PR updates automatically. No need to re-create.

### Multiple Commits Squash

If the user wants a clean single-commit PR:

```bash
git rebase -i origin/main
```

Ask before doing an interactive rebase. It rewrites history.

## Error Handling

| Error | Action |
|---|---|
| `gh` / `glab` not installed | Tell the user to install the CLI |
| Not authenticated | Run `gh auth login` or `glab auth login` |
| No remote named `origin` | Ask the user to add a remote |
| Branch is behind target | Pull and resolve conflicts first |
| Permission denied | Check fork workflow, suggest fork + PR |

## Command Reference

| Step | GitHub | GitLab |
|---|---|---|
| Check status | `git status -sb` | `git status -sb` |
| Push | `git push -u origin <branch>` | `git push -u origin <branch>` |
| Create PR | `gh pr create --base main --title "..." --body "..."` | `glab mr create --target-branch main --title "..." --description "..."` |
| List existing | `gh pr list --head <branch>` | `glab mr list --source-branch <branch>` |
| View PR | `gh pr view <number>` | `glab mr view <number>` |
| Draft PR | `gh pr create --draft` | `glab mr create --draft` |
