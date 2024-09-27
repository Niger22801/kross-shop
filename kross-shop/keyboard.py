from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

baggyy = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='✅Заказать', callback_data='zakaz'),
    ]

])

trubkaaaaa = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='share number', callback_data='trubka', request_contact=True),
    ]

])

under = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='🏚вернуться', callback_data='home'),
        InlineKeyboardButton(text='✅ заказать', callback_data='offersss'),
        InlineKeyboardButton(text='>>', callback_data='wpered')
    ]

])

sizes = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='M/L', callback_data='ml', ),
        InlineKeyboardButton(text='L/XL', callback_data='lxl'),
        InlineKeyboardButton(text='XL/XXL', callback_data='xlxxl'),
    ]

])

updater = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='NIKE', callback_data='nike_up'),
        InlineKeyboardButton(text='ADIDAS', callback_data='adidas_up'),
        InlineKeyboardButton(text='PUMA', callback_data='puma_up'),
    ],
    [
        InlineKeyboardButton(text='NEW BALANCE', callback_data='balance_up'),
        InlineKeyboardButton(text='REEBOK', callback_data='reebok_up')
    ],
    [
        InlineKeyboardButton(text='OTHER', callback_data='other_up')
    ]

])

online = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='NIKE', callback_data='nike'),
        InlineKeyboardButton(text='ADIDAS', callback_data='adidas'),
        InlineKeyboardButton(text='PUMA', callback_data='puma'),
    ],
    [
        InlineKeyboardButton(text='NEW BALANCE', callback_data='balance'),
        InlineKeyboardButton(text='REEBOK', callback_data='reebok')
    ],
    [
        InlineKeyboardButton(text='OTHER', callback_data='other')
    ]

])
adminpanel = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='➕добавить', callback_data='plus'),
        InlineKeyboardButton(text='🔄изменить',callback_data='update'),
        InlineKeyboardButton(text='➖удалить', callback_data='delete')
    ],
    [
        InlineKeyboardButton(text='Добавить трек код',callback_data='tcode')
    ]

])

offers_add = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='NIKE', callback_data='nike_add', ),
        InlineKeyboardButton(text='ADIDAS', callback_data='adidas_add'),
        InlineKeyboardButton(text='PUMA', callback_data='puma_add'),
    ],
    [
        InlineKeyboardButton(text='NEW BALANCE', callback_data='balance_add'),
        InlineKeyboardButton(text='REEBOK', callback_data='reebok_add')
    ],
    [
        InlineKeyboardButton(text='OTHER', callback_data='other_add')
    ]

])

offers_del = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='NIKE', callback_data='nike_del', ),
        InlineKeyboardButton(text='ADIDAS', callback_data='adidas_del'),
        InlineKeyboardButton(text='PUMA', callback_data='puma_del'),
    ],
    [
        InlineKeyboardButton(text='NEW BALANCE', callback_data='balance_del'),
        InlineKeyboardButton(text='REEBOK', callback_data='reebok_del')
    ],
    [
        InlineKeyboardButton(text='OTHER', callback_data='other_del')
    ]
])

reply = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='📩Белпочта', callback_data='bel'),
    ],
    [
        InlineKeyboardButton(text='📩Европочта', callback_data='euro'),
    ]

])

keyboard12 = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='🛍 - Товары', callback_data='offerss'),
    ],
    [
        InlineKeyboardButton(text='👤 - Связь с администратором', url='https://t.me/Morocco_snk'),
        InlineKeyboardButton(text='ℹ️ - Полная информация', callback_data='info')
    ],
    [
        InlineKeyboardButton(text='📦Получить трек код',callback_data='get_code')
    ]

])

number_k = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='слушать', callback_data='music'),
        InlineKeyboardButton(text='добавить', callback_data='add music'),
    ]

])
