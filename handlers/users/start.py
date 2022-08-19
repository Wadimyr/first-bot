from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer('Привет')
