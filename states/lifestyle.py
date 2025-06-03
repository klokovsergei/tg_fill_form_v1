from aiogram.fsm.state import State, StatesGroup


class FSMLifestyle(StatesGroup):
    meals_per_day = State()  # Сколько приёмов пищи в день?
    breakfast_time = State()  # Во сколько обычно завтракаете?
    heaviest_meal = State()  # Какой приём пищи самый обильный?
    cooking_attitude = State()  # Как относитесь к приготовлению еды?
    snacks_frequency = State()  # Как часто перекусываете?
    frequent_foods = State()  # Какие продукты едите чаще всего?
    daily_drinks = State()  # Какие напитки пьёте ежедневно?
    food_intolerance = State()  # Пищевая непереносимость или аллергии?
    food_intolerance_details = State()  # комментарий по непереносимым продуктам
    eating_features = State()  # Особенности питания?
    eating_features_details = State()  # комментарий по особенностям питания
    past_diets = State()  # Были ли жёсткие диеты или голодовки?
    past_diets_details = State()  # комментарий по диетам
    supplements = State()  # Принимаете ли БАДы, витамины, ферменты?
    supplements_details = State()  # комментарий по добавкам
    readiness_to_change = State()  # Насколько готовы менять рацион?
