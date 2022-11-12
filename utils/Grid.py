import utils.References as References
from utils.TerminalUtils import *


def save_grid(path):
    pass  # TODO: save


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


def read_grid(path):
    file = open(path, 'r')
    matrice = []
    for line in file.readlines():
        matrice.append(line.replace("\n", "").split(" "))
    return matrice


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


def print_blocs(grid):
    to_return = [References.common_liste]
    if References.settings["shape"] == "cercle":
        to_return.append(References.cercle_liste)
    elif References.settings["shape"] == "losange":
        to_return.append(References.losange_liste)
    elif References.settings["shape"] == "triangle":
        to_return.append(References.triangle_liste)
    return to_return


def get_size(grid):
    height = len(grid)
    width = len(grid[0])
    return width, height


def load_grid(string_shape: str):
    matrice = []
    for line in string_shape.split("\n"):
        if len(line) > 0:
            t = []
            for char in line.replace(" ", ""):
                t.append(char)
            matrice.append(t)
    return matrice
