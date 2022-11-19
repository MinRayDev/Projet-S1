from utils import References, ColorUtils
from utils.terminal_utils import *


def game_notification(text: str, color: str = ColorUtils.WHITE) -> None:
    x, y = draw_frame(4 + (References.grid["width"] * 2) + 40, 2, 45, 2)
    draw(text, x + 1, y, color)


def menu_notification(text: str, y_diff: int, color: str = ColorUtils.WHITE) -> None:
    draw_centered(text, y_diff, color)
    draw_frame(get_window_width_center() - (len(text) // 2) - 2, get_window_height_center() + y_diff - 1, len(text) + 4,
               2)


def alert(text: str) -> None:
    game_notification(text, ColorUtils.DARK_RED)


def warn(text: str) -> None:
    game_notification(text, ColorUtils.DARK_YELLOW)


def clear_notification() -> None:
    clear_area(4 + (References.grid["width"] * 2) + 5 + 30 + 5, 2, 46, 4)
