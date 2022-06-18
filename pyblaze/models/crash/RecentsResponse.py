from typing import List

from pyblaze.models.crash import RecentsEntity
from pydantic import BaseModel


class RecentsResponse(BaseModel):
    data: List[RecentsEntity]
