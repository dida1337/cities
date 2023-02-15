from aiogram.dispatcher.filters.state import StatesGroup, State


class Game_State(StatesGroup):
    play_or_no = State()
    play = State()