from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.start_kb import restart
from parsers.encar import get_raw_encar
from parsers.exchange_rates import get_rates
from parsers.tax import get_tax

router = Router()


class FSMlink(StatesGroup):
    var = State()


@router.callback_query(Text('l'))
async def link_start(cal: types.CallbackQuery, state: FSMContext):
    await cal.message.answer('Отправьте ссылку с энкара ')
    await state.set_state(FSMlink.var)


@router.message(FSMlink.var)
async def link_answer(message: types.Message, state: FSMContext):
    if message.text.startswith('http://www.encar.com/'):
        print(message.text)
        try:
            data = get_raw_encar(message.text)
            age = data[0]
            engine = data[1]
            capacity = data[2]
            price = data[3]
            age_raw = data[4]
            dvs_type = data[5]
            rates = get_rates()
            usd = rates['USD'][1]
            """ФУНКЦИЯ РАСЧЕТА ГОСПОШЛИН"""
            tax = get_tax(age, engine, '195', capacity, str(price))
            """ЗАТРАТЫ В КОРЕЕ"""
            spending_in_korea = (1500 * usd) + (1500 * usd) * 0.03  # setting
            """КОМИССИЯ В РОССИИ"""
            kom_ru = 50000
            """ДОСТАВКА"""
            delivery = 300000
            total = spending_in_korea + kom_ru + float(
                tax['total'].replace(' ', '').replace(',', '.')) + delivery + price

            result_messsage = f'🕵️ Ваш запрос: 👇\n🚗 Возраст автомобиля: {age_raw} лет\n' \
                              f'🚕 Тип двигателя: {dvs_type}\n' \
                              f'🚙 Объем двигателя: {capacity} м3\n' \
                              f'💰 Стоимость автомобиля в руб: {float(price):.02f} ₽\n\n' \
                              f'• Таможенный сбор: {tax["sbor"]} ₽\n• Утилизационный сбор: {tax["util"]} ₽\n' \
                              f'• Таможенная пошлина: {tax["tax"]} ₽\n• Расходы в Корее: {spending_in_korea:.02f}\n' \
                              f'• Комиссия РФ: {kom_ru} ₽\n' \
                              f'• Доставка {delivery} ₽\n\n ✅ Итоговая стоимость автомобиля: {total:.02f} ₽'
            await message.answer(result_messsage, reply_markup=restart())

        except Exception as e:
            await message.answer('Ссылка не рабочая', reply_markup=restart())
        finally:
            await state.clear()
    else:
        await message.answer('Введите корректную ссылку')
