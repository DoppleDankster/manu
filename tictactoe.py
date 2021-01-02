def nouveau_plateau():
    """
    permet de génerer un nouveau plateau de jeu
    """
    plateau = []
    for i in range(3):
        plateau.append([" ", " ", " "])
    return plateau


def affiche_plateau(plateau):
    """
    Permet de print le plateau en 2D
    """
    for ligne in plateau:  # pour chaque element dans la liste "pleateau"
        print(ligne)  # print cet element uniquement


def check_horizontal(ligne):
    """
    Return False si il y a des espaces
    Return X si X à gagné
    Return O si X à gagné
    """
    # un espace se trouve dans la liste
    if " " in ligne:
        print("ESPACE")
    elif "X" in ligne and "O" in ligne:
        print("NUL")
    elif "X" not in ligne:
        print("O")
    else:
        print("X")


def flip_plateau(plateau):
    """pivote un plateau de 90°+"""
    flipped = []
    for i in range(3):
        colonne = []
        for ligne in plateau:
            colonne.append(ligne[i])
        flipped.append(colonne)
    return flipped


def check_diag1(plateau):
    diag = []
    for i in range(3):
        diag.append(plateau[i][i])
    # do check


def check_diag2(plateau):
    diag = []
    for i in range(3):
        diag.append(plateau[i][2 - i])
    # do check
