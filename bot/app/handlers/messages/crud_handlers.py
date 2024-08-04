from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils import markdown

from ...config import settings

router = Router(name=__name__)


@router.message(Command("send", prefix=settings.prefixes_command))
async def handle_send(message: types.Message):
    await message.answer(
        text=markdown.text(
            "Отправлено сообщение:",
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(Command("get_all", prefix=settings.prefixes_command))
async def handle_get_all(message: types.Message):
    await message.answer(
        text=markdown.text(
            "Получены сообщения:",
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
    )
