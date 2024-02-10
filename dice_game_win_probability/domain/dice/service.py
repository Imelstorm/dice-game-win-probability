from typing import (
    Union,
    List,
)


class DiceService(object):

    __MIN_K = 6
    __MAX_K = 99

    def __init__(self):
        self.__probabilities: list[float] = []

    async def calculate_win_probability(self, k: int | None) -> Union[float, List[float]]:
        if not k:
            return await self.__calculate_serial_probability()

        if self.__MIN_K > k > self.__MAX_K:
            raise ValueError(f"k should be between {self.__MIN_K} and {self.__MAX_K}")

        return await self.__calculate_single_probability(k)

    async def __calculate_serial_probability(self) -> [float]:
        if self.__probabilities:
            return self.__probabilities

        for k in range(self.__MIN_K, self.__MAX_K + 1):
            prob_bob_wins = (1 / k) * (1 / (1 - ((k - 1) / k) ** 2))
            self.__probabilities.append(prob_bob_wins)

        return self.__probabilities

    async def __calculate_single_probability(self, k: int) -> float:
        if not self.__probabilities:
            await self.__calculate_serial_probability()
        return self.__probabilities[k - self.__MIN_K]
