"""Fichier contenant les fonctions permettant de vérifier qu'une entrée soit correcte.
@project Tetris
@author Gauthier
@author Marielle
"""


def is_correct_number(number: str, min_value: int, max_value: int) -> bool:
    """Vérifie si un string est numéric et s'il est compris entre 2 nombres.

    :param number: Nombre à vérifier.
    :param min_value: Valeur inférieure.
    :param max_value: Valeur supérieure.

    """
    return number.isnumeric() and (min_value <= int(number) <= max_value)
