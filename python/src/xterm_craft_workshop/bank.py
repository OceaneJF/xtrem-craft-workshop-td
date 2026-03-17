from typing import Dict
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError


class Bank:

    def __init__(self, exchange_rate: Dict[str, float] = {}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def create(from_currency: Currency, to_currency: Currency, rate: float) -> "Bank":
        bank = Bank({})
        bank.addEchangeRate(from_currency, to_currency, rate)

        return bank
    
    def addEchangeRate(self, from_currency: Currency, to_currency: Currency, rate: float) -> None:
        self._exchange_rate[f'{from_currency.value}->{to_currency.value}'] = rate

    def can_convert(self, from_currency: Currency, to_currency: Currency) -> bool:
        return from_currency.value == to_currency.value or f'{from_currency.value}->{to_currency.value}' in self._exchange_rate
    
    def convert(self, money: Money, to_currency: Currency) -> Money:
        if not self.can_convert(money.currency, to_currency):
            raise MissingExchangeRateError(money.currency, to_currency)
        amount = money.amount if money.currency.value == to_currency.value  else money.amount * self._exchange_rate[f'{money.currency.value}->{to_currency.value}']
        return Money(amount, to_currency) 
