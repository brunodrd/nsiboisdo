# TESTS
def test_concatener():
    l1 = ListeChainee()
    l1.insert(5)
    l1.insert(3)
    l1.insert(1)

    l2 = ListeChainee()
    l2.insert(10)
    l2.insert(7)
    l2.insert(-5)

    l3 = concatener(l1, l2) # /!\ Attention à l'ordre, ici l2 au bout de l1
    result = ''
    while not l3.est_vide():
        result += str(l3.tete()) + ' '
        l3 = l3.queue()
    return result

assert test_concatener() == '1 3 5 -5 7 10 '
