class Cellule:
    """Un maillon : une valeur et une référence vers le maillon suivant."""
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

def liste_vide():
    return None

def est_vide(L):
    return L is None

def cons(x, L):
    return Cellule(x, L)

def tete(L):
    assert not est_vide(L), "liste vide"
    return L.valeur

def queue(L):
    assert not est_vide(L), "liste vide"
    return L.suivant