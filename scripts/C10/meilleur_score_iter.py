def meilleur_score_iter(seq1, seq2):
    """
    Prend en paramètres deux chaines de caractères seq1 et seq2
    Renvoie le meilleur score d'alignement
    """
    n = len(seq1)
    m = len(seq2)
    # score[i][j] est le meilleur score d'alignement de seq1[:i] et seq2[:j]
    score = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        score[i][0] = ...
    for j in range(m + 1):
        score[0][j] = ...
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
    return score[n][m]

def test_meilleur_score_iter():
    assert meilleur_score_iter('AGTACG', 'ACATAG') == 1
    assert meilleur_score_iter('GTTAACC', 'CGTAAC') == 2
    print("tests réussis")