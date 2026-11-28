import { Hono } from "hono";

import { VERSION } from "../version.js";

export const healthRoutes = new Hono().get("/health", (c) =>
  c.json({ status: "ok", version: VERSION })
);
