from typing import Optional, List

import in_game
from utils.notifications import *
from utils.terminal_utils import *
import os
from utils import Grid, References, shape_utils, Utils, DebugUtils, menus, game_menus
from utils.file_utils import get_base_path, get_saves_path, get_maps_path, file_exists, load_blocs, save_grid, read_grid

# Test
# def test():
#     print("- test")
#     exit()
#
#
# print(Utils.actions_string("arrêt", stop=References.STOP_WORDS, back=References.BACK_WORDS, menu=References.MENU_WORDS, stop_action=test))
# exit()

# TODO: replace tout les import * verif pep
# TODO: faire diagram vue en algo pour expliquer le fonctionnement
# TODO: faire des listes pour le stop, menu, back pour pouvoir écrire de différentes manières
# TODO: faire responsive


def update_score(count: int) -> int:
    References.score += count
    return References.score


def print_grid(grid: List[List[str]]) -> None:
    width, height = Grid.get_size(References.grid["matrice"])
    for i, character in enumerate(References.game_letters):
        draw(character, (i * 2) + 5, 1)
    for i in range(width):
        draw("═", (i * 2) + 5, 2)
        draw("═", (i * 2) + 5, height + 3)
    draw("╔", 3, 2)
    draw("╗", (width * 2) + 5, 2)
    draw("╚", 3, height + 3)
    draw("╝", (width * 2) + 5, height + 3)
    for i, line in enumerate(grid):
        draw(str(References.game_letters[i]).upper(), 1, i + 3)
        draw("║", 3, 3 + i)
        draw("║", (width * 2) + 5, i + 3)
        for j, co in enumerate(line):
            if co == "0":
                co = " "
            elif co == "1":
                co = "⬝"
            elif co == "2":
                co = "■"
            draw(co + " ", 5 + (j * 2), 3 + i)


def print_blocs(blocs) -> None:
    width = Grid.get_size(References.grid["matrice"])[0]
    bloc_line: int = 0
    last_x: int = 4 + (width * 2) + 5
    last_list_size: int = 0
    for i, block in enumerate(blocs):
        max_x: int = 0
        t = 0
        if len(block["matrice"]) == 5:
            t = -1
        elif len(block["matrice"]) == 3:
            t = 1
        for j, cube_line in enumerate(Grid.bloc_to_string(block['matrice']).split("\n")):
            if len(cube_line) > 0:
                draw(cube_line, last_x, bloc_line + j + 6 + t)
                if len(block['matrice'][j]) == 0 or '1' not in block['matrice'][j]:
                    continue
                nbx = max(idx for idx, val in enumerate(block['matrice'][j]) if val == '1')
                if nbx > max_x:
                    max_x = nbx
        draw(str(i + 1 + last_list_size), last_x, bloc_line + len(block['matrice']) + 7 + t)
        last_x += max_x * 2 + 3
        if last_x >= get_window_size()[0] - 10:
            last_x = (width * 2) + 9
            bloc_line += 7


def draw_game(blocs) -> None:
    width = Grid.get_size(References.grid["matrice"])[0]
    print_grid(References.grid["matrice"])
    score_frame = draw_frame(4 + (width * 2) + 5, 2, 30, 2)
    draw(f"Score: {References.score}", score_frame[0], score_frame[1])
    print_blocs(blocs)
    References.console_x, References.console_y = draw_frame(get_window_size()[0] - 16, get_window_size()[1] - 7, 17, 7)


