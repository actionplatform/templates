# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}Desktop app: [Tauri 2](https://tauri.app) (Rust backend) with a React + TypeScript + Vite frontend.

## Install

Prerequisites: Node (`nvm use`), Rust (`rustup`, the version in `rust-toolchain.toml`) and the [Tauri system dependencies](https://tauri.app/start/prerequisites/) (WebView2 on Windows, Xcode tools on macOS, `libwebkit2gtk-4.1-dev` and friends on Linux).

```bash
nvm use
npm ci
```

## Run

```bash
npm run tauri dev      # the app window with hot reload
npm run dev            # the frontend alone in a browser, http://localhost:1420
npm run tauri build    # installers and bundles in src-tauri/target/release/bundle/
```

## Test / lint

```bash
npm test               # frontend, Vitest with @tauri-apps/api mocked
npm run lint           # ESLint + Prettier
npm run build          # type-check + dist/
npm run test:rust      # cargo test
npm run lint:rust      # cargo fmt --check + clippy -D warnings
```

`npm run lint` and `npm test` are what the platform's `check.sh` runs; the Rust checks run in `.github/workflows/rust.yml` because they need the Tauri system libraries.

## Release

Push a tag `v*` (the platform's `release` does) and `.github/workflows/release.yml` builds the bundles on macOS (arm64 and x64), Ubuntu and Windows with `tauri-apps/tauri-action` and attaches them to the GitHub release. The only secret it needs is the built-in `GITHUB_TOKEN`.

Builds are unsigned by default. To sign, add the repository secrets and the workflow passes them through:

| Secret | For |
|---|---|
| `APPLE_CERTIFICATE`, `APPLE_CERTIFICATE_PASSWORD`, `APPLE_SIGNING_IDENTITY` | macOS code signing |
| `APPLE_ID`, `APPLE_PASSWORD`, `APPLE_TEAM_ID` | macOS notarization |
| `TAURI_SIGNING_PRIVATE_KEY`, `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` | updater artifacts signature |

## Layout

```
index.html              Vite entry
src/
├── main.tsx            mounts <App />
├── App.tsx             the window: greeting form, app info
├── api.ts              typed wrappers over the Rust commands
└── styles.css
tests/                  Vitest + Testing Library, invoke mocked
src-tauri/
├── Cargo.toml          Cargo.lock is committed
├── tauri.conf.json     window, bundle, security policy
├── capabilities/       what the frontend may call
├── icons/              replace with `npm run tauri icon <png>`
└── src/
    ├── main.rs         entrypoint
    ├── lib.rs          builds the app, registers the commands
    └── commands.rs     greet, app_info, with their tests
```
