# AGENTS.md

Rules.

## Commits

[Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): `type(scope)!: description`, in English, imperative, lowercase, no period.

| Type       | When                       | SemVer |
| ---------- | -------------------------- | ------ |
| `feat`     | new feature                | minor  |
| `fix`      | bug fix                    | patch  |
| `docs`     | documentation only         | —      |
| `style`    | formatting, no code change | —      |
| `refactor` | neither fix nor feature    | —      |
| `perf`     | performance                | patch  |
| `test`     | tests                      | —      |
| `build`    | build system, dependencies | —      |
| `ci`       | CI config and scripts      | —      |
| `chore`    | maintenance, releases      | —      |
| `revert`   | reverts a commit           | —      |

`!` after the type/scope, or a `BREAKING CHANGE:` footer, marks a major bump. One commit per concern; stage files explicitly — never `git add .`. CI enforces the format on every pull request (`conventional-commit` workflow).

## Branches

Git-flow, enforced by git hooks locally (`action-platform install` once per clone) and by CI on pull requests:

- Work on `<kind>/<code>[-slug]` — `action-platform branch feature 42 login`. Kinds: `feature bugfix hotfix release support chore docs refactor test ci perf`.
- Never commit on `main`, `master` or `develop`; the release tool is the only thing that does.
- `feature`/`bugfix`/… merge into `develop` (or the default branch when there is no `develop`); `release`/`hotfix` into `main` and `develop`.

## Enforced on the code host

With `[gitflow.protection] enforce = true` in `platform.toml`, the platform protects `main`, `master` and `develop` on GitHub, GitLab or Bitbucket: no direct push, no force push, no deletion. Changes merge only through a pull request whose `gitflow` and `conventional-commit` checks, and the project's CI, pass. Only the platform's own identity pushes `chore(release)` commits; nobody else bypasses this, owners included.

## Layout

```
app/
├── Http/Controllers/   HTTP: call the model, write the response (HealthController, ItemController)
├── Http/Requests/      validation rules for a request body
├── Models/             Eloquent models
└── Providers/
bootstrap/app.php       routing (/health, /api/v1) and JSON error rendering
routes/api.php          every API route
database/               migrations, factories, the SQLite file
tests/Feature/          the HTTP contract
.code_quality/          pint.json, phpstan.neon
```

`app/Services/` is created on demand; keep rules out of controllers once they grow.

## Checks before a PR

```bash
composer lint
composer analyse
composer test
```

## Do not

- Add settings/config modules; read env vars through `config/` only.
- Hardcode secrets, URLs of other environments, or account ids.
- Edit `LAST_VERSION` by hand — the release workflow writes it from the tag.
