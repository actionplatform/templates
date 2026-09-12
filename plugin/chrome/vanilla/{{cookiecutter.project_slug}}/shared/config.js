(function () {
  const root = typeof self !== "undefined" ? self : globalThis;
  root.{{ cookiecutter.package_name|upper }} = root.{{ cookiecutter.package_name|upper }} || {};

  root.{{ cookiecutter.package_name|upper }}.CONFIG = {
    API_BASE: "{{ cookiecutter.api_base }}",
    POLL_INTERVAL_MS: 3000,
  };

  root.{{ cookiecutter.package_name|upper }}.KEYS = {
    TOKEN: "token",
    SETTINGS: "settings",
  };
})();
