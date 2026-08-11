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

