from xterm_craft_workshop.money import Money
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.money_calculator import MoneyCalculator

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
        expected : float = 1000.5
        amount : int = 4002
        value : int = 4
        currency : Currency = Currency.USD
        result = MoneyCalculator.divide(amount, currency, value) 
        assert result == expected

    
