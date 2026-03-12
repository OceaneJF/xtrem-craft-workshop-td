
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
    
    def test_should_deposit_the_same_currency(self):
        portfolio: Portfolio = Portfolio()
        portfolio.deposit(10, Currency.EUR)
        portfolio.deposit(20, Currency.EUR)
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        assert portfolio.evaluate(bank, Currency.EUR) == 30

    def test_shouldnot_add_an_unvalid_currency(self):
        portfolio: Portfolio = Portfolio()
        with pytest.raises(TypeError):
            portfolio.deposit(10, "Yen")
