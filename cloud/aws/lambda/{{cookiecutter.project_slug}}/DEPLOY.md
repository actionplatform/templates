# Deploy — AWS Lambda (SAM)

Overlay `cloud/aws/lambda`. The app runs on Lambda (arm64, python3.12) behind an HTTP API Gateway. Dependencies build into a layer; code into the function.

## Local

```bash
pip install aws-sam-cli
sam build
sam local start-api            # http://127.0.0.1:3000/ping
sam deploy                     # dev stack: {{ cookiecutter.project_slug }}-dev
sam deploy --config-env prod   # prod stack: {{ cookiecutter.project_slug }}-prod
```

## CI

`.github/workflows/deploy.yml` deploys on push: `develop` → dev, `master`/`main` → prod. Per environment: secret `AWS_DEPLOY_ROLE_ARN` (OIDC role); optional `DOMAIN_NAME` var + `DOMAIN_CERTIFICATE_ARN` secret for a custom domain.

The handler calls `app.create_app()` — the convention every `web/python/*` template follows.

## Files

```
template.yaml        # SAM resources: function, deps layer, HTTP API
samconfig.toml       # dev / prod stacks
lambda_handler.py    # Mangum adapter
Makefile             # SAM build recipes
```
