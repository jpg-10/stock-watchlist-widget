from typing import List

from interfaces.IWatchlistRepository import IWatchlistRepository
from repositories.SQLiteDatabase import SQLiteDatabase
from models.watchlist import Watchlist

class SQLiteWatchlistRepository(IWatchlistRepository):
    def __init__(self, database: SQLiteDatabase):
        self.database = database

    def add_watchlist(self, watchlist: Watchlist) -> None:
        with self.database.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO watchlists 
                    (watchlist_id, watchlist) 
                VALUES (?, ?)
                ''', (watchlist.id, watchlist)
            )

    def delete_watchlist(self, watchlist: Watchlist) -> None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                '''
                Delete from watchlists 
                where watchlist_id = ?
                ''', (watchlist.id,)
            )

    def get_all_watchlist(self) -> List[Watchlist]:
        with self.database.connect() as connection:
            cursor = connection.execute(
                '''
                SELECT * FROM watchlists
                ORDER BY watchlist_id
                '''
            )
            rows = cursor.fetchall()
            return [Watchlist(**dict(row)) for row in rows]

    def get_watchlist_by_id(self, watchlist_id: int) -> Watchlist | None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                '''
                SELECT watchlist_id, watchlist
                FROM watchlists
                where watchlist_id = ?
                ''', (watchlist_id,)
            )
            row = cursor.fetchone()
            return Watchlist(**dict(row)) if row else None

    def update_watchlist(self, watchlist: Watchlist) -> None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                '''
                UPDATE watchlists 
                where watchlist_id = ?
                set watchlist_name = ?, watchlist_products = ?, watchlist_sort_fields = ?, watchlist_sort_direction = ?
                ''', (watchlist.id, watchlist.name, watchlist.products, watchlist.sort_field, watchlist.sort_direction)
            )
