from pydantic import BaseModel


class Time(BaseModel):
    epoch: int
