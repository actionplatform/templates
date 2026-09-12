importScripts("shared/config.js", "shared/api.js");

const { CONFIG, KEYS, api } = self.{{ cookiecutter.package_name|upper }};

chrome.runtime.onInstalled.addListener(async () => {
  const stored = await chrome.storage.local.get(KEYS.SETTINGS);
  if (!stored[KEYS.SETTINGS]) {
    await chrome.storage.local.set({ [KEYS.SETTINGS]: { enabled: true } });
  }
});

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.type === "EVENT") {
    handleEvent(message.payload).then(sendResponse, (err) =>
      sendResponse({ error: String(err) })
    );
    return true;
  }
  return false;
});

async function handleEvent(payload) {
  const stored = await chrome.storage.local.get([KEYS.TOKEN, KEYS.SETTINGS]);
  if (!stored[KEYS.SETTINGS]?.enabled) return { skipped: true };
  return api.request("/events", {
    method: "POST",
    token: stored[KEYS.TOKEN],
    body: payload,
  });
}

self.{{ cookiecutter.package_name|upper }}.handleEvent = handleEvent;
self.{{ cookiecutter.package_name|upper }}.POLL_INTERVAL_MS = CONFIG.POLL_INTERVAL_MS;
