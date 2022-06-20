from typing import List

from pyblaze.models.double import Record
from pydantic import BaseModel


class RecentHistoryResponse(BaseModel):
    records: List[Record]
