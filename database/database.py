from services.storage import load_users_db

user_info: dict[str, str | bool] = {
    'firstname': ''
    , 'lastname': ''
    , 'gender': ''
    , 'username': ''
    , 'birthday': ''
    , 'email': ''
    , 'is_form_filled': False
    , 'is_join': False
    , 'time_start': '' # дата запуска бота
    , 'time_join': '' # дата прохождения регистрации
    , 'is_alive': False
    , 'phone': ''
    , 'notification': False
}

# Инициализируем "базу данных"
users_db: dict[int, dict[str, str | bool]] = load_users_db()
