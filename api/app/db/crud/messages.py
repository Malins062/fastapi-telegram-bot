from api.app.db.engine import db
from api.app.db.models.message import Message, MessageStrType
from api.app.db.models.user import User

collection = db[Message.ConfigDict.table_name]


async def create_message(text: MessageStrType, sender: User) -> dict:
    message = Message(text=text, sender=sender).dict()
    await collection.insert_one(message)
    return {"Success": True}


async def get_messages(skip: int = 0, limit: int = 10):
    cursor = await collection.find().skip(skip).limit(limit)
    res = [message for message in cursor]
    return res
