class Cell:
    """ Une classe pour décrire une cellule (maillon) d'une liste chainée"""
    
    def __init__(self, v, s):
        self.cle = v
        self.suiv = s

def est_vide(l):
    return l is None

def tete(l):
    """ Renvoie l'élément de tête de l"""
    assert l is not None, "tete: erreur liste vide"
    return l.cle

def queue(l):
    """ Renvoie une liste correspondant à la queue de l"""
    assert not est_vide(l), "queue: erreur liste vide"
    return l.suiv


def supprimer(k, lst):
    """ 
    Supprime la cellule d'index k de la liste non vide lst.
    Ne renvoie rien: lst est modifié !
    """
    pass
