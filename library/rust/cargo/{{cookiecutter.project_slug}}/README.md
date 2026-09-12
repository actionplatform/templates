# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
cargo add {{ cookiecutter.package_name }}
```

## Develop

```bash
cargo test
cargo fmt --check
cargo clippy -- -D warnings
```

`rustfmt.toml` and `clippy.toml` at the root mirror `.code_quality/` — cargo only reads them there.
