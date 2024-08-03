import json
from datetime import datetime
from uuid import uuid4

from api.app.config import settings
from api.app.db.engine import db
from api.app.db.models.message import Message, MessageStrType
from api.app.db.models.user import User

collection = db[Message.ConfigDict.table_name]


async def create_message(text: MessageStrType, sender: User) -> dict:
    msg_text = json.dumps(Message(text=text, sender=sender).dict())
    dt = datetime.now().strftime(settings.db.datetime_format)
    await collection.insert_one({dt: msg_text})
    return {"Success": True}


async def get_messages(msg_filter=None, skip: int = 0, limit: int = 10):
    if msg_filter is None:
        msg_filter = {}
    res = []

    cursor = (collection.find(msg_filter).
              skip(skip).
              limit(limit))
    if cursor is None:
        return res

    for message in await cursor.to_list(length=limit):
        message.pop("_id")
        res.append(message)

    return res
