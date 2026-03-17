from python.src.xterm_craft_workshop.money import Money
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency


class Portfolio:
    def __init__(self):
        # self.amount_dict: dict[Currency, float] = {}
        self.money_dict: list[Money] = []
    
    # def evaluate(self, bank: Bank, currency: Currency) -> float:
    #     if not isinstance(currency, Currency):
    #         raise TypeError("currency should be an instance of Currency")
    #     total = 0
    #     for c, amount in self.amount_dict.items():
    #         total = total + bank.convert(amount, c, currency)
        
    #     return total

    # def deposit(self, amount: float, currency: Currency):
    #     if not isinstance(currency, Currency):
    #         raise TypeError("currency should be an instance of Currency")
    #     if amount < 0:
    #         raise ValueError("amount should be positive")
    #     self.amount_dict[currency] = self.amount_dict[currency] + amount if currency in self.amount_dict else amount

    def deposit(self, money: Money):
        if not isinstance(money, Money):
            raise TypeError("money should be an instance of Money")
        self.money_dict.append(money)

    def evaluate(self, bank: Bank, currency: Currency) -> Money:
        if not isinstance(currency, Currency):
            raise TypeError("currency should be an instance of Currency")
        total = Money(0, currency)
        for money in self.money_dict:
            total = total + bank.convert(money, currency)
        return total