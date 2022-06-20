from typing import List

from pyblaze.models.crash import Bet
from pydantic import BaseModel


class GetGameByIdResponse(BaseModel):
    id: str
    server_seed: str
    crash_point: float
    bets: List[Bet]
    total_bets_placed: int
    totalBetPages: int
