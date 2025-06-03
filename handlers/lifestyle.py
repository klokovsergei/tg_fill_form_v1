from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from database.database import users_db
from keyboards.join_kb import create_join_keyboard
from models.user_data import UserData
from services.storage_user_data import save_users_db

from lexicon.lexicon import LEXICON
from states.habits import FSMHabits
from states.lifestyle import FSMLifestyle

router = Router()


@router.callback_query(F.data == 'lifestyle', StateFilter(default_state))
async def process_start_fill_lifestyle(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(
        text=LEXICON['meals_per_day'],
        reply_markup=create_join_keyboard(
            *[f'button_meals_{i}' for i in range(1, 6)], row_width=2
        ))
    await state.set_state(FSMLifestyle.meals_per_day)


@router.callback_query(F.data == 'yes_lifestyle')
async def process_answer_filled_lifestyle(callback: CallbackQuery):
    await callback.answer(text=LEXICON['lifestyle_yes'])


@router.callback_query(StateFilter(FSMLifestyle.meals_per_day))
async def process_fill_meals_per_day(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(meals_per_day=callback.data)
    await callback.message.answer(text=LEXICON['breakfast_time'])
    await state.set_state(FSMLifestyle.breakfast_time)


@router.message(
    StateFilter(FSMLifestyle.breakfast_time),
    F.text.len() > 4)
async def process_fill_breakfast_time(message: Message, state: FSMContext):
    await state.update_data(breakfast_time=message.text.strip())
    await message.answer(
        text=LEXICON['heaviest_meal'],
        reply_markup=create_join_keyboard(
            'button_breakfast', 'button_lunch', 'button_dinner', 'button_equal',
            row_width=2
        ))
    await state.set_state(FSMLifestyle.heaviest_meal)


@router.callback_query(StateFilter(FSMLifestyle.heaviest_meal))
async def process_fill_heaviest_meal(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(heaviest_meal=callback.data)
    await callback.message.answer(
        text=LEXICON['cooking_attitude'],
        reply_markup=create_join_keyboard(
            'button_cooking_love', 'button_cooking_neutral', 'button_cooking_rarely'
        ))
    await state.set_state(FSMLifestyle.cooking_attitude)


@router.callback_query(StateFilter(FSMLifestyle.cooking_attitude))
async def process_fill_cooking_attitude(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(cooking_attitude=callback.data)
    await callback.message.answer(
        text=LEXICON['snacks_frequency'],
        reply_markup=create_join_keyboard(
            'never', 'sometimes', 'always'
        ))
    await state.set_state(FSMLifestyle.snacks_frequency)


@router.callback_query(StateFilter(FSMLifestyle.snacks_frequency))
async def process_fill_snacks_frequency(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(snacks_frequency=callback.data)
    await callback.message.answer(text=LEXICON['frequent_foods'])
    await state.set_state(FSMLifestyle.frequent_foods)


@router.message(
    StateFilter(FSMLifestyle.frequent_foods),
    F.text.len() > 5)
async def process_fill_frequent_foods(message: Message, state: FSMContext):
    await state.update_data(frequent_foods=message.text.strip())
    await message.answer(text=LEXICON['daily_drinks'])
    await state.set_state(FSMLifestyle.daily_drinks)


@router.message(
    StateFilter(FSMLifestyle.daily_drinks),
    F.text.len() > 5)
async def process_fill_daily_drinks(message: Message, state: FSMContext):
    await state.update_data(daily_drinks=message.text.strip())
    await message.answer(
        text=LEXICON['food_intolerance'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button', 'dont_know',
            row_width=3
        ))
    await state.set_state(FSMLifestyle.food_intolerance)


@router.callback_query(StateFilter(FSMLifestyle.food_intolerance))
async def process_fill_food_intolerance(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(food_intolerance=callback.data)

    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['food_intolerance_details'])
        await state.set_state(FSMLifestyle.food_intolerance_details)
    else:
        await state.update_data(food_intolerance_details='')
        await callback.message.answer(
            text=LEXICON['eating_features'],
            reply_markup=create_join_keyboard(
                'overeating', 'on_the_go', 'sweets_after_meal',
                'emotional_eating', 'no_features', 'other'
            ))
        await state.set_state(FSMLifestyle.eating_features)


@router.message(
    StateFilter(FSMLifestyle.food_intolerance_details),
    F.text.len() > 5)
async def process_fill_food_intolerance_details(message: Message, state: FSMContext):
    await state.update_data(food_intolerance_details=message.text.strip())
    await message.answer(
        text=LEXICON['eating_features'],
        reply_markup=create_join_keyboard(
            'overeating', 'on_the_go', 'sweets_after_meal',
            'emotional_eating', 'no_features', 'other'
        ))
    await state.set_state(FSMLifestyle.eating_features)


@router.callback_query(StateFilter(FSMLifestyle.eating_features))
async def process_fill_eating_features(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(eating_features=callback.data)

    if callback.data == 'other':
        await callback.message.answer(text=LEXICON['eating_features_details'])
        await state.set_state(FSMLifestyle.eating_features_details)
    else:
        await state.update_data(eating_features_details='')
        await callback.message.answer(
            text=LEXICON['past_diets'],
            reply_markup=create_join_keyboard(
                'no_button', 'yes_button',
                row_width=2
            ))
        await state.set_state(FSMLifestyle.past_diets)


@router.message(
    StateFilter(FSMLifestyle.eating_features_details),
    F.text.len() > 5)
async def process_fill_eating_features_details(message: Message, state: FSMContext):
    await state.update_data(eating_features_details=message.text.strip())
    await message.answer(
        text=LEXICON['past_diets'],
        reply_markup=create_join_keyboard(
            'no_button', 'yes_button',
            row_width=2
        ))
    await state.set_state(FSMLifestyle.past_diets)


@router.callback_query(StateFilter(FSMLifestyle.past_diets))
async def process_fill_past_diets(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(past_diets=callback.data)

    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['past_diets_details'])
        await state.set_state(FSMLifestyle.past_diets_details)
    else:
        await state.update_data(past_diets_details='')
        await callback.message.answer(
            text=LEXICON['supplements'],
            reply_markup=create_join_keyboard(
                'no_button', 'yes_button',
                row_width=2
            ))
        await state.set_state(FSMLifestyle.supplements)


@router.message(
    StateFilter(FSMLifestyle.past_diets_details),
    F.text.len() > 5)
async def process_fill_past_diets_details(message: Message, state: FSMContext):
    await state.update_data(past_diets_details=message.text.strip())
    await message.answer(
        text=LEXICON['supplements'],
        reply_markup=create_join_keyboard(
            'no_button', 'yes_button',
            row_width=2
        ))
    await state.set_state(FSMLifestyle.supplements)


@router.callback_query(StateFilter(FSMLifestyle.supplements))
async def process_fill_supplements(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(supplements=callback.data)

    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['supplements_details'])
        await state.set_state(FSMLifestyle.supplements_details)
    else:
        await state.update_data(supplements_details='')
        await callback.message.answer(
            text=LEXICON['readiness_to_change'],
            reply_markup=create_join_keyboard(
                *[f'button_{i}' for i in range(1, 11)], row_width=5
            ))
        await state.set_state(FSMLifestyle.readiness_to_change)


@router.message(
    StateFilter(FSMLifestyle.supplements_details),
    F.text.len() > 5)
async def process_fill_supplements_details(message: Message, state: FSMContext):
    await state.update_data(supplements_details=message.text.strip())
    await message.answer(
        text=LEXICON['readiness_to_change'],
        reply_markup=create_join_keyboard(
            *[f'button_{i}' for i in range(1, 11)], row_width=5
        ))
    await state.set_state(FSMLifestyle.readiness_to_change)

@router.callback_query(StateFilter(FSMLifestyle.readiness_to_change))
async def process_fill_readiness_to_change(callback: CallbackQuery, support_chats, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(readiness_to_change=callback.data)
    user_info = await state.get_data()
    await state.clear()

    user: UserData = users_db[callback.from_user.id]
    bot_name = await callback.bot.get_me()

    user.lifestyle.is_fill = True

    for field_name in user_info:
        setattr(user.lifestyle, field_name, user_info[field_name])

    for chat_id in support_chats:
        await callback.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['filled_lifestyle'].format(
                bot_name=bot_name.username,
                meals_per_day=LEXICON[user.lifestyle.meals_per_day],
                breakfast_time=user.lifestyle.breakfast_time,
                heaviest_meal=LEXICON[user.lifestyle.heaviest_meal],
                cooking_attitude=LEXICON[user.lifestyle.cooking_attitude],
                snacks_frequency=LEXICON[user.lifestyle.snacks_frequency],
                frequent_foods=user.lifestyle.frequent_foods,
                daily_drinks=user.lifestyle.daily_drinks,
                food_intolerance=LEXICON[user.lifestyle.food_intolerance],
                eating_features=LEXICON[user.lifestyle.eating_features],
                past_diets=LEXICON[user.lifestyle.past_diets],
                supplements=LEXICON[user.lifestyle.supplements],
                readiness_to_change=LEXICON[user.lifestyle.readiness_to_change]
            )
        )
    await callback.message.answer(text=LEXICON['lifestyle_thanks'])
    await save_users_db(users_db)

@router.message(StateFilter(FSMLifestyle.breakfast_time))
@router.message(StateFilter(FSMLifestyle.frequent_foods))
@router.message(StateFilter(FSMLifestyle.daily_drinks))
@router.message(StateFilter(FSMLifestyle.food_intolerance_details))
@router.message(StateFilter(FSMLifestyle.eating_features_details))
async def process_too_short_message(message: Message):
    await message.answer(text=LEXICON['not_so_short'])


@router.message(StateFilter(FSMLifestyle.meals_per_day))
@router.message(StateFilter(FSMLifestyle.breakfast_time))
@router.message(StateFilter(FSMLifestyle.heaviest_meal))
@router.message(StateFilter(FSMLifestyle.cooking_attitude))
async def warning_not_children(message: Message):
    await message.answer(text=LEXICON['not_button'])
