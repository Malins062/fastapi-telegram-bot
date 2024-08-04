import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault
from db.engine import redis_storage as storage

from .config import settings
from .handlers import router
from .loggers.logger import init_logger

ALLOWED_UPDATES = ["message", "callback_query", "inline_query"]


async def start_bot(bot: Bot):
    commands = [
        BotCommand(
            command="create_message",
            description="Создать сообщение",
        ),
        BotCommand(
            command="get_messages",
            description="Получить все сообщения",
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start():
    bot = Bot(
        token=str(settings.bot_token),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher(storage=storage)

    dp.startup.register(start_bot)

    dp.include_router(router)

    try:
        # Ignoring all cached commands before the bot starts working
        await bot.delete_webhook(drop_pending_updates=True)

        # Start polling with only ALLOWED updates
        await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    init_logger()

    asyncio.run(start())
