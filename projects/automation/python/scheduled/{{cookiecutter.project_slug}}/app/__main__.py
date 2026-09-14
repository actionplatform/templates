"""`python -m app list` and `python -m app run <job>`. Exit code 1 when the job fails or does not exist."""

import argparse
import sys

from app import scheduler


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="app", description="{{ cookiecutter.description }}"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="print the job names")
    run = commands.add_parser("run", help="run one job")
    run.add_argument("job")
    args = parser.parse_args(argv)

    if args.command == "list":
        for name in scheduler.names():
            print(name)

        return 0

    try:
        print(scheduler.run(args.job))
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
