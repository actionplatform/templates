// Run a browser-global script inside a vm context and return that context.
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

function loadScripts(files, ctx = {}) {
  ctx.self = ctx.self || {};
  ctx.globalThis = ctx.self;
  vm.createContext(ctx);
  for (const f of files) {
    vm.runInContext(
      fs.readFileSync(path.join(__dirname, "..", "..", f), "utf8"),
      ctx,
      { filename: f }
    );
  }
  return ctx;
}

module.exports = { loadScripts };
