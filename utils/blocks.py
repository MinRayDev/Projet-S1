"""Fichier contenant des fonctions permettant d'intéragir avec les blocs.
@project Tetris
@author Gauthier
@author Marielle
"""
import random
from typing import List, Dict, Union
from utils import references, grids
from utils.files import load_blocs


def select_blocks() -> List[List[List[str]]]:
    """Selectionne les blocs en fonction du régime de choix de blocs et les retourne.

    :return: Une liste de matrice.
    :rtype: List[List[List[str]]].

    """
    list_to_return: List[List[List[str]]] = []

    # Charge tous les blocs possibles dans cette carte.
    blocs_liste = grids.get_blocs(references.settings["shape"], load_blocs())

    if references.settings["bloc_placement"] == 1:
        # Les blocs sont tous ajouter dans une nouvelle liste.
        for liste in blocs_liste:
            list_to_return += liste
    elif references.settings["bloc_placement"] == 2:
        temp_list: List[Dict[str, Union[str, List[List[str]]]]] = []
        # Les blocs sont tous ajouter dans une nouvelle liste.
        for liste in blocs_liste:
            temp_list += liste

        # On choisis 3 blocs différents de manière aléatoire dans la liste de blocs.
        for i in range(3):
            while True:
                choice = random.choice(temp_list)
                if choice not in list_to_return:
                    list_to_return.append(random.choice(temp_list))
                    break
    return list_to_return


def block_to_string(matrice: List[List[str]]) -> str:
    """Convertis une matrice en string.

    :param matrice: Matrice du bloc à convertir en string.

    :return: La matrice en string.
    :rtype: str

    """
    string_to_return = ""
    for line in matrice:
        for char in line:
            # Ajoute le caractère de bloc si le caractère de base était un 1 (donc que le caractère composait le bloc).
            string_to_return += references.blocs_char + " " if char == "1" else "  "
        string_to_return += "\n"
    return string_to_return
