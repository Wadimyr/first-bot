import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.start import start_cmd
from keyboards.inline.back import back
from loader import dp
from states.get_info import GetInfo


@dp.callback_query_handler(Text(equals='random'))
async def random_number(call: types.CallbackQuery):
    """
    Обработчик кнопки "Рандомное число"
    """
    number = random.randint(0, 50000)

    await call.message.edit_text(f'Твое рандомное число - {number}', reply_markup=back)


@dp.callback_query_handler(Text(equals='back'), state='*')
async def go_back(call: types.CallbackQuery, state: FSMContext):
    """
    Обработчик кнопки "Назад"
    """
    await state.reset_state(True)
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


@dp.callback_query_handler(Text(equals='empty'))
async def do_nothing(call: types.CallbackQuery):
    await call.message.edit_text("Здесь ничего нет", reply_markup=back)


@dp.callback_query_handler(Text(equals="test"))
async def new_test(call: types.CallbackQuery):
    mes = await call.message.edit_text("Хорошо, вы попали на тестирование.\n"
                                       "Первый вопрос: <b>2 + 2 = ?</b>", reply_markup=back)

    await GetInfo.q1.set()

    state = dp.current_state(chat=call.message.chat.id, user=call.message.chat.id)

    await state.update_data(
        {
            'message_id': mes.message_id
        }
    )


@dp.message_handler(state=GetInfo.q1)
async def get_q1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    message_id = data.get('message_id')

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message_id)

    mes = await message.answer('Супер! А вот и второй вопрос:\n'
                               '<b>10 + 10 = ?</b>')

    await state.update_data(
        {
            'message_id': mes.message_id,
            'question_1': text,
            'correct_answer_1': 4
        }
    )

    await state.set_state(GetInfo.q2)


@dp.message_handler(state=GetInfo.q2)
async def get_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    message_id = data.get('message_id')

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message_id)

    mes = await message.answer('Финальый вопрос!\n'
                               '<b>3214 + 423 = ?</b>')

    await state.update_data(
        {
            'message_id': mes.message_id,
            'question_2': text,
            'correct_answer_2': 20
        }
    )
    await state.set_state(GetInfo.q3)


@dp.message_handler(state=GetInfo.q3)
async def get_q3(message: types.Message, state: FSMContext):
    data = await state.get_data()

    message_id = data.get('message_id')

    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message_id)

    q1 = data.get('question_1')
    q2 = data.get('question_2')
    q3 = message.text

    correct_q1 = data.get('correct_answer_1')
    correct_q2 = data.get('correct_answer_2')
    correct_q3 = 3637

    await state.reset_state(with_data=True)

    counter_true = 0
    counter_false = 0

    if int(q1) == correct_q1:
        final_q1 = q1 + '<b> + </b>'
        counter_true += 1
    else:
        counter_false += 1
        final_q1 = q1 + '<b> - </b>'

    if int(q2) == correct_q2:
        counter_true += 1
        final_q2 = q2 + '<b> + </b>'
    else:
        counter_false += 1
        final_q2 = q2 + '<b> - </b>'

    if int(q3) == correct_q3:
        counter_true += 1
        final_q3 = q3 + '<b> + </b>'
    else:
        counter_false += 1
        final_q3 = q3 + '<b> - </b>'

    await message.answer('Тест завершен!\n'
                         'Вот ваши результаты:\n\n'
                         f'{final_q1}\n'
                         f'{final_q2}\n'
                         f'{final_q3}\n\n'
                         f'Количество правильных ответов: <b>{counter_true}</b>\n'
                         f'Количество неправильный ответов: <b>{counter_false}</b>', reply_markup=back)


@dp.callback_query_handler(Text(equals="smile"))
async def smile(call: types.CallbackQuery):
    quotes = ["😀", '🫠', "🤯"]

    quote = random.choice(quotes)
    await call.message.edit_text(quote, reply_markup=back)
