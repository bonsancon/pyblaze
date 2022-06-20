from typing import List

from pyblaze.models.crash import Record
from pydantic import BaseModel


class RecentHistoryResponse(BaseModel):
    records: List[Record]
    total_pages: int
    total_records: int
