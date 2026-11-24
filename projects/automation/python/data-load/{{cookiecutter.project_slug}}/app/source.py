"""Extract and transform: read the example CSV into typed records."""

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "data" / "example.csv"


@dataclass(frozen=True)
class Record:
    id: int
    name: str
    updated_at: datetime


def transform(row: dict[str, str]) -> Record:
    return Record(
        id=int(row["id"]),
        name=row["name"].strip(),
        updated_at=datetime.fromisoformat(row["updated_at"].strip()),
    )


def read(path: Path = DEFAULT_PATH) -> list[Record]:
    with path.open(newline="", encoding="utf-8") as handle:
        return [transform(row) for row in csv.DictReader(handle)]
