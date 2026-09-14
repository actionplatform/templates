import { createApp } from "./app";

const port = Number(process.env.PORT ?? 8000);
const host = process.env.HOST ?? "0.0.0.0";

createApp()
  .listen({ port, host })
  .then((address) => console.log(`listening on ${address}`))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
