// Package cmd holds every command. One file per command; the root wires them.
package cmd

import (
	"github.com/spf13/cobra"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/version"
)

// New builds the root command with its subcommands; tests call it with their own output.
func New() *cobra.Command {
	root := &cobra.Command{
		Use:           "{{ cookiecutter.project_slug }}",
		Short:         "{{ cookiecutter.description }}",
		Version:       version.Version,
		SilenceUsage:  true,
		SilenceErrors: true,
	}
	root.SetVersionTemplate("{{ '{{' }}.Name{{ '}}' }} {{ '{{' }}.Version{{ '}}' }}\n")

	root.AddCommand(versionCommand(), helloCommand(), sumCommand())

	return root
}

// Execute runs the root command with os.Args.
func Execute() error {
	return New().Execute()
}
