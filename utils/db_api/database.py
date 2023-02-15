import asyncio
from email.mime import message
from time import time
from typing import List
import datetime
import aiogram
import aioredis
import asyncpg
import uuid
import traceback

import pytz
from matplotlib.cbook import report_memory

from aiogram.utils import exceptions
from numpy import source

from data import config

sender_status = True



class DataBase:

    def __init__(self, pool:asyncpg.Pool,redis:aioredis.Redis):
        self.pool = pool
        self.redis = redis

    async def get_status(self, user_id: int):
        sql = 'Select status from users where user_id = $1'

        async with self.pool.acquire() as conn:
            return await conn.fetchval(sql, user_id)

    async def add_user(self, user_id: int):
        sql = 'Insert into users (user_id) values ($1)'

        async with self.pool.acquire() as conn:
            await conn.execute(sql, user_id)
