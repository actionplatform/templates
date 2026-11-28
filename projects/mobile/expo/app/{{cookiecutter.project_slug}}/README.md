# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}Expo SDK 58, React Native and TypeScript with expo-router. Bundle id `{{ cookiecutter.__bundle_id }}`.

## Install

```bash
nvm use
npm ci
```

## Run

```bash
npm start              # Expo dev server, scan the QR code with Expo Go
npm run ios            # iOS simulator
npm run android        # Android emulator
npm run web            # browser
npm run export:web     # static web build into dist/
```

## Build

[EAS Build](https://docs.expo.dev/build/introduction/) profiles live in `eas.json`:

```bash
npx eas-cli build --profile development   # development client, internal
npx eas-cli build --profile preview       # internal distribution
npx eas-cli build --profile production    # store build
```

## Test / lint

```bash
npm test
npm run lint           # eslint, prettier check and tsc --noEmit
npx expo-doctor
```

## Layout

```
app.json                Expo config
eas.json                EAS Build profiles
src/app/
├── _layout.tsx         stack navigator
├── index.tsx           home screen
└── about.tsx           about screen
tests/
└── app.test.tsx        both screens and the navigation between them
```

No state library, no UI kit — add them when the app needs them.
