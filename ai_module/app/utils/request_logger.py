"""Utility for logging details of incoming HTTP requests."""

import json

from fastapi import Request

from app.logging.logger import logger


async def log_request(request: Request):
    """Log the details of an incoming request, including method, URL, query params, and body.

    Args:
        request (Request): The incoming HTTP request.
    """
    try:
        body = await request.body()
        body = body.decode("utf-8")
        body = json.loads(body) if body else "Empty Body"
    except json.JSONDecodeError as jde:
        body = f"Unable to parse body: {str(jde)}"
    except TypeError as te:
        body = f"Type error in body: {str(te)}"

    logger.info("Request: %s %s", request.method, request.url)
    logger.info("Query Params: %s", request.query_params)
    logger.info("Body: %s", body)