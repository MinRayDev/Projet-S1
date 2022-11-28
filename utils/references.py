from typing import Optional, Dict, List, Union

from utils import colors

GAME_TYPES = ["NEW", "LOADED"]
GRID_TYPES = ["cercle", "losange", "triangle"]
settings = {"shape": "", "size": 0, "bloc_placement": 0}
grid_matrice = None
STOP_WORDS = ["stop", "arrêt", "arret"]
MENU_WORDS = ["menu", "menus"]
BACK_WORDS = ["back", "retour"]
SAVE_WORDS = ["save", "saves"]
RULE_WORDS = ["rule", "rules"]
log_path = ""
game_letters: Optional[List[str]] = None

blocs_liste: List[Dict[str, Union[str, List[List[str]]]]] = []
score = 0
console_x = 0
console_y = 0

try_pos = 0

do_size: bool = True
do_shape: bool = True
do_placement: bool = True

blocs_char = colors.WHITE + "■"
