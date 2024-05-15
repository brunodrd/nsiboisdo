PIECES = [100, 50, 20, 10, 5, 2, 1] # système monnaitaire canonique


def rendu_aux(v, sol, i):
    """
        v (entier): somme à rendre;
        sol (liste python): la solution
        i (entier): index de la pièce à tester
        """
    # Cas de base
    if ...:
        return ...
    # Cas récursifs
    if ...:
        # On ne peut prendre la pièce, on essaie avec la suivante
        return rendu_aux(..., ..., ...)
    else:        
        ... # On prend la pièce...
        # ... et on résoud le pb avec v - PIECES[i]
        return ... 