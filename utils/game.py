import os
from typing import List, Optional, Tuple

from utils.menus import rules
from utils.terminal import clear, draw_ascii_art, get_window_width_center, get_window_height_center, draw_centered, \
    draw, get_window_size, draw_frame, clear_game_console, set_cursor, clear_area
from utils import references, colors, grids, blocs, numbers
from utils.files import get_resources_path, save_game
from utils.notifications import alert, clear_notification, menu_notification


def stop(selected: bool = False) -> None:
    color = colors.DARK_RED
    if selected:
        color = colors.DARK_GREEN
    clear()
    draw_ascii_art(get_resources_path() + "\\end_screen.txt", get_window_width_center() - (55 // 2),
                   get_window_height_center() - 8, color)
    draw_centered("Score: " + str(references.score))
    draw_centered("Press any key to continue...", 10)
    input()
    clear()
    exit()


def print_grid(grid: List[List[str]]) -> None:
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


def print_blocs(blocs_to_draw) -> None:
    width = grids.get_size(references.grid_matrice)[0]
    bloc_line: int = 0
    last_x: int = 4 + (width * 2) + 5
    last_list_size: int = 0
    for i, block in enumerate(blocs_to_draw):
        max_x: int = 0
        t = 0
        if len(block["matrice"]) == 5:
            t = -1
        elif len(block["matrice"]) == 3:
            t = 1
        for j, cube_line in enumerate(blocs.bloc_to_string(block['matrice']).split("\n")):
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


def update_score(count: int) -> int:
    references.score += count
    return references.score


def draw_game(blocs_to_draw) -> None:
    width = grids.get_size(references.grid_matrice)[0]
    print_grid(references.grid_matrice)
    score_frame = draw_frame(4 + (width * 2) + 5, 2, 30, 2)
    draw(f"Score: {references.score}", score_frame[0], score_frame[1])
    print_blocs(blocs_to_draw)
    references.console_x, references.console_y = draw_frame(get_window_size()[0] - 16, get_window_size()[1] - 7, 17, 7)


def inputs(blocs_to_draw) -> Optional[Tuple[str, int, int]]:
    inputed_number = ""
    while not numbers.is_correct_number(inputed_number, 1, len(blocs_to_draw)):
        clear_game_console()
        draw("Choisissez une", references.console_x, references.console_y)
        draw("forme: ", references.console_x, references.console_y + 1)
        set_cursor(os.get_terminal_size()[0] - 8, os.get_terminal_size()[1] - 6 + 1)
        inputed_number = input()
        if inputed_number in references.STOP_WORDS:
            stop(True)
        elif inputed_number in references.MENU_WORDS:
            menu(references.grid_matrice)
            clear()
            return None
        if not numbers.is_correct_number(inputed_number, 1, len(blocs_to_draw)):
            clear_notification()
            alert("Veuillez entrer un nombre valide !")
    clear_notification()

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


def menu(grid: List[List[str]]) -> None:
    while True:
        clear()
        draw_frame(get_window_width_center() - 9, 1, 18, 4)
        draw_centered("Game Menu", -get_window_height_center()+3)

        draw_frame(get_window_width_center() // 2 - 18, get_window_height_center() - 9, 35, 20)
        for i, line in enumerate(
                open(get_resources_path() + "\\save_icon.txt", "r", encoding="utf-8").readlines()):
            draw(line.replace("\n", ""), get_window_width_center() // 2 - 15, get_window_height_center() - 7 + i)
        draw("1. Save", get_window_width_center() // 2 - len("1. Save") // 2, get_window_height_center() - 9 + 20 - 3)

        draw_frame(get_window_width_center() - 18, get_window_height_center() - 9, 35, 20)
        for i, line in enumerate(
                open(get_resources_path() + "\\rules_logo.txt", "r", encoding="utf-8").readlines()):
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
        if inputed.lower() in references.SAVE_WORDS or inputed == "1":
            clear_area(0, get_window_height_center() + 13, get_window_size()[0], get_window_size()[1])
            draw_centered("Entrez le nom du fichier:", 13)
            set_cursor(get_window_width_center(), get_window_height_center() + 15)
            inputed_file_name = input("")
            save_game(inputed_file_name, grid, references.score)
            clear()
        elif inputed.lower() in references.RULE_WORDS or inputed == "2":
            rules()
            clear()
        elif inputed.lower() in ["settings", "setting", "paramètres", "paramètre", "couleur", "couleurs", "color",
                                 "colors", "coulors", "coulor", "3"]:
            color_settings()
        elif inputed.lower() in references.STOP_WORDS or inputed == "4":
            stop(True)
        elif inputed.lower() in references.BACK_WORDS or inputed == "5":
            break
        else:
            menu_notification("Veuillez entrer une proposition valide", -12, colors.DARK_RED)
        set_cursor(0, get_window_size()[1])


def color_settings():
    clear()
    draw_frame(get_window_width_center() - 9, 1, 18, 4)
    draw_centered("Color Settings", -get_window_height_center() + 3)
    draw("■ Basic", 5, 15)
    draw(f"{colors.DARK_RED}■ {colors.WHITE}Red", 5, 16)
    draw(f"{colors.DARK_PURPLE}■ {colors.WHITE}Purple", 5, 17)
    draw(f"{colors.DARK_BLUE}■ {colors.WHITE}Blue", 5, 18)
    draw(f"{colors.DARK_GREEN}■ {colors.WHITE}Green", 5, 19)
    draw(f"{colors.DARK_YELLOW}■ {colors.WHITE}Yellow", 5, 20)
    color = ""
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


