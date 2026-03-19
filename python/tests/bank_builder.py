from typing_extensions import Final, final
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from tests.exchange_rate import ExchangeRate


class BankBuilder:
    def __init__(self, currency: Currency = None):
        self._rates: list[ExchangeRate] = []
        self._pivot: Final[Currency] = currency

    def with_exchange_rate(self, currency: Currency, rate: float) -> "BankBuilder":
        if currency == self._pivot:
            raise AttributeError("Impossible d'ajouter un taux pour la devise pivot")
        self._rates.append(ExchangeRate(currency, rate))
        return self

    def build(self) -> Bank:
        bank = Bank({})
        for exchange_rate in self._rates:
            bank.addEchangeRate(Currency.EUR, exchange_rate.currency, exchange_rate.rate)
        return bank
