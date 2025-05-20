"""Utility for generating standardized API responses."""

from fastapi.responses import JSONResponse

def success_response(data):
    """
    Generates a standardized success response.

    Args:
        data (Any): The data to include in the response body.

    Returns:
        JSONResponse: A JSON response with a status of "ok" and the provided data, 
                      along with a 200 HTTP status code.
    """
    return JSONResponse(content={
        "status": "ok",
        "data": data
    }, status_code=200)

def error_response(error_code, error_message, error_fields=None):
    """
    Generates a standardized error response in JSON format.

    Args:
        error_code (str): A unique code representing the specific error.
        error_message (str): A descriptive message explaining the error.
        error_fields (list, optional): A list of fields related to the error, if applicable. Defaults to an empty list.

    Returns:
        JSONResponse: A JSON response object with the error details and a status code of 400.
    """
    if error_fields is None:
        error_fields = []
    return JSONResponse(content={
        "status": "error",
        "error_code": error_code,
        "error_message": error_message,
        "error_fields": error_fields
    }, status_code=400)