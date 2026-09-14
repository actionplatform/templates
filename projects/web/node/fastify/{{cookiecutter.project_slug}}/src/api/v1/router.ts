import { FastifyInstance } from "fastify";

import { helloRoutes } from "./hello";

export async function v1Routes(app: FastifyInstance): Promise<void> {
  app.register(helloRoutes);
}
