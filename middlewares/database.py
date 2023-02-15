import time
import aioredis

import asyncpg

from aiogram import types
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from utils.cache import Cache
from utils.db_api.database import DataBase
from utils.db_cache import DataBaseCache

class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "channel_post"]

    def __init__(
            self,
            redis: aioredis.Redis,
            pool: asyncpg.Pool,
            database: DataBase,
            cache: Cache

    ):
        super().__init__()
        self.cache = Cache(redis)
        self.db = DataBase(pool,redis)
        self.db_cache = DataBaseCache(database,cache)



    async def pre_process(self, obj, data, *args):
        data['cache'] = self.cache
        data['db'] = self.db
        data['db_cache'] = self.db_cache
        if isinstance(obj, types.Message) and '_steps' in obj.conf:
            obj.conf['_steps'].append(('added conns', time.monotonic(), time.monotonic() - obj.conf['_steps'][-1][1]))

    async def post_process(self, obj, data, *args):
        pass
