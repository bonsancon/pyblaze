from datetime import datetime

from pydantic import BaseModel


class Record(BaseModel):
    id: str
    status: str
    created_at: datetime
    crash_point: float
    server_seed: str
