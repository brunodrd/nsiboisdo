"""Corrigé de la série 1 : programmer avec l'interface du TAD Liste.

Toutes les fonctions n'utilisent que l'interface : elles fonctionnent avec
liste_tuple comme avec liste_cellule (exercice 10).
Lancer : python3 corrige_serie1.py   ou   python3 corrige_serie1.py cellule
"""
import sys

if len(sys.argv) > 1 and sys.argv[1] == "cellule":
    from liste_cellule import liste_vide, est_vide, cons, tete, queue
else:
    from liste_tuple import liste_vide, est_vide, cons, tete, queue


# Exercice 3 -------------------------------------------------------------
def vers_chaine(L):
    morceaux = []
    while not est_vide(L):
        morceaux.append(str(tete(L)))
        L = queue(L)
    morceaux.append("None")
    return " -> ".join(morceaux)


# Exercice 4 -------------------------------------------------------------
def somme_rec(L):
    if est_vide(L):
        return 0
    return tete(L) + somme_rec(queue(L))

def somme_iter(L):
    s = 0
    while not est_vide(L):
        s += tete(L)
        L = queue(L)
    return s


# Exercice 5 -------------------------------------------------------------
def nb_occurrences(L, x):
    n = 0
    while not est_vide(L):
        if tete(L) == x:
            n += 1
        L = queue(L)
    return n

def maximum(L):
    assert not est_vide(L), "liste vide"
    m = tete(L)
    L = queue(L)
    while not est_vide(L):
        if tete(L) > m:
            m = tete(L)
        L = queue(L)
    return m


# Exercice 6 -------------------------------------------------------------
def depuis_tableau(T):
    L = liste_vide()
    for i in range(len(T) - 1, -1, -1):     # cons ajoute en tête : on part de la fin
        L = cons(T[i], L)
    return L

def vers_tableau(L):
    T = []
    while not est_vide(L):
        T.append(tete(L))
        L = queue(L)
    return T


# Exercice 7 -------------------------------------------------------------
def ajouter_en_fin(L, x):
    if est_vide(L):
        return cons(x, liste_vide())
    return cons(tete(L), ajouter_en_fin(queue(L), x))


# Exercice 8 -------------------------------------------------------------
def supprimer(L, k):
    assert k >= 0 and not est_vide(L), "indice hors limites"
    if k == 0:
        return queue(L)
    return cons(tete(L), supprimer(queue(L), k - 1))


# Exercice 9 -------------------------------------------------------------
def supprimer_valeur(L, x):
    if est_vide(L):
        return L
    if tete(L) == x:
        return queue(L)
    return cons(tete(L), supprimer_valeur(queue(L), x))


# Pour aller plus loin ---------------------------------------------------
def renverser(L):
    R = liste_vide()
    while not est_vide(L):
        R = cons(tete(L), R)
        L = queue(L)
    return R

def concatener(L1, L2):
    if est_vide(L1):
        return L2
    return cons(tete(L1), concatener(queue(L1), L2))


# Tests -----------------------------------------------------------------
if __name__ == "__main__":
    L = cons(3, cons(5, cons(7, liste_vide())))
    assert tete(L) == 3 and tete(queue(L)) == 5
    assert vers_chaine(L) == "3 -> 5 -> 7 -> None"
    assert vers_chaine(liste_vide()) == "None"

    assert somme_rec(L) == somme_iter(L) == 15
    assert somme_rec(liste_vide()) == somme_iter(liste_vide()) == 0

    M = depuis_tableau([1, 4, 2, 4])
    assert nb_occurrences(M, 4) == 2 and nb_occurrences(M, 9) == 0
    assert maximum(M) == 4 and maximum(depuis_tableau([-3, -1, -2])) == -1

    assert vers_tableau(depuis_tableau([1, 2, 3])) == [1, 2, 3]
    assert vers_tableau(depuis_tableau([])) == []

    assert vers_tableau(ajouter_en_fin(L, 9)) == [3, 5, 7, 9]
    assert vers_tableau(ajouter_en_fin(liste_vide(), 4)) == [4]
    assert vers_tableau(L) == [3, 5, 7]                     # L inchangée

    N = depuis_tableau([0, 1, 2, 3, 4])
    assert vers_tableau(supprimer(N, 0)) == [1, 2, 3, 4]
    assert vers_tableau(supprimer(N, 2)) == [0, 1, 3, 4]
    assert vers_tableau(supprimer(N, 4)) == [0, 1, 2, 3]
    assert queue(queue(supprimer(N, 2))) is queue(queue(queue(N)))   # partage
    for k in (5, -1):
        try:
            supprimer(N, k)
            raise RuntimeError("assertion attendue")
        except AssertionError:
            pass

    assert vers_tableau(supprimer_valeur(M, 4)) == [1, 2, 4]
    assert vers_tableau(supprimer_valeur(M, 9)) == [1, 4, 2, 4]

    assert vers_tableau(renverser(L)) == [7, 5, 3]
    A, B = depuis_tableau([1, 2]), depuis_tableau([3, 4])
    C = concatener(A, B)
    assert vers_tableau(C) == [1, 2, 3, 4] and queue(queue(C)) is B
    print("Série 1 : tous les tests passent")
