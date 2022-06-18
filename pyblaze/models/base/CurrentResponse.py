from datetime import datetime
from typing import Union

from pydantic import BaseModel


class CurrentResponse(BaseModel):
    id: str
    status: str
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]
