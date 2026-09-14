package {{ cookiecutter.package_name }}

import (
	"os"
	"strings"
	"testing"
)

func TestVersion(t *testing.T) {
	raw, err := os.ReadFile("LAST_VERSION")
	if err != nil {
		t.Fatalf("read LAST_VERSION: %v", err)
	}
	want := strings.TrimSpace(string(raw))
	if Version != want {
		t.Fatalf("Version = %q, want %q", Version, want)
	}
}
