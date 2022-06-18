from pydantic import BaseModel


class Announcement(BaseModel):
    id: int
    content: str
    action_description: str
    action_active: bool
    action_href: str
