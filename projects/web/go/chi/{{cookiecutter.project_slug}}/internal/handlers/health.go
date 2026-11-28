// Package handlers is the HTTP layer: parse the request, call a service, write the response.
package handlers

import (
	"net/http"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/models"
)

// Health reports the version. Every API exposes it at /health.
func Health(version string) http.HandlerFunc {
	return func(w http.ResponseWriter, _ *http.Request) {
		writeJSON(w, http.StatusOK, models.Health{Status: "ok", Version: version})
	}
}
