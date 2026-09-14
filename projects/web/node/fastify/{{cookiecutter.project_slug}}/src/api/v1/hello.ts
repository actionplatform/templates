import { FastifyInstance } from "fastify";

type HelloQuery = { name?: string };

export async function helloRoutes(app: FastifyInstance): Promise<void> {
  app.get<{ Querystring: HelloQuery }>("/hello", async (request) => ({
    message: `hello, ${request.query.name ?? "world"}`,
  }));
}
