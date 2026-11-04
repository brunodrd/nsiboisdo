"""Entiers relatifs et complément à 2 – corrigé des exercices Python."""


def code_c2(x: int, n: int) -> str:
    """Renvoie le code en complément à 2 de l'entier relatif x sur n bits.

    Préconditions : n >= 1 et -2**(n-1) <= x <= 2**(n-1) - 1.
    >>> code_c2(-107, 8)
    '10010101'
    """
    assert n >= 1
    assert -2 ** (n - 1) <= x <= 2 ** (n - 1) - 1, "x non représentable sur n bits"
    if x < 0:
        x = 2 ** n + x          # 2**n - |x|
    code = ""
    for _ in range(n):          # exactement n bits, zéros de tête compris
        code = str(x % 2) + code
        x = x // 2
    return code


def valeur_c2(code: str) -> int:
    """Renvoie l'entier relatif dont `code` est le code en complément à 2.

    Précondition : `code` est une chaîne non vide de '0' et de '1'.
    >>> valeur_c2("10010101")
    -107
    """
    assert len(code) > 0
    n = len(code)
    v = 0
    for c in code:
        assert c in "01"
        v = 2 * v + int(c)
    if code[0] == "1":          # bit de poids fort à 1 : entier négatif
        v = v - 2 ** n
    return v


# ---- Fonctions de la ressource Eduscol (sept. 2019), recopiées à l'identique
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


def addition(code_a: str, code_b: str) -> str:
    """Additionne deux codes de même longueur n comme un additionneur à n bits
    et renvoie les n bits du résultat (la retenue sortante n'en fait pas partie)."""
    assert len(code_a) == len(code_b)
    n = len(code_a)
    s = (int(code_a, 2) + int(code_b, 2)) % 2 ** n
    return format(s, f"0{n}b")


def astuce(code: str) -> str:
    """Défi : depuis la droite, on recopie jusqu'au premier 1 inclus,
    puis on inverse tous les bits suivants."""
    i = len(code) - 1
    while i >= 0 and code[i] == "0":
        i = i - 1
    if i < 0:
        return code
    return cp1(code[:i]) + code[i:]


# ------------------------------------------------------------------ tests
def tests():
    assert code_c2(-107, 8) == "10010101"
    assert code_c2(107, 8) == "01101011"
    assert code_c2(-1, 8) == "11111111"
    assert code_c2(-128, 8) == "10000000"
    assert code_c2(0, 4) == "0000"
    for n in (1, 4, 8, 16):
        for x in range(-2 ** (n - 1), 2 ** (n - 1)):
            c = code_c2(x, n)
            assert len(c) == n
            assert valeur_c2(c) == x                         # aller-retour
            assert c == format(x % 2 ** n, f"0{n}b")         # Python : x % 2**n
    for k in range(256):
        c = format(k, "08b")
        assert cp2(cp2(c)) == c                              # involutive sur les codes
        assert cp2(c) == astuce(c)
        x = valeur_c2(c)
        if x != -128:
            assert valeur_c2(cp2(c)) == -x                   # cp2 donne l'opposé
    assert [c for c in (format(k, "08b") for k in range(256)) if cp2(c) == c] \
        == ["00000000", "10000000"]
    print("Tous les tests passent.")


if __name__ == "__main__":
    tests()
