
import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money import Money
from xterm_craft_workshop.portfolio import Portfolio


class TestPortfolio:
    def test_should_evaluate_an_empty_portfolio_to_0(self):
        portfolio: Portfolio = Portfolio()
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == Money(0, Currency.USD)

    def test_should_deposit_an_amount_in_a_currency(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(Money(10, Currency.EUR))
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == Money(12, Currency.USD)

    def test_should_deposit_an_amount_in_different_currencies(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(Money(10, Currency.EUR))
        portfolio.deposit(Money(5, Currency.USD))
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == Money(17, Currency.USD)

    def test_should_deposit_the_same_currency(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(Money(10, Currency.USD))
        portfolio.deposit(Money(20, Currency.USD))
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == Money(30, Currency.USD)

    def test_shouldnot_add_an_unvalid_currency(self):
        with pytest.raises(TypeError) as error:
            Money(10, "Yen")
        assert str(error.value) == "currency should be an instance of Currency"

    def test_shouldnot_convert_if_exchange_rate_is_missing(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(Money(10, Currency.EUR))
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        with pytest.raises(Exception) as error:
            portfolio.evaluate(bank, Currency.KRW)

        assert str(error.value) == "EUR->KRW"

    def test_should_raise_error_when_depositing_negative_amout(self):
        with pytest.raises(ValueError) as error:
            Money(-1, Currency.EUR)

        assert str(error.value) == "amount should be positive"

    def test_shouldnot_evaluate_with_an_invalid_currency(self):
        portfolio: Portfolio = Portfolio()
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        with pytest.raises(TypeError) as error:
            portfolio.evaluate(bank, "Yen")
        assert str(error.value) == "currency should be an instance of Currency"

    def test_should_accept_zero_amount(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(Money(0, Currency.EUR))
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == Money(0, Currency.USD)
