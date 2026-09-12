package main

import (
	"log"
	"os"

	"github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}/internal/app"
)

func main() {
	addr := os.Getenv("ADDR")
	if addr == "" {
		addr = ":8000"
	}
	r := app.New()
	log.Printf("listening on %s", addr)
	if err := r.Run(addr); err != nil {
		log.Fatal(err)
	}
}
