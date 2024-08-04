from pydantic import BaseModel

from .user import User

MessageStrType = str


class Message(BaseModel):
    """
    Mongo model table for message
    """

    dt: str
    text: str
    sender: User

    class ConfigDict:
        table_name = "messages"
        key = "msg"
        from_attributes = True
