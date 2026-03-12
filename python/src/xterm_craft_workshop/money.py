from xterm_craft_workshop.currency import Currency


class Money:
    def __init__(self, amount: int, currency: Currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise TypeError("Cannot add two Money with different currencies")
        res = self.amount + other.amount
        return Money(res, self.currency)

    def __eq__(self, value):
        return self.amount == value.amount and self.currency == value.currency
        
