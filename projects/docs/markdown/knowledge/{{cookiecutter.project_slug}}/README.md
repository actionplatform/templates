# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}Plain Markdown, read on the code host. No build, no site.

## Run

Nothing to run: open [`docs/index.md`](docs/index.md). Agents read [`AGENTS.md`](AGENTS.md) (Claude Code through [`CLAUDE.md`](CLAUDE.md)) and the skills under `.claude/skills/`.

## Test

```bash
npm ci
npm run lint
npm test
```

`npm run lint` checks the Markdown format with Prettier (`npm run format` fixes it); `npm test` fails on a broken relative link or heading anchor.

## Layout

```
docs/                    the pages; docs/index.md is the entry point
.claude/skills/add-page/ example agent skill: how to add a page
AGENTS.md                rules for agents and contributors
CLAUDE.md                points Claude Code at AGENTS.md
.code_quality/           Prettier and remark config
```
