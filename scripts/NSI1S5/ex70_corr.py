def occurences(v, t):
    """
    renvoie le nombre d'occurence de la valeur 'v' dans le tableau 't'
    v: entier
    t: tableau non vide
    """
    # Supprimer 'pass' et compléter
    compteur = 0
    for i in range(len(t)):
        if t[i] == v:
            compteur = compteur + 1
    return compteur