import unittest

import asyncio

import pytest

from dice_game_win_probability.domain.dice import DiceService, WrongKForDiceError


@pytest.mark.asyncio
async def test_calculate_probability():
    dice_service = DiceService()
    result = await dice_service.calculate_win_probability(6)
    assert result == 0.5454545454545456


@pytest.mark.asyncio
async def test_calculate_win_probability_without_k():
    dice_service = DiceService()
    result = await dice_service.calculate_win_probability()
    assert len(result) == 94


@pytest.mark.asyncio
async def test_calculate_win_probability_with_lower_k_value():
    dice_service = DiceService()
    with pytest.raises(WrongKForDiceError):
        await dice_service.calculate_win_probability(5)


@pytest.mark.asyncio
async def test_calculate_win_probability_with_higher_k_value():
    dice_service = DiceService()
    with pytest.raises(WrongKForDiceError):
        await dice_service.calculate_win_probability(100)
