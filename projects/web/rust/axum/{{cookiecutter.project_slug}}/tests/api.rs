use axum::{
    body::Body,
    http::{header, Method, Request, StatusCode},
    Router,
};
use http_body_util::BodyExt;
use serde_json::{json, Value};
use tower::ServiceExt;

async fn call(app: &Router, method: Method, uri: &str, body: Option<&str>) -> (StatusCode, Value) {
    let request = Request::builder()
        .method(method)
        .uri(uri)
        .header(header::CONTENT_TYPE, "application/json")
        .body(Body::from(body.unwrap_or("").to_string()))
        .unwrap();
    let response = app.clone().oneshot(request).await.unwrap();
    let status = response.status();
    let bytes = response.into_body().collect().await.unwrap().to_bytes();

    (
        status,
        serde_json::from_slice(&bytes).unwrap_or(Value::Null),
    )
}

fn app() -> Router {
    {{ cookiecutter.package_name }}::app()
}

#[tokio::test]
async fn health_reports_ok_and_version() {
    let (status, body) = call(&app(), Method::GET, "/health", None).await;

    assert_eq!(status, StatusCode::OK);
    assert_eq!(body["status"], "ok");
    assert_eq!(body["version"], {{ cookiecutter.package_name }}::VERSION);
}

#[tokio::test]
async fn items_start_empty() {
    let (status, body) = call(&app(), Method::GET, "/api/v1/items", None).await;

    assert_eq!(status, StatusCode::OK);
    assert_eq!(body, json!([]));
}

#[tokio::test]
async fn create_then_get_and_list() {
    let app = app();

    let (status, created) = call(
        &app,
        Method::POST,
        "/api/v1/items",
        Some(r#"{"name":"first"}"#),
    )
    .await;
    assert_eq!(status, StatusCode::CREATED);
    assert_eq!(created, json!({"id": 1, "name": "first"}));

    let (status, fetched) = call(&app, Method::GET, "/api/v1/items/1", None).await;
    assert_eq!(status, StatusCode::OK);
    assert_eq!(fetched, created);

    let (_, listed) = call(&app, Method::GET, "/api/v1/items", None).await;
    assert_eq!(listed, json!([created]));
}

#[tokio::test]
async fn create_rejects_blank_name() {
    let (status, body) = call(
        &app(),
        Method::POST,
        "/api/v1/items",
        Some(r#"{"name":" "}"#),
    )
    .await;

    assert_eq!(status, StatusCode::UNPROCESSABLE_ENTITY);
    assert!(body["error"].as_str().unwrap().contains("name is required"));
}

#[tokio::test]
async fn create_rejects_bad_json() {
    let (status, _) = call(&app(), Method::POST, "/api/v1/items", Some("nope")).await;

    assert_eq!(status, StatusCode::BAD_REQUEST);
}

#[tokio::test]
async fn unknown_item_is_404() {
    let app = app();

    let (status, _) = call(&app, Method::GET, "/api/v1/items/42", None).await;
    assert_eq!(status, StatusCode::NOT_FOUND);

    let (status, _) = call(&app, Method::GET, "/api/v1/items/abc", None).await;
    assert_eq!(status, StatusCode::NOT_FOUND);
}
