type WelcomeProps = {
  name: string;
  description: string;
  docsUrl: string;
};

export function Welcome({ name, description, docsUrl }: WelcomeProps) {
  return (
    <section className="welcome">
      <h1>{name}</h1>
      <p>{description}</p>
      <p className="note">Created with the Action Platform.</p>
      <a href={docsUrl}>Documentation</a>
    </section>
  );
}
