# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
bundle install
bundle exec rackup    # http://localhost:9292/ping
```

## Test / lint

```bash
bundle exec rspec
bundle exec rubocop
```

## Layout

Five layers; each one depends only on the ones below it.

```
app.rb                App.create, mounts every API
app/
├── version.rb        App::VERSION
├── api/              HTTP only — routes, status codes; no rules
│   ├── ping.rb       GET /ping
│   └── v1/           versioned APIs; items is the example resource
├── schemas/          Data — the contract of every response
├── services/         business rules; receive repositories, raise DomainError
├── repositories/     data access — one class per store, one method per query
└── core/             cross-cutting: errors, base_api
spec/
├── support/          helpers shared by every spec (Client)
├── api/              contract through rack-test
└── services/         rules, with a repository and no HTTP
```

`api` calls `services`, never a repository. `services` raise `DomainError` subclasses (`NotFoundError`, `ValidationError`, `ConflictError`); `core/base_api.rb` turns them into `{"detail": {"code", "message", "field"}}`. `repositories` hold no rules and no HTTP — the in-memory one behind `items` is the placeholder for a database or an external API.
