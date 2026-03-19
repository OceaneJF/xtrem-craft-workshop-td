from typing_extensions import Final
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.exchange_rate import ExchangeRate


class BankBuilder:
    def __init__(self, currency: Currency = None):
        self._rates: list[ExchangeRate] = []
        self._pivot: Final[Currency] = currency

    def with_exchange_rate(self, currency: Currency, rate: float) -> "BankBuilder":
        if currency == self._pivot:
            raise AttributeError("Impossible d'ajouter un taux pour la devise pivot")
        if rate <= 0:
            raise AttributeError("Le taux doit être strictement positif")
        self._rates.append(ExchangeRate(currency, rate))
        return self

    def build(self) -> Bank:
        if self._pivot is None:
            raise AttributeError("La devise pivot est obligatoire")
        bank = Bank(self._pivot)
        for exchange_rate in self._rates:
            bank.addEchangeRate(exchange_rate)
        return bank
