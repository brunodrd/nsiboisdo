def liste_vide():
    return None

def cons(e, l):
    """ Construit une liste à partir d'un élément e et d'une liste l"""
    return (e, l)

def tete(l):
    """ Renvoie l'élément de tête de l"""
    assert l is not None, "tete: erreur liste vide"
    return l[0]

def queue(l):
    """ Renvoie une liste correspondant à la queue de l"""
    assert l is not None, "queue: erreur liste vide"
    return l[1]

def est_vide(l):
    return l is None

# TESTS
premiers = cons(2, cons(3, cons(5, cons(7, liste_vide()))))
print(tete(premiers))
print(queue(premiers))
print(est_vide(premiers))
