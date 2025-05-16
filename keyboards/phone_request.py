from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_phone_request():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Поделиться номером", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
