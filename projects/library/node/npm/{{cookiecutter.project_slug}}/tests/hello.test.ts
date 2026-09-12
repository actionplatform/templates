import { describe, expect, it } from "vitest";

import { hello } from "../src";

describe("hello", () => {
  it("defaults to world", () => {
    expect(hello()).toBe("hello, world");
  });

  it("greets a name", () => {
    expect(hello("ana")).toBe("hello, ana");
  });
});
