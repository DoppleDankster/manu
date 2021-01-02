# une fonction newboard() qui crée un plateau de jeu vide et le return
# hint : listes bidimensionnelles


def newboard():
    # méthode mongole de niveau 1 plato = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    plateau = []
    for i in range(3):
        plateau.append([" ", " ", " "])
    return plateau


def display_board(plateau):
    """
    Permet de print le plateau en 2D
    """
    for ligne in plateau:  # pour chaque element dans la liste "pleateau"
        print(ligne)  # print cet element uniquement


plateau = newboard()
plateau[1][1] = "X"
plateau[0][0] = "O"
display_board(plateau)
# une fonction test qui vérifie si la partie est terminée ou pas

# une fonction game() qui lance le jeu et qui return quand la partie est fini
# elle return soit "X" soit "O" soit "NUL" en fonction du gagnant