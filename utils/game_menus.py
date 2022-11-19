from in_game import *
from typing import List

from utils import References
from utils.terminal_utils import *
from utils.notifications import menu_notification
from utils.file_utils import get_resources_path, save_game


def menu(grid: List[List[str]]) -> None:
    clear()
    while True:
        draw_frame(get_window_width_center() - 9, 1, 18, 4)
        draw_centered("Game Menu", -16)

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
        if inputed == "save":
            clear_area(0, get_window_height_center() + 13, get_window_size()[0], get_window_size()[1])
            draw_centered("Entrez le nom du fichier:", 13)
            set_cursor(get_window_width_center(), get_window_height_center() + 15)
            inputed_file_name = input("")
            save_game(inputed_file_name, grid, References.score)
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
