from aiogram.fsm.state import StatesGroup, State

class FSMUserForm(StatesGroup):
    fill_firstname = State()
    fill_lastname = State()
    fill_gender = State()
    fill_birthday = State()
    fill_city = State()
    fill_email = State()
    fill_phone = State()
    fill_notifications = State()
    edit_user_form = State()