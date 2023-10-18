class Cell:
    """ Une classe pour décrire un maillon d'une liste chainée"""
    
    def __init__(self, v, s):
        self.val = v
        self.suiv = s

class ListeChainee:
    def __init__(self):
        """Initialise une liste chaînée vide."""
        self.head = None
    
    def est_vide(self):
        return self.head is None
    
    def insert(self, element):
        """ Construit une liste en insérant 'element' en tete"""
        self.head = Cell(element, self.head)
        
    def tete(self):
        """Renvoie le contenu de la premiere cellule"""
        
        assert self.head  is not None , "tete : erreur liste vide"
        return self.head.val
    
    def queue(self):
        """Renvoie une liste chaînée correpsondant à la queue de la liste"""
        
        assert self.head  is not None , "queue : erreur liste vide"
        reste = ListeChainee()
        reste.head = self.head.suiv
        return reste
    
def concat(l1, l2):
    """ renvoie la concaténation l2,l1, avec résultat dans l1"""
    if l2.est_vide():
        return l1
    else:
        concat(l1, l2.queue()).insert(l2.tete())
        return l1
