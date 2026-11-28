//! Router and shared state; every route is mounted here.

pub mod handlers;
pub mod models;
pub mod services;

use std::sync::Arc;

use axum::{routing::get, Router};

use crate::services::items::Items;

pub const VERSION: &str = env!("CARGO_PKG_VERSION");

pub fn app() -> Router {
    let items = Arc::new(Items::default());

    Router::new()
        .route("/health", get(handlers::health::health))
        .route(
            "/api/v1/items",
            get(handlers::items::list).post(handlers::items::create),
        )
        .route("/api/v1/items/{id}", get(handlers::items::get))
        .with_state(items)
}
