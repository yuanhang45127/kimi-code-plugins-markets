---
name: review-workflow
description: Systematic code review that checks correctness, readability, security, and test coverage
---

# Code Review Workflow

When asked to review code, a PR, or a commit, follow this structured process.

## Step 1: Understand the change

- Read the diff or the code being reviewed
- Identify the purpose: feature, bugfix, refactor, docs, chore

## Step 2: Check each dimension

### Correctness
- Does the code do what it intends to?
- Are edge cases handled? (empty input, null, boundary values)
- Are error paths properly managed?
- Are there race conditions or timing issues?

### Readability & Maintainability
- Are names descriptive and unambiguous?
- Is the code structure easy to follow?
- Would a new team member understand it?
- Are there comments explaining *why*, not *what*?

### Security
- Are inputs validated and sanitised?
- Are there any hardcoded secrets or credentials?
- Is there proper access control?
- Any injection risks (SQL, command, XSS)?

### Test coverage
- Are there tests for this change?
- Do tests cover edge cases and error paths?
- Do the tests actually test what they claim to?

## Step 3: Structure the review report

```
## Summary
<one-paragraph overview of what the change does>

## Required Changes (blocking)
- <item> — <why this must change>

## Suggestions (non-blocking)
- <item> — <why this would improve the code>

## Positives
- <what was done well>
```

## Tone

- Be constructive, not critical
- Explain *why* something should change, not just *what* to change
- Praise good patterns when you see them
