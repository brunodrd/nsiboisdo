def renverse(c):
    """
    Renvoie la chaine c renversée
    """
    if len(c) <= 1: # <=1 car on veut traiter le cas de la chaine vide
        return c
    else:
        # version utilisant les tranches
        return c[-1] + renverse(c[0:-1])