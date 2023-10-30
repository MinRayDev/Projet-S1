"""Fichier avec une grande partie du fonctionnement du jeu, l'affichage du jeu, l'affichage du menu interne au jeu.
@project Tetris
"""
import os
from typing import Optional

from utils.menus import rules
from utils.references import BlockType, GridType
from utils.terminal import clear, draw_ascii_art, get_window_width_center, get_window_height_center, draw_centered, \
    draw, get_window_size, draw_frame, clear_game_console, set_cursor, clear_area
from utils import references, colors, grids, blocks, numbers
from utils.files import get_resources_path, save_game
from utils.notifications import alert, clear_notification, menu_notification


def stop(selected: bool = False) -> None:
    """Arrête la partie en cours.

    :param selected: True si le joueur a choisi d'arrêter la partie, False s'il n'a pas choisi.

    """
    color = colors.DARK_GREEN if selected else colors.DARK_RED
    # Dessine le menu.
    clear()
    draw_ascii_art(get_resources_path() + "/end_screen.txt", get_window_width_center() - (55 // 2),
                   get_window_height_center() - 8, color)
    draw_centered("Score: " + str(references.score))
    draw_centered("Appuyez sur n'importe quelle touche pour continuer...", 10)

    input()
    clear()
    exit()


def print_grid(grid: list[list[str]]) -> None:
    """Dessine la grille.

    :param grid: matrice de la grille.

    :rtype: None

    """
    # Dessine le cadre et les lettres.
    width, height = grids.get_size(references.grid_matrice)
    for i, character in enumerate(references.game_letters):
        draw(character, (i * 2) + 5, 1)
    for i in range(width):
        draw("═", (i * 2) + 5, 2)
        draw("═", (i * 2) + 5, height + 3)
    draw("╔", 3, 2)
    draw("╗", (width * 2) + 5, 2)
    draw("╚", 3, height + 3)
    draw("╝", (width * 2) + 5, height + 3)

    # Dessine la grille et les côtés du cadre.
    for i, line in enumerate(grid):
        draw(str(references.game_letters[i]).upper(), 1, i + 3)
        draw("║", 3, 3 + i)
        draw("║", (width * 2) + 5, i + 3)
        for j, co in enumerate(line):
            if co == "0":
                co = " "
            elif co == "1":
                co = "⬝"
            elif co == "2":
                co = references.blocs_char
            draw(co + " ", 5 + (j * 2), 3 + i)


def print_blocs(blocs_to_draw: list[list[list[str]]], selected: Optional[str] = None) -> None:
    """Dessine la grille.

    :param blocs_to_draw: Liste des matrices des blocs.
    :param selected: Bloc selectionné.

    :rtype: None

    """
    # Dessine les blocs
    width = grids.get_size(references.grid_matrice)[0]
    block_line: int = 0
    last_x: int = 4 + (width * 2) + 5
    last_list_size: int = 0
    for i, block in enumerate(blocs_to_draw):
        max_x: int = 0
        blocks_size_diff = 0
        # La variable blocks_size_diff varie pour que les blocks soient toujours alignés malgrés leurs tailles différentes (3, 4, 5)
        if len(block) == 5:
            blocks_size_diff = -1
        elif len(block) == 3:
            blocks_size_diff = 1
        for j, cube_line in enumerate(blocks.block_to_string(block).split("\n")):
            if len(cube_line) > 0:
                draw(cube_line, last_x, block_line + j + 6 + blocks_size_diff)
                if len(block[j]) == 0 or '1' not in block[j]:
                    continue
                nbx = max(idx for idx, val in enumerate(block[j]) if val == '1')
                if nbx > max_x:
                    max_x = nbx
        draw(str(i + 1 + last_list_size), last_x, block_line + len(block) + 7 + blocks_size_diff, colors.DARK_RED) if str(i + 1 + last_list_size) == selected else draw(str(i + 1 + last_list_size), last_x, block_line + len(block) + 7 + blocks_size_diff)
        last_x += max_x * 2 + 3
        if last_x >= get_window_size()[0] - 10:
            last_x = (width * 2) + 9
            block_line += 7


def update_score(count: int) -> int:
    """Incrémente le score et le retourne.

    :param count: Nombre à incrémenter.

    :return: Le score.
    :rtype: Int.

    """
    references.score += count
    return references.score


def draw_game(blocs_to_draw: list[BlockType]) -> None:
    """Dessine la partie (la grille, les blocs et le score).

    :param blocs_to_draw: Liste des blocs à dessiner.

    """
    width = grids.get_size(references.grid_matrice)[0]
    print_grid(references.grid_matrice)
    score_frame = draw_frame(4 + (width * 2) + 5, 2, 30, 2)
    draw(f"Score: {references.score}", score_frame[0], score_frame[1])
    print_blocs(blocs_to_draw)
    draw_frame(get_window_size()[0] - 16, get_window_size()[1] - 7, 16, 7)


def inputs(block_list: list[BlockType]) -> Optional[tuple[str, int, int]]:
    """Permet à l'utilisateur de selectionner les paramètres de sa partie.

    :param block_list: Liste des blocs.

    :return Les paramètres de la partie.
    :rtype: Optional[Tuple[str, int, int]] (Soit None, soit un Tuple[str, int, int]).

    """
    inputed_number = ""
    while not numbers.is_correct_number(inputed_number, 1, len(block_list)):
        clear_game_console()
        draw("Choisissez une", get_window_size()[0] - 15, get_window_size()[1] - 6)
        draw("forme: ", get_window_size()[0] - 15, get_window_size()[1] - 5)
        set_cursor(os.get_terminal_size()[0] - 8, os.get_terminal_size()[1] - 6 + 1)
        inputed_number = input()
        if inputed_number in references.STOP_WORDS:
            stop(True)
        elif inputed_number in references.MENU_WORDS:
            menu(references.grid_matrice)
            clear()
            return None
        if not numbers.is_correct_number(inputed_number, 1, len(block_list)):
            clear_notification()
            alert("Veuillez entrer un nombre valide !")
    clear_notification()
    clear_area(grids.get_size(references.grid_matrice)[0]*2+6, 5, get_window_size()[0], get_window_size()[1])
    print_blocs(block_list, inputed_number)
    draw_frame(get_window_size()[0] - 16, get_window_size()[1] - 7, 16, 7)
    x, y = " ", " "
    while x not in references.game_letters or y not in references.game_letters:
        clear_game_console()
        set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
        inputed_coos = input("x y: ")
        if inputed_coos in references.STOP_WORDS:
            stop(True)
        elif inputed_coos in references.MENU_WORDS:
            menu(references.grid_matrice)
            clear()
            return None
        elif " " not in inputed_coos:
            clear_notification()
            alert("Veuillez entrer des coordonnées valides !")
            continue
        x = inputed_coos.split(" ")[0]
        y = inputed_coos.split(" ")[1]
        if x not in references.game_letters or y not in references.game_letters:
            clear_notification()
            alert("Veuillez entrer des coordonnées valides !")
    clear_notification()
    set_cursor(get_window_size()[0] - 15, get_window_size()[1] - 6)
    return inputed_number, references.game_letters.index(x), references.game_letters.index(y)


def menu(grid: GridType) -> None:
    """Affiche le menu de jeu.

    :param grid: Grille de jeu.

    """
    while True:
        # Dessine le menu.
        clear()
        draw_frame(get_window_width_center() - 9, 1, 18, 4)
        draw_centered("Menu du jeu", -get_window_height_center()+3)

        draw_frame(get_window_width_center() // 2 - 18, get_window_height_center() - 9, 35, 20)
        for i, line in enumerate(
                open(get_resources_path() + "/save_icon.txt", "r", encoding="utf-8").readlines()):
            draw(line.replace("\n", ""), get_window_width_center() // 2 - 15, get_window_height_center() - 7 + i)
        draw("1. Sauvegarde", get_window_width_center() // 2 - len("1. Sauvegarde") // 2, get_window_height_center() - 9 + 20 - 3)

        draw_frame(get_window_width_center() - 18, get_window_height_center() - 9, 35, 20)
        for i, line in enumerate(
                open(get_resources_path() + "/rules_logo.txt", "r", encoding="utf-8").readlines()):
            draw(line.replace("\n", ""), get_window_width_center() - 14, get_window_height_center() - 7 + i)
        draw_centered("2. Règles", 8)

        x, y = draw_frame(get_window_width_center() + 18, get_window_height_center() - 9, 35, 6)
        draw("3. Paramètres visuels", x + 35 // 2 - len("3. Paramètres visuels") // 2, y + 2)

        x, y = draw_frame(get_window_width_center() + 18, get_window_height_center() - 2, 35, 6)
        draw("4. Stop", x + 35 // 2 - len("4. Stop") // 2, y + 2)

        x, y = draw_frame(get_window_width_center() + 18, get_window_height_center() + 5, 35, 6)
        draw("5. Retour", x + 35 // 2 - len("5. Retour") // 2, y + 2)

        draw_centered("Que voulez vous faire ?", 13)
        set_cursor(get_window_width_center(), get_window_height_center() + 15)

        # Choix de l'action.
        inputed: str = input()
        if inputed.lower() in references.SAVE_WORDS or inputed == "1":
            # Sauvegarde de la grille.
            clear_area(0, get_window_height_center() + 13, get_window_size()[0], get_window_size()[1])
            draw_centered("Entrez le nom du fichier:", 13)
            set_cursor(get_window_width_center(), get_window_height_center() + 15)
            inputed_file_name = input("")
            save_game(inputed_file_name, grid, references.score)
            clear()
        elif inputed.lower() in references.RULE_WORDS or inputed == "2":
            # Affiche les règles.
            rules()
            clear()
        elif inputed.lower() in ["settings", "setting", "paramètres", "paramètre", "couleur", "couleurs", "color",
                                 "colors", "coulors", "coulor", "3"]:
            # Paramètrage des couleurs.
            color_settings()
        elif inputed.lower() in references.STOP_WORDS or inputed == "4":
            stop(True)
        elif inputed.lower() in references.BACK_WORDS or inputed == "5":
            break
        else:
            menu_notification("Veuillez entrer une proposition valide", -12, colors.DARK_RED)
        set_cursor(0, get_window_size()[1])


def color_settings() -> None:
    """Permet à l'utilisateur de modifier la couleur des blocs.

    """
    # Dessine le menu.
    clear()
    draw_frame(get_window_width_center() - 12, 1, 24, 4)
    draw_centered("Paramètres de couleurs", -get_window_height_center() + 3)
    draw("■ Basic", 5, 15)
    draw(f"{colors.DARK_RED}■ {colors.WHITE}Red", 5, 16)
    draw(f"{colors.DARK_PURPLE}■ {colors.WHITE}Purple", 5, 17)
    draw(f"{colors.DARK_BLUE}■ {colors.WHITE}Blue", 5, 18)
    draw(f"{colors.DARK_GREEN}■ {colors.WHITE}Green", 5, 19)
    draw(f"{colors.DARK_YELLOW}■ {colors.WHITE}Yellow", 5, 20)
    color = ""

    # Selection de la couleur.
    while color.lower() not in ["white", "blanc", "rouge", "red", "purple", "violet", "blue", "bleu", "green", "vert", "yellow", "jaune", "1", "2", "3", "4", "5", "6"]:
        draw_centered("Choisissez une couleur de bloc", 10)
        set_cursor(get_window_width_center(), get_window_height_center()+12)
        color = input()
        if color in references.STOP_WORDS:
            stop(True)
        elif color in references.BACK_WORDS:
            return
    if color in ["white", "blanc", "1"]:
        references.blocs_char = f"{colors.WHITE}■"
    elif color in ["rouge", "red", "2"]:
        references.blocs_char = f"{colors.DARK_RED}■"
    elif color in ["purple", "violet", "3"]:
        references.blocs_char = f"{colors.DARK_PURPLE}■"
    elif color in ["blue", "bleu", "4"]:
        references.blocs_char = f"{colors.DARK_BLUE}■"
    elif color in ["green", "vert", "5"]:
        references.blocs_char = f"{colors.DARK_GREEN}■"
    elif color in ["yellow", "jaune", "6"]:
        references.blocs_char = f"{colors.DARK_YELLOW}■"
