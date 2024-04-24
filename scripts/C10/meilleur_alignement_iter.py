def meilleur_alignement_iter(seq1, seq2):
    """
    Prend en paramètres deux chaines de caractères seq1 et seq2
    Renvoie un couple le score maximal d'alignement et un alignement
    le réalisant qui est une liste de deux chaînes de caractères
    """
    # ---------------------------------------------------- #
    # Calcul du score maximal par prog dynamique          #
    #  on remplit le tableau score du bas vers le haut     #
    #  on parcourt les sous-problèmes par index croissants #
    # ---------------------------------------------------- #
    n = len(seq1)
    m = len(seq2)
    # score[i][j] est le meilleur score d'alignement de seq1[:i] et seq2[:j]
    score = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        score[i][0] = -i
    for j in range(m + 1):
        score[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):            
            # premier sous-problème : alignement des derniers caractères des préfixes seq1[:i] et seq2[:j]
            s1 = ...
            # second sous-problème : le dernier caractère de seq1[:i]  est aligné avec un trou
            s2 =  ...
            # troisième sous-problème  : le dernier caractère de seq1[:j]  est aligné avec un trou
            s3 =  ...
            # formule de récurrence pour le calcul de score[i][j]
            # sous-cas où les derniers caractères sont identiques dans le premier sous-problème
            if seq1[i - 1] == seq2[j - 1]:
                score[i][j] = ...
            # sous-cas où les derniers caractères sont différents
            else:
                score[i][j] = ...
    # le score de Needle-Wunsch de seq1 et seq2 est la valeur de la dernière cas du tableau
    # index du sous-problème : i index de ligne et j index de colonne
    i, j = n, m
    s = score[i][j]
    # ----------------------------------------------- #
    # Reconstruction d'un alignement de score maximal #
    # On redescend du haut vers le bas                #
    # On parcourt les choix successifs  à rebours     #
    # Jusqu'à ce que i ou j soit nul (cas de base)    #
    # ----------------------------------------------- #
    
    # alignement[0] est un alignement optimal pour seq1
    # alignement[1] est un alignement optimal pour seq2
    alignement = ['', '']    
    while i != 0 and j != 0:
        s1 = score[i - 1][j - 1]
        s2 = score[i][j - 1]
        s3 =  score[i - 1][j]
        # à compléter
        ...
    # si i différent de 0 on aligne seq1[:i] avec i * '_' 
    if i != 0:
        alignement[0] = ...
        alignement[1] = ...
    # si j différent de 0 on aligne j * '_'  avec seq2[:j]
    if j != 0:
        alignement[0] = ...
        alignement[1] = ...
    return (score[n][m], alignement)
        

def test_meilleur_alignement_iter():
    assert meilleur_alignement_iter('GTTAACC', 'CGTAAC') == (2, ['_GTTAACC', 'CG_TAA_C'])
    assert meilleur_alignement_iter('AGTACG', 'ACATAG') == (1, ['A_GTACG', 'ACATA_G'])
    print("tests réussis")
    
