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

# Fonction 'identiques'
# À compléter

def identiques(lst1, lst2):
    """
    Renvoie True si lst1 et lst2 sont identiques, False sinon.
    """
    # 1) On parcours les 2 listes en même temps
    while not lst1.est_vide() and not lst2.est_vide():
        if lst1.tete() != lst2.tete():
            return False
        # Les éléments sont identiques, on avance jusqu'à la prochaine cellule
        lst1 = lst1.queue()
        lst2 = lst2.queue(
    
    # 2) On a quitté la boucle: les éléments sont jusqu'ici identiques, mais
    # au moins une des 2 listes est vide!
    if lst1.est_vide():
        # On aura identité uniquement si lst2 est aussi vide!
        return lst2.est_vide()
    else:
        # Cas trivial: ici lst2 est vide mais pas lst1, donc ...!?
        return False