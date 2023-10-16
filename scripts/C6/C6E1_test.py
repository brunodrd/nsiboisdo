lst = Cell(3, Cell(7, Cell(9, None)))
inserer(-1, 0, lst)

assert tete(queue(lst)) == 3, "tete(queue(lst)) == 3"
assert tete(lst) == -1, "tete(lst) == -1"
