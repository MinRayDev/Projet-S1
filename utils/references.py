"""Fichier avec toutes les variables et constantes (hors couleurs) utilisées dans plusieurs modules.
@project Tetris
@author Gauthier
@author Marielle
"""
from typing import Dict, List, Optional, Tuple, Union
from utils import colors

# Paramètres de la partie et matrice de la grille de jeu.
settings: Dict[str, Union[str, int]] = {"shape": "", "size": 0, "bloc_placement": 0}
grid_matrice: Optional[List[List[str]]] = None

# Différents types de carte.
GRID_TYPES: List[str] = ["cercle", "losange", "triangle"]

# Différentes listes de mots clés à utiliser dans les menus ou en jeu.
STOP_WORDS: List[str] = ["stop", "arrêt", "arret"]
MENU_WORDS: List[str] = ["menu", "menus"]
BACK_WORDS: List[str] = ["back", "return", "retour", "précédent"]
SAVE_WORDS: List[str] = ["save", "saves", "sauvegarder"]
RULE_WORDS: List[str] = ["rule", "rules", "regle", "regles", "règle", "règles"]

# Lettres qui vont être utilisées pour les coordonnées de la grille.
game_letters: Optional[List[str]] = None

# Variables du score et du nombre d'essais pour placer un bloc déjà effectuées.
score: int = 0
try_pos: int = 0

# Variables permettant de savoir si la taille, la forme et le type de placement doivent encore être décidés.
do_size: bool = True
do_shape: bool = True
do_placement: bool = True

# Caractère pour dessiner les blocs (change en fonction de la couleur).
blocs_char: str = colors.WHITE + "■"

