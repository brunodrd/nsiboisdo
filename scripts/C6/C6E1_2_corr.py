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
    if k == 0:
        # Suppression en tête: on écrase la 1re clé avec la 2ème
        # puis on établit le chaînage de manière à supprimer la 2eme cellule.
        lst.cle = tete(queue(lst))
        lst.suiv = queue(queue(lst))
    else:
        # Initialisation de variables utiles
        # Compteur (index)
        pos = 1
        # Déclaration de 2 pointeurs autour de la cellule à supprimer
        # ----+--------+-------+-------+---
        # ... | xk-1   | xk    | xk+1  |...
        # ----+--------+-------+-------+---
        #       ^         ^       ^
        #       |         |       |
        #      prec.    à suppr.  suivant
        
        precedent = lst
        suivant = queue(queue(lst))
        
        # Déplacement des pointeurs autour de l'index k
        while pos != k:
            suivant = queue(suivant)
            precedent = queue(precedent)
            pos += 1
        
        # On a trouvé la cellule à supprimer, on établit
        # le chaînage de manière à la "court-circuiter"
        precedent.suiv = suivant