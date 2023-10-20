class Cell:
    """ Une classe pour décrire une cellule d'une liste chainée"""
    
    def __init__(self, v, s):
        self.val = v
        self.suiv = s

class ListeChainee:
    def __init__(self):
        """Initialise une liste vide."""
        self.head = None
    
    def est_vide(self):
        return self.head is None
    
    def insert(self, element):
        """ Construit une liste chaînée en insérant 'element' en tete"""
        self.head = Cell(element, self.head)
        
    def tete(self):
        """Renvoie le contenu de la premiere cellule"""
        
        assert self.head  is not None , "tete : erreur liste vide"
        return self.head.val
    
    def queue(self):
        """Renvoie une liste chaînée correspondant à la queue de la liste"""
        assert self.head  is not None , "queue : erreur liste vide"
        
        reste = ListeChainee()
        reste.head = self.head.suiv
        return reste
    
# Recherche séquentielle
# 1) Récursive

def recherche_aux(x, lst, i):
    """ 
    Fonction auxilliaire récursive qui recherche 'x' dans 'lst'
    à partir d'une position 'i';
    x: valeur à rechercher
    lst: liste chainée
    i: index où se trouve éventuellement x
    """
    if lst.est_vide():
        return None
    elif x == lst.tete():
        return ...
    else:
        return recherche_aux(..., ..., ...)
    
def chercher(x, lst):
    return recherche_aux(x, lst, 0)
