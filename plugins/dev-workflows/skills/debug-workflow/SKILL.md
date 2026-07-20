---
name: debug-workflow
description: Systematic debugging workflow — reproduce, isolate, understand root cause, fix, verify
---

# Systematic Debugging Workflow

When asked to debug an issue, follow this structured approach.

## Step 1: Reproduce

- Get the exact steps, input, or environment that triggers the bug
- If there's an error message, read it carefully — start with the first line, not the last
- If possible, reproduce the issue in a controlled environment

## Step 2: Isolate

- Narrow down the failing code path
- Use binary search: comment out half the code, test, repeat
- Check assumptions: is the input what you think it is? Is the dependency version correct?
- Add logging at key decision points

## Step 3: Understand the root cause

- Once the failing code is located, understand *why* it fails
- Is it a logic error? Type mismatch? Race condition? Off-by-one? API misuse?
- Check the documentation or spec if unsure

## Step 4: Fix

- Write the minimal fix — the smallest change that addresses the root cause
- If the fix is non-trivial, add a comment explaining why this change works
- Do NOT fix unrelated issues in the same change

## Step 5: Verify

- Confirm the fix resolves the original issue
- Run existing tests to ensure no regressions
- If there was no test for this case, consider adding one
