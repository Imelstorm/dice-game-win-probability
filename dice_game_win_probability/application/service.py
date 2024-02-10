from typing import (
    Union,
    List,
)

from dice_game_win_probability.domain.dice import DiceService


class ApplicationService:
    def __init__(self, dice_service: DiceService):
        self.__dice_service = dice_service

    async def calculate_win_probability(self, k: int | None) -> Union[float, List[float]]:
        return await self.__dice_service.calculate_win_probability(k)
