"""Fichier contenant des fonctions permettant d'intéragir avec des fichiers.
@project Tetris
"""
import os
import json
from io import StringIO
from utils import references
from utils.references import BlockType, GridType


def get_base_path() -> str:
    """Obtient le chemin d'accès du dossier du projet.

    :return: Le chemin d'accès.
    :rtype: Str.

    """
    return os.getcwd()


def get_resources_path() -> str:
    """Obtient le chemin d'accès vers le dossier des ressources du projet.

    :return: Le chemin d'accès.
    :rtype: Str.

    """
    return os.path.join(get_base_path(), "resources")


def get_saves_path() -> str:
    """Obtient le chemin d'accès vers le dossier des sauvegardes.

    :return: Le chemin d'accès.
    :rtype: Str.

    """
    return os.path.join(get_resources_path(), "saves")


def get_maps_path() -> str:
    """Obtient le chemin d'accès vers le dossier des cartes.

    :return: Le chemin d'accès.
    :rtype: Str.

    """
    return os.path.join(get_resources_path(), "maps")


def save_grid(path: str, grid: GridType) -> None:
    """Sauvegarde la grille en tant que string dans un fichier.

    La grille va être sauvegardée comme un string composé de 0, de 1, d'espaces et de sauts de ligne.
    Les 0 représentent les points en dehors de la carte et les 1 les points à l'intérieur de la carte.

    :param path: Chemin d'accès du fichier.
    :param grid: Grid est une matrice (elle peut être vue comme une carte vièrge où aucune partie ne s'est déroulée).

    """

    with open(path, "w") as file:
        grid_sb = StringIO()
        for line in grid:
            for i, char in enumerate(line):
                # On ajoute au string le charactère suivis d'un espace.
                grid_sb.write(char + " " if i + 1 < len(line) else char)
            grid_sb.write("\n")
        # On écrit le string de la grille dans le fichier en sans le dernier saut de ligne.
        file.write(grid_sb.getvalue()[:-1])


def read_grid(path: str) -> GridType:
    """Lis un fichier et retourne une matrice.

    :param path: Le chemin d'accès vers le fichier à lire.

    :return: Une matrice.
    :rtype: list[list[str]].

    """
    with open(path, 'r') as file:
        matrice: GridType = []
        [matrice.append(line.replace("\n", "").split(" ")) for line in file.readlines()]
        return matrice


def load_blocs() -> list[list[BlockType]]:
    """Lis tous les blocs d'un dossier, les contertis tous en matrice et les retourne tous dans une liste.

    :return: Tous les blocs dans une liste.
    :rtype: list[list[BlockType]].

    """
    map_blocks: dict[str, list[BlockType]] = {}

    # Pour tous les dossiers dans le dossier des blocs.
    for directory in os.listdir(get_resources_path() + "/blocks"):
        blocks: list[BlockType] = []

        # Pour tous les fichiers dans les dossiers.
        for file in os.listdir(get_resources_path() + "/blocks/" + directory):
            with open(get_resources_path() + "/blocks/" + directory + "/" + file, "r") as opened_file:
                bloc_matrice: BlockType = []

                # Le fichier est convertis en matrice
                for line in opened_file.readlines():
                    line_list: list[str] = [char for char in line if char != " " and char != "\n"]
                    bloc_matrice.append(line_list)
                blocks.append(bloc_matrice)

        map_blocks[directory] = blocks

    return [map_blocks["common"], map_blocks["cercle"], map_blocks["losange"], map_blocks["triangle"]]


def file_exists(path: str) -> bool:
    """Vérifie si un fichier existe.

    :param path: Le chemin d'accès du fichier à vérifier.
    :type path: Str.

    :return: Vrai si le fichier existe et non s'il n'existe pas.
    :rtype: Bool.

    """
    return os.path.exists(path)


def save_game(file_name: str, grid: GridType, score: int) -> None:
    """Sauvegarde une partie comme un fichier json.

    Le fichier sera obligatoirement sauvegardé dans le dossier des sauvegardes.

    :param file_name: Le nom du fichier.
    :param grid: La grille de la partie.
    :param score: Le score de la partie.

    """

    # On met les informations dans un dictionnaire.
    game_dict = {"grid_matrice": grid, "score": score, "settings": references.settings}
    # On convertit le dictionnaire en fichier json.
    json.dump(game_dict, open(get_saves_path() + "/" + file_name + ".json", "w"))


def load_game_json(save: int) -> dict[str, GridType | int | dict[str, str | int]]:
    """Chage une partie à partie d'un fichier json et la retourne en tant que dictionnaire.

    :param save: L'index du fichier à charger dans le dossier des sauvegardes.

    :return: Un dictionnaire contenant les informations de la partie comme les paramètres, la grille et le score.
    :rtype: dict[str, GridType | int | dict[str, str | int]].

    """
    # On convertit le fichier json en dictionnaire.
    return json.load(open(get_saves_path() + "/" + os.listdir(get_saves_path())[save]))


def create_game_directories() -> None:
    """Créé les dossiers nécessaires au bon fonctionnement du jeu."""
    if not file_exists(get_saves_path()):
        os.mkdir(get_saves_path())
    if not file_exists(get_maps_path()):
        os.mkdir(get_maps_path())
