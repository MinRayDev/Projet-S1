import string


def get_letters(letter_indice: int) -> list:
    return list(string.ascii_lowercase)[:letter_indice]


