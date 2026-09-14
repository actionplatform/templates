package main

import (
	"os"

	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/cmd"
)

func main() {
	if err := cmd.Execute(); err != nil {
		os.Exit(1)
	}
}
