from typing import List

from pyblaze.models.blaze import ChatRoomMessage
from pydantic import BaseModel


class ChatRoomResponse(BaseModel):
    messages: List[ChatRoomMessage]
