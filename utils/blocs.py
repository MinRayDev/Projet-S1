import random
from typing import List, Dict, Union
from utils import references


def select_blocs() -> List[Dict[str, Union[str, List[List[str]]]]]:
    list_to_return: List[Dict[str, Union[str, List[List[str]]]]] = []
    if references.settings["bloc_placement"] == 1:
        for liste in references.blocs_liste:
            list_to_return += liste
    elif references.settings["bloc_placement"] == 2:
        temp_list: List[Dict[str, Union[str, List[List[str]]]]] = []
        for liste in references.blocs_liste:
            temp_list += liste
        for i in range(3):
            while True:
                choice = random.choice(temp_list)
                if choice not in list_to_return:
                    list_to_return.append(random.choice(temp_list))
                    break
    return list_to_return


def bloc_to_string(matrice: List[List[str]]) -> str:
    string_to_return = ""
    for line in matrice:
        for co in line:
            string_to_return += references.blocs_char + " " if co == "1" else "  "
        string_to_return += "\n"
    return string_to_return
