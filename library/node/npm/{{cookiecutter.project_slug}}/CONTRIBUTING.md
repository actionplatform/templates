# Contributing

## Commit style

```
ICON TYPE: Comment in English
```

| Icon | Type     | When                                       |
|------|----------|--------------------------------------------|
| ⚙️   | FEATURE  | New feature                                |
| 🪲   | BUG      | Bug fix                                    |
| 📘   | DOCS     | Documentation                              |
| ❤️   | TEST     | Automated tests                            |
| ⬆️   | CI/CD    | Continuous integration / delivery          |
| ⚠️   | SECURITY | Security improvements                      |
| 📝   | LINT   | Formatting / lint fixes                    |
| 📦   | NPM    | Releases and dependency updates            |

One commit per concern. Stage files explicitly — never `git add .`.

## Release

Tag `vX.Y.Z` and publish a GitHub release. The `publish-npm` workflow writes `LAST_VERSION` from the tag, runs tests and lint, and publishes to npm.
