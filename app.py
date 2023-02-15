import logging
from typing import List, Tuple
import aioredis
import asyncpg
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiohttp import web
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config


from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def create_pool(user: str, password: str, database: str, host: str):
    pool = await asyncpg.create_pool(
        user=user,
        password=password,
        database=database,
        host=host,
        max_size=25,
        max_inactive_connection_lifetime=15,
        port=5432
    )
    return pool


async def setup_logic(dp: Dispatcher):
    pool = await create_pool(
        user=config.PG_USER,
        password=config.PG_PASSWORD,
        database=config.PG_DATABASE,
        host=config.PG_HOST
    )
    dp['pool'] = pool
    redis_pool = aioredis.Redis(
        host=config.CACHE_REDIS_HOST,
        port=config.CACHE_REDIS_PORT,
        password=config.CACHE_REDIS_PASSWORD,
        db=6,
        max_connections=100,
        encoding='utf8',
    )
    dp['redis'] = redis_pool

    
    


    from utils.db_api.database import DataBase
    dp['database'] = DataBase(pool,redis_pool)
    from utils.cache import Cache
    dp['cache'] = Cache(redis_pool)

    import middlewares
    middlewares.register_middlewares(dp)
    import filters
    filters.register_filters(dp)
    import handlers
    handlers.users.register_handlers(dp)
    handlers.errors.register_handlers(dp)


async def on_startup(dispatcher: Dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    await setup_logic(dispatcher)
    # dp.middleware.setup(LoggingMiddleware())
    logging.getLogger('aiogram').setLevel(logging.WARNING)


async def on_startup_webhook(app: web.Application):
    await on_startup(app['dp'])


async def init_webhooks() -> web.Application:
    import web_handlers
    app = web.Application()
    subapps: List[Tuple[str, web.Application]] = [
        ('/tg/webhooks/', web_handlers.tg_updates_app),
    ]
    app['bot'] = dp.bot
    app['dp'] = dp
    for prefix, subapp in subapps:
        subapp['bot'] = dp.bot
        subapp['dp'] = dp
        app.add_subapp(prefix, subapp)
    app.on_startup.append(on_startup_webhook)
    return app


if __name__ == '__main__':

    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = RedisStorage2(
        host=config.FSM_REDIS_HOST, port=config.FSM_REDIS_PORT, password=config.FSM_REDIS_PASSWORD, pool_size=100,db=7
    )
    #storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    if config.WEBHOOK_USE:
        web.run_app(app=init_webhooks(), host='0.0.0.0', port=5013)
    else:
        executor.start_polling(dp, on_startup=on_startup, skip_updates=False)


