from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

quiz_menu_in_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Maths"),
            KeyboardButton(text="Uzbek 🇺🇿"),
        ],
        [
            KeyboardButton(text="Logic"),
            KeyboardButton(text="Random"),
            KeyboardButton(text="/help"),
        ],
    ],
    resize_keyboard=True
)