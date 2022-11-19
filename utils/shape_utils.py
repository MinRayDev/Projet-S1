import math


def add_space(string: str) -> str:
    """Add a space between all characters in string and return it.

    :param string: string to add spaces.
    :return: the string with spaces.

    """
    string_to_return: str = ""

    for char in string:
        string_to_return += char + " " if char != "\n" else char

    return string_to_return


def gen_losange(size: int) -> str:
    """Generate a string of a losange and return it.

    :param size: size of the losange.
    :return: the string of the losange.

    """
    string_to_return: str = ""
    offset = 2 if size % 2 == 0 else 1

    for x in range(math.ceil(size / 2)):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"

    for x in range(int(size / 2) + 1 - 2, -1, -1):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"

    return add_space(string_to_return)


def gen_triangle(size: int) -> str:
    """Generate a string of a triangle and return it.

    :param size: size of the triangle.
    :return: the string of the triangle.

    """
    string_to_return: str = ""
    offset = 2 if size % 2 == 0 else 1

    for x in range(math.ceil(size / 2)):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"

    return add_space(string_to_return)


def gen_circle(size: int) -> str:
    """Generate a string of a circle and return it.

    :param size: size of the circle.
    :return: the string of the circle.

    """
    string_to_return: str = ""

    for x in range(int(size / (3 * 2))):
        string_to_return += "0" * (int(size / (3 * 2)) - x)
        string_to_return += "1" * (size - (int(size / (3 * 2)) - x) * 2)
        string_to_return += "0" * (int(size / (3 * 2)) - x)
        string_to_return += "\n"

    for x in range(math.ceil(size - int(size / 3))):
        if x <= size:
            string_to_return += "1" * size
            string_to_return += "\n"
        else:
            string_to_return += "1" * (size - int(size / 3) + size)
            string_to_return += "\n"

    for x in range(int(size / (3 * 2))):
        string_to_return += "0" * (x + 1)
        string_to_return += "1" * (size - (x + 1) * 2)
        string_to_return += "0" * (x + 1)
        string_to_return += "\n"

    return add_space(string_to_return)
