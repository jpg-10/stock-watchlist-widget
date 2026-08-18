# implement CRUDs for the Asset Repository
from abc import abstractmethod, ABC
from typing import List

from models.asset import Asset

class IAssetRepository(ABC):
    @abstractmethod
    def add_asset(self, asset: Asset) -> None: pass

    @abstractmethod
    def delete_asset(self, asset: Asset) -> None: pass

    @abstractmethod
    def get_all_assets(self) -> List[Asset]: pass

    @abstractmethod
    def get_asset_by_id(self, asset_id: int) -> Asset | None: pass

    @abstractmethod
    def update_asset(self, asset: Asset) -> None: pass

    @abstractmethod
    def get_asset_by_name(self, asset_name: str) -> Asset | None: pass