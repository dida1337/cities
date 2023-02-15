from aiogram import Dispatcher

from .role_filter import UserFilter,NoRegUserFilter,AdminFilter,SubscribeFilter,BanFilter,Vip



def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(BanFilter)
    dp.filters_factory.bind(UserFilter)
    dp.filters_factory.bind(NoRegUserFilter)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(SubscribeFilter)
    dp.filters_factory.bind(Vip)