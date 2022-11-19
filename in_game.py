from utils.terminal_utils import *
import os
from utils import References, shape_utils, Grid, Utils, ColorUtils, DebugUtils
from utils.file_utils import get_resources_path


def rules() -> None:
    clear()
    draw("🐮", get_window_width_center(), get_window_height_center())
    input()


def exit_game() -> None:
    clear()
    exit()


def stop(selected: bool = False) -> None:
    color = ColorUtils.DARK_RED
    if selected:
        color = ColorUtils.DARK_GREEN
    clear()
    draw_ascii_art(get_resources_path() + "\\end_screen.txt", get_window_width_center() - (55 // 2), get_window_height_center() - 8, color)
    draw_centered("Score: " + str(References.score))
    draw_centered("Press any key to continue...", 10)
    input()
    clear()
    exit()


def clear_game_console() -> None:
    clear_area(References.console_x, References.console_y, os.get_terminal_size()[0] - References.console_x,
               os.get_terminal_size()[1] - References.console_y)
