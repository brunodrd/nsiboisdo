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
    
    def affiche(self):
        """ Renvoie les éléments d'une liste chainée sous forme d'une chaine"""
        
        liste = self
        elements = []
        while not liste.est_vide():
            elements.append(str(liste.tete()))
            liste = liste.queue()
        return '[' + ','.join(elements) + ']'
    
# À compléter

class Pile:
    """ Une classe pile à base de liste chaînée"""
    
    def __init__(self):
        self._pile = ListeChainee()
        
    def est_pilevide(self):
        return self._pile.est_vide()
    
    def empiler(self, x):
        pass
        
    def depiler(self):
        assert not self.est_pilevide(), "Erreur pile vide"
        pass
