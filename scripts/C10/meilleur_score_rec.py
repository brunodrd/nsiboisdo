def meilleur_score_rec(seq1, seq2):
    """
    Prend en paramètres deux chaines de caractères seq1 et seq2
    Renvoie le meilleur score d'alignement
    """
    
    def s(i, j):
        """Fonction récursive auxiliaire
        Calcule et renvoie score[i][j]
        """
        if i == 0:
            if j == 0:
                return ...
            else:
                return  ...
        elif j == 0:
             return ...
        else:
            # premier sous-problème : alignement des derniers caractères des préfixes seq1[:i] et seq2[:j]
            s1 = ...
            # second sous-problème : le dernier caractère de seq1[:i]  est aligné avec un trou
            s2 =  ...
            # troisième sous-problème  : le dernier caractère de seq1[:j]  est aligné avec un trou
            s3 =  ...
            # formule de récurrence pour le calcul de score[i][j]
            # sous-cas où les derniers caractères sont identiques dans le premier sous-problème
            if seq1[i - 1] == seq2[j - 1]:
                return ...
            # sous-cas où les derniers caractères sont différents
            else:
                return  ...
    
    
    n = len(seq1)
    m = len(seq2)
    return s(n, m)

def test_meilleur_score_rec():
    assert meilleur_score_rec('AGTC', 'ACTG') == 0
    assert meilleur_score_rec('GTT', 'CGTT') == 2
    print("tests réussis")
    
#test_meilleur_score_rec()