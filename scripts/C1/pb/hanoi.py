def hanoi(n, start, inter, stop):
    """
    Résoud récursivement le problème des tours de Hanoï.
    start, inter, stop: tours (type str)
    n: entier naturel
    """
    if n == 0: # Cas de base: il n'y a plus de disques à déplacer
        ...
    else: # Cas récursifs
        hanoi(..., ..., ..., ...) # Déplacement récursif de n-1 disques vers la tour intermédiaire
        print(start, "-->", stop)
        hanoi(..., ..., ..., ...) # Déplacer recursivement les n-1 disques de l'étape 1 vers sa destination