def inserer(x, k, l):
    """ Insère x à l'index k de la liste l non vide"""
    if k == 0:
        c = Cell(tete(l), queue(l))
        l.cle = x
        l.suiv = c
    else:
        pos = 1
        # Initialisation de 2 pointeurs et de la cellule à insérer
        # +---+---+---+...
        # | x0| x1| x2|...
        # +---+---+---+...
        #   ^   ^ 
        #   |   |
        #  av. à_décaler
        #      (pos)
        cell_avant = l
        cell_a_decaler = queue(l)
        cell_a_inserer = Cell(x, None)

        # Déplacement des pointeurs jusqu'à trouver l'index k
        while pos != k:
            cell_a_decaler = queue(cell_a_decaler)
            cell_avant = queue(cell_avant)
            pos += 1

        # On a trouvé la position, on assure maintenant le chaînage
        cell_avant.suiv = cell_a_inserer
        cell_a_inserer.suiv = cell_a_decaler
