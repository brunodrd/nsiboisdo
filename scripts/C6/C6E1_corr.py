def inserer(x, k, lst):
    """ Insère x à l'index k de la liste lst non vide.
    Ne renvoie rien: lst est modifié!
    """
    if k == 0: # il s'agit d'une insertion en tête
        c = Cell(tete(lst), queue(lst))
        lst.cle = x
        lst.suiv = c
    else:
        ## 1) Initialisation des variables utiles##        
        # compteur pour trouver l'index d'insertion
        pos = 1 
        
        # 2 pointeurs 'precedent' et 'cell_a_decaler'
        # ---+--------+---+-----+...
        #    | xk-1   | xk| xk+1|...
        # ---+--------+---+-----+...
        #      ^        ^ 
        #      |        |
        #cell. prec   cell. à décaler (pour l'insertion)
        #      
        precedent = lst
        cell_a_decaler = queue(lst)
        # Création de la cellule à insérer
        cell_a_inserer = Cell(x, None)
        
        # 2) Déplacement des pointeurs jusqu'à trouver l'index k
        while pos != k:
            cell_a_decaler = queue(cell_a_decaler)
            precedent = queue(precedent)
            pos += 1
        
        # On a trouvé la position, on assure maintenant le chaînage
        precedent.suiv = cell_a_inserer
        cell_a_inserer.suiv = cell_a_decaler