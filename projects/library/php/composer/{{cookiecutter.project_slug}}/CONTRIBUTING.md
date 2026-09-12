# Contributing

## Commit style

[Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): `type(scope)!: description`, in English, imperative, lowercase, no period.

| Type | When | SemVer |
|------|------|--------|
| `feat` | new feature | minor |
| `fix` | bug fix | patch |
| `docs` | documentation only | — |
| `style` | formatting, no code change | — |
| `refactor` | neither fix nor feature | — |
| `perf` | performance | patch |
| `test` | tests | — |
| `build` | build system, dependencies | — |
| `ci` | CI config and scripts | — |
| `chore` | maintenance, releases | — |
| `revert` | reverts a commit | — |

`!` after the type/scope, or a `BREAKING CHANGE:` footer, marks a major bump. One commit per concern; stage files explicitly — never `git add .`. CI enforces the format on every pull request (`conventional-commit` workflow).

## Release

Tag `vX.Y.Z` and publish a GitHub release. The `publish-packagist` workflow writes `LAST_VERSION` from the tag, runs tests and lint, and tells Packagist to fetch the tag.
