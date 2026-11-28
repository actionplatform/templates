mod commands;

pub use commands::{app_info, greeting, AppInfo};

pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![
            commands::greet,
            commands::app_info
        ])
        .run(tauri::generate_context!())
        .expect("error while running the application");
}
