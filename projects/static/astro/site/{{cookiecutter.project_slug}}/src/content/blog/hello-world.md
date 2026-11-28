---
title: Hello, world
description: The first post, and how posts are written.
date: 2025-01-15
---

Every post is a Markdown file in `src/content/blog`. The file name becomes the
URL: this one lives at `/blog/hello-world/`.

The front matter is checked against the schema in `src/content.config.ts`, so
a missing title or a bad date fails the build instead of reaching production.

## Writing a post

Add a file, fill in `title`, `description` and `date`, and write. Set
`draft: true` to keep a post out of the index and out of the build.
