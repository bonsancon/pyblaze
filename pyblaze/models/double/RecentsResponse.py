from typing import List

from pyblaze.models.double import RecentsEntity
from pydantic import BaseModel


class RecentsResponse(BaseModel):
    data: List[RecentsEntity]
