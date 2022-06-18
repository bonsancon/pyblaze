from typing import Union

from pydantic import BaseModel


class Currency(BaseModel):
    type: str
    name: str
    symbol: str
    eur_rate: Union[float, None]
    fiat: bool
