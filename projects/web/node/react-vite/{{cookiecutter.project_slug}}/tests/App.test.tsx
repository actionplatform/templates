import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { App, PROJECT } from "../src/App";

describe("App", () => {
  it("shows the project, the platform note and the docs link", () => {
    render(<App />);

    expect(
      screen.getByRole("heading", { name: PROJECT.name })
    ).toBeInTheDocument();
    expect(screen.getByText(PROJECT.description)).toBeInTheDocument();
    expect(screen.getByText(/Action Platform/)).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "Documentation" })
    ).toHaveAttribute("href", PROJECT.docsUrl);
  });
});
