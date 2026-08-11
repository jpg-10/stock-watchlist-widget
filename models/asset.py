# this model is a parent for different assets such as stocks, ETFs, krypto etc.

class Asset():
    def __init__(self, isin: str | None, name: str, symbol: str, currency: str):
        self.isin = isin
        self.name = name
        self.symbol = symbol
        self.currency = currency