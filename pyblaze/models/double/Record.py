from datetime import datetime

from pydantic import BaseModel


class Record(BaseModel):
    id: str
    created_at: datetime
    color: int
    roll: int
    server_seed: str
