package cmd

import (
	"fmt"

	"github.com/spf13/cobra"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/version"
)

func versionCommand() *cobra.Command {
	return &cobra.Command{
		Use:   "version",
		Short: "Print version, commit and build date",
		Args:  cobra.NoArgs,
		RunE: func(cmd *cobra.Command, args []string) error {
			_, err := fmt.Fprintln(cmd.OutOrStdout(), version.String())

			return err
		},
	}
}
