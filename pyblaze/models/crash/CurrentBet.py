from typing import Union

from pyblaze.models.base import Bet as BaseModel


class CurrentBet(BaseModel):
    cashed_out_at: Union[float, None]
