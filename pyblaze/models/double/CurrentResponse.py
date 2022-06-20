from typing import List, Union

from pyblaze.enums import DoubleColor
from pyblaze.models.base import CurrentResponse as BaseModel
from pyblaze.models.double import Bet


class CurrentResponse(BaseModel):
    color: Union[int, None]
    roll: Union[int, None]
    total_red_eur_bet: float
    total_red_bets_placed: int
    total_white_eur_bet: float
    total_white_bets_placed: int
    total_black_eur_bet: float
    total_black_bets_placed: int
    bets: List[Bet]

    def get_color_name(self) -> str:
        return DoubleColor.create_by_int(self.color).value
