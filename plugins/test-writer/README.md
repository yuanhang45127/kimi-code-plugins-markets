# Test Writer Plugin for Kimi Code

E2E and integration test authoring assistant — generates Playwright, Vitest, and pytest tests from natural language specs.

Inspired by the [Playwright Plugin](https://github.com/microsoft/playwright-claude) for Claude Code.

## How it works

The plugin loads the `write-tests` skill at session start, which teaches Kimi a structured workflow for generating tests:

1. Detect the project's existing testing framework
2. Follow best-practice test structure for that framework
3. Cover happy path, edge cases, and error states
4. Ensure tests are independent and idempotent

## Usage

Just describe what you want to test:

```
Write an E2E test for the login flow
Add unit tests for the user service
Generate pytest tests for the /api/users endpoint
```

Or use the slash commands:

```
/test-writer:e2e login flow with Google OAuth
/test-writer:vitest UserService.createUser
/test-writer:pytest api/users endpoints
```

## Supported frameworks

| Framework | Type | Slash command |
|-----------|------|---------------|
| Playwright | E2E (Chromium, Firefox, WebKit) | `/test-writer:e2e` |
| Vitest / Jest | Unit & integration (JS/TS) | `/test-writer:vitest` |
| pytest | Unit & integration (Python) | `/test-writer:pytest` |

## Notes

- Tests are generated following the project's existing conventions
- Always review generated tests before committing
- For Playwright, you need Playwright installed in your project
