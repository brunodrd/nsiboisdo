def puissance(x, n):
    """
    Calcule récursivement x à la puissance n
    """
    if n == 0:
        return 1
    else:
        return puissance(x, n-1) * x