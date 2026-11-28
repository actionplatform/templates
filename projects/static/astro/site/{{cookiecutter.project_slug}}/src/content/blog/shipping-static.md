---
title: Shipping a static site
description: What the build produces and how it is served.
date: 2025-02-10
---

`npm run build` writes plain HTML, CSS and assets to `dist/`. There is no
server to run: any web server or CDN can serve the folder as it is.

## Serving it

The Dockerfile copies `dist/` into an nginx image that listens on `$PORT` and
answers `GET /health` with `200`, which is what a container platform asks
before sending traffic.
