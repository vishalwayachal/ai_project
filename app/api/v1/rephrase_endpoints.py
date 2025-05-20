"""API endpoints for text rephrasing functionality."""

from fastapi import APIRouter
from pydantic import ValidationError
from app.utils.response_utils import success_response, error_response
from app.models.rephrase import RephraseRequest, RephraseResponse
from app.services.rephrase_service import rephrase_text
from app.logging.logger import logger

router = APIRouter()

@router.post("/rephrase", response_model=RephraseResponse)
def rephrase_text_endpoint(payload: RephraseRequest):
    """Handle the rephrase text API endpoint.

    Args:
        payload (RephraseRequest): The input payload containing the text to rephrase.

    Returns:
        RephraseResponse: The rephrased text wrapped in a response model.
    """
    logger.info("Received request to rephrase text")
    try:
        payload = RephraseRequest(**payload.dict())
        rephrased_text = rephrase_text(payload.text)
        logger.info("Successfully rephrased text")
        return success_response({"rephrased_text": rephrased_text})
    except ValidationError as ve:
        logger.error("Validation error: %s", ve.json())
        return error_response(422, "Validation Error", ve.errors())
    except ValueError as ve:
        logger.error("Value error: %s", str(ve))
        return error_response(400, "Bad Request")
    except RuntimeError as re:
        logger.error("Runtime error: %s", str(re))
        return error_response(500, "Runtime Error")
        