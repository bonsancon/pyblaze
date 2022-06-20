from typing import Union

from pyblaze.models.base import Bet as BaseModel


class Bet(BaseModel):
    cashed_out_at: Union[float, None]
