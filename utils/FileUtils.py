import os

from utils import References


def load_blocks() -> dict:
    dictionary: dict = {}
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
