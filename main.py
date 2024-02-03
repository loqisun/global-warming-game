key = '6918758649:AAGiAXmu3QTj5F-h1t1ID5pxSp7v1MHQirI'

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = key

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Конечно! Давай начнем."),
            types.KeyboardButton(text="Что? Какая игра? Не, давай потом.")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Ответь, готов ли ты начать"
    )
    await message.answer(f"Привет! Готов к игре?", reply_markup=keyboard)


@dp.message(F.text.lower() == "конечно! давай начнем.")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="а"),
        types.KeyboardButton(text="б"),
        types.KeyboardButton(text="в")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"Отлично! Тогда вот первый вопрос:\n\n"
                        "<b>Что является главным фактором глобального потепления?</b>\n"
                            "а)Человеческая деятельность\n"
                            "б)Рост вулканической активности\n"
                            "в)Вымирание многих видов животных, что изменило экосистему планеты", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "а")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="г"),
        types.KeyboardButton(text="д"),
        types.KeyboardButton(text="е")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n"
                         "Следующий вопрос:\n\n"
                        "<b>Что называют парниковым эффектом?</b>\n"
                            "г)Поглощение углекислого газа растениями\n"
                            "д)Увеличение концентрации углекислого газа в атмосфере\n"
                            "е)Когда тепло удерживается на поверхности Земли парниковыми газами", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "б")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="г"),
        types.KeyboardButton(text="д"),
        types.KeyboardButton(text="е")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>а)Человеческая деятельность</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Что называют парниковым эффектом?</b>\n"
                            "г)Поглощение углекислого газа растениями\n"
                            "д)Увеличение концентрации углекислого газа в атмосфере\n"
                            "е)Когда тепло удерживается на поверхности Земли парниковыми газами", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "в")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="г"),
        types.KeyboardButton(text="д"),
        types.KeyboardButton(text="е")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>а)Человеческая деятельность</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Что называют парниковым эффектом?</b>\n"
                            "г)Поглощение углекислого газа растениями\n"
                            "д)Увеличение концентрации углекислого газа в атмосфере\n"
                            "е)Когда тепло удерживается на поверхности Земли парниковыми газами", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "г")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="ж"),
        types.KeyboardButton(text="з"),
        types.KeyboardButton(text="и")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>е)Когда тепло удерживается на поверхности Земли парниковыми газами</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Какая страна вырабатывала больше всего углекислого газа в 2018 году?</b>\n"
                            "ж)Объединённые Арабские Эмираты\n"
                            "з)Кувейт\n"
                            "и)Катар", reply_markup=keyboard)

@dp.message(F.text.lower() == "д")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="ж"),
        types.KeyboardButton(text="з"),
        types.KeyboardButton(text="и")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>е)Когда тепло удерживается на поверхности Земли парниковыми газами</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Какая страна вырабатывала больше всего углекислого газа в 2018 году?</b>\n"
                            "ж)Объединённые Арабские Эмираты\n"
                            "з)Кувейт\n"
                            "и)Катар", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "е")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="ж"),
        types.KeyboardButton(text="з"),
        types.KeyboardButton(text="и")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Какая страна вырабатывала больше всего углекислого газа в 2018 году?</b>\n"
                            "ж)Объединённые Арабские Эмираты\n"
                            "з)Кувейт\n"
                            "и)Катар", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "ж")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="к"),
        types.KeyboardButton(text="л"),
        types.KeyboardButton(text="м")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>и)Катар</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Какой регион мира является наиболее уязвим к изменениям климата?</b>\n"
                            "к)Африка\n"
                            "л)Южная Америка\n"
                            "м)Австралия", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "з")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="к"),
        types.KeyboardButton(text="л"),
        types.KeyboardButton(text="м")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>и)Катар</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Какой регион мира является наиболее уязвим к изменениям климата?</b>\n"
                            "к)Африка\n"
                            "л)Южная Америка\n"
                            "м)Австралия", reply_markup=keyboard)

@dp.message(F.text.lower() == "и")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="к"),
        types.KeyboardButton(text="л"),
        types.KeyboardButton(text="м")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n"  
                         "Следующий вопрос:\n\n"
                        "<b>Какой регион мира является наиболее уязвим к изменениям климата?</b>\n"
                            "к)Африка\n"
                            "л)Южная Америка\n"
                            "м)Австралия", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "к")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="н"),
        types.KeyboardButton(text="о"),
        types.KeyboardButton(text="п")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n"  
                         "Следующий вопрос:\n\n"
                        "<b>Какие животные находятся под угрозой исчезновения из-за глобального потепления?</b>\n"
                            "н)Тигры, гепарды и слоны\n"
                            "о)Черепахи, лосось и лягушки\n"
                            "п)Киты и черепахи", reply_markup=keyboard)

