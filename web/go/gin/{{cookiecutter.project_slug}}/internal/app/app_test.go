package app

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func get(t *testing.T, path string) (int, map[string]any) {
	t.Helper()
	w := httptest.NewRecorder()
	New().ServeHTTP(w, httptest.NewRequest(http.MethodGet, path, nil))
	var body map[string]any
	if err := json.Unmarshal(w.Body.Bytes(), &body); err != nil {
		t.Fatalf("invalid json: %v", err)
	}
	return w.Code, body
}

func TestPing(t *testing.T) {
	code, body := get(t, "/ping")
	if code != http.StatusOK || body["status"] != "ok" || body["version"] != Version {
		t.Fatalf("got %d %v", code, body)
	}
}

func TestHello(t *testing.T) {
	code, body := get(t, "/api/v1/hello?name=ana")
	if code != http.StatusOK || body["message"] != "hello, ana" {
		t.Fatalf("got %d %v", code, body)
	}
}
