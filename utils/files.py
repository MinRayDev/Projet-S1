"""Fichier contenant des fonctions permettant d'intéragir avec des fichiers.
@project Tetris
@author Gauthier
@author Marielle
"""
import os
import json
from typing import List, Dict
from utils import references


def get_base_path() -> str:
    """Obtient le chemin d'accès du dossier du projet.

    :return: Le chemin d'accès.
    :rtype: str.

    """
    return os.getcwd()


def get_resources_path() -> str:
    """Obtient le chemin d'accès vers le dossier des ressources du projet.

    :return: Le chemin d'accès.
    :rtype: str.

    """
    return get_base_path() + "/resources"


def get_saves_path() -> str:
    """Obtient le chemin d'accès vers le dossier des sauvegardes.

    :return: Le chemin d'accès.
    :rtype: str.

    """
    return get_resources_path() + "/saves"


def get_maps_path() -> str:
    """Obtient le chemin d'accès vers le dossier des cartes.

    :return: Le chemin d'accès.
    :rtype: str.

    """
    return get_resources_path() + "/maps"


def save_grid(path: str, grid: List[List[str]]) -> None:
    """Sauvegarde la grille en tant que string dans un fichier.

    La grille va être sauvegardée comme un string composé de 0, de 1, d'espaces et de sauts de ligne.
    Les 0 représentent les points en dehors de la carte et les 1 les points à l'intérieur de la carte.

    :param path: Chemin d'accès du fichier.
    :param grid: grid est une matrice (elle peut être vue comme une carte vièrge où aucune partie ne s'est déroulée).

    :rtype: None.

    """

    with open(path, "w") as file:
        grid_string: str = ""

        for line in grid:
            for i, char in enumerate(line):
                # On ajoute au string le charactère suivis d'un espace.
                grid_string += char + " " if i + 1 < len(line) else char
            grid_string += "\n"

        # On écrit le string de la grille dans le fichier en sans le dernier saut de ligne.
        file.write(grid_string[:-1])


def read_grid(path: str) -> List[List[str]]:
    """Lis un fichier et retourne une matrice.

    :param path: Le chemin d'accès vers le fichier à lire.

    :return: Une matrice.
    :rtype: List[List[str]].

    """
    with open(path, 'r')as file:
        matrice: List[List[str]] = []
        [matrice.append(line.replace("\n", "").split(" ")) for line in file.readlines()]
        return matrice


def load_blocs() -> List[List[List[List[str]]]]:
    """Lis tous les blocs d'un dossier, les contertis tous en matrice et les retournes tous dans une liste.

    :return: Tous les blocs dans une liste.
    :rtype: List[List[List[List[str]]]].

    """
    dictionary: Dict[str, List[List[List[str]]]] = {}

    # Pour tous les dossiers dans le dossier des blocs.
    for directory in os.listdir(get_resources_path() + "/blocks"):
        blocs: List[List[List[str]]] = []

        # Pour tous les fichiers dans les dossiers.
        for file in os.listdir(get_resources_path() + "/blocks/" + directory):

            opened_file = open(get_resources_path() + "/blocks/" + directory + "/" + file, "r")
            matrice: List[List[str]] = []

            # Le fichier est convertis en matrice
            for line in opened_file.readlines():
                line_list: List[str] = [char for char in line if char != " " and char != "\n"]
                matrice.append(line_list)

            blocs.append(matrice)

        dictionary[directory] = blocs

    return [dictionary["common"], dictionary["cercle"], dictionary["losange"], dictionary["triangle"]]


def file_exists(path) -> bool:
    """Vérifie si un fichier existe.

    :param path: Le chemin d'accès du fichier à vérifier.

    :return: Vrai si le fichier existe et non s'il n'existe pas.
    :rtype: bool.

    """
    return os.path.exists(path)


def save_game(file_name: str, grid: List[List[str]], score: int) -> None:
    """Sauvegarde une partie comme un fichier json.

    Le fichier sera obligatoirement sauvegardé dans le dossier des sauvegardes.

    :param file_name: Le nom du fichier.
    :param grid: La grille de la partie.
    :param score: Le score de la partie.

    :rtype: None.

    """

    # On met les informations dans un dictionnaire.
    game_dict = {"grid_matrice": grid, "score": score, "settings": references.settings}
    # On convertis le dictionnaire en fichier json.
    json.dump(game_dict, open(get_saves_path() + "/" + file_name + ".json", "w"))


def load_game_json(save: int) -> Dict:
    """Chage une partie à partie d'un fichier json et la retourne en tant que dictionnaire.

    :param save: L'index du fichier à charger dans le dossier des sauvegardes.

    :return: Un dictionnaire contenant les informations de la partie comme les paramètres, la grille et le score.
    :rtype: Dict.

    """
    # On convertis le fichier json en dictionnaire.
    return json.load(open(get_saves_path() + "/" + os.listdir(get_saves_path())[save]))


def create_game_directories() -> None:
    """Créé les dossiers nécessaires au bon fonctionnement du jeu.

    :rtype: None.

    """
    if not file_exists(get_saves_path()):
        os.mkdir(get_saves_path())
    if not file_exists(get_maps_path()):
        os.mkdir(get_maps_path())
