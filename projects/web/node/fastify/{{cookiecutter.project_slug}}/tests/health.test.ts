import { describe, expect, it } from "vitest";

import { createApp, VERSION } from "../src/app";

describe("GET /health", () => {
  it("reports the version", async () => {
    const response = await createApp().inject({ method: "GET", url: "/health" });

    expect(response.statusCode).toBe(200);
    expect(response.json()).toEqual({ status: "ok", version: VERSION });
  });
});
