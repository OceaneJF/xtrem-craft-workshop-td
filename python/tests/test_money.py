import pytest

from xterm_craft_workshop.money import Money
from xterm_craft_workshop.currency import Currency

class TestMoney:
    def test_add_in_usd_returns_value(self):

        tenDollars =  Money(10, Currency.USD)
        fiveDollars =  Money(5, Currency.USD)
        expectedResult = Money(15, Currency.USD)
        
        res = fiveDollars + tenDollars
        
        assert res == expectedResult
        assert isinstance(res, Money)

    def test_multiply_in_euros_returns_positive_number(self):
        tenDollars =  Money(10, Currency.USD)
        value = 2.0
        expectedResult = Money(20, Currency.USD)
        
        res =  value * tenDollars
        
        assert res == expectedResult
        assert isinstance(res, Money)

    def test_divide_in_korean_won_returns_float(self):
        amount = Money(4002, Currency.USD)
        value = 4
        expectedResult = Money(1000.5, Currency.USD)

        res = amount / value

        assert res == expectedResult
        assert isinstance(res, Money)

    def test_zero_amount_is_valid(self):
        money = Money(0, Currency.USD)
        assert money.amount == 0

    def test_invalid_currency_raises_type_error_with_message(self):
        with pytest.raises(TypeError) as error:
            Money(10, "Yen")
        assert str(error.value) == "currency should be an instance of Currency"

    def test_negative_amount_raises_value_error_with_message(self):
        with pytest.raises(ValueError) as error:
            Money(-1, Currency.USD)
        assert str(error.value) == "amount should be positive"

    def test_same_amount_different_currency_are_not_equal(self):
        assert Money(10, Currency.USD) != Money(10, Currency.EUR)

