package items

import (
	"errors"
	"strings"
	"testing"
)

func TestCreateTrimsAndAssignsIDs(t *testing.T) {
	s := NewStore()

	first, err := s.Create("  pen ")
	if err != nil || first.ID != 1 || first.Name != "pen" {
		t.Fatalf("got %+v %v", first, err)
	}

	second, _ := s.Create("ink")
	if second.ID != 2 {
		t.Fatalf("got id %d", second.ID)
	}
}

func TestCreateRejectsBadNames(t *testing.T) {
	s := NewStore()

	for _, name := range []string{"", "   ", strings.Repeat("x", maxName+1)} {
		if _, err := s.Create(name); !errors.Is(err, ErrInvalid) {
			t.Fatalf("%q: got %v", name, err)
		}
	}
}

func TestGetUnknownIsNotFound(t *testing.T) {
	if _, err := NewStore().Get(7); !errors.Is(err, ErrNotFound) {
		t.Fatalf("got %v", err)
	}
}

func TestListIsOrdered(t *testing.T) {
	s := NewStore()
	for _, name := range []string{"a", "b", "c"} {
		_, _ = s.Create(name)
	}

	got := s.List()
	if len(got) != 3 || got[0].Name != "a" || got[2].Name != "c" {
		t.Fatalf("got %+v", got)
	}
}
