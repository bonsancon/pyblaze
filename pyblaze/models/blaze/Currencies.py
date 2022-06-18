from typing import List

from pyblaze.models.blaze import Currency
from pydantic import BaseModel


class Currencies(BaseModel):
    data: List[Currency]
