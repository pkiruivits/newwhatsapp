from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from app.core.config import settings
from app.api.v1.api import router


from fastapi.openapi.utils import get_openapi

from app.api.errors import HTTPRequestError

#from app.database.redis_client import redis_client
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    app.include_router(router)
    #application.add_event_handler("startup", create_redis_pool)
    #application.add_event_handler("shutdown", close_redis_pool)
    return app


app = create_app()


app.add_middleware(
    CORSMiddleware, 
    allow_origins=settings.ALLOWED_ORIGINS, 
    allow_methods=["*"], 
    allow_headers=["*"], 
    allow_credentials=True 
    )

@app.on_event("startup")
async def startup():
    pass
    #redis_client.start(6379)
    

@app.exception_handler(HTTPRequestError)
async def bad_request_exception_handler(request: Request, exc: HTTPRequestError):
    return JSONResponse(
        status_code=exc.status_code or 400,
        content={
            'code': exc.code,
            'description': exc.description,
            'detail': exc.detail
        }
    )