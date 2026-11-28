// Package server is the gRPC layer: translate requests to the items rules and rules errors to status codes.
package server

import (
	"context"
	"errors"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	itemsv1 "{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/gen/items/v1"
	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/items"
)

type Items struct {
	itemsv1.UnimplementedItemServiceServer
	store *items.Store
}

func NewItems(store *items.Store) *Items {
	return &Items{store: store}
}

func (s *Items) ListItems(_ context.Context, _ *itemsv1.ListItemsRequest) (*itemsv1.ListItemsResponse, error) {
	rows := s.store.List()
	out := make([]*itemsv1.Item, 0, len(rows))

	for _, row := range rows {
		out = append(out, toProto(row))
	}

	return &itemsv1.ListItemsResponse{Items: out}, nil
}

func (s *Items) GetItem(_ context.Context, req *itemsv1.GetItemRequest) (*itemsv1.GetItemResponse, error) {
	row, err := s.store.Get(req.GetId())
	if err != nil {
		return nil, toStatus(err)
	}

	return &itemsv1.GetItemResponse{Item: toProto(row)}, nil
}

func (s *Items) CreateItem(_ context.Context, req *itemsv1.CreateItemRequest) (*itemsv1.CreateItemResponse, error) {
	row, err := s.store.Create(req.GetName())
	if err != nil {
		return nil, toStatus(err)
	}

	return &itemsv1.CreateItemResponse{Item: toProto(row)}, nil
}

func toProto(row items.Item) *itemsv1.Item {
	return &itemsv1.Item{Id: row.ID, Name: row.Name}
}

func toStatus(err error) error {
	switch {
	case errors.Is(err, items.ErrInvalid):
		return status.Error(codes.InvalidArgument, err.Error())
	case errors.Is(err, items.ErrNotFound):
		return status.Error(codes.NotFound, err.Error())
	default:
		return status.Error(codes.Internal, "internal error")
	}
}
