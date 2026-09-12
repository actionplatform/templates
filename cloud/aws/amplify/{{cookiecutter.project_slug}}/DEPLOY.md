# Deploy — AWS Amplify Hosting

Overlay `cloud/aws/amplify`. Amplify builds the app from the repo on every push to a connected branch; the workflow only triggers the build and waits, so GitHub shows the real result.

## One-time setup

1. Amplify console → New app → connect this repo. Connect `develop` (dev) and `master`/`main` (prod).
2. Build settings: Amplify reads `amplify.yml` from the repo. Add env vars there (`REACT_APP_API_URL`).
3. Security headers come from `customHttp.yml`.
4. GitHub → environment `dev` and `prod`: var `AMPLIFY_APP_ID`, secret `AWS_DEPLOY_ROLE_ARN` (OIDC role with `amplify:StartJob`, `amplify:ListJobs`, `amplify:GetJob`).

## Files

```
amplify.yml        # build spec: npm ci, lint, test, build → build/
customHttp.yml     # security headers
.github/workflows/deploy.yml
```
