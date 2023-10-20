l1 = ListeChainee()
l2 = ListeChainee()
l3 = ListeChainee()
l4 = ListeChainee()
    
l1.insert(5)
l1.insert(3)
l1.insert(1)
    
l3.insert(5)
l3.insert(3)
l3.insert(1)
    
assert identiques(l1, l3) is True
assert identiques(l1, l2) is False
assert identiques(l2, l4) is True
assert identiques(l2, l3) is False
