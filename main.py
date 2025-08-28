from fastapi import FastAPI
from utils.exception_handlers import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from utils.my_logging import Logging
from utils.pathes import Pathes
from api.v1 import router as api_v1_router

load_dotenv()
Logging.setup_root_logger(Pathes.folder_logs,Pathes.log_fastapi)


env = os.getenv("ENV") 
if not env:
    raise Exception(f"Domain or env is empty")

middleware = [
    Middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE"],
        allow_headers=["Content-Type"], 
        max_age=600,  
    )
    ]


if env == "dev":
    app = FastAPI(middleware=middleware)
else:
    app = FastAPI(middleware=middleware,docs_url=None,redoc_url=None,openapi_url=None,swagger_ui_oauth2_redirect_url=None)
    
app.add_exception_handler(RequestValidationError, validation_exception_handler) # type: ignore

app.include_router(api_v1_router, prefix="/api/v1",tags=["ApiV1"])
    






