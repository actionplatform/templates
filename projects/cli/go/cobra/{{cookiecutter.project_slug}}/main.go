package main

import (
	"fmt"
	"os"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/cmd"
)

func main() {
	if err := cmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}
