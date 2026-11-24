import logging
import subprocess
import sys
from pathlib import Path

from app import task
from app.__main__ import main

ROOT = Path(__file__).resolve().parent.parent


def test_run_defaults_to_world(monkeypatch):
    monkeypatch.delenv("GREETING_NAME", raising=False)

    assert task.run() == "hello, world"


def test_run_reads_name_from_env(monkeypatch):
    monkeypatch.setenv("GREETING_NAME", " Ada ")

    assert task.run() == "hello, Ada"


def test_main_exits_zero_and_logs(monkeypatch, caplog):
    monkeypatch.setenv("GREETING_NAME", "Ada")

    with caplog.at_level(logging.INFO):
        assert main([]) == 0

    assert "hello, Ada" in caplog.text


def test_main_exits_one_and_logs_the_error(monkeypatch, caplog):
    monkeypatch.setenv("GREETING_NAME", " ")

    with caplog.at_level(logging.INFO):
        assert main([]) == 1

    assert "job failed: GREETING_NAME must not be empty" in caplog.text


def run_module(**env: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "app"],
        cwd=ROOT,
        env={"PATH": "", **env},
        capture_output=True,
        text=True,
    )


def test_cli_logs_to_stdout():
    result = run_module(GREETING_NAME="Ada")

    assert result.returncode == 0
    assert "hello, Ada" in result.stdout


def test_cli_log_level_filters_output():
    result = run_module(LOG_LEVEL="WARNING")

    assert result.returncode == 0
    assert result.stdout == ""


def test_cli_failure_exit_code():
    result = run_module(GREETING_NAME="")

    assert result.returncode == 1
    assert "job failed" in result.stdout
