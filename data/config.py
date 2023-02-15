import pathlib

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env((pathlib.Path(__file__).parent.parent / '.env').__str__())

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str

ADMINS = list(map(int, env.list("ADMINS")))  # Тут у нас будет список из админов

PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
PG_DATABASE = env.str("PG_DATABASE")
PG_HOST = env.str('PG_HOST')

FSM_REDIS_HOST = env.str('FSM_REDIS_HOST')
FSM_REDIS_PASSWORD = env.str('FSM_REDIS_PASSWORD')
FSM_REDIS_PORT = env.int('FSM_REDIS_PORT')


CACHE_REDIS_HOST = env.str('CACHE_REDIS_HOST')
CACHE_REDIS_PASSWORD = env.str('CACHE_REDIS_PASSWORD')
CACHE_REDIS_PORT = env.int('CACHE_REDIS_PORT')

WEBHOOK_USE = False
