import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault

from config import settings
from db.redis.engine import redis_storage as storage
from handlers import router

ALLOWED_UPDATES = ["message", "callback_query", "inline_query"]


async def start_bot(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Стартовая страница бота",
        ),
        BotCommand(
            command="help",
            description="Краткая справочная информация",
        ),
        BotCommand(
            command="send",
            description="Отправить сообщение",
        ),
        BotCommand(
            command="get_all",
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
    asyncio.run(start())
