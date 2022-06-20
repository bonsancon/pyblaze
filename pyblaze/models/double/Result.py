from pydantic import BaseModel


class Result(BaseModel):
    color: str
    roll: int
