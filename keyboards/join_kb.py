from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON


def create_join_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button],
        callback_data=button) for button in buttons])
    kb_builder.adjust(1)
    return kb_builder.as_markup()
