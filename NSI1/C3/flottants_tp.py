"""Exercices 7 à 11 – Nombres à virgule et flottants.

Règle du jeu : dans valeur_binaire, n'utilisez pas int(chaine, 2).
Exécutez le fichier pour lancer les tests : décommentez chaque test
dans le bloc final quand la fonction correspondante est écrite.
"""

import math


# ============================================================ Fonction du cours
def bits_fraction(p, q, n):
    """Renvoie la chaîne des n premiers chiffres binaires
    après la virgule du nombre p / q, avec 0 <= p < q."""
    assert 0 <= p < q, "il faut 0 <= p < q"
    chiffres = ""
    for _ in range(n):
        p = 2 * p
        chiffres = chiffres + str(p // q)
        p = p % q
    return chiffres


# ============================================================ Exercice 7
def valeur_binaire(ecriture: str) -> float:
    """Renvoie la valeur du nombre dont `ecriture` est l'écriture binaire,
    avec une virgule éventuelle.

    Précondition : `ecriture` ne contient que des '0', des '1'
    et au plus une virgule.
    >>> valeur_binaire("101,1101")
    5.8125
    """
    # 1. Séparer la partie entière et la partie fractionnaire
    # 2. Calculer la valeur de la partie entière
    # 3. Ajouter les chiffres après la virgule, de poids 0.5, 0.25, 0.125…
    # À COMPLÉTER
    ...


# ============================================================ Exercice 8
def boucle_protegee():
    """Version protégée de la boucle de l'énoncé : 15 tours au plus."""
    x = 0
    nb_tours = 0
    while x != 1 and nb_tours < 15:
        x = x + 0.1
        nb_tours = nb_tours + 1
        print(nb_tours, x)


def boucle_corrigee():
    """Affiche 0,1 ; 0,2 ; … ; 1, puis s'arrête."""
    # À COMPLÉTER (exercice 8, question 3)
    ...


# ============================================================ Exercice 9
def presque_egal(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """Renvoie True si l'écart entre a et b est strictement inférieur
    à tolerance.

    >>> presque_egal(0.1 + 0.2, 0.3)
    True
    """
    # À COMPLÉTER
    ...


# ============================================================ Exercice 10
def ecriture_finie(p: int, q: int) -> bool:
    """Renvoie True si p / q a une écriture binaire finie.

    Précondition : p et q entiers, q > 0.
    >>> ecriture_finie(3, 8)
    True
    >>> ecriture_finie(1, 10)
    False
    """
    # À COMPLÉTER
    ...


# ============================================================ Exercice 11
def total_euros(n: int) -> float:
    """Additionne n fois un prix de 0,10 €, en euros (flottants)."""
    total = 0
    for _ in range(n):
        total = total + 0.1
    return total


def total_centimes(n: int) -> int:
    """Additionne n fois un prix de 0,10 €, en centimes (entiers)."""
    # À COMPLÉTER
    ...


# ============================================================ Tests
def test_valeur_binaire():
    assert valeur_binaire("101,1101") == 5.8125
    assert valeur_binaire("11,01") == 3.25
    assert valeur_binaire("110") == 6
    assert valeur_binaire("0,01") == 0.25
    # À COMPLÉTER : ajouter les nombres de l'exercice 1


def test_presque_egal():
    assert presque_egal(0.1 + 0.2, 0.3)
    assert not presque_egal(0.3, 0.31)
    assert presque_egal(1, 1.0005, 0.001)


def test_ecriture_finie():
    assert ecriture_finie(3, 8)
    assert not ecriture_finie(1, 10)
    # À COMPLÉTER : ajouter les nombres de l'exercice 4


if __name__ == "__main__":
    # test_valeur_binaire(); print("valeur_binaire : OK")
    # test_presque_egal(); print("presque_egal : OK")
    # test_ecriture_finie(); print("ecriture_finie : OK")
    pass
