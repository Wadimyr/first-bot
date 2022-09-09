from aiogram.dispatcher.filters.state import StatesGroup, State


class GetInfo(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    quote = State()
    media = State()