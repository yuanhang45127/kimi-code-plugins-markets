---
description: Generate pytest tests for Python functions, classes, or API endpoints
---

Generate pytest tests for: $ARGUMENTS

Follow the write-tests workflow:
1. Identify the function/class public API
2. Cover: happy path, edge cases (via `@pytest.mark.parametrize`), error handling
3. Use fixtures for shared setup and cleanup
4. Include meaningful docstrings on each test
5. Make tests independent and idempotent
