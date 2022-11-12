import random
import game
from utils import GameUtils, FileUtils, Grid, References, ShapeUtils, DebugUtils
from utils.TerminalUtils import *

blocs = FileUtils.load_blocks()
References.common_liste = blocs["common"]
References.cercle_liste = blocs["cercle"]
References.losange_liste = blocs["losange"]
References.triangle_liste = blocs["triangle"]

clear()
path = DebugUtils.get_log_path()
game.menu()
clear()


References.blocs_liste = Grid.print_blocs("")
grid = None
if References.settings["shape"] == References.grid_types[0]:
    grid = Grid.load_grid(ShapeUtils.gen_cercle(References.settings["size"]))
elif References.settings["shape"] == References.grid_types[1]:
    grid = Grid.load_grid(ShapeUtils.gen_losange(References.settings["size"]))
elif References.settings["shape"] == References.grid_types[2]:
    grid = Grid.load_grid(ShapeUtils.gen_triangle(References.settings["size"]))
width, height = Grid.get_size(grid)
References.grid["width"] = width
References.grid["height"] = height
letters = GameUtils.get_letters(width)


def draw_game():
    for i, character in enumerate(letters):
        draw(character, (i * 2) + 5, 1)
    for i in range(width):
        draw("═", (i * 2) + 5, 2)
        draw("═", (i * 2) + 5, height + 3)
    draw("╔", 3, 2)
    draw("╗", (width * 2) + 5, 2)
    draw("╚", 3, height + 3)
    draw("╝", (width * 2) + 5, height + 3)
    for i, line in enumerate(grid):
        draw(str(letters[i]).upper(), 1, i + 3)
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
    if References.settings["bloc_placement"] == 1:
        d = 0
        last_x = 4 + (width * 2) + 5
        a = 0
        for liste in References.blocs_liste:
            for i, block in enumerate(liste):
                j = 0
                for j, cube in enumerate(Grid.bloc_to_string(block['matrice']).split("\n")):
                    draw(cube, last_x, 6 + j + d)
                draw(str(i + 1 + a), last_x, 6 + j + d + 1)

                max_x = 0
                for line in liste[i]['matrice']:
                    if len(line) == 0 or '1' not in line:
                        continue
                    nbx = max(idx for idx, val in enumerate(line) if val == '1')
                    if nbx > max_x:
                        max_x = nbx

                last_x += max_x * 2 + 3
                if last_x >= os.get_terminal_size()[0] - 10:
                    last_x = 4 + (width * 2) + 5
                    d += 7
            a = len(liste)
            d -= 1
    elif References.settings["bloc_placement"] == 2:
        d = 0
        last_x = 4 + (width * 2) + 5
        References.random_blocs.clear()
        for i in range(3):
            References.random_blocs.append(random.choice(References.blocs_liste[0] + References.blocs_liste[1]))
        for i, block in enumerate(References.random_blocs):
            j = 0
            z = 0
            if len(block['matrice']) > 4:
                z = 1
            for j, cube in enumerate(Grid.bloc_to_string(block['matrice']).split("\n")):
                draw(cube, last_x, 6 + j + d - z)
            draw(str(i + 1), last_x, 6 + j + d + 1 - z)

            max_x = 0
            for line in References.random_blocs[i]['matrice']:
                if len(line) == 0 or '1' not in line:
                    continue
                nbx = max(idx for idx, val in enumerate(line) if val == '1')
                if nbx > max_x:
                    max_x = nbx

            last_x += max_x * 2 + 3
            if last_x >= os.get_terminal_size()[0] - 10:
                last_x = 4 + (width * 2) + 5
                d += 7
        d -= 1
        # TODO: impl
    References.console_x, References.console_y = draw_frame(os.get_terminal_size()[0] - 16,
                                                            os.get_terminal_size()[1] - 7, 17, 7)


# TODO: github
draw_game()

# while True:
#     if i == "c":
#         size, shape, bloc_placement = game.settings_setup()
#         References.settings["size"] = size
#         References.settings["shape"] = shape
#         References.settings["bloc_placement"] = bloc_placement
#     elif i == "r":
#         pass  # TODO: écrire les règles

# time.sleep(3)

while True:
    test = ""
    while True:
        clear_area(References.console_x, References.console_y, os.get_terminal_size()[0] - References.console_x,
                   os.get_terminal_size()[1] - References.console_y)
        draw("Choisissez une", References.console_x, References.console_y)
        draw("forme: ", References.console_x, References.console_y + 1)
        set_cursor(os.get_terminal_size()[0] - 8, os.get_terminal_size()[1] - 6 + 1)
        test = input()
        if test == "stop":
            game.stop(True)
        if test.isnumeric():
            if 0 < int(test) <= (len(References.blocs_liste[0]) + len(References.blocs_liste[1])):
                break
        game.alert("Veuillez entrer un nombre valide !")
    game.clear_notification()
    block_to_place = References.blocs_liste[0][int(test)]
    if int(test) > len(References.blocs_liste[0]):
        block_to_place = References.blocs_liste[1][int(test) - len(References.blocs_liste[0])]
    clear_area(References.console_x, References.console_y, os.get_terminal_size()[0] - References.console_x,
               os.get_terminal_size()[1] - References.console_y)
    while True:
        clear_area(References.console_x, References.console_y, os.get_terminal_size()[0] - References.console_x,
                   os.get_terminal_size()[1] - References.console_y)
        set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
        inputed_coos = input("x y: ")
        if inputed_coos == "stop":
            game.stop(True)
        if " " not in inputed_coos:
            game.alert("Veuillez entrer des coordonnées valides !")
            continue
        x = inputed_coos.split(" ")[0]
        y = inputed_coos.split(" ")[1]
        if x not in letters or y not in letters:
            game.alert("Veuillez entrer des coordonnées valides !")
            continue
        break
    game.clear_notification()
    set_cursor(os.get_terminal_size()[0] - 15, os.get_terminal_size()[1] - 6)
    y_index = letters.index(y)
    x_index = letters.index(x)
    if grid[y_index][x_index] == "0":
        References.try_pos += 1
        game.warn(f"Hors de la grille. Plus que {str(3 - References.try_pos)} essais !")
        if References.try_pos >= 3:
            game.clear_notification()
            game.stop()
        continue
    game.clear_notification()
    grid[y_index].pop(x_index)
    grid[y_index].insert(x_index, "2")
    clear()
    draw_game()
