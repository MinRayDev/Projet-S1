"""Fichier avec toutes les fonctions permettant d'intéragir avec les grilles de jeu.
@project Tetris
@author Gauthier
@author Marielle
"""
from typing import List, Tuple

from utils import references
from utils.terminal import draw


# todo
def draw_grid(grid: List[List[str]], x: int, y: int) -> None:
    """Dessine une grille.

    :param grid: Matrice de la grille.
    :param x: Position x.
    :param y: Position y.

    :rtype: None.

    """
    for i, line in enumerate(grid):
        string = ""
        for co in line:
            string += " ⬝" if co == "1" else "  "
        draw(string, x, y + i)


def get_blocs(grid_type: str, all_blocs: List[List[List[List[str]]]]) -> List[List[List[List[str]]]]:
    """Donne la liste entioère des blocs utilisables dans une forme de carte.

    :param grid_type: Type de la grille.
    :param all_blocs: Liste des blocs.

    :return: Liste des blocs utilisables.
    :rtype: List[List[List[List[str]]]].

    """
    for i in range(3):
        if grid_type == references.GRID_TYPES[i]:
            return [all_blocs[0] + all_blocs[i + 1]]
    return [all_blocs[0]]


def get_size(grid: List[List[str]]) -> Tuple[int, int]:
    """Donne la taille d'une grille.

    :param grid: Matrice de la grille.

    :return: Taille de la grille (longueur, hauteur).
    :rtype: Tuple[int, int].

    """
    height = len(grid)
    width = len(grid[0])
    return width, height


def convert_grid(string_matrice: str) -> List[List[str]]:
    """Convertis un string en une matrice.

    :param string_matrice: String à convertir.

    :return: Une matrice.
    :rtype: List[List[str]].

    """
    matrice: List[List[str]] = []
    for line in string_matrice.split("\n"):
        if len(line) > 0:
            line_list = []
            for char in line.replace(" ", ""):
                line_list.append(char)
            matrice.append(line_list)
    return matrice


def emplace_bloc(grid: List[List[str]], block: List[List[str]], i: int, j: int) -> List[List[str]]:
    """Place un bloc sur une grille.

    :param grid: Grille où placer le bloc.
    :param block: Bloc à placer.
    :param i: Coordonnées où placer le bloc.
    :param j: Coordonnées où placer le bloc.

    :return: La matrice avec le bloc placé.
    :rtype: List[List[str]].

    """
    bloc_parts = []
    for y_, y in enumerate(block):
        for x_, x in enumerate(y):
            if x == "1":
                bloc_parts.append((len(block) - y_ - 1, x_))
    for bloc_part in bloc_parts:
        grid[j - bloc_part[0]].pop(i + bloc_part[1])
        grid[j - bloc_part[0]].insert(i + bloc_part[1], "2")
    return grid


def valid_position(grid, block, i, j) -> bool:
    """Vérifie si un bloc peut être placer sur une grille.

    :param grid: Grille où placer le bloc.
    :param block: Bloc à placer.
    :param i: Coordonnées où placer le bloc.
    :param j: Coordonnées où placer le bloc.

    :return: True s'il peut être placer, False sinon.
    :rtype: bool.

    """
    bloc_parts = []
    for y_, y in enumerate(block):
        for x_, x in enumerate(y):
            if x == "1":
                bloc_parts.append((len(block) - y_ - 1, x_))
    for bloc_part in bloc_parts:
        if (j - bloc_part[0] < 0) or (i + bloc_part[1] >= len(grid[j - bloc_part[0]])):
            return False
        if grid[j - bloc_part[0]][i + bloc_part[1]] == "2" or \
                grid[j - bloc_part[0]][i + bloc_part[1]] == "0":
            return False
    return True


def row_state(grid, i) -> bool:
    """Vérifie si une ligne est pleine.

    :param grid: Grille contenant la ligne.
    :param i: Index de la ligne à vérifier.

    :return: True si remplie, False sinon.
    :rtype: bool.

    """
    for x in grid[i]:
        if x == "1":
            return False
    return True


def col_state(grid, j) -> bool:
    """Vérifie si une colonne est pleine.

    :param grid: Grille contenant la colonne.
    :param j: Index de la colonne à vérifier.

    :return: True si remplie, False sinon.
    :rtype: bool.

    """
    col = []
    for line in grid:
        col.append(line[j])
    for y in col:
        if y == "1":
            return False
    return True


def row_clear(grid: List[List[str]], i: int) -> int:
    """Vide une ligne et retourne le nombre de blocs supprimés.

    :param grid: Grille contenant la ligne.
    :param i: Index de la ligne à supprimer.

    :return: Nombre de blocs supprimés.
    :rtype: int.

    """
    score: int = 0
    for j, x in enumerate(grid[i]):
        if x == "2":
            references.grid_matrice[i].pop(j)
            references.grid_matrice[i].insert(j, "1")
            score += 1
    return score


def col_clear(grid: List[List[str]], j: int) -> int:
    """Vide une colonne et retourne le nombre de blocs supprimés.

    :param grid: Grille contenant la colonne.
    :param j: Index de la colonne à supprimer.

    :return: Nombre de blocs supprimés.
    :rtype: int.

    """
    score: int = 0
    for i, line in enumerate(grid):
        if line[j] == "2":
            references.grid_matrice[i].pop(j)
            references.grid_matrice[i].insert(j, "1")
            score += 1
    return score
