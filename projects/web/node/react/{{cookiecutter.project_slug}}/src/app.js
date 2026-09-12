import React, { lazy, Suspense } from "react";
import { Route, Routes } from "react-router-dom";
import { ErrorBoundary } from "components/atoms";
import { ROUTES } from "constants/routes";

const HomeView = lazy(() => import("./views/HomeView"));
const NotFoundView = lazy(() => import("./views/NotFoundView"));

const fallbackStyle = { padding: "2rem" };
const RouteFallback = () => <div style={fallbackStyle}>Loading…</div>;

const wrap = (Component) => (
  <ErrorBoundary>
    <Suspense fallback={<RouteFallback />}>
      <Component />
    </Suspense>
  </ErrorBoundary>
);

const App = () => (
  <Routes>
    <Route path={ROUTES.HOME} element={wrap(HomeView)} />
    <Route path="*" element={wrap(NotFoundView)} />
  </Routes>
);

export default App;
