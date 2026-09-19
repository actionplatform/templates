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

## Layout

```
src/
└── lib.rs            the public API (`hello`) and `VERSION`; unit tests next to the code
tests/
└── hello.rs          integration tests — the crate as a user sees it
Cargo.toml            name, version (written from the release tag), edition
rust-toolchain.toml   the toolchain every checkout and CI uses
rustfmt.toml, clippy.toml   at the root, where cargo reads them
```

Public items go in `src/lib.rs` (or modules it re-exports); every public function has a unit test beside it and, when it is part of the API, an integration test in `tests/`.
