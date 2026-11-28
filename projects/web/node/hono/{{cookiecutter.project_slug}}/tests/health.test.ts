import { describe, expect, it } from "vitest";

import { createApp } from "../src/app.js";
import { VERSION } from "../src/version.js";

describe("GET /health", () => {
  it("reports the version", async () => {
    const response = await createApp().request("/health");

    expect(response.status).toBe(200);
    expect(await response.json()).toEqual({ status: "ok", version: VERSION });
  });

  it("answers an unknown route with the error shape", async () => {
    const response = await createApp().request("/nope");

    expect(response.status).toBe(404);
    expect(await response.json()).toEqual({ error: "not found" });
  });
});
