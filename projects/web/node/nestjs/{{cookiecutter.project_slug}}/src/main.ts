import { NestFactory } from "@nestjs/core";
import type { NestExpressApplication } from "@nestjs/platform-express";

import { AppModule } from "./app.module.js";
import { configureApp } from "./configure.js";

const port = Number(process.env.PORT ?? 8000);
const host = process.env.HOST ?? "0.0.0.0";

const app = await NestFactory.create<NestExpressApplication>(AppModule);
configureApp(app);
app.enableShutdownHooks();
await app.listen(port, host);
