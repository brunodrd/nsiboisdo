l1 = ListeChainee()
l1.insert(5)
l1.insert(3)
l1.insert(1)
l2 = list_insert(-1, l1)
l1 = ListeChainee()
l1.insert(5)
l1.insert(3)
l1.insert(1)
l3 = list_insert(6, l1)
l1 = ListeChainee()
l1.insert(5)
l1.insert(3)
l1.insert(1)
l4 = list_insert(4, l1)
assert l2.affiche() == '[-1,1,3,5]'
assert l3.affiche() == '[1,3,5,6]'
assert l4.affiche() == '[1,3,4,5]'
