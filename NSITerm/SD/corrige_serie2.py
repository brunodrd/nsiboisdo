"""Corrigé de la série 2 : la liste modifiable en place (cours, section 2.3)."""


class Cellule:
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant


class Liste:
    """Liste chaînée modifiable en place."""

    # --- méthodes du cours ------------------------------------------------
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def ajouter_en_tete(self, x):
        self.tete = Cellule(x, self.tete)

    def premier(self):
        assert not self.est_vide(), "liste vide"
        return self.tete.valeur

    def __len__(self):
        n = 0
        c = self.tete
        while c is not None:
            n += 1
            c = c.suivant
        return n

    def __str__(self):
        morceaux = []
        c = self.tete
        while c is not None:
            morceaux.append(str(c.valeur))
            c = c.suivant
        return " -> ".join(morceaux + ["None"])

    def inserer(self, k, x):
        if k == 0:
            self.ajouter_en_tete(x)
            return
        c = self.tete
        for _ in range(k - 1):
            assert c is not None, "indice hors limites"
            c = c.suivant
        assert c is not None, "indice hors limites"
        c.suivant = Cellule(x, c.suivant)

    # --- Exercice 2 -------------------------------------------------------
    def lire(self, k):
        assert k >= 0, "indice hors limites"
        c = self.tete
        for _ in range(k):
            assert c is not None, "indice hors limites"
            c = c.suivant
        assert c is not None, "indice hors limites"
        return c.valeur

    # --- Exercice 4 -------------------------------------------------------
    def supprimer(self, k):
        assert k >= 0 and not self.est_vide(), "indice hors limites"
        if k == 0:
            self.tete = self.tete.suivant
            return
        c = self.tete
        for _ in range(k - 1):                  # cellule d'indice k - 1
            c = c.suivant
            assert c is not None, "indice hors limites"
        assert c.suivant is not None, "indice hors limites"
        c.suivant = c.suivant.suivant

    # --- Exercice 5 -------------------------------------------------------
    def dernier(self):
        assert not self.est_vide(), "liste vide"
        c = self.tete
        while c.suivant is not None:
            c = c.suivant
        return c.valeur

    def ajouter_en_fin(self, x):
        if self.est_vide():
            self.tete = Cellule(x, None)
            return
        c = self.tete
        while c.suivant is not None:
            c = c.suivant
        c.suivant = Cellule(x, None)

    # --- Exercice 6 -------------------------------------------------------
    def retirer_tous(self, x):
        while self.tete is not None and self.tete.valeur == x:
            self.tete = self.tete.suivant
        c = self.tete
        while c is not None and c.suivant is not None:
            if c.suivant.valeur == x:
                c.suivant = c.suivant.suivant   # on reste sur c
            else:
                c = c.suivant

    # --- Exercice 7 -------------------------------------------------------
    def concatener(self, autre):
        """Accroche les cellules de autre à la fin de self (sans copie)."""
        if self.est_vide():
            self.tete = autre.tete
            return
        c = self.tete
        while c.suivant is not None:
            c = c.suivant
        c.suivant = autre.tete


# --- Exercice 9 (pour aller plus loin) : une file en O(1) ----------------
class File:
    def __init__(self):
        self.tete = None
        self.fin = None

    def est_vide(self):
        return self.tete is None

    def enfiler(self, x):
        nouvelle = Cellule(x, None)
        if self.est_vide():
            self.tete = nouvelle
        else:
            self.fin.suivant = nouvelle
        self.fin = nouvelle

    def defiler(self):
        assert not self.est_vide(), "file vide"
        x = self.tete.valeur
        self.tete = self.tete.suivant
        if self.tete is None:
            self.fin = None
        return x


def depuis_tableau(T):
    L = Liste()
    for i in range(len(T) - 1, -1, -1):
        L.ajouter_en_tete(T[i])
    return L


def doit_echouer(f, *args):
    try:
        f(*args)
    except AssertionError:
        return
    raise RuntimeError("assertion attendue")


if __name__ == "__main__":
    # Exercice 1
    L = Liste()
    L.ajouter_en_tete(30)
    L.ajouter_en_tete(20)
    L.ajouter_en_tete(10)
    assert str(L) == "10 -> 20 -> 30 -> None" and len(L) == 3
    c = L.tete
    c = c.suivant
    assert c.valeur == 20 and c.suivant.suivant is None

    # Exercice 2
    assert L.lire(0) == 10 and L.lire(2) == 30
    doit_echouer(L.lire, 3)
    doit_echouer(L.lire, -1)

    # Exercice 3 (traces)
    M = depuis_tableau([1, 2, 3])
    M.inserer(0, 99)
    assert str(M) == "99 -> 1 -> 2 -> 3 -> None"
    M.inserer(2, 42)
    assert str(M) == "99 -> 1 -> 42 -> 2 -> 3 -> None"
    M.inserer(5, 7)
    assert str(M) == "99 -> 1 -> 42 -> 2 -> 3 -> 7 -> None"
    doit_echouer(M.inserer, 8, 0)

    # Exercice 4
    S = depuis_tableau([0, 1, 2, 3, 4])
    S.supprimer(0); assert str(S) == "1 -> 2 -> 3 -> 4 -> None"
    S.supprimer(1); assert str(S) == "1 -> 3 -> 4 -> None"
    S.supprimer(2); assert str(S) == "1 -> 3 -> None"
    doit_echouer(S.supprimer, 2)
    doit_echouer(Liste().supprimer, 0)

    # Exercice 5
    F = Liste()
    F.ajouter_en_fin(1); F.ajouter_en_fin(2)
    assert str(F) == "1 -> 2 -> None" and F.dernier() == 2
    doit_echouer(Liste().dernier)

    # Exercice 6
    R = depuis_tableau([4, 4, 1, 4, 2, 4, 4])
    R.retirer_tous(4)
    assert str(R) == "1 -> 2 -> None"
    R2 = depuis_tableau([4, 4]); R2.retirer_tous(4); assert R2.est_vide()

    # Exercice 7 : concaténation et effet de bord
    L1, L2 = depuis_tableau([1, 2]), depuis_tableau([3, 4])
    L1.concatener(L2)
    assert str(L1) == "1 -> 2 -> 3 -> 4 -> None"
    L2.inserer(1, 99)                       # modifie aussi L1 !
    assert str(L1) == "1 -> 2 -> 3 -> 99 -> 4 -> None"
    L2.ajouter_en_tete(0)                   # ne modifie pas L1
    assert str(L1) == "1 -> 2 -> 3 -> 99 -> 4 -> None"
    V = Liste(); V.concatener(depuis_tableau([5])); assert str(V) == "5 -> None"

    # Exercice 9
    f = File()
    for x in (1, 2, 3):
        f.enfiler(x)
    assert f.defiler() == 1 and f.defiler() == 2
    f.enfiler(4)
    assert f.defiler() == 3 and f.defiler() == 4 and f.est_vide()
    f.enfiler(5); assert f.defiler() == 5
    print("Série 2 : tous les tests passent")
