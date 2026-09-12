import React from "react";
import { Link } from "react-router-dom";
import { PageLayout } from "components/templates";
import { ROUTES } from "constants/routes";

const NotFoundPage = () => (
  <PageLayout>
    <h1>404</h1>
    <Link to={ROUTES.HOME}>Back home</Link>
  </PageLayout>
);

export default NotFoundPage;
