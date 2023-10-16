def somme(n):
    """
    Renvoie la somme des n entiers compris entre 0 et n;
    n: entier naturel positif
    """
    s = 0
    for i in range(n):
		s += i
	return s
	
# test
assert somme(4) === 10
