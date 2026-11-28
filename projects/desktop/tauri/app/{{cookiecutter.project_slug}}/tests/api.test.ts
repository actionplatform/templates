import { invoke } from "@tauri-apps/api/core";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { appInfo, greet } from "../src/api";

vi.mock("@tauri-apps/api/core", () => ({ invoke: vi.fn() }));

describe("api", () => {
  beforeEach(() => {
    vi.mocked(invoke).mockReset();
  });

  it("greet calls the greet command with the name", async () => {
    vi.mocked(invoke).mockResolvedValue("Hello, Ada!");

    await expect(greet("Ada")).resolves.toBe("Hello, Ada!");
    expect(invoke).toHaveBeenCalledWith("greet", { name: "Ada" });
  });

  it("appInfo calls the app_info command", async () => {
    const info = { name: "app", version: "0.0.0", os: "linux" };
    vi.mocked(invoke).mockResolvedValue(info);

    await expect(appInfo()).resolves.toEqual(info);
    expect(invoke).toHaveBeenCalledWith("app_info");
  });
});
