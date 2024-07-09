def appartient(x, t):
    """
    Renvoie True ou False selon que x appartienne à t ou pas
    """
    if len(t) == 0:
        return False
    elif x == t[0]:
        return True
    else:
        return appartient(x, t[1:])        