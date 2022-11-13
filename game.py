from utils.TerminalUtils import *
from utils import References, ShapeUtils, Grid, Utils, ColorUtils


def menu():
    clear()
    window_height = get_window_size()[1]
    for i, line in enumerate(open(References.base_path + "\\resources\\menu.txt", "r").readlines()):
        draw(line.replace("\n", ""), get_window_width_center() - (83 // 2), get_window_height_center() - 11 + i)
    draw_frame(get_window_width_center() - 11, get_window_height_center() - 2, 22, 4)
    draw_centered("Press 'a' to start", 0)
    draw_frame(get_window_width_center() - 15, get_window_height_center() + 3, 30, 4)
    draw_centered("Press 'r' to see the rules", 5)
    while True:
        set_cursor(get_window_width_center(), (window_height - 4))
        inp = input()
        if inp == "a":
            settings_setup()
            break
        elif inp == "r":  # TODO: rules
            break
        clear_area(get_window_width_center() - len(inp), (window_height - 4), get_window_width_center() + len(inp),
                   (window_height - 4))


def settings_setup():
    clear()
    window_width, window_height = get_window_size()
    draw_frame(get_window_width_center() - 15, get_window_height_center() - 15, 30, 4)
    draw_centered("Paramètrage de la partie", -13)

    x_, y_ = draw_frame(get_window_width_center() - 18, get_window_height_center() - 2, 36, 5)
    size = ""
    while not Utils.is_correct_number(size, 21, 26):
        clear_area(x_, y_, 35, 4)
        draw_centered("Choisir une dimension de plateau:", -1)
        set_cursor(get_window_width_center(), get_window_height_center() + 1)
        size = input()
        if not Utils.is_correct_number(size, 21, 26):
            menu_notification("Veuillez entrer un nombre compris entre 21 et 26", -6, ColorUtils.DARK_RED)
    clear_area(0, get_window_height_center() - 10, window_width, window_height)

    grid = Grid.load_grid(ShapeUtils.gen_cercle(12))
    Grid.draw_grid(grid, (window_width // 6) - 12, get_window_height_center() - 5)
    txt = "1. Cercle"
    draw(txt, (window_width // 6) - (len(txt) // 2), get_window_height_center() + 8)

    grid = Grid.load_grid(ShapeUtils.gen_losange(12))
    Grid.draw_grid(grid, ((window_width * 2) // 3) - (window_width // 6) - 12, get_window_height_center() - 5)
    txt = "2. Losange"
    draw(txt, ((window_width * 2) // 3) - (window_width // 6) + (len(txt) // 2) - 12, get_window_height_center() + 8)

    grid = Grid.load_grid(ShapeUtils.gen_triangle(12))
    Grid.draw_grid(grid, window_width - (window_width // 6) - 12, get_window_height_center() - 2)
    txt = "3. Triangle"
    draw(txt, window_width - (window_width // 6) + (len(txt) // 2) - 12, get_window_height_center() + 8)

    x_, y_ = draw_frame(get_window_width_center() - 20, get_window_height_center() + 10, 40, 5)
    shape = "0"
    while not Utils.is_correct_number(shape, 1, 3):
        clear_area(x_, y_, 35, 4)
        draw_centered("Veuillez choisir une forme proposée: ", 11)
        set_cursor(get_window_width_center(), get_window_height_center() + 13)
        shape = input()
        if not Utils.is_correct_number(shape, 1, 3):
            menu_notification("Veuillez choisir une forme proposée", -9, ColorUtils.DARK_RED)
    clear_area(0, get_window_height_center() - 10, window_width, window_height)

    set_cursor((window_width // 6) - 12, get_window_height_center() - 5)
    menu_notification( "1/ Afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un", -6)
    menu_notification("2/ Afficher uniquement 3 blocs sélectionnés aléatoirement", -1)

    bloc_placement = ""
    while bloc_placement != "1" and bloc_placement != "2":
        clear_area(0, (window_height - 4), window_width, 10)
        set_cursor(int(window_width / 2), (window_height - 4))
        bloc_placement = input()
        if bloc_placement != "1" and bloc_placement != "2":
            menu_notification("Veuillez entrer un nombre correct !", 4, ColorUtils.DARK_RED)
    References.settings["shape"] = References.grid_types[int(shape) - 1]
    References.settings["size"] = int(size)
    References.settings["bloc_placement"] = int(bloc_placement)


def game_notification(text: str, color: str = ColorUtils.WHITE):
    x, y = draw_frame(4 + (References.grid["width"] * 2) + 5 + 30 + 5, 2, 45, 2)
    draw(text, x + 1, y, color)


def menu_notification(text: str, y_diff: int, color: str = ColorUtils.WHITE):
    draw_centered(text, y_diff, color)
    draw_frame(get_window_width_center() - (len(text) // 2) - 2, get_window_height_center() + y_diff - 1, len(text) + 4,
               2)


def alert(text: str):
    game_notification(text, ColorUtils.DARK_RED)


def warn(text: str):
    game_notification(text, ColorUtils.DARK_YELLOW)


def clear_notification():
    clear_area(4 + (References.grid["width"] * 2) + 5 + 30 + 5, 2, 46, 4)


def stop(selected: bool = False):
    color = ColorUtils.DARK_RED
    if selected:
        color = ColorUtils.DARK_GREEN
    clear()
    for i, line in enumerate(open(References.base_path + "\\resources\\end_screen.txt", "r").readlines()):
        draw(line.replace("\n", ""), get_window_width_center() - (55 // 2), get_window_height_center() - 8 + i, color)
    draw_centered("Score: " + str(References.score))
    draw_centered("Press any key to continue...", 10)
    input()
    clear()
    exit()


def clear_game_console():
    clear_area(References.console_x, References.console_y, os.get_terminal_size()[0] - References.console_x,  os.get_terminal_size()[1] - References.console_y)
