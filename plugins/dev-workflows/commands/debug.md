---
description: Debug an issue using systematic reproduction, isolation, root cause analysis, and verification
---

Debug this issue: $ARGUMENTS

Follow the debug-workflow skill:
1. **Reproduce** — get exact steps/input that triggers the bug
2. **Isolate** — narrow down the failing code path (binary search, check assumptions)
3. **Root cause** — understand WHY it fails (logic error? race condition? API misuse?)
4. **Fix** — minimal change that addresses root cause
5. **Verify** — confirm fix works and existing tests still pass
