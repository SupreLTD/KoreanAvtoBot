from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


class PriceChoose(CallbackData, prefix='p'):
    action: str
    data: str
    answer: str


def age_choose():
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(text="до 3 лет", callback_data=PriceChoose(action='price',
                                                                                 answer='до 3 лет',
                                                                                 data='0-3').pack()),
           types.InlineKeyboardButton(text="от 3 до 5 лет", callback_data=PriceChoose(action='price',
                                                                                      answer='от 3 до 5 лет',
                                                                                      data='3-5').pack()))
    kb.row(types.InlineKeyboardButton(text='старше 5 лет', callback_data=PriceChoose(action='price',
                                                                                     answer='старше 5 лет',
                                                                                     data='5-7').pack()))

    return kb.as_markup()


def engine_choose():
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(text="Бензин", callback_data=PriceChoose(action='engine',
                                                                               answer='Бензин',
                                                                               data='1').pack()),
           types.InlineKeyboardButton(text="Дизель", callback_data=PriceChoose(action='engine',
                                                                               answer='Дизель',
                                                                               data='2').pack()))
    return kb.as_markup()
