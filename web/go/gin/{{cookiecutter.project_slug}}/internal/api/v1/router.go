// Package v1 holds every versioned handler. One file per resource.
package v1

import "github.com/gin-gonic/gin"

// Register mounts every v1 route on the group.
func Register(g *gin.RouterGroup) {
	g.GET("/hello", Hello)
}
