import json

import requests
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
from aiogram.utils import markdown

from db.models.message import Message
from config import settings

router = Router(name=__name__)
TIME_OUT = 2.5


class Form(StatesGroup):
    message = State()


@router.message(Command("create_message", prefix=settings.prefixes_command))
async def handle_create_message(message: types.Message, state: FSMContext):
    await state.set_state(Form.message)
    await message.reply("Введите текст сообщения:")


@router.message(Form.message)
async def process_message(message: types.Message, state: FSMContext):
    await state.clear()

    url = f"{settings.api.host}:{settings.api.port}" + "".join(
        [settings.api.prefix, settings.api.v1.prefix, settings.api.v1.message]
    )
    data = {
        "id": message.from_user.id,
        "full_name": message.from_user.full_name,
    }
    params = {"text": message.text}

    try:
        response = requests.post(url, data=json.dumps(data), params=params, timeout=TIME_OUT)
    except requests.Timeout:
        await message.reply(f"Сервер не отвечает: {url}")
        return

    if response.status_code == 200:
        await message.reply("Сообщение успешно создано.")
    else:
        await message.reply("Не удалось создать сообщение.")


@router.message(Command("get_messages", prefix=settings.prefixes_command))
async def handle_get_messages(message: types.Message):
    url = f"{settings.api.host}:{settings.api.port}" + "".join(
        [settings.api.prefix, settings.api.v1.prefix, settings.api.v1.messages]
    )
    params = {
        "skip": 0,
        "limit": 100,
    }
    try:
        response = requests.get(url, params=params, timeout=TIME_OUT)
    except requests.Timeout:
        await message.reply(f"Сервер не отвечает: {url}")
        return

    messages = response.json()
    if not messages or response.status_code != 200:
        await message.reply("Сообщений нет.")
    else:
        for msg in messages:
            data = msg.get('msg')
            data = Message.parse_raw(data)
            text = f"Дата и время: {data.dt}!\n" \
                   f"Автор: {data.sender.full_name} #{data.sender.id}\n" \
                   f"Текст: {data.text}"
            await message.answer(text)
