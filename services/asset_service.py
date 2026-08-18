from models.asset import Asset
from repositories.SQLiteAssetRepository import SQLiteAssetRepository

class AssetService:
    def __init__(self, asset_repository: SQLiteAssetRepository) -> None:
        self.asset_repository = asset_repository

    def get_asset_by_id(self, asset_id: int) -> Asset | None:
        return self.asset_repository.get_asset_by_id(asset_id)

    def get_all_assets(self) -> list[Asset]:
        return self.asset_repository.get_all_assets()

    def delete_asset(self, asset: Asset) -> None:
        if self.get_asset_by_name(asset.name) is not None:
            self.asset_repository.delete_asset(asset)
        else: raise ValueError("Asset is not in the watchlist")

    def add_asset(self, asset: Asset) -> None:
        if self.get_asset_by_name(asset.name) is None:
            self.asset_repository.add_asset(asset)
        else: raise ValueError("Asset is already in the watchlist")

    def update_asset(self, asset: Asset) -> None:
        if self.get_asset_by_name(asset.name) is not None:
            self.asset_repository.update_asset(asset)
        else: raise ValueError("Asset is not in the watchlist")

    def get_asset_by_name(self, asset_name: str) -> Asset | None:
        return self.asset_repository.get_asset_by_name(asset_name)