def est_trie(t, g, d):
    """
    t: tableau
    g,d: entiers naturels
    renvoie True si t est trié par ordre croissant entre les indices g et d (inclus),
    False sinon.
    """
    # par ordre croissant 
    return all(t[i+1] >= t[i] for i in range(g, d))

def fusion(t, g, m, d):
    """
    t: tableau
    g,m,d: entiers naturels
    ....
    """
    assert est_trie(t, g, m)
    assert est_trie(t, m+1, d)
    
    i, j = g, m + 1
    aux = t[:] # réalise une copie de t
    for k in range(g, d+1):
        if i > m:
            t[k] = aux[j]
            j += 1
        elif j > d:
            t[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            t[k] = aux[j]
            j += 1
        else:
            t[k] = aux[i]
            i += 1
    
    assert est_trie(t, g, d)

###########################################################################################""""""
def tri_aux(t, g, d):
    """Fonction d'assistance """
    if ...: # Cas de base, tableau à un élément
        return
    else: # cas récursif
        m = g + (d - g) // 2 # sensiblement la moitié du tableau
        ... # tri récursif de la partie gauche
        ... # tri récursif de la partie droite
        ... # fusion

def tri_fusion(t):
    tri_aux(...)