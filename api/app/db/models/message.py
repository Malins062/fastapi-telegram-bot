from typing import Optional
from uuid import UUID, uuid4

from api.app.db.models.user import User
from pydantic import BaseModel, Field

MessageStrType = str


class Message(BaseModel):
    """
    Redis model table for message
    """

    id: Optional[UUID] = Field(default_factory=uuid4)
    text: str
    sender: User

    class ConfigDict:
        table_name = "messages"
        from_attributes = True
