from typing import List

from pyblaze.models.blaze import ChatRoomConfig
from pydantic import BaseModel


class ChatRoomsResponse(BaseModel):
    data: List[ChatRoomConfig]
