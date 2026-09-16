import { FastifyInstance } from "fastify";

import { VERSION } from "../app";

export async function healthRoutes(app: FastifyInstance): Promise<void> {
  app.get("/health", async () => ({ status: "ok", version: VERSION }));
}
