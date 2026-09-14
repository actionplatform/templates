from typer.testing import CliRunner

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.cli import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.output.strip() == __version__


def test_hello_defaults_to_world():
    result = runner.invoke(app, ["hello"])

    assert result.exit_code == 0
    assert result.output.strip() == "hello, world"


def test_hello_with_name():
    result = runner.invoke(app, ["hello", "--name", "Fernando"])

    assert result.exit_code == 0
    assert result.output.strip() == "hello, Fernando"
