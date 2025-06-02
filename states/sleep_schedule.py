from aiogram.fsm.state import StatesGroup, State


class FSMSleepSchedule(StatesGroup):
    sleep_time = State()  # Во сколько ложитесь и встаёте
    fall_asleep_speed = State()  # Как быстро засыпаете
    night_awakenings = State()  # Часто ли просыпаетесь ночью
    morning_feeling = State()  # Чувствуете ли себя отдохнувшим по утрам
    daytime_sleepiness = State()  # Есть ли дневная сонливость
