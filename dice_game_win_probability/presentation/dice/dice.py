from typing import (
    Annotated,
    Any,
)

from fastapi import (
    APIRouter,
    Header,
)

from dice_game_win_probability.di import application_container


dice_router = APIRouter()


@dice_router.get("")
async def calculate_win_probability(k: Annotated[int | None, Header(ge=6, le=99)] = None) -> Any:
    return await application_container.application_service().calculate_win_probability(k)
