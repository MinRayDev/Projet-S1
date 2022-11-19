import os
import json
from typing import List, Dict, Union
from utils import References


def save_grid(path: str, grid: List[List[str]]) -> None:
    """Save grid as string in a file.

    The grid will be saved as a string of characters with 0s, 1s, spaces and line breaks.
    The 0s are the points outside the map and the 1s are the points inside the map.

    :param path: path of the file.
    :param grid: grid is a matrice.

    """
    file = open(path, "w")
    grid_string: str = ""

    for line in grid:
        for i, char in enumerate(line):
            grid_string += char + " " if i + 1 < len(line) else char

        grid_string += "\n"

    file.write(grid_string[:-1])
    file.close()


def read_grid(path: str) -> List[List[str]]:
    """Read a grid file and return the grid as a matrice.

    :param path: The path to the file to read.
    :return: The grid as a matrice.

    """
    file = open(path, 'r')
    matrice: List[List[str]] = []
    [matrice.append(line.replace("\n", "").split(" ")) for line in file.readlines()]
    file.close()
    return matrice


def load_blocs() -> Dict[str, List[Dict[str, Union[str, List[List[str]]]]]]:
    """Read all blocs from directories, convert them to matrice and return all of them in a List.

        All blocs are stored in different directories, so the function read all files in these directories and convert their contents into blocs,
        blocs are dictionary dict(str, str | List[List|str]]). All blocs that are in the same directory are stored in the same List it-self is store in a dictionary,
        the key is the name of the directory.

        :return: All blocs in a List.

    """
    dictionary: Dict[str, List[Dict[str, Union[str, List[List[str]]]]]] = {}

    for directory in os.listdir(get_resources_path() + "\\blocks"):
        blocs: List[Dict[str, Union[str, List[List[str]]]]] = []

        for file in os.listdir(get_resources_path() + "\\blocks\\" + directory):
            opened_file = open(get_resources_path() + "\\blocks\\" + directory + "\\" + file, "r")
            matrice: List[List[str]] = []

            for line in opened_file.readlines():
                line_list: List[str] = []
                [line_list.append(char) for char in line if char != " " and char != "\n"]
                # for char in line:
                #     if char != " " and char != "\n":
                #         line_list.append(char)
                matrice.append(line_list)

            blocs.append({"name": file[:-4], "matrice": matrice})

        dictionary[directory] = blocs

    return dictionary


def file_exists(path) -> bool:
    """Check if a file exists and return it.

    :param path: path to the file to check.

    :return: True if the file exists and False otherwise.

    """
    return os.path.exists(path)


def save_game(file_name: str, grid: List[List[str]], score: int) -> None:
    """Save a game as a json file.

    The file will necessarily be saved in the saves' directory.

    :param file_name: The name of the file to save.
    :param grid: grid of the game.
    :param score: score of the game.

    """
    game_dict = {"grid_matrice": grid, "score": score, "settings": References.settings}
    json.dump(game_dict, open(get_saves_path() + "\\" + file_name + ".json", "w"))


def load_game(save: int):
    """Load a game from a json file and return it as a dictionary.

    :param save: The index of the game to load in the saves' directory.
    :return: A dictionary containing the game information as the grid, the score or the settings dictionary.

    """
    return json.load(open(get_saves_path() + "\\" + os.listdir(get_saves_path())[save]))


def get_base_path() -> str:
    """Get path to the base directory of the project.

    :return: The path.

    """
    return os.path.join(os.path.dirname(__file__).split("utils")[0])


def get_resources_path():
    """Get path to the resources directory of the project.

    :return: The path.

    """
    return get_base_path() + "\\resources"


def get_saves_path():
    """Get path to the saves directory of the project.

    :return: The path.

    """
    return get_resources_path() + "\\saves"


def get_maps_path():
    """Get path to the maps directory of the project.

    :return: The path.

    """
    return get_resources_path() + "\\maps"
