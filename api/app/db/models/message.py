from pydantic import BaseModel, Field
from uuid import UUID, uuid4

from api.app.db.models.user import User


class Message(BaseModel):
    """
    Redis model table for message
    """

    id: UUID = Field(default_factory=uuid4)
    text: str
    sender: User

    class ConfigDict:
        table_name = "messages"
        from_attributes = True
