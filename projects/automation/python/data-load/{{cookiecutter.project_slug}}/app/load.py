"""Load: idempotent upsert of records into Postgres in one transaction."""

from dataclasses import dataclass

import psycopg

from app.source import Record

CREATE = """
CREATE TABLE IF NOT EXISTS records (
    id integer PRIMARY KEY,
    name text NOT NULL,
    updated_at timestamptz NOT NULL
)
"""

UPSERT = """
INSERT INTO records (id, name, updated_at)
VALUES (%s, %s, %s)
ON CONFLICT (id) DO UPDATE
SET name = EXCLUDED.name, updated_at = EXCLUDED.updated_at
WHERE records.name IS DISTINCT FROM EXCLUDED.name
   OR records.updated_at IS DISTINCT FROM EXCLUDED.updated_at
RETURNING (xmax = 0) AS inserted
"""


@dataclass(frozen=True)
class Counts:
    inserted: int = 0
    updated: int = 0
    unchanged: int = 0


def load(
    conn: psycopg.Connection, records: list[Record], dry_run: bool = False
) -> Counts:
    inserted = updated = 0
    with conn.transaction(force_rollback=dry_run), conn.cursor() as cur:
        cur.execute(CREATE)
        for record in records:
            cur.execute(UPSERT, (record.id, record.name, record.updated_at))
            row = cur.fetchone()
            if row is None:
                continue
            if row[0]:
                inserted += 1
            else:
                updated += 1

    return Counts(inserted, updated, len(records) - inserted - updated)
