from pydantic import BaseModel


class ChatRoomConfig(BaseModel):
    id: int
    name: str
