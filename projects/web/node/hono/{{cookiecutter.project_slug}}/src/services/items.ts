import { InvalidItemError, ItemNotFoundError } from "../errors.js";

export const MAX_NAME = 40;

export interface Item {
  id: number;
  name: string;
}

export class ItemsService {
  private readonly rows = new Map<number, Item>();
  private lastId = 0;

  list(): Item[] {
    return [...this.rows.values()];
  }

  get(id: number): Item {
    const item = this.rows.get(id);

    if (!item) {
      throw new ItemNotFoundError(`item ${id} not found`);
    }

    return item;
  }

  create(name: unknown): Item {
    if (typeof name !== "string" || name.trim() === "") {
      throw new InvalidItemError("name is required");
    }

    const trimmed = name.trim();

    if (trimmed.length > MAX_NAME) {
      throw new InvalidItemError(`name is longer than ${MAX_NAME} characters`);
    }

    this.lastId += 1;
    const item = { id: this.lastId, name: trimmed };
    this.rows.set(item.id, item);

    return item;
  }
}
