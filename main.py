import json
import string
from typing import List, Tuple

from utils import grids, references, menus, game, blocs, shapes, logging
from utils.files import get_maps_path, file_exists, load_blocs, save_grid, read_grid, create_game_directories, \
    get_saves_path
from utils.game import update_score, draw_game, inputs
from utils.notifications import warn, clear_notification
from utils.terminal import clear

# TODO: faire diagram vue en algo pour expliquer le fonctionnement


if __name__ == "__main__":
    create_game_directories()

    references.log_path = logging.get_log_path()

    game_type = menus.main_menu()

    references.blocs_liste = grids.get_blocs(references.settings["shape"], load_blocs())  # TODO: remove la reference et le mettre en arg si on a le droit

    if game_type == "New":
        grid_file_path: str = get_maps_path() + str(references.settings["shape"]) + "-" + str(
            references.settings["size"]) + ".txt"
        if not file_exists(grid_file_path):
            if references.settings["shape"] == references.GRID_TYPES[0]:
                save_grid(grid_file_path, grids.convert_grid(shapes.gen_circle(references.settings["size"])))
            elif references.settings["shape"] == references.GRID_TYPES[1]:
                save_grid(grid_file_path, grids.convert_grid(shapes.gen_losange(references.settings["size"])))
            elif references.settings["shape"] == references.GRID_TYPES[2]:
                save_grid(grid_file_path, grids.convert_grid(shapes.gen_triangle(references.settings["size"])))

        grid_matrice: List[List[str]] = read_grid(grid_file_path)
        references.grid_matrice = grid_matrice

    size: Tuple[int, int] = grids.get_size(references.grid_matrice)

    references.game_letters = string.ascii_lowercase[:(grids.get_size(references.grid_matrice)[0])]
    clear()
    while True:
        usable_blocs = blocs.select_blocs()
        draw_game(usable_blocs)
        test = inputs(usable_blocs)
        if test is None:
            continue
        inputed_string, x_index, y_index = test
        if not grids.valid_position(references.grid_matrice, usable_blocs[int(inputed_string) - 1]["matrice"], x_index, y_index):
            references.try_pos += 1
            if references.try_pos >= 3:
                game.stop()
            clear()
            warn(f"Hors de la grille. Plus que {str(3 - references.try_pos)} essais !")
            continue
        grids.emplace_bloc(references.grid_matrice, usable_blocs[int(inputed_string) - 1]["matrice"], x_index, y_index)
        clear_notification()
        score_increment: int = 0
        for i in range(size[1]):
            if grids.row_state(references.grid_matrice, i):
                score_increment += grids.row_clear(references.grid_matrice, i)
        for j in range(size[0]):
            if grids.col_state(references.grid_matrice, j):
                score_increment += grids.col_clear(references.grid_matrice, j)
        update_score(score_increment)
        clear()
