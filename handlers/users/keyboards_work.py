import random

from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.start import start_cmd
from keyboards.inline.back import back
from loader import dp


@dp.callback_query_handler(Text(equals='random'))
async def random_number(call: types.CallbackQuery):
    """
    Обработчик кнопки "Рандомное число"
    """
    number = random.randint(0, 50000)

    await call.message.edit_text(f'Твое рандомное число - {number}', reply_markup=back)


@dp.callback_query_handler(Text(equals='back'))
async def go_back(call: types.CallbackQuery):
    """
    Обработчик кнопки "Назад"
    """
    await call.message.delete()
    await start_cmd(message=call.message)


@dp.callback_query_handler(Text(equals='text'))
async def random_quote(call: types.CallbackQuery):
    """
    Обработчик кнопки "Цитата"
    """

    quotes = ['Всегда держи данное слово: это твоя цена.', 'Я не нарушаю правила, я играю по своим!',
              'Мне плевать на тех, кто меня ненавидит. Я живу ради тех людей, которые меня любят.',
              'Я не Минздрав — предупреждать не буду.', 'Цена пацана измеряется выполнением его обещаний.']

    quote = random.choice(quotes)

    await call.message.edit_text(quote, reply_markup=back)
