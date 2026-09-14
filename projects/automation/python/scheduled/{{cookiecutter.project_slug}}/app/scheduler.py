"""The job registry. Nothing here runs by itself: cron, CI, EventBridge or a CronJob calls `python -m app run <job>`."""

from collections.abc import Callable

from app.jobs import example

Job = Callable[[], str]

JOBS: dict[str, Job] = {
    "example": example.run,
}


def names() -> list[str]:
    return sorted(JOBS)


def run(name: str) -> str:
    try:
        job = JOBS[name]
    except KeyError:
        raise ValueError(
            f"unknown job {name!r}; known: {', '.join(names())}"
        ) from None

    return job()
