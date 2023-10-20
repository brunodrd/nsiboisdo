p = Pile()
p.empiler(10)
p.empiler(5)
p.empiler(1)
assert p.depiler() == 1
assert p.depiler() == 5
assert p.depiler() == 10