package main

import (
	"context"
	"log"
	"net"
	"os"
	"os/signal"
	"syscall"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/app"
)

func main() {
	httpPort := env("PORT", "8000")
	grpcPort := env("GRPC_PORT", "50051")

	grpcLn, err := net.Listen("tcp", ":"+grpcPort)
	if err != nil {
		log.Fatal(err)
	}

	httpLn, err := net.Listen("tcp", ":"+httpPort)
	if err != nil {
		log.Fatal(err)
	}

	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer stop()

	log.Printf("grpc on :%s, http /health on :%s", grpcPort, httpPort)

	if err := app.New().Serve(ctx, grpcLn, httpLn); err != nil {
		log.Fatal(err)
	}
}

func env(key, fallback string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}

	return fallback
}
