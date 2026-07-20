---
name: tdd-workflow
description: Guides the Red/Green/Refactor TDD cycle — write the test first, make it pass, then refactor
---

# TDD Workflow (Red / Green / Refactor)

When the user wants to develop a new feature using TDD, follow this strict sequence.

## Phase 1: Red — Write a failing test first

Before writing any implementation code:

1. Understand what the feature should do. Ask clarifying questions if needed.
2. Write a test that expresses the desired behaviour
3. Run the test — confirm it fails with the expected error (the "Red" signal)

## Phase 2: Green — Make the test pass

1. Write the minimal implementation code to pass the test
2. Do NOT optimise, refactor, or add extra functionality
3. Run the test — confirm it passes (the "Green" signal)

## Phase 3: Refactor — Clean up

1. Now that the test is green, improve the code quality
2. Run the test again to confirm refactoring didn't break anything
3. Look for: duplication, unclear naming, unnecessary complexity

## Key rules

- **Never write implementation before the test** — that breaks the TDD cycle
- **Minimal code for green** — resist the urge to over-engineer upfront
- **Refactor only when green** — never refactor on a red test
- Run the test after every phase to verify the state

## When to use

- Building a new function, class, or module
- Adding a feature to existing code
- Fixing a bug (write a test that reproduces it first!)
