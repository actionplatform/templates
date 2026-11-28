import { beforeEach, describe, expect, it } from "vitest";

import { InvalidItemError, ItemNotFoundError } from "../src/errors.js";
import { ItemsService } from "../src/services/items.js";

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

  it("rejects an invalid name", () => {
    expect(() => service.create("  ")).toThrow(InvalidItemError);
    expect(() => service.create("x".repeat(41))).toThrow(InvalidItemError);
  });

  it("throws for an unknown id", () => {
    expect(() => service.get(42)).toThrow(ItemNotFoundError);
  });
});
