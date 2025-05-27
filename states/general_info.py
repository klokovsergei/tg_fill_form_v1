from aiogram.fsm.state import StatesGroup, State


class FSMGeneralInfo(StatesGroup):
    children = State()  # Есть ли дети?
    children_info = State() # Если есть, информация о детях
    childhood_health = State()  # Как проходило детство в плане здоровья
    employment_type = State()  # Тип занятости
    stress_level = State()  # Уровень стресса (от 1 до 10)
    mood_swings = State()  # Перепады настроения
    anxiety = State()  # Тревожность
    apathy = State()  # Апатия
    physical_activity = State()  # Уровень физической активности
    physical_activity_comment = State() # Комментарий к физической активности
