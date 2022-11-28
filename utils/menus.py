import os
from typing import Union

from utils import numbers, grids, references, colors
from utils.files import get_resources_path, load_game_json, get_saves_path
from utils.notifications import menu_notification
from utils.shapes import gen_losange, gen_triangle, gen_circle
from utils.terminal import clear, get_window_size, draw_ascii_art, get_window_width_center, get_window_height_center, \
    draw_centered, draw_frame, set_cursor, draw, clear_area


def exit_game() -> None:
    clear()
    exit()


def main_menu() -> str:
    window_height = get_window_size()[1]
    while True:
        # Clear terminal window
        clear()

        # Draw main menu
        draw_ascii_art(get_resources_path() + "\\menu.txt", get_window_width_center() - (83 // 2),
                       get_window_height_center() - 11)
        draw_frame(get_window_width_center() - 11, get_window_height_center() - 2, 22, 4)
        draw_centered("Press 'a' to start", 0)
        draw_frame(get_window_width_center() - 15, get_window_height_center() + 3, 30, 4)
        draw_centered("Press 'r' to see the rules", 5)
        set_cursor(get_window_width_center(), (window_height - 4))

        # Wait until user's input
        inp = input()

        # Choose between launch the game or see the rules
        if inp == "a":

            # Choose between load a game or create a new game
            game_type: str = choose_game_type()

            if game_type == "1":

                # If user choose to create a new game then he will setup settings of the game
                t = settings_setup()
                if t != "back":
                    references.settings["shape"] = t[0]
                    references.settings["size"] = t[1]
                    references.settings["bloc_placement"] = t[2]
                    return "New"
            elif game_type == "2":
                party_loaded = load_game()
                references.settings["shape"] = party_loaded["settings"]["shape"]
                references.settings["size"] = party_loaded["settings"]["size"]
                references.settings["bloc_placement"] = party_loaded["settings"]["bloc_placement"]
                references.grid_matrice = party_loaded["grid_matrice"]
                references.score = party_loaded["score"]
                return "Loaded"
            elif game_type == "back":
                continue
        elif inp == "r":
            rules()
        elif inp in references.STOP_WORDS:
            exit_game()
        # clear_area(get_window_width_center() - len(inp), (window_height - 4), get_window_width_center() + len(inp), (window_height - 4))


def load_game():
    clear()
    menu_notification(" Saves", -get_window_height_center() + 2)
    i = 0
    j = 0
    x = 2
    max_len: int = 0
    for file in os.listdir(get_saves_path()):
        draw(str(j + 1) + "/ " + file[:-5], x, i + 6)
        max_len += len(str(j + 1) + "/ " + file[:-5]) if len(str(j + 1) + "/ " + file[:-5]) > max_len else 0
        i += 1
        j += 1
        if i + 6 >= get_window_height_center() + 13:
            x += max_len + 3
            max_len = 0
            i = 0
    draw_centered("Choisissez le fichier de partie que vous voulez:", 14)
    set_cursor(get_window_width_center(), get_window_height_center() + 16)
    while True:
        inputed = input()

        if inputed.lower() in references.STOP_WORDS:
            exit_game()
        elif inputed.lower() in references.BACK_WORDS:
            break
        elif numbers.is_correct_number(inputed, 1, len(os.listdir(get_saves_path()))):
            return load_game_json(int(inputed) - 1)
        else:
            clear_area(0, get_window_height_center() + 16, get_window_size()[0], 2)
            set_cursor(get_window_width_center(), get_window_height_center() + 16)


# TODO: refaire le naming des variables
def choose_game_type() -> str:
    # Clear the terminal window
    clear()
    window_width, window_height = get_window_size()

    # draw the game type menu
    menu_notification("1/ New Game", -6)
    menu_notification("2/ Load Game ", -1)
    game_type = ""

    # loop while the user doesnt choose an available game type or write an action word (like stop or back)
    while game_type != "1" and game_type != "2":

        # clear the writting area
        clear_area(0, (window_height - 4), window_width, 10)

        # set the cursor position at the center of the screen
        set_cursor(int(window_width / 2), (window_height - 4))

        # user input what he want
        game_type = input()

        if game_type.lower() in references.STOP_WORDS:
            exit_game()
        elif game_type.lower() in references.BACK_WORDS:
            return "back"
        elif game_type != "1" and game_type != "2":
            menu_notification("Veuillez entrer un nombre correct !", 4, colors.DARK_RED)
    return game_type


def settings_set_size() -> str:
    size = ""
    while not numbers.is_correct_number(size, 21, 26):
        x_, y_ = draw_frame(get_window_width_center() - 18, get_window_height_center() - 2, 36, 5)
        clear_area(x_, y_, 35, 4)
        draw_centered("Choisir une dimension de plateau:", -1)
        set_cursor(get_window_width_center(), get_window_height_center() + 1)
        size = input()
        if size.lower() in references.STOP_WORDS:
            exit_game()
        elif size.lower() in references.BACK_WORDS:
            return "back"
        elif not numbers.is_correct_number(size, 21, 26):
            menu_notification("Veuillez entrer un nombre compris entre 21 et 26", -6, colors.DARK_RED)
    return size


def settings_set_shape() -> str:
    window_width, window_height = get_window_size()
    grid = grids.convert_grid(gen_circle(11))
    grids.draw_grid(grid, (window_width // 6) - 11, get_window_height_center() - 5)
    shape_name = "1. Cercle"
    draw(shape_name, (window_width // 6) - (len(shape_name) // 2), get_window_height_center() + 8)

    grid = grids.convert_grid(gen_losange(11))
    grids.draw_grid(grid, ((window_width * 2) // 3) - (window_width // 6) - 11, get_window_height_center() - 5)
    shape_name = "2. Losange"
    draw(shape_name, ((window_width * 2) // 3) - (window_width // 6) + (len(shape_name) // 2) - 11,
         get_window_height_center() + 8)

    grid = grids.convert_grid(gen_triangle(11))
    grids.draw_grid(grid, window_width - (window_width // 6) - 11, get_window_height_center() - 2)
    shape_name = "3. Triangle"
    draw(shape_name, window_width - (window_width // 6) + (len(shape_name) // 2) - 11, get_window_height_center() + 8)

    x_, y_ = draw_frame(get_window_width_center() - 20, get_window_height_center() + 10, 40, 5)
    shape = "0"
    while not numbers.is_correct_number(shape, 1, 3):
        clear_area(x_, y_, 35, 4)
        draw_centered("Veuillez choisir une forme proposée: ", 11)
        set_cursor(get_window_width_center(), get_window_height_center() + 13)
        shape = input()
        if shape.lower() in references.STOP_WORDS:
            exit_game()
        elif shape.lower() in references.BACK_WORDS:
            return "back"
        elif not numbers.is_correct_number(shape, 1, 3):
            menu_notification("Veuillez choisir une forme proposée", -9, colors.DARK_RED)
    return shape


def settings_set_placement_type() -> str:
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
        if bloc_placement.lower() in references.STOP_WORDS:
            exit_game()
        elif bloc_placement.lower() in references.BACK_WORDS:
            return "back"
        if bloc_placement != "1" and bloc_placement != "2":
            menu_notification("Veuillez entrer un nombre correct !", 4, colors.DARK_RED)
    return bloc_placement


def settings_setup() -> Union[str, tuple[str, int, int]]:
    clear()
    window_width, window_height = get_window_size()
    draw_frame(get_window_width_center() - 15, get_window_height_center() - 15, 30, 4)
    draw_centered("Paramètrage de la partie", -13)
    size: str = ""
    shape: str = ""
    bloc_placement: str = ""
    while True:
        if references.do_size:
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            size = settings_set_size()

            if size in references.BACK_WORDS:
                main_menu()
                return "back"
            elif size in references.STOP_WORDS:
                exit_game()
            else:
                references.do_size = False

        if references.do_shape and (not references.do_size):
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            shape = settings_set_shape()
            if shape in references.BACK_WORDS:
                references.do_size = True
                continue
            elif shape in references.STOP_WORDS:
                exit_game()
            else:
                references.do_shape = False

        if references.do_placement and (not references.do_size and not references.do_shape):
            clear_area(0, get_window_height_center() - 10, window_width, window_height)
            bloc_placement = settings_set_placement_type()
            if bloc_placement in references.BACK_WORDS:
                references.do_shape = True
                continue
            elif bloc_placement in references.STOP_WORDS:
                exit_game()
            else:
                references.do_placement = False

        if not references.do_size and not references.do_shape and not references.do_placement:
            return references.GRID_TYPES[int(shape) - 1], int(size), int(bloc_placement)


def rules() -> None:
    clear()
    x, y = draw_frame(1, 1, get_window_size()[0] - 1, get_window_size()[1] - 1)
    draw("- Tout d’abord, l’utilisateur va devoir choisir entre charger une ancienne partie et en créer une nouvelle.",
         x + 1, y + 1)
    draw("- Ensuite, l’utilisateur devra choisir la dimension du plateau qu’il souhaite (entre 21 et 26).", x + 1,
         y + 3)
    draw("- Il devra par la suite choisir entre trois formes : le cercle, le losange et le triangle (1,2,3).", x + 1,
         y + 5)
    draw(
        "- Puis le jeu proposera deux issues à l’utilisateur soit d’avoir uniquement 3 blocs sélectionnés aléatoirement ou",
        x + 1, y + 7)
    draw(
        "d’afficher à chaque tour de jeu l’ensemble des blocs disponibles et l’utilisateur en sélectionne un (1 ou 2).",
        x + 1, y + 8)
    draw(
        "- Enfin, un plateau de jeu sera généré sur lequel l’utilisateur devra placer les blocs de tel sorte à remplir",
        x + 1, y + 10)
    draw(
        "les lignes et les colonnes. Chaque fois qu’une ligne ou qu’une colonne est pleine, elle se vide et donne au joueur",
        x + 1, y + 11)
    draw("un certain nombre de points. L’utilisateur dispose de 3 tentatives pour rentrer des coordonnées convenable.",
         x + 1, y + 12)
    draw("Une fois ces 3 tentatives dépassées le jeu s’arrête et il nous affiche un « Game over »", x + 1, y + 13)

    draw("- À tout moment dans les menus l’utilisateur peut entrer des mots clés comme « back » ou « retour »", x + 1,
         y + 15)
    draw("pour revenir à l’ancienne page de configuration. À tout moment lors de la partie, le joueur peut utiliser",
         x + 1, y + 16)
    draw("des mots clés comme « menu » pour accéder au menu permettant de reconsulter les règles ou sauvegarder.",
         x + 1, y + 17)
    draw(
        "N’importe quand, aussi bien dans les menus que pendant la partie l’utilisateur pourra utiliser des mots comme",
        x + 1, y + 18)
    draw("« stop » ou « arrêt » pour mettre fin à la partie.", x + 1, y + 19)
    draw_centered("ATTENTION", -get_window_height_center() + y + 22, colors.DARK_RED)
    draw_centered(
        "En cas d’utilisation de la commande « stop » la partie ne sera pas sauvegardée sauf si déjà fait au préalable.",
        -get_window_height_center() + y + 23, colors.DARK_RED)
    set_cursor(get_window_width_center(), 27)
    input()
