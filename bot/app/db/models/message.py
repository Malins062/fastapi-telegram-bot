import json

from pydantic import BaseModel

from ..engine import redis
from .user import User

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

    @classmethod
    async def redis_get_messages(cls):
        msgs = await redis.get(cls.ConfigDict.table_name)
        if msgs:
            return json.loads(msgs)
        else:
            return None

    @classmethod
    async def redis_save_messages(cls, messages: str):
        await redis.set(cls.ConfigDict.table_name, messages)

    @classmethod
    async def redis_clear_messages(cls):
        await redis.delete(cls.ConfigDict.table_name)
