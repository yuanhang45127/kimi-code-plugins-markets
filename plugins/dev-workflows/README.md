# Dev Workflows Plugin for Kimi Code

Structured development workflows — TDD, code review, and systematic debugging for consistent agent behaviour.

Inspired by [Superpowers](https://github.com/superpowers-dev/superpowers) for Claude Code.

## How it works

The plugin loads three structured workflows as skills, with the TDD workflow active by default at session start. Each workflow enforces a step-by-step process that produces consistent, high-quality results.

## Workflows

### TDD (Red / Green / Refactor)

The classic test-driven development cycle, enforced step by step:

1. **Red** — Write a failing test first
2. **Green** — Write minimal implementation to pass
3. **Refactor** — Clean up while keeping tests green

```
/let's TDD a shopping cart total function
/dev-workflows:tdd shipping cost calculator
```

### Code Review

Systematic review covering four dimensions: correctness, readability, security, test coverage. Outputs a structured report.

```
/review the latest commit
/dev-workflows:review PR #42
```

### Systematic Debugging

Five-step debugging workflow: reproduce → isolate → root cause → fix → verify.

```
/debug this test failure in CI
/dev-workflows:debug the user login timeout issue
```

## Usage

The workflows activate automatically when you use relevant language ("let's TDD this", "review this code", "debug this"). You can also invoke them directly via slash commands:

| Command | Workflow |
|---------|----------|
| `/dev-workflows:tdd <feature>` | TDD cycle |
| `/dev-workflows:review <code/diff>` | Code review |
| `/dev-workflows:debug <issue>` | Debugging session |

## Notes

- The TDD workflow is loaded automatically at session start
- These workflows are opinionated — they enforce a specific process for consistency
- Feel free to ask the agent which step it's on at any point
