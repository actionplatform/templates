import type { INestApplication } from "@nestjs/common";
import { Test } from "@nestjs/testing";
import request from "supertest";

import { AppModule } from "../src/app.module.js";
import { configureApp } from "../src/configure.js";
import { VERSION } from "../src/version.js";

describe("GET /health", () => {
  let app: INestApplication;

  beforeAll(async () => {
    const module = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();
    app = module.createNestApplication();
    configureApp(app);
    await app.init();
  });

  afterAll(() => app.close());

  it("reports the version", async () => {
    const response = await request(app.getHttpServer()).get("/health");

    expect(response.status).toBe(200);
    expect(response.body).toEqual({ status: "ok", version: VERSION });
  });

  it("answers an unknown route with the error shape", async () => {
    const response = await request(app.getHttpServer()).get("/nope");

    expect(response.status).toBe(404);
    expect(response.body).toHaveProperty("error");
  });
});
