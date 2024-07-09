def tri_insertion(t):
    """
    Trie t par insertion. Renvoie un nouveau tableau
    """
    
    if len(t) == 0:
        return []
    else:
        return placer(t[0], tri_insertion(t[1:]))