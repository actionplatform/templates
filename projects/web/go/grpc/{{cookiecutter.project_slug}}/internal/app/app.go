// Package app wires the gRPC server, the health service and the HTTP /health the platform probes.
package app

import (
	"context"
	"encoding/json"
	"errors"
	"net"
	"net/http"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/health"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
	"google.golang.org/grpc/reflection"

	itemsv1 "{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/gen/items/v1"
	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/items"
	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/server"
)

const Version = "0.0.0"

type App struct {
	GRPC   *grpc.Server
	Health *health.Server
}

func New() *App {
	app := &App{GRPC: grpc.NewServer(), Health: health.NewServer()}

	itemsv1.RegisterItemServiceServer(app.GRPC, server.NewItems(items.NewStore()))
	healthpb.RegisterHealthServer(app.GRPC, app.Health)
	reflection.Register(app.GRPC)

	app.Health.SetServingStatus("", healthpb.HealthCheckResponse_SERVING)
	app.Health.SetServingStatus(itemsv1.ItemService_ServiceDesc.ServiceName, healthpb.HealthCheckResponse_SERVING)

	return app
}

// HTTP answers GET /health: 200 while the gRPC server serves, 503 once it is shutting down.
func (a *App) HTTP() http.Handler {
	mux := http.NewServeMux()

	mux.HandleFunc("GET /health", func(w http.ResponseWriter, r *http.Request) {
		res, err := a.Health.Check(r.Context(), &healthpb.HealthCheckRequest{})
		code, state := http.StatusOK, "ok"

		if err != nil || res.GetStatus() != healthpb.HealthCheckResponse_SERVING {
			code, state = http.StatusServiceUnavailable, "unavailable"
		}

		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(code)
		_ = json.NewEncoder(w).Encode(map[string]string{"status": state, "version": Version})
	})

	return mux
}

// Serve runs gRPC on grpcLn and HTTP on httpLn until ctx ends, then drains both.
func (a *App) Serve(ctx context.Context, grpcLn, httpLn net.Listener) error {
	httpSrv := &http.Server{Handler: a.HTTP(), ReadHeaderTimeout: 5 * time.Second}
	errs := make(chan error, 2)

	go func() { errs <- a.GRPC.Serve(grpcLn) }()
	go func() { errs <- httpSrv.Serve(httpLn) }()

	var err error

	select {
	case <-ctx.Done():
	case err = <-errs:
	}

	a.Health.Shutdown()

	shutdown, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	a.GRPC.GracefulStop()

	if herr := httpSrv.Shutdown(shutdown); herr != nil && err == nil {
		err = herr
	}

	if errors.Is(err, http.ErrServerClosed) || errors.Is(err, grpc.ErrServerStopped) {
		return nil
	}

	return err
}
