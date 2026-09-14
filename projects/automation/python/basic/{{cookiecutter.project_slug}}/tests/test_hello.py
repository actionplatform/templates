import pytest

from app.__main__ import main
from app.tasks.hello import hello


def test_hello():
    assert hello("Fernando") == "hello, Fernando"


def test_hello_refuses_empty_name():
    with pytest.raises(ValueError):
        hello("  ")


def test_main_prints_and_exits_zero(capsys):
    assert main(["--name", "Fernando"]) == 0
    assert capsys.readouterr().out.strip() == "hello, Fernando"


def test_main_reports_failure(capsys):
    assert main(["--name", " "]) == 1
    assert "name is required" in capsys.readouterr().err
