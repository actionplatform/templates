//! {{ cookiecutter.description }}

/// Crate version, written from the release tag.
pub const VERSION: &str = "0.1.0";

/// Dummy public function. Replace with the real API.
pub fn hello(name: &str) -> String {
    let name = if name.is_empty() { "world" } else { name };
    format!("hello, {name}")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn defaults_to_world() {
        assert_eq!(hello(""), "hello, world");
    }

    #[test]
    fn greets_name() {
        assert_eq!(hello("ana"), "hello, ana");
    }

    #[test]
    fn version_is_set() {
        assert_eq!(VERSION, "0.1.0");
    }
}
