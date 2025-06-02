from aiogram.fsm.state import State, StatesGroup

class FSMHabits(StatesGroup):
    smoking = State() # Курите ли вы?
    smoking_details = State()  # детали курения
    alcohol = State()          # Употребляете ли алкоголь?
    alcohol_details = State()  # детали употребления алкоголя
    other_habits = State()     # Другие привычки