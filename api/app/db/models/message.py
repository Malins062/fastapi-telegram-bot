from pydantic import BaseModel

from api.app.db.models.user import User


class Message(BaseModel):
    """
    Redis model table for message
    """

    id: int
    text: str
    user: User

    class ConfigDict:
        table_name = "messages"
        from_attributes = True
