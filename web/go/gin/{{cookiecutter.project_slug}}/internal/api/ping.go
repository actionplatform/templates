package api

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Ping reports the version. Every API exposes it at the root.
func Ping(version string) gin.HandlerFunc {
	return func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok", "version": version})
	}
}
