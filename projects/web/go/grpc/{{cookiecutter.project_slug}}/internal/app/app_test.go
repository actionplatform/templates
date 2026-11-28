package app

import (
	"context"
	"net"
	"net/http"
	"net/http/httptest"
	"testing"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials/insecure"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/test/bufconn"

	itemsv1 "{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/gen/items/v1"
)

func start(t *testing.T) (*App, *grpc.ClientConn) {
	t.Helper()

	lis := bufconn.Listen(1 << 20)
	a := New()

	go func() { _ = a.GRPC.Serve(lis) }()
	t.Cleanup(a.GRPC.Stop)

	conn, err := grpc.NewClient(
		"passthrough:///bufnet",
		grpc.WithContextDialer(func(context.Context, string) (net.Conn, error) { return lis.Dial() }),
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)
	if err != nil {
		t.Fatal(err)
	}

	t.Cleanup(func() { _ = conn.Close() })

	return a, conn
}

func TestCreateAndGetItem(t *testing.T) {
	_, conn := start(t)
	client := itemsv1.NewItemServiceClient(conn)
	ctx := context.Background()

	created, err := client.CreateItem(ctx, &itemsv1.CreateItemRequest{Name: "pen"})
	if err != nil || created.GetItem().GetName() != "pen" || created.GetItem().GetId() != 1 {
		t.Fatalf("got %v %v", created, err)
	}

	got, err := client.GetItem(ctx, &itemsv1.GetItemRequest{Id: 1})
	if err != nil || got.GetItem().GetName() != "pen" {
		t.Fatalf("got %v %v", got, err)
	}
}

func TestListItems(t *testing.T) {
	_, conn := start(t)
	client := itemsv1.NewItemServiceClient(conn)
	ctx := context.Background()

	empty, err := client.ListItems(ctx, &itemsv1.ListItemsRequest{})
	if err != nil || len(empty.GetItems()) != 0 {
		t.Fatalf("got %v %v", empty, err)
	}

	for _, name := range []string{"a", "b"} {
		if _, err := client.CreateItem(ctx, &itemsv1.CreateItemRequest{Name: name}); err != nil {
			t.Fatal(err)
		}
	}

	list, err := client.ListItems(ctx, &itemsv1.ListItemsRequest{})
	if err != nil || len(list.GetItems()) != 2 {
		t.Fatalf("got %v %v", list, err)
	}
}

func TestCreateRejectsEmptyName(t *testing.T) {
	_, conn := start(t)

	_, err := itemsv1.NewItemServiceClient(conn).CreateItem(context.Background(), &itemsv1.CreateItemRequest{Name: " "})
	if status.Code(err) != codes.InvalidArgument {
		t.Fatalf("got %v", err)
	}
}

func TestGetUnknownItem(t *testing.T) {
	_, conn := start(t)

	_, err := itemsv1.NewItemServiceClient(conn).GetItem(context.Background(), &itemsv1.GetItemRequest{Id: 99})
	if status.Code(err) != codes.NotFound {
		t.Fatalf("got %v", err)
	}
}

func TestGRPCHealth(t *testing.T) {
	_, conn := start(t)
	client := healthpb.NewHealthClient(conn)

	for _, service := range []string{"", itemsv1.ItemService_ServiceDesc.ServiceName} {
		res, err := client.Check(context.Background(), &healthpb.HealthCheckRequest{Service: service})
		if err != nil || res.GetStatus() != healthpb.HealthCheckResponse_SERVING {
			t.Fatalf("%q: got %v %v", service, res, err)
		}
	}
}

func TestHTTPHealth(t *testing.T) {
	w := httptest.NewRecorder()

	New().HTTP().ServeHTTP(w, httptest.NewRequest(http.MethodGet, "/health", nil))

	if w.Code != http.StatusOK || w.Body.String() != "{\"status\":\"ok\",\"version\":\""+Version+"\"}\n" {
		t.Fatalf("got %d %s", w.Code, w.Body.String())
	}
}

func TestHTTPHealthAfterShutdown(t *testing.T) {
	a := New()
	a.Health.Shutdown()
	w := httptest.NewRecorder()

	a.HTTP().ServeHTTP(w, httptest.NewRequest(http.MethodGet, "/health", nil))

	if w.Code != http.StatusServiceUnavailable {
		t.Fatalf("got %d", w.Code)
	}
}

func TestHTTPHealthRejectsPost(t *testing.T) {
	w := httptest.NewRecorder()

	New().HTTP().ServeHTTP(w, httptest.NewRequest(http.MethodPost, "/health", nil))

	if w.Code != http.StatusMethodNotAllowed {
		t.Fatalf("got %d", w.Code)
	}
}

func TestServeStopsOnContext(t *testing.T) {
	grpcLn, _ := net.Listen("tcp", "127.0.0.1:0")
	httpLn, _ := net.Listen("tcp", "127.0.0.1:0")
	ctx, cancel := context.WithCancel(context.Background())
	done := make(chan error, 1)

	go func() { done <- New().Serve(ctx, grpcLn, httpLn) }()

	res, err := http.Get("http://" + httpLn.Addr().String() + "/health")
	if err != nil || res.StatusCode != http.StatusOK {
		t.Fatalf("got %v %v", res, err)
	}

	_ = res.Body.Close()
	cancel()

	if err := <-done; err != nil {
		t.Fatal(err)
	}
}
