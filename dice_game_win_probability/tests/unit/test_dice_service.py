import pytest

from dice_game_win_probability.domain.dice import DiceService


@pytest.mark.asyncio
async def test_calculate_probability():
    dice_service = DiceService()
    result = await dice_service.calculate_win_probability(6)
    assert result == 0.5454545454545456
