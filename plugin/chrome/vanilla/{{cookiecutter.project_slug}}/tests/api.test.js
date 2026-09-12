const { test } = require("node:test");
const assert = require("node:assert/strict");
const { loadScripts } = require("./helpers/load");

function setup(fetchImpl) {
  const ctx = loadScripts(["shared/config.js", "shared/api.js"], {
    fetch: fetchImpl,
  });
  return Object.values(ctx.self)[0];
}

test("request sends bearer token and parses json", async () => {
  let seen;
  const ns = setup(async (url, init) => {
    seen = { url, init };
    return { ok: true, status: 200, json: async () => ({ ok: 1 }) };
  });
  const out = await ns.api.request("/things", { token: "t" });
  assert.deepEqual(out, { ok: 1 });
  assert.equal(seen.init.headers.Authorization, "Bearer t");
  assert.ok(seen.url.endsWith("/things"));
});

test("request throws on non-2xx", async () => {
  const ns = setup(async () => ({
    ok: false,
    status: 500,
    text: async () => "boom",
  }));
  await assert.rejects(ns.api.request("/x"), /\[500\] boom/);
});
