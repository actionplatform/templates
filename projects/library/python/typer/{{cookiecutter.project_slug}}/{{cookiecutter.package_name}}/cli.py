"""Commands. Each one is a function on `app`; the body stays small and calls plain functions."""

import typer

from {{ cookiecutter.package_name }} import __version__

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.description }}",
    no_args_is_help=True,
)


@app.command()
def version() -> None:
    """Print the version."""
    typer.echo(__version__)


@app.command()
def hello(
    name: str = typer.Option("world", "--name", "-n", help="Who to greet"),
) -> None:
    """Say hello."""
    typer.echo(f"hello, {name}")
