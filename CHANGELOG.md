# Changelog

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
