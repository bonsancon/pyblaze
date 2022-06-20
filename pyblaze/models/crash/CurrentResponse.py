from typing import List, Union

from pyblaze.models.crash import Bet
from pydantic import BaseModel


class CurrentResponse(BaseModel):
    crash_point: Union[float, None]
    total_eur_bet: float
    total_bets_placed: int
    total_eur_won: Union[float, None]
    bets: List[Bet]
