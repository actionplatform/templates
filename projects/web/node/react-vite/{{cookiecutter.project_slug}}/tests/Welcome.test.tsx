import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Welcome } from "../src/components/Welcome";

describe("Welcome", () => {
  it("renders what it is given", () => {
    render(
      <Welcome name="Acme" description="Widgets" docsUrl="https://example.test/docs" />
    );

    expect(screen.getByRole("heading", { name: "Acme" })).toBeInTheDocument();
    expect(screen.getByText("Widgets")).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Documentation" })).toHaveAttribute(
      "href",
      "https://example.test/docs"
    );
  });
});
