# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
go install github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}@latest
```

## Run

```bash
go run . version
go run . hello
go run . hello --name Fernando
go build -o {{ cookiecutter.project_slug }} .
```

## Test / lint

```bash
go test ./...
go vet ./...
gofmt -l .
```

## Layout

```
main.go                     calls cmd.Execute()
cmd/
├── root.go                 root command, version and hello
└── root_test.go            runs commands against a buffer
internal/version/version.go Version, written from the release tag
```

A new command is a function returning `*cobra.Command`, added in `New()`. Keep the body small and call plain functions.
