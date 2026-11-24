"""`python -m app`: runs the job once. Exit code 0 on success, 1 on failure."""

import argparse
import logging
import os
import sys

from app import task

logger = logging.getLogger("app")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="app",
        description="{{ cookiecutter.description }}",
    )
    parser.parse_args(argv)

    level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        stream=sys.stdout,
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )

    try:
        task.run()
    except Exception as error:
        logger.error("job failed: %s", error)

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
