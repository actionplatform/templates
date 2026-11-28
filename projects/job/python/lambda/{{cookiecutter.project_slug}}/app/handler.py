"""Lambda entrypoint: a scheduled event runs the task once, an SQS batch runs it per record."""

import json
import logging
import os
from typing import Any

from app import task

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())


def process_record(record: dict[str, Any]) -> str:
    body = json.loads(record["body"])

    return task.run(str(body.get("name", "")))


def handler(event: dict[str, Any], _context: Any = None) -> dict[str, Any]:
    records = event.get("Records")

    if records is None:
        return {"message": task.run()}

    failures = []

    for record in records:
        try:
            process_record(record)
        except Exception as error:
            logger.error(
                "record %s failed: %s", record.get("messageId"), error
            )
            failures.append({"itemIdentifier": record.get("messageId")})

    return {"batchItemFailures": failures}
