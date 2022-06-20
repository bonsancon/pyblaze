from datetime import datetime
from typing import List

from pyblaze.models.double import Bet
from pydantic import BaseModel


class GetGameByIdResponse(BaseModel):
    id: str
    created_at: datetime
    color: int
    roll: int
    bets: List[Bet]
    totalBetPages: int
