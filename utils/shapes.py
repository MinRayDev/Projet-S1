"""Fichier avec toutes les fonctions permettant de générer les formes de cartes de jeu.
@project Tetris
@author Gauthier
@author Marielle
"""
import math


def add_space(string: str) -> str:
    """Ajoute des espaces entre tous les caractères d'un string et le retourne.

    :param string: String auquel il faut ajouter des espaces.

    :return: String avec des espaces.
    :rtype: str.
    """
    string_to_return: str = ""

    for char in string:
        # Si le caractère n'est pas un saut de ligne on ajoute un espace
        string_to_return += char + " " if char != "\n" else char

    return string_to_return


def gen_losange(size: int) -> str:
    """Génère le string d'un losange et le retourne.

    :param size: Taille du losange.

    :return: String du losange.
    :rtype: str.

    """
    string_to_return: str = ""

    # Si le nombre est pair il y aura 2 colonnes du milieu sinon une seule.
    offset = 2 if size % 2 == 0 else 1

    # Première partie du losange.
    # Pour toutes les lignes de cette partie on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 augmente et de 0 diminue lorsque le nombre d'itérations augmente.
    # Math.ceil(x) revient à arrondir au supérieur x.
    for x in range(math.ceil(size / 2)):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"

    # Seconde partie du losange.
    # Pour toutes les lignes de cette partie on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 diminue et de 0 augmente lorsque le nombre d'itérations augmente.
    for x in range(math.ceil(size / 2) - 2, -1, -1):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"

    return add_space(string_to_return)


def gen_triangle(size: int) -> str:
    """Génère le string d'un triangle et le retourne.

    :param size: Taille du triangle.

    :return: String du triangle.
    :rtype: str.

    """
    string_to_return: str = ""

    # Si le nombre est pair il y aura 2 colonnes du milieu sinon une seule.
    offset = 2 if size % 2 == 0 else 1

    # Pour toutes les lignes on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 augmente et de 0 diminue lorsque le nombre d'itérations augmente.
    # Math.ceil(x) revient à arrondir au supérieur x.
    for x in range(math.ceil(size / 2)):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"

    return add_space(string_to_return)


def gen_circle(size: int) -> str:
    """Génère le string d'un cercle et le retourne.

    :param size: Taille du cercle.

    :return: String du cercle.
    :rtype: str.

    """
    string_to_return: str = ""

    # Première partie du cercle.
    # Pour toutes les lignes de cette partie on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 augmente et de 0 diminue lorsque le nombre d'itérations augmente.
    for x in range(size // (3 * 2)):
        string_to_return += "0" * (int(size / (3 * 2)) - x)
        string_to_return += "1" * (size - (int(size / (3 * 2)) - x) * 2)
        string_to_return += "0" * (int(size / (3 * 2)) - x)
        string_to_return += "\n"

    # Seconde partie du cercle.
    # Pour toutes les lignes de cette partie on va dessiner que des 1.
    for x in range(math.ceil(size - (size // 3))):
        if x <= size:
            string_to_return += "1" * size
            string_to_return += "\n"
        else:
            string_to_return += "1" * int(size / 3)
            string_to_return += "\n"

    # Trosième partie du losange.
    # Pour toutes les lignes de cette partie on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 diminue et de 0 augmente lorsque le nombre d'itérations augmente.
    for x in range(int(size / (3 * 2))):
        string_to_return += "0" * (x + 1)
        string_to_return += "1" * (size - (x + 1) * 2)
        string_to_return += "0" * (x + 1)
        string_to_return += "\n"

    return add_space(string_to_return)
