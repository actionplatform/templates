---
name: conventional-commit
description: Write a Conventional Commits message for the staged changes. Use when the user asks for a commit message or is about to commit.
---

# Conventional commit

1. Run `git diff --staged`. If nothing is staged, say so and stop.
2. Pick the type that fits the change: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` or `revert`.
3. Add a scope in parentheses when the change sits in one module or directory.
4. Write the subject as `type(scope): description`, imperative, lowercase, no trailing period, at most 72 characters.
5. Add a body only when the reason is not obvious from the diff. Wrap it at 72 characters.
6. Mark a breaking change with `!` after the type or scope and a `BREAKING CHANGE:` footer.

Print the message and nothing else. Do not run `git commit` unless the user asks.
