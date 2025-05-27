from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON


def create_join_keyboard(*buttons: str, row_width: int = 1) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button],
        callback_data=button) for button in buttons])
    kb_builder.adjust(row_width)
    return kb_builder.as_markup()
