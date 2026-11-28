use tokio::net::TcpListener;

#[tokio::main]
async fn main() {
    let port = std::env::var("PORT").unwrap_or_else(|_| "8000".to_string());
    let listener = TcpListener::bind(format!("0.0.0.0:{port}"))
        .await
        .expect("bind");

    println!("listening on {port}");

    axum::serve(listener, {{ cookiecutter.package_name }}::app())
        .with_graceful_shutdown(shutdown())
        .await
        .expect("serve");
}

async fn shutdown() {
    let _ = tokio::signal::ctrl_c().await;
}
