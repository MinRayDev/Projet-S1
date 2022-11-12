def gen_losange(size):  # TODO: supporter les size pairs
    string_to_return = ""
    if size % 2 == 0:
        size -= 1
    for x in range(int(size / 2) + 1):
        string_to_return += "0" * (int(size / 2) - x)
        string_to_return += "1" * (2 * x + 1)
        string_to_return += "0" * (int(size / 2) - x)
        string_to_return += "\n"
    for x in range(int(size / 2) + 1 - 2, -1, -1):
        string_to_return += "0" * (int(size / 2) - x)
        string_to_return += "1" * (2 * x + 1)
        string_to_return += "0" * (int(size / 2) - x)
        string_to_return += "\n"
    return string_to_return


def gen_triangle(size):
    string_to_return = ""
    if size % 2 == 0:
        size -= 1
    for x in range(int(size / 2) + 1):
        string_to_return += "0" * (int(size / 2) - x)
        string_to_return += "1" * (2 * x + 1)
        string_to_return += "0" * (int(size / 2) - x)
        string_to_return += "\n"
    return string_to_return


def gen_cercle(size):
    string_to_return = ""
    for x in range(int(size / (3 * 2))):
        string_to_return += "0" * (int(size / (3 * 2)) - x)
        string_to_return += "1" * (size - (int(size / (3 * 2)) - x) * 2)
        string_to_return += "0" * (int(size / (3 * 2)) - x)
        string_to_return += "\n"
    for x in range(size - int(size/3)+1):
        if x <= size:
            string_to_return += "1" * size
            string_to_return += "\n"
        else:
            string_to_return += "1" * (size - int(size / 3) + size)
            string_to_return += "\n"
    for x in range(int(size/(3*2))):
        string_to_return += "0" * (x+1)
        string_to_return += "1" * (size - (x+1)*2)
        string_to_return += "0" * (x+1)
        string_to_return += "\n"
    return string_to_return
