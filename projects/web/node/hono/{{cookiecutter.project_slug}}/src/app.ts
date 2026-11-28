import { Hono } from "hono";

import { healthRoutes } from "./api/health.js";
import { itemsRoutes } from "./api/v1/items.js";
import { InvalidItemError, ItemNotFoundError } from "./errors.js";
import { ItemsService } from "./services/items.js";

export const API_V1_PREFIX = "/api/v1";

export function createApp(items = new ItemsService()): Hono {
  const app = new Hono();

  app.route("/", healthRoutes);
  app.route(`${API_V1_PREFIX}/items`, itemsRoutes(items));

  app.notFound((c) => c.json({ error: "not found" }, 404));

  app.onError((error, c) => {
    if (error instanceof InvalidItemError) {
      return c.json({ error: error.message }, 422);
    }

    if (error instanceof ItemNotFoundError) {
      return c.json({ error: error.message }, 404);
    }

    return c.json({ error: "internal error" }, 500);
  });

  return app;
}
