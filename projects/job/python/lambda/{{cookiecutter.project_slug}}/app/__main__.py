"""`python -m app [event.json]`: invokes the handler locally. Exit code 0 on success, 1 on failure."""

import argparse
import json
import logging
import os
import sys

from app.handler import handler

logger = logging.getLogger("app")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="app",
        description="{{ cookiecutter.description }}",
    )
    parser.add_argument("event", nargs="?", default="events/schedule.json")
    args = parser.parse_args(argv)

    level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        stream=sys.stdout,
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )

    try:
        with open(args.event) as file:
            result = handler(json.load(file))
    except Exception as error:
        logger.error("job failed: %s", error)

        return 1

    if result.get("batchItemFailures"):
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
