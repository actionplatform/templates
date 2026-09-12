# Service — postgres

Provisions a PostgreSQL database for `{{ cookiecutter.project_slug }}` and exposes it as env vars.

Provider: **{{ cookiecutter.provider }}**

```bash
./services/postgres/link        # prints the env vars; `eval "$(./services/postgres/link)"` to load them
```

| Var | Meaning |
|-----|---------|
| `DATABASE_URL` | `postgresql://user:pass@host:5432/db` |

With `aws-rds`, `requirements/policy.json` is the least privilege `up` needs (RDS, SSM parameter under `/{{ cookiecutter.project_slug }}/`, EC2 describe). Attach it to the deploy role after replacing `ACCOUNT_ID`.
