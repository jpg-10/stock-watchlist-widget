import sqlite3

class SQLiteDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection