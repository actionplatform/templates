use axum::Json;

use crate::models::Health;
use crate::VERSION;

/// Every API exposes the version at `/health`.
pub async fn health() -> Json<Health> {
    Json(Health {
        status: "ok",
        version: VERSION,
    })
}
