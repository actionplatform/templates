import { Module } from "@nestjs/common";

import { HealthController } from "./health/health.controller.js";
import { ItemsModule } from "./items/items.module.js";

@Module({
  imports: [ItemsModule],
  controllers: [HealthController],
})
export class AppModule {}
