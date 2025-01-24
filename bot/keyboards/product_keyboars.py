from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_menu_btn = InlineKeyboardButton(
    text="В меню", callback_data="menu"
)

main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[[main_menu_btn]]
)

get_data_kb = [
    [
        InlineKeyboardButton(
            text="Получить данные по товару", callback_data="get_data"
        )
    ]
]

get_data_kb = InlineKeyboardMarkup(inline_keyboard=get_data_kb)