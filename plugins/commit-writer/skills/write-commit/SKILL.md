---
name: write-commit
description: Generate a conventional commit message from staged git changes
---

# Write Commit Message

When asked to write a commit message, follow these steps:

1. Run `git diff --cached` to inspect the staged changes
2. Analyse the diff and determine the commit type:

   | Type       | When to use                                         |
   |------------|------------------------------------------------------|
   | `feat`     | A new feature                                        |
   | `fix`      | A bug fix                                            |
   | `docs`     | Documentation only changes                           |
   | `style`    | Formatting, missing semicolons, etc. (no logic change) |
   | `refactor` | Code change that neither fixes a bug nor adds a feature |
   | `test`     | Adding or updating tests                             |
   | `chore`    | Changes to build process, tooling, or dependencies   |

3. Format the message using Conventional Commits:

   ```
   <type>(<scope>): <short summary>

   <optional body explaining the what and why>
   ```

4. Present the generated message to the user and ask if they'd like to apply it
