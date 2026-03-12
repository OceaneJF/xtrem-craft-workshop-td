
import pytest

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.portfolio import Portfolio


class TestPortfolio:
    def test_should_evaluate_an_empty_portfolio_to_0(self):
        portfolio: Portfolio = Portfolio()
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == 0

    def test_should_deposit_an_amount_in_a_currency(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(10, Currency.EUR)
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == 12

    def test_should_deposit_an_amount_in_different_currencies(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(10, Currency.EUR)
        portfolio.deposit(5, Currency.USD)
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == 17
    
    def test_should_deposit_the_same_currency(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(10, Currency.USD)
        portfolio.deposit(20, Currency.USD)
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.USD) == 30

    def test_shouldnot_add_an_unvalid_currency(self):
        portfolio: Portfolio = Portfolio()
        with pytest.raises(TypeError):
            portfolio.deposit(10, "Yen")

    def test_shouldnot_convert_if_exchange_rate_is_missing(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(10, Currency.EUR)
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        with pytest.raises(Exception) as error:
            portfolio.evaluate(bank, Currency.KRW)
        
        assert str(error.value) == "EUR->KRW"

    def test_should_raise_error_when_depositing_negative_amout(self):
        portfolio: Portfolio = Portfolio()
        with pytest.raises(ValueError) as error:
            portfolio.deposit(-1, Currency.EUR)
        
        assert str(error.value) == "amount should be positive"
