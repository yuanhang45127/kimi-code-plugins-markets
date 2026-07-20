---
description: Generate unit/integration tests using Vitest for a given module or component
---

Generate Vitest tests for: $ARGUMENTS

Follow the write-tests workflow:
1. Identify the module's public API and key functions
2. Cover: happy path, edge cases, error handling
3. Use `describe`/`it` blocks with Arrange-Act-Assert pattern
4. Mock external dependencies where appropriate
5. Make tests independent — no shared mutable state
