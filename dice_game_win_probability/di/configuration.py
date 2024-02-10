from dependency_injector import (
    containers,
    providers,
)

from dice_game_win_probability.config import (
    Cors,
    Service,
)


class Configuration(containers.DeclarativeContainer):
    service = providers.Configuration(pydantic_settings=[Service()])
    cors = providers.Configuration(pydantic_settings=[Cors()])
