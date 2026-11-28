package version

import "testing"

func TestString(t *testing.T) {
	Version, Commit, Date = "1.2.3", "abc1234", "2026-01-02T03:04:05Z"
	want := "1.2.3 (commit abc1234, built 2026-01-02T03:04:05Z)"

	if got := String(); got != want {
		t.Fatalf("got %q, want %q", got, want)
	}
}
