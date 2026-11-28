// Package version holds the build identity, injected by ldflags at release time.
package version

import "fmt"

var (
	Version = "0.0.0"
	Commit  = "none"
	Date    = "unknown"
)

func String() string {
	return fmt.Sprintf("%s (commit %s, built %s)", Version, Commit, Date)
}
