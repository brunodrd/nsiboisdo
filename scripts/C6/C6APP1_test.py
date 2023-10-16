# TESTS
premiers = cons(2, cons(3, cons(5, cons(7, liste_vide()))))
assert tete(premiers) == 2, "tete(premiers) == 2"
assert queue(premiers) == (3, (5, (7, None))), "queue(premiers) == (3, (5, (7, None)))"
assert est_vide(premiers) == False, "est_vide(premiers)"
