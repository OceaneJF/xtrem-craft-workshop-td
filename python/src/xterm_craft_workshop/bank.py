from typing import Dict
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.exchange_rate import Exchange_rate


class Bank:

    def __init__(self, pivot : Currency, exchange_rate: list[Exchange_rate] = []) -> None:
        self._exchange_rate = exchange_rate
        self._pivot = pivot

    @staticmethod
    def create(exchange_rate : Exchange_rate, pivot : Currency) -> "Bank":
        bank = Bank(pivot)
        bank.addEchangeRate(exchange_rate)

        return bank
    
    def addEchangeRate(self, exchange_rate: Exchange_rate) -> None:
        self._exchange_rate.append(exchange_rate)

    def can_convert(self, currency: Currency) -> bool:
        return any(er.currency == currency for er in self._exchange_rate)
    
    def convert(self, money: Money, to_currency: Currency) -> Money:
        if not self.can_convert(money.currency, to_currency):
            raise MissingExchangeRateError(money.currency, to_currency)
        amount = money.amount if money.currency.value == to_currency.value  else money.amount * self._exchange_rate[f'{money.currency.value}->{to_currency.value}']
        return Money(amount, to_currency) 
