import os
import json

from typing import List

from utils import References


def save_grid(path: str, grid: List[List[str]]) -> None:
    file = open(path, "w")
    string = ""
    for line in grid:
        print("a")
        print(len(line))
        for i, char in enumerate(line):
            print(i)
            if i + 1 < len(line):
                string += char + " "
            else:
                string += char
        string += "\n"
    file.write(string[:-1])
    file.close()


def read_grid(path) -> List[List[str]]:
    file = open(path, 'r')
    matrice = []
    for line in file.readlines():
        matrice.append(line.replace("\n", "").split(" "))
    file.close()
    return matrice


def load_blocks():
    dictionary = {}
    for dir_ in os.listdir(References.base_path + "\\resources\\blocks"):
        blocks = []
        for file in os.listdir(References.base_path + "\\resources\\blocks\\" + dir_):
            opened_file = open(References.base_path + "\\resources\\blocks\\" + dir_ + "\\" + file, "r")
            matrice = []
            for line in opened_file.readlines():
                l_matrice = []
                for char in line:
                    if char != " " and char != "\n":
                        l_matrice.append(char)
                matrice.append(l_matrice)
            block = {"name": file[:-4], "matrice": matrice}
            blocks.append(block)
        dictionary[dir_] = blocks
    return dictionary


def file_exists(path) -> bool:
    return os.path.exists(path)


def save_game(file_name: str, grid: List[List[str]], score: int):
    dict_save = {"grid_matrice": grid, "score": score, "settings": References.settings}
    file = open(References.base_path + "\\resources\\saves\\" + file_name + ".json", "w")
    file.write(json.dumps(dict_save))
    file.close()
