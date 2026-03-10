import pytest
import re

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError


class TestBank:
    
    bank : Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
    
    def test_should_convert_euro_to_usd_returns_float(self):
        bank : Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        
        expected = 12
        
        converted = bank.convert(10, Currency.EUR, Currency.USD)
        
        assert converted == expected

    def test_should_convert_euro_to_usd_returns_same_value(self):
        expected = 10
        
        converted = self.bank.convert(10, Currency.EUR, Currency.EUR)
        assert converted == expected

    def test_should_convert_with_missing_exchange_rate_throws_exception(self):
        with pytest.raises(MissingExchangeRateError) as error:
            self.bank.convert(10, Currency.EUR, Currency.KRW)
        
        assert str(error.value) == "EUR->KRW"

    def test_should_convert_with_different_exchange_rate_returns_different_floats(self):
        bank : Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        epsilon = 0.001
        
        converted1 = bank.convert(10, Currency.EUR, Currency.USD)
        self.bank.addEchangeRate(Currency.EUR, Currency.USD, 1.3)
        converted2 = bank.convert(10, Currency.EUR, Currency.USD)
        
        assert converted1 - converted2 < epsilon
        