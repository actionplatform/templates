import { serve } from "@hono/node-server";

import { createApp } from "./app.js";

const port = Number(process.env.PORT ?? 8000);
const hostname = process.env.HOST ?? "0.0.0.0";

const server = serve({ fetch: createApp().fetch, port, hostname }, (info) => {
  console.log(`listening on http://${info.address}:${info.port}`);
});

process.on("SIGTERM", () => server.close(() => process.exit(0)));
process.on("SIGINT", () => server.close(() => process.exit(0)));
