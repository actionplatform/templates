# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
npm install @{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
```

## Usage

```ts
import { hello } from "@{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}";

hello("ana"); // "hello, ana"
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
src/hello.ts      # hello() — dummy
tests/            # vitest
.code_quality/    # eslint, prettier, tsconfig
```

## Publish

Releasing does not publish. The platform deploys a release to a scope — `npm-next` (dist-tag `next`) for candidates, `npm` (`latest`) for stable releases — by dispatching `.github/workflows/publish.yml` on the tag with `version` and `registry`; the workflow publishes with provenance through npm trusted publishing (link the repository to the package on npmjs.com once). `platform.toml` declares both targets.
