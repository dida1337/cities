import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Game, ReplyKeyboardRemove

from keyboards.default.game_keyboard import game_start
from keyboards.inline.game_keyboard import game_key_word
from states.game_state import Game_State

all_city = ['Львов', 'Киев', 'Харьков', 'Одесса', 'Днепр', 'Запорожье', 'Луцк', 'Луцьк', 'Ровно', 'Тернополь', 'Хмельницкий', 'Черновцы', 'Ивано-Франковск',  'Ужгород', 'Винница',
            'Алушта', 'Ялта']

copy_list_for_game = []

used_city = []


async def start_game(message: types.Message, state: FSMContext):
    await state.finish()
    await state.reset_state()
    global copy_list_for_game
    copy_list_for_game = all_city.copy()
    used_city.clear()
    await message.answer("🏙<b>Привет, поиграем в города?</b>", reply_markup=game_start)

    await Game_State.play_or_no.set()


async def start_play(message: types.Message, state: FSMContext):
    play_choice = message.text



    first_city_from_bot = random.choice(copy_list_for_game)

    copy_list_for_game.remove(first_city_from_bot)
    used_city.append(first_city_from_bot)

    if play_choice == "🎮Да, играем":
        await message.answer("Хорошо, тогда начнем!", reply_markup=ReplyKeyboardRemove())
        await message.answer(f'''Хорошо, тогда начнем!
Я выбираю город:  {first_city_from_bot}. Твой город на букву {first_city_from_bot[-1]}
''',reply_markup=await game_key_word(first_city_from_bot))


async def next_city(callback_data: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    city_from_bot = callback_data.data.split('_')[-1]

    await callback_data.message.answer(f'''Твой город на букву {city_from_bot[-1]}
Можешь начинать вводить: ''', reply_markup=ReplyKeyboardRemove())

    await state.update_data(city_from_bot=city_from_bot)
    await Game_State.play.set()



async def regular_play(message: types.Message, state: FSMContext):
    city_from_user = message.text

    data = await state.get_data()

    city_from_bot = data.get('city_from_bot')

    print('Город от юзера - ', city_from_user)
    print('Город от бота - ', city_from_bot)

    if city_from_user in copy_list_for_game and city_from_user not in used_city:
        if city_from_user[0].lower() == city_from_bot[-1].lower():
            await message.answer(f"{city_from_user} - ваш город")
            copy_list_for_game.remove(city_from_user)
            used_city.append(city_from_user)
            city_from_bot = [city for city in copy_list_for_game if city.startswith(city_from_user[-1].upper())]

            if city_from_bot:
                bot_choice = city_from_bot[0]
                await message.answer(f"Мой город - {bot_choice}. Введи город на букву {bot_choice[-1]}", reply_markup= await game_key_word(bot_choice))
                copy_list_for_game.remove(bot_choice)
                used_city.append(bot_choice)
            else:
                await message.answer("Я не знаю больше городов на эту букву. Ты выиграл!")
    else:
        await message.answer('''Город уже был использован или ты должен ввести город на последнюю букву предыдущего города
Напиши команду /start если попал в тупик!''')
