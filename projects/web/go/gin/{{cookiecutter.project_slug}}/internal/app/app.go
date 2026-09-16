// Package app builds the router and mounts every route.
package app

import (
	"github.com/gin-gonic/gin"

	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/handlers"
	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/services"
)

const Version = "0.1.3"

const APIV1Prefix = "/api/v1"

func New() *gin.Engine {
	items := handlers.NewItems(services.NewItems())

	r := gin.New()
	r.Use(gin.Logger(), gin.Recovery())

	r.GET("/health", handlers.Health(Version))

	v1 := r.Group(APIV1Prefix)
	v1.GET("/items", items.List)
	v1.POST("/items", items.Create)
	v1.GET("/items/:id", items.Get)

	return r
}
