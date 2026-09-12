// Shared helpers for every content script. Loaded before the page-specific one.
(function () {
  const root = typeof self !== "undefined" ? self : globalThis;
  const { CONFIG } = root.{{ cookiecutter.package_name|upper }};

  function send(payload) {
    return chrome.runtime.sendMessage({ type: "EVENT", payload });
  }

  function watch(read, onChange) {
    let last = null;
    setInterval(() => {
      const next = read();
      const key = next ? JSON.stringify(next) : null;
      if (key !== last) {
        last = key;
        if (next) onChange(next);
      }
    }, CONFIG.POLL_INTERVAL_MS);
  }

  root.{{ cookiecutter.package_name|upper }}.content = { send, watch };
})();
