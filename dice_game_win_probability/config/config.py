from pydantic import BaseSettings


_SERVICE_CONFIG_PREFIX = "DICE_GAME_WIN_PROBABILITY_"


class Cors(BaseSettings):
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True

    class Config:
        env_prefix = _SERVICE_CONFIG_PREFIX + "CORS_"


class Service(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8080
    log_level: str = "debug"
    uvicorn_debug: bool = False
    workers_count: int = 1
    timeout_keepalive: int = 3
    limit_concurrency: int = 20
    connection_backlog: int = 150
    access_log: bool = False
    openapi_file: str | None = None
    redoc_url: str | None = None
    docs_url: str | None = "/docs"
    api_prefix: str = ""

    class Config:
        env_prefix = _SERVICE_CONFIG_PREFIX + "SERVICE_"
