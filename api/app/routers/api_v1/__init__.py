from fastapi import APIRouter

from ...config import settings
from .messages import router as messages_router

router = APIRouter(prefix=settings.api.v1.prefix, tags=["API_v1"])
router.include_router(
    messages_router,
)
