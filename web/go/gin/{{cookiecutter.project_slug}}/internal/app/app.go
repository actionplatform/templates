// Package app wires the router. Handlers live under api/, business logic under service/.
package app

import (
	"github.com/gin-gonic/gin"

	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/api"
	v1 "github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/api/v1"
)

const Version = "0.1.0"

const APIV1Prefix = "/api/v1"

func New() *gin.Engine {
	r := gin.New()
	r.Use(gin.Logger(), gin.Recovery())

	r.GET("/ping", api.Ping(Version))
	v1.Register(r.Group(APIV1Prefix))

	return r
}
