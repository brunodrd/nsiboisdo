def rendu_bottomup(pieces, somme):
    """
    Renvoie le nombre de pieces minimal 'nb_piece' nécessaire pour former 'somme'
    """
    nb_piece = [0] * (somme+1) # initialisation du cache
    for n in range(1, somme+1): # on effectue le calcul de tous les ss pb jusqu'à somme
        nb_piece[n] = n
        for p in pieces:
            if p <= n:
                nb_piece[n] = min(..., ...)
    return nb_piece[somme]