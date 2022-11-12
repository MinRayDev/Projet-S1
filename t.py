from utils import References, Grid, FileUtils

blocs = FileUtils.load_blocks()
References.common_liste = blocs["common"]
References.cercle_liste = blocs["cercle"]
References.losange_liste = blocs["losange"]
References.triangle_liste = blocs["triangle"]
References.grid_type = "losange"
References.blocs_liste = Grid.print_blocs("")
for block in References.blocs_liste:
    print(block)