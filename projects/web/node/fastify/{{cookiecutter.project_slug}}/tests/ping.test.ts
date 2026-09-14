import { describe, expect, it } from "vitest";

import { createApp, VERSION } from "../src/app";

describe("GET /ping", () => {
  it("reports the version", async () => {
    const response = await createApp().inject({ method: "GET", url: "/ping" });

    expect(response.statusCode).toBe(200);
    expect(response.json()).toEqual({ status: "ok", version: VERSION });
  });
});
