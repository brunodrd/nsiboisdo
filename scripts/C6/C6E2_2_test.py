# TESTS
l1 = ListeChainee()
l1.insert(5)
l1.insert(3)
l1.insert(1)
l1.insert(10)
l1.insert(7)

assert chercher_iter(1, l1) == 2
assert chercher_iter(100, l1) == None