from typing import Optional, Dict, List, Union

GAME_TYPES = ["NEW", "LOADED"]
GRID_TYPES = ["cercle", "losange", "triangle"]
settings = {"shape": "", "size": 0, "bloc_placement": 0}
grid = {"width": 0, "height": 0, "matrice": None}
STOP_WORDS = ["stop", "arrêt", "arret"]
MENU_WORDS = ["menu", "menus"]
BACK_WORDS = ["back", "retour"]
log_path = ""
game_letters: Optional[List[str]] = None
common_liste: List[Dict[str, Union[str, List[List[str]]]]] = []
cercle_liste: List[Dict[str, Union[str, List[List[str]]]]] = []
losange_liste: List[Dict[str, Union[str, List[List[str]]]]] = []
triangle_liste: List[Dict[str, Union[str, List[List[str]]]]] = []
blocs_liste: List[Dict[str, Union[str, List[List[str]]]]] = []
score = 0
console_x = 0
console_y = 0

try_pos = 0

do_size: bool = True
do_shape: bool = True
do_placement: bool = True
