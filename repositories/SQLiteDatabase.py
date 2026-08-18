import sqlite3

class SQLiteDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def initialize(self):
        with self.connect() as connection:
            connection.execute("""
                               CREATE TABLE IF NOT EXISTS assets
                               (
                                   id       INTEGER PRIMARY KEY AUTOINCREMENT,
                                   isin     TEXT,
                                   name     TEXT NOT NULL,
                                   symbol   TEXT NOT NULL,
                                   currency TEXT NOT NULL
                               )
                               """)

            connection.execute("""
                               CREATE TABLE IF NOT EXISTS watchlists
                               (
                                   id             INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name           TEXT NOT NULL,
                                   sort_field     TEXT NOT NULL,
                                   sort_direction TEXT NOT NULL
                               )
                               """)

            connection.execute("""
                               CREATE TABLE IF NOT EXISTS watchlist_assets
                               (
                                   watchlist_id INTEGER NOT NULL,
                                   asset_id     INTEGER NOT NULL,

                                   PRIMARY KEY (watchlist_id, asset_id),

                                   FOREIGN KEY (watchlist_id)
                                       REFERENCES watchlists (id),

                                   FOREIGN KEY (asset_id)
                                       REFERENCES assets (id)
                               )
                               """)