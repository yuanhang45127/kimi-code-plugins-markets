---
name: lookup-docs
description: Fetches live library documentation from official sources to answer API usage questions accurately
arguments:
  - library
  - version
---

# Lookup Documentation

When asked about a library's API, signature, or usage, follow this workflow:

## Step 1: Identify the library and ecosystem

| Ecosystem | Official registry docs URL | Notes |
|-----------|---------------------------|-------|
| npm/JS/TS | `https://www.npmjs.com/package/<name>` | Check for README and latest version |
| PyPI/Python | `https://pypi.org/project/<name>/` | Check for release history and docs link |
| Go | `https://pkg.go.dev/<module-path>` | Has full API reference |
| crates.io/Rust | `https://docs.rs/<crate>/latest/<crate>/` | Auto-generated docs with search |
| RubyGems | `https://www.rubydocs.org/gems/<gem>` | Versioned documentation |

## Step 2: Fetch version-specific information

When the user mentions a specific version (e.g. "React 19", "Next.js 16"), visit the versioned docs:

- npm: `https://www.npmjs.com/package/<name>/v/<version>`
- PyPI: `https://pypi.org/project/<name>/<version>/`
- `https://github.com/<owner>/<repo>/blob/v<version>/README.md`

## Step 3: Read source-level docs for specific APIs

For method signatures and type definitions, try:

- TypeScript: Check DefinitelyTyped or the package's bundled types
- Python: Read the source on GitHub for the relevant version tag
- Rust: `https://docs.rs/<crate>/<version>/<crate>/<module>/index.html`

## Step 4: Synthesise

Combine the fetched docs with your existing knowledge. If the docs show a different API than what you recall, trust the docs and explain the difference to the user.

## When invoked with arguments

- `$library` — the library name to look up
- `$version` — optional version constraint

Always cite the source URL so the user can verify the information.
