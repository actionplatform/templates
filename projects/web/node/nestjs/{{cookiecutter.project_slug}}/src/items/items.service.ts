import { Injectable, NotFoundException } from "@nestjs/common";

import type { Item } from "./item.js";

@Injectable()
export class ItemsService {
  private readonly rows = new Map<number, Item>();
  private lastId = 0;

  list(): Item[] {
    return [...this.rows.values()];
  }

  get(id: number): Item {
    const item = this.rows.get(id);

    if (!item) {
      throw new NotFoundException(`item ${id} not found`);
    }

    return item;
  }

  create(name: string): Item {
    this.lastId += 1;
    const item = { id: this.lastId, name };
    this.rows.set(item.id, item);

    return item;
  }
}
