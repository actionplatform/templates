# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Run

```bash
go run ./cmd/server        # http://localhost:8000/ping
```

`ADDR` overrides the listen address (default `:8000`).

## Test / lint

```bash
go test ./...
go vet ./...
gofmt -l .
```

## Layout

```
cmd/server/main.go        # main only: env, app.New, Run
internal/
├── app/app.go            # router, middlewares, groups; Version
├── api/                  # HTTP handlers: parse request, write response
│   ├── ping.go           # GET /ping
│   └── v1/
│       ├── router.go     # Register(group) — mounts every v1 route
│       └── hello.go      # dummy, one file per resource
├── service/              # business rules — never imports gin
├── repository/           # data access — never imports gin
└── model/                # domain structs
```

`service/`, `repository/` and `model/` are created on demand; the handler → service → repository chain is the rule.
