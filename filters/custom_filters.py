import re
from datetime import datetime

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsDateFormat(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        date = re.sub(r'[,\-/]', '.', message.text.strip())
        date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])[.\-/\,](0?[1-9]|1[0-2])[.\-/\,](\d{4})$'
        if re.match(date_pattern, date):
            try:

                datetime.strptime(date, '%d.%m.%Y')
                return True
            except ValueError:
                return False
        return False


class IsEmailOrSkip(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        text = message.text.strip()
        if text == '*':
            return True
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(email_pattern, text))


class CityNameFilter(BaseFilter):
    def __init__(self):
        self.pattern = re.compile(r'^[A-Za-zА-Яа-яЁё\s\-.]+$' , re.UNICODE)

    async def __call__(self, message: Message) -> bool:
        city = message.text.strip()
        return bool(self.pattern.fullmatch(city))