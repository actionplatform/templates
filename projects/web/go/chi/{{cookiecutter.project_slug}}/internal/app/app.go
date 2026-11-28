// Package app builds the router and mounts every route.
package app

import (
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/handlers"
	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/services"
)

const Version = "0.0.0"

const APIV1Prefix = "/api/v1"

func New() http.Handler {
	items := handlers.NewItems(services.NewItems())

	r := chi.NewRouter()
	r.Use(middleware.Logger, middleware.Recoverer)

	r.Get("/health", handlers.Health(Version))

	r.Route(APIV1Prefix, func(v1 chi.Router) {
		v1.Get("/items", items.List)
		v1.Post("/items", items.Create)
		v1.Get("/items/{id}", items.Get)
	})

	return r
}
