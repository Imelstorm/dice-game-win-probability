from dependency_injector import (
    containers,
    providers,
)

from dice_game_win_probability.application import ApplicationService


class ApplicationContainer(containers.DeclarativeContainer):
    dice_service = providers.Dependency()

    application_service = providers.Singleton(
        ApplicationService,
        dice_service=dice_service,
    )
