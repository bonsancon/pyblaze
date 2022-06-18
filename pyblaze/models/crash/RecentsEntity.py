from pydantic import BaseModel


class RecentsEntity(BaseModel):
    id: str
    crash_point: float
