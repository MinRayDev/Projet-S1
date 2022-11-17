from typing import List, Tuple

from utils import References, DebugUtils
from utils.TerminalUtils import *


def draw_grid(grid, x, y):
    i = 0
    for line in grid:
        string = ""
        for co in line:
            if co == "0":
                co = " "
            elif co == "1":
                co = "⬝"
            string += " "
            string += co
        draw(string, x, y + i)
        i += 1


def bloc_to_string(matrice):
    string_to_return = ""
    for line in matrice:
        for co in line:
            if co == "0":
                co = " "
            elif co == "1":
                co = "■"
            string_to_return += co + " "
        string_to_return += "\n"
    return string_to_return


def get_blocs(grid_type: str) -> List[List[str]]:
    to_return: List[List[str]] = [References.common_liste]
    if grid_type == "cercle":
        to_return.append(References.cercle_liste)
    elif grid_type == "losange":
        to_return.append(References.losange_liste)
    elif grid_type == "triangle":
        to_return.append(References.triangle_liste)
    return to_return


def get_size(grid: List[List[str]]) -> Tuple[int, int]:
    height = len(grid)
    width = len(grid[0])
    return width, height


def load_grid(string_shape: str) -> List[List[str]]:
    matrice: List[List[str]] = []
    for line in string_shape.split("\n"):
        if len(line) > 0:
            t = []
            for char in line.replace(" ", ""):
                t.append(char)
            matrice.append(t)
    return matrice


def emplace_bloc(grid, bloc, i, j):
    bloc_parts = []
    for y_, y in enumerate(bloc):
        for x_, x in enumerate(y):
            if x == "1":
                bloc_parts.append((len(bloc) - y_ - 1, x_))
    for bloc_part in bloc_parts:
        References.grid["matrice"][j - bloc_part[0]].pop(i + bloc_part[1])
        References.grid["matrice"][j - bloc_part[0]].insert(i + bloc_part[1], "2")


def valid_position(grid, bloc, i, j) -> bool:
    bloc_parts = []
    for y_, y in enumerate(bloc):
        for x_, x in enumerate(y):
            if x == "1":
                bloc_parts.append((len(bloc) - y_ - 1, x_))
    for bloc_part in bloc_parts:
        if (j - bloc_part[0] < 0) or (i + bloc_part[1] >= len(References.grid["matrice"][j - bloc_part[0]])):
            return False
        if References.grid["matrice"][j - bloc_part[0]][i + bloc_part[1]] == "2" or References.grid["matrice"][j - bloc_part[0]][i + bloc_part[1]] == "0":
            return False
    return True


def row_state(grid, i) -> bool:
    for x in grid[i]:
        if x == "1":
            return False
    return True


def col_state(grid, j) -> bool:
    col = []
    for line in grid:
        col.append(line[j])
    for y in col:
        if y == "1":
            return False
    return True


def row_clear(grid, i) -> int:
    score: int = 0
    for j, x in enumerate(grid[i]):
        if x == "2":
            References.grid["matrice"][i].pop(j)
            References.grid["matrice"][i].insert(j, "1")
            score += 1
    return score


def col_clear(grid, j) -> int:
    score: int = 0
    for i, line in enumerate(grid):
        if line[j] == "2":
            References.grid["matrice"][i].pop(j)
            References.grid["matrice"][i].insert(j, "1")
            score += 1
    return score
