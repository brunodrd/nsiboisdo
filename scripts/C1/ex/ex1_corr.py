def fact(n):
    """
    Renvoie la factorielle de n (notée n!)
    n : entier naturel
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)