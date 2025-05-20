"""Unit tests for the rephrase service."""

from app.services.rephrase_service import rephrase_text

def test_rephrase_text():
    """Test the rephrase_text function to ensure it returns the expected output."""
    input_text = "This is a test."
    expected_output = "Rephrased text here"
    assert rephrase_text(input_text) == expected_output

# Ensure no OCR-related tests are present.