import json
from pathlib import Path

DB_PATH = Path("database/users_db.json")


async def save_users_db(users_db: dict[int, dict[str, str | bool]]) -> None:
    """Сохраняет users_db в JSON-файл"""
    serializable_db = {
        str(user_id): user_data for user_id, user_data in users_db.items()
    }

    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(serializable_db, f, ensure_ascii=False, indent=4)


def load_users_db() -> dict[int, dict[str, str | bool]]:
    """Загружает users_db из JSON-файла"""
    if not DB_PATH.exists() or DB_PATH.stat().st_size == 0:
        return {}

    with DB_PATH.open("r", encoding="utf-8") as f:
        raw_data: dict[str, dict[str, str | bool]] = json.load(f)

    deserialized_db = {
        int(user_id): inner for user_id, inner in raw_data.items()
    }

    return deserialized_db
