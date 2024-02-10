from dependency_injector import (
    containers,
    providers,
)
from fastapi import (
    APIRouter,
    FastAPI,
)

from dice_game_win_probability.logger import init_logger
from .configuration import Configuration


class Core(containers.DeclarativeContainer):
    config = providers.Container(Configuration)
    init_logger(config.service.log_level())
    app = providers.Singleton(
        FastAPI,
        debug=config.service.uvicorn_debug(),
        docs_url=config.service.docs_url(),
        redoc_url=config.service.redoc_url(),
    )
    router = providers.Singleton(APIRouter, prefix=config.service.api_prefix())
