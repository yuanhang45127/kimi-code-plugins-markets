---
description: Generate a conventional commit message from staged changes
---

Analyse the staged git changes and generate a conventional commit message. Use `git diff --cached` to inspect the diff, determine the appropriate commit type (feat, fix, docs, style, refactor, test, chore), and produce a message following the format:

```
<type>(<scope>): <short summary>

<optional body>
```

$ARGUMENTS
