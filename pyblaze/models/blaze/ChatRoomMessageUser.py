from typing import Union

from pydantic import BaseModel


class ChatRoomMessageUser(BaseModel):
    id: str
    username: str
    label: Union[str, None]
    level: int
    rank: str
