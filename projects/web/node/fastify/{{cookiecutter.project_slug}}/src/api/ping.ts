import { FastifyInstance } from "fastify";

import { VERSION } from "../app";

export async function pingRoutes(app: FastifyInstance): Promise<void> {
  app.get("/ping", async () => ({ status: "ok", version: VERSION }));
}
