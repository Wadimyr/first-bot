from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=3,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text='Рандомное число', callback_data='random'),
                                    InlineKeyboardButton(text='Цитата', callback_data='text')
                                ],
                                [
                                    InlineKeyboardButton(text='Смайлик', callback_data='smile'),
                                    InlineKeyboardButton(text='Начать тестирование', callback_data='test'),
                                    InlineKeyboardButton(text='Получить File ID', callback_data='empty')
                                ]
                            ])
