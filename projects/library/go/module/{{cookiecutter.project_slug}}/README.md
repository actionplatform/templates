# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Install

```bash
go get {{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}
```

## Usage

```go
import "{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}"

{{ cookiecutter.package_name }}.Hello("ana") // "hello, ana"
```

## Develop

```bash
go test ./...
go vet ./...
gofmt -l .
```

Lint config: `.code_quality/.golangci.yml` (`golangci-lint run -c .code_quality/.golangci.yml`).
