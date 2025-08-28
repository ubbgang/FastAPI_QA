from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from utils.my_logging import Logging

def validation_exception_handler(request: Request, exc: RequestValidationError):
    
    error_details = {
        "body": exc.body,
        "errors": exc.errors()
    }
    Logging().log_attention(f"Error when validate data. {error_details}")
    
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "error": {
                "code": "invalid_request",
                "message": "Error when validate data"
            }
        },
    )