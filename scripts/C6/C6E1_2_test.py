# TESTS
lst = Cell(3, Cell(7, Cell(9, Cell(0, None))))
supprimer(0, lst)
assert tete(lst) == 7
assert tete(queue(queue(lst))) == 0
supprimer(2, lst)
assert tete(queue(lst)) == 9