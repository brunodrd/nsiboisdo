class Pile:
    """ Une classe pile à base de liste chaînée"""
    
    def __init__(self):
        self._pile = ListeChainee()
        
    def est_pilevide(self):
        return self._pile.est_vide()
    
    def empiler(self, x):
        self._pile.insert(x)
        
    def depiler(self):
        assert not self.est_pilevide(), "Erreur pile vide"
        
        val = self._pile.tete()
        self._pile = self._pile.queue()
        return val
        
    def sommet(self):
        assert not self.est_pilevide()
        return self._pile.tete()