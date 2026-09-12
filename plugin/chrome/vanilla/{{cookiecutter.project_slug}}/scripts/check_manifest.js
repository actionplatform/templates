#!/usr/bin/env node
// Manifest is MV3, every referenced file exists, CSP is restrictive.
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const manifest = JSON.parse(
  fs.readFileSync(path.join(root, "manifest.json"), "utf8")
);
const errors = [];

if (manifest.manifest_version !== 3) errors.push("manifest_version must be 3");

const csp = manifest.content_security_policy?.extension_pages || "";
if (!csp.includes("script-src 'self'"))
  errors.push("CSP missing script-src 'self'");

const files = [
  manifest.background?.service_worker,
  manifest.action?.default_popup,
  ...(manifest.content_scripts || []).flatMap((cs) => cs.js || []),
].filter(Boolean);

for (const f of files) {
  if (!fs.existsSync(path.join(root, f))) errors.push(`missing file: ${f}`);
}

const pkg = JSON.parse(
  fs.readFileSync(path.join(root, "package.json"), "utf8")
);
if (pkg.version !== manifest.version)
  errors.push("package.json and manifest.json versions differ");

for (const e of errors) console.error(`error: ${e}`);
console.log(`checked manifest v${manifest.version}, ${files.length} files`);
process.exit(errors.length ? 1 : 0);
