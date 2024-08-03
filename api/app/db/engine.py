from motor.motor_asyncio import AsyncIOMotorClient

from api.app.config import settings

mongo_client = AsyncIOMotorClient(settings.db.mongo_uri)
db = mongo_client.get_database(settings.db.mongo_db)
