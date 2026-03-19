import pytest

from xterm_craft_workshop.bank import Bank
from xterm_craft_workshop.currency import Currency
from xterm_craft_workshop.missing_exchange_rate_error import MissingExchangeRateError
from xterm_craft_workshop.money import Money

from tests.bank_builder import BankBuilder
from xterm_craft_workshop.exchange_rate import ExchangeRate


class TestBank:
    bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()

    # Règle : On peut convertir depuis la devise pivot vers une autre devise
    def test_should_convert_euro_to_usd_returns_money(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        expected = Money(12, Currency.USD)

        converted = bank.convert(Money(10, Currency.EUR), Currency.USD)

        assert converted == expected
        assert isinstance(converted, Money)

    # Règle : On peut convertir une devise vers elle-même
    def test_should_convert_euro_to_usd_returns_same_value(self):
        expected = Money(10, Currency.EUR)

        converted = self.bank.convert(Money(10, Currency.EUR), Currency.EUR)
        assert converted == expected

    # Règle : On ne peut pas convertir si le taux est manquant
    def test_should_convert_with_missing_exchange_rate_throws_exception(self):
        with pytest.raises(MissingExchangeRateError) as error:
            self.bank.convert(Money(10, Currency.EUR), Currency.KRW)

        assert str(error.value) == "EUR->KRW"

    # Règle : Le taux est toujours défini depuis la devise pivot
    def test_should_convert_with_different_exchange_rate_returns_different_floats(self):
        bank1 = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        bank2 = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.3).build()

        converted1 = bank1.convert(Money(10, Currency.EUR), Currency.USD)
        converted2 = bank2.convert(Money(10, Currency.EUR), Currency.USD)

        assert converted1 != converted2

    # Règle : Une banque a exactement une devise pivot
    def test_bank_cant_change_pivot(self):
        bank = BankBuilder(Currency.EUR).build()
        with pytest.raises(AttributeError):
            bank.pivot = Currency.USD

    # Règle : On ne peut pas définir de banque sans devise pivot
    def test_should_have_a_pivot_currency(self) :
        with pytest.raises(AttributeError):
            BankBuilder().build()

    # Règle : On ne peut pas ajouter un taux pour la devise pivot elle-même
    def test_shouldnt_add_exchange_rate_on_pivot(self):
        with pytest.raises(AttributeError):
            bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.EUR, 1.2).build()

    # Règle : On ne peut pas ajouter un taux de change négatif ou nul
    def test_shouldnt_add_negative_exchange_rate(self):
        with pytest.raises(AttributeError):
            BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, -1.2).build()

    # Règle : On ne peut pas ajouter un taux de change négatif ou nul
    def test_shouldnt_add_zero_exchange_rate(self):
        with pytest.raises(AttributeError):
            BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 0).build()

    # Règle : On ne peut pas ajouter un taux sur une devise qui en a déjà un
    def test_shouldnt_add_existing_exchange_rate(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        with pytest.raises(AttributeError):
            bank.addEchangeRate(ExchangeRate(Currency.USD, 1.2))

    # Règle : Round Tripping à 10^-3
    def test_round_tripping_conversion(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        converted = bank.convert(Money(10, Currency.USD), Currency.EUR)
        reconverted = bank.convert(converted, Currency.USD)
        assert abs(reconverted.amount - 10) < 0.001

    # Règle : Le montant est obligatoirement non-négatif
    def test_shouldnt_convert_negative_amount(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        with pytest.raises(ValueError):
            bank.convert(Money(-10, Currency.EUR), Currency.USD)

    # Règle : On peut convertir une devise vers elle-même
    def test_should_convert_currency_to_itself(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        expected = Money(10, Currency.USD)

        converted = bank.convert(Money(10, Currency.USD), Currency.USD)

        assert converted == expected

    # Règle : On peut convertir vers la devise pivot
    def test_should_convert_to_pivot_currency(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        expected = Money(10, Currency.EUR)

        converted = bank.convert(Money(12, Currency.USD), Currency.EUR)

        assert converted == expected

    # Règle : On peut convertir depuis une devise tierce en passant par la pivot
    def test_should_convert_from_third_currency_via_pivot(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).with_exchange_rate(Currency.GBP, 1.5).build()
        expected = Money(12.5, Currency.GBP)

        converted = bank.convert(Money(10, Currency.USD), Currency.GBP)

        assert converted == expected

    # Règle : On doit définir un règlement d'arrondi des résultats de conversion
    def test_should_round_conversion_result_to_3_decimals(self):
        bank = BankBuilder(Currency.EUR).with_exchange_rate(Currency.USD, 1.2).build()
        expected = Money(1.208, Currency.EUR)

        converted = bank.convert(Money(1.45, Currency.USD), Currency.EUR)

        assert converted == expected
