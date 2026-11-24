"""The job's work: reads its config from the environment."""

import logging
import os

logger = logging.getLogger(__name__)


def run() -> str:
    name = os.environ.get("GREETING_NAME", "world").strip()

    if not name:
        raise ValueError("GREETING_NAME must not be empty")

    message = f"hello, {name}"
    logger.info(message)

    return message
