from python.src.bank import Bank
from python.src.currency import Currency


class Portfolio:
    def __init__(self):
        self.amount_dict: dict[Currency, float] = {}
    
    def evaluate(self, bank: Bank, currency: Currency) -> float:
        total = 0
        for c, amount in self.amount_dict.items():
            total = total + bank.convert(amount, c, currency)
        
        return total

    def deposit(self, amount: float, currency: Currency):
        if not isinstance(currency, Currency):
            raise TypeError("currency should be an instance of Currency")
        self.amount_dict[currency] = self.amount_dict[currency] + amount if currency in self.amount_dict else amount