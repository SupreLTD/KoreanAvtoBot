from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def main():
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(text="Через ссылку на encar", callback_data='l', ),
           types.InlineKeyboardButton(text="Через ввод цены", callback_data='p'))

    return kb.as_markup()


def restart():
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text='🔄 Новый расчет', callback_data='start'))

    return kb.as_markup()
