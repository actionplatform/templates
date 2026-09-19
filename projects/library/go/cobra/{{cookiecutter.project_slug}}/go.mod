module github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}

go {{ cookiecutter._go_version }}

require github.com/spf13/cobra v1.8.1

require (
	github.com/inconshreveable/mousetrap v1.1.0 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
)
