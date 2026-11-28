import { Controller, Get } from "@nestjs/common";

import { VERSION } from "../version.js";

@Controller("health")
export class HealthController {
  @Get()
  check(): { status: string; version: string } {
    return { status: "ok", version: VERSION };
  }
}
