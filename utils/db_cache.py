
import aiogram
from utils.cache import Cache
from utils.db_api.database import DataBase


class DataBaseCache:
    def __init__(self, db_conn: DataBase, cache_conn: Cache):
        self._db = db_conn
        self._cache = cache_conn


    async def get_status(self, user_id: int):
        status_from_cache = await self._cache.get_user(user_id)
        if status_from_cache == None:
            status_from_db = await self._db.get_status(user_id)
            await self._cache.add_user(user_id, status_from_db)
            return status_from_db
        return status_from_cache