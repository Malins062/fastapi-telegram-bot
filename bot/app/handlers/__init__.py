__all__ = ("router",)

from aiogram import Router

from .messages import router as messages_commands_router
from .base_commands import router as base_commands_router
from .user_commands import router as user_commands_router

router = Router(name=__name__)

router.include_routers(
    base_commands_router,
    messages_commands_router,
    user_commands_router,
)
