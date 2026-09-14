from app import scheduler
from app.__main__ import main
from app.jobs import example


def test_example_job_returns_a_summary():
    assert example.run().startswith("example ran at ")


def test_registry_lists_and_runs():
    assert scheduler.names() == ["example"]
    assert scheduler.run("example").startswith("example ran at ")


def test_main_list_and_run(capsys):
    assert main(["list"]) == 0
    assert capsys.readouterr().out.strip() == "example"
    assert main(["run", "example"]) == 0
    assert "example ran at" in capsys.readouterr().out


def test_main_unknown_job_fails(capsys):
    assert main(["run", "nope"]) == 1
    assert "unknown job" in capsys.readouterr().err
