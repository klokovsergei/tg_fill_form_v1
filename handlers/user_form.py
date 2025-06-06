import re
from datetime import datetime, date

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from database.database import users_db
from database.media_db import MEDIA
from filters.custom_filters import IsDateFormat, IsEmailOrSkip, CityNameFilter
from keyboards.join_kb import create_join_keyboard
from keyboards.phone_request import create_phone_request
from models.user_data import UserData
from services.storage_user_data import save_users_db
from states.user_form import FSMUserForm

from lexicon.lexicon import LEXICON

router = Router()


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text=LEXICON['cancel_no'])


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['cancel_state'],
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(Command(commands='join'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    user: UserData = users_db[message.from_user.id]
    if user.is_join:
        await message.answer(
            text=LEXICON['already_joined'],
            reply_markup=create_join_keyboard(
                'firstname', 'lastname', 'phone', 'birthday', 'email', 'cancel_button'
            ))
        await state.set_state(FSMUserForm.edit_user_form)
    else:
        await message.answer(text=LEXICON['fill_firstname'])
        await state.set_state(FSMUserForm.fill_firstname)


@router.callback_query(F.data == 'join', StateFilter(default_state))
async def process_fillform_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.message.answer(text=LEXICON['fill_firstname'])
    await state.set_state(FSMUserForm.fill_firstname)


@router.message(StateFilter(FSMUserForm.fill_firstname), F.text.isalpha())
async def process_name_send(message: Message, state: FSMContext):
    await state.update_data(firstname=message.text.strip())
    await message.answer(text=LEXICON['fill_lastname'])
    await state.set_state(FSMUserForm.fill_lastname)


@router.message(StateFilter(FSMUserForm.fill_lastname), F.text.isalpha())
async def process_lastname_send(message: Message, state: FSMContext):
    await state.update_data(lastname=message.text.strip())
    await message.answer(
        text=LEXICON['fill_gender'],
        reply_markup=create_join_keyboard(
            'male', 'female'
        ))
    await state.set_state(FSMUserForm.fill_gender)


@router.message(StateFilter(FSMUserForm.fill_firstname))
@router.message(StateFilter(FSMUserForm.fill_lastname))
async def warning_not_name(message: Message):
    await message.answer(text=LEXICON['not_name'])


@router.callback_query(StateFilter(FSMUserForm.fill_gender))
async def process_gender_send(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(gender=callback.data)

    await callback.message.answer(text=LEXICON['fill_birthday'])
    await state.set_state(FSMUserForm.fill_birthday)


@router.message(StateFilter(FSMUserForm.fill_birthday), IsDateFormat())
async def process_birthday_send(message: Message, state: FSMContext):
    day = re.sub(r'[,\-/]', '.', message.text.strip())

    await state.update_data(birthday=day)
    await message.answer(text=LEXICON['fill_city'])
    await state.set_state(FSMUserForm.fill_city)


@router.message(StateFilter(FSMUserForm.fill_birthday))
async def warning_not_birthday(message: Message):
    await message.answer(text=LEXICON['not_date'])


@router.message(StateFilter(FSMUserForm.fill_city), CityNameFilter())
async def process_city_send(message: Message, state: FSMContext):
    await state.update_data(city=message.text.strip())
    await message.answer(text=LEXICON['fill_email'])
    await state.set_state(FSMUserForm.fill_email)


@router.message(StateFilter(FSMUserForm.fill_city))
async def warning_not_city(message: Message):
    await message.answer(text=LEXICON['not_city'])


@router.message(StateFilter(FSMUserForm.fill_email), IsEmailOrSkip())
async def process_email_send(message: Message, state: FSMContext):
    await state.update_data(email=message.text.strip())

    await message.answer_photo(
        photo=MEDIA['share_phone_instruction'],
        caption=LEXICON['fill_phone'],
        reply_markup=create_phone_request()
    )
    await state.set_state(FSMUserForm.fill_phone)


@router.message(StateFilter(FSMUserForm.fill_email))
async def warning_not_email(message: Message):
    await message.answer(text=LEXICON['not_email'])


@router.message(F.contact, StateFilter(FSMUserForm.fill_phone))
async def process_phone_send(message: Message, state: FSMContext):
    if message.contact.user_id != message.from_user.id:
        await message.answer(text=LEXICON['not_your_number'])
        return

    await state.update_data(phone=message.contact.phone_number)
    await message.answer(text=LEXICON['thanks_number'],
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(
        text=LEXICON['is_notification'],
        reply_markup=create_join_keyboard(
            'yes_button', 'no_button',
            row_width=2
        ))
    await state.set_state(FSMUserForm.fill_notifications)


@router.message(StateFilter(FSMUserForm.fill_phone))
async def warning_not_phone(message: Message):
    await message.answer(text=LEXICON['not_phone'])


@router.callback_query(StateFilter(FSMUserForm.fill_notifications))
async def process_subscribe_notification(callback: CallbackQuery, support_chats, state: FSMContext):
    await state.update_data(notification=(callback.data == 'yes_button'))
    user_info = await state.get_data()
    await state.clear()

    user: UserData = users_db[callback.from_user.id]
    bot_name = await callback.bot.get_me()

    user.is_join = True
    user.user_join.time_join = datetime.now()
    user.user_join.birthday = datetime.strptime(user_info.pop('birthday'), '%d.%m.%Y')

    for field_name in user_info:
        setattr(user.user_join, field_name, user_info[field_name])

    today = date.today()
    birthday = user.user_join.birthday
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    for chat_id in support_chats:
        await callback.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['new_join_up'].format(
                bot_name=bot_name.username,
                firstname=user.user_join.firstname,
                lastname=user.user_join.lastname,
                username=user.user_join.username,
                gender=user.user_join.gender,
                birthday=user.user_join.birthday.strftime('%d.%m.%Y'),
                age=age,
                city=user.user_join.city,
                email=user.user_join.email,
                phone=user.user_join.phone,
                time_start=user.user_join.time_start.strftime('%d.%m.%Y %H:%M:%S'),
                time_join=user.user_join.time_join.strftime('%d.%m.%Y %H:%M:%S'),
            )
        )

    await callback.message.edit_text(text=LEXICON['join_compliant'], reply_markup=None)
    await save_users_db(users_db)


@router.message(StateFilter(FSMUserForm.fill_notifications))
@router.message(StateFilter(FSMUserForm.fill_gender))
async def warning_not_notifications(message: Message):
    await message.answer(text=LEXICON['not_button'])
