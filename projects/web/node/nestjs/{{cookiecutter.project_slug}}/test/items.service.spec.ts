import { NotFoundException } from "@nestjs/common";

import { ItemsService } from "../src/items/items.service.js";

describe("ItemsService", () => {
  let service: ItemsService;

  beforeEach(() => {
    service = new ItemsService();
  });

  it("assigns increasing ids", () => {
    expect(service.create("pen").id).toBe(1);
    expect(service.create("ink").id).toBe(2);
  });

  it("lists what was created", () => {
    service.create("pen");

    expect(service.list()).toEqual([{ id: 1, name: "pen" }]);
  });

  it("gets an item by id", () => {
    const created = service.create("pen");

    expect(service.get(created.id)).toEqual(created);
  });

  it("throws NotFoundException for an unknown id", () => {
    expect(() => service.get(42)).toThrow(NotFoundException);
  });
});
