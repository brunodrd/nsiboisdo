"""Exercices 9 et 10 – Complément à 2 en Python.

Règle du jeu : dans code_c2 et valeur_c2, n'utilisez ni bin(), ni format(),
ni int(chaine, 2). Ces fonctions servent uniquement à VÉRIFIER, dans les tests.
"""


# ============================================================ Exercice 9
def code_c2(x: int, n: int) -> str:
    """Renvoie le code en complément à 2 de l'entier relatif x sur n bits.

    Préconditions : n >= 1 et -2**(n-1) <= x <= 2**(n-1) - 1.
    >>> code_c2(-107, 8)
    '10010101'
    """
    # 1. Vérifier les préconditions avec assert
    # 2. Si x est négatif, le remplacer par 2**n - |x|
    # 3. Écrire l'entier naturel obtenu en binaire sur EXACTEMENT n bits
    # À COMPLÉTER
    ...


def valeur_c2(code: str) -> int:
    """Renvoie l'entier relatif dont `code` est le code en complément à 2.

    Précondition : `code` est une chaîne non vide de '0' et de '1'.
    >>> valeur_c2("10010101")
    -107
    """
    # À COMPLÉTER
    ...


# ============================================================ Exercice 10
# Fonctions de la ressource Eduscol « Représentation des entiers relatifs »
def cp1(code):
    '''
    Renvoie le complément à 1 d'un code binaire
    Entrée : chaîne de caractères d'un code binaire
    Sortie : chaîne de caractères de même longueur du complément à 1
    '''
    code_cp1 = ""
    for c in code:
        if c == '0':
            code_cp1 += '1'
        else:
            code_cp1 += '0'
    return code_cp1


def cp2(code):
    '''
    Renvoie le complément à 2 d'un code binaire
    Entrée : chaîne de caractères d'un code binaire
    Sortie : chaîne de caractères de même longueur du complément à 2
    '''
    taille = len(code)
    code_cp1 = cp1(code)
    retenue = 1
    code_cp2 = ""
    j = taille
    while j > 0:
        j -= 1
        if retenue == 1:
            if code_cp1[j] == '0':
                code_cp2 = '1' + code_cp2
                retenue = 0
            else:
                code_cp2 = '0' + code_cp2
        else:
            code_cp2 = code_cp1[j] + code_cp2
    return code_cp2


# ============================================================ Tests
def test_code_c2():
    assert code_c2(-107, 8) == "10010101"
    assert code_c2(107, 8) == "01101011"
    assert code_c2(0, 4) == "0000"
    assert code_c2(-128, 8) == "10000000"
    for x in range(-128, 128):
        assert code_c2(x, 8) == format(x % 256, "08b")


def test_valeur_c2():
    assert valeur_c2("10010101") == -107
    assert valeur_c2("01111111") == 127
    # À COMPLÉTER : vérifier que valeur_c2(code_c2(x, 8)) == x pour x de -128 à 127


def test_cp2():
    # À COMPLÉTER (exercice 10, question 3)
    ...


if __name__ == "__main__":
    test_code_c2()
    print("code_c2 : OK")
    test_valeur_c2()
    print("valeur_c2 : OK")
    # test_cp2(); print("cp2 : OK")
