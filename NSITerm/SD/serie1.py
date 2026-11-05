"""Série 1 : programmer avec l'interface du TAD Liste.

Mode d'emploi
-------------
1. Placer ce fichier dans le même dossier que votre module liste_tuple.py (exercice 2).
2. Pour chaque exercice, écrire le code des fonctions à la place de pass.
3. En bas du fichier, retirer le # devant la ligne de test de l'exercice, puis exécuter.
   Si rien ne s'affiche à part le message final, tous les tests actifs sont réussis.

Règle du jeu : on n'utilise que les cinq opérations importées ci-dessous.
Pas d'accès direct aux paires (L[0], L[1]), pas de len.
"""

from liste_tuple import liste_vide, est_vide, cons, tete, queue


# ---------- Exercice 3 : afficher une liste ----------

def vers_chaine(L):
    """Renvoie une chaîne décrivant la liste, par exemple "3 -> 5 -> 7 -> None"."""
    pass


def test_ex3():
    L = cons(3, cons(5, cons(7, liste_vide())))
    assert vers_chaine(L) == "3 -> 5 -> 7 -> None"
    assert vers_chaine(liste_vide()) == "None"
    print("✅ Validé !")


# ---------- Exercice 4 : somme des éléments ----------

def somme_rec(L):
    """Renvoie la somme des éléments de L (version récursive)."""
    pass


def somme_iter(L):
    """Renvoie la somme des éléments de L (version itérative)."""
    pass


def test_ex4():
    L = cons(3, cons(5, cons(7, liste_vide())))
    assert somme_rec(L) == somme_iter(L) == 15
    assert somme_rec(liste_vide()) == somme_iter(liste_vide()) == 0
    print("✅ Validé !")


# ---------- Exercice 5 : compter et chercher le maximum ----------

def nb_occurrences(L, x):
    """Renvoie le nombre d'éléments de L égaux à x."""
    pass


def maximum(L):
    """Renvoie le plus grand élément de L, liste non vide (vérifié par une assertion)."""
    pass


def test_ex5():
    M = cons(1, cons(4, cons(2, cons(4, liste_vide()))))
    assert nb_occurrences(M, 4) == 2
    assert nb_occurrences(M, 9) == 0
    assert maximum(M) == 4
    assert maximum(cons(-3, cons(-1, liste_vide()))) == -1
    print("✅ Validé !")


# ---------- Exercice 6 : conversions avec un tableau ----------

def depuis_tableau(T):
    """Renvoie la liste ayant les mêmes éléments que le tableau T, dans le même ordre."""
    pass


def vers_tableau(L):
    """Renvoie le tableau ayant les mêmes éléments que la liste L, dans le même ordre."""
    pass


def test_ex6():
    assert vers_tableau(depuis_tableau([1, 2, 3])) == [1, 2, 3]
    assert vers_tableau(depuis_tableau([])) == []
    print("✅ Validé !")


# ---------- Exercice 7 : changer d'implémentation ----------
# Pas de nouvelle fonction : suivre l'énoncé et modifier la ligne d'import en haut du fichier.


# ========== Pour aller plus loin ==========

# ---------- Exercice 8 : remplacer une valeur ----------

def remplacer(L, a, b):
    """Renvoie une nouvelle liste où chaque élément égal à a est remplacé par b."""
    pass


def test_ex8():
    L = depuis_tableau([3, 5, 3])
    assert vers_tableau(remplacer(L, 3, 9)) == [9, 5, 9]
    assert vers_tableau(remplacer(L, 7, 9)) == [3, 5, 3]
    assert vers_tableau(remplacer(liste_vide(), 3, 9)) == []
    assert vers_tableau(L) == [3, 5, 3]
    print("✅ Validé !")


# ---------- Exercice 9 : supprimer l'élément d'indice k ----------

def supprimer(L, k):
    """Renvoie une nouvelle liste privée de l'élément d'indice k."""
    assert not est_vide(L), "indice hors limites"
    if k == 0:
        return ...
    return cons(..., supprimer(..., ...))


def test_ex9():
    N = depuis_tableau([0, 1, 2, 3, 4])
    assert vers_tableau(supprimer(N, 0)) == [1, 2, 3, 4]
    assert vers_tableau(supprimer(N, 2)) == [0, 1, 3, 4]
    assert vers_tableau(supprimer(N, 4)) == [0, 1, 2, 3]
    print("✅ Validé !")


# ---------- Exercice 10 : supprimer une valeur ----------

def supprimer_valeur(L, x):
    """Renvoie une nouvelle liste où la première occurrence de x a été supprimée."""
    pass


def test_ex10():
    M = depuis_tableau([1, 4, 2, 4])
    assert vers_tableau(supprimer_valeur(M, 4)) == [1, 2, 4]
    assert vers_tableau(supprimer_valeur(M, 9)) == [1, 4, 2, 4]
    print("✅ Validé !")


# ---------- Tests à activer au fur et à mesure ----------

# test_ex3()
# test_ex4()
# test_ex5()
# test_ex6()
# test_ex8()
# test_ex9()
# test_ex10()

print("✅ Fin du programme : tous les tests actifs sont réussis.")
