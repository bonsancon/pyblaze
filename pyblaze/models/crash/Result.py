from pydantic import BaseModel


class Result(BaseModel):
    crash_point: float
