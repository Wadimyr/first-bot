from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from keyboards.inline.menu_kb import menu
from loader import dp


@dp.message_handler(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(text='Привет, выбери действие на клавиатуре ниже.',
                         reply_markup=menu)
