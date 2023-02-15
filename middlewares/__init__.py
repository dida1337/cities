from aiogram import Dispatcher

from middlewares.database import DbMiddleware
from .role import RoleMiddleware
from .throttling import ThrottlingMiddleware


def register_middlewares(dp: Dispatcher):
    dp.middleware.setup(DbMiddleware(
        pool=dp['pool'],
        redis=dp['redis'],
        database=dp['database'],
        cache=dp['cache']
    ))
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(RoleMiddleware())