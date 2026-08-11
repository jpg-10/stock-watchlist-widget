# this model is a parent for different assets such as stocks, ETFs, krypto etc.

class Asset():
    def __init__(self, isin, name):
        self.isin = isin
        self.name = name