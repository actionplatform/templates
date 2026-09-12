# Service — postgres

Provisions a PostgreSQL database for `{{ cookiecutter.project_slug }}` and exposes it as env vars.

Provider: **{{ cookiecutter.provider }}**

```bash
./services/postgres/link        # prints the env vars; `eval "$(./services/postgres/link)"` to load them
```

| Var | Meaning |
|-----|---------|
| `DATABASE_URL` | `postgresql://user:pass@host:5432/db` |
