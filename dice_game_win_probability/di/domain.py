from dependency_injector import (
    containers,
    providers,
)

from dice_game_win_probability.domain.dice import DiceService


class DomainContainer(containers.DeclarativeContainer):
    dice_service = providers.Singleton(DiceService)
