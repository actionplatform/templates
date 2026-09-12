package {{ cookiecutter.package_name }}

import "testing"

func TestHello(t *testing.T) {
	if got := Hello(""); got != "hello, world" {
		t.Fatalf("Hello(\"\") = %q", got)
	}
	if got := Hello("ana"); got != "hello, ana" {
		t.Fatalf("Hello(ana) = %q", got)
	}
}
