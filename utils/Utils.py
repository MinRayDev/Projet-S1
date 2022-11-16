import random
from utils import References


def is_correct_number(number, minvalue, maxvalue) -> bool:
    return number.isnumeric() and (minvalue <= int(number) <= maxvalue)


def select_blocs() -> list[dict[str, str | list[list[str]]]]:
    liste_to_return = []
    if References.settings["bloc_placement"] == 1:
        for liste in References.blocs_liste:
            liste_to_return += liste
    elif References.settings["bloc_placement"] == 2:
        temp_liste = []
        for liste in References.blocs_liste:
            temp_liste += liste
        for i in range(3):
            while True:
                choice = random.choice(temp_liste)
                if choice not in liste_to_return:
                    liste_to_return.append(random.choice(temp_liste))
                    break
    return liste_to_return
