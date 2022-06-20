from typing import Union

from pydantic import BaseModel


class Result(BaseModel):
    color: str
    roll: int
    hash: Union[str, None]
