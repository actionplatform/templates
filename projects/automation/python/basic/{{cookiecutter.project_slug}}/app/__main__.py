"""`python -m app [--name NAME]`: runs the task and prints its result. Exit code 1 on failure."""

import argparse
import sys

from app.tasks.hello import hello


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="app",
        description="{{ cookiecutter.description }}",
    )
    parser.add_argument("--name", default="world", help="who to greet")
    args = parser.parse_args(argv)

    try:
        print(hello(args.name))
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
