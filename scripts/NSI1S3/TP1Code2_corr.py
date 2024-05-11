def convertir_sur_16_bits(n):
    """
    Renvoie la conversion binaire de n sur 16 bits
    """
    assert n < 2**16, "Erreur: n nécessite plus de 16 bits"
    
    result = dec2bin(n)
    k = 16 - len(result) # nb de zéros à ajouter
    for i in range(k):
        result = '0' + result
    return result    