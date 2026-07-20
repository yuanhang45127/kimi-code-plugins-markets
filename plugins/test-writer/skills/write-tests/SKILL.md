---
name: write-tests
description: Generates E2E, unit, and integration tests from natural language specs using Playwright, Vitest, or pytest
arguments:
  - framework
  - target
---

# Write Tests

When asked to write tests, follow this workflow:

## Step 1: Determine the testing framework

Check the project for existing test configuration:

- **E2E**: Look for `playwright.config` (Playwright), `cypress.config` (Cypress)
- **Unit/Integration (JS/TS)**: Look for `vitest.config`, `jest.config`, or test scripts in `package.json`
- **Unit/Integration (Python)**: Look for `pytest.ini`, `pyproject.toml` (tool.pytest), `conftest.py`
- **Go**: Look for `_test.go` files and `go.mod`
- **Rust**: Look for `Cargo.toml` with `[dev-dependencies]`

Default to the framework already in use. If none is detected, ask the user.

## Step 2: Structure the tests

### E2E (Playwright)

```typescript
import { test, expect } from '@playwright/test';

test.describe('<feature>', () => {
  test('happy path: <description>', async ({ page }) => {
    await page.goto('<url>');
    // ... interactions
    await expect(<selector>).<matcher>();
  });

  test('edge case: <description>', async ({ page }) => {
    // ... edge case logic
  });

  test('error state: <description>', async ({ page }) => {
    // ... error handling logic
  });
});
```

### Unit (Vitest)

```typescript
import { describe, it, expect, vi } from 'vitest';

describe('<feature>', () => {
  it('should <expected behavior>', () => {
    // Arrange
    // Act
    // Assert
  });
});
```

### Python (pytest)

```python
import pytest
from <module> import <function>


def test_happy_path():
    """<description>"""
    # Arrange
    # Act
    # Assert
    assert <result> == <expected>


@pytest.mark.parametrize("input,expected", [
    (<case1>),
    (<case2>),
])
def test_edge_cases(input, expected):
    assert <function>(input) == expected
```

## Step 3: Coverage checklist

Before finishing, check:
- [ ] Happy path covered
- [ ] At least 2 edge cases covered
- [ ] Error / negative scenario covered
- [ ] Tests are independent (no shared mutable state)
- [ ] Tests are idempotent (can run multiple times)
- [ ] Async operations properly awaited

## When invoked with arguments

- `$framework` — target framework (playwright, vitest, pytest)
- `$target` — component/feature to test
