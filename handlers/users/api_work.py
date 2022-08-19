from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('api'))
async def api_cmd(message: types.Message):
    await message.answer('Я работаю :)')  # Отправляем сообщение с текстом

    await message.answer(
        f'<b>ID пользователя - {message.from_user.id}</b>\n'  # Получаем из объекта message ID пользователя
        f'<b>ID чата - {message.chat.id}</b>\n\n'  # Получаем из message ID чата
        f'<i>Имя пользователя - {message.from_user.first_name}</i>\n'  # Получаем из message Имя пользователя
        f'<u>Фамилия пользователя - {message.from_user.last_name}</u>\n'  # Получаем из message Фамилию пользователя (если её нет, то вернет None)
        f'<s>Username пользователя - {message.from_user.username}</s>\n\n'  # Получаем из message Username пользователя (если нет, то вернет None)
        f'<a href="https://vk.com/feed">Дата отправки сообщения</a> - {message.date}'
        # Получаем из message Дату отправки сообщения (от пользователя)
    )