@dp.message(F.text.lower() == "л")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="н"),
        types.KeyboardButton(text="о"),
        types.KeyboardButton(text="п")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n"  
                         "Правильный ответ: <i>к)Африка</i>\n\n"
                         "Следующий вопрос:\n\n"
                        "<b>Какие животные находятся под угрозой исчезновения из-за глобального потепления?</b>\n"
                            "н)Тигры, гепарды и слоны\n"
                            "о)Черепахи, лосось и лягушки\n"
                            "п)Киты и черепахи", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "м")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="н"),
        types.KeyboardButton(text="о"),
        types.KeyboardButton(text="п")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n"  
                         "Правильный ответ: <i>к)Африка</i>\n\n"
                         "Следующий вопрос:\n\n"
                        "<b>Какие животные находятся под угрозой исчезновения из-за глобального потепления?</b>\n"
                            "н)Тигры, гепарды и слоны\n"
                            "о)Черепахи, лосось и лягушки\n"
                            "п)Киты и черепахи", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "н")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="р"),
        types.KeyboardButton(text="с"),
        types.KeyboardButton(text="т")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n"  
                         "Правильный ответ: <i>о)Черепахи, лосось и лягушки</i>\n\n"
                         "Следующий вопрос:\n\n"
                        "<b>Когда впервые сообщили о глобальном изменении климата?</b>\n"
                            "р)1980\n"
                            "с)1957\n"
                            "т)1992", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "о")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="р"),
        types.KeyboardButton(text="с"),
        types.KeyboardButton(text="т")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n"  
                         "Следующий вопрос:\n\n"
                        "<b>Когда впервые сообщили о глобальном изменении климата?</b>\n"
                            "р)1980\n"
                            "с)1957\n"
                            "т)1992", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "п")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="р"),
        types.KeyboardButton(text="с"),
        types.KeyboardButton(text="т")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n"  
                         "Правильный ответ: <i>о)Черепахи, лосось и лягушки</i>\n\n"
                         "Следующий вопрос:\n\n"
                        "<b>Когда впервые сообщили о глобальном изменении климата?</b>\n"
                            "р)1980\n"
                            "с)1957\n"
                            "т)1992", reply_markup=keyboard)

@dp.message(F.text.lower() == "р")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="у"),
        types.KeyboardButton(text="ф"),
        types.KeyboardButton(text="х")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n"  
                         "Следующий вопрос:\n\n"
                        "<b>Каковы последствия таяния ледников из-за глобального потепления?</b>\n"
                            "у)Морская фауна активно разрастается\n"
                            "ф)Умирают морские обитатели\n"
                            "х)Поднимается уровень мирового океана", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "с")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="у"),
        types.KeyboardButton(text="ф"),
        types.KeyboardButton(text="х")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>р)1980</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Каковы последствия таяния ледников из-за глобального потепления?</b>\n"
                            "у)Морская фауна активно разрастается\n"
                            "ф)Умирают морские обитатели\n"
                            "х)Поднимается уровень мирового океана", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "т")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="у"),
        types.KeyboardButton(text="ф"),
        types.KeyboardButton(text="х")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>р)1980</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>Каковы последствия таяния ледников из-за глобального потепления?</b>\n"
                            "у)Морская фауна активно разрастается\n"
                            "ф)Умирают морские обитатели\n"
                            "х)Поднимается уровень мирового океана", reply_markup=keyboard)

@dp.message(F.text.lower() == "у")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="ц"),
        types.KeyboardButton(text="ч"),
        types.KeyboardButton(text="ш")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>х)Поднимается уровень мирового океана</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>На сколько выросла средняя температура на Земле начиная с 1905 года?</b>\n"
                            "ц)На три градуса\n"
                            "ч)Меньше чем на один градус\n"
                            "ш)На пять градусов", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "ф")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="ц"),
        types.KeyboardButton(text="ч"),
        types.KeyboardButton(text="ш")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>х)Поднимается уровень мирового океана</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>На сколько выросла средняя температура на Земле начиная с 1905 года?</b>\n"
                            "ц)На три градуса\n"
                            "ч)Меньше чем на один градус\n"
                            "ш)На пять градусов", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "х")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="ц"),
        types.KeyboardButton(text="ч"),
        types.KeyboardButton(text="ш")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>На сколько выросла средняя температура на Земле начиная с 1905 года?</b>\n"
                            "ц)На три градуса\n"
                            "ч)Меньше чем на один градус\n"
                            "ш)На пять градусов", reply_markup=keyboard)

