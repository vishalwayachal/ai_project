"""Service layer for text rephrasing using transformers."""

from transformers import pipeline
from app.logging.logger import logger

# Initialize the text generation pipeline (placeholder for actual implementation)
rephrase_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")

def rephrase_text(input_text: str) -> str:
    """Rephrase the input text using a transformers pipeline.

    Args:
        input_text (str): The text to be rephrased.

    Returns:
        str: The rephrased text.
    """
    try:
        if not input_text.strip():
            raise ValueError("Input text cannot be empty")
        logger.info("Rephrasing text using transformers pipeline")
        result = rephrase_pipeline(input_text, max_length=512, num_return_sequences=1)
        logger.info("Text rephrased successfully")
        return result[0]['generated_text']
    except ValueError as ve:
        logger.error("Validation error in rephrase service: %s", str(ve))
        raise
    except RuntimeError as re:
        logger.error("Runtime error in rephrase service: %s", str(re))
        raise