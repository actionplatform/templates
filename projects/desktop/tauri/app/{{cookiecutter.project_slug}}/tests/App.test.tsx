import { invoke } from "@tauri-apps/api/core";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { App, PROJECT } from "../src/App";

vi.mock("@tauri-apps/api/core", () => ({ invoke: vi.fn() }));

const info = { name: "app", version: "1.2.3", os: "macos" };

describe("App", () => {
  beforeEach(() => {
    vi.mocked(invoke).mockReset();
  });

  it("shows the project, the app info and the docs link", async () => {
    vi.mocked(invoke).mockResolvedValue(info);
    render(<App />);

    expect(
      screen.getByRole("heading", { name: PROJECT.name })
    ).toBeInTheDocument();
    expect(
      await screen.findByText(/app 1\.2\.3 on macos/)
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "Documentation" })
    ).toHaveAttribute("href", PROJECT.docsUrl);
  });

  it("greets through the backend command", async () => {
    vi.mocked(invoke).mockImplementation(async (command) =>
      command === "greet" ? "Hello, Ada!" : info
    );
    render(<App />);

    await userEvent.type(screen.getByLabelText("Name"), "Ada");
    await userEvent.click(screen.getByRole("button", { name: "Greet" }));

    expect(await screen.findByRole("status")).toHaveTextContent("Hello, Ada!");
    expect(invoke).toHaveBeenCalledWith("greet", { name: "Ada" });
  });

  it("shows the error when the backend fails", async () => {
    vi.mocked(invoke).mockRejectedValue("backend down");
    render(<App />);

    expect(await screen.findByRole("alert")).toHaveTextContent("backend down");
  });
});
