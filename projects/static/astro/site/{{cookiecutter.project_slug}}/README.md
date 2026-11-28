# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}A static [Astro](https://astro.build) site: a landing page and a blog. `npm run build` writes plain HTML to `dist/`.

## Install

```bash
nvm use
npm ci
```

## Run

```bash
npm run dev            # http://localhost:4321
npm run build          # type-check + dist/
npm run preview        # serves dist/
```

## Container

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 -e PORT=8000 {{ cookiecutter.project_slug }}
curl -i localhost:8000/health
```

The image is optional: `dist/` is the artifact, and any web server or CDN can serve it. The Dockerfile builds the site and copies `dist/` into an unprivileged nginx that listens on `$PORT` (default `8000`) and answers `GET /health` with `200`.

## Test / lint

```bash
npm test
npm run lint           # eslint + astro check
npm run format
npm run build
```

## Layout

```
astro.config.mjs
src/
├── content.config.ts   the blog collection and its schema
├── content/blog/       one Markdown file per post
├── layouts/Layout.astro
├── lib/posts.ts        sorting, drafts, reading time, dates
├── pages/
│   ├── index.astro     landing page
│   ├── 404.astro
│   └── blog/
│       ├── index.astro     post list
│       └── [slug].astro    one page per post
└── styles/global.css
public/                 copied to dist/ as is
tests/posts.test.ts     unit tests for src/lib/posts.ts
Dockerfile              build, then nginx on $PORT
nginx.conf.template     /health and the static root
```

Adding a post: drop a Markdown file in `src/content/blog/` with `title`, `description` and `date` (`draft: true` hides it).
