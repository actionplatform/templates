from datetime import UTC, datetime


def run() -> str:
    now = datetime.now(UTC).isoformat(timespec="seconds")

    return f"example ran at {now}"
