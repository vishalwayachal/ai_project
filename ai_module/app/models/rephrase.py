"""Data models for the rephrase functionality."""

from pydantic import BaseModel

class RephraseRequest(BaseModel):
    """
    RephraseRequest is a data model representing a request to rephrase text.

    Attributes:
        text (str): The text that needs to be rephrased.
    """
    text: str

class RephraseResponse(BaseModel):
    """
    Represents the response model for a rephrasing operation.

    Attributes:
        rephrased_text (str): The text that has been rephrased.
    """
    rephrased_text: str