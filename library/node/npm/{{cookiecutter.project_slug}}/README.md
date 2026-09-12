# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
npm install @{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
```

## Develop

```bash
nvm use
npm ci
npm test
npm run lint
npm run format
npm run build
```

## Layout

```
src/index.ts      # public API
tests/            # vitest
.code_quality/    # eslint, prettier, tsconfig
```
