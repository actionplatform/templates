package v1

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Hello is a dummy endpoint. Replace with real resources.
func Hello(c *gin.Context) {
	name := c.DefaultQuery("name", "world")
	c.JSON(http.StatusOK, gin.H{"message": "hello, " + name})
}
