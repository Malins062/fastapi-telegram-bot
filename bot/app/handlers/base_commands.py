from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from ..config import settings

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(
            f"😉 Привет, {markdown.hbold(message.from_user.full_name)}!",
            "Я могу отправлять сообщения на API!",
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(Command("help", prefix=settings.prefixes_command))
async def handle_help(message: types.Message, state: FSMContext):
    await message.answer(
        text=markdown.text(
            "Описание бота",
            " ",
            sep="\n",
        ),
        reply_markup=types.ReplyKeyboardRemove(),
    )
