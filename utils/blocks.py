"""Fichier contenant des fonctions permettant d'intéragir avec les blocs.
@project Tetris
"""
import random
from io import StringIO
from utils import references, grids
from utils.files import load_blocs
from utils.references import BlockType


def select_blocks() -> list[BlockType]:
    """Selectionne les blocs en fonction du régime de choix de blocs et les retourne.

    :return: Une liste de matrice.
    :rtype: List[BlockType].

    """
    blocks: list[BlockType] = []

    # Charge tous les blocs possibles dans cette carte.
    available_blocks: list[list[BlockType]] = grids.get_blocs(references.settings["shape"], load_blocs())

    if references.settings["bloc_placement"] == 1:
        # Les blocs sont tous ajouter dans une nouvelle liste.
        for liste in available_blocks:
            blocks += liste
    elif references.settings["bloc_placement"] == 2:
        temp_list: list[dict[str, str | list[list[str]]]] = []
        # Les blocs sont tous ajouter dans une nouvelle liste.
        for liste in available_blocks:
            temp_list += liste

        # On choisit 3 blocs différents de manière aléatoire dans la liste de blocs.
        for i in range(3):
            while True:
                choice = random.choice(temp_list)
                if choice not in blocks:
                    blocks.append(random.choice(temp_list))
                    break
    return blocks


def block_to_string(block: BlockType) -> str:
    """Convertis une matrice en string.

    :param block: Matrice du bloc à convertir en string.

    :return: La matrice en string.
    :rtype: Str.

    """
    sb: StringIO = StringIO()
    for line in block:
        for char in line:
            # Ajoute le caractère de bloc si le caractère de base était un 1 (donc que le caractère composait le bloc).
            sb.write(references.blocs_char + " " if char == "1" else "  ")
        sb.write("\n")
    return sb.getvalue()
