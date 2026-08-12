# implement CRUDs for the Watchlist Repository
from abc import abstractmethod, ABC
from typing import List

from models.watchlist import Watchlist

class IWatchlistRepository(ABC):
    @abstractmethod
    def add_watchlist(self, watchlist: Watchlist) -> None: pass

    @abstractmethod
    def delete_watchlist(self, watchlist: Watchlist) -> None: pass

    @abstractmethod
    def get_all_watchlist(self) -> List[Watchlist]: pass

    @abstractmethod
    def get_watchlist_by_id(self, watchlist_id: int) -> Watchlist | None: pass

    @abstractmethod
    def update_watchlist(self, watchlist: Watchlist) -> None: pass