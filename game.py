import json

from utils.TerminalUtils import *
from utils import References, ShapeUtils, Grid, Utils, ColorUtils, DebugUtils, FileUtils


def rules():
    clear()
    draw("🐮", get_window_width_center(), get_window_height_center())

    input()


def main_menu() -> str:
    window_height = get_window_size()[1]
    while True:
        clear()
        for i, line in enumerate(open(References.base_path + "\\resources\\menu.txt", "r").readlines()):
            draw(line.replace("\n", ""), get_window_width_center() - (83 // 2), get_window_height_center() - 11 + i)
        draw_frame(get_window_width_center() - 11, get_window_height_center() - 2, 22, 4)
        draw_centered("Press 'a' to start", 0)
        draw_frame(get_window_width_center() - 15, get_window_height_center() + 3, 30, 4)
        draw_centered("Press 'r' to see the rules", 5)
        set_cursor(get_window_width_center(), (window_height - 4))
        inp = input()
        if inp == "a":
            t = load_new_game()
            if t == "1":
                settings_setup()
                return "New"
            elif t == "2":
                party_loaded: dict = load_game()
                References.settings["shape"] = party_loaded["settings"]["shape"]
                References.settings["size"] = party_loaded["settings"]["size"]
                References.settings["bloc_placement"] = party_loaded["settings"]["bloc_placement"]
                References.grid["matrice"] = party_loaded["grid_matrice"]
                References.score = party_loaded["score"]
                return "Loaded"
        elif inp == "r":  # TODO: rules
            break
        elif inp == "stop":
            clear()
            exit()
        clear_area(get_window_width_center() - len(inp), (window_height - 4), get_window_width_center() + len(inp),
                   (window_height - 4))


def load_game():
    clear()
    menu_notification(" Saves", -15)
    i = 0
    x = 2
    for file in os.listdir(References.base_path + "\\resources\\saves"):
        draw(str(i+1) + "/ " + file[:-5], x, get_window_height_center()-15+4+i)
        i += 1
    draw_centered("Choisissez le fichier de partie que vous voulez:", 14)
    set_cursor(get_window_width_center(), get_window_height_center()+16)
    while True:
        inputed = input()
        if Utils.is_correct_number(inputed, 1, len(os.listdir(References.base_path + "\\resources\\saves"))):
            return json.load(open(References.base_path + "\\resources\\saves\\" + os.listdir(References.base_path + "\\resources\\saves")[i-1]))


def load_new_game():
    clear()
    window_width, window_height = get_window_size()
    set_cursor((window_width // 6) - 12, get_window_height_center() - 5)
    menu_notification("1/ New Game", -6)
    menu_notification("2/ Load Game ", -1)
    bloc_placement = ""
    while bloc_placement != "1" and bloc_placement != "2":
        clear_area(0, (window_height - 4), window_width, 10)
        set_cursor(int(window_width / 2), (window_height - 4))
        bloc_placement = input()
        if bloc_placement.lower() == "back":
            return "back"
        elif bloc_placement.lower() == "stop":
            clear()
            exit()
        elif bloc_placement != "1" and bloc_placement != "2":
            menu_notification("Veuillez entrer un nombre correct !", 4, ColorUtils.DARK_RED)
    return bloc_placement


def settings_set_size():
    size = ""
    while not Utils.is_correct_number(size, 21, 26):
        x_, y_ = draw_frame(get_window_width_center() - 18, get_window_height_center() - 2, 36, 5)
        clear_area(x_, y_, 35, 4)
        draw_centered("Choisir une dimension de plateau:", -1)
        set_cursor(get_window_width_center(), get_window_height_center() + 1)
        size = input()
        if size.lower() == "back":
            return "back"
        if size.lower() == "stop":
            clear()
            exit()
        if not Utils.is_correct_number(size, 21, 26):
            menu_notification("Veuillez entrer un nombre compris entre 21 et 26", -6, ColorUtils.DARK_RED)
    return size


def settings_set_shape():
    window_width, window_height = get_window_size()
    grid = Grid.load_grid(ShapeUtils.gen_cercle(11))
    Grid.draw_grid(grid, (window_width // 6) - 11, get_window_height_center() - 5)
    shape_name = "1. Cercle"
    draw(shape_name, (window_width // 6) - (len(shape_name) // 2), get_window_height_center() + 8)

    grid = Grid.load_grid(ShapeUtils.gen_losange(11))
    Grid.draw_grid(grid, ((window_width * 2) // 3) - (window_width // 6) - 11, get_window_height_center() - 5)
    shape_name = "2. Losange"
    draw(shape_name, ((window_width * 2) // 3) - (window_width // 6) + (len(shape_name) // 2) - 11,
         get_window_height_center() + 8)

    grid = Grid.load_grid(ShapeUtils.gen_triangle(11))
    Grid.draw_grid(grid, window_width - (window_width // 6) - 11, get_window_height_center() - 2)
    shape_name = "3. Triangle"
    draw(shape_name, window_width - (window_width // 6) + (len(shape_name) // 2) - 11, get_window_height_center() + 8)

    x_, y_ = draw_frame(get_window_width_center() - 20, get_window_height_center() + 10, 40, 5)
    shape = "0"
    while not Utils.is_correct_number(shape, 1, 3):
        clear_area(x_, y_, 35, 4)
        draw_centered("Veuillez choisir une forme proposée: ", 11)
        set_cursor(get_window_width_center(), get_window_height_center() + 13)
        shape = input()
        if shape.lower() == "back":
            return "back"
        if shape.lower() == "stop":
            clear()
            exit()
        if not Utils.is_correct_number(shape, 1, 3):
            menu_notification("Veuillez choisir une forme proposée", -9, ColorUtils.DARK_RED)
    return shape


def settings_set_placement_type():
    window_width, window_height = get_window_size()
    set_cursor((window_width // 6) - 12, get_window_height_center() - 5)
    menu_notification(
        "1/ Afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un", -6)
    menu_notification("2/ Afficher uniquement 3 blocs sélectionnés aléatoirement", -1)

    bloc_placement = ""
    while bloc_placement != "1" and bloc_placement != "2":
        clear_area(0, (window_height - 4), window_width, 10)
        set_cursor(int(window_width / 2), (window_height - 4))
        bloc_placement = input()
        if bloc_placement.lower() == "back":
            return "back"
        if bloc_placement.lower() == "stop":
            clear()
            exit()
        if bloc_placement != "1" and bloc_placement != "2":
            menu_notification("Veuillez entrer un nombre correct !", 4, ColorUtils.DARK_RED)
    return bloc_placement


def settings_setup():
    clear()
    window_width, window_height = get_window_size()
    draw_frame(get_window_width_center() - 15, get_window_height_center() - 15, 30, 4)
    draw_centered("Paramètrage de la partie", -13)
    size: str = ""
    shape: str = ""
    bloc_placement: str = ""
    while True:
        if References.do_size:
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            size = settings_set_size()

            if size == "back":
                main_menu()
                break
            else:
                References.do_size = False
        DebugUtils.log("Size: " + str(size), References.log_path)

        if References.do_shape and (not References.do_size):
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            shape = settings_set_shape()
            DebugUtils.log(str(shape), References.log_path)
            if shape == "back":
                References.do_size = True
                continue
            else:
                References.do_shape = False
        DebugUtils.log("Shape: " + str(shape), References.log_path)

        if References.do_placement and (not References.do_size and not References.do_shape):
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            bloc_placement = settings_set_placement_type()
            if bloc_placement == "back":
                References.do_shape = True
                continue
            else:
                References.do_placement = False
        DebugUtils.log("Placement: " + str(bloc_placement), References.log_path)

        if not References.do_size and not References.do_shape and not References.do_placement:
            DebugUtils.log("End: " + str(size) + " " + str(shape) + " " + str(bloc_placement), References.log_path)
            References.settings["shape"] = References.grid_types[int(shape) - 1]
            References.settings["size"] = int(size)
            References.settings["bloc_placement"] = int(bloc_placement)
            break


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


def clear_game_console() -> None:
    clear_area(References.console_x, References.console_y, os.get_terminal_size()[0] - References.console_x,
               os.get_terminal_size()[1] - References.console_y)


def menu(grid: list[list[str]]):  # TODO: saves, stop, back, rules
    clear()
    while True:
        draw_frame(get_window_width_center() - 9, 1, 18, 4)
        draw_centered("Game Menu", -16)

        draw_frame(get_window_width_center() // 2 - 18, get_window_height_center() - 9, 35, 20)
        for i, line in enumerate(
                open(References.base_path + "\\resources\\save_icon.txt", "r", encoding="utf-8").readlines()):
            draw(line.replace("\n", ""), get_window_width_center() // 2 - 15, get_window_height_center() - 7 + i)
        draw("1. Save", get_window_width_center() // 2 - len("1. Save") // 2, get_window_height_center() - 9 + 20 - 3)

        draw_frame(get_window_width_center() - 18, get_window_height_center() - 9, 35, 20)
        for i, line in enumerate(
                open(References.base_path + "\\resources\\rules_logo.txt", "r", encoding="utf-8").readlines()):
            draw(line.replace("\n", ""), get_window_width_center() - 14, get_window_height_center() - 7 + i)
        draw_centered("2. Rules", 8)

        x, y = draw_frame(get_window_width_center() + 18, get_window_height_center() - 9, 35, 6)
        draw("3. Visual Settings", x + 35 // 2 - len("3. Visual Settings") // 2, y + 2)

        x, y = draw_frame(get_window_width_center() + 18, get_window_height_center() - 2, 35, 6)
        draw("4. Stop", x + 35 // 2 - len("4. Stop") // 2, y + 2)

        x, y = draw_frame(get_window_width_center() + 18, get_window_height_center() + 5, 35, 6)
        draw("5. Back", x + 35 // 2 - len("5. Back") // 2, y + 2)

        draw_centered("Que voulez vous faire ?", 13)
        set_cursor(get_window_width_center(), get_window_height_center() + 15)
        inputed = input()
        if inputed == "save":
            clear_area(0, get_window_height_center() + 13, get_window_size()[0], get_window_size()[1])
            draw_centered("Entrez le nom du fichier:", 13)
            set_cursor(get_window_width_center(), get_window_height_center() + 15)
            inputed_file_name = input("")
            FileUtils.save_game(inputed_file_name, grid, References.score)
            clear()
        elif inputed == "rules":
            rules()
            clear()
        elif inputed == "stop":
            stop(True)
        elif inputed == "back":
            break
        else:
            menu_notification("Veuillez entrer une proposition valide", -12, ColorUtils.DARK_RED)
        set_cursor(0, get_window_size()[1])
