from pydantic import BaseModel


class User(BaseModel):
    id: int
    id_str: str
    username: str
    rank: str
