import asyncio
import logging
from redis.asyncio import Redis

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from config_data.config import Config, load_config
from handlers import (command, user_form, other_handlers, general_info, medical_history,
                      sleep_schedule, habits, lifestyle)
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config('.env')

    redis = Redis(
        host=config.redis.host,  # адрес сервера Redis
        port=config.redis.port,  # порт (по умолчанию Redis использует 6379)
        db=config.redis.db  # номер базы данных (по умолчанию 0)
    )
    storage = RedisStorage(redis=redis)

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)
    dp['support_chats'] = config.tg_bot.support_channel_ids
    dp['admin_list'] = config.tg_bot.admin_ids

    await set_main_menu(bot)

    dp.include_router(user_form.router)
    dp.include_router(general_info.router)
    dp.include_router(medical_history.router)
    dp.include_router(sleep_schedule.router)
    dp.include_router(habits.router)
    dp.include_router(lifestyle.router)
    dp.include_router(command.router)
    dp.include_router(other_handlers.router)

    logger.info('Обнуляем очередь апдейтов')
    await bot.delete_webhook(drop_pending_updates=True)

    logger.info('Запускаем polling')

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
