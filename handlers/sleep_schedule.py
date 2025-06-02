from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.callback_answer import CallbackAnswer

from database.database import users_db
from keyboards.join_kb import create_join_keyboard
from models.user_data import UserData
from services.storage_user_data import save_users_db

from lexicon.lexicon import LEXICON
from states.medical_history import FSMMedicalHistory
from states.sleep_schedule import FSMSleepSchedule

router = Router()


@router.callback_query(F.data == 'sleep_schedule', StateFilter(default_state))
async def process_start_fill_sleep_schedule(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(text=LEXICON['sleep_time'])
    await state.set_state(FSMSleepSchedule.sleep_time)


@router.message(
    StateFilter(FSMSleepSchedule.sleep_time),
    F.text.len() > 5)
async def process_fill_sleep_time(message: Message, state: FSMContext):
    await state.update_data(sleep_time=message.text.strip())
    await message.answer(
        text=LEXICON['fall_asleep_speed'],
        reply_markup=create_join_keyboard(
            'button_sleep_easy', 'button_sleep_medium', 'button_sleep_hard',
            row_width=3
        ))
    await state.set_state(FSMSleepSchedule.fall_asleep_speed)


@router.callback_query(StateFilter(FSMSleepSchedule.fall_asleep_speed))
async def process_fill_fall_asleep_speed(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(fall_asleep_speed=callback.data)
    await callback.message.answer(
        text=LEXICON['night_awakenings']
        , reply_markup=create_join_keyboard(
            'never', 'rarely', 'often',
            row_width=3
        ))
    await state.set_state(FSMSleepSchedule.night_awakenings)


@router.callback_query(StateFilter(FSMSleepSchedule.night_awakenings))
async def process_fill_night_awakenings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(night_awakenings=callback.data)
    await callback.message.answer(
        text=LEXICON['morning_feeling']
        , reply_markup=create_join_keyboard(
            'yes_button', 'rarely', 'no_button',
            row_width=3
        ))
    await state.set_state(FSMSleepSchedule.morning_feeling)


@router.callback_query(StateFilter(FSMSleepSchedule.morning_feeling))
async def process_fill_morning_feeling(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(morning_feeling=callback.data)
    await callback.message.answer(
        text=LEXICON['daytime_sleepiness']
        , reply_markup=create_join_keyboard(
            'never', 'rarely', 'often',
            row_width=3
        ))
    await state.set_state(FSMSleepSchedule.daytime_sleepiness)


@router.callback_query(StateFilter(FSMSleepSchedule.daytime_sleepiness))
async def process_fill_daytime_sleepiness(callback: CallbackQuery, state: FSMContext, support_chats):
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(daytime_sleepiness=callback.data)
    user_info = await state.get_data()
    await state.clear()

    user: UserData = users_db[callback.from_user.id]
    bot_name = await callback.bot.get_me()

    user.sleep_schedule.is_fill = True

    for field_name in user_info:
        setattr(user.sleep_schedule, field_name, user_info[field_name])

    for chat_id in support_chats:
        await callback.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['filled_sleep_schedule'].format(
                bot_name=bot_name.username,
                sleep_time=user.sleep_schedule.sleep_time,
                fall_asleep_speed=LEXICON[user.sleep_schedule.fall_asleep_speed],
                night_awakenings=LEXICON[user.sleep_schedule.night_awakenings],
                morning_feeling=LEXICON[user.sleep_schedule.morning_feeling],
                daytime_sleepiness=LEXICON[user.sleep_schedule.daytime_sleepiness]
            ))
    await callback.message.answer(text=LEXICON['sleep_schedule_thanks'])
    await save_users_db(users_db)


@router.message(StateFilter(FSMSleepSchedule.sleep_time))
async def process_too_short_message(message: Message):
    await message.answer(text=LEXICON['not_so_short'])


@router.message(StateFilter(FSMSleepSchedule.fall_asleep_speed))
@router.message(StateFilter(FSMSleepSchedule.night_awakenings))
@router.message(StateFilter(FSMSleepSchedule.morning_feeling))
@router.message(StateFilter(FSMSleepSchedule.daytime_sleepiness))
async def warning_not_children(message: Message):
    await message.answer(text=LEXICON['not_button'])
