"""TP – Écrire un entier naturel en base 2, 10 et 16.

Complétez les fonctions marquées « À COMPLÉTER », puis exécutez le fichier :
les tests en bas de page doivent tous passer.
Règle du jeu : dans vos fonctions, n'utilisez NI bin(), NI hex(), NI int(chaine, base).
Ces fonctions natives servent uniquement à VÉRIFIER vos résultats dans les tests.
"""

CHIFFRES = "0123456789ABCDEF"


# ======================================================= Partie B (pour tous)
def binaire_vers_decimal(ecriture: str) -> int:
    """Renvoie l'entier naturel dont `ecriture` est l'écriture binaire.

    Précondition : `ecriture` est une chaîne non vide formée de '0' et de '1'.
    >>> binaire_vers_decimal("10011")
    19
    """
    # À COMPLÉTER
    ...


def decimal_vers_binaire(n: int) -> str:
    """Renvoie l'écriture binaire (sans préfixe) de l'entier naturel n.

    Précondition : n est un entier, n >= 0.
    >>> decimal_vers_binaire(25)
    '11001'
    """
    # À COMPLÉTER
    ...


# ================================================== Partie C (approfondissement)
def vers_base(n: int, b: int) -> str:
    """Renvoie l'écriture de l'entier naturel n en base b (2 <= b <= 16).

    >>> vers_base(480, 16)
    '1E0'
    """
    # À COMPLÉTER
    ...


def depuis_base(ecriture: str, b: int) -> int:
    """Renvoie l'entier naturel dont `ecriture` est l'écriture en base b
    (2 <= b <= 16, chiffres en majuscules).

    >>> depuis_base("1E0", 16)
    480
    """
    # À COMPLÉTER
    ...


def nb_bits(n: int) -> int:
    """Renvoie le nombre de bits de l'écriture binaire de l'entier naturel n.

    >>> nb_bits(1000)
    10
    """
    # À COMPLÉTER
    ...


# ============================================================== Défi
def binaire_vers_hexa(ecriture: str) -> str:
    """Convertit une écriture binaire en écriture hexadécimale par paquets de
    4 bits, SANS convertir le nombre entier en base 10.

    >>> binaire_vers_hexa("1101011111")
    '35F'
    """
    # À COMPLÉTER
    ...


# ============================================================== Tests
def test_binaire_vers_decimal():
    assert binaire_vers_decimal("10011") == 19
    assert binaire_vers_decimal("0") == 0
    assert binaire_vers_decimal("11111111") == 255
    for n in range(1000):                      # comparaison avec Python
        assert binaire_vers_decimal(bin(n)[2:]) == n


def test_decimal_vers_binaire():
    assert decimal_vers_binaire(25) == "11001"
    assert decimal_vers_binaire(0) == "0"
    for n in range(1000):
        assert decimal_vers_binaire(n) == bin(n)[2:]


def test_vers_base_depuis_base():
    assert vers_base(480, 16) == "1E0"
    assert depuis_base("213", 4) == 39
    # À COMPLÉTER : ajoutez au moins deux tests de votre choix
    for b in range(2, 17):
        for n in range(500):
            assert depuis_base(vers_base(n, b), b) == n   # aller-retour


def test_nb_bits():
    assert nb_bits(1000) == 10
    # À COMPLÉTER : comparez avec n.bit_length() pour n de 1 à 4999


def test_binaire_vers_hexa():
    assert binaire_vers_hexa("1101011111") == "35F"
    for n in range(1, 2000):
        assert binaire_vers_hexa(bin(n)[2:]) == hex(n)[2:].upper()


if __name__ == "__main__":
    test_binaire_vers_decimal()
    print("binaire_vers_decimal : OK")
    test_decimal_vers_binaire()
    print("decimal_vers_binaire : OK")
    # Décommentez au fur et à mesure :
    # test_vers_base_depuis_base(); print("vers_base / depuis_base : OK")
    # test_nb_bits(); print("nb_bits : OK")
    # test_binaire_vers_hexa(); print("binaire_vers_hexa : OK")
