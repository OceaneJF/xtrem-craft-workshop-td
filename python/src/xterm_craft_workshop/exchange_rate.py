from xterm_craft_workshop.currency import Currency


class ExchangeRate:
    def __init__(self, currency: Currency, rate: float):
        self.currency = currency
        self.rate = rate
