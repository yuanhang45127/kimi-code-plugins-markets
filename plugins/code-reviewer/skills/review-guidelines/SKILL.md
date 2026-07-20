---
name: review-guidelines
description: Loads code review best practices and guidelines at session start
---

# Code Review Guidelines

When reviewing code, follow these principles:

## 1. Correctness First
- Does the code do what it intends to do?
- Are there edge cases that aren't handled?
- Are error paths properly managed?

## 2. Readability
- Is the code easy to understand at a glance?
- Are variable and function names descriptive?
- Would comments help future readers understand *why* a decision was made?

## 3. Performance & Maintainability
- Is there unnecessary complexity?
- Could the code be simplified without losing expressiveness?
- Are there obvious performance pitfalls (N+1 queries, unnecessary allocations, etc.)?
