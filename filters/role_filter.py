import typing

from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types.base import TelegramObject

from utils.misc.roles import UserRole



class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj: TelegramObject):
        if self.is_admin is None:
            return True
        data = ctx_data.get()
        return (data.get("role") is UserRole.ADMIN) == self.is_admin


class SubscribeFilter(BoundFilter):
    key = 'is_sub'

    def __init__(self, is_sub: typing.Optional[bool] = None):
        self.is_sub = is_sub

    async def check(self, obj: TelegramObject):
        if self.is_sub is None:
            return True
        data = ctx_data.get()
        return (data.get("role") is UserRole.SUB) == self.is_sub

class UserFilter(BoundFilter):
    key = 'is_user'

    def __init__(self, is_user: typing.Optional[bool] = None):
        self.is_user = is_user

    async def check(self, obj: TelegramObject):
        if self.is_user is None:
            return True
        data = ctx_data.get()
        return (data.get("role") is UserRole.USER) == self.is_user

class NoRegUserFilter(BoundFilter):
    key = 'is_noReg'

    def __init__(self, is_noReg: typing.Optional[bool] = None):
        self.is_noReg = is_noReg

    async def check(self, obj: TelegramObject):
        if self.is_noReg is None:
            return True
        data = ctx_data.get()
        return (data.get("role") is UserRole.NOT_REG_USER) == self.is_noReg


class BanFilter(BoundFilter):
    key = 'is_ban'

    def __init__(self, is_ban: typing.Optional[bool] = None):
        self.is_ban = is_ban

    async def check(self, obj: TelegramObject):
        if self.is_ban is None:
            return True
        data = ctx_data.get()
        return (data.get("role") is UserRole.BAN) == self.is_ban

class Vip(BoundFilter):
    key = 'is_vip'

    def __init__(self, is_vip: typing.Optional[bool] = None):
        self.is_vip = is_vip

    async def check(self, obj: TelegramObject):
        if self.is_vip is None:
            return True
        data = ctx_data.get()
        return (data.get("role") is UserRole.VIP) == self.is_vip

