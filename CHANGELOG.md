# Changelog

## v0.2.0 — 2026-09-19

### Refactoring
- **cloud:** clouds live in plugins; one Dockerfile for the docker overlay

## v0.1.5 — 2026-09-16

### Bug Fixes
- **cloud:** aws/lambda Ruby recipe and handler — synced from apx-aws-lambda

## v0.1.4 — 2026-09-16

### Bug Fixes
- **cloud:** aws/lambda Ruby package without puma and rackup — synced from apx-aws-lambda

## v0.1.3 — 2026-09-15

### Breaking Changes
- **cloud:** aws/lambda overlay for every web language — synced from apx-aws-lambda

### Bug Fixes
- **ruby:** the health API class is HealthApi — app.rb mounts it under that name

## v0.1.2 — 2026-09-15

### Breaking Changes
- **web:** the health route is GET /health on every web template — API Gateway reserves /ping on execute-api and answers it itself

### Features
- **web:** ruby sinatra template with ping and items across five layers
- **index:** index.json is the catalog — types, stacks, frameworks and icons; index.toml, repo-level CI and lint config removed; README index with links
- **matrix:** register the six templates
- **automation:** automation/python/basic and scheduled
- **cobra:** library/go/cobra — Go CLI with Cobra
- **typer:** library/python/typer — Python CLI with Typer
- **react-vite:** web/node/react-vite — React + TypeScript + Vite + Vitest
- **fastify:** web/node/fastify — Fastify + TypeScript + Vitest

### Bug Fixes
- **go:** no trailing space in the package comment when the description is empty
- **python:** version test formatted the same for any package name
- **automation:** keep argparse call exploded so ruff format is stable for any description
- **rust:** rustfmt-clean lib.rs even with an empty description
- **kotlin:** package name derived from the slug without underscores, whatever package_name is passed

### Docs
- **index:** register web/ruby/sinatra and the ruby stack
- catalog table with icons; --directory paths under projects/

### Chores
- **templates:** every generated project starts at 0.0.0 until its first release

## v0.1.1 — 2026-09-14

### Features
- **kotlin:** Spring Boot web API template in Kotlin with the same layers, ktlint
- **java:** Spring Boot web API template with the same layers, checkstyle
- **gin:** handlers, services and models; ping and items as the example resource
- **fastapi:** layered layout — api, schemas, services, repositories, core/errors; ping and items as the example resource
- **ci:** Bitbucket Pipelines for every project template
- **projects:** record ci in platform.toml
- **projects:** drop tracked .githooks, hooks come from the CLI; pin trivy-action v0.36.0

### Bug Fixes
- **library:** version tests compare against LAST_VERSION instead of a literal

### Docs
- register web/java/spring and web/kotlin/spring in the matrix

### CI
- **trivy:** fail on findings, upload sarif only on public repositories
- **trivy:** grant actions:read so upload-sarif can report

### Chores
- **platform:** update configuration
