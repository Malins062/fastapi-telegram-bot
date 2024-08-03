import json
from datetime import datetime

from api.app.db.engine import db
from api.app.db.models.message import Message, MessageStrType
from api.app.db.models.user import User
from fastapi import HTTPException, Query
from starlette.status import HTTP_404_NOT_FOUND

from app.config import settings

collection = db[Message.ConfigDict.table_name]


async def create_message(text: MessageStrType, sender: User) -> dict:
    msg_text = json.dumps(
        Message(
            dt=datetime.now().strftime(settings.db.datetime_format),
            text=text,
            sender=sender,
        ).dict()
    )
    result = await collection.insert_one({Message.ConfigDict.key: msg_text})

    return {"id": str(result.inserted_id), Message.ConfigDict.key: msg_text}


async def get_messages(
    skip: int = Query(0, ge=0), limit: int = Query(settings.db.pagination_count, gt=0)
):
    cursor = collection.find({}).skip(skip).limit(limit)
    if cursor is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    res = []
    for message in await cursor.to_list(length=limit):
        message.pop("_id")
        res.append(message)

    return res
