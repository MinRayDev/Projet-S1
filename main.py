import game
import random
from utils.TerminalUtils import *
from utils import GameUtils, FileUtils, Grid, References, ShapeUtils, DebugUtils, Utils


# TODO: impl stop partout, back dans les menus

def draw_game():
    clear()
    width, height = References.grid["width"], References.grid["height"]
    for i, character in enumerate(References.game_letters):
        draw(character, (i * 2) + 5, 1)
    for i in range(width):
        draw("═", (i * 2) + 5, 2)
        draw("═", (i * 2) + 5, height + 3)
    draw("╔", 3, 2)
    draw("╗", (width * 2) + 5, 2)
    draw("╚", 3, height + 3)
    draw("╝", (width * 2) + 5, height + 3)
    for i, line in enumerate(grid_matrice):
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

    score_frame = draw_frame(4 + (width * 2) + 5, 2, 30, 2)
    draw(f"Score: {References.score}", score_frame[0], score_frame[1])
    bloc_line: int = 0
    last_x: int = 4 + (width * 2) + 5
    if References.settings["bloc_placement"] == 1:
        last_list_size: int = 0
        for liste in References.blocs_liste:
            for i, block in enumerate(liste):
                max_x: int = 0
                for j, cube_line in enumerate(Grid.bloc_to_string(block['matrice']).split("\n")):
                    if len(cube_line) > 0:
                        draw(cube_line, last_x, bloc_line + j + 6)
                        if len(liste[i]['matrice'][j]) == 0 or '1' not in liste[i]['matrice'][j]:
                            continue
                        nbx = max(idx for idx, val in enumerate(liste[i]['matrice'][j]) if val == '1')
                        if nbx > max_x:
                            max_x = nbx
                draw(str(i + 1 + last_list_size), last_x, bloc_line + len(liste[i]['matrice']) + 7)
                last_x += max_x * 2 + 3
                if last_x >= get_window_size()[0] - 10:
                    last_x = (width * 2) + 9
                    bloc_line += 7
            last_list_size = len(liste)
            bloc_line -= 1
    elif References.settings["bloc_placement"] == 2:
        References.random_blocs.clear()
        for i in range(3):
            References.random_blocs.append(random.choice(References.blocs_liste[0] + References.blocs_liste[1]))
        for i, block in enumerate(References.random_blocs):
            z: int = 0
            max_x: int = 0
            if len(block['matrice']) > 4:
                z = 1
            for j, cube_line in enumerate(Grid.bloc_to_string(block['matrice']).split("\n")):
                if len(cube_line) > 0:
                    draw(cube_line, last_x, 6 + j + bloc_line - z)
                    if len(References.random_blocs[i]['matrice'][j]) == 0 or '1' not in \
                            References.random_blocs[i]['matrice'][j]:
                        continue
                    nbx = max(idx for idx, val in enumerate(References.random_blocs[i]['matrice'][j]) if val == '1')
                    if nbx > max_x:
                        max_x = nbx
            draw(str(i + 1), last_x, bloc_line + len(References.random_blocs[i]['matrice']) - z + 7)
            last_x += max_x * 2 + 3
            if last_x >= get_window_size()[0] - 10:
                last_x = 4 + (width * 2) + 5
                bloc_line += 7
    References.console_x, References.console_y = draw_frame(get_window_size()[0] - 16, get_window_size()[1] - 7, 17, 7)
    inputs()


def inputs():
    while True:
        inputed_number = ""
        while not Utils.is_correct_number(inputed_number, 1, (len(References.blocs_liste[0]) + len(References.blocs_liste[1]))):
            game.clear_game_console()
            draw("Choisissez une", References.console_x, References.console_y)
            draw("forme: ", References.console_x, References.console_y + 1)
            set_cursor(os.get_terminal_size()[0] - 8, os.get_terminal_size()[1] - 6 + 1)
            inputed_number = input()
            if inputed_number == "stop":
                game.stop(True)
            if not Utils.is_correct_number(inputed_number, 1, (len(References.blocs_liste[0]) + len(References.blocs_liste[1]))):
                game.alert("Veuillez entrer un nombre valide !")
        game.clear_notification()
        # block_to_place = References.blocs_liste[0][int(test)]
        # if int(test) > len(References.blocs_liste[0]):
        #     block_to_place = References.blocs_liste[1][int(test) - len(References.blocs_liste[0])]

        x, y = "", ""
        while x not in References.game_letters or y not in References.game_letters:
            game.clear_game_console()
            set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
            inputed_coos = input("x y: ")
            if inputed_coos == "stop":
                game.stop(True)
            if " " not in inputed_coos:
                game.alert("Veuillez entrer des coordonnées valides !")
                continue
            x = inputed_coos.split(" ")[0]
            y = inputed_coos.split(" ")[1]
            if x not in References.game_letters or y not in References.game_letters:
                game.alert("Veuillez entrer des coordonnées valides !")
                continue
        game.clear_notification()
        set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
        y_index = References.game_letters.index(y)
        x_index = References.game_letters.index(x)
        if References.grid["matrice"][y_index][x_index] == "0":
            References.try_pos += 1
            game.warn(f"Hors de la grille. Plus que {str(3 - References.try_pos)} essais !")
            if References.try_pos >= 3:
                game.stop()
            continue
        game.clear_notification()
        References.grid["matrice"][y_index].pop(x_index)
        References.grid["matrice"][y_index].insert(x_index, "2")
        draw_game()


if __name__ == "__main__":
    blocs: dict = FileUtils.load_blocks()
    References.common_liste = blocs["common"]
    References.cercle_liste = blocs["cercle"]
    References.losange_liste = blocs["losange"]
    References.triangle_liste = blocs["triangle"]
    References.log_path = DebugUtils.get_log_path()
    game.menu()
    References.blocs_liste = Grid.print_blocs("")
    grid_matrice = None
    if References.settings["shape"] == References.grid_types[0]:
        grid_matrice = Grid.load_grid(ShapeUtils.gen_cercle(References.settings["size"]))
    elif References.settings["shape"] == References.grid_types[1]:
        grid_matrice = Grid.load_grid(ShapeUtils.gen_losange(References.settings["size"]))
    elif References.settings["shape"] == References.grid_types[2]:
        grid_matrice = Grid.load_grid(ShapeUtils.gen_triangle(References.settings["size"]))
    size = Grid.get_size(grid_matrice)
    References.grid["width"] = size[0]
    References.grid["height"] = size[1]
    References.grid["matrice"] = grid_matrice
    References.game_letters = GameUtils.get_letters(size[0])
    draw_game()
