package cmd

import (
	"bytes"
	"strings"
	"testing"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/version"
)

func run(t *testing.T, args ...string) (string, error) {
	t.Helper()

	var out bytes.Buffer

	root := New()
	root.SetOut(&out)
	root.SetErr(&out)
	root.SetArgs(args)
	err := root.Execute()

	return strings.TrimSpace(out.String()), err
}

func TestVersionCommand(t *testing.T) {
	got, err := run(t, "version")
	if err != nil {
		t.Fatal(err)
	}

	if got != version.String() {
		t.Fatalf("got %q", got)
	}
}

func TestVersionFlag(t *testing.T) {
	got, err := run(t, "--version")
	if err != nil {
		t.Fatal(err)
	}

	if !strings.HasSuffix(got, version.Version) {
		t.Fatalf("got %q", got)
	}
}

func TestHello(t *testing.T) {
	cases := map[string][]string{
		"hello, world": {"hello"},
		"hello, Ana":   {"hello", "--name", "Ana"},
	}

	for want, args := range cases {
		got, err := run(t, args...)
		if err != nil || got != want {
			t.Fatalf("%v: got %q, %v", args, got, err)
		}
	}
}

func TestSum(t *testing.T) {
	got, err := run(t, "sum", "1", "2", "39")
	if err != nil || got != "42" {
		t.Fatalf("got %q, %v", got, err)
	}
}

func TestSumRejectsText(t *testing.T) {
	if _, err := run(t, "sum", "1", "x"); err == nil {
		t.Fatal("expected an error")
	}
}

func TestSumNeedsArguments(t *testing.T) {
	if _, err := run(t, "sum"); err == nil {
		t.Fatal("expected an error")
	}
}
