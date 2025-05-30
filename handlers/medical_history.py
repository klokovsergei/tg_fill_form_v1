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


@router.callback_query(StateFilter(FSMMedicalHistory.probiotics_tolerance))
async def process_fill_probiotics_tolerance(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(probiotics_tolerance=callback.data)
    if callback.data == 'button_bad_tolerance':
        await callback.message.answer(text=LEXICON['probiotics_tolerance_details'])
        await state.set_state(FSMMedicalHistory.probiotics_tolerance_details)
    else:
        await state.update_data(probiotics_tolerance_details='')
        await callback.message.answer(
            text=LEXICON['stool_problems'],
            reply_markup=create_join_keyboard(
                'button_stool_none',
                'button_stool_constipation',
                'button_stool_diarrhea',
                'button_stool_mixed',
                row_width=2
            ))
        await state.set_state(FSMMedicalHistory.stool_problems)


@router.message(
    StateFilter(FSMMedicalHistory.probiotics_tolerance_details),
    F.text.len() > 5)
async def process_fill_probiotics_tolerance_details(message: Message, state: FSMContext):
    await state.update_data(probiotics_tolerance_details=message.text.strip())
    await message.answer(
        text=LEXICON['stool_problems'],
        reply_markup=create_join_keyboard(
            'button_stool_none',
            'button_stool_constipation',
            'button_stool_diarrhea',
            'button_stool_mixed',
            row_width=2
        ))
    await state.set_state(FSMMedicalHistory.stool_problems)


@router.callback_query(StateFilter(FSMMedicalHistory.stool_problems))
async def process_fill_stool_problems(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(stool_problems=callback.data)
    await callback.message.answer(
        text=LEXICON['heartburn_frequency'],
        reply_markup=create_join_keyboard(
        'never', 'rarely', 'often'
        ))
    await state.set_state(FSMMedicalHistory.heartburn_frequency)


@router.callback_query(StateFilter(FSMMedicalHistory.heartburn_frequency))
async def process_fill_heartburn_frequency(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(heartburn_frequency=callback.data)
    if callback.data == 'never':
        await state.update_data(heartburn_details='')
        await callback.message.answer(
            text=LEXICON['current_complaints'],
            reply_markup=create_join_keyboard(
                'yes_button', 'no_button'
            ))
        await state.set_state(FSMMedicalHistory.current_complaints)
    else:
        await callback.message.answer(text=LEXICON['heartburn_details'])
        await state.set_state(FSMMedicalHistory.heartburn_details)


@router.message(
    StateFilter(FSMMedicalHistory.heartburn_details),
    F.text.len() > 5)
async def process_fill_heartburn_details(message: Message, state: FSMContext):
    await state.update_data(heartburn_details=message.text.strip())
    await message.answer(
        text=LEXICON['current_complaints'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button'
        ))
    await state.set_state(FSMMedicalHistory.current_complaints)


@router.callback_query(StateFilter(FSMMedicalHistory.current_complaints))
async def process_fill_current_complaints(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(current_complaints=callback.data)
    if callback.data == 'yes_button':
        await callback.message.answer(text=LEXICON['current_complaints_details'])
        await state.set_state(FSMMedicalHistory.current_complaints_details)
    else:
        await state.update_data(current_complaints_details='')
        await callback.message.answer(
            text=LEXICON['serious_issues'],
            reply_markup=create_join_keyboard(
                'yes_button', 'no_button'
            ))
        await state.set_state(FSMMedicalHistory.serious_issues)


@router.message(
    StateFilter(FSMMedicalHistory.current_complaints_details),
    F.text.len() > 5)
async def process_fill_current_complaints_details(message: Message, state: FSMContext):
    await state.update_data(current_complaints_details=message.text.strip())
    await message.answer(
        text=LEXICON['serious_issues'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button'
        ))
    await state.set_state(FSMMedicalHistory.serious_issues)


@router.callback_query(StateFilter(FSMMedicalHistory.serious_issues))
async def process_fill_serious_issues(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    user: UserData = users_db[callback.from_user.id]

    await state.update_data(serious_issues=callback.data)
    if callback.data == 'no_button':
        await state.update_data(serious_issues_details='')
        if user.user_join.gender == 'female':
            await callback.message.answer(
                text=LEXICON['menstrual_issues'],
                reply_markup=create_join_keyboard(
                    'yes_button', 'no_button'
                ))
            await state.set_state(FSMMedicalHistory.menstrual_issues)
        else:
            await state.update_data(menstrual_issues='not_applicable')
            await state.update_data(menstrual_issues_details='')

            await callback.message.answer(text=LEXICON['family_diseases'])
            await state.set_state(FSMMedicalHistory.family_diseases)

        await callback.message.answer(text=LEXICON['current_complaints_details'])
        await state.set_state(FSMMedicalHistory.current_complaints_details)
    else:
        await callback.message.answer(text=LEXICON['serious_issues_details'])
        await state.set_state(FSMMedicalHistory.serious_issues_details)


@router.message(
    StateFilter(FSMMedicalHistory.serious_issues_details),
    F.text.len() > 5)
async def process_fill_serious_issues_details(message: Message, state: FSMContext):
    await state.update_data(serious_issues_details=message.text.strip())

    user: UserData = users_db[message.from_user.id]

    if user.user_join.gender == 'female':
        await message.answer(
            text=LEXICON['menstrual_issues'],
            reply_markup=create_join_keyboard(
                'yes_button', 'no_button'
            ))
        await state.set_state(FSMMedicalHistory.menstrual_issues)
    else:
        await state.update_data(menstrual_issues='not_applicable')
        await state.update_data(menstrual_issues_details='')

        await message.answer(text=LEXICON['family_diseases'])
        await state.set_state(FSMMedicalHistory.family_diseases)


@router.callback_query(StateFilter(FSMMedicalHistory.menstrual_issues))
async def process_fill_menstrual_issues(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await state.update_data(menstrual_issues=callback.data)
    if callback.data == 'no_button':
        await state.update_data(menstrual_issues_details='')
        await callback.message.answer(text=LEXICON['family_diseases'])
        await state.set_state(FSMMedicalHistory.family_diseases)
    else:
        await callback.message.answer(text=LEXICON['menstrual_issues_details'])
        await state.set_state(FSMMedicalHistory.menstrual_issues_details)


@router.message(
    StateFilter(FSMMedicalHistory.menstrual_issues_details),
    F.text.len() > 5)
async def process_fill_menstrual_issues_details(message: Message, state: FSMContext):
    await state.update_data(menstrual_issues_details=message.text.strip())
    await message.answer(text=LEXICON['family_diseases'])
    await state.set_state(FSMMedicalHistory.family_diseases)


@router.message(
    StateFilter(FSMMedicalHistory.family_diseases),
    F.text.len() > 5)
async def process_fill_family_diseases(message: Message, state: FSMContext):
    await state.update_data(family_diseases=message.text.strip())
    await message.answer(text=LEXICON['family_alive'])
    await state.set_state(FSMMedicalHistory.family_alive)


@router.message(
    StateFilter(FSMMedicalHistory.family_alive),
    F.text.len() > 5)
async def process_fill_family_diseases(message: Message, state: FSMContext, support_chats):
    await state.update_data(family_alive=message.text.strip())
    user_info = await state.get_data()
    await state.clear()

    user: UserData = users_db[message.from_user.id]
    bot_name = await message.bot.get_me()

    user.medical_history.is_fill = True


    for field_name in user_info:
        setattr(user.medical_history, field_name, user_info[field_name])

    for chat_id in support_chats:
        await message.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['filled_medical_history'].format(
                bot_name=bot_name.username,
                diagnosis=user.medical_history.diagnosis,
                surgeries=LEXICON[user.medical_history.surgeries],
                surgeries_details=user.medical_history.surgeries_details,
                past_medications=user.medical_history.past_medications,
                current_medications=user.medical_history.current_medications,
                allergies=LEXICON[user.medical_history.allergies],
                allergies_details=user.medical_history.allergies_details,
                probiotics_tolerance=LEXICON[user.medical_history.probiotics_tolerance],
                probiotics_tolerance_details=user.medical_history.probiotics_tolerance_details,
                stool_problems=LEXICON[user.medical_history.stool_problems],
                heartburn_frequency=LEXICON[user.medical_history.heartburn_frequency],
                heartburn_details=user.medical_history.heartburn_details,
                current_complaints=LEXICON[user.medical_history.current_complaints],
                current_complaints_details=user.medical_history.current_complaints_details,
                serious_issues=LEXICON[user.medical_history.serious_issues],
                serious_issues_details=user.medical_history.serious_issues_details,
                menstrual_issues=LEXICON[user.medical_history.menstrual_issues],
                menstrual_issues_details=user.medical_history.menstrual_issues_details,
                family_diseases=user.medical_history.family_diseases,
                family_alive=user.medical_history.family_alive

            )
        )
    await message.answer(text=LEXICON['medical_history_thanks'])
    await save_users_db(users_db)


@router.message(StateFilter(FSMMedicalHistory.diagnosis))
@router.message(StateFilter(FSMMedicalHistory.surgeries_details))
@router.message(StateFilter(FSMMedicalHistory.past_medications))
@router.message(StateFilter(FSMMedicalHistory.current_medications))
@router.message(StateFilter(FSMMedicalHistory.allergies_details))
@router.message(StateFilter(FSMMedicalHistory.probiotics_tolerance_details))
@router.message(StateFilter(FSMMedicalHistory.heartburn_details))
@router.message(StateFilter(FSMMedicalHistory.current_complaints_details))
@router.message(StateFilter(FSMMedicalHistory.serious_issues_details))
@router.message(StateFilter(FSMMedicalHistory.menstrual_issues_details))
@router.message(StateFilter(FSMMedicalHistory.family_diseases))
@router.message(StateFilter(FSMMedicalHistory.family_alive))
async def process_too_short_message(message: Message):
    await message.answer(text=LEXICON['not_so_short'])


@router.message(StateFilter(FSMMedicalHistory.surgeries))
@router.message(StateFilter(FSMMedicalHistory.allergies))
@router.message(StateFilter(FSMMedicalHistory.probiotics_tolerance))
@router.message(StateFilter(FSMMedicalHistory.stool_problems))
@router.message(StateFilter(FSMMedicalHistory.heartburn_frequency))
@router.message(StateFilter(FSMMedicalHistory.menstrual_issues))
async def warning_not_children(message: Message):
    await message.answer(text=LEXICON['not_button'])
