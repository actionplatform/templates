package cmd

import (
	"bytes"
	"strings"
	"testing"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/version"
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
	if got := run(t, "hello", "--name", "Ana"); got != "hello, Ana" {
		t.Fatalf("got %q", got)
	}
}
