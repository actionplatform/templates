from datetime import datetime, timezone


def run() -> str:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    return f"example ran at {now}"
