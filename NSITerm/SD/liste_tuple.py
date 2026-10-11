"""Implémentation du TAD Liste par paires (cours, section 2.1)."""

def liste_vide():
    return None

def est_vide(L):
    return L is None

def cons(x, L):
    return (x, L)

def tete(L):
    assert not est_vide(L), "liste vide"
    return L[0]

def queue(L):
    assert not est_vide(L), "liste vide"
    return L[1]
