"""AWS Lambda entry point — adapts the ASGI app with Mangum."""

import os

from mangum import Mangum

from app import create_app

app = create_app()

handler = Mangum(
    app,
    lifespan="off",
    api_gateway_base_path=os.environ.get("API_STAGE", ""),
)


def lambda_handler(event, context):
    return handler(event, context)
