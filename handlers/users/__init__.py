from aiogram import Dispatcher, types


from aiogram.dispatcher.filters import Text, CommandStart

from states.game_state import Game_State
from . import(
   start,

)

def register_handlers(dp: Dispatcher):

   dp.register_message_handler(start.start_game, commands=['start'], state='*')
   dp.register_message_handler(start.start_play, text=["🎮Да, играем", "🎃Нет, не играем"], state=Game_State.play_or_no)
   dp.register_callback_query_handler(start.next_city, Text(contains="next_city_"), state='*')
   dp.register_message_handler(start.regular_play, state=Game_State.play)



