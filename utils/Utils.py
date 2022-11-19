import random
import string
from typing import List, Dict, Union
from utils import References


# TODO: impl la fonction
def actions_string(inputed_string: str, **kwargs):
    print(kwargs)
    for arg in kwargs:
        if isinstance(kwargs[arg], list):
            if inputed_string.lower() in kwargs[arg]:
                if str(arg + "_action") not in kwargs:
                    raise ValueError("Missing action parameter")
                return kwargs[str(arg + "_action")]()


def get_letters(letter_index: int) -> List[str]:
    return list(string.ascii_lowercase)[:letter_index]


def is_correct_number(number: str, min_value: int, max_value: int) -> bool:
    return number.isnumeric() and (min_value <= int(number) <= max_value)


def select_blocs() -> List[Dict[str, Union[str, List[List[str]]]]]:
    list_to_return: List[Dict[str, Union[str, List[List[str]]]]] = []
    if References.settings["bloc_placement"] == 1:
        for liste in References.blocs_liste:
            list_to_return += liste
    elif References.settings["bloc_placement"] == 2:
        temp_list: List[Dict[str, Union[str, List[List[str]]]]] = []
        for liste in References.blocs_liste:
            temp_list += liste
        for i in range(3):
            while True:
                choice = random.choice(temp_list)
                if choice not in list_to_return:
                    list_to_return.append(random.choice(temp_list))
                    break
    return list_to_return
