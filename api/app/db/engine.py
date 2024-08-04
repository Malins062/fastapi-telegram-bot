from motor.motor_asyncio import AsyncIOMotorClient

from ..config import settings

mongo_client = AsyncIOMotorClient(settings.db.mongo_uri)
db = mongo_client.get_database(settings.db.mongo_db)
