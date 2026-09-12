import { describe, expect, it } from "vitest";

import { VERSION } from "../src";

describe("version", () => {
  it("is set", () => {
    expect(VERSION).toBe("0.1.0");
  });
});
