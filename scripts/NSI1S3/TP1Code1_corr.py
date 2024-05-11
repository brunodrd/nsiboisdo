def dec2bin(n):
    """
    Renvoie une chaîne correspondant à la représentation binaire de l'entier n.
    """
    result = ''
    quotient = n
    if quotient == 0:
        result = '0'
    else:
        while quotient != 0:
            result = str(quotient % 2) + result
            quotient = quotient // 2
    return result