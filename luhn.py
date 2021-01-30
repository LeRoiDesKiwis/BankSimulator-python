card_types = {
    51: "MasterCard",
    52: "MasterCard",
    53: "MasterCard",
    54: "MasterCard",
    55: "MasterCard",
    34: "American Express",
    37: "American Express",
    4: "Visa",
}


def luhn(string):
    string = string[::-1]
    int_string = [int(i) for i in string]
    for i in range(1, len(int_string), 2):
        int_string[i] = int_string[i] * 2

        if int_string[i] > 9:
            int_string[i] -= 9

    return sum(int_string)


def valid(string):
    return 10 - (luhn(string + "0") % 10)


def card_type(card_number):
    for (key, value) in card_types.items():
        if card_number.startswith(str(key)):
            return value
    return "Unknown"

def is_valid(card_number):
    return luhn(card_number)%10 == 0