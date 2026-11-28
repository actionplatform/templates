import {
  Body,
  Controller,
  Get,
  NotFoundException,
  Param,
  ParseIntPipe,
  Post,
} from "@nestjs/common";

import { CreateItemDto } from "./dto/create-item.dto.js";
import type { Item } from "./item.js";
import { ItemsService } from "./items.service.js";

@Controller("api/v1/items")
export class ItemsController {
  constructor(private readonly items: ItemsService) {}

  @Get()
  list(): Item[] {
    return this.items.list();
  }

  @Post()
  create(@Body() body: CreateItemDto): Item {
    return this.items.create(body.name);
  }

  @Get(":id")
  get(
    @Param(
      "id",
      new ParseIntPipe({
        exceptionFactory: () => new NotFoundException("item not found"),
      })
    )
    id: number
  ): Item {
    return this.items.get(id);
  }
}
