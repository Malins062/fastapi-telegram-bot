__all__ = ("router",)

from aiogram import Router

from .messages_commands import router as messages_commands_router
from .user_commands import router as user_commands_router

router = Router(name=__name__)

router.include_routers(
    messages_commands_router,
    user_commands_router,
)
