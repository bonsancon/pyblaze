from typing import Union

from pydantic import BaseModel


class Result(BaseModel):
    crash_point: float
    hash: Union[str, None]
