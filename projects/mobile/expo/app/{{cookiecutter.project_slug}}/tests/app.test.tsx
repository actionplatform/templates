import { fireEvent, renderRouter, screen } from "expo-router/testing-library";

import About from "../src/app/about";
import Home from "../src/app/index";

const routes = { index: Home, about: About };

describe("app", () => {
  it("renders the home screen", async () => {
    await renderRouter(routes, { initialUrl: "/" });

    expect(screen.getByRole("header")).toBeTruthy();
    expect(screen.getByText("About")).toBeTruthy();
  });

  it("navigates to the about screen and back", async () => {
    await renderRouter(routes, { initialUrl: "/" });

    await fireEvent.press(screen.getByText("About"));
    expect(screen).toHavePathname("/about");
    expect(screen.getByText(/Version/)).toBeTruthy();

    await fireEvent.press(screen.getByText("Back"));
    expect(screen).toHavePathname("/");
  });
});
