import os
import sys

from typing import Tuple

from utils import ColorUtils


def draw(text: str, x: int, y: int, color: str = ColorUtils.WHITE) -> None:
    print(f"\033[{y};{x}H{color}{text}", end='', flush=True)


def draw_centered(text: str, y_dist: int = 0, color: str = ColorUtils.WHITE) -> None:
    window_width, window_height = get_window_size()
    draw(text, ((window_width // 2) - (len(text) // 2)), (window_height // 2) + y_dist, color)


def clear_area(x: int, y: int, width: int, height: int) -> None:
    for x_ in range(x, x + width):
        for y_ in range(y, y + height):
            draw(" ", x_, y_)


def set_cursor(x: int, y: int) -> None:
    draw("", x, y)


def get_window_size() -> Tuple[int, int]:
    return os.get_terminal_size()


def clear() -> None:
    if "win" in sys.platform:
        os.system("cls")
    else:
        clear_area(0, 0, os.get_terminal_size()[0], os.get_terminal_size()[1])


def get_window_width_center() -> int:
    return os.get_terminal_size()[0] // 2


def get_window_height_center() -> int:
    return os.get_terminal_size()[1] // 2


def draw_frame(x: int, y: int, width: int, height: int) -> Tuple[int, int]:
    draw("╔", x, y)
    for x_ in range(x + 1, x + width):
        draw("═", x_, y)
    draw("╗", x + width, y)
    for y_ in range(y + 1, y + height):
        draw("║", x, y_)
        draw("║", x + width, y_)
    draw("╚", x, y + height)
    for x_ in range(x + 1, x + width):
        draw("═", x_, y + height)
    draw("╝", x + width, y + height)
    return x + 1, y + 1
