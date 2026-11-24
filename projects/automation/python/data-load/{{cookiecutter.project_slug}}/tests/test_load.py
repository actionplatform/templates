import os
from datetime import UTC, datetime

import psycopg
import pytest

from app import load
from app.__main__ import main
from app.source import Record

DATABASE_URL = os.environ.get("DATABASE_URL")

pytestmark = pytest.mark.skipif(
    not DATABASE_URL, reason="DATABASE_URL is not set"
)

T1 = datetime(2026, 1, 1, tzinfo=UTC)
T2 = datetime(2026, 1, 2, tzinfo=UTC)


@pytest.fixture
def conn():
    assert DATABASE_URL
    with psycopg.connect(DATABASE_URL, autocommit=True) as connection:
        connection.execute("DROP TABLE IF EXISTS records")
        yield connection
        connection.execute("DROP TABLE IF EXISTS records")


def rows(conn):
    return conn.execute(
        "SELECT id, name, updated_at FROM records ORDER BY id"
    ).fetchall()


def test_first_load_inserts_all(conn):
    counts = load.load(conn, [Record(1, "a", T1), Record(2, "b", T1)])

    assert counts == load.Counts(inserted=2, updated=0, unchanged=0)
    assert len(rows(conn)) == 2


def test_second_load_changes_nothing(conn):
    records = [Record(1, "a", T1), Record(2, "b", T1)]
    load.load(conn, records)
    before = rows(conn)

    counts = load.load(conn, records)

    assert counts == load.Counts(inserted=0, updated=0, unchanged=2)
    assert rows(conn) == before


def test_changed_record_is_updated(conn):
    load.load(conn, [Record(1, "a", T1), Record(2, "b", T1)])

    counts = load.load(conn, [Record(1, "a", T1), Record(2, "b2", T2)])

    assert counts == load.Counts(inserted=0, updated=1, unchanged=1)
    assert rows(conn)[1][1] == "b2"


def test_dry_run_rolls_back(conn):
    counts = load.load(conn, [Record(1, "a", T1)], dry_run=True)

    assert counts.inserted == 1
    assert conn.execute("SELECT to_regclass('records')").fetchone() == (None,)


@pytest.mark.usefixtures("conn")
def test_main_twice_reports_no_changes(capsys):
    assert main([]) == 0
    assert "inserted=3 updated=0 unchanged=0" in capsys.readouterr().out
    assert main([]) == 0
    assert "inserted=0 updated=0 unchanged=3" in capsys.readouterr().out
