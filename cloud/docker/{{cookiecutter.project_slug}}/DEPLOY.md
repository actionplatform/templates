# Deploy — Docker

Overlay `cloud/docker`. One image, port 8000.

```bash
docker compose up --build        # http://localhost:8000
docker build -t {{ cookiecutter.project_slug }} .
```

Push the image to any registry and run it on Dokploy, ECS, Fly, a VPS — the `[deploy]` section of `platform.toml` picks the target for `action-platform deploy`.
