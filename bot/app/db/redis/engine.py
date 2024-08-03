from aiogram.fsm.storage.redis import RedisStorage

from ...config import settings

# Redis storage
redis_storage = RedisStorage.from_url(settings.db.redis_url)

# Redis
redis = redis_storage.redis
