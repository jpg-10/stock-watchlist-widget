from repositories.SQLiteDatabase import SQLiteDatabase
from repositories.SQLiteAssetRepository import SQLiteAssetRepository
from repositories.SQLiteWatchlistRepository import SQLiteWatchlistRepository
import os

def main():
    database = SQLiteDatabase("watchlist.db")
    database.initialize()
    print(os.path.abspath("watchlist.db"))

if __name__ == "__main__":
    main()
