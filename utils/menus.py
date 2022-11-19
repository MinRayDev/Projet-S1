from utils import Utils, Grid
from utils.file_utils import get_resources_path, load_game, get_saves_path
from utils.notifications import *
from utils.shape_utils import gen_losange, gen_triangle, gen_circle
from utils.terminal_utils import *


def main_menu() -> str:
    window_height = get_window_size()[1]
    while True:
        clear()
        draw_ascii_art(get_resources_path() + "\\menu.txt", get_window_width_center() - (83 // 2), get_window_height_center() - 11)
        draw_frame(get_window_width_center() - 11, get_window_height_center() - 2, 22, 4)
        draw_centered("Press 'a' to start", 0)
        draw_frame(get_window_width_center() - 15, get_window_height_center() + 3, 30, 4)
        draw_centered("Press 'r' to see the rules", 5)
        set_cursor(get_window_width_center(), (window_height - 4))
        inp = input()
        if inp == "a":
            game_type: str = load_new_game()
            if game_type == "1":
                settings_setup()
                return "New"
            elif game_type == "2":
                party_loaded = load_game()
                References.settings["shape"] = party_loaded["settings"]["shape"]
                References.settings["size"] = party_loaded["settings"]["size"]
                References.settings["bloc_placement"] = party_loaded["settings"]["bloc_placement"]
                References.grid["matrice"] = party_loaded["grid_matrice"]
                References.score = party_loaded["score"]
                return "Loaded"
            elif game_type in References.STOP_WORDS:
                clear()
                exit()
        elif inp == "r":  # TODO: rules
            break
        # TODO: Stop
        clear_area(get_window_width_center() - len(inp), (window_height - 4), get_window_width_center() + len(inp),
                   (window_height - 4))
        return ""


def load_game():
    clear()
    menu_notification(" Saves", -(get_window_size()[1] // 2) + 2)
    i = 0
    x = 2
    for file in os.listdir(get_saves_path()):
        draw(str(i + 1) + "/ " + file[:-5], x, get_window_height_center() - 15 + 4 + i)
        i += 1
    draw_centered("Choisissez le fichier de partie que vous voulez:", 14)
    set_cursor(get_window_width_center(), get_window_height_center() + 16)
    loop_condition = True
    while loop_condition:  # TODO: back vers main menu, stop
        inputed = input()
        loop_condition = Utils.actions_string(inputed_string=inputed, stop=True, is_game_launched=False, back=True)
        if not loop_condition:
            break
        if Utils.is_correct_number(inputed, 1, len(os.listdir(get_saves_path()))):
            return load_game(int(inputed) - 1)
        else:
            clear_area(0, get_window_height_center() + 16, get_window_size()[0], 2)
            set_cursor(get_window_width_center(), get_window_height_center() + 16)


# TODO: refaire le naming des variables
def load_new_game() -> str:
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
        if bloc_placement.lower() == "back":  # TODO: back vers main menu, stop
            return "back"
        elif bloc_placement.lower() == "stop":
            clear()
            exit()
        elif bloc_placement != "1" and bloc_placement != "2":
            menu_notification("Veuillez entrer un nombre correct !", 4, ColorUtils.DARK_RED)
    return bloc_placement


def settings_set_size() -> str:
    size = ""
    while not Utils.is_correct_number(size, 21, 26):
        x_, y_ = draw_frame(get_window_width_center() - 18, get_window_height_center() - 2, 36, 5)
        clear_area(x_, y_, 35, 4)
        draw_centered("Choisir une dimension de plateau:", -1)
        set_cursor(get_window_width_center(), get_window_height_center() + 1)
        size = input()
        if size.lower() == "back":  # TODO: back vers main menu, stop
            return "back"
        if size.lower() == "stop":
            clear()
            exit()
        if not Utils.is_correct_number(size, 21, 26):
            menu_notification("Veuillez entrer un nombre compris entre 21 et 26", -6, ColorUtils.DARK_RED)
    return size


def settings_set_shape() -> str:  # TODO: back vers main menu, stop
    window_width, window_height = get_window_size()
    grid = Grid.convert_grid(gen_circle(11))
    Grid.draw_grid(grid, (window_width // 6) - 11, get_window_height_center() - 5)
    shape_name = "1. Cercle"
    draw(shape_name, (window_width // 6) - (len(shape_name) // 2), get_window_height_center() + 8)

    grid = Grid.convert_grid(gen_losange(11))
    Grid.draw_grid(grid, ((window_width * 2) // 3) - (window_width // 6) - 11, get_window_height_center() - 5)
    shape_name = "2. Losange"
    draw(shape_name, ((window_width * 2) // 3) - (window_width // 6) + (len(shape_name) // 2) - 11,
         get_window_height_center() + 8)

    grid = Grid.convert_grid(gen_triangle(11))
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


def settings_set_placement_type() -> str:  # TODO: back vers main menu, stop
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


def settings_setup() -> None:  # TODO: back vers main menu, stop
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

        if References.do_shape and (not References.do_size):
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            shape = settings_set_shape()
            if shape == "back":
                References.do_size = True
                continue
            else:
                References.do_shape = False

        if References.do_placement and (not References.do_size and not References.do_shape):
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            bloc_placement = settings_set_placement_type()
            if bloc_placement == "back":
                References.do_shape = True
                continue
            else:
                References.do_placement = False

        if not References.do_size and not References.do_shape and not References.do_placement:
            References.settings["shape"] = References.GRID_TYPES[int(shape) - 1]
            References.settings["size"] = int(size)
            References.settings["bloc_placement"] = int(bloc_placement)
            break
