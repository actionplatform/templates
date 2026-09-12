import React from "react";
import { Button } from "components/atoms";
import { PageLayout } from "components/templates";

const HomePage = () => (
  <PageLayout>
    <h1>{{ cookiecutter.project_name }}</h1>
    <p>{{ cookiecutter.description }}</p>
    <Button>Get started</Button>
  </PageLayout>
);

export default HomePage;
