from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def game_key_word(city: str):
    game_key = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Продолжить", callback_data=f'next_city_{city}')
            ]
        ]
    )
    return game_key