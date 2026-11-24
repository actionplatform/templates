from datetime import UTC, datetime

import pytest

from app import source


def test_transform_parses_and_strips():
    record = source.transform(
        {
            "id": "7",
            "name": " Seven ",
            "updated_at": "2026-01-01T00:00:00+00:00",
        }
    )

    assert record == source.Record(
        7, "Seven", datetime(2026, 1, 1, tzinfo=UTC)
    )


def test_transform_rejects_bad_id():
    with pytest.raises(ValueError):
        source.transform(
            {
                "id": "x",
                "name": "n",
                "updated_at": "2026-01-01T00:00:00+00:00",
            }
        )


def test_read_example_file():
    records = source.read()

    assert [r.id for r in records] == [1, 2, 3]
    assert all(r.updated_at.tzinfo is not None for r in records)


def test_read_custom_path(tmp_path):
    path = tmp_path / "in.csv"
    path.write_text("id,name,updated_at\n9,Nine,2026-02-01T00:00:00+00:00\n")

    assert [r.id for r in source.read(path)] == [9]
