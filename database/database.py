from models.user_data import UserData
from services.storage import load_users_db
from services.storage_user_data import load_users_db_v2

user_info: dict[str, str | bool] = {
    'firstname': ''
    , 'lastname': ''
    , 'gender': ''
    , 'username': ''
    , 'birthday': ''
    , 'email': ''
    , 'city': ''
    , 'is_form_filled': False
    , 'is_join': False
    , 'time_start': ''  # дата запуска бота
    , 'time_join': ''  # дата прохождения регистрации
    , 'is_alive': False
    , 'phone': ''
    , 'notification': False
}

# Инициализируем "базу данных"
users_db: dict[int, dict[str, str | bool]] = load_users_db()
users_db_v2: dict[int, UserData] = load_users_db_v2()
print(users_db_v2)
