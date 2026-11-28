package cmd

import (
	"fmt"
	"strconv"

	"github.com/spf13/cobra"
)

func sumCommand() *cobra.Command {
	return &cobra.Command{
		Use:   "sum NUMBER...",
		Short: "Add integers",
		Args:  cobra.MinimumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			total, err := sum(args)
			if err != nil {
				return err
			}

			fmt.Fprintln(cmd.OutOrStdout(), total)

			return nil
		},
	}
}

func sum(args []string) (int, error) {
	total := 0

	for _, arg := range args {
		n, err := strconv.Atoi(arg)
		if err != nil {
			return 0, fmt.Errorf("not an integer: %q", arg)
		}

		total += n
	}

	return total, nil
}
