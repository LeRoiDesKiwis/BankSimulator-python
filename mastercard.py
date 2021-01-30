import luhn
import util
import bank

cards = {}

def __register_card(card_number, bank_account):
    """Enregistre une nouvelle carte de paiement

    :param bank_account: le compte bancaire a lié à la carte
    :param card_number: le numéro de carte
    """
    payment_card = bank.PaymentCard(card_number, bank_account)
    cards[card_number] = payment_card

def get_card(number):
    return cards[number]

def create_card(bank_account):
    """Créer une carte de paiement liée à un compte bancaire, et renvoie le numéro de celle-ci

    :param bank_account: le compte bancaire a lié à la carte
    :return: le numéro de carte
    """
    card_number = "53"+util.generate_row_digit(13)
    card_number = luhn.valid(card_number)
    __register_card(card_number, bank_account)

    return card_number
