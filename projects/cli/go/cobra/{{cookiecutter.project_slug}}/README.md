# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Install

Download the archive for your system from the [releases page](https://{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/releases), check it against `checksums.txt`, and put the binary on your `PATH`.

```bash
tar -xzf {{ cookiecutter.project_slug }}_<version>_<os>_<arch>.tar.gz
sha256sum --check --ignore-missing checksums.txt
```

With Go:

```bash
go install {{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}@latest
```

Archives exist for linux, darwin and windows (zip), on amd64 and arm64.

## Run

```bash
go run . --help
go run . version
go run . hello --name Ana
go run . sum 1 2 39
```

## Test

```bash
go test ./...
go vet ./...
gofmt -l .
golangci-lint run -c .code_quality/.golangci.yml
```

## Build and release

```bash
go build -ldflags "-X {{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/version.Version=1.2.3" -o {{ cookiecutter.project_slug }} .
goreleaser release --snapshot --clean
```

A release is a `v*` tag. `.goreleaser.yaml` builds the binaries with version, commit and date injected through ldflags, packs the archives, writes `checksums.txt` and the changelog. With `ci = "github"`, `.github/workflows/release.yml` runs it on the tag and publishes the GitHub release; on other hosts `.goreleaser.yaml` stays and you run `goreleaser release --clean` from your pipeline.

## Layout

```
main.go                      calls cmd.Execute(), prints the error
cmd/
├── root.go                  root command and --version
├── version.go               version, commit and build date
├── hello.go                 hello --name
├── sum.go                   sum NUMBER...
└── root_test.go             runs commands against a buffer
internal/version/            Version, Commit, Date set by ldflags
.goreleaser.yaml             targets, archives, checksums, changelog
.github/workflows/release.yml  goreleaser on v* tags
.code_quality/.golangci.yml  golangci-lint rules
```

A new command is a function returning `*cobra.Command`, added in `New()`. Keep the body small and call plain functions.
