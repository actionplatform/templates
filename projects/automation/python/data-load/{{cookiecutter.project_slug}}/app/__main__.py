"""`python -m app [--dry-run]`. Exit code 1 when the load fails."""

import argparse
import os
import sys

import psycopg

from app import load, source


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="app",
        description="{{ cookiecutter.description }}",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="run the load and roll the transaction back",
    )
    args = parser.parse_args(argv)

    try:
        records = source.read()
        with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
            counts = load.load(conn, records, dry_run=args.dry_run)
    except Exception as error:
        print(f"error: {error!r}", file=sys.stderr)

        return 1

    suffix = " (dry run, rolled back)" if args.dry_run else ""
    print(
        f"inserted={counts.inserted} updated={counts.updated} "
        f"unchanged={counts.unchanged}{suffix}"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
