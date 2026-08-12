from enum import Enum

# the direction to order the yields can be ascending or descending
class SortField(Enum):
    SYMBOL = 'symbol'
    PERFORMANCE = 'performance'

class SortDirection(Enum):
    ASCENDING = 'ascending'
    DESCENDING = 'descending'

class Watchlist:
    def __init__(self,
                 identifier: int | None,
                 name: str,
                 products,
                 sort_field: SortField = SortField.SYMBOL,
                 sort_direction: SortDirection = SortDirection.DESCENDING):
        self.id = identifier
        self.name = name
        self.products = products
        self.sort_field = sort_field
        self.sort_direction = sort_direction

    # add an asset to the watchlist
    def add_asset(self, asset):
        for p in self.products:
            if p.isin == asset.isin:
                raise ValueError(f"{asset.name} is already in the watchlist and therefore cannot be added.")
        self.products.append(asset)

    # remove an asset from the watchlist
    def remove_asset(self, asset):
        for p in self.products:
            if p.isin == asset.isin:
                self.products.remove(asset)
                exit()
        raise ValueError(f"{asset.name} is not in the watchlist and therefore cannot be removed.")
