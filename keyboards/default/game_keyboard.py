from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

game_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎮Да, играем"), KeyboardButton(text="🎃Нет, не играем")
        ]
    ], resize_keyboard=True
)