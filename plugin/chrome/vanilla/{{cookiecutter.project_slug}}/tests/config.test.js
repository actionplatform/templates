const { test } = require("node:test");
const assert = require("node:assert/strict");
const { loadScripts } = require("./helpers/load");

const ns = Object.values(loadScripts(["shared/config.js"]).self)[0];

test("config exposes an API base", () => {
  assert.match(ns.CONFIG.API_BASE, /^https?:\/\//);
});

test("storage keys are distinct", () => {
  const values = Object.values(ns.KEYS);
  assert.equal(new Set(values).size, values.length);
});
