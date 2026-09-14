package cmd

import (
	"bytes"
	"strings"
	"testing"

	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/version"
)

func run(t *testing.T, args ...string) string {
	t.Helper()
	var out bytes.Buffer
	root := New()
	root.SetOut(&out)
	root.SetArgs(args)
	if err := root.Execute(); err != nil {
		t.Fatalf("%v: %v", args, err)
	}
	return strings.TrimSpace(out.String())
}

func TestVersion(t *testing.T) {
	if got := run(t, "version"); got != version.Version {
		t.Fatalf("got %q", got)
	}
}

func TestHello(t *testing.T) {
	if got := run(t, "hello"); got != "hello, world" {
		t.Fatalf("got %q", got)
	}
	if got := run(t, "hello", "--name", "Fernando"); got != "hello, Fernando" {
		t.Fatalf("got %q", got)
	}
}
