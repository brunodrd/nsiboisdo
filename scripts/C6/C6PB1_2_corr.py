def concatener(lst1, lst2):
    """ Renvoie une nouvelle liste chaînée issue de la concaténation de l1 et l2, c-a-d
    formée des éléments de l2 puis de l1;
    l1, l2: listes chaînées non vides
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
