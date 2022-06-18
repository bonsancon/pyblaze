from datetime import datetime

from pyblaze.enums import DoubleColor
from pydantic import BaseModel


class RecentsEntity(BaseModel):
    id: str
    created_at: datetime
    color: int
    roll: int
    server_seed: str

    def get_color_name(self) -> str:
        return DoubleColor.create_by_int(self.color).value
