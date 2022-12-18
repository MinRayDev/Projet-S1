"""Fichier avec toutes les fonctions permettant d'afficher des notifications de jeu et de menu.
@project Tetris
@author Gauthier
@author Marielle
"""
from utils import references, colors, grids
from utils.terminal import draw, draw_frame, draw_centered, get_window_width_center, get_window_height_center, clear_area


def game_notification(text: str, color: str = colors.WHITE) -> None:
    """Dessine une notification.

    Dans ce programme une notification est générée en dessinant un cadre et un texte à l'intérieur.
    :param text: Texte dans la notification.
    :param color: (optionnel) Couleur du texte.

    :rtype: None.

    """
    x, y = draw_frame(4 + (grids.get_size(references.grid_matrice)[0] * 2) + 40, 2, 45, 2)
    draw(text, x + 1, y, color)


def menu_notification(text: str, y_dist: int, color: str = colors.WHITE) -> None:
    """Dessine une notification par rapport au centre du terminal.

    :param text: Texte de la notification.
    :param y_dist: Distance de l'axe y de la notification par rapport au centre de la hauteur du terminal.
    :param color: (optionnel) Couleur du texte.

    :rtype: None.

     """
    draw_centered(text, y_dist, color)
    draw_frame(get_window_width_center() - (len(text) // 2) - 2, get_window_height_center() + y_dist - 1, len(text) + 4, 2)


def alert(text: str) -> None:
    """Dessine une notification en rouge sombre.

    :param text: Texte de la notification.

    :rtype: None.

    """
    game_notification(text, colors.DARK_RED)


def warn(text: str) -> None:
    """Dessine une notification en jaune sombre.

    :param text: Texte de la notification.

    :rtype: None.

    """
    game_notification(text, colors.DARK_YELLOW)


def clear_notification() -> None:
    """Vide la zone de notification.

    :rtype: None.

    """
    clear_area(4 + (grids.get_size(references.grid_matrice)[0] * 2) + 40, 2, 46, 4)
