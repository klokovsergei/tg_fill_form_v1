from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    support_channel_ids: list[int]


@dataclass
class RedisConfig:
    host: str
    port: int
    db: int = 0


@dataclass
class Config:
    tg_bot: TgBot
    redis: RedisConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS'))),
            support_channel_ids=list(map(int, env.list('SUPPORT_CHAT_ID')))
        ),
        redis=RedisConfig(
            host=env('REDIS_HOST', 'localhost'),
            port=env.int('REDIS_PORT', 6379),
            db=env.int('REDIS_DB', 0)
        )
    )
