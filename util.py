import random

def generate_row_digit(length):
    """
    :param length: la longueur de la chaîne de caractère
    :return: une suite de chiffre aléatoires de taille length
    """
    return "".join([random.randint(0, 9) for i in range(0, length)])