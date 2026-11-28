import { Hono } from "hono";

import type { ItemsService } from "../../services/items.js";

export function itemsRoutes(items: ItemsService): Hono {
  const routes = new Hono();

  routes.get("/", (c) => c.json(items.list()));

  routes.post("/", async (c) => {
    const body: unknown = await c.req.json().catch(() => undefined);

    if (typeof body !== "object" || body === null || Array.isArray(body)) {
      return c.json({ error: "invalid json body" }, 400);
    }

    return c.json(items.create((body as { name?: unknown }).name), 201);
  });

  routes.get("/:id", (c) => {
    const id = Number(c.req.param("id"));

    if (!Number.isInteger(id)) {
      return c.json({ error: "item not found" }, 404);
    }

    return c.json(items.get(id));
  });

  return routes;
}
