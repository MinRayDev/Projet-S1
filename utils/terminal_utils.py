import os
import sys
from typing import Tuple
from utils import ColorUtils


def draw(text: str, x: int, y: int, color: str = ColorUtils.WHITE) -> None:
    """Draw a text in the terminal.

    :param text: text to draw.
    :param x: x position to draw.
    :param y: y position to draw.
    :param color: (optional) color of the text.

    """
    print(f"\033[{y};{x}H{color}{text}", end='', flush=True)


def draw_centered(text: str, y_dist: int = 0, color: str = ColorUtils.WHITE) -> None:
    """Draw text relative to the center of the terminal.

    :param text: text to draw.
    :param y_dist: distance on y-axis from the heigh center of the terminal.
    :param color: (optional) color of the text.

    """
    window_width, window_height = get_window_size()
    draw(text, ((window_width // 2) - (len(text) // 2)), (window_height // 2) + y_dist, color)


def clear_area(x: int, y: int, width: int, height: int) -> None:
    """Clear all in an area.

    :param x: column index where the area starts.
    :param y: line index where the area starts.
    :param width: width of the area.
    :param height: height of the area.

    """

    for i in range(x, x + width):
        for j in range(y, y + height):
            draw(" ", i, j)


def set_cursor(x: int, y: int) -> None:
    """Set the cursor position at the given x,y coordinates.

    :param x: column index.
    :param y: line index.

    """
    draw("", x, y)


def get_window_size() -> Tuple[int, int]:
    """Get the size of the terminal.

    :return: the size of the terminal (columns, lines).
    :rtype: Tuple[int, int].

    """
    return os.get_terminal_size()


def clear() -> None:
    """Clear the terminal."""

    if "win" in sys.platform:
        # If user's os is windows the program use a command
        os.system("cls")
    else:
        # else we clear all the terminal by replacing characters with spaces
        clear_area(0, 0, os.get_terminal_size()[1], os.get_terminal_size()[0])


def get_window_width_center() -> int:
    """Get and return the center of the width of the window."""
    return os.get_terminal_size()[0] // 2


def get_window_height_center() -> int:
    """Get and return the center of the height of the window."""
    return os.get_terminal_size()[1] // 2


def draw_frame(x: int, y: int, width: int, height: int) -> Tuple[int, int]:
    """Draw a frame and return (x, y) coordinates.

    :param x: x coordinate to draw.
    :param y: y coordinate to draw.
    :param width: width of the frame.
    :param height: height of the frame.
    :return: coordinates of the inside of the frame (x, y).
    :rtype: tuple of (int, int).

    """
    draw("╔", x, y)
    draw("╗", x + width, y)
    draw("╚", x, y + height)
    draw("╝", x + width, y + height)

    for i in range(x + 1, x + width):
        draw("═", i, y)
        draw("═", i, y + height)

    for j in range(y + 1, y + height):
        draw("║", x, j)
        draw("║", x + width, j)

    return x + 1, y + 1


def draw_ascii_art(file_path: str, x: int, y: int, color: str = ColorUtils.WHITE) -> None:
    """Draw an ASCII art.

    :param file_path: Path to the file of the ASCII to draw
    :param x: x position to draw.
    :param y: y position to draw.
    :param color: (optional) color of the text.

    """

    for i, line in enumerate(open(file_path, "r").readlines()):
        draw(line.replace("\n", ""), x, y + i, color)
