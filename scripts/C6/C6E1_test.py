lst = Cell(3, Cell(7, Cell(9, Cell(0, None))))
inserer(-1, 3, lst)

assert tete(lst) == 3
assert tete(queue(queue(queue(lst)))) == -1
inserer(1000, 0, lst)
assert tete(lst) == 1000