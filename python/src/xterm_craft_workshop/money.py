from xterm_craft_workshop.currency import Currency


class Money:
    def __init__(self, amount: int, currency: Currency):
        if not isinstance(currency, Currency):
            raise TypeError("currency should be an instance of Currency")
        if amount < 0:
            raise ValueError("amount should be positive")
        
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise TypeError("Cannot add two Money with different currencies")
        res = self.amount + other.amount
        return Money(res, self.currency)

    def __eq__(self, value):
        return self.amount == value.amount and self.currency == value.currency
        
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Can only multiply Money by a number")
        res = self.amount * other
        return Money(res, self.currency)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Can only divide Money by a number")
        res = self.amount / other
        return Money(res, self.currency)
