import time

from aiogram import types
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from utils.cache import Cache
from utils.db_cache import DataBaseCache

from utils.misc.roles import UserRole
from utils.db_api.database import DataBase

class RoleMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update", "channel_post"]

    def __init__(self):
        super().__init__()

    async def pre_process(self, obj, data, *args):
        db_cache = data['db_cache']
        db_cache : DataBaseCache
        user_status = await db_cache.get_status(obj.from_user.id)
        if user_status:
            user_status = int(user_status)
        else:
            user_status = 0
        if not getattr(obj, "from_user", None):
            data["role"] = None
        elif user_status == 1:
            data["role"] = UserRole.USER
        elif user_status == 1337:
            data["role"] = UserRole.ADMIN
        elif user_status == 2:
            data["role"] = UserRole.SUB
        elif user_status == 666:
            data["role"] = UserRole.BLOCKED
        elif user_status == 5:
            data["role"] = UserRole.BAN
        elif user_status == 777:
            data["role"] = UserRole.VIP
        else:
            data["role"] = UserRole.NOT_REG_USER
        if isinstance(obj, types.Message) and '_steps' in obj.conf:
            obj.conf['_steps'].append(('added role', time.monotonic(), time.monotonic() - obj.conf['_steps'][-1][1]))

    async def post_process(self, obj, data, *args):
        del data["role"]
