import mastercard
import util
import enum

class PaymentMethod:

    def __init__(self, bank_account):
        self.bank_account = bank_account

    def can_debit(self, amount):
        return self.bank_account.can_pay(amount)

    def can_credit(self, amount):
        return True

    def credit(self, amount):
        self.bank_account.credit(amount)

    def debit(self, amount):
        self.bank_account.debit(amount)

class PaymentCard(PaymentMethod):

    def __init__(self, card_number, bank_account):
        super().__init__(bank_account)
        self.card_number = card_number
        self.bank_account = bank_account

    def can_credit(self, amount):
        return False

class BankManager:

    def __init__(self):
        self.banks = []

    def register_bank(self, name):
        self.banks.append(Bank(name))

    def pay_with_card(self, debitor:str, creditor:str):
        return self.pay(mastercard.get_card(debitor), mastercard.get_card(creditor))

    def pay(self, debitor:PaymentMethod, creditor:PaymentMethod, amount) -> tuple:
        if not creditor.can_credit(amount):
            return PaymentResult.CANNOT_CREDIT

        if not debitor.can_debit(amount):
            return PaymentResult.INSUFFICIENT_FUNDS

        debitor.debit(amount)
        creditor.credit(amount)

    def register(self, bank_id, name):
        return self.banks[bank_id].register(name)

class BankAccount:

    def __init__(self, name):
        self.name = name
        self.__amount = 0
        self.__iban = "FR"+util.generate_row_digit(25)

    def get_iban(self):
        return self.__iban

    def credit(self, amount):
        """ Créditer un certain montant du compte

        :param amount: le montant à créditer
        """
        self.__amount += amount

    def debit(self, amount):
        """ Débiter un certain montant du compte

        :param amount: le montant à débiter
        """
        self.__amount -= amount

    def can_pay(self, amount):
        """ Vérifier si le compte est soldable

        :param amount: True si le compte est soldable, sinon False
        """
        return self.__amount >= amount

class PaymentResult(enum):
    ACCEPTED = (0, "Payment accepted")
    INSUFFICIENT_FUNDS = (1, "Insufficient funds")
    CANNOT_CREDIT = (2, "This payment method cannot be credited !")

class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def register(self, name):
        """Permet d'enregistrer un nouvel utilisateur dans cette banque.

        :param name: nom du client
        :return: la carte bancaire du nouveau client et son iban
        """
        bank_account = BankAccount(name)
        return mastercard.create_card(bank_account), bank_account.get_iban()

    def make_transaction(self, debitor: BankAccount, creditor: BankAccount, amount) -> tuple:
        """
        :param debitor: celui qui va donner la somme
        :param creditor: celui qui va recevoir la somme
        :param amount: montant de la transaction
        :return: le résultat de l'opération
        """
        if not debitor.can_pay(amount):
            return PaymentResult.FUND_INSUFFICIENT
        debitor.debit(amount)
        creditor.credit(amount)
        return PaymentResult.ACCEPTED