const { KEYS, api } = window.{{ cookiecutter.package_name|upper }};
const $ = (sel) => document.querySelector(sel);

async function init() {
  const stored = await chrome.storage.local.get(KEYS.SETTINGS);
  const settings = stored[KEYS.SETTINGS] || { enabled: true };
  $("#enabled").checked = settings.enabled;

  $("#enabled").addEventListener("change", async (e) => {
    await chrome.storage.local.set({
      [KEYS.SETTINGS]: { ...settings, enabled: e.target.checked },
    });
  });

  try {
    await api.health();
    $("#status-dot").classList.add("ok");
    $("#api-status").textContent = "reachable";
  } catch (err) {
    $("#status-dot").classList.add("error");
    $("#api-status").textContent = String(err.message || err);
  }
}

init();
