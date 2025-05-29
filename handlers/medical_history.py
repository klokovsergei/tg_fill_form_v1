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
from states.medical_history import FSMMedicalHistory

router = Router()


@router.callback_query(F.data == 'medical_history', StateFilter(default_state))
async def process_start_fill_medical_history(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(text=LEXICON['diagnosis'])
    await state.set_state(FSMMedicalHistory.diagnosis)


@router.message(
    StateFilter(FSMMedicalHistory.diagnosis),
    F.text.len() > 5)
async def process_fill_diagnosis(message: Message, state: FSMContext):
    await state.update_data(diagnosis=message.text.strip())
    await message.answer(
        text=LEXICON['surgeries'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button', row_width=2
        ))
    await state.set_state(FSMMedicalHistory.surgeries)


@router.callback_query(StateFilter(FSMMedicalHistory.surgeries))
async def process_fill_surgeries(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(surgeries=callback.data)
    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['surgeries_details'])
        await state.set_state(FSMMedicalHistory.surgeries_details)
        return
    else:
        await state.update_data(surgeries_details='')
        await callback.message.answer(text=LEXICON['past_medications'])
        await state.set_state(FSMMedicalHistory.past_medications)


@router.message(
    StateFilter(FSMMedicalHistory.surgeries_details),
    F.text.len() > 5)
async def process_fill_surgeries_details(message: Message, state: FSMContext):
    await state.update_data(surgeries_details=message.text.strip())
    await message.answer(text=LEXICON['past_medications'])
    await state.set_state(FSMMedicalHistory.past_medications)


@router.message(
    StateFilter(FSMMedicalHistory.past_medications),
    F.text.len() > 2)
async def process_fill_past_medications(message: Message, state: FSMContext):
    await state.update_data(past_medications=message.text.strip())
    await message.answer(text=LEXICON['current_medications'])
    await state.set_state(FSMMedicalHistory.current_medications)


@router.message(
    StateFilter(FSMMedicalHistory.current_medications),
    F.text.len() > 2)
async def process_fill_current_medications(message: Message, state: FSMContext):
    await state.update_data(current_medications=message.text.strip())
    await message.answer(
        text=LEXICON['allergies'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button', row_width=2
        ))
    await state.set_state(FSMMedicalHistory.allergies)


@router.callback_query(StateFilter(FSMMedicalHistory.allergies))
async def process_fill_allergies(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(allergies=callback.data)
    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['allergies_details'])
        await state.set_state(FSMMedicalHistory.allergies_details)
    else:
        await state.update_data(allergies_details='')
        await callback.message.answer(
            text=LEXICON['probiotics_tolerance'],
            reply_markup=create_join_keyboard(
                'button_good_tolerance',
                'button_neutral_tolerance',
                'button_bad_tolerance',
                row_width=3
            ))
        await state.set_state(FSMMedicalHistory.probiotics_tolerance)


@router.message(
    StateFilter(FSMMedicalHistory.allergies_details),
    F.text.len() > 5)
async def process_fill_allergies_details(message: Message, state: FSMContext):
    await state.update_data(allergies_details=message.text.strip())
    await message.answer(
        text=LEXICON['probiotics_tolerance'],
        reply_markup=create_join_keyboard(
            'button_good_tolerance',
            'button_neutral_tolerance',
            'button_bad_tolerance',
            row_width=3
        ))
    await state.set_state(FSMMedicalHistory.probiotics_tolerance)


#####
#####

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


@router.message(StateFilter(FSMMedicalHistory.diagnosis))
@router.message(StateFilter(FSMMedicalHistory.surgeries_details))
@router.message(StateFilter(FSMMedicalHistory.past_medications))
@router.message(StateFilter(FSMMedicalHistory.current_medications))
@router.message(StateFilter(FSMMedicalHistory.allergies_details))
async def process_too_short_message(message: Message):
    await message.answer(text=LEXICON['not_so_short'])


@router.message(StateFilter(FSMMedicalHistory.surgeries))
@router.message(StateFilter(FSMMedicalHistory.allergies))
@router.message(StateFilter(FSMMedicalHistory.probiotics_tolerance))
async def warning_not_children(message: Message):
    await message.answer(text=LEXICON['not_button'])
