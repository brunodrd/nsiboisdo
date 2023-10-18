l1 = ListeChainee()
l1.insert(5)
l1.insert(3)
l1.insert(1)

l2 = ListeChainee()
l2.insert(10)
l2.insert(7)
l = concat(l1, l2)
assert l.tete() == 7
assert l.queue().tete() == 10
assert l.queue().queue().tete() == 1
assert l.queue().queue().queue().tete() == 3
assert l.queue().queue().queue().queue().tete() == 5
