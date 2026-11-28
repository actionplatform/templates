import json
import logging
import subprocess
import sys
from pathlib import Path

import pytest

from app import task
from app.__main__ import main
from app.handler import handler

ROOT = Path(__file__).resolve().parent.parent
EVENTS = ROOT / "events"


def sqs_event(*bodies: str) -> dict:
    return {
        "Records": [
            {"messageId": f"m{i}", "body": body}
            for i, body in enumerate(bodies)
        ]
    }


def test_run_defaults_to_world(monkeypatch):
    monkeypatch.delenv("GREETING_NAME", raising=False)

    assert task.run() == "hello, world"


def test_run_reads_name_from_env(monkeypatch):
    monkeypatch.setenv("GREETING_NAME", " Ada ")

    assert task.run() == "hello, Ada"


def test_run_prefers_the_subject_over_env(monkeypatch):
    monkeypatch.setenv("GREETING_NAME", "Ada")

    assert task.run("Grace") == "hello, Grace"


def test_run_rejects_an_empty_name(monkeypatch):
    monkeypatch.setenv("GREETING_NAME", " ")

    with pytest.raises(ValueError, match="GREETING_NAME"):
        task.run()


def test_handler_runs_the_task_on_a_scheduled_event(monkeypatch):
    monkeypatch.setenv("GREETING_NAME", "Ada")
    event = json.loads((EVENTS / "schedule.json").read_text())

    assert handler(event) == {"message": "hello, Ada"}


def test_handler_processes_every_sqs_record(caplog):
    event = json.loads((EVENTS / "sqs.json").read_text())

    with caplog.at_level(logging.INFO):
        assert handler(event) == {"batchItemFailures": []}

    assert "hello, Ada" in caplog.text


def test_handler_reports_only_the_failed_records(monkeypatch):
    monkeypatch.setenv("GREETING_NAME", "")
    event = sqs_event('{"name": "Ada"}', "{}", "not json")

    assert handler(event) == {
        "batchItemFailures": [
            {"itemIdentifier": "m1"},
            {"itemIdentifier": "m2"},
        ]
    }


def test_main_exits_zero_and_logs(monkeypatch, caplog):
    monkeypatch.setenv("GREETING_NAME", "Ada")

    with caplog.at_level(logging.INFO):
        assert main([str(EVENTS / "schedule.json")]) == 0

    assert "hello, Ada" in caplog.text


def test_main_exits_one_when_the_task_fails(monkeypatch, caplog):
    monkeypatch.setenv("GREETING_NAME", " ")

    with caplog.at_level(logging.INFO):
        assert main([str(EVENTS / "schedule.json")]) == 1

    assert "job failed: GREETING_NAME must not be empty" in caplog.text


def test_main_exits_one_when_a_record_fails(tmp_path):
    event = tmp_path / "event.json"
    event.write_text(json.dumps(sqs_event("not json")))

    assert main([str(event)]) == 1


def run_module(*args: str, **env: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "app", *args],
        cwd=ROOT,
        env={"PATH": "", **env},
        capture_output=True,
        text=True,
    )


def test_cli_logs_to_stdout():
    result = run_module(GREETING_NAME="Ada")

    assert result.returncode == 0
    assert "hello, Ada" in result.stdout


def test_cli_failure_exit_code():
    result = run_module(GREETING_NAME="")

    assert result.returncode == 1
    assert "job failed" in result.stdout
