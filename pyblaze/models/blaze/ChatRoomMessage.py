from datetime import datetime

from pyblaze.models.blaze import ChatRoomMessageUser
from pydantic import BaseModel


class ChatRoomMessage(BaseModel):
    id: str
    text: str
    available: bool
    created_at: datetime
    user: ChatRoomMessageUser
