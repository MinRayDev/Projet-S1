"""Fichier avec toutes les fonctions permettant d'intéragir de manière plus simple avec le terminal.
@project Tetris
@author Gauthier
@author Marielle
"""
import os
import sys
from typing import Tuple
from utils import colors


def clear_game_console() -> None:
    """Vide la console de jeu.

    :rtype: None.

    """
    clear_area(get_window_size()[0] - 15, get_window_size()[1] - 6, get_window_size()[0] - 1, get_window_size()[1] - 1)


def draw(text: str, x: int, y: int, color: str = colors.WHITE) -> None:
    """Dessine un texte dans le terminal.

    :param text: Texte à dessiner.
    :param x: Position sur l'axe x où dessiner.
    :param y: Position sur l'axe y où dessiner.
    :param color: (optionnel) Couleur du texte.

    :rtype: None.

    """
    # \033[{y};{x}H pour mettre le curseur à la position x, y, end='' pour qu'il n'y ait pas de saut de ligne, flush=True pour forcer le print directement.
    print(f"\033[{y};{x}H{color}{text}", end='', flush=True)


def draw_centered(text: str, y_dist: int = 0, color: str = colors.WHITE) -> None:
    """Dessine un texte par rapport au centre du terminal.

    :param text: Texte à dessiner.
    :param y_dist: Distance sur l'axe y du centre de la hauteur du terminal.
    :param color: (optionnel) Couleur du texte.

    :rtype: None.

    """
    window_width, window_height = get_window_size()
    # Dessine le texte de manbière centré en retirant la moitié de la longueur du texte à la moitié de la longueur du terminal.
    draw(text, ((window_width // 2) - (len(text) // 2)), (window_height // 2) + y_dist, color)


def clear_area(x: int, y: int, width: int, height: int) -> None:
    """Vide une zone.

    :param x: Position sur l'axe x où la zone commence.
    :param y: Position sur l'axe y où la zone commence.
    :param width: Longueur de la zone.
    :param height: Hauteur de la zone.

    :rtype: None.

    """

    for i in range(x, x + width):
        for j in range(y, y + height):
            # Remplace le caractère par un espace (pour qu'il soit visuellement vide) aux coordonnées i, j.
            draw(" ", i, j)


def set_cursor(x: int, y: int) -> None:
    """Place le curseur d'écriture aux coordonnées x, y.

    :param x: Position sur l'axe x où dessiner.
    :param y: Position sur l'axe y où dessiner.

    :rtype: None.

    """
    # Dessine un caractère vide (pour que le caractère aux coordonnées ne soit pas remplacé par un caractère vide comme avec un espace) aux coordonnées x, y.
    draw("", x, y)


def clear() -> None:
    """Vide le terminal.
    
    :rtype: None.
    
    """
    if "win" in sys.platform:
        # Si l'os de l'utilsateur est windows la commande "cls" est utilisée.
        os.system("cls")
    else:
        # Sinon le terminal est vidé en utilisant la fonction clear_area.
        os.system("clear")


def draw_frame(x: int, y: int, width: int, height: int) -> Tuple[int, int]:
    """Dessine un cadre et retourne les coordonnées x, y à l'intérieur du cadre.

    :param x: coordonné x où dessiner.
    :param y: coordonné y où dessiner.
    :param width: longueur du cadre.
    :param height: hauteur du cadre.

    :return: coordonnées à l'intérieur du cadre (x, y).
    :rtype: Tuple[int, int].

    """
    # Dessine les 4 coins du cadre.
    draw("╔", x, y)
    draw("╗", x + width, y)
    draw("╚", x, y + height)
    draw("╝", x + width, y + height)

    # Dessine pour toutes les colonnes du cadre, des "=" en haut et en bas du cadre.
    for i in range(x + 1, x + width):
        draw("═", i, y)
        draw("═", i, y + height)

    # Dessine pour toutes les lignes du cadre, des "=" à droite et à gauche du cadre.
    for j in range(y + 1, y + height):
        draw("║", x, j)
        draw("║", x + width, j)

    return x + 1, y + 1


def draw_ascii_art(file_path: str, x: int, y: int, color: str = colors.WHITE) -> None:
    """Dessine un ASCII art.

    :param file_path: Chemin d'accès du fichier à dessiner.
    :param x: coordonné x où dessiner.
    :param y: coordonné y où dessiner.
    :param color: (optionnel) Couleur du texte.

    :rtype: None.

    """

    # Pour toutes les lignes du String de l'ASCII art dessiner la ligne et descendre à chaque itération afin de restituer l'ASCII art.
    for i, line in enumerate(open(file_path, "r").readlines()):
        draw(line.replace("\n", ""), x, y + i, color)


def get_window_size() -> Tuple[int, int]:
    """Obtient et retourne la taille du terminal.

    :return: Taille du terminal (x, y).
    :rtype: Tuple[int, int].

    """
    return os.get_terminal_size()


def get_window_width_center() -> int:
    """Obtient et retourne le centre de la longueur du terminal.

    :rtype: None.

    """
    return os.get_terminal_size()[0] // 2


def get_window_height_center() -> int:
    """Obtient et retourne le centre de la hauteur du terminal.

    :rtype: None.

    """
    return os.get_terminal_size()[1] // 2
