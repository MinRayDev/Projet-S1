import math


def add_space(string: str):
    string_to_return = ""
    for char in string:
        if char != "\n":
            string_to_return += char + " "
        else:
            string_to_return += char
    return string_to_return


def gen_losange(size: int) -> str:
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
    string_to_return: str = ""
    offset = 2 if size % 2 == 0 else 1
    for x in range(math.ceil(size / 2)):
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "1" * (2 * x + offset)
        string_to_return += "0" * (int(size / 2) - (x + offset - 1))
        string_to_return += "\n"
    return add_space(string_to_return)


def gen_cercle(size: int) -> str:
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
