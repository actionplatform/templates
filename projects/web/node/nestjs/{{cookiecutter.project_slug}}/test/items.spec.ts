import type { INestApplication } from "@nestjs/common";
import { Test } from "@nestjs/testing";
import request from "supertest";

import { AppModule } from "../src/app.module.js";
import { configureApp } from "../src/configure.js";

describe("items", () => {
  let app: INestApplication;

  beforeEach(async () => {
    const module = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = module.createNestApplication();
    configureApp(app);
    await app.init();
  });

  afterEach(() => app.close());

  const http = () => request(app.getHttpServer());

  it("starts empty", async () => {
    const response = await http().get("/api/v1/items");

    expect(response.status).toBe(200);
    expect(response.body).toEqual([]);
  });

  it("creates, lists and gets an item", async () => {
    const created = await http().post("/api/v1/items").send({ name: "pen" });

    expect(created.status).toBe(201);
    expect(created.body).toEqual({ id: 1, name: "pen" });

    const listed = await http().get("/api/v1/items");
    expect(listed.body).toEqual([{ id: 1, name: "pen" }]);

    const fetched = await http().get("/api/v1/items/1");
    expect(fetched.status).toBe(200);
    expect(fetched.body).toEqual({ id: 1, name: "pen" });
  });

  it("trims the name", async () => {
    const response = await http()
      .post("/api/v1/items")
      .send({ name: "  pen " });

    expect(response.status).toBe(201);
    expect(response.body.name).toBe("pen");
  });

  it.each([
    ["a blank name", { name: "   " }],
    ["a missing name", {}],
    ["a non-string name", { name: 7 }],
    ["a name over 40 characters", { name: "x".repeat(41) }],
  ])("rejects %s with 422", async (_label, body) => {
    const response = await http().post("/api/v1/items").send(body);

    expect(response.status).toBe(422);
    expect(typeof response.body.error).toBe("string");
  });

  it("rejects an invalid json body with 400", async () => {
    const response = await http()
      .post("/api/v1/items")
      .set("Content-Type", "application/json")
      .send("{not json");

    expect(response.status).toBe(400);
    expect(typeof response.body.error).toBe("string");
  });

  it("answers an unknown id with 404", async () => {
    const response = await http().get("/api/v1/items/999");

    expect(response.status).toBe(404);
    expect(response.body).toEqual({ error: "item 999 not found" });
  });

  it("answers a non-numeric id with 404", async () => {
    const response = await http().get("/api/v1/items/abc");

    expect(response.status).toBe(404);
    expect(response.body).toEqual({ error: "item not found" });
  });
});
