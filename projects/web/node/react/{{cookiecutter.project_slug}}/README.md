# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
nvm use
npm ci
npm run dev          # http://localhost:3000 — /api proxied to :8000
```

`REACT_APP_API_URL` overrides the API base URL (defaults to `/api/v1`).

## Test / lint

```bash
npm test
npm run lint
npm run format:check
npm run build
```

## Layout (Atomic Design, no organisms tier)

```
src/
├── components/
│   ├── atoms/      # Button, ErrorBoundary
│   ├── molecules/  # composed atoms
│   ├── templates/  # layouts
│   └── pages/      # full pages, composed from the tiers above
├── hooks/          # all business logic lives here (useRequest)
├── stores/         # zustand
├── views/          # one file per route, renders a page
├── constants/
├── lib/
└── utils/
```

Rules: no hardcoded colors — use the CSS variables in `src/assets/main.css`; logic goes in `src/hooks/`, never in components.
