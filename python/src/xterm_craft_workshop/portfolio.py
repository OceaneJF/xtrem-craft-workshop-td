from xterm_craft_workshop.money import Money
from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency


class Portfolio:
    def __init__(self):
        self.money_dict: list[Money] = []
    

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