(function () {
  const root = typeof self !== "undefined" ? self : globalThis;
  const { CONFIG } = root.{{ cookiecutter.package_name|upper }};

  async function request(path, { method = "GET", token, body } = {}) {
    const headers = { "Content-Type": "application/json" };
    if (token) headers.Authorization = `Bearer ${token}`;
    const res = await fetch(`${CONFIG.API_BASE}${path}`, {
      method,
      headers,
      body: body ? JSON.stringify(body) : undefined,
    });
    if (!res.ok) throw new Error(`[${res.status}] ${await res.text()}`);
    return res.status === 204 ? null : res.json();
  }

  root.{{ cookiecutter.package_name|upper }}.api = {
    request,
    ping: () => request("/ping"),
  };
})();
