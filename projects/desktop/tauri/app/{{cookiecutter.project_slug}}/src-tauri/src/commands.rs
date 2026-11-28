use serde::Serialize;

#[derive(Debug, PartialEq, Serialize)]
pub struct AppInfo {
    pub name: String,
    pub version: String,
    pub os: String,
}

pub fn greeting(name: &str) -> String {
    match name.trim() {
        "" => "Hello, stranger!".to_string(),
        name => format!("Hello, {name}!"),
    }
}

#[tauri::command]
pub fn greet(name: &str) -> String {
    greeting(name)
}

#[tauri::command]
pub fn app_info() -> AppInfo {
    AppInfo {
        name: env!("CARGO_PKG_NAME").to_string(),
        version: env!("CARGO_PKG_VERSION").to_string(),
        os: std::env::consts::OS.to_string(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greets_by_name() {
        assert_eq!(greet("Ada"), "Hello, Ada!");
    }

    #[test]
    fn trims_the_name() {
        assert_eq!(greeting("  Ada  "), "Hello, Ada!");
    }

    #[test]
    fn greets_a_stranger_without_a_name() {
        assert_eq!(greeting(""), "Hello, stranger!");
        assert_eq!(greeting("   "), "Hello, stranger!");
    }

    #[test]
    fn reports_the_package_and_platform() {
        let info = app_info();

        assert_eq!(info.name, "{{ cookiecutter.package_name }}");
        assert_eq!(info.version, env!("CARGO_PKG_VERSION"));
        assert_eq!(info.os, std::env::consts::OS);
    }

    #[test]
    fn serializes_for_the_frontend() {
        let json = serde_json::to_value(app_info()).unwrap();

        assert!(json.get("name").is_some());
        assert!(json.get("version").is_some());
        assert!(json.get("os").is_some());
    }
}
