from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency


class BankBuilder:
    def __init__(self, currency: Currency):
        self._rates: list[tuple[Currency, float]] = []
        self._pivot: Currency = currency

    def with_exchange_rate(self, currency: Currency, rate: float) -> "BankBuilder":
        self._rates.append((currency, rate))
        return self

    def build(self) -> Bank:
        bank = Bank({})
        for currency, rate in self._rates:
            bank.addEchangeRate(Currency.EUR, currency, rate)
        return bank
