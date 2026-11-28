// Package items holds the business rules. It knows nothing of gRPC.
package items

import (
	"errors"
	"fmt"
	"sort"
	"strings"
	"sync"
)

const maxName = 40

var ErrInvalid = errors.New("invalid")

var ErrNotFound = errors.New("not found")

type Item struct {
	ID   int64
	Name string
}

// Store keeps items in memory, standing in for a database or an external API. Replace the storage; keep the methods.
type Store struct {
	mu     sync.Mutex
	rows   map[int64]Item
	lastID int64
}

func NewStore() *Store {
	return &Store{rows: map[int64]Item{}}
}

// List returns every item ordered by id.
func (s *Store) List() []Item {
	s.mu.Lock()
	defer s.mu.Unlock()

	out := make([]Item, 0, len(s.rows))
	for _, item := range s.rows {
		out = append(out, item)
	}

	sort.Slice(out, func(i, j int) bool { return out[i].ID < out[j].ID })

	return out
}

// Get returns one item or ErrNotFound.
func (s *Store) Get(id int64) (Item, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	item, ok := s.rows[id]
	if !ok {
		return Item{}, fmt.Errorf("%w: item %d", ErrNotFound, id)
	}

	return item, nil
}

// Create validates the name and stores the item.
func (s *Store) Create(name string) (Item, error) {
	name = strings.TrimSpace(name)

	if name == "" {
		return Item{}, fmt.Errorf("%w: name is required", ErrInvalid)
	}

	if len(name) > maxName {
		return Item{}, fmt.Errorf("%w: name is longer than %d characters", ErrInvalid, maxName)
	}

	s.mu.Lock()
	defer s.mu.Unlock()

	s.lastID++
	item := Item{ID: s.lastID, Name: name}
	s.rows[item.ID] = item

	return item, nil
}
