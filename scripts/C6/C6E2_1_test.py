# TESTS
l1 = ListeChainee()
l1.insert(5)
l1.insert(3)
l1.insert(1)
l1.insert(10)
l1.insert(7)

assert chercher(7, l1) == 0
assert chercher(5, l1) == 4
assert chercher(100, l1) == None