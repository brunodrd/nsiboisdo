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


def croixcarre(c):
    """
    Renvoie une chaîne de caractères correspondant à un carré de coté c avec une 
    croix à l'intérieur.
    """
    assert c%2 == 1, "Erreur c impair"
    
    figure = ligne_XX(c) + '\n' # 1re ligne
    for i in range(c-2):
        if i != ((c-3) // 2):
            figure = figure + ligne_X__X((c+1) // 2) + ligne__X((c-1) // 2) + '\n'
        else:
            figure = figure + ligne_XX(c) + '\n' # ligne du milieu particulière: que des'X'
    figure = figure + ligne_XX(c) # dernière ligne
    return figure