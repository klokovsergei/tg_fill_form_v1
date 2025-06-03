import asyncio
from datetime import datetime

from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.join_kb import create_join_keyboard
from lexicon.lexicon import LEXICON
from database.database import users_db, UserData
from services.buttons import get_buttons_auto
from services.storage_user_data import save_users_db

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, support_chats):
    user_id = message.from_user.id

    # if user_id in users_db and users_db[user_id]['is_alive']:
    #     await message.answer(LEXICON['/help'])
    #     return

    if user_id not in users_db:
        users_db[user_id] = UserData()

    bot_name = await message.bot.get_me()

    user: UserData = users_db[user_id]
    user.user_join.username = message.from_user.username
    user.user_join.time_start = datetime.now()
    user.user_join.is_alive = True

    for chat_id in support_chats:
        await message.bot.send_message(
            chat_id=chat_id,
            text=LEXICON['new_user'].format(
                bot_name=bot_name.username,
                username=user.user_join.username,
                user_id=user_id,
                time_join=user.user_join.time_start,
            )
        )
    await save_users_db(users_db)
    await message.answer(
        LEXICON[message.text],
        reply_markup=create_join_keyboard(
            'join', 'cancel_button'
        ))


@router.callback_query(F.data == 'cancel_button')
async def process_del_kb(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.clear()


@router.message(Command(commands='fill'))
async def process_fill_command(message: Message):
    user: UserData = users_db[message.from_user.id]
    if not user.is_join:
        await message.answer(LEXICON['not_join'])
        return

    # проверку какие блоки уже заполнены
    buttons = [
        'general_info'
        , 'medical_history'
        , 'lifestyle'
        , 'sleep_schedule'
        , 'habits'
        # , 'goals_docs'
        , 'cancel_button'
    ]

    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_join_keyboard(
            *get_buttons_auto(user, buttons)
        ))


@router.message(Command(commands='stop'))
async def process_stop_command(message: Message, admin_list, bot: Bot):
    if message.from_user.id not in admin_list:
        await message.answer(LEXICON['not_admin'])
        return
    await save_users_db(users_db)
    await message.answer(LEXICON[message.text])

    await bot.session.close()
    await asyncio.sleep(5)
    asyncio.get_event_loop().stop()
