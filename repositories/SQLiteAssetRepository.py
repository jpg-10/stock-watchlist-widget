from interfaces.IAssetRepository import IAssetRepository
from models.asset import Asset
from repositories.SQLiteDatabase import SQLiteDatabase

class SQLiteAssetRepository(IAssetRepository):
    def __init__(self, database: SQLiteDatabase):
        self.database = database

    def get_all_assets(self):
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                SELECT * 
                FROM assets
                """
            )
            rows = cursor.fetchall()
            return [Asset(**dict(row)) for row in rows]

    def get_asset_by_id(self, asset_id: int) -> None | Asset:
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                SELECT * 
                FROM assets 
                WHERE id = ?
                """,
                (asset_id, )
            )
            row = cursor.fetchall()
            return None if row is None else Asset(**dict(row))

    def add_asset(self, asset: Asset) -> None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO assets
                    (isin, name, symbol, currency)
                VALUES (?, ?, ?, ?)
                """,
                (asset.isin, asset.name, asset.symbol, asset.currency)
            )

    def delete_asset(self, asset: Asset) -> None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                DELETE FROM assets
                WHERE id = ?
                """,
                (asset.id, )
            )

    def update_asset(self, asset: Asset) -> None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                """
                UPDATE assets
                SET isin = ?, name = ?, symbol = ?, currency = ?
                WHERE id = ?
                """,
                (asset.isin, asset.name, asset.symbol, asset.currency, asset.id)
            )

    def get_asset_by_name(self, asset_name: str) -> Asset | None:
        with self.database.connect() as connection:
            cursor = connection.execute(
                '''
                SELECT * from assets WHERE name = ?
                ''', (asset_name, )
            )
            row = cursor.fetchone()
            return None if row is None else Asset(**dict(row))