# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
go get github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
```

## Develop

```bash
go test ./...
go vet ./...
gofmt -l .
```

Lint config: `.code_quality/.golangci.yml` (`golangci-lint run -c .code_quality/.golangci.yml`).
