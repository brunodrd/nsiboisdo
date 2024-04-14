PIECES = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu(somme):
    """
    Renvoie une "liste" contenant les pieces à utiliser pour former
    somme.
    """
    liste_pieces = []
    i = len(PIECES) - 1
    while somme > 0:
        if somme >= PIECES[i]:
            somme = somme - PIECES[i]
            liste_pieces.append(PIECES[i])
        else:
            i = i - 1
    return liste_pieces

print(rendu(58))