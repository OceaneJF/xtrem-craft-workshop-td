import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money

from tests.bank_builder import BankBuilder


class TestBank:
    bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()

    def test_should_convert_euro_to_usd_returns_money(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        expected = Money(12, Currency.USD)

        converted = bank.convert(Money(10, Currency.EUR), Currency.USD)

        assert converted == expected
        assert isinstance(converted, Money)

    def test_should_convert_euro_to_usd_returns_same_value(self):
        expected = Money(10, Currency.EUR)

        converted = self.bank.convert(Money(10, Currency.EUR), Currency.EUR)
        assert converted == expected

    def test_should_convert_with_missing_exchange_rate_throws_exception(self):
        with pytest.raises(MissingExchangeRateError) as error:
            self.bank.convert(Money(10, Currency.EUR), Currency.KRW)

        assert str(error.value) == "EUR->KRW"

    def test_should_convert_with_different_exchange_rate_returns_different_floats(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        epsilon = 0.001

        converted1 = bank.convert(Money(10, Currency.EUR), Currency.USD)
        self.bank.addEchangeRate(Currency.EUR, Currency.USD, 1.3)
        converted2 = bank.convert(Money(10, Currency.EUR), Currency.USD)

        assert abs(converted1.amount - converted2.amount) < epsilon

    def test_bank_cant_change_pivot(self):
        bank = BankBuilder(Currency.EUR).build()
        with pytest.raises(AttributeError):
            bank.pivot = Currency.USD

    def test_should_have_a_pivot_currency(self) :
        with pytest.raises(AttributeError):
            BankBuilder().build()

    def test_shouldnt_add_exchange_rate_on_pivot(self):
        with pytest.raises(AttributeError):
            bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.EUR, 1.2).build()

    def test_shouldnt_add_negative_exchange_rate(self):
        with pytest.raises(AttributeError):
            BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, -1.2).build()

    def test_shouldnt_add_zero_exchange_rate(self):
        with pytest.raises(AttributeError):
            BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 0).build()

    def test_shouldnt_add_existing_exchange_rate(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        with pytest.raises(AttributeError):
            bank.addEchangeRate(Currency.EUR, Currency.USD, 1.2)