def inputs(blocs) -> Optional[Tuple[str, int, int]]:
    inputed_number = ""
    while not Utils.is_correct_number(inputed_number, 1,
                                      (len(References.blocs_liste[0]) + len(References.blocs_liste[1]))):
        in_game.clear_game_console()
        draw("Choisissez une", References.console_x, References.console_y)
        draw("forme: ", References.console_x, References.console_y + 1)
        set_cursor(os.get_terminal_size()[0] - 8, os.get_terminal_size()[1] - 6 + 1)
        inputed_number = input()
        if inputed_number in References.STOP_WORDS:
            in_game.stop(True)
        if not Utils.is_correct_number(inputed_number, 1,
                                       (len(References.blocs_liste[0]) + len(References.blocs_liste[1]))):
            alert("Veuillez entrer un nombre valide !")
    clear_notification()

    x, y = "", ""
    while x not in References.game_letters or y not in References.game_letters:
        in_game.clear_game_console()
        set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
        inputed_coos = input("x y: ")
        if inputed_coos == "stop":
            in_game.stop(True)
        if inputed_coos == "menu":
            game_menus.menu(References.grid["matrice"])
            clear()
            return None
        if " " not in inputed_coos:
            clear_notification()
            alert("Veuillez entrer des coordonnées valides !")
            continue
        x = inputed_coos.split(" ")[0]
        y = inputed_coos.split(" ")[1]
        if x not in References.game_letters or y not in References.game_letters:
            clear_notification()
            alert("Veuillez entrer des coordonnées valides !")
    clear_notification()
    set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
    return inputed_number, References.game_letters.index(x), References.game_letters.index(y)


if __name__ == "__main__":  # TODO: verif si les files save & maps existent si non, les créer
    if not file_exists(get_saves_path()):
        os.mkdir(get_saves_path())
    if not file_exists(get_maps_path()):
        os.mkdir(get_maps_path())
    if not file_exists(get_base_path() + "\\logs"):
        os.mkdir(get_base_path() + "\\logs")
    bloc_list = load_blocs()
    References.common_liste = bloc_list["common"]
    References.cercle_liste = bloc_list["cercle"]
    References.losange_liste = bloc_list["losange"]
    References.triangle_liste = bloc_list["triangle"]
    References.log_path = DebugUtils.get_log_path()
    game_type = menus.main_menu()
    References.blocs_liste = Grid.get_blocs(References.settings["shape"])
    if game_type == "New":
        grid_matrice: Optional[List[List[str]]] = None
        grid_file_path: str = get_maps_path() + str(References.settings["shape"]) + "-" + str(References.settings["size"]) + ".txt"
        if not file_exists(grid_file_path):
            if References.settings["shape"] == References.GRID_TYPES[0]:
                save_grid(grid_file_path, Grid.convert_grid(shape_utils.gen_circle(References.settings["size"])))
            elif References.settings["shape"] == References.GRID_TYPES[1]:
                save_grid(grid_file_path, Grid.convert_grid(shape_utils.gen_losange(References.settings["size"])))
            elif References.settings["shape"] == References.GRID_TYPES[2]:
                save_grid(grid_file_path, Grid.convert_grid(shape_utils.gen_triangle(References.settings["size"])))
        grid_matrice = read_grid(grid_file_path)

        References.grid["matrice"] = grid_matrice
    size: Tuple[int, int] = Grid.get_size(References.grid["matrice"])
    References.grid["width"] = size[0]
    References.grid["height"] = size[1]

    References.game_letters = Utils.get_letters(Grid.get_size(References.grid["matrice"])[0])
    clear()
    while True:

        usable_blocs = Utils.select_blocs()
        draw_game(usable_blocs)
        test = inputs(usable_blocs)
        if test is None:
            continue
        inputed_string, x_index, y_index = test
        if not Grid.valid_position(References.grid["matrice"], usable_blocs[int(inputed_string) - 1]["matrice"],
                                   x_index, y_index):
            References.try_pos += 1
            clear()
            warn(f"Hors de la grille. Plus que {str(3 - References.try_pos)} essais !")
            if References.try_pos >= 3:
                in_game.stop()
            continue
        Grid.emplace_bloc(References.grid["matrice"], usable_blocs[int(inputed_string) - 1]["matrice"], x_index,
                          y_index)
        clear_notification()
        score_increment: int = 0
        for i in range(size[1]):
            if Grid.row_state(References.grid["matrice"], i):
                score_increment += Grid.row_clear(References.grid["matrice"], i)
        for j in range(size[0]):
            if Grid.col_state(References.grid["matrice"], j):
                score_increment += Grid.col_clear(References.grid["matrice"], j)
        update_score(score_increment)
        clear()
