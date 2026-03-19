from xterm_craft_workshop.money import Money
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.exchange_rate import ExchangeRate


class Bank:

    def __init__(self, pivot: Currency, exchange_rate: list[ExchangeRate] = None) -> None:
        self._exchange_rate = exchange_rate if exchange_rate is not None else []
        self._pivot = pivot

    @property
    def pivot(self) -> Currency:
        return self._pivot

    @staticmethod
    def create(exchange_rate: ExchangeRate, pivot: Currency) -> "Bank":
        bank = Bank(pivot)
        bank.addEchangeRate(exchange_rate)
        return bank

    def addEchangeRate(self, exchange_rate: ExchangeRate) -> None:
        if self.can_convert(exchange_rate.currency):
            raise AttributeError("Un taux existe déjà pour cette devise")
        self._exchange_rate.append(exchange_rate)

    def can_convert(self, currency: Currency) -> bool:
        return any(er.currency == currency for er in self._exchange_rate)

    def get_rate(self, currency: Currency) -> ExchangeRate:
        return next(er for er in self._exchange_rate if er.currency == currency)

    def convert(self, money: Money, to_currency: Currency) -> Money:
        # Règle : Le montant est obligatoirement non-négatif
        if money.amount < 0:
            raise AttributeError("Amount cannot be negative")

        # Règle : On peut convertir une devise vers elle-même
        if money.currency == to_currency:
            return Money(money.amount, to_currency)

        # Règle : On peut convertir depuis la devise pivot vers une autre devise
        if money.currency == self._pivot:
            if not self.can_convert(to_currency):
                raise MissingExchangeRateError(money.currency, to_currency)
            amount = round(money.amount * self.get_rate(to_currency).rate, 3)

        # Règle : On peut convertir vers la devise pivot
        elif to_currency == self._pivot:
            if not self.can_convert(money.currency):
                raise MissingExchangeRateError(money.currency, to_currency)
            amount = round(money.amount / self.get_rate(money.currency).rate, 3)

        # Règle : On peut convertir depuis une devise tierce en passant par la pivot
        else:
            if not self.can_convert(money.currency):
                raise MissingExchangeRateError(money.currency, to_currency)
            if not self.can_convert(to_currency):
                raise MissingExchangeRateError(money.currency, to_currency)
            amount = round(money.amount / self.get_rate(money.currency).rate * self.get_rate(to_currency).rate, 3)

        return Money(amount, to_currency)
