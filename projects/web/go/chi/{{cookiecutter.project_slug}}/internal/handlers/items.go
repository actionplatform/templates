package handlers

import (
	"encoding/json"
	"errors"
	"net/http"
	"strconv"

	"github.com/go-chi/chi/v5"

	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/models"
	"{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}/internal/services"
)

// Items is the example resource: handler → service → response.
type Items struct {
	svc *services.Items
}

func NewItems(svc *services.Items) *Items {
	return &Items{svc: svc}
}

func (h *Items) List(w http.ResponseWriter, _ *http.Request) {
	writeJSON(w, http.StatusOK, h.svc.List())
}

func (h *Items) Create(w http.ResponseWriter, r *http.Request) {
	var body models.ItemCreate

	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		writeError(w, http.StatusBadRequest, "invalid json body")

		return
	}

	item, err := h.svc.Create(body.Name)
	if err != nil {
		fail(w, err)

		return
	}

	writeJSON(w, http.StatusCreated, item)
}

func (h *Items) Get(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(chi.URLParam(r, "id"))
	if err != nil {
		writeError(w, http.StatusNotFound, "item not found")

		return
	}

	item, err := h.svc.Get(id)
	if err != nil {
		fail(w, err)

		return
	}

	writeJSON(w, http.StatusOK, item)
}

func fail(w http.ResponseWriter, err error) {
	switch {
	case errors.Is(err, services.ErrInvalid):
		writeError(w, http.StatusUnprocessableEntity, err.Error())
	case errors.Is(err, services.ErrNotFound):
		writeError(w, http.StatusNotFound, err.Error())
	default:
		writeError(w, http.StatusInternalServerError, "internal error")
	}
}
