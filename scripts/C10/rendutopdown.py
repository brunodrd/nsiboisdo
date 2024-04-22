def rendu(pieces, somme):
    """Version récursive avec mémoïsation"""
    memo = [None] * (somme + 1) # intialisation du tableau avec des None 
    return rendu_topdown(pieces, somme, memo)

def rendu_topdown(pieces, s, memo):
    if memo[s] is not None: # si on a déjà calculé le nombre optimal de pièces pour rendre la somme s
        return memo[s]      # on le renvoie directement
    elif s == 0:
        memo[s] = 0
        return 0
    else:
        nb_pieces = s     # nb_pieces = 1 + 1 + ... + 1 dans le pire des cas
        for p in pieces:
            if p <= s:   # inutile de tester une pièce dont la valeur dépasse la somme s à rendre
                nb_pieces = min(nb_pieces, 1 + rendu_topdown(pieces, s-p, memo))
        memo[s] = nb_pieces
        return nb_pieces