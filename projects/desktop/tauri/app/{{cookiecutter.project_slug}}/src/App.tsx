import { FormEvent, useEffect, useState } from "react";

import { AppInfo, appInfo, greet } from "./api";

export const PROJECT = {
  name: "{{ cookiecutter.project_name }}",
  description: "{{ cookiecutter.description }}",
  docsUrl: "https://{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}#readme",
};

export function App() {
  const [info, setInfo] = useState<AppInfo | null>(null);
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    appInfo()
      .then(setInfo)
      .catch((reason) => setError(String(reason)));
  }, []);

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setError("");

    try {
      setMessage(await greet(name));
    } catch (reason) {
      setError(String(reason));
    }
  }

  return (
    <main className="app">
      <section className="welcome">
        <h1>{PROJECT.name}</h1>
        {PROJECT.description && <p>{PROJECT.description}</p>}
        <p className="note">Created with the Action Platform.</p>

        <form onSubmit={onSubmit}>
          <input
            aria-label="Name"
            value={name}
            onChange={(event) => setName(event.target.value)}
            placeholder="Your name"
          />
          <button type="submit">Greet</button>
        </form>

        {message && <p role="status">{message}</p>}
        {error && <p role="alert">{error}</p>}
        {info && (
          <p className="note">
            {info.name} {info.version} on {info.os}
          </p>
        )}
        <a href={PROJECT.docsUrl}>Documentation</a>
      </section>
    </main>
  );
}
