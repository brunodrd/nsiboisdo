def ligne_XX(n):
    """ Renvoie une ligne remplie de n caractères 'X X ...X X' """
    assert n >= 1
    return 'X ' * n

def ligne_X__X(n):
    """ Renvoie une ligne de n caractères 'X __ __ ....__ X' """
    assert n >= 3
    return 'X ' + '  ' * (n-2) + 'X '

def ligne__X(n):
    """ Renvoie une ligne de n caractères '__ __ ...__ X'"""
    assert n >= 2
    return '  '*(n-1) + 'X '

def diaggauche(c):
    """ Renvoie une chaîne correspondant à un carré et sa diagonale gauche
    c: entier naturel
    """
    figure = ligne_XX(c) + '\n' # ligne 0
    for i in range(..., ...): # lignes 1 à c-2 inclus
        figure = figure + ... + ... + '\n'
    figure = figure + ... # ligne c-1
    return figure