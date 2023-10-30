"""Fichier avec toutes les variables et constantes (hors couleurs) utilisées dans plusieurs modules.
@project Tetris
"""
from typing import Optional, NewType, Type
from utils import colors

# Type alias pour les listes et les matrices.
# BlockType: TypeAlias = list[list[str]]
BlockType: Type['BlockType'] = NewType("BlockType", list[list[str]])
GridType: Type['GridType'] = NewType("GridType", list[list[str]])
# GridType: TypeAlias = list[list[str]]

# Paramètres de la partie et matrice de la grille de jeu.
settings: dict[str, str | int] = {"shape": "", "size": 0, "bloc_placement": 0}
grid_matrice: Optional[GridType] = None

# Différents types de carte.
GRID_TYPES: list[str] = ["cercle", "losange", "triangle"]

# Différentes listes de mots clés à utiliser dans les menus ou en jeu.
STOP_WORDS: set[str] = {"stop", "arrêt", "arret"}
MENU_WORDS: set[str] = {"menu", "menus"}
BACK_WORDS: set[str] = {"back", "return", "retour", "précédent"}
SAVE_WORDS: set[str] = {"save", "saves", "sauvegarder"}
RULE_WORDS: set[str] = {"rule", "rules", "regle", "regles", "règle", "règles"}

# Lettres qui vont être utilisées pour les coordonnées de la grille.
game_letters: Optional[list[str]] = None

# Variables du score et du nombre d'essais pour placer un bloc déjà effectué.
score: int = 0
try_pos: int = 0

# Variables permettant de savoir si la taille, la forme et le type de placement doivent encore être décidés.
do_size: bool = True
do_shape: bool = True
do_placement: bool = True

# Caractère pour dessiner les blocs (change en fonction de la couleur).
blocs_char: str = colors.WHITE + "■"
