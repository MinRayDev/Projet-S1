"""Fichier principal du projet.
@project Tetris
"""
import string
from typing import Tuple, List, Optional

from utils import grids, references, menus, game, blocks, shapes
from utils.files import get_maps_path, file_exists, save_grid, read_grid, create_game_directories
from utils.game import update_score, draw_game, inputs
from utils.notifications import warn, clear_notification
from utils.references import BlockType
from utils.terminal import clear

if __name__ == "__main__":

    # Création des dossiers nécessaires au jeu.
    create_game_directories()
    # Création d'une nouvelle partie, True si la partie est vraiment nouvelle, False si la partie est chargée
    new_game: bool = menus.main_menu()

    if new_game:
        grid_file_path: str = get_maps_path() + "/" + str(references.settings["shape"]) + "-" + str(
            references.settings["size"]) + ".txt"

        if not file_exists(grid_file_path):
            # Création du fichier et sauvegarde de la carte en fonction de la forme de la carte.
            if references.settings["shape"] == references.GRID_TYPES[0]:
                save_grid(grid_file_path, grids.convert_grid(shapes.gen_circle(references.settings["size"])))
            elif references.settings["shape"] == references.GRID_TYPES[1]:
                save_grid(grid_file_path, grids.convert_grid(shapes.gen_losange(references.settings["size"])))
            elif references.settings["shape"] == references.GRID_TYPES[2]:
                save_grid(grid_file_path, grids.convert_grid(shapes.gen_triangle(references.settings["size"])))

        references.grid_matrice = read_grid(grid_file_path)

    size: tuple[int, int] = grids.get_size(references.grid_matrice)
    references.game_letters = string.ascii_lowercase[:(grids.get_size(references.grid_matrice)[0])]

    clear()

    while True:
        usable_blocks: list[BlockType] = blocks.select_blocks()
        draw_game(usable_blocks)
        user_inputs: Optional[tuple[str, int, int]] = inputs(usable_blocks)
        # Si elles sont nulles (correspond à l'utilisation du menu).
        if user_inputs is None:
            # Retourne au début de la boucle.
            continue
        # On sépare les entrées du joueur, (numéro du bloc selectionné, coordonnée x, coordonnée y).
        block_input, x_index, y_index = user_inputs
        if not grids.valid_position(references.grid_matrice, usable_blocks[int(block_input) - 1], x_index, y_index):
            references.try_pos += 1
            if references.try_pos >= 3:
                game.stop()
            clear()
            warn(f"Hors de la grille. Plus que {str(3 - references.try_pos)} essais !")
            # Retourne au début de la boucle.
            continue
        grids.emplace_bloc(references.grid_matrice, usable_blocks[int(block_input) - 1], x_index, y_index)
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
