"""Fichier avec toutes les fonctions permettant de générer les formes de cartes de jeu.
@project Tetris
"""
import math
from io import StringIO


def add_space(string: str) -> str:
    """Ajoute des espaces entre tous les caractères d'un string et le retourne.

    :param string: String auquel il faut ajouter des espaces.

    :return: String avec des espaces.
    :rtype: Str.

    """
    sb: StringIO = StringIO()

    for char in string:
        # Si le caractère n'est pas un saut de ligne, on ajoute un espace
        sb.write(char + " " if char != "\n" else char)

    return sb.getvalue()


def gen_losange(size: int) -> str:
    """Génère le string d'un losange et le retourne.

    :param size: Taille du losange.

    :return: String du losange.
    :rtype: Str.

    """
    sb: StringIO = StringIO()

    # Si le nombre est pair il y aura 2 colonnes du milieu sinon une seule.
    offset = 2 if size % 2 == 0 else 1

    # Première partie du losange.
    # Pour toutes les lignes de cette partie, on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 augmente et de 0 diminue lorsque le nombre d'itérations augmente.
    # Math.ceil(x) revient à arrondir au supérieur x.
    for x in range(math.ceil(size / 2)):
        sb.write("0" * (int(size / 2) - (x + offset - 1)))
        sb.write("1" * (2 * x + offset))
        sb.write("0" * (int(size / 2) - (x + offset - 1)))
        sb.write("\n")

    # Seconde partie du losange.
    # Pour toutes les lignes de cette partie, on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 diminue et de 0 augmente lorsque le nombre d'itérations augmente.
    for x in range(math.ceil(size / 2) - 2, -1, -1):
        sb.write("0" * (int(size / 2) - (x + offset - 1)))
        sb.write("1" * (2 * x + offset))
        sb.write("0" * (int(size / 2) - (x + offset - 1)))
        sb.write("\n")

    return add_space(sb.getvalue())


def gen_triangle(size: int) -> str:
    """Génère le string d'un triangle et le retourne.

    :param size: Taille du triangle.

    :return: String du triangle.
    :rtype: Str.

    """
    sb: StringIO = StringIO()

    # Si le nombre est pair il y aura 2 colonnes du milieu sinon une seule.
    offset = 2 if size % 2 == 0 else 1

    # Pour toutes les lignes, on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 augmente et de 0 diminue lorsque le nombre d'itérations augmente.
    # Math.ceil(x) revient à arrondir au supérieur x.
    for x in range(math.ceil(size / 2)):
        sb.write("0" * (int(size / 2) - (x + offset - 1)))
        sb.write("1" * (2 * x + offset))
        sb.write("0" * (int(size / 2) - (x + offset - 1)))
        sb.write("\n")

    return add_space(sb.getvalue())


def gen_circle(size: int) -> str:
    """Génère le string d'un cercle et le retourne.

    :param size: Taille du cercle.

    :return: String du cercle.
    :rtype: Str.

    """
    sb: StringIO = StringIO()
    # Première partie du cercle.
    # Pour toutes les lignes de cette partie, on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 augmente et de 0 diminue lorsque le nombre d'itérations augmente.
    for x in range(size // (3 * 2)):
        sb.write("0" * (int(size / (3 * 2)) - x))
        sb.write("1" * (size - (int(size / (3 * 2)) - x) * 2))
        sb.write("0" * (int(size / (3 * 2)) - x))
        sb.write("\n")

    # Seconde partie du cercle.
    # Pour toutes les lignes de cette partie, on va dessiner que des 1.
    for x in range(math.ceil(size - (size // 3))):
        if x <= size:
            sb.write("1" * size)
            sb.write("\n")
        else:
            sb.write("1" * (size - (x - size)))
            sb.write("\n")

    # Trosième partie du losange.
    # Pour toutes les lignes de cette partie, on va dessiner plus ou moins de 0 et de 1 en fonction de la ligne, le nombre de 1 diminue et de 0 augmente lorsque le nombre d'itérations augmente.
    for x in range(int(size / (3 * 2))):
        sb.write("0" * (x + 1))
        sb.write("1" * (size - (x + 1) * 2))
        sb.write("0" * (x + 1))
        sb.write("\n")

    return add_space(sb.getvalue())
