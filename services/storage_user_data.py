import json
from datetime import datetime
from typing import Any
from dataclasses import asdict, is_dataclass
from dacite import from_dict, Config
from pathlib import Path

from models.user_data import UserData

DB_PATH = Path('database/users_db.json')

def _serialize_dataclass(obj: Any) -> Any:
    if is_dataclass(obj):
        return {k: _serialize_dataclass(v) for k, v in asdict(obj).items()}
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: _serialize_dataclass(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_serialize_dataclass(i) for i in obj]
    else:
        return obj


def _deserialize_user_data(data: dict[str, Any]) -> UserData:
    config = Config(type_hooks={datetime: datetime.fromisoformat})
    return from_dict(data_class=UserData, data=data, config=config)


async def save_users_db(users_db: dict[int, UserData], filepath: str = DB_PATH) -> None:
    serializable_data = {
        str(user_id): _serialize_dataclass(user_data)
        for user_id, user_data in users_db.items()
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(serializable_data, f, ensure_ascii=False, indent=2)


def load_users_db(filepath: str = DB_PATH) -> dict[int, UserData]:
    if not DB_PATH.exists() or DB_PATH.stat().st_size == 0:
        return {}

    with open(filepath, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    return {
        int(user_id): _deserialize_user_data(user_data)
        for user_id, user_data in raw_data.items()
    }
