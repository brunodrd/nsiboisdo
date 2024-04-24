from math import inf

def meilleur_score_rec_memo(seq1, seq2):
    """
    Prend en paramètres deux chaines de caractères seq1 et seq2
    Renvoie le meilleur score d'alignement
    """
    
    def s(i, j):
        """Fonction récursive auxiliaire
        Calcule et renvoie score[i][j]
        """
        if score[i][j] == -inf:     
            # cas de base
            if i == 0:
                if j == 0:
                    score[i][j] = ...
                else:
                    score[i][j] = ...
            elif j == 0:
                 score[i][j] = ...
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
                    score[i][j] = ...
                # sous-cas où les derniers caractères sont différents
                else:
                    score[i][j] = ...
        return score[i][j]
    
    
    n = len(seq1)
    m = len(seq2)
    # tableau de mémoisation
    # score[i][j] est le meilleur score d'alignement de seq1[:i] et seq2[:j]
    score = [[-inf for j in range(m + 1)] for i in range(n + 1)]
    return s(n, m)

def test_meilleur_score_rec_memo():
    assert meilleur_score_rec_memo('AGTACG', 'ACATAG') == 1
    assert meilleur_score_rec_memo('GTTAACC', 'CGTAAC') == 2
    assert meilleur_score_rec_memo('GTAGTAAACGTTCACC', 'CGGTCAGTAAC') == -1
    print("tests réussis")
    
test_meilleur_score_rec_memo()