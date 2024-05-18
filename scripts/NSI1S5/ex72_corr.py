def max_tab(t):
    """
    renvoie la valeur maximale rencontrée dans tableau d'entiers t
    t: tableau non vide
    """
    assert len(t) > 0, "Erreur: tableau vide"
    
    valeur_maxi = t[0] # initialisation
    for i in range(1, len(t)):
        if valeur_maxi < t[i]:
            valeur_maxi = t[i] # on a trouvé une valeur plus grande
    return valeur_maxi