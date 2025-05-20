"""Main application file for the FastAPI app."""

import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.api.v1.rephrase_endpoints import router as rephrase_router
from app.logging.logger import logger
from app.utils.request_logger import log_request

app = FastAPI()

logger.info("Starting AI-Module application")

class LogExecutionTimeMiddleware(BaseHTTPMiddleware):
    """Middleware to log the execution time of each request."""
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        execution_time = time.time() - start_time
        logger.info("%s %s took %.2f seconds", request.method, request.url, execution_time)
        return response

app.add_middleware(LogExecutionTimeMiddleware)

class LogRequestMiddleware(BaseHTTPMiddleware):
    """Middleware to log the details of each request."""
    async def dispatch(self, request, call_next):
        await log_request(request)
        response = await call_next(request)
        return response

app.add_middleware(LogRequestMiddleware)

@app.exception_handler(Exception)
async def global_exception_handler(exc: Exception):
    """Global exception handler to log and handle unhandled exceptions."""
    logger.error("Unhandled exception: %s", str(exc))
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

app.include_router(rephrase_router, prefix="/api/v1", tags=["Rephrase"])

@app.get("/")
def read_root():
    """
    Handles the root endpoint of the FastAPI application.

    Logs an informational message when the root endpoint is accessed
    and returns a welcome message as a JSON response.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the FastAPI app!"}