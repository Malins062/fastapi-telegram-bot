from api.app.db.models.user import User
from pydantic import BaseModel

MessageStrType = str


class Message(BaseModel):
    """
    Redis model table for message
    """

    text: str
    sender: User

    class ConfigDict:
        table_name = "messages"
        from_attributes = True
