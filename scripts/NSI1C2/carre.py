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

def carre(c):
    """
    Renvoie une chaîne de caractères correspondant à un carré de coté c
    """
    figure = ... + '\n' # 1re ligne
    for i in range(c-2):
        figure = ... + '\n'
    figure = ... # dernière ligne
    return figure