# Action Platform — Templates

Cookiecutter templates for bootstrapping projects on the Action Platform.

## Usage

```bash
pipx install cookiecutter

cookiecutter gh:actionplatform/templates --directory web/python
cookiecutter gh:actionplatform/templates --directory plugin/wordpress
```

Or via the CLI:

```bash
action-platform init                # interactive: type → stack → name
action-platform init web python     # direct
action-platform init --list         # show available matrix
```

## Matrix

| Type      | Stacks                        |
|-----------|-------------------------------|
| `web`     | python, go, php, java         |
| `api`     | python, go, java, node        |
| `library` | python, go, php, node         |
| `cli`     | python, go, rust              |
| `plugin`  | wordpress, chrome             |
| `empty`   | — (only `platform.toml` + `.code_quality/`) |

`plugin` second level is the **host system**, not the language (language is imposed by the host).

## Structure

```
templates/
├── index.toml                 # matrix read by the CLI
├── web/python/
├── web/go/
├── library/python/
├── plugin/wordpress/
├── plugin/chrome/
└── empty/
```

Each leaf directory is an independent cookiecutter template with its own `cookiecutter.json`. Select it with `--directory <type>/<stack>`.

## Conventions

- Every template ships `platform.toml` so the project works with `action-platform release` and `deploy` out of the box.
- Every template ships `.code_quality/` with the stack's lint/format config.
- Variables are declared in `cookiecutter.json`; keep defaults sensible.

## Related

- [action-platform](https://github.com/actionplatform/action-platform) — CLI and core
- [strategy](https://github.com/actionplatform/strategy) — vision and decisions
