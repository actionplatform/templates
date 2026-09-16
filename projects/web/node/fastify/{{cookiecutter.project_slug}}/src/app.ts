import Fastify, { FastifyInstance } from "fastify";

import { healthRoutes } from "./api/health";
import { v1Routes } from "./api/v1/router";

export const VERSION = "0.0.0";

export const API_V1_PREFIX = "/api/v1";

export function createApp(): FastifyInstance {
  const app = Fastify({ logger: false });

  app.register(healthRoutes);
  app.register(v1Routes, { prefix: API_V1_PREFIX });

  return app;
}
