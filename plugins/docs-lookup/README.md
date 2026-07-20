# Docs Lookup Plugin for Kimi Code

Fetches live library documentation from official sources — reduces hallucinations about API signatures and usage.

Inspired by [Context7](https://github.com/context7/context7) for Claude Code.

## How it works

The plugin loads the `lookup-docs` skill at session start, which teaches Kimi how to:

1. Identify the library's ecosystem (npm, PyPI, Go, crates.io, etc.)
2. Fetch version-specific documentation from the official registry
3. Read source-level API signatures and type definitions
4. Present a concise, cited summary

## Usage

Ask naturally about any library's API:

```
How do I use the new React 19 use() hook?
What's the correct signature for Pydantic v2 Field?
Show me how to configure Vite 6 with React
```

Or use the slash command:

```
/docs-lookup:quick-docs react 19
/docs-lookup:quick-docs pydantic 2
```

## What makes it different

Instead of relying on training data that may be outdated, Kimi fetches the actual docs at query time. This eliminates the most common category of AI hallucination: fabricated method signatures.

## Notes

- The plugin relies on Kimi Code's built-in web fetching capabilities
- For best results, specify the library version when asking
