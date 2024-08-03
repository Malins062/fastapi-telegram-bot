from api.app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = AsyncIOMotorClient(settings.db.mongo_uri)
db = mongo_client.get_database(settings.db.mongo_db)
