---
name: add-page
description: Add a page to this knowledge repository. Use when asked to write down, document or record something new in the docs.
---

# Add a page

1. Pick a short kebab-case file name and create `docs/<name>.md` with one `#` title.
2. Write the content in plain Markdown. Link other pages with relative paths.
3. Add a link to the new page under `## Pages` in `docs/index.md`.
4. Run `npm run format` and `npm test`; fix every broken link it reports.
