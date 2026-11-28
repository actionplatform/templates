import { beforeEach, describe, expect, it } from "vitest";

import { createApp } from "../src/app.js";

const post = (app: ReturnType<typeof createApp>, body: string) =>
  app.request("/api/v1/items", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body,
  });

describe("items", () => {
  let app: ReturnType<typeof createApp>;

  beforeEach(() => {
    app = createApp();
  });

  it("starts empty", async () => {
    const response = await app.request("/api/v1/items");

    expect(response.status).toBe(200);
    expect(await response.json()).toEqual([]);
  });

  it("creates, lists and gets an item", async () => {
    const created = await post(app, JSON.stringify({ name: "pen" }));

    expect(created.status).toBe(201);
    expect(await created.json()).toEqual({ id: 1, name: "pen" });

    const listed = await app.request("/api/v1/items");
    expect(await listed.json()).toEqual([{ id: 1, name: "pen" }]);

    const fetched = await app.request("/api/v1/items/1");
    expect(fetched.status).toBe(200);
    expect(await fetched.json()).toEqual({ id: 1, name: "pen" });
  });

  it("trims the name", async () => {
    const response = await post(app, JSON.stringify({ name: "  pen " }));

    expect(response.status).toBe(201);
    expect(await response.json()).toEqual({ id: 1, name: "pen" });
  });

  it.each([
    ["a blank name", { name: "   " }],
    ["a missing name", {}],
    ["a non-string name", { name: 7 }],
    ["a name over 40 characters", { name: "x".repeat(41) }],
  ])("rejects %s with 422", async (_label, body) => {
    const response = await post(app, JSON.stringify(body));

    expect(response.status).toBe(422);
    expect(await response.json()).toHaveProperty("error");
  });

  it.each([["{not json"], ["[]"], ["null"]])(
    "rejects the body %s with 400",
    async (body) => {
      const response = await post(app, body);

      expect(response.status).toBe(400);
      expect(await response.json()).toEqual({ error: "invalid json body" });
    }
  );

  it("answers an unknown id with 404", async () => {
    const response = await app.request("/api/v1/items/999");

    expect(response.status).toBe(404);
    expect(await response.json()).toEqual({ error: "item 999 not found" });
  });

  it("answers a non-numeric id with 404", async () => {
    const response = await app.request("/api/v1/items/abc");

    expect(response.status).toBe(404);
    expect(await response.json()).toEqual({ error: "item not found" });
  });
});
