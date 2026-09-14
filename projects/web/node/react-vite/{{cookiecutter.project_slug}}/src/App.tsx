import { Welcome } from "./components/Welcome";

export const PROJECT = {
  name: "{{ cookiecutter.project_name }}",
  description: "{{ cookiecutter.description }}",
  docsUrl: "https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}#readme",
};

export function App() {
  return (
    <main className="app">
      <Welcome
        name={PROJECT.name}
        description={PROJECT.description}
        docsUrl={PROJECT.docsUrl}
      />
    </main>
  );
}
