from pip._internal import models

from models.asset import Asset

# a stock is an asset
class Stock(Asset):
    def __init__(self, isin, name, market_cap, enterprise_value, profit_margin, return_on_assets,
                 return_on_equity, revenue, total_cash, total_debt):
        super().__init__(isin, name)
        self.market_cap = market_cap
        self.enterprise_value = enterprise_value
        self.profit_margin = profit_margin
        self.return_on_assets = return_on_assets
        self.return_on_equity = return_on_equity
        self.revenue = revenue
        self.total_cash = total_cash
        self.total_debt = total_debt