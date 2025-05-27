from models.user_data import UserData
from services.storage_user_data import load_users_db

# Инициализируем "базу данных"
users_db: dict[int, UserData] = load_users_db()
