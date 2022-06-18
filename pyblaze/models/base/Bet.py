from typing import Union

from pyblaze.models import User
from pydantic import BaseModel


class Bet(BaseModel):
    id: str
    amount: int
    win_amount: Union[float, None]
    currency_type: str
    status: str
    user: User
