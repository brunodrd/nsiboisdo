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
        
def concat(l1, l2):
    """
    Renvoie la concaténation l1---l2, en modifiant l2 (l1 placé en
    tête de l2).
    """
    
    # À compléter
    if ...:
        return l2
    else:
        concat(l1.queue(), ...).insert(...)
        return l2
