import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

import { VERSION } from "../src";

describe("version", () => {
  it("matches LAST_VERSION", () => {
    const expected = readFileSync(join(__dirname, "..", "LAST_VERSION"), "utf8").trim();
    expect(VERSION).toBe(expected);
  });
});
