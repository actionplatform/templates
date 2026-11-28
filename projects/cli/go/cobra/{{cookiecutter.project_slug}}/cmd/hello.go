package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

func helloCommand() *cobra.Command {
	var name string

	command := &cobra.Command{
		Use:   "hello",
		Short: "Say hello",
		Args:  cobra.NoArgs,
		RunE: func(cmd *cobra.Command, args []string) error {
			_, err := fmt.Fprintf(cmd.OutOrStdout(), "hello, %s\n", name)

			return err
		},
	}
	command.Flags().StringVarP(&name, "name", "n", "world", "who to greet")

	return command
}