@dp.message(F.text.lower() == "ц")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="э"),
        types.KeyboardButton(text="ю"),
        types.KeyboardButton(text="я")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>ч)Меньше чем на один градус</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>К какому году ожидаются такие показатели — повышение среднегодовой температуры на 2 градуса?</b>\n"
                            "э)2040\n"
                            "ю)2025\n"
                            "я)2077", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "ч")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="э"),
        types.KeyboardButton(text="ю"),
        types.KeyboardButton(text="я")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>К какому году ожидаются такие показатели — повышение среднегодовой температуры на 2 градуса?</b>\n"
                            "э)2040\n"
                            "ю)2025\n"
                            "я)2077", reply_markup=keyboard)

@dp.message(F.text.lower() == "ш")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="э"),
        types.KeyboardButton(text="ю"),
        types.KeyboardButton(text="я")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>ч)Меньше чем на один градус</i>\n\n" 
                         "Следующий вопрос:\n\n"
                        "<b>К какому году ожидаются такие показатели — повышение среднегодовой температуры на 2 градуса?</b>\n"
                            "э)2040\n"
                            "ю)2025\n"
                            "я)2077", reply_markup=keyboard)

@dp.message(F.text.lower() == "э")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="b"),
        types.KeyboardButton(text="c"),
        types.KeyboardButton(text="d")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Правильно!</b>\n\n" 
                         "И последний вопрос:\n\n"
                        "<b>Следствием климатических изменений может стать...</b>\n"
                            "b)Появление новых коралловых рифов\n"
                            "c)Снижение температуры на полюсах Земли\n"
                            "d)Уменьшение количества питьевой воды", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "ю")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="b"),
        types.KeyboardButton(text="c"),
        types.KeyboardButton(text="d")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>э)2040</i>\n\n" 
                         "И последний вопрос:\n\n"
                        "<b>Следствием климатических изменений может стать...</b>\n"
                            "b)Появление новых коралловых рифов\n"
                            "c)Снижение температуры на полюсах Земли\n"
                            "d)Уменьшение количества питьевой воды", reply_markup=keyboard)

@dp.message(F.text.lower() == "я")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="b"),
        types.KeyboardButton(text="c"),
        types.KeyboardButton(text="d")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери вариант ответа"
    )
    await message.answer(f"<b>Неправильно!</b>\n\n" 
                         "Правильный ответ: <i>э)2040</i>\n\n" 
                         "И последний вопрос:\n\n"
                        "<b>Следствием климатических изменений может стать...</b>\n"
                            "b)Появление новых коралловых рифов\n"
                            "c)Снижение температуры на полюсах Земли\n"
                            "d)Уменьшение количества питьевой воды", reply_markup=keyboard)

@dp.message(F.text.lower() == "b")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="Спасибо за игру!")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Игра окончилась!"
    )
    await message.answer("<b>Неправильно!</b>\n\n"
                         "Правильный ответ: <i>d)Уменьшение количества питьевой воды</i>\n\n", reply_markup=keyboard)
#await message.answer("Спасибо за игру! Надеюсь тебе понравился тест и ты узнал много нового. Приходи еще!😁")

@dp.message(F.text.lower() == "c")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="Спасибо за игру!")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Игра окончилась!"
    )
    await message.answer("<b>Неправильно!</b>\n\n"
                         "Правильный ответ: <i>d)Уменьшение количества питьевой воды</i>\n\n", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "d")
async def game_goes(message: types.Message):
    kb = [
    [
        types.KeyboardButton(text="Спасибо за игру!")
    ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Игра окончилась!"
    )
    await message.answer("<b>Правильно!</b>", reply_markup=keyboard)

@dp.message(F.text.lower() == "спасибо за игру!")
async def game_ends(message: types.Message):
    await message.answer("Спасибо тебе за игру тоже! Надеюсь тебе понравился тест и ты узнал много нового. Приходи еще!😁")

@dp.message(F.text.lower() == "что? какая игра? не, давай потом.")
async def game_ends(message: types.Message):
    await message.answer("А я думал, что мы подружились...😢")

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())