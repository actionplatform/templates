// Package cmd holds every command. One file per command; the root wires them.
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"

	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/version"
)

// New builds the root command with its subcommands; tests call it with their own output.
func New() *cobra.Command {
	root := &cobra.Command{
		Use:   "{{ cookiecutter.project_slug }}",
		Short: "{{ cookiecutter.description }}",
	}

	root.AddCommand(versionCommand(), helloCommand())

	return root
}

// Execute runs the root command with os.Args.
func Execute() error {
	return New().Execute()
}

func versionCommand() *cobra.Command {
	return &cobra.Command{
		Use:   "version",
		Short: "Print the version",
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Fprintln(cmd.OutOrStdout(), version.Version)
		},
	}
}

func helloCommand() *cobra.Command {
	var name string

	command := &cobra.Command{
		Use:   "hello",
		Short: "Say hello",
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Fprintf(cmd.OutOrStdout(), "hello, %s\n", name)
		},
	}
	command.Flags().StringVarP(&name, "name", "n", "world", "who to greet")

	return command
}
