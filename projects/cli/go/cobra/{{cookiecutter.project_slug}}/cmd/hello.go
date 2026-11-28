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
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Fprintf(cmd.OutOrStdout(), "hello, %s\n", name)
		},
	}
	command.Flags().StringVarP(&name, "name", "n", "world", "who to greet")

	return command
}
