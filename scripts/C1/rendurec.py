PIECES = [100, 50, 20, 10, 5, 2, 1] # exemple de système monnétaire canonique


def rendu_aux(v, sol, i):
    """
        v (entier): somme à rendre;
        sol (liste python): la solution
        i (entier): index de la pièce à tester
        """
    # Cas de base: lorsque la valeur à rendred est nulle
    if ...:
        return ...
    # Cas récursifs: il faut distinguer 2 cas
    if ...:
        # On ne peut prendre la pièce, on essaie avec la suivante
        return rendu_aux(..., ..., ...)
    else:        
        ... # On prend la pièce...
        # ... et on résoud le pb avec v - PIECES[i]
        return ... 