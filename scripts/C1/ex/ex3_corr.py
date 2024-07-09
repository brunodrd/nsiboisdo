def binaire(n):
    """
    Calcule la décomposition de n en binaire et renvoie
    le résultat sous la forme d'une chaine de caractères.
    """
    if n == 0:
        return ''
    else:
        return binaire(n//2) + str(n%2)