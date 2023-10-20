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
        """ Affiche les éléments d'une liste chainée"""
        
        liste = self
        elements = []
        while not liste.est_vide():
            elements.append(str(liste.tete()))
            liste = liste.queue()
        return '[' + ','.join(elements) + ']'

def concatener(lst1, lst2):
    """ Renvoie une nouvelle liste chaînée issue de la concaténation de lst1 et lst2, c-a-d
    formée des éléments de l1 puis de l2;
    lst1, lst2: listes chaînées non vides
    """
    assert not lst1.est_vide() and not lst2.est_vide(), "Erreur: liste vide"
    
    # Création d'une liste vide et d'une référence sur le dernier élément de cette liste
    lst3 = ListeChainee()
    lst3.head = Cell(lst1.tete(), None)
    cellule_courante = lst3.head
    # Nécessité de réajuster lst1, sinon on risque de copier deux fois son 1er élément !!
    lst1.head = lst1.head.suiv
    
    for liste in (lst1, lst2):
        while not liste.est_vide():
            x = liste.tete()
            cellule_courante.suiv = Cell(x, None)
            cellule_courante = cellule_courante.suiv
            liste = liste.queue()
    
    return lst3


def list_insert(x, lst):
    if lst.est_vide():
        l = ListeChainee()
        l.insert(x)
        return l
    elif x < lst.tete():
        l = ListeChainee()
        l.insert(x)
        return concatener(l, lst)
    else:
        l = ListeChainee()
        l.insert(lst.tete())
        return concatener(l, list_insert(x, lst.queue()))