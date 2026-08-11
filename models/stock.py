from pip._internal import models

from models.asset import Asset

# a stock is an asset
class Stock(Asset):
    def __init__(self,
                 isin: str,
                 name: str,
                 symbol: str,
                 currency: str,
                 market_cap: float | int,
                 enterprise_value: float | int,
                 profit_margin: float | int,
                 return_on_assets: float | int,
                 return_on_equity: float | int,
                 revenue: float | int,
                 total_cash: float | int,
                 total_debt: float | int):
        super().__init__(isin, name, symbol, currency)
        self.isin = isin
        self.market_cap = market_cap
        self.enterprise_value = enterprise_value
        self.profit_margin = profit_margin
        self.return_on_assets = return_on_assets
        self.return_on_equity = return_on_equity
        self.revenue = revenue
        self.total_cash = total_cash
        self.total_debt = total_debt