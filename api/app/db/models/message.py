from api.app.db.models.user import User
from pydantic import BaseModel

MessageStrType = str


class Message(BaseModel):
    """
    Redis model table for message
    """

    dt: str
    text: str
    sender: User

    class ConfigDict:
        table_name = "messages"
        key = "msg"
        from_attributes = True
