# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
nvm use
npm ci
```

## Run

```bash
npm run dev            # http://localhost:3000
npm run build          # type-check + dist/
npm run preview        # serves dist/
```

## Test / lint

```bash
npm test
npm run lint
npm run format
npm run build
```

## Layout

```
index.html              Vite entry
src/
├── main.tsx            mounts <App />
├── App.tsx             the page: name, description, platform note, docs link
├── styles.css
└── components/
    └── Welcome.tsx
tests/
├── setup.ts            jest-dom matchers
└── App.test.tsx        Testing Library, jsdom
```

No router, no state library, no UI kit — add them when a second page needs them.
