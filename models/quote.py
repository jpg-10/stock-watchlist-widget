from datetime import datetime

# this model is showing the quote of an asset depending on its current price and previous close
class Quote:
    def __init__(self,
                 symbol: str,
                 price: float | int,
                 previous_close: float | int,
                 timestamp: datetime):
        self.symbol = symbol
        self.price = price
        self.previous_close = previous_close
        self.timestamp = timestamp

    # show the total price change on this day
    @property
    def price_change(self) -> float:
        return self.price - self.previous_close

    # depending on the price change, show the percentage the asset has gained / fallen
    @property
    def percent_change(self) -> float:
        return (self.price_change / self.previous_close) * 100


