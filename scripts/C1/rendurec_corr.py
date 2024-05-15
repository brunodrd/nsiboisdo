PIECES = [100, 50, 20, 10, 5, 2, 1] # système monnaitaire canonique


def rendu_aux(v, sol, i):
    """
        v (entier): somme à rendre;
        sol (liste python): la solution
        i (entier): index de la pièce à tester
        """
    # Cas de base
    if v == 0:
        return sol
    # Cas récursifs
    if v < PIECES[i]:
        # On ne peut prendre la pièce, on essaie avec la suivante
        return rendu_aux(v, sol, i+1)
    else:        
        sol.append(PIECES[i]) # On prend la pièce...
        # ... et on résoud le pb avec v - PIECES[i]
        return rendu_aux(v - PIECES[i], sol, i)