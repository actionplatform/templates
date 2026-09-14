import { describe, expect, it } from "vitest";

import { createApp } from "../src/app";

describe("GET /api/v1/hello", () => {
  it("greets the name", async () => {
    const response = await createApp().inject({
      method: "GET",
      url: "/api/v1/hello?name=Fernando",
    });

    expect(response.statusCode).toBe(200);
    expect(response.json()).toEqual({ message: "hello, Fernando" });
  });

  it("defaults to world", async () => {
    const response = await createApp().inject({
      method: "GET",
      url: "/api/v1/hello",
    });

    expect(response.json()).toEqual({ message: "hello, world" });
  });
});
