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

router = Router()


@router.callback_query(F.data == 'habits', StateFilter(default_state))
async def process_start_fill_smoking(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(
        text=LEXICON['smoking'],
        reply_markup=create_join_keyboard(
            'no_button', 'rarely', 'regularly',
            row_width=3
        ))
    await state.set_state(FSMHabits.smoking)


@router.callback_query(F.data == 'yes_habits')
async def process_start_fill_general_info(callback: CallbackQuery):
    await callback.answer(text=LEXICON['habits_yes'])


@router.callback_query(StateFilter(FSMHabits.smoking))
async def process_fill_smoking(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(smoking=callback.data)

    if callback.data == 'regularly':
        await callback.message.answer(text=LEXICON['smoking_details'])
        await state.set_state(FSMHabits.smoking_details)
    else:
        await state.update_data(smoking_details='')
        await callback.message.answer(
            text=LEXICON['alcohol'],
            reply_markup=create_join_keyboard(
                'no_button', 'rarely', 'sometimes', 'often',
                row_width=2
            ))
        await state.set_state(FSMHabits.alcohol)


@router.message(
    StateFilter(FSMHabits.smoking_details),
    F.text.len() > 5)
async def process_fill_smoking_details(message: Message, state: FSMContext):
    await state.update_data(smoking_details=message.text.strip())
    await message.answer(
        text=LEXICON['alcohol'],
        reply_markup=create_join_keyboard(
            'no_button', 'rarely', 'sometimes', 'often',
            row_width=2
        ))
    await state.set_state(FSMHabits.alcohol)


@router.callback_query(StateFilter(FSMHabits.alcohol))
async def process_fill_alcohol(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(alcohol=callback.data)
    if callback.data == 'often':
        await callback.message.answer(text=LEXICON['alcohol_details'])
        await state.set_state(FSMHabits.alcohol_details)
    else:
        await state.update_data(alcohol_details='')
        await callback.message.answer(text=LEXICON['other_habits'])
        await state.set_state(FSMHabits.other_habits)


@router.message(
    StateFilter(FSMHabits.alcohol_details),
    F.text.len() > 5)
async def process_fill_alcohol_details(message: Message, state: FSMContext):
    await state.update_data(alcohol_details=message.text.strip())
    await message.answer(text=LEXICON['other_habits'])
    await state.set_state(FSMHabits.other_habits)


@router.message(StateFilter(FSMHabits.other_habits),
                F.text.len() > 5)
async def process_fill_other_habits(message: Message, state: FSMContext, support_chats):
    await state.update_data(other_habits=message.text.strip())
    user_info = await state.get_data()
    await state.clear()

    user: UserData = users_db[message.from_user.id]
    bot_name = await message.bot.get_me()

    user.habits.is_fill = True

    for field_name in user_info:
        setattr(user.habits, field_name, user_info[field_name])

    for chat_id in support_chats:
        await message.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['filled_habits'].format(
                bot_name=bot_name.username,
                smoking=LEXICON[user.habits.smoking],
                smoking_details=user.habits.smoking_details,
                alcohol=LEXICON[user.habits.alcohol],
                alcohol_details=user.habits.alcohol_details,
                other_habits=user.habits.other_habits,

            ))
    await message.answer(text=LEXICON['habits_thanks'])
    await save_users_db(users_db)


@router.message(StateFilter(FSMHabits.smoking_details))
@router.message(StateFilter(FSMHabits.alcohol_details))
@router.message(StateFilter(FSMHabits.other_habits))
async def process_too_short_message(message: Message):
    await message.answer(text=LEXICON['not_so_short'])


@router.message(StateFilter(FSMHabits.smoking))
@router.message(StateFilter(FSMHabits.alcohol))
async def warning_not_children(message: Message):
    await message.answer(text=LEXICON['not_button'])
