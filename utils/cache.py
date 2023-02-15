from typing import List
import json
import aioredis
import asyncpg
import orjson


class Cache:

    def __init__(self, conn:aioredis.Redis):
        self.conn = conn

    async def add_user(self, user_id: int, data: asyncpg.Record, expire: int = 120):
        if data is not None:
            key = user_id
            await self.conn.set(key, data, ex=expire)

    async def del_user(self, user_id: int):
        key = user_id
        await self.conn.delete(key)

    async def get_user(self, user_id: int):
        key = user_id
        data = await self.conn.get(key)
        if data is not None:
            data = data.decode('utf-8')
            await self.conn.expire(key, 120)
            return data
        return None