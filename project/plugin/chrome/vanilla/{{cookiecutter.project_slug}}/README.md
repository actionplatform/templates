# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

Chrome extension, Manifest V3. No bundler: plain scripts loaded in order by `manifest.json`.

## Develop

```bash
nvm use
npm ci
npm test
npm run lint
npm run format
```

Load unpacked: `chrome://extensions` → Developer mode → Load unpacked → this folder.

## Layout

```
manifest.json          # MV3; every script it references must exist
background.js          # service worker: receives EVENT messages, calls the API
content/base.js        # helpers shared by every content script (send, watch)
content/example.js     # one file per site
popup/                 # action popup (html/css/js)
shared/config.js       # API base + storage keys, exposed on self.{{ cookiecutter.package_name|upper }}
shared/api.js          # fetch wrapper
scripts/bump.js        # keeps package.json, manifest.json and LAST_VERSION in sync
scripts/check_manifest.js
tests/                 # node --test, scripts loaded through vm
```

## Release

```bash
npm run bump patch     # or minor / major / x.y.z
npm run build          # build/extension.zip for the Web Store
```
