from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from database.database import users_db
from keyboards.join_kb import create_join_keyboard
from models.user_data import UserData
from services.storage_user_data import save_users_db
from states.general_info import FSMGeneralInfo

from lexicon.lexicon import LEXICON

router = Router()


@router.callback_query(F.data == 'general_info', StateFilter(default_state))
async def process_start_fill_general_info(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(
        text=LEXICON['children'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button', row_width=2
        ))
    await state.set_state(FSMGeneralInfo.children)


@router.callback_query(StateFilter(FSMGeneralInfo.children))
async def process_fill_children(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(children=callback.data)
    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['children_info'])
        await state.set_state(FSMGeneralInfo.children_info)
        return
    else:
        await state.update_data(children_info='')
        await callback.message.answer(text=LEXICON['childhood_health'])
        await state.set_state(FSMGeneralInfo.childhood_health)


@router.message(StateFilter(FSMGeneralInfo.children_info))
async def process_fill_children_info(message: Message, state: FSMContext):
    await state.update_data(children_info=message.text.strip())
    await message.answer(text=LEXICON['childhood_health'])
    await state.set_state(FSMGeneralInfo.childhood_health)


@router.message(
    StateFilter(FSMGeneralInfo.childhood_health),
    F.text.len() > 5)
async def process_fill_children_health(message: Message, state: FSMContext):
    await state.update_data(childhood_health=message.text.strip())
    await message.answer(
        text=LEXICON['employment_type'],
        reply_markup=create_join_keyboard(
            'employment_sedentary', 'employment_active',
            'employment_mixed', 'employment_none'
        ))
    await state.set_state(FSMGeneralInfo.employment_type)


@router.callback_query(StateFilter(FSMGeneralInfo.employment_type))
async def process_fill_employment_type(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(employment_type=callback.data)
    await callback.message.answer(
        text=LEXICON['physical_activity'],
        reply_markup=create_join_keyboard(
            'button_low_activity', 'button_walk_5k',
            'button_irregular_sport', 'button_regular_training'
        ))

    await state.set_state(FSMGeneralInfo.physical_activity)


@router.callback_query(StateFilter(FSMGeneralInfo.physical_activity))
async def process_fill_physical_activity(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(physical_activity=callback.data)

    if callback.data == 'button_regular_training':
        await callback.message.answer(
            text=LEXICON['physical_activity_comment'])
        await state.set_state(FSMGeneralInfo.physical_activity_comment)
        return

    await state.update_data(physical_activity_comment='')
    await callback.message.answer(
        text=LEXICON['stress_level'])
    await state.set_state(FSMGeneralInfo.stress_level)


@router.message(
    StateFilter(FSMGeneralInfo.physical_activity_comment),
    F.text.len() > 5)
async def process_fill_physical_activity_comment(message: Message, state: FSMContext):
    await state.update_data(physical_activity_comment=message.text.strip())
    await message.answer(
        text=LEXICON['stress_level'],
        reply_markup=create_join_keyboard(
            *[f'button_{i}' for i in range(1, 11)], row_width=5
        ))
    await state.set_state(FSMGeneralInfo.stress_level)


@router.callback_query(StateFilter(FSMGeneralInfo.stress_level))
async def process_fill_stress_level(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(stress_level=callback.data.removeprefix('button_'))
    await callback.message.answer(
        text=LEXICON['mood_swings'],
        reply_markup=create_join_keyboard(
            'never', 'rarely', 'often',
            row_width=3
        ))
    await state.set_state(FSMGeneralInfo.mood_swings)


@router.callback_query(StateFilter(FSMGeneralInfo.mood_swings))
async def process_fill_mood_swings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(mood_swings=callback.data)
    await callback.message.answer(
        text=LEXICON['anxiety'],
        reply_markup=create_join_keyboard(
            'never', 'rarely', 'often',
            row_width=3
        ))
    await state.set_state(FSMGeneralInfo.anxiety)


@router.callback_query(StateFilter(FSMGeneralInfo.anxiety))
async def process_fill_anxiety(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(anxiety=callback.data)
    await callback.message.answer(
        text=LEXICON['apathy'],
        reply_markup=create_join_keyboard(
            'never', 'rarely', 'often',
            row_width=3
        ))
    await state.set_state(FSMGeneralInfo.apathy)


@router.callback_query(StateFilter(FSMGeneralInfo.apathy))
async def process_fill_apathy(callback: CallbackQuery, support_chats, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(apathy=callback.data)
    user_info = await state.get_data()
    await state.clear()

    user: UserData = users_db[callback.from_user.id]
    bot_name = await callback.bot.get_me()

    user.general_info.is_fill = True

    for field_name in user_info:
        setattr(user.general_info, field_name, user_info[field_name])

    for chat_id in support_chats:
        await callback.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['filled_general_info'].format(
                bot_name=bot_name.username,
                children=LEXICON[user.general_info.children],
                children_info_block=user.general_info.children_info,
                childhood_health=user.general_info.childhood_health,
                employment_type=LEXICON[user.general_info.employment_type],
                stress_level=user.general_info.stress_level,
                mood_swings=LEXICON[user.general_info.mood_swings],
                anxiety=LEXICON[user.general_info.anxiety],
                apathy=LEXICON[user.general_info.apathy],
                physical_activity=LEXICON[user.general_info.physical_activity],
                physical_activity_comment=user.general_info.physical_activity_comment,
            )
        )
    await callback.message.answer(text=LEXICON['general_info_thanks'])
    await save_users_db(users_db)


@router.message(StateFilter(FSMGeneralInfo.childhood_health))
async def process_too_short_message(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['not_so_short'])


@router.message(StateFilter(FSMGeneralInfo.children))
@router.message(StateFilter(FSMGeneralInfo.employment_type))
@router.message(StateFilter(FSMGeneralInfo.stress_level))
@router.message(StateFilter(FSMGeneralInfo.mood_swings))
@router.message(StateFilter(FSMGeneralInfo.anxiety))
@router.message(StateFilter(FSMGeneralInfo.apathy))
@router.message(StateFilter(FSMGeneralInfo.physical_activity))
async def warning_not_children(message: Message):
    await message.answer(text=LEXICON['not_button'])
