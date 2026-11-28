use std::sync::Arc;

use axum::{
    extract::{rejection::JsonRejection, Path, State},
    http::StatusCode,
    response::{IntoResponse, Response},
    Json,
};
use serde_json::json;

use crate::models::{Item, ItemCreate};
use crate::services::items::{Error, Items};

type Shared = State<Arc<Items>>;

impl IntoResponse for Error {
    fn into_response(self) -> Response {
        let status = match self {
            Error::Invalid(_) => StatusCode::UNPROCESSABLE_ENTITY,
            Error::NotFound(_) => StatusCode::NOT_FOUND,
        };

        (status, Json(json!({ "error": self.to_string() }))).into_response()
    }
}

pub async fn list(State(items): Shared) -> Json<Vec<Item>> {
    Json(items.list())
}

pub async fn create(
    State(items): Shared,
    body: Result<Json<ItemCreate>, JsonRejection>,
) -> Result<(StatusCode, Json<Item>), Response> {
    let Json(body) = body.map_err(|_| {
        (
            StatusCode::BAD_REQUEST,
            Json(json!({ "error": "invalid json body" })),
        )
            .into_response()
    })?;

    let item = items
        .create(&body.name)
        .map_err(IntoResponse::into_response)?;

    Ok((StatusCode::CREATED, Json(item)))
}

pub async fn get(State(items): Shared, Path(id): Path<String>) -> Result<Json<Item>, Error> {
    let id = id.parse().map_err(|_| Error::NotFound(id))?;

    items.get(id).map(Json)
}
