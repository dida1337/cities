from aiogram import Dispatcher

from . import error_handler


def register_handlers(dp: Dispatcher):
    dp.register_errors_handler(error_handler.errors_handler)
