from typing import Any

import uvicorn
import uvicorn.config
from fastapi import (
    Request,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from dice_game_win_probability.di import di_container
from dice_game_win_probability.presentation import (
    dice_router,
)

CORS_ACCESS_CONTROL_ALLOW_ORIGIN_HEADER_NAME = "Access-Control-Allow-Origin"
WITH_DETAIL_ERROR_INTERNAL_SERVER = {"detail": "Internal Server Error"}

fastapi_app = di_container.app()
config = di_container.config()


log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["loggers"]["uvicorn"]["level"] = config.service.log_level().upper()
log_config["loggers"]["uvicorn"]["error"] = config.service.log_level().upper()

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors.allow_origins(),
    allow_credentials=config.cors.allow_credentials(),
    allow_methods=config.cors.allow_methods(),
    allow_headers=config.cors.allow_headers(),
)

di_container.router().include_router(router=dice_router, prefix="/dice", tags=["dice"])
fastapi_app.include_router(router=di_container.router())


# implementation from https://github.com/tiangolo/fastapi/issues/775#issuecomment-723628299
@fastapi_app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def custom_http_exception_handler(request: Request, _: Any) -> JSONResponse:
    response = JSONResponse(
        content=WITH_DETAIL_ERROR_INTERNAL_SERVER, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    if origin := request.headers.get("origin"):
        cors = CORSMiddleware(
            app=fastapi_app,
            allow_origins=config.cors.allow_origins(),
            allow_credentials=config.cors.allow_credentials(),
            allow_methods=config.cors.allow_methods(),
            allow_headers=config.cors.allow_headers(),
        )
        response.headers.update(cors.simple_headers)
        has_cookie = "cookie" in request.headers
        if cors.allow_all_origins and has_cookie:
            response.headers[CORS_ACCESS_CONTROL_ALLOW_ORIGIN_HEADER_NAME] = origin
        elif not cors.allow_all_origins and cors.is_allowed_origin(origin=origin):
            response.headers[CORS_ACCESS_CONTROL_ALLOW_ORIGIN_HEADER_NAME] = origin
            response.headers.add_vary_header("Origin")
    return response


def run() -> None:
    uvicorn.run(
        "dice_game_win_probability.__main__:fastapi_app",
        host=config.service.host(),
        port=config.service.port(),
        log_level=config.service.log_level(),
        log_config=log_config,
        workers=config.service.workers_count(),
        timeout_keep_alive=config.service.timeout_keepalive(),
        limit_concurrency=config.service.limit_concurrency(),
        backlog=config.service.connection_backlog(),
        loop="uvloop",
        lifespan="on",
        access_log=config.service.access_log(),
    )


if __name__ == "__main__":
    run()
